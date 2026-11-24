# Completeness and Structure Audit

**Audit date:** 2026-11-23  
**Scope:** The two reading projects currently stored under `formatted_editions/books/`.

## What “complete” means here

This project distinguishes three different checks:

1. **Complete against repository source** — all text portions selected from the stated repository transcription have been transferred.
2. **Complete against the historical printed edition** — the transcription has been collated with the complete stated edition, including its relevant text and structure.
3. **Complete work / collection** — all distinct works combined in a source compilation have been accounted for, including separately transmitted companion works.

Passing the first check does not automatically pass the second or third. A faithful formatted transcription is not a new translation or paraphrase.

## 1. Corpus Hermeticum — Mead (1906)

**Reading index:** [Corpus Hermeticum](./books/corpus-hermeticum-mead-1906/README.md)  
**Source:** `books_04/Corpus_Hermeticum_Mead_1906.txt`

- The formatted directory contains all 15 tractate entries present in the selected transcription.
- Tractate XV jumps from section 4 to section 6 in the supplied source. No section 5 has been invented or filled from another edition.
- The source compilation also contains supplementary works: *Of Asclepius to the King*, *The Encomium of Kings*, and *The Perfect Sermon / Asclepius*.
- The *Perfect Sermon / Asclepius* file is explicitly a partial extract because the source itself ends during Book III, section 1.
- The modern introductory essay in the source compilation is not part of Mead's translated tractate text and is not presented as one of the tractates.
- The tractate files are formatted drafts. They have not yet been collated line by line against the 1906 printed edition.

**Assessment:** The 15 tractate bodies are represented from the selected repository transcription, with a source-level gap in Tractate XV. The supplementary *Perfect Sermon* is not complete. The files should not be labelled a fully verified edition yet.

## 2. 1 Enoch — source compilation attributed to Charles/Dillmann (1893)

**Reading index:** [1 Enoch](./books/book-of-enoch-charles-1893/README.md)  
**Source:** `books_02/The Book of Enoch.txt` (duplicated byte-for-byte in `books_05/`)

- The selected source contains 108 1 Enoch chapter entries: 107 headings written as `Enoch N.` and one written as `Chapt 13.`.
- A normalized body-text comparison confirmed that all 108 chapter bodies are present in the six formatted files after layout normalization.
- The source contains 68 additional sections headed `Enoch Slavonic N.`; these belong to the separate Slavonic *Book of the Secrets of Enoch* (2 Enoch) and are excluded from the 1 Enoch files.
- The blessing sentence located before the source table of contents belongs at the opening of Chapter I; it has been moved into Chapter 1 in the reading file.
- The source transcription flattened most verse numbering. Verse structure has now been restored for Chapters I–XC. Book 1 contains 36 chapter bodies, Book 2 contains 35, Book 3 contains 11, and Book 4 contains 8; all 90 match the selected repository source after removal of inserted labels and editorial markup. Chapter LXXI is the final chapter of the Parables, titled “Two earlier Visions of Enoch,” and contains 17 verses in two visions (1–4 and 5–17). Charles's later 1912 text notes a lost passage between verses 13 and 14; the selected repository transcription has no corresponding wording, and none has been reconstructed. Chapter LXXV verse 5 is bracketed; Chapters LXXX and LXXXI are bracketed interpolations; Chapter XC verse 15 is bracketed as an interpolation. Chapter LXXXII preserves the printed numbering 1–12, 14, 14, 15–20. Chapter XCII has verses 1–5 restored and its chapter body checked after markup insertion. Chapter CVII has verses 1–3 restored with body text preservation checked. Chapter XCI and Chapters XCIII–CVI and CVIII remain chapter-only (Book 5 paragraphs are readability formatting, not verse structure).
- The six book divisions are inherited from the repository compilation. They are retained as source structure, not claimed as a new critical reconstruction.
- The six files contain the 1 Enoch reading text, not the entire 391-page 1893 Charles volume. The general and special introductions, critical and exegetical notes, appendices, and indices are not included.
- Textual collation against the 1893 scan is still outstanding. The source compilation's attribution is not proof that its wording is identical to the printed edition.

**Assessment:** Complete against the selected repository transcription at the chapter-body level; not yet complete at verse-structure level, not a reproduction of the entire 1893 scholarly volume, and not textually verified against the facsimile. The separate 2 Enoch material remains to be formatted as its own work.

## Release rule

Do not use “complete edition” or “verified transcription” in a title, badge, or catalog status until the relevant printed edition has been checked for:

- complete textual coverage;
- chapter and verse numbering;
- source divisions and headings;
- omissions, duplications, and OCR errors;
- notes, appendices, and other material included in the declared scope.

A project may still be described as **complete against its selected repository transcription** when that narrower check has passed and the limitation is stated clearly.
