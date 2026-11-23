# Source and Editorial Notes

## Selected source

- **Repository path:** `books_02/The Book of Enoch.txt`
- **Duplicate path:** `books_05/The Book of Enoch.txt`
- **Blob SHA:** `8dd96699c7be48d2c00c34e0bf6df8069f492356`
- **Source size:** 257,424 characters in the fetched UTF-8 transcription
- **Source attribution:** The compilation identifies an Ethiopic/Geez 1 Enoch text with R. H. Charles and Professor Dillmann, dated 1893, and a separate Slavonic Enoch text attributed to Morfill/Sokoloff and Charles, dated 1896.

The bibliographic record for Charles's 1893 edition describes it as translated from Professor Dillmann's Ethiopic text, emended and revised using Ethiopic manuscripts and Greek and Latin fragments. The repository's short attribution line is therefore normalized in this edition to “R. H. Charles, based on Professor Dillmann's Ethiopic text.” This metadata correction does not claim that the repository transcription has been collated against the printed book.

## Why this source was selected

The source file explicitly identifies the historical 1893 Ethiopic edition. A second file, `books_01/Book-of-Enoch (screen).txt`, identifies a modern English translation associated with M. Knibb and was deliberately not used as the basis for a full-text derivative.

The repository has two identical copies of the selected combined text in `books_02/` and `books_05/`; their identical Git blob SHA confirms they contain the same stored content.

## Separation of 1 Enoch and 2 Enoch

The selected file combines two distinct works:

- **1 Enoch:** chapters 1–108, organized in six book divisions in this source compilation.
- **2 Enoch:** headings marked `Enoch Slavonic 1.` through `Enoch Slavonic 68.`, interspersed among the 1 Enoch chapters.

Only 1 Enoch chapters 1–108 are reproduced in this directory. The Slavonic sections are excluded. They should be handled as a separate edition, preferably using the dedicated Morfill 1896 source file already held in the repository.

## Extraction and formatting

- Each 1 Enoch chapter was located by its explicit `Enoch N.` heading; Chapter 13 is headed `Chapt 13.` in the source and was retained as Chapter 13.
- The chapter text ends at the next labelled 1 Enoch or Slavonic Enoch section.
- Slavonic sections are excluded rather than spliced into 1 Enoch.
- Standalone printed page numbers and source divider headings are removed.
- Hard-wrapped lines are rejoined within paragraphs.
- The opening sentence that appears before the source table of contents is preserved as an unnumbered prefatory statement in Book 1.
- No attempt has been made to modernize spelling, correct OCR, or reconstruct readings.

## Verification and rights

The underlying 1893 printed edition is identifiable through library catalog records. That does not by itself certify every line of the repository's combined transcription or the copyright status of every later-added editorial element. This derivative excludes the modern Knibb text and the combined source's non-1-Enoch Slavonic sections, and still requires collation with the historical facsimile. Confirm applicable rights before redistribution in any jurisdiction.
