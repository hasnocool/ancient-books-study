# Repository Working Agreement

## Purpose and editorial boundaries

This repository is a digital humanities corpus and research workspace. Preserve the distinction between archival sources, faithful formatted transcriptions, modern-language adaptations, story adaptations, meaning guides, interpretations, and evidence artifacts.

Read `README.md`, `CONTRIBUTING.md`, the relevant directory README, and the current issue/report before beginning work. For formatted derivatives, also read `docs/AUDIT_STANDARDS.md` and `docs/formatted-content-pipeline.md`.

## Preservation rules

- Never overwrite, normalize in place, or delete archival source files.
- Do not merge editions, translations, or witnesses because filenames or normalized text look similar.
- Keep OCR correction, editorial emendation, translation, modernization, and interpretation distinct.
- Mark unknown provenance and rights as unknown; never infer them from filenames.
- Do not claim facsimile verification, independent human review, or completed testing unless the evidence exists.
- A downloaded image is not an inspected image. Page/layout inspection is not line-by-line diplomatic proofing.
- Automated similarity or regression checks identify candidates; they do not establish semantic fidelity or resolve copyright.

## Canonical project locations

- Archival text batches: `books_01/` through `books_05/`
- Source PDFs: `pdfs/`
- Research evidence, OCR, manifests, and reports: `artifacts/`
- Faithful formatted reading editions: `formatted_editions/`
- Modern-language adaptations: `modernized_editions/`
- Story adaptations: `formatted_stories/`
- Meaning guides: `formatted_meanings/`
- Interpretive studies and visual prompts: `formatted_interpretation/`
- Standards and project documentation: `docs/`
- Audit/retrieval code and tests: `tools/`, `tests/`

Use repository-relative paths only. Do not include machine-specific checkout paths in committed documentation.

## 1 Enoch 1893 proofing boundary

The authoritative ledger is `formatted_editions/books/book-of-enoch-charles-1893/IMAGE_PROOFING_LOG.md`; issue #1 tracks the work. At the 2026-11-26 review point:

- 50/254 pages have page/layout-level visual inspection records (pp.55–104).
- 0/254 pages have completed line-by-line diplomatic textual/apparatus proofing.
- Independent human approval is pending.
- pp.63–74 were inspected from 340×569 images, which are insufficient for detailed Greek/apparatus proofing.
- Do not increase counts based on retrieval, OCR, metadata, or automated checks.

If any of these facts change, reconcile the ledger, issue #1, and this file in the same change.

## Source and rights requirements

For each new derivative, record work identity, author/attribution, translator/editor, language, exact edition, source path and stable source URL, rights basis, extraction method, editorial transformations, coverage, verification status, reviewer, and unresolved issues. Use explicit unknown/not-established values where evidence is missing.

Do not create or publish derivatives of works marked restricted or rights-unresolved in `copyrighted_works/` without documented permission or a suitable public-domain/licensed source.

## Validation

Run from the repository root with Python 3.12+:

```bash
python3 tools/audit_corpus.py all --json-out /tmp/ancient-books-audit.json
python3 -m unittest discover -s tests -v
```

For focused proofing-data changes, also run:

```bash
python3 -m unittest discover -s tests -p "test_proofing_dataset_integrity.py" -v
```

Review all warnings manually. Do not commit temporary audit output unless it is intended as a maintained report. Never describe a command as passed unless it was executed and its result inspected.

## Change management

- Keep changes scoped and preserve source files.
- Update the relevant catalog, ledger, issue, and documentation when their underlying facts change.
- Add regression tests for data-integrity invariants and keep tests independent of network access.
- Use a branch and pull request for substantive changes; do not merge or publish without explicit authorization.
