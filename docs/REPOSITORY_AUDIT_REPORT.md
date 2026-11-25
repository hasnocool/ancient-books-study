# Repository Audit — Remediation Report

**Review date:** 2026-11-25  
**Repository:** hasnocool/ancient-books-study  
**Scope:** Documentation corrections, modernized-edition organization, local audit tooling, and 1 Enoch structural/source review.

## Completed changes

### Documentation and navigation

- Added modernized_editions to the root repository layout and clarified the separation between archival sources, faithful formatted editions, and modern-language adaptations.
- Added a dedicated modernized-editions landing page with editorial rules and verification labels.
- Added repeatable audit standards covering provenance, completeness levels, text comparison, numbering, automated checks, and human review.
- Corrected stale source notes that said Chapters 72–108 still needed verse restoration.
- Updated the Chapter 91 restoration note to describe the preserved repository sequence and the documented Charles rearrangement without claiming the issue is unresolved.
- Removed duplicate Gospel of Thomas and Vitruvius rows from the formatted-editions catalog.
- Consolidated repeated Gospel of Thomas material in the completeness audit.
- Standardized Chapter 91's verse headings to match the modernized edition's Markdown structure.
- Added a review log for all 108 modernized chapters and a historical-source collation log for 1 Enoch.

### Structural comparison

All six formatted 1 Enoch source files were compared with the 108 modernized chapter files by chapter and numbered-unit label. **108 of 108 chapter label sequences matched.**

The original combined Enoch archive file was also compared against the six formatted chapter files by normalized body text. **108 of 108 chapter bodies now match.** Seven sequential embedded page-number artifacts (53–59) were found in Chapters 91, 93, 96, 98, 100, 102, and 104; they were removed from the formatted derivative. The archival source file was not changed. The local validator now repeats this raw-to-formatted transfer check and emits token-level differences for any future mismatches.

The comparison preserved source irregularities rather than repairing them, including unnumbered chapters, numbering gaps, repeated verse numbers, and interpolation labels. A verse-length anomaly screen across all 108 chapters found no units outside the severe word-count thresholds after removing editorial apparatus. Moderate examples in Chapters 10:20, 72:20, and 89:4 were inspected; Chapter 69:2 was revised to retain the ordinal sequence of 21 names, and commentary was separated from Chapter 98:5. These checks are triage and spot review only; they do not prove that the modernized wording preserves every nuance of the source.

### Historical source findings

The 1893 Clarendon Press facsimile and catalog record were consulted. The title page and preface describe a translation based mainly on a British Museum manuscript designated G, with readings adopted from additional Ethiopic manuscripts and Greek/Latin fragments.

The 1893 contents list the main translation sections through Chapter 104. They also list Appendix D as additional notes on Chapters 37–108 and Appendix E as a Latin fragment for Chapter 106:1–18. Therefore Chapters 105–108 must not automatically be described as part of the 1893 main translation text. Their source and structural reference must be identified separately.

Sample comparisons already documented in the Enoch source notes show wording differences in Chapter 1:2, Chapter 2, and Chapter 3. The selected repository transcription is not verbatim Charles 1893, and its exact textual lineage remains unresolved.

See the [source collation log](../formatted_editions/books/book-of-enoch-charles-1893/SOURCE_COLLATION_LOG.md) for references and the chapter-by-chapter collation procedure.

## 1 Enoch semantic review and witness comparison — current update

An assistant-led verse-by-verse comparison has now been completed across **all 108 modernized chapter files** against the selected formatted repository transcription. Corrections made during that pass are recorded in `modernized_editions/books/1-enoch-repository-transcription/REVIEW_LOG.md`. This is a first-pass editorial review, not independent human approval. A second reviewer must still approve every chapter and resolve flagged interpretations.

The 1893 searchable scan text layer has also been sampled at selected readings (including 7:2, 13:1, 14:11, 20:3–4, 22:11, 46:1, and 65:6). Those comparisons support several lexical and numerical corrections, but they are not a complete collation and are not visual page-image proofreading. The 1893 main translation sections run through Chapter 104. A separate Charles/Oesterley 1917 witness, reprinting Charles's 1912 second edition, has been identified for the later material. Its paratext classifies 105 as two verses of uncertain date, 106–107 as the Noah fragment, and 108 as an appendix. Chapters 105–108 have only been sampled against this witness; full page-by-page collation remains open.

See `formatted_editions/books/book-of-enoch-charles-1893/SOURCE_COLLATION_LOG.md` for the 1893 text-layer observations, the 1917 witness identification, and the page-image limitations. The PDF screenshot service rejected the large scans, so no scan page is claimed as visually proofread.

## Corpus-wide remote inventory — current update

A complete, untruncated Git-tree inventory of `books_01`–`books_05` was completed at tree SHA `867210a4e1898fba0155ae0885a7d35b7810e3e0`. It found **165 text files / 203,704,878 bytes**, with **24 zero-byte placeholders**. Git blob hashes confirmed **43 non-empty exact-byte duplicate groups** involving 100 files (57 copies beyond one representative per group), plus one zero-byte group. No duplicates or placeholders were changed.

Targeted content checks identified several rights and provenance leads, including modern copyrighted translations and commentary, a text whose own notice says it is not public domain, and OCR replacement-character damage in a four-path exact duplicate group. These findings are leads rather than legal determinations; the whole-corpus rights and OCR review remains outstanding. The detailed per-folder counts, full duplicate path groups, empty-file list, and rights/OCR leads are in `docs/CORPUS_INVENTORY_AUDIT.md`.

The local audit toolkit and test suite still have **not** been run from a complete local checkout. A clone attempt failed at DNS resolution of `github.com`; the remote inventory is not represented as a successful local script run.

## Local audit toolkit added

The toolkit is dependency-free and targets Python 3.12 or later. It contains a read-only orchestrator plus individual entry points for:

- file inventory and empty/suspiciously small files;
- exact, normalized, and conservative near-duplicate candidates;
- relative Markdown links and heading anchors;
- edition provenance metadata screening;
- 1 Enoch expected-file and verse-label sequence checks;
- normalized archive-to-formatted text transfer comparisons, including word-level discrepancy reporting;
- formatted-to-modernized verse-label and unit-length comparisons for human review;
- a generated formatted-edition catalog preview.

Unit tests cover normalization, verse-label variants, duplicate/missing numbering, chapter extraction, and read-only behavior.

The toolkit and tests have been committed, but the full Python test suite and whole-corpus scan have **not** been executed from a fresh local checkout in this review environment. Run them locally using the commands in tools/README.md. Do not treat the static code review as a successful test run.

## Remaining work — not marked complete

| Work item | Status |
|---|---|
| Run the local audit toolkit across all five archival directories | Pending local execution; remote Git-tree inventory completed (165 files, 24 empty, 43 non-empty exact duplicate groups) |
| Run the Python unittest suite | Pending local execution |
| Complete independent human semantic review of every modernized 1 Enoch verse | Pending; assistant-led first-pass comparison of all 108 chapters completed and corrections logged |
| Fully collate Chapters 1–104 against the 1893 facsimile | Pending; selected searchable text-layer comparisons completed, no page-image proofing |
| Collate Chapters 105–108 against their explicitly identified later witness | 1917 text-layer comparison complete for 105–108; visual page-image collation and independent review pending |
| Identify exact textual lineage of the combined repository transcription | Unresolved |
| Inspect uncertain readings directly from scan page images | Pending; the initial PDF page-image capture attempt was blocked by the provider's file-size limit |
| Review copyright and licensing metadata for every archival item | Pending; targeted rights/provenance signals recorded in corpus inventory report |
| Resolve all zero-byte files, OCR defects, and duplicate candidates | Pending manual review; remote inventory and exact-byte groups recorded, no changes made |

## Safety and preservation

No archival source text was overwritten, deleted, or automatically normalized. Duplicate detection is advisory; differing editions and translations must remain separate unless a human review establishes their relationship. No paid GitHub Actions workflow was added.

## Overall assessment

The repository now has clearer editorial layers, consistent 1 Enoch navigation, reconciled documentation, and a repeatable local validation toolkit. The 1 Enoch chapter/verse structure matches across the 108 source and modernized files. The repository is **not yet publication-ready as a semantically reviewed or facsimile-verified edition**. The remaining work is explicitly tracked rather than represented as completed.
