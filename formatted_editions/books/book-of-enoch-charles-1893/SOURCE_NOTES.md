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
- Chapter divisions, verse labels, and source-marked interpolations have been restored through Chapter 108. Known source irregularities and editorial differences are documented rather than silently repaired: Chapter 16 lacks verse 3; Chapters 4 and 35 are unnumbered; Chapter 91 includes an interpolated verse 11 and retains verses 12–17 in the repository sequence; Chapter 106 retains the repository's sequence and its documented rearrangement note. The combined archive transcription duplicated Chapter 82 verse label 14; the formatted and modernized derivatives correct the first of those labels to 13, following the authentic 1893 printed text.
- A full normalized comparison of the original combined archive file against the six formatted reading files now passes **108/108 chapter bodies**. The comparison removes verse labels, Markdown/editorial markup, whitespace, and standalone page-number lines; it also accounts for the opening blessing relocated from the source preamble into Chapter 1. Seven embedded page-number artifacts (53–59) were removed from the formatted derivative in Chapters 91, 93, 96, 98, 100, 102, and 104 to restore an exact normalized match. The original archival source file was not modified. This verifies transfer from that selected archive file, not the accuracy of the transcription against the 1893 printing.
- The modern-language derivative is maintained separately at `modernized_editions/books/1-enoch-repository-transcription/`. Its 108 chapter files have been committed. A separate local audit tool now checks file coverage, verse-label sequences, and extreme source/adaptation word-count ratios. These mechanical checks do not replace a human semantic review. An assistant-led verse-by-verse comparison against the selected formatted source has now been completed for all 108 chapter files, with corrections and unresolved interpretations recorded in that derivative's `REVIEW_LOG.md`. This is not independent human approval; a second reviewer must still approve every chapter.
- Chapters 91–108 have a documented normalized body-transfer check (18/18), and the restoration log records the chapter-level verse restoration work. Any remaining contradictions between older log entries and later completion notes should be resolved by treating this note and the current audit report as the latest status, while preserving historical log entries as dated history.
- The exact textual lineage of the selected transcription remains unresolved. Direct sample comparison with the 1893 text layer shows wording differences. A complete line-by-line collation against every page of the 1893 facsimile remains outstanding. The 1893 contents label Section V as Chapters XCI–CIV, but the translation pagination continues through pp.265–308 and includes CV–CVIII after that literary unit. Charles distinguishes CV from XCI–CIV; identifies CVI–CVII as a Noachian fragment; and calls CVIII an independent final addition. These chapters are printed in the 1893 volume and must not be described as absent from it. Appendix E separately prints a Latin fragment of CVI.1–18 on pp.372–375; that Latin witness is distinct from the Ethiopic translation on pp.302–304. A Charles/Oesterley 1917 witness, reprinting Charles's 1912 second edition, remains useful as a parallel structural witness for CV–CVIII, including the transposition of CVI.17, but is not the sole source for their presence in the 1893 volume. Visual collation of the 1917 scan remains outstanding.
- This directory contains the Enoch narrative reading text, not the complete 391-page 1893 scholarly volume. The general and special introductions, critical and exegetical notes, appendices, Greek and Latin fragments, and indices are outside this edition's declared scope.
- The combined repository input contains 68 Slavonic sections belonging to 2 Enoch. Those are excluded from 1 Enoch and are addressed by the separate [2 Enoch formatted edition](../book-of-the-secrets-of-enoch-morfill-1896/README.md).

**Current status:** chapter coverage and structural restoration are complete against the selected repository transcription. An assistant-led first-pass semantic review of all 108 chapters is logged; independent human approval remains pending. The authentic 1893 searchable text-layer and critical-apparatus pass is now documented sequentially for Chapters 1–104; it is not a systematic word-by-word collation of all manuscript variants and not page-image proofing. A separate 1917 text-layer comparison for Chapters 105–108 is documented in `SOURCE_COLLATION_LOG.md`. Full page-image collation of the 1893 witness (Chapters 1–104),  visual collation of the complete 1917 witness for Chapters 105–108, and identification of the selected repository transcription's exact lineage remain outstanding. The user-attached 101-page 1917 PDF ends at 107:3 and cannot serve as a visual witness for Chapter 108.
  
## Bibliographic references

- [Initial source-collation log](./SOURCE_COLLATION_LOG.md), including the 1893 section scope and outstanding verification work.
- [Digitized 1893 Clarendon Press edition (PDF)](https://upload.wikimedia.org/wikipedia/commons/1/1d/The_book_of_Enoch._August_Dillmann%2C_Robert_Charles._1893_%28IA_bookenochtransl00dillgoog%29.pdf)
- [Open Library record for the 1893 edition](https://openlibrary.org/works/OL16305356W/The_book_of_Enoch)
- [Wikisource transcription of Charles's translation](https://en.wikisource.org/wiki/The_Book_of_Enoch_%28Charles%29)

These references establish the historical edition and provide comparison material. They do not prove that the supplied repository transcription was taken directly from the 1893 printing.


## Repository PDF provenance audit — 25 November 2026

The `pdfs/enoch-editions/` directory contains eight PDFs: two older project transcriptions and five digitized scans/editions. The older files should not be represented as facsimiles; the historical scans are the page-image witnesses, with their distinct editions and limitations described in the PDF inventory.

| Repository file | Git blob SHA | Size | Provenance and role |
|---|---|---:|---|
| `enoch-1893-charles-dillmann.pdf` | `398352f3010cd7f059c91a24e8c32b9f8b1539a6` | 540,432 bytes | Modern 66-page composite/re-typeset compilation, integrating 1 Enoch and Slavonic 2 Enoch / later material. It is not the 1893 Clarendon volume. |
| `enoch-1893-clarendon-original.pdf` | `38be2b5e0e95779f92dcb19a745fc654b010b711` | 16,777,301 bytes | New large scan identified by the repository commit as the Cornell/Internet Archive 1893 Clarendon original (428 scanned pages). The external catalog and title page independently identify the Cornell-held Oxford Clarendon Press edition of 1893. Use this PDF for the 1893 page-image audit. |
| `enoch-1917-charles-oesterley.pdf` | `9bd830eafb560890c6c78d2f89d828b603d6a979` | 438,198 bytes | 101-page Word/PDFMaker 2005 transcription, not a 1917 facsimile. It ends after 107:3 and has no Chapter 108. |
| `enoch-1917-spck-original.pdf` | `80523ea72dfed5c4159dce85420e9ab1496dd3d4` | 7,051,515 bytes | New full SPCK scan described in the repository commit as a 160-page Claremont scan. The scanned copy identifies itself as the tenth impression (1962), first published in 1917; its preface says it reprints Charles's 1912 second edition. Use it as the page-image witness to the 1917 textual edition, while accurately describing the scanned physical impression as 1962. |

### Historical publication and scan notes

- **1893:** The Cornell/Internet Archive catalogue record identifies the scan as *The Book of Enoch*, Oxford: Clarendon Press, 1893, Internet Archive identifier `cu31924014590545`. The scanned title page names R. H. Charles and the Clarendon Press. The original historical volume's main translated text covers Chapters 1–104. Appendix E separately contains a New Latin fragment (106:1–18); it does not supply a complete Chapter 105–108 translation.
- **1917:** The full SPCK edition includes Chapters 105–108. The newly added repository PDF is a scan of a later 1962 impression, not the first impression of 1917. The preface indicates that the translation reprints Charles's 1912 second edition.
- The repository files' blob hashes and byte sizes are supplied to identify the precise current artifacts. No byte-for-byte identity with external Wikimedia/Internet Archive files is claimed.

### Page-image review status

- **1893:** The new Cornell scan is now available inside this repository, but a systematic visual collation of printed pp. 55–308 remains outstanding. Earlier assistant-led sequential work used the searchable OCR and critical apparatus; it must not be described as full page-image proofing.
- **1917:** Printed pp. 150–154, including p. 152, have been visually inspected in the full SPCK scan. Printed p. 152 maps to zero-based PDF index 153 in the 160-page scan. The full scan's text layer for Chapters 105–108 has also been reviewed.
- The older 101-page project transcription ending at 107:3 is not evidence for the complete 1917 edition and cannot substitute for the full scan of Chapter 108.

### Editorial consequence

Continue to preserve the selected repository transcription in the formatted and modernized reading editions unless a deliberate, source-specific emendation is documented. Differences in wording, verse order, interpolation status, or witness readings belong in the collation log, not in silent harmonization.
