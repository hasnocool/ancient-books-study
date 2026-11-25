#!/usr/bin/env python3
"""
Full Diplomatic Proofing — 1 Enoch (Charles 1893)
Fuzzy-match OCR segments to repository verses, with apparatus extraction.
"""

import re
import json
import csv
from pathlib import Path
from difflib import SequenceMatcher
from dataclasses import dataclass, asdict
from typing import Optional

# ─── Configuration ──────────────────────────────────────────────
OCR_DIR = Path("artifacts/1-enoch-1893/ocr")
REPO_DIR = Path("formatted_editions/books/book-of-enoch-charles-1893")
OUTPUT_DIR = Path("artifacts/1-enoch-1893/reports/diplomatic_proofing_full")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

REPO_FILES = [
    ("intro", None, "Introduction (pp.55-56)"),
    ("book-01-watchers-chapters-01-36.md", range(1, 37), "Book 1: Watchers (pp.57-104)"),
    ("book-02-parables-chapters-37-71.md", range(37, 72), "Book 2: Parables (pp.105-186)"),
    ("book-03-luminaries-chapters-72-82.md", range(72, 83), "Book 3: Luminaries (pp.187-218)"),
    ("book-04-visions-chapters-83-90.md", range(83, 91), "Book 4: Dream-Visions (pp.219-259)"),
    ("book-05-laws-of-enoch-chapters-91-105.md", range(91, 106), "Book 5: Laws (pp.265-308)"),
    ("book-06-deluge-chapters-106-108.md", range(106, 109), "Book 6: Deluge (pp.301-308)"),
]

# ─── Data Classes ──────────────────────────────────────────────
@dataclass
class Verse:
    chapter: int
    verse: int
    text: str
    is_interpolation: bool = False

@dataclass
class Discrepancy:
    page: int
    leaf: int
    repo_chapter: int
    repo_verse: int
    discrepancy_type: str
    charles_text: str
    repo_text: str
    similarity: float
    confidence: str
    notes: str
    verified: bool = False
    reviewer: str = ""

@dataclass
class ApparatusEntry:
    page: int
    lemma: str
    sigla: list[str]
    witnesses: str
    charles_note: str
    repo_has: bool = False

# ─── Core Functions ────────────────────────────────────────────
def load_repo_verses() -> dict[int, dict[int, Verse]]:
    """Parse all repository files into chapter→verse dict."""
    chapters = {}
    for fname, ch_range, _ in REPO_FILES:
        fpath = REPO_DIR / fname
        if not fpath.exists():
            continue
        text = fpath.read_text(encoding='utf-8')
        current_chapter = None
        current_verse = None
        buffer = []
        
        for line in text.split('\n'):
            m = re.match(r'^## Chapter (\d+)', line)
            if m:
                if current_chapter and buffer:
                    chapters.setdefault(current_chapter, {})[current_verse] = Verse(
                        current_chapter, current_verse, '\n'.join(buffer).strip(),
                        is_interpolation="(interpolation)" in line.lower()
                    )
                current_chapter = int(m.group(1))
                chapters[current_chapter] = {}
                current_verse = None
                buffer = []
                continue
            
            m = re.match(r'^\*\*\[Verse\s+(\d+)', line)
            if m:
                if current_verse and buffer:
                    chapters.setdefault(current_chapter, {})[current_verse] = Verse(
                        current_chapter, current_verse, '\n'.join(buffer).strip(),
                        is_interpolation="(interpolation)" in line.lower()
                    )
                current_verse = int(m.group(1))
                verse_text = re.sub(r'^\*\*\[Verse\s+\d+[^\]]*\]\*\*\s*', '', line)
                buffer = [verse_text] if verse_text.strip() else []
                continue
            
            m = re.match(r'^\[\s*Verse\s+(\d+)', line)
            if m:
                if current_verse and buffer:
                    chapters.setdefault(current_chapter, {})[current_verse] = Verse(
                        current_chapter, current_verse, '\n'.join(buffer).strip(),
                        is_interpolation="(interpolation)" in line.lower()
                    )
                current_verse = int(m.group(1))
                verse_text = re.sub(r'^\[\s*Verse\s+\d+[^\]]*\]\s*', '', line)
                buffer = [verse_text] if verse_text.strip() else []
                continue
            
            m = re.match(r'^\*\*(\d+)\.\*\*\s*(.*)', line)
            if m:
                if current_verse and buffer:
                    chapters.setdefault(current_chapter, {})[current_verse] = Verse(
                        current_chapter, current_verse, '\n'.join(buffer).strip(),
                        is_interpolation="(interpolation)" in line.lower()
                    )
                current_verse = int(m.group(1))
                buffer = [m.group(2)]
                continue
            
            if current_verse is not None and line.strip():
                buffer.append(line.strip())
        
        if current_chapter and current_verse and buffer:
            chapters.setdefault(current_chapter, {})[current_verse] = Verse(
                current_chapter, current_verse, '\n'.join(buffer).strip(),
                is_interpolation="(interpolation)" in line.lower()
            )
    
    return chapters

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('"', '"').replace('"', '"')
    text = text.replace(''', "'").replace(''', "'")
    return text.strip()

def extract_ocr_segments(ocr_text: str, page_num: int) -> list[dict]:
    """Extract meaningful text segments from OCR."""
    segments = re.split(r'\n\s*\n|\. {2,}|\? {2,}|\! {2,}', ocr_text)
    results = []
    for seg in segments:
        seg = seg.strip()
        if len(seg) > 40:
            results.append({
                'page': page_num,
                'text': seg[:500],
                'length': len(seg)
            })
    return results

def load_ocr_page(page: int) -> str:
    """Load OCR text for a page."""
    n = page + 21
    possible_dirs = [
        f"pp{page//10*10}-{page//10*10+9}",
        "pp55-62", "pp63-74", "pp75-84", "pp85-94", "pp95-104",
        "pp105-186", "pp187-259", "pp265-308", "pp301-308"
    ]
    for sub in possible_dirs:
        f = OCR_DIR / sub / f"p{page:03d}_n{n:03d}.txt"
        if f.exists():
            return f.read_text(encoding='utf-8')
    return ""

def find_best_match(ocr_text: str, repo_verses: dict, threshold: float = 0.6) -> Optional[tuple]:
    """Find best matching repository verse for OCR text segment."""
    best_match = None
    best_score = 0
    best_verse = None
    
    ocr_clean = clean_text(ocr_text)
    if len(ocr_clean) < 30:
        return None
    
    for chapter, verses in repo_verses.items():
        for verse_num, verse_obj in verses.items():
            repo_clean = clean_text(verse_obj.text)
            score = SequenceMatcher(None, ocr_clean[:300], repo_clean[:300]).ratio()
            if score > best_score and score >= threshold:
                best_score = score
                best_match = repo_clean
                best_verse = (chapter, verse_num, verse_obj.is_interpolation)
    
    if best_match:
        return best_match, best_score, best_verse
    return None

def classify_discrepancy(ocr: str, repo: str, is_interpolation: bool) -> str:
    if is_interpolation:
        return "interpolation"
    
    if re.search(r'\bye\b', ocr) and re.search(r'\byou\b', repo):
        return "modernization"
    if re.search(r'\bthou\b', ocr) and re.search(r'\byou\b', repo):
        return "modernization"
    if re.search(r'\bthee\b', ocr) and re.search(r'\byou\b', repo):
        return "modernization"
    
    ocr_errors = ['themselvese', 'agamst', 'donot', 'tiplied', 'vead', 'Semjizd', 'Rufael', 'LHMAG', 'TwmT']
    for err in ocr_errors:
        if err in ocr:
            return "ocr_error"
    
    if '[' in ocr and ']' in ocr and '[' not in repo:
        return "structural"
    
    if SequenceMatcher(None, ocr, repo).ratio() < 0.9:
        return "lexical_variant"
    
    return "match"

def extract_apparatus_from_ocr(page: int, ocr_text: str) -> list[ApparatusEntry]:
    entries = []
    sigla_pattern = r'\b(G|M|S|Gr\.|Lat\.|Syr\.|Arm\.|Eth\.|Giz\.|Syn\.)\b'
    
    lines = ocr_text.split('\n')
    for line in lines:
        line = line.strip()
        if len(line) < 30:
            continue
        sigla_found = re.findall(sigla_pattern, line)
        if sigla_found:
            lemma_match = re.match(r'^([^.]+?)\s*[.:]\s*', line)
            lemma = lemma_match.group(1) if lemma_match else line[:100]
            entries.append(ApparatusEntry(
                page=page,
                lemma=lemma.strip(),
                sigla=sigla_found,
                witnesses=line,
                charles_note=line[:300],
                repo_has=False
            ))
    return entries

def process_page(page: int, repo_verses: dict) -> tuple[list[Discrepancy], list[ApparatusEntry]]:
    """Process a single page."""
    ocr_text = load_ocr_page(page)
    if not ocr_text:
        return [], []
    
    discrepancies = []
    segments = extract_ocr_segments(ocr_text, page)
    
    for seg in segments:
        match_result = find_best_match(seg['text'], repo_verses)
        if match_result:
            repo_text, score, (ch, vs, is_interp) = match_result
            disc_type = classify_discrepancy(clean_text(seg['text']), repo_text, is_interp)
            confidence = "high" if score > 0.85 else "medium" if score > 0.7 else "low"
            
            discrepancies.append(Discrepancy(
                page=page,
                leaf=page + 21,
                repo_chapter=ch,
                repo_verse=vs,
                discrepancy_type=disc_type,
                charles_text=seg['text'][:200],
                repo_text=repo_text[:200],
                similarity=round(score, 3),
                confidence=confidence,
                notes=f"Fuzzy match (score: {score:.2f})"
            ))
    
    apparatus = extract_apparatus_from_ocr(page, ocr_text)
    return discrepancies, apparatus

def process_section(page_start: int, page_end: int, repo_verses: dict) -> dict:
    all_discrepancies = []
    all_apparatus = []
    
    for page in range(page_start, page_end + 1):
        print(f"  Processing page {page}...")
        discs, app = process_page(page, repo_verses)
        all_discrepancies.extend(discs)
        all_apparatus.extend(app)
    
    by_type = {}
    by_confidence = {}
    for d in all_discrepancies:
        by_type[d.discrepancy_type] = by_type.get(d.discrepancy_type, 0) + 1
        by_confidence[d.confidence] = by_confidence.get(d.confidence, 0) + 1
    
    return {
        'pages': f"{page_start}-{page_end}",
        'discrepancies': [asdict(d) for d in all_discrepancies],
        'apparatus': [asdict(a) for a in all_apparatus],
        'stats': {
            'total_discrepancies': len(all_discrepancies),
            'by_type': by_type,
            'by_confidence': by_confidence
        }
    }

def main():
    print("Loading repository verses...")
    repo_verses = load_repo_verses()
    total_verses = sum(len(v) for v in repo_verses.values())
    print(f"Loaded {len(repo_verses)} chapters, {total_verses} verses")
    
    sections = [
        (55, 62, "Introduction + Ch1-6"),
        (63, 74, "Ch6-10"),
        (75, 84, "Ch10-15"),
        (85, 94, "Ch15-22"),
        (95, 104, "Ch22-36"),
        (105, 124, "Ch37-46"),
        (125, 144, "Ch47-56"),
        (145, 164, "Ch57-66"),
        (165, 186, "Ch67-71"),
        (187, 206, "Ch72-77"),
        (207, 218, "Ch78-82"),
        (219, 238, "Ch83-88"),
        (239, 259, "Ch89-90"),
        (265, 284, "Ch91-96"),
        (285, 308, "Ch97-105"),
        (301, 308, "Ch106-108 (CV-CVIII)"),
    ]
    
    all_results = {}
    
    for start, end, label in sections:
        print(f"\n=== Section: {label} (pp.{start}-{end}) ===")
        result = process_section(start, end, repo_verses)
        all_results[f"pp{start}-{end}"] = result
        
        out_file = OUTPUT_DIR / f"proofing_pp{start}-{end}.json"
        out_file.write_text(json.dumps(result, indent=2))
        print(f"  Saved: {out_file} ({result['stats']['total_discrepancies']} discrepancies)")
    
    combined = {
        'metadata': {
            'total_pages': 254,
            'total_chapters': len(repo_verses),
            'total_verses': total_verses,
            'sections_processed': len(sections)
        },
        'sections': all_results
    }
    
    combined_file = OUTPUT_DIR / "proofing_full_combined.json"
    combined_file.write_text(json.dumps(combined, indent=2))
    print(f"\nCombined report: {combined_file}")
    
    csv_file = OUTPUT_DIR / "verification_queue.csv"
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Page', 'Leaf', 'Chapter', 'Verse', 'Type', 'Charles Text', 'Repo Text', 'Similarity', 'Confidence', 'Notes', 'Verified', 'Reviewer'])
        for section_data in all_results.values():
            for d in section_data['discrepancies']:
                writer.writerow([
                    d['page'], d['leaf'], d['repo_chapter'], d['repo_verse'],
                    d['discrepancy_type'], d['charles_text'], d['repo_text'],
                    d['similarity'], d['confidence'], d['notes'], '', ''
                ])
    print(f"Verification queue: {csv_file}")

if __name__ == '__main__':
    main()