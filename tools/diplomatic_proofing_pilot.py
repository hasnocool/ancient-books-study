#!/usr/bin/env python3
"""
Diplomatic Proofing Pilot — 1 Enoch (Charles 1893)
Compares OCR text from Cornell scan vs. repository formatted edition.
"""

import re
import json
from pathlib import Path
from difflib import SequenceMatcher

# Paths
OCR_DIR = Path("artifacts/1-enoch-1893/ocr/pp55-62")
REPO_FILE = Path("formatted_editions/books/book-of-enoch-charles-1893/book-01-watchers-chapters-01-36.md")
OUTPUT_DIR = Path("artifacts/1-enoch-1893/reports/diplomatic_proofing")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_ocr_pages():
    """Load OCR text for pp.55-62."""
    pages = {}
    for i in range(55, 63):
        n = i + 21
        f = OCR_DIR / f"p{i:03d}_n{n:03d}.txt"
        if f.exists():
            pages[i] = f.read_text(encoding='utf-8')
    return pages

def load_repo_chapters():
    """Parse repository markdown into chapter/verse structure."""
    text = REPO_FILE.read_text(encoding='utf-8')
    chapters = {}
    current_chapter = None
    current_verse = None
    buffer = []
    
    for line in text.split('\n'):
        # Chapter header
        m = re.match(r'^## Chapter (\d+)', line)
        if m:
            if current_chapter and buffer:
                chapters[current_chapter][current_verse] = '\n'.join(buffer).strip()
            current_chapter = int(m.group(1))
            chapters[current_chapter] = {}
            current_verse = None
            buffer = []
            continue
        
        # Verse marker
        m = re.match(r'^\*\*(\d+)\.\*\*\s*(.*)', line)
        if m:
            if current_verse and buffer:
                chapters[current_chapter][current_verse] = '\n'.join(buffer).strip()
            current_verse = int(m.group(1))
            buffer = [m.group(2)]
            continue
        
        # Continuation
        if current_verse is not None and line.strip():
            buffer.append(line.strip())
    
    # Flush last
    if current_chapter and current_verse and buffer:
        chapters[current_chapter][current_verse] = '\n'.join(buffer).strip()
    
    return chapters

def clean_text(text):
    """Normalize text for comparison."""
    # Remove extra whitespace, normalize quotes, etc.
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('"', '"').replace('"', '"')
    text = text.replace(''', "'").replace(''', "'")
    return text.strip()

def find_best_match(ocr_text, repo_verses, threshold=0.6):
    """Find best matching repository verse for OCR text segment."""
    best_match = None
    best_score = 0
    best_verse = None
    
    ocr_clean = clean_text(ocr_text)
    if len(ocr_clean) < 20:
        return None, 0, None
    
    for chapter, verses in repo_verses.items():
        for verse_num, verse_text in verses.items():
            repo_clean = clean_text(verse_text)
            score = SequenceMatcher(None, ocr_clean[:200], repo_clean[:200]).ratio()
            if score > best_score and score >= threshold:
                best_score = score
                best_match = repo_clean
                best_verse = (chapter, verse_num)
    
    return best_match, best_score, best_verse

def extract_ocr_segments(ocr_text, page_num):
    """Extract meaningful text segments from OCR."""
    # Split by double newlines or major punctuation
    segments = re.split(r'\n\s*\n|\. {2,}|\? {2,}|\! {2,}', ocr_text)
    results = []
    for seg in segments:
        seg = seg.strip()
        if len(seg) > 30:  # Filter noise
            results.append({
                'page': page_num,
                'text': seg[:500],
                'length': len(seg)
            })
    return results

def main():
    print("Loading OCR pages...")
    ocr_pages = load_ocr_pages()
    print(f"Loaded {len(ocr_pages)} pages")
    
    print("Loading repository chapters...")
    repo_chapters = load_repo_chapters()
    total_verses = sum(len(v) for v in repo_chapters.values())
    print(f"Loaded {len(repo_chapters)} chapters, {total_verses} verses")
    
    # Extract OCR segments
    all_segments = []
    for page_num, text in ocr_pages.items():
        segments = extract_ocr_segments(text, page_num)
        all_segments.extend(segments)
    
    print(f"Extracted {len(all_segments)} OCR segments")
    
    # Match segments to repository verses
    matches = []
    for seg in all_segments:
        match, score, verse_ref = find_best_match(seg['text'], repo_chapters)
        if match:
            matches.append({
                'page': seg['page'],
                'ocr_excerpt': seg['text'][:200],
                'repo_chapter': verse_ref[0],
                'repo_verse': verse_ref[1],
                'repo_excerpt': match[:200],
                'similarity': round(score, 3),
                'status': 'matched' if score > 0.8 else 'partial'
            })
    
    print(f"Found {len(matches)} matches")
    
    # Save results
    output = {
        'pages_processed': list(ocr_pages.keys()),
        'repo_chapters': list(repo_chapters.keys()),
        'total_ocr_segments': len(all_segments),
        'total_matches': len(matches),
        'matches': matches
    }
    
    out_file = OUTPUT_DIR / "pilot_pp55-62_matches.json"
    out_file.write_text(json.dumps(output, indent=2))
    print(f"Results saved to {out_file}")
    
    # Print summary
    print("\n=== MATCH SUMMARY ===")
    for m in matches[:20]:
        print(f"  p{m['page']} -> Ch{m['repo_chapter']}.{m['repo_verse']} ({m['similarity']:.0%}) {m['status']}")
        print(f"    OCR: {m['ocr_excerpt'][:80]}...")
        print(f"    REPO: {m['repo_excerpt'][:80]}...")
        print()

if __name__ == '__main__':
    main()