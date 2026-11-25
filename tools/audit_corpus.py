#!/usr/bin/env python3
"""Read-only quality checks for the Ancient Books Study corpus (Python 3.12+)."""
from __future__ import annotations
import argparse, collections, hashlib, json, re, sys, unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

ARCHIVE_DIRS = ("books_01", "books_02", "books_03", "books_04", "books_05")
IGNORED_DIRS = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", "node_modules"}
ENOCH_CHAPTERS = range(1, 109)
VERSE_MARKER = re.compile(
    r"(?m)^\s*(?:###\s+Verse\s+(\d+)(?:\s*[—-].*)?|"
    r"\*\*\[Verse\s+(\d+)\](?:\s*[—-][^*]*)?\*\*|"
    r"\*\*(\d+)\.\s*\*\*|"
    r"\*\*\[(\d+)\]\*\*)"
)
CHAPTER_MARKER = re.compile(r"(?m)^##\s+Chapter\s+(\d+)\b")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def normalized_text(text: str) -> str:
    """Comparison-only normalization; never write this representation back."""
    text = unicodedata.normalize("NFKC", text).casefold()
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return " ".join(text.split())

def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", text, flags=re.UNICODE))

def walk_files(root: Path, suffixes: set[str] | None = None):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in IGNORED_DIRS for part in path.relative_to(root).parts):
            continue
        if suffixes is not None and path.suffix.lower() not in suffixes:
            continue
        yield path

def issue(severity: str, check: str, path: str, message: str, **extra):
    item = {"severity": severity, "check": check, "path": path, "message": message}
    item.update(extra)
    return item

def audit_inventory(root: Path) -> dict:
    files = list(walk_files(root))
    by_area, empty, suspicious, total_bytes = collections.Counter(), [], [], 0
    for path in files:
        rel = path.relative_to(root).as_posix()
        by_area[rel.split("/", 1)[0]] += 1
        size = path.stat().st_size
        total_bytes += size
        if size == 0:
            empty.append(rel)
        elif size < 80 and path.suffix.lower() in {".md", ".txt"}:
            suspicious.append({"path": rel, "bytes": size})
    return {"file_count": len(files), "total_bytes": total_bytes,
            "by_top_level_directory": dict(sorted(by_area.items())),
            "empty_files": empty, "suspiciously_small_text_files": suspicious}

def audit_duplicates(root: Path) -> dict:
    archive_files = []
    for folder in ARCHIVE_DIRS:
        base = root / folder
        if base.exists():
            archive_files.extend(walk_files(base))
    exact, normalized = collections.defaultdict(list), collections.defaultdict(list)
    for path in archive_files:
        rel = path.relative_to(root).as_posix()
        exact[sha256_file(path)].append(rel)
        if path.stat().st_size <= 8 * 1024 * 1024:
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            normalized[hashlib.sha256(normalized_text(text).encode("utf-8")).hexdigest()].append(rel)
    exact_groups = [sorted(v) for v in exact.values() if len(v) > 1]
    normalized_groups = [sorted(v) for v in normalized.values() if len(v) > 1]
    return {"archive_file_count": len(archive_files),
            "exact_duplicate_groups": sorted(exact_groups),
            "normalized_text_duplicate_groups": sorted(normalized_groups),
            "note": "Exact groups have identical bytes. Normalized groups match after Unicode compatibility normalization, case-folding, and whitespace normalization; these are review candidates, not deletion instructions."}

def heading_slug(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text).lower().strip()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "-", text)

def markdown_anchors(path: Path) -> set[str]:
    anchors, seen = set(), collections.Counter()
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return anchors
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        base = heading_slug(match.group(2))
        count = seen[base]
        seen[base] += 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors

def audit_markdown(root: Path) -> dict:
    markdown_files = list(walk_files(root, {".md", ".markdown"}))
    broken, checked, anchor_cache = [], 0, {}
    for source in markdown_files:
        try:
            text = source.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError) as exc:
            broken.append(issue("error", "markdown-encoding", source.relative_to(root).as_posix(), str(exc)))
            continue
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().strip("<>")
            if not target:
                continue
            if target.startswith("#"):
                checked += 1
                anchor = unquote(target[1:])
                anchors = anchor_cache.setdefault(source, markdown_anchors(source))
                if anchor and anchor not in anchors:
                    broken.append(issue("warning", "markdown-anchor", source.relative_to(root).as_posix(), f"Heading anchor not found: {anchor}"))
                continue
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//"):
                continue
            checked += 1
            raw_path = unquote(parsed.path)
            candidate = (source.parent / raw_path).resolve() if raw_path else source.resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                broken.append(issue("error", "markdown-link", source.relative_to(root).as_posix(), f"Relative link escapes repository: {target}"))
                continue
            if candidate.is_dir():
                if not (candidate / "README.md").is_file() and not (candidate / "readme.md").is_file():
                    broken.append(issue("warning", "markdown-link", source.relative_to(root).as_posix(), f"Directory link has no README: {target}"))
            elif not candidate.is_file():
                broken.append(issue("warning", "markdown-link", source.relative_to(root).as_posix(), f"Target does not exist: {target}"))
            elif parsed.fragment:
                anchors = anchor_cache.setdefault(candidate, markdown_anchors(candidate))
                fragment = unquote(parsed.fragment)
                if fragment and fragment not in anchors:
                    broken.append(issue("warning", "markdown-anchor", source.relative_to(root).as_posix(), f"Anchor not found in {target}: {fragment}"))
    return {"markdown_file_count": len(markdown_files), "relative_links_checked": checked, "issues": broken}

def audit_provenance(root: Path) -> dict:
    candidates = []
    for base in (root / "formatted_editions" / "books", root / "modernized_editions" / "books"):
        if base.exists():
            candidates.extend(folder / "README.md" for folder in sorted(base.iterdir()) if folder.is_dir() and (folder / "README.md").exists())
    records = []
    for path in candidates:
        text = path.read_text(encoding="utf-8", errors="replace").casefold()
        missing = []
        if not re.search(r"\b(source|sources|source file|source text)\b", text):
            missing.append("source identification")
        if not re.search(r"\b(rights|copyright|license|public domain)\b", text):
            missing.append("rights statement")
        if not re.search(r"\b(status|verification|verified|draft)\b", text):
            missing.append("verification status")
        records.append({"path": path.relative_to(root).as_posix(), "missing_metadata": missing})
    return {"edition_readmes_checked": len(records), "records": records,
            "note": "Keyword screening is advisory; it does not establish that metadata is accurate or legally sufficient."}

def chapter_sections(text: str) -> dict[int, str]:
    matches, sections = list(CHAPTER_MARKER.finditer(text)), {}
    for index, match in enumerate(matches):
        number = int(match.group(1))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[number] = text[match.end():end]
    return sections

def verse_units(section: str) -> list[tuple[int, str]]:
    matches, units = list(VERSE_MARKER.finditer(section)), []
    for index, match in enumerate(matches):
        number = next(int(group) for group in match.groups() if group is not None)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        body = re.sub(r"(?m)^\s*---\s*$", "", section[match.end():end])
        units.append((number, body.strip()))
    return units

def load_enoch_sources(root: Path) -> dict[int, str]:
    base = root / "formatted_editions" / "books" / "book-of-enoch-charles-1893"
    filenames = ("book-01-watchers-chapters-01-36.md", "book-02-parables-chapters-37-71.md",
                 "book-03-luminaries-chapters-72-82.md", "book-04-visions-chapters-83-90.md",
                 "book-05-laws-of-enoch-chapters-91-105.md", "book-06-deluge-chapters-106-108.md")
    sources = {}
    for filename in filenames:
        path = base / filename
        if path.exists():
            sources.update(chapter_sections(path.read_text(encoding="utf-8", errors="replace")))
    return sources

def audit_enoch(root: Path) -> dict:
    modern_base = root / "modernized_editions" / "books" / "1-enoch-repository-transcription"
    source_sections = load_enoch_sources(root)
    missing_files, missing_source_sections, missing_units = [], [], []
    mismatches, outliers, modern_count = [], [], 0
    known_unnumbered = {4, 35, 44}
    for number in ENOCH_CHAPTERS:
        modern_path = modern_base / f"chapter-{number:03d}.md"
        if not modern_path.exists():
            missing_files.append(number)
            continue
        modern_count += 1
        modern = modern_path.read_text(encoding="utf-8", errors="replace")
        modern_section = chapter_sections(modern).get(number, modern)
        modern_units = verse_units(modern_section)
        if number not in source_sections:
            missing_source_sections.append(number)
            continue
        source_units = verse_units(source_sections[number])
        source_labels, modern_labels = [n for n, _ in source_units], [n for n, _ in modern_units]
        if source_labels != modern_labels:
            mismatches.append({"chapter": number, "source_labels": source_labels, "modernized_labels": modern_labels})
        if not source_units and number not in known_unnumbered:
            missing_units.append({"chapter": number, "reason": "No numbered units detected in selected source"})
        if source_units and not modern_units:
            missing_units.append({"chapter": number, "reason": "No numbered units detected in modernized file"})
        for (source_num, source_body), (modern_num, modern_body) in zip(source_units, modern_units):
            source_words, modern_words = word_count(source_body), word_count(modern_body)
            if source_words < 8 or modern_words < 8:
                continue
            ratio = modern_words / source_words
            if ratio < 0.35 or ratio > 2.8:
                outliers.append({"chapter": number, "source_verse": source_num, "modernized_verse": modern_num,
                                 "source_words": source_words, "modernized_words": modern_words, "ratio": round(ratio, 3)})
    return {"expected_chapters": len(ENOCH_CHAPTERS), "modernized_files_found": modern_count,
            "source_chapter_sections_found": len(source_sections), "missing_files": missing_files,
            "missing_source_sections": missing_source_sections, "numbered_unit_sequence_mismatches": mismatches,
            "missing_numbered_units": missing_units, "extreme_verse_length_ratios": outliers,
            "known_unnumbered_chapters": sorted(known_unnumbered),
            "interpretation": "Sequence comparison and word-count outliers are mechanical checks only. They cannot establish semantic fidelity; each outlier requires human review."}

def audit_comparison(root: Path) -> dict:
    result = audit_enoch(root)
    return {"extreme_verse_length_ratios": result["extreme_verse_length_ratios"],
            "numbered_unit_sequence_mismatches": result["numbered_unit_sequence_mismatches"],
            "method": "Compare paired source and adaptation units. Large word-count ratios are review candidates, not proof of mistranslation or omission."}


def audit_catalog(root: Path) -> dict:
    """Build a reviewable catalog view from edition README files without overwriting CATALOG.md."""
    rows = []
    base = root / "formatted_editions" / "books"
    if base.exists():
        for folder in sorted(p for p in base.iterdir() if p.is_dir()):
            readme = folder / "README.md"
            if not readme.exists():
                continue
            text = readme.read_text(encoding="utf-8", errors="replace")
            title_match = re.search(r"(?m)^#\s+(.+)$", text)
            status_match = re.search(r"(?im)^\s*[-*]?\s*(?:\*\*)?(?:status|verification status)(?:\*\*)?\s*:\s*(.+)$", text)
            rows.append({
                "title": title_match.group(1).strip() if title_match else folder.name,
                "path": readme.relative_to(root).as_posix(),
                "status_line": status_match.group(1).strip() if status_match else "Not declared in a recognized status line",
            })
    markdown = ["# Generated formatted-edition catalog preview", "",
                "This is a review preview generated from per-edition README files. It does not overwrite formatted_editions/CATALOG.md.", "",
                "| Edition | Index | Status text found |", "|---|---|---|"]
    for row in rows:
        markdown.append(f"| {row['title'].replace('|', '&#124;')} | [{row['path']}]({row['path']}) | {row['status_line'].replace('|', '&#124;')} |")
    return {"edition_count": len(rows), "editions": rows, "markdown_preview": "\n".join(markdown) + "\n"}

def collect_issues(results: dict) -> list[dict]:
    issues = []
    for path in results.get("inventory", {}).get("empty_files", []):
        issues.append(issue("warning", "inventory", path, "File is empty (zero bytes)."))
    for item in results.get("inventory", {}).get("suspiciously_small_text_files", []):
        issues.append(issue("warning", "inventory", item["path"], f"Text file is unusually small ({item['bytes']} bytes)."))
    for group in results.get("duplicates", {}).get("exact_duplicate_groups", []):
        issues.append(issue("info", "duplicates", group[0], "Exact duplicate content group.", files=group))
    for group in results.get("duplicates", {}).get("normalized_text_duplicate_groups", []):
        issues.append(issue("info", "duplicates", group[0], "Normalized duplicate candidate group.", files=group))
    issues.extend(results.get("markdown", {}).get("issues", []))
    for record in results.get("provenance", {}).get("records", []):
        if record["missing_metadata"]:
            issues.append(issue("warning", "provenance", record["path"], "Possible missing metadata: " + ", ".join(record["missing_metadata"])))
    enoch = results.get("enoch", {})
    for chapter in enoch.get("missing_files", []):
        issues.append(issue("error", "enoch", f"chapter-{chapter:03d}.md", "Expected modernized chapter file is missing."))
    for mismatch in enoch.get("numbered_unit_sequence_mismatches", []):
        issues.append(issue("error", "enoch", f"chapter-{mismatch['chapter']:03d}.md", "Unit labels differ from formatted source.",
                            source=mismatch["source_labels"], modernized=mismatch["modernized_labels"]))
    for outlier in enoch.get("extreme_verse_length_ratios", []):
        issues.append(issue("warning", "semantic-review", f"chapter-{outlier['chapter']:03d}.md", "Unit length differs substantially from source; human review required.", **outlier))
    return issues

def run_checks(root: Path, selected: set[str]) -> dict:
    results = {"repository_root": str(root.resolve())}
    checks = {"inventory": audit_inventory, "duplicates": audit_duplicates, "markdown": audit_markdown,
              "provenance": audit_provenance, "enoch": audit_enoch, "compare": audit_comparison,
              "catalog": audit_catalog}
    for name in ("inventory", "duplicates", "markdown", "provenance", "enoch", "compare", "catalog"):
        if name in selected:
            key = "comparison_review_candidates" if name == "compare" else name
            results[key] = checks[name](root)
    results["issues"] = collect_issues(results)
    return results

def print_report(results: dict) -> None:
    print(f"Repository: {results['repository_root']}")
    if "inventory" in results:
        item = results["inventory"]
        print(f"Inventory: {item['file_count']} files; {item['total_bytes']:,} bytes")
        print(f"Empty files: {len(item['empty_files'])}; suspiciously small text files: {len(item['suspiciously_small_text_files'])}")
    if "duplicates" in results:
        item = results["duplicates"]
        print(f"Duplicates: {len(item['exact_duplicate_groups'])} exact groups; {len(item['normalized_text_duplicate_groups'])} normalized groups")
    if "markdown" in results:
        item = results["markdown"]
        print(f"Markdown: {item['markdown_file_count']} files; {item['relative_links_checked']} relative links checked; {len(item['issues'])} issues")
    if "provenance" in results:
        item = results["provenance"]
        missing = sum(bool(row["missing_metadata"]) for row in item["records"])
        print(f"Provenance: {item['edition_readmes_checked']} edition READMEs checked; {missing} possible metadata gaps")
    if "catalog" in results:
        print(f"Catalog preview: {results['catalog']['edition_count']} formatted-edition indexes found")
    if "enoch" in results:
        item = results["enoch"]
        print(f"1 Enoch: {item['modernized_files_found']}/108 modernized files; {item['source_chapter_sections_found']} source sections")
        print(f"  Missing files: {len(item['missing_files'])}; numbering mismatches: {len(item['numbered_unit_sequence_mismatches'])}; length outliers: {len(item['extreme_verse_length_ratios'])}")
    counts = collections.Counter(row["severity"] for row in results["issues"])
    print("Issues: " + ", ".join(f"{name}={counts[name]}" for name in ("error", "warning", "info")))
    for row in results["issues"]:
        print(f"[{row['severity'].upper()}] {row['path']}: {row['message']}")

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("check", nargs="?", default="all",
        choices=("all", "inventory", "duplicates", "markdown", "provenance", "enoch", "compare", "catalog"))
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root (default: current directory)")
    parser.add_argument("--json-out", type=Path, help="Optional path for a machine-readable JSON report")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"Repository root is not a directory: {root}")
    selected = {"inventory", "duplicates", "markdown", "provenance", "enoch", "compare", "catalog"} if args.check == "all" else {args.check}
    results = run_checks(root, selected)
    print_report(results)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"JSON report written to {args.json_out}")
    return 1 if any(row["severity"] == "error" for row in results["issues"]) else 0

if __name__ == "__main__":
    sys.exit(main())
