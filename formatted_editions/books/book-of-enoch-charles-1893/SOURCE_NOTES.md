# Source and Editorial Notes

## Selected source

- **Repository path:** `books_02/The Book of Enoch.txt`
- **Duplicate path:** `books_05/The Book of Enoch.txt`
- **Blob SHA:** `8dd96699c7be48d2c00c34e0bf6df8069f492356`
- **Source size:** 257,424 characters in the fetched UTF-8 transcription
- **Attribution printed in compilation:** an Ethiopic/Geez text associated with R. H. Charles and Professor Dillmann (1893), combined with a separate Slavonic Enoch translation attributed to Morfill/Sokoloff and Charles (1896).

The historical title page confirms that R. H. Charles edited a 1893 work translated from Professor Dillmann's Ethiopic text. However, the wording in the selected repository transcription is not identical to the printed 1893 text. It must not be described as a verbatim Charles 1893 transcription until its precise textual source is identified.

## Direct comparison against the 1893 printing

A comparison was made against the digitized Clarendon Press 1893 edition:

- In Chapter I, verse 2, the printed edition begins with a form equivalent to “And Enoch answered and spake—(Enoch) a righteous man”; the repository source has different wording (“Enoch answered and spoke: I, Enoch, a righteous…”).
- Chapter II also has word and grammatical differences (for example, the printed edition uses “ye” where the repository source uses “you”).
- The printed Chapter III includes a seasonal parenthetical that is absent from the repository source.

These are textual differences, not just formatting changes. The repository wording has been retained; the 1893 printing is used here as a reference for structure only. Do not merge the printed edition's words into this source without opening a separate edition and documenting the change.

## Separation of 1 Enoch and 2 Enoch

The selected file combines two distinct works:

- **1 Enoch:** chapter entries 1–108, organized in six divisions in this source compilation.
- **2 Enoch:** headings marked `Enoch Slavonic 1.` through `Enoch Slavonic 68.`, interspersed among the 1 Enoch chapters.

Only 1 Enoch is reproduced in this directory. The Slavonic sections are deliberately excluded and should be handled as a separate edition, preferably using the dedicated Morfill 1896 source file already held in the repository.

## Extraction and formatting

- All 108 1 Enoch chapter entries were located: 107 headings written as `Enoch N.` and one written as `Chapt 13.`.
- Each chapter body ends at the next labelled 1 Enoch or Slavonic Enoch section.
- Slavonic sections are excluded rather than spliced into 1 Enoch.
- Standalone printed page numbers and source divider headings are removed.
- Hard-wrapped lines are rejoined within paragraphs.
- The opening blessing sentence in the compilation was placed at the start of Chapter I as the first-unit equivalent. Its wording is preserved from the compilation and is not a verbatim quote from Charles's 1893 printing.
- For Chapters 1–36, verse labels follow the chapter/verse structure in Charles's 1893 printing (printed pp. 57–105). Chapter IV and Chapter XXXV are unnumbered units in that printing, so no verse number has been invented. Chapter VIII verses 1–3, Chapter IX verse 7, and Chapter X verses 1–3 are bracketed in the 1893 printing as interpolations; the reading file preserves those brackets on the verse labels.
- For Chapters 37–71, verse labels follow Charles's chapter/verse structure. The editor's interpolation markers have been preserved: XXXIX.1–2; XLI.3–8; XLIII; XLIV; L; LIV.7–LV.2; LVI.5–LVII.3a; LIX; LX; and LXV–LXIX.25. The complete chapter bodies for XXXVII–LXXI were compared with the selected repository source after removal of structural markup; all 35 matched.
- Chapter LXXI is part of the Parables, under the heading “Two earlier Visions of Enoch.” Its 17 verse divisions are restored, with verses 1–4 forming the first vision and verses 5–17 the second.
- Charles's later 1912 text records a lost passage between verses 13 and 14. The selected repository transcription has no corresponding passage; it is not reconstructed here. This later-edition note remains a collation issue for the 1893 printing.
- Chapters LXXII–CVIII have now had verse boundaries restored in the six formatted reading files. The restoration uses Charles's printed 1893 structure for the earlier chapters and documented later structural references where recorded in the restoration log. This structural work does not establish that the repository wording is verbatim Charles 1893.
- No spelling or wording has been silently modernized or repaired in the formatted derivative.

## Completeness and verification

- All 108 1 Enoch chapter entries from the selected repository transcription are represented in the six formatted reading files.
- Chapter divisions, verse labels, and source-marked interpolations have been restored through Chapter 108. Known irregularities are preserved rather than silently repaired: Chapter 16 lacks verse 3; Chapters 4 and 35 are unnumbered; Chapter 82 is numbered 1–12, 14, 14, 15–20; Chapter 91 includes an interpolated verse 11 and retains verses 12–17 in the repository sequence; Chapter 106 retains the repository's sequence and its documented rearrangement note.
- The prior normalized transfer checks recorded in the restoration log cover the chapter bodies against the selected repository transcription. These checks validate transfer/structure only; they do not prove semantic equivalence with the 1893 printing.
- The modern-language derivative is maintained separately at `modernized_editions/books/1-enoch-repository-transcription/`. Its 108 chapter files have been committed. A separate local audit tool now checks file coverage, verse-label sequences, and extreme source/adaptation word-count ratios. These mechanical checks do not replace a human semantic review.
- Chapters 91–108 have a documented normalized body-transfer check (18/18), and the restoration log records the chapter-level verse restoration work. Any remaining contradictions between older log entries and later completion notes should be resolved by treating this note and the current audit report as the latest status, while preserving historical log entries as dated history.
- The exact textual lineage of the selected transcription remains unresolved. Direct sample comparison with the 1893 facsimile shows wording differences. A complete line-by-line collation against every page of the 1893 facsimile remains outstanding.
- This directory contains the Enoch narrative reading text, not the complete 391-page 1893 scholarly volume. The general and special introductions, critical and exegetical notes, appendices, Greek and Latin fragments, and indices are outside this edition's declared scope.
- The combined repository input contains 68 Slavonic sections belonging to 2 Enoch. Those are excluded from 1 Enoch and are addressed by the separate [2 Enoch formatted edition](../book-of-the-secrets-of-enoch-morfill-1896/README.md).

**Current status:** chapter coverage and structural restoration are complete against the selected repository transcription; source-to-adaptation semantic review and full historical facsimile collation remain pending.
  
## Bibliographic references

- [Digitized 1893 Clarendon Press edition (PDF)](https://upload.wikimedia.org/wikipedia/commons/1/1d/The_book_of_Enoch._August_Dillmann%2C_Robert_Charles._1893_%28IA_bookenochtransl00dillgoog%29.pdf)
- [Open Library record for the 1893 edition](https://openlibrary.org/works/OL16305356W/The_book_of_Enoch)
- [Wikisource transcription of Charles's translation](https://en.wikisource.org/wiki/The_Book_of_Enoch_%28Charles%29)

These references establish the historical edition and provide comparison material. They do not prove that the supplied repository transcription was taken directly from the 1893 printing.
