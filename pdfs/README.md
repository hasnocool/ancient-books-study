# 1 Enoch source PDFs

This directory now contains **seven PDFs**. They are not interchangeable: several are modern transcriptions, three are full digitizations of the 1893 edition, one is a separate revised 1912 edition, and one is the later SPCK witness. **Do not cite a filename alone as proof that a file is a historical facsimile.**

## File inventory

| File | Repository size | Bibliographic / evidentiary role |
|---|---:|---|
| [`enoch-1893-charles-dillmann.pdf`](./enoch-1893-charles-dillmann.pdf) | 540,432 bytes | Older 66-page modern composite/re-typeset artifact. It combines 1 Enoch with Slavonic 2 Enoch and later material. It is not a photographic scan of the 1893 Clarendon volume. |
| [`enoch-1893-clarendon-original.pdf`](./enoch-1893-clarendon-original.pdf) | 16,777,301 bytes | Cornell / Internet Archive scan of the 1893 Clarendon edition; 428 scanned pages. The catalogue/title page identifies R. H. Charles, Oxford: Clarendon Press, 1893. |
| [`enoch-1893-opusmagnum.pdf`](./enoch-1893-opusmagnum.pdf) | 11,632,626 bytes | Additional OpusMagnum-hosted full scan of the 1893 Clarendon edition; the addition commit identifies 420 pages. Its PDF text layer identifies the 1893 title page and the translation's printed-page range (57–308). It is the most promising smaller candidate for image proofing, but page screenshots from this environment still returned cache misses; it has **not** yet supplied inspected translation-page pixels. The scan's exact lineage relative to the other digitizations has not been established. |
| [`enoch-1893-utoronto.pdf`](./enoch-1893-utoronto.pdf) | 34,951,905 bytes | University of Toronto / Knox College scan of the 1893 Clarendon edition; the addition commit identifies 424 scanned pages. This is the local copy of the Toronto-held witness previously identified through the Knox/Luminist record. |
| [`enoch-1912-clarendon-2nd-edition.pdf`](./enoch-1912-clarendon-2nd-edition.pdf) | 30,939,230 bytes | University of Toronto / Robarts scan of Charles's revised second edition, Oxford: Clarendon Press, 1912; 454 scanned pages. It is a distinct edition, not another 1893 scan. Useful as an additional textual witness for the later Noah material and Chapter 108, but not a substitute for the SPCK 1917 page images. |
| [`enoch-1917-charles-oesterley.pdf`](./enoch-1917-charles-oesterley.pdf) | 438,198 bytes | Older 101-page Word/PDFMaker transcription created in 2005, not a scanned 1917 impression. It ends after 107:3 and contains no Chapter 108. |
| [`enoch-1917-spck-original.pdf`](./enoch-1917-spck-original.pdf) | 7,051,515 bytes | Full SPCK scan described as 160 PDF pages. The scanned physical copy is the tenth impression (1962), and its title page says “First published in 1917.” Its preface identifies the translation as reprinted from Charles's 1912 second edition. Cite the textual edition as 1917, but identify the scanned physical impression as 1962. |

## Source scope and hierarchy

### 1893 Clarendon Press

The 1893 main translated text covers Chapters 1–104, printed pp. 57–308. The volume also contains extensive introduction, apparatus, appendices, and fragmentary material. Appendix E separately includes a New Latin fragment of 1 Enoch 106:1–18; that fragment is not a complete 1893 main-text edition of Chapters 105–108.

The Cornell, OpusMagnum, and University of Toronto PDFs are separate repository files of the same bibliographic edition. Their scan-page counts differ (428, 420, and 424 respectively); do not equate PDF page index with the printed page number. The 418-page University of Michigan / Google Books digitization is another external reference, not one of the seven files currently stored here.

Useful provenance records:
- [Cornell / Internet Archive record](https://archive.org/details/cu31924014590545), identifier `cu31924014590545`.
- [University of Michigan / Google Books scan record](https://archive.org/details/bookenochtransl00dillgoog), also described on [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:The_book_of_Enoch._August_Dillmann,_Robert_Charles._1893_(IA_bookenochtransl00dillgoog).pdf).
- [Knox College / University of Toronto edition record](https://openlibrary.org/books/OL7109536M/The_book_of_Enoch), Internet Archive identifier `thebookofenoch00unknuoft`.
- [OpusMagnum-hosted scan](https://opusmagnum.org/wp-content/uploads/2018/05/The-Book-of-Enoch-by-August-Dillman-1.pdf).

### 1912 Clarendon Press second edition

This is a revised and substantially recast edition, not a facsimile of the 1893 printing. The University of Toronto / Robarts copy is catalogued as a 454-page Internet Archive scan. Its contents identify Section V (Chapters 91–104), a separate fragment of the Book of Noah (Chapters 106–107), and Chapter 108 in a later section. It therefore provides a useful additional witness for portions of Chapters 106–108, but it does not supply Chapter 105 as a replacement for the 1917 text.

The scanned copy's title-page date is 1912. Its 454-page pagination is different from the 1893 and 1917 scans. See [Source Library's catalogue and page record](https://kloss.sourcelibrary.org/book/the-book-of-enoch-or-1-enoch-charles).

### 1917 SPCK textual edition

The 1917 Charles/Oesterley edition includes Chapters 105–108. The repository scan is a 1962 tenth impression of the edition first published in 1917; the preface explains that the translation reprints Charles's 1912 second edition. The distinction between publication date and the scanned physical copy matters for accurate citations.

External scan reference: [Internet Archive / Claremont scan](https://archive.org/details/bookofenoch0000unse).

## Visual verification status

- **1893:** The searchable text layer and critical apparatus have received a sequential assistant-led review for Chapters 1–104. The OpusMagnum PDF is now the preferred first candidate to test for visual proofing because it is a smaller 420-page scan and its contents confirm the printed translation range. The PDF text is accessible, but repeated page-image/screenshot attempts from this environment still returned cache misses. Printed pp. 55–308 are **not** visually verified.
- **1912:** The 454-page Robarts / University of Toronto scan is identified as the revised second edition. It has not yet been page-image proofed here. It is a supplementary textual witness, not a replacement for the 1917 edition.
- **1917:** Printed pp. 150, 151, 153, and 154 have been visually inspected in the full SPCK scan. Printed p. 152 remains an image-retrieval gap; in the 160-page scan it maps to zero-based PDF index 153. The searchable text layer for Chapters 105–108 has been reviewed.
- The older 66-page and 101-page PDFs remain preserved as project artifacts. They document previous project inputs, but they are not substitutes for the historical scans.
- The exact textual lineage of the selected combined repository transcription remains unresolved. Do not silently replace its wording with a reading from another edition; log each witness difference.

See [the historical-source collation log](../formatted_editions/books/book-of-enoch-charles-1893/SOURCE_COLLATION_LOG.md) and [the chapter review log](../modernized_editions/books/1-enoch-repository-transcription/REVIEW_LOG.md).
