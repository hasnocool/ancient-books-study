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

The comparison preserved source irregularities rather than repairing them, including unnumbered chapters, numbering gaps, repeated verse numbers, and interpolation labels. This is a structural result only; it does not prove that the modernized wording preserves every nuance of the source.

### Historical source findings

The 1893 Clarendon Press facsimile and catalog record were consulted. The title page and preface describe a translation based mainly on a British Museum manuscript designated G, with readings adopted from additional Ethiopic manuscripts and Greek/Latin fragments.

The 1893 contents list the main translation sections through Chapter 104. They also list Appendix D as additional notes on Chapters 37–108 and Appendix E as a Latin fragment for Chapter 106:1–18. Therefore Chapters 105–108 must not automatically be described as part of the 1893 main translation text. Their source and structural reference must be identified separately.

Sample comparisons already documented in the Enoch source notes show wording differences in Chapter 1:2, Chapter 2, and Chapter 3. The selected repository transcription is not verbatim Charles 1893, and its exact textual lineage remains unresolved.

See the [source collation log](../formatted_editions/books/book-of-enoch-charles-1893/SOURCE_COLLATION_LOG.md) for references and the chapter-by-chapter collation procedure.

## Local audit toolkit added

The toolkit is dependency-free and targets Python 3.12 or later. It contains a read-only orchestrator plus individual entry points for:

- file inventory and empty/suspiciously small files;
- exact, normalized, and conservative near-duplicate candidates;
- relative Markdown links and heading anchors;
- edition provenance metadata screening;
- 1 Enoch expected-file and verse-label sequence checks;
- extreme source/adaptation word-count ratios for human review;
- a generated formatted-edition catalog preview.

Unit tests cover normalization, verse-label variants, duplicate/missing numbering, chapter extraction, and read-only behavior.

The toolkit and tests have been committed, but the full Python test suite and whole-corpus scan have **not** been executed from a fresh local checkout in this review environment. Run them locally using the commands in tools/README.md. Do not treat the static code review as a successful test run.

## Remaining work — not marked complete

| Work item | Status |
|---|---|
| Run the local audit toolkit across all five archival directories | Pending local execution |
| Run the Python unittest suite | Pending local execution |
| Review every modernized 1 Enoch verse semantically | Pending human review |
| Fully collate Chapters 1–104 against the 1893 facsimile | Pending |
| Collate Chapters 105–108 against their explicitly identified later witness | Pending |
| Identify exact textual lineage of the combined repository transcription | Unresolved |
| Inspect uncertain readings directly from scan page images | Pending; the initial PDF page-image capture attempt was blocked by the provider's file-size limit |
| Review copyright and licensing metadata for every archival item | Pending corpus-wide review |
| Resolve all zero-byte files, OCR defects, and duplicate candidates | Pending inventory and manual review |

## Safety and preservation

No archival source text was overwritten, deleted, or automatically normalized. Duplicate detection is advisory; differing editions and translations must remain separate unless a human review establishes their relationship. No paid GitHub Actions workflow was added.

## Overall assessment

The repository now has clearer editorial layers, consistent 1 Enoch navigation, reconciled documentation, and a repeatable local validation toolkit. The 1 Enoch chapter/verse structure matches across the 108 source and modernized files. The repository is **not yet publication-ready as a semantically reviewed or facsimile-verified edition**. The remaining work is explicitly tracked rather than represented as completed.
