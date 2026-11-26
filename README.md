# Ancient Books Study

A public text corpus for studying ancient literature, religious traditions, historical scholarship, archaeology, science, architecture, mythology, and esoteric traditions.

The repository is primarily a **document collection and research workspace**, not a packaged application. It preserves archival source files and maintains separately labelled formatted transcriptions, modern-language adaptations, interpretations, OCR/page-image evidence, and research reports.

## Repository layout

| Directory | Contents |
|---|---|
| [`books_01/`](./books_01/)–[`books_05/`](./books_05/) | Original numbered collection batches: religious texts, translations, Enoch literature, Gnostic writings, epic literature, architecture, medicine, mathematics, mythology, and historical/scientific works. |
| [`copyrighted_works/`](./copyrighted_works/) | Rights and provenance risk records for selected works; source files remain in their original collection folders. |
| [`pdfs/`](./pdfs/) | Source PDFs and digitized editions, with provenance and scan-verification notes. |
| [`artifacts/`](./artifacts/) | Downloaded page images, OCR extracts, manifests, collation datasets, and research/audit reports. |
| [`formatted_editions/`](./formatted_editions/) | Faithful formatted reading transcriptions, source notes, editorial standards, and catalog. |
| [`modernized_editions/`](./modernized_editions/) | Clearly labelled modern-language adaptations, kept separate from archival and faithful formatted texts. |
| [`formatted_stories/`](./formatted_stories/) | Source-grounded narrative adaptations; not transcriptions or independent textual witnesses. |
| [`formatted_meanings/`](./formatted_meanings/) | Section-level meaning guides and explanatory notes. |
| [`formatted_interpretation/`](./formatted_interpretation/) | Verse-by-verse interpretive studies and separately labelled visual prompts. |
| [`docs/`](./docs/) | Usage guidance, audit standards, pipeline specification, and repository review reports. |
| [`tools/`](./tools/) and [`tests/`](./tests/) | Read-only corpus audit utilities, retrieval/proofing tools, and regression tests. |
| [`.github/workflows/`](./.github/workflows/) | Targeted GitHub Actions validation workflows. |

## Example texts

- [New King James Version 1982 NKJV.txt](./books_01/New%20King%20James%20Version%201982%20NKJV.txt)
- [Bhagavad_Gita.txt](./books_01/Bhagavad_Gita.txt)
- [Aramaic_Text_Vol1.txt](./books_01/Aramaic_Text_Vol1.txt)
- [The Papyrus Ebers](./books_02/ANCIENT%20EGYPTIAN%20MEDICINE%20THE%20PAPYRUS%20EBERS.txt)
- [Old Testament Pseudepigrapha, vol. 1](./books_03/The_Old_Testament_Pseudepigrapha_vol.1_Charlesworth_1983.txt)
- [Corpus Hermeticum — Mead, 1906](./books_04/Corpus_Hermeticum_Mead_1906.txt)
- [The Rhind Papyrus, vol. 1](./books_05/The_Rhind_Papyrus_Volume_1.txt)

## Editorial layers and verification

Keep these categories distinct:

1. **Archival source** — preserved as received; never silently normalize or overwrite it.
2. **Faithful formatted transcription** — a reading derivative of one identified source, with layout cleanup documented.
3. **Modern-language adaptation** — contemporary re-expression, not a transcription or new translation.
4. **Story adaptation / meaning guide / interpretation** — derivative study aids with explicit source references and editorial status.
5. **Evidence artifacts** — page images, OCR, manifests, discrepancy candidates, and collation logs.

A successful OCR transfer, matching chapter count, image download, or automated test is not facsimile verification or independent human review. Every published status must say exactly what was checked and against which witness. See [Audit Standards](./docs/AUDIT_STANDARDS.md), the [formatted-content pipeline](./docs/formatted-content-pipeline.md), and the [Formatted Editions Catalog](./formatted_editions/CATALOG.md).

The 1 Enoch 1893 work remains an active proofing project. Its current evidence boundary is **50/254 page/layout inspections, 0/254 full line-by-line diplomatic textual/apparatus proofing, and independent human approval pending**. The page/layout count includes pp.63–74 at medium resolution; those pages are not suitable for detailed Greek/apparatus proofing. Consult the [proofing ledger](./formatted_editions/books/book-of-enoch-charles-1893/IMAGE_PROOFING_LOG.md) and [issue #1](https://github.com/hasnocool/ancient-books-study/issues/1) before changing those counts.

## Using the collection

No install or build step is required to read the text files. Clone the repository:

```bash
git clone https://github.com/hasnocool/ancient-books-study.git
cd ancient-books-study
```

Search with ripgrep (if installed):

```bash
rg -n -i "search phrase" books_01 books_02 books_03 books_04 books_05
```

For substantial research, record the exact path, edition, translator, page/section, source URL, and verification status with every extracted note.

## Quality checks

Use Python 3.12+ from the repository root:

```bash
python3 tools/audit_corpus.py all --json-out /tmp/ancient-books-audit.json
python3 -m unittest discover -s tests -v
```

The local toolkit is read-only with respect to source documents. Review warnings manually: duplicate candidates, outlier lengths, and provenance keyword matches are not grounds for automatic deletion or correction. GitHub Actions currently runs a focused proofing-integrity regression workflow; the complete corpus audit and full test suite are also available locally and are being added to automated validation. See [tools/README.md](./tools/README.md).

## Collection notes

- The collection contains translations, OCR results, text extracts, and secondary scholarship; it is not a canonical source database.
- Treat every file as requiring source verification. OCR, formatting, edition, and translation quality vary.
- Similar filenames may represent duplicates, alternate editions, translations, or partial extracts.
- Some files are empty placeholders or incomplete scans; do not treat their presence as completed acquisition.
- The repository includes conventional scholarship, alternative interpretations, religious polemic, pseudoscience, and disputed claims. Inclusion does not imply endorsement or factual accuracy.

## Rights and provenance

**No repository-wide content license is declared.** Individual works may be public domain, licensed, copyrighted, or of uncertain status. Repository inclusion does not grant reuse rights. The records in [copyrighted_works/](./copyrighted_works/) are preliminary risk/provenance documentation, not legal opinions or universal clearance decisions.

Before redistributing, publishing, or creating derivatives, verify the exact source edition, translation/editorial contributions, applicable jurisdiction, license or public-domain basis, and rights in OCR/transcription data. Do not redistribute works whose rights are unresolved. Report concerns with the exact file path and source evidence.

## Contributing

Contributions are welcome, especially source metadata, OCR corrections, duplicate analysis, and verified public-domain or appropriately licensed texts. Read [CONTRIBUTING.md](./CONTRIBUTING.md) and [AGENTS.md](./AGENTS.md) before making changes.
