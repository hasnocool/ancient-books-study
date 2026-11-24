# Completeness and Structure Audit

**Audit date:** 2026-11-23  
**Scope:** Three reading projects currently stored under `formatted_editions/books/`.

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
- The source transcription flattened most verse numbering. Verse structure has now been restored for Chapters I–CVIII. Book 1 contains 36 chapter bodies, Book 2 contains 35, Book 3 contains 11, and Book 4 contains 8; all 90 match the selected repository source after removal of inserted labels and editorial markup. Chapter LXXI is the final chapter of the Parables, titled “Two earlier Visions of Enoch,” and contains 17 verses in two visions (1–4 and 5–17). Charles's later 1912 text notes a lost passage between verses 13 and 14; the selected repository transcription has no corresponding wording, and none has been reconstructed. Chapter LXXV verse 5 is bracketed; Chapters LXXX and LXXXI are bracketed interpolations; Chapter XC verse 15 is bracketed as an interpolation. Chapter LXXXII preserves the printed numbering 1–12, 14, 14, 15–20. Verse labels are now present across Chapters I–CVIII, but two Charles-order rearrangements are documented and not applied: 91:12–17 remains in Chapter 91's numeric source position, and 106:17 remains before 106:15–16 (the repository source sequence matches Charles's rearrangement). This is a source-sequence formatted edition, not an exact reproduction of Charles's printed order. In the concluding section: XCII 1–5; XCIII 1–10 plus bracketed interpolation 11–14; XCIV 1–11; XCV 1–7; XCVI 1–8 with verse 2 bracketed; XCVII 1–10; XCVIII 1–16; XCIX 1–16; C 1–13; CI 1–9; CII 1–11; CIII 1–15; CIV 1–13; CV 1–2. Chapter XCI has verses 1–19, verse 11 marked interpolation; 91:12–17 are noted as relocated after chapter 93 in Charles's printed order. Chapter CVI has verses 1–19. Charles relocates verse 17 to follow verse 14; this formatted file retains the repository source order, so that printed rearrangement is not applied. CVII has verses 1–3. CVIII has verses 1–15. Final normalized chapter-body checks for Chapters 91–108 passed 18/18 after removal of verse labels, editorial markup, and layout artifacts; Chapter 107's missing heading was restored. Book 5 source-body comparison passed 15/15; OCR markers retained.
- The six book divisions are inherited from the repository compilation. They are retained as source structure, not claimed as a new critical reconstruction.
- The six files contain the 1 Enoch reading text, not the entire 391-page 1893 Charles volume. The general and special introductions, critical and exegetical notes, appendices, and indices are not included.
- Textual collation against the 1893 scan is still outstanding. The source compilation's attribution is not proof that its wording is identical to the printed edition.

**Assessment:** Complete against the selected repository transcription at the chapter-body and verse-structure formatting level; not a reproduction of the entire 1893 scholarly volume, and not textually verified against the facsimile. The separate 2 Enoch material remains to be formatted as its own work.

## 3. 2 Enoch — Morfill/Charles (1896)

**Reading index:** [2 Enoch](./books/book-of-the-secrets-of-enoch-morfill-1896/README.md)  
**Sources:** third-party manually collated USFM main text; repository standalone OCR for the appendix.

- Main text: 68 chapters / 360 numbered verses, plus a separate one-verse prologue. USFM blocks 2–69 map to Chapters 1–68; block 1 is the prologue.
- An automated sequence comparison against the cited USFM found all 68 chapter headings and 361 verse entries (prologue plus main text) in the four Markdown files. All 361 verse bodies matched the USFM text exactly after removal of verse labels and layout markup; no mismatches were found.
- Appendix audit: five sections, with 19 + 26 + 37 + 11 + 11 = 104 entries. Section III.31 is an explicitly bracketed manuscript variant and is counted separately; no verse number was silently inserted.
- The main text files were generated from the collated USFM source with chapter and verse markers retained. Verse numbering is continuous within each chapter.
- The appendix is separately included as sections I–V (104 verses), based on the repository standalone OCR. Its verse structure was checked against a clean retype; OCR wording has not been collated against page images.
- Appendix Section III verse 31 is marked as a manuscript variant. The source footnote notes it is not present in all manuscripts; the variant is retained.
- Appendix introduction is retained. OCR page-number lines 86–93 were removed, while standalone numerals in the text (e.g. 50, 100, 282) were preserved. A note on a variant of III.37 is moved to the end of the appendix file.
- Later retypes' chapter numbering 69–73 is not adopted; the 1896 appendix sections I–V are kept separate from the main 68 chapters.
- The third-party USFM source states it was collated and corrected by hand from two scans. This project has not independently verified the USFM against the facsimile, nor fully collated the appendix OCR.

**Assessment:** Coverage of the main 68 chapters and the five-section appendix is complete. The formatted edition is not yet a facsimile-verified transcription or critical edition.

## Release rule

Do not use “complete edition” or “verified transcription” in a title, badge, or catalog status until the relevant printed edition has been checked for:

- complete textual coverage;
- chapter and verse numbering;
- source divisions and headings;
- omissions, duplications, and OCR errors;
- notes, appendices, and other material included in the declared scope.

A project may still be described as **complete against its selected repository transcription** when that narrower check has passed and the limitation is stated clearly.


## Gospel of Thomas — Mattison public-domain translation

- Formatted edition: `books/gospel-of-thomas-mattison-public-domain/`.
- Coverage: prologue, all 114 sayings in numerical order, closing title, and separate translator's notes.
- Four reading files split at saying headings: 1–30, 31–60, 61–90, 91–114.
- Source: Mark M. Mattison's translation, explicitly dedicated to the public domain on Gospels.net. Transfer used a digital mirror identifying the Gospels.net source; this is not an independent facsimile or Coptic collation.
