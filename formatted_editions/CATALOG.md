# Formatted Editions Catalog

This catalog tracks derivative reading editions. The numbered `books_*` directories remain the untouched source archive.

| Work | Formatted path | Source file | Mode | Status | Notes |
|---|---|---|---|---|---|
| *Corpus Hermeticum* — all 15 tractates | [Open work index](./books/corpus-hermeticum-mead-1906/README.md) | `books_04/Corpus_Hermeticum_Mead_1906.txt` | Faithful formatted transcription | Formatted drafts | All 15 tractate bodies represented from the supplied transcription. Tractate XV has no §5 in that source. Two supplementary texts are included; the *Perfect Sermon / Asclepius* extract is partial. No facsimile collation yet. |
| *The Book of Enoch* (1 Enoch; source attributed to Charles/Dillmann, 1893) | [Open six-part reading draft](./books/book-of-enoch-charles-1893/README.md) | `books_02/The Book of Enoch.txt` | Faithful formatted transcription | Formatted drafts | All 108 1 Enoch chapter bodies match the selected repository transcription after layout normalization. Verse structure restored for all 108 chapters; all 108 chapter bodies match the selected repository transcription after markup removal. Chapter LXXI closes the Parables (two visions, 17 verses). Chapter LXXV v.5, Chapters LXXX–LXXXI, and Chapter XC v.15 retain their 1893 interpolation markings. Chapter LXXXII preserves the printed numbering sequence 1–12, 14, 14, 15–20. Chapters XCI–CVIII have verse restoration; Chapter XCI verse 11 is marked interpolation and 91:12–17 are noted as relocated after chapter 93 in Charles's printed order; Chapter CVI retains verse 17's numbering before 15–16 to note Charles's rearrangement; the missing Chapter CVII heading was restored. Chapters 91–108 passed final normalized body checks (18/18). All 15 Book 5 chapter bodies pass normalized source comparison. Verse restoration is structural, not a complete collation against the printed edition. The wording is not verbatim Charles 1893. The 68 Slavonic 2 Enoch sections are excluded for a separate edition. The full 1893 scholarly volume is not reproduced, and facsimile collation remains outstanding. |

## Processing queue

The following are candidates, not approvals to reproduce their full contents. Confirm the exact edition, OCR quality, source provenance, and rights before formatting.

| Candidate | Existing source path(s) | Initial action |
|---|---|---|
| *The Book of the Secrets of Enoch* (2 Enoch; Morfill/Charles, 1896) | [Open formatted draft](./books/book-of-the-secrets-of-enoch-morfill-1896/README.md) | `books_02/The Book of Enoch.txt`; standalone OCR in `books_05/` | Faithful formatted transcription | Formatted draft | Four reading files contain all 68 numbered sections. The sections are extracted from a combined transcription where markers are physically out of order/interleaved; an independent transfer audit is unresolved. No verses added; facsimile collation remains outstanding. |
| *The Gospel of Thomas* | `books_03/The Gospel Of Thomas.txt`; `books_04/Gospel_of_Thomas.txt` | Compare the two source files and identify their translation/edition before selecting a text. |
| *The Book of Enoch* (1 Enoch) | `books_01/Book-of-Enoch (screen).txt`; `books_02/The Book of Enoch.txt`; `books_05/The Book of Enoch.txt` | Compare edition identities; do not merge translations or treat duplicate filenames as proof of identical text. |
| *The Rhind Mathematical Papyrus* | `books_02/Arnold Buffum Chace, Ludlow Bull, Henry Parker Manning - The Rhind Mathematical Papyrus. Volume II. Photographs, Transcription, Transliteration, Literal Translation. 2-Mathematical Association of Amer.txt`; `books_05/The_Rhind_Papyrus_Volume_1.txt` | Inspect volume/part identity; one listed source is empty. |
| *Vitruvius: Ten Books on Architecture* | `books_05/vitruviustenbook00vitruoft.txt` | Confirm translator and edition; format chapters/books without modernizing the translation. |

## Status definitions

- **Queued** — identified but not yet processed.
- **Formatting** — formatting work is in progress.
- **Formatted draft** — a first formatting pass exists; textual verification remains.
- **Verified** — checked against the stated edition or a reliable facsimile.
- **Needs source** — provenance, completeness, or source quality is insufficient.
- **Rights review** — reuse or redistribution status is unresolved.

## Collection observations

The source collections contain repeated works, alternate translations, near-duplicates, incomplete scans, OCR artifacts, and zero-byte placeholders. A candidate must be checked by content and edition metadata, not filename alone.
