# Formatted Editions Catalog

This catalog tracks derivative reading editions. The numbered `books_*` directories remain the untouched source archive.

| Work | Formatted path | Source file | Mode | Status | Notes |
|---|---|---|---|---|---|
| *Corpus Hermeticum* — all 15 tractates | [Open work index](./books/corpus-hermeticum-mead-1906/README.md) | `books_04/Corpus_Hermeticum_Mead_1906.txt` | Faithful formatted transcription | Formatted drafts | All 15 tractate bodies represented from the supplied transcription. Tractate XV has no §5 in that source. Two supplementary texts are included; the *Perfect Sermon / Asclepius* extract is partial. No facsimile collation yet. |
| *The Book of Enoch* (1 Enoch; source attributed to Charles/Dillmann, 1893) | [Open six-part reading draft](./books/book-of-enoch-charles-1893/README.md) | `books_02/The Book of Enoch.txt` | Faithful formatted transcription | Formatted drafts | All 108 1 Enoch chapter bodies match the selected repository transcription after layout normalization. Verse numbering is absent from that transcription; 68 Slavonic 2 Enoch sections are excluded for a separate edition. The full 1893 scholarly volume is not reproduced, and facsimile collation remains outstanding. |

## Processing queue

The following are candidates, not approvals to reproduce their full contents. Confirm the exact edition, OCR quality, source provenance, and rights before formatting.

| Candidate | Existing source path(s) | Initial action |
|---|---|---|
| *The Book of the Secrets of Enoch* (W. R. Morfill translation; R. H. Charles editor, 1896) | `books_05/The Book of the Secrets of Enoch translated from the Slavonic by W R Morfill 1896.txt` | Review the Cornell scan transcription and its OCR before creating an edition. The source file itself notes that the Cornell original has no known copyright restrictions in the United States; confirm applicable rights independently. |
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
