# Source and Editorial Notes

## Selected source

- **Repository path:** `books_02/The Book of Enoch.txt`
- **Duplicate path:** `books_05/The Book of Enoch.txt`
- **Blob SHA:** `8dd96699c7be48d2c00c34e0bf6df8069f492356`
- **Source size:** 257,424 characters in the fetched UTF-8 transcription
- **Source attribution:** The compilation identifies an Ethiopic/Geez 1 Enoch text associated with R. H. Charles and Professor August Dillmann, dated 1893, and a separate Slavonic Enoch text associated with Morfill/Sokoloff and Charles, dated 1896.

The 1893 title page identifies the work as translated from Professor Dillmann's Ethiopic text and edited by R. H. Charles. The repository compilation's shorter attribution line is not enough to establish that every line of its transcription is identical to the 1893 printing. The edition attribution is therefore recorded as source-provided metadata, pending collation.

## Why this source was selected

The source file explicitly identifies the historical 1893 Ethiopic edition. A second file, `books_01/Book-of-Enoch (screen).txt`, identifies a modern English translation associated with M. Knibb and was deliberately not used as the basis for this derivative.

The repository has two identical copies of the selected combined text in `books_02/` and `books_05/`; their identical Git blob SHA confirms they contain the same stored content.

## Separation of 1 Enoch and 2 Enoch

The selected file combines two distinct works:

- **1 Enoch:** chapter entries 1–108, organized in six divisions in this source compilation.
- **2 Enoch:** headings marked `Enoch Slavonic 1.` through `Enoch Slavonic 68.`, interspersed among the 1 Enoch chapters.

Only 1 Enoch is reproduced in this directory. The Slavonic sections are deliberately excluded and should be handled as a separate edition, preferably using the dedicated Morfill 1896 source file already held in the repository. Thus this directory is complete only for the 1 Enoch chapter text represented in the selected source; it is not a rewrite of every work contained in that combined source file.

## Extraction and formatting

- All 108 1 Enoch chapter entries were located: 107 headings written as `Enoch N.` and one source heading written as `Chapt 13.`.
- Each chapter body ends at the next labelled 1 Enoch or Slavonic Enoch section.
- Slavonic sections are excluded rather than spliced into 1 Enoch.
- Standalone printed page numbers and source divider headings are removed.
- Hard-wrapped lines are rejoined within paragraphs.
- The opening blessing sentence occurs before the source table of contents. In the 1893 printed structure it belongs at the start of Chapter I, so the reading edition now places it inside Chapter 1 rather than treating it as front matter.
- The repository transcription does not preserve the complete verse numbering of the printed edition. Chapter headings are retained, but verse numbers and boundaries are not invented. A verse-level edition requires collation against the original printing.
- No attempt has been made to modernize spelling, silently correct OCR, or reconstruct missing readings.

## Completeness and verification

A normalized comparison was performed between the 108 chapter bodies in the selected repository transcription and the 108 chapter bodies in the formatted files. All 108 matched after normalization for whitespace, standalone page numbers, and source divider labels. This verifies transfer from the selected transcription; it does **not** establish that the selected transcription itself is complete or textually identical to the 1893 printed edition.

The complete 1893 volume contains substantially more than the translated chapter text: it includes general and special introductions, critical and exegetical notes, appendices, and indices. Those scholarly materials are outside the scope of this reading-text draft. The historical scan still needs page-by-page collation before the text can be labelled verified.

## Bibliographic cross-check

- [Open Library record for the 1893 edition](https://openlibrary.org/works/OL16305356W/The_book_of_Enoch) identifies the work as *The Book of Enoch* (1893), associated with R. H. Charles and August Dillmann.
- [Wikisource transcription of the Charles translation](https://en.wikisource.org/wiki/The_Book_of_Enoch_%28Charles%29) provides a chapter-by-chapter comparison reference.
- A [digitized 1893 scan](https://upload.wikimedia.org/wikipedia/commons/1/1d/The_book_of_Enoch._August_Dillmann%2C_Robert_Charles._1893_%28IA_bookenochtransl00dillgoog%29.pdf) is available for facsimile collation.

These references identify the historical edition and comparison material. They do not substitute for checking the repository transcription line by line against the scan.
