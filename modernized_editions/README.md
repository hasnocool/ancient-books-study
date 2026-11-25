# Modernized Editions

This directory contains modern-language adaptations of historical texts. These are derivative reading aids, not archival source files, not faithful transcriptions, and not necessarily new translations from the original languages.

## Editorial rules

- Keep every adaptation separate from the original archival collection and the faithful formatted edition.
- State the exact source path, edition attribution, and known provenance limitations.
- Preserve source chapter, section, verse, and sequence information unless a documented editorial decision says otherwise.
- Do not invent missing words, verses, chapter divisions, or historical claims.
- Identify interpolations, damaged text, uncertain readings, and numbering irregularities.
- Do not describe an adaptation as a new translation from an ancient language unless it was actually translated from that language by a qualified process.
- A complete file set is not proof of semantic fidelity. Each adaptation needs a source-to-adaptation review.

## Current editions

- [1 Enoch — modern-language rendering of the selected repository transcription, Chapters 1–108](./books/1-enoch-repository-transcription/README.md)

## Verification labels

| Label | Meaning |
|---|---|
| **Drafted** | A derivative file exists; editorial review may remain. |
| **Structurally checked** | Chapter/section and verse labels have been checked against the selected formatted source. |
| **First-pass semantic review complete** | An assistant-led verse-by-verse comparison and correction log exist; this is not independent approval. |
| **Independent human review pending** | A second reviewer has not yet approved every verse and resolved flagged interpretations. |
| **Facsimile collation pending** | Searchable text-layer comparisons do not replace page-image collation of the identified historical edition. |
| **Reviewed** | A documented human review has assessed fidelity, with issues and evidence recorded. |

Do not use **Verified** as a blanket status when only file coverage or numbering has been checked.

## Local quality checks

From the repository root:

```bash
python3 tools/audit_corpus.py all
python3 tools/audit_corpus.py enoch
python3 -m unittest discover -s tests -v
```

The audit toolkit is read-only by default. It reports structural and metadata problems; it does not rewrite source texts or automatically resolve textual variants.

## 1 Enoch scope and source limitation

The current 1 Enoch adaptation is based on the selected repository transcription in `formatted_editions/books/book-of-enoch-charles-1893/`. That transcription is attributed to R. H. Charles and August Dillmann (1893), but its exact textual lineage is unresolved and it is not verified as a verbatim transcription of the 1893 printing. The adaptation is therefore a modernization of the selected repository text, not a fresh Ethiopic translation and not a verified Charles 1893 text.

See the edition-specific [chapter index and editorial statement](./books/1-enoch-repository-transcription/README.md), the [source notes](../formatted_editions/books/book-of-enoch-charles-1893/SOURCE_NOTES.md), and the [restoration log](../formatted_editions/books/book-of-enoch-charles-1893/VERSE_RESTORATION_LOG.md).
