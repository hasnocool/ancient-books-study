# Repository Audit Standards

These standards apply to archival source files and all derivative editions. They define what local automated checks can establish and what requires human or source-image review.

## 1. Editorial layers

1. **Archival source** — collected file preserved as received. Do not silently normalize or overwrite it.
2. **Faithful formatted transcription** — derivative that preserves the identified source edition's wording and order while documenting layout cleanup.
3. **Modern-language adaptation** — a separate derivative that re-expresses source text in contemporary language. It must not be presented as a transcription or an original-language translation unless it actually is one.
4. **Study edition** — source text accompanied by clearly separated commentary and apparatus.

## 2. Required provenance record

For each derivative, record as much as can be established:

- Work title and alternate titles.
- Author, compiler, or attributed author.
- Translator and editor.
- Language and textual tradition.
- Printed edition, publisher, place, and date.
- Exact archival source path and stable archive/facsimile URL.
- Rights or license basis for the specific text and translation.
- OCR/transcription method and known limitations.
- Editorial mode and every material transformation.
- Verification status, review date, reviewer, and unresolved issues.

Unknown information must be marked **unknown** or **not established**. Do not infer a source edition from a filename or title alone.

## 3. Completeness levels

Use these as separate claims, not interchangeable badges:

- **File coverage checked** — all expected derivative files exist.
- **Structure checked** — section identifiers and order match the selected source structure, including source irregularities.
- **Transfer checked** — normalized source body text is accounted for in the derivative without missing or duplicated source passages.
- **Semantic review completed** — a human has compared each derivative unit with its corresponding source and logged omissions, additions, and interpretive changes.
- **Facsimile collated** — text and structure have been compared with page images of the identified historical edition; uncertain readings are recorded.
- **Rights reviewed** — a documented basis for redistribution or a restriction is recorded.

Never promote a work to **Verified** solely because every file exists or headings are numbered.

## 4. Text comparison rules

- Preserve original archival bytes.
- Normalize whitespace only in comparison copies.
- Keep translation, modernization, OCR correction, and textual emendation separate.
- Compare by stable units: book, chapter, verse, section, paragraph, or source page.
- Record source and derivative identifiers for every discrepancy.
- Flag extreme length differences as review candidates, not automatic proof of an omission.
- A similarity score cannot establish theological, historical, or semantic equivalence.
- Do not reconstruct missing text from memory or another edition without separately identifying the witness and editorial decision.

## 5. Structural numbering

- Preserve source numbering gaps, duplicated numbers, unnumbered passages, and interpolations.
- Expected numbering must come from the selected source or a documented structural reference.
- If another edition supplies numbering, identify that edition and do not imply that its wording was adopted.
- Use a stable and consistent Markdown heading format for numbered units.

## 6. Automated checks

The local audit tool may report:

- File inventory, empty files, and suspiciously small files.
- Exact duplicate content and normalized-text duplicate candidates.
- Missing or broken relative Markdown links and heading anchors.
- Missing provenance and rights metadata.
- Missing chapter files and heading/verse sequence differences.
- Extreme verse-length ratios and unit-count discrepancies.
- Files that appear in no catalog or catalog entries with missing targets.

Automated reports are advisory. They must not make source edits, delete duplicates, decide copyright, or claim semantic equivalence.

## 7. Human review requirements

Human review is required for:

- Semantic fidelity of a modern-language adaptation.
- OCR words, proper names, numerals, foreign-language text, and damaged passages.
- Textual variants and interpolation boundaries where witnesses disagree.
- Copyright status where the applicable law or license is uncertain.
- Final publication or reuse claims.

Record the reviewer, date, source consulted, locations checked, findings, and unresolved questions.

## 8. Running the audit

The standard-library-only toolkit is run from the repository root:

```bash
python3 tools/audit_corpus.py all
python3 tools/audit_corpus.py inventory
python3 tools/audit_corpus.py duplicates
python3 tools/audit_corpus.py markdown
python3 tools/audit_corpus.py provenance
python3 tools/audit_corpus.py enoch
python3 tools/audit_corpus.py compare
python3 tools/generate_catalog.py --catalog-out /tmp/formatted-catalog-preview.md
python3 -m unittest discover -s tests -v
```

The default mode is read-only. Reports are printed or written to a user-selected path; no source document is modified. Thin command-specific entry points are documented in tools/README.md.
