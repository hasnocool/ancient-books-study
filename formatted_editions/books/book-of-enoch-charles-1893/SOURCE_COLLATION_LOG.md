# 1 Enoch — Historical Source Collation Log

**Status:** Initial bibliographic and sample-text collation completed; full chapter-by-chapter collation remains open.  
**Primary reference:** R. H. Charles, ed., *The Book of Enoch: Translated from Professor Dillmann's Ethiopic Text* (Oxford: Clarendon Press, 1893).

## Primary facsimile and catalog records

- [1893 scanned PDF at Wikimedia Commons](https://commons.wikimedia.org/wiki/File:The_book_of_Enoch._August_Dillmann,_Robert_Charles._1893_(IA_bookenochtransl00dillgoog).pdf)
- [Open Library edition record](https://openlibrary.org/books/OL7109536M/The_book_of_Enoch)
- [Internet Archive item](https://archive.org/details/cu31924014590545)

The scanned title page identifies the Clarendon Press edition as 1893 and describes the work as translated from Professor Dillmann's Ethiopic text, emended and revised using additional Ethiopic manuscripts and Greek and Latin fragments. The preface says the translation was made mainly from a British Museum manuscript designated G and that the editor adopted variant readings from other manuscripts and fragments.

## Bibliographic structure observed in the 1893 contents

The scanned contents identify these main translation sections:

| Printed section | Chapters | Printed pages |
|---|---:|---:|
| I | 1–36 | 57–105 |
| II — The Similitudes | 37–71 | 110–186 |
| III — Book of Celestial Physics | 72–82 | 191–219 |
| IV — Dream-Visions | 83–90 | 223–259 |
| V | 91–104 | 265–308 |

The same contents list additional material outside the main translation sections, including Appendix D (additional notes on Chapters 37–108) and Appendix E (the New Latin fragment, Chapter 106:1–18). The existence of notes or a fragment referring to a chapter does not by itself establish that the complete chapter appears in the main 1893 translation.

**Editorial consequence:** Do not claim that the 1893 main translation supplies the complete text or verse structure for Chapters 105–108. The repository's later chapters and their structural numbering must be attributed to the later reference edition actually used, as recorded in the verse-restoration log. Keep the original source sequence, but do not conflate it with the 1893 printed arrangement.

## Repository-source transfer verification

A normalized body-text comparison was completed between the original combined repository transcription at `books_02/The Book of Enoch.txt` and the six formatted 1 Enoch reading files.

- **Result: 108/108 chapter bodies match exactly** after normalizing whitespace and line wrapping, removing standalone page-number lines, stripping verse labels and Markdown/editorial markup, and restoring the opening blessing sentence from the source preamble to its documented Chapter 1 location.
- The comparison identified seven embedded page-number artifacts, numbered 53–59, within formatted Chapters 91, 93, 96, 98, 100, 102, and 104. These were removed from the formatted derivative only. The archival source transcription was left unchanged.
- The local validator now repeats this comparison through `python3 tools/compare_source_text.py` and includes token-level differences in its JSON report if a chapter no longer matches.

This is an **archival transfer check**, not a historical collation. It establishes that the formatted text preserves the selected combined repository transcription after documented layout cleanup. It does not establish that the selected transcription is accurate, complete, or verbatim Charles 1893.

## Sample textual comparison already established

The repository's selected combined transcription is not verbatim Charles 1893. The following examples are recorded in the existing source notes and corroborated by the searchable text layer of the 1893 scan:

| Location | 1893 reference observation | Repository transcription observation | Status |
|---|---|---|---|
| Chapter 1:2 | Begins “And Enoch answered and spake—(Enoch) a righteous man...” | Uses “Enoch answered and spoke: I, Enoch, a righteous...” | Wording differs |
| Chapter 2 | Uses the archaic second-person form “ye” in the printed text | Uses “you” in the repository transcription | Wording differs |
| Chapter 3 | Includes a seasonal parenthetical in the printed text | Corresponding parenthetical is absent from the repository transcription | Apparent omission |

These are sufficient to reject the description “verbatim Charles 1893 transcription.” They are not a full collation and do not identify the repository transcription's exact intermediate source.

## Separation of 1 Enoch and 2 Enoch

The 1893 preface describes the Slavonic Enoch as a distinct work that Charles hoped to publish separately, with a translation by W. R. Morfill. The repository's combined source interleaves 68 Slavonic Enoch sections with the 1 Enoch material. The 68 sections are therefore not to be merged into the 1 Enoch reading text. They belong in the separate 2 Enoch edition.

## Additional 1893 text-layer spot comparisons

The Cornell / Internet Archive scan of the same 1893 Clarendon Press edition was used as a second searchable witness. Its scan metadata identifies the 1893 Oxford publication and Cornell holdings. Page-image capture of this second PDF was also rejected by the web screenshot service because the 11.09 MB PDF exceeded the service's size limit; the following are therefore text-layer comparisons, not visual proofreading.

| Chapter / verse | Printed page | 1893 text-layer reading | Repository/adaptation comparison |
|---|---:|---|---|
| 1:2 | 57 | Opens “And Enoch answered and spake—(Enoch) a righteous man…” | The selected archive's wording instead begins “Enoch answered and spoke: I, Enoch…”. This is a substantive person/voice difference, not just spelling. The adaptation follows the selected archive source. |
| 2:1 | 59 | Describes the luminaries as not deviating from their orbits and rising/setting “each in its season” | The modernized text follows the selected archive's plainer description of the appointed courses. |
| 2:2 | 59 | Addresses the reader as “Behold ye the earth…” and describes God's work as appearing unvaryingly | The modernized text retains the injunction but updates the old second-person grammar and syntax. |
| 2:3 | 59 | Explicit parenthetical: “(in the winter season)” before describing the earth's water, clouds, dew, and rain | That seasonal parenthetical is absent from the selected repository transcription and modernized verse. It has not been silently supplied from the 1893 witness. |
| 3:1 | 60 | Begins “I observed and saw how (in the winter)…” before describing the trees | The selected archive does not retain that seasonal parenthetical; the modernized text follows the selected archive. |
| Chapter 4 (unnumbered) | 60 | Begins “And again I observed the days of summer…” and describes seeking shade from the sun's heat | The selected formatted source retains the same unnumbered summer passage; the modernized file correctly does not invent verse labels. |
| 5:1–9 | 61–62 | Nine numbered verses, including the “eternal execration” wording in verse 5 | The selected formatted source preserves the nine-verse sequence and key wording; the modernization is a language update, not a verbatim rendering. |
| 6:6 | 62–63 | “They descended in the days of Jared on the summit of Mount Hermon” | The repository and modernization use this 1893 printed reading. Charles's note explains that he follows the Greek; the Ethiopic text has “descended on Ardis,” identified as the summit of Hermon. This is a witness variant, not an error to silently harmonize. |
| 7:2 | 65 | “three thousand ells” | The adaptation retains **3,000 ells**. Charles's critical note on p. 65 says the number three thousand appears in the Gizeh Greek fragment but is absent from the Syncellus Greek. It is therefore a witness-specific reading, not a reading uniformly attested in both Greek fragments. |
| 7:5 | 65 | Lists sins against birds, beasts, reptiles, and fish, then eating one another's flesh and drinking blood | The modernization preserves that sequence; the detailed apparatus explains the phrase “one another's flesh” as possibly referring to conflict among different classes of giants. |
| 8:1–3 | pp. 66–67 | The printed verse labels are bracketed as an interpolation; v.4 is outside the brackets | Both formatted source and modernization retain the three-unit interpolation boundary; no additional verse is bracketed. |
| 9:1 | p. 67 | Names “Michael, Gabriel, Surjan and Urjan” | The adaptation preserves the repository forms Surjan and Urjan. The 1893 note says these are variants of Suriel and Uriel, and suggests Raphael may be preferable to Surjan in accordance with the Greek. This remains a witness/onomastic question, not a correction to make silently. |
| 9:7 | p. 70 | Square-bracketed statement concerning Semjaza's authority and enchantments | The formatted source and modernization both mark this as an interpolation. |
| 9:3 | pp. 67–68, critical note p. 70 | Printed translation: “the souls of men”; Charles's note proposes “the spirits of the souls” | The modernization follows the selected repository reading (“souls of human beings”) and does not silently apply Charles's critical emendation. Record this as a witness/apparatus variant for independent review. |
| 9:6 | p. 69, critical note p. 70 | Verse text is printed without square brackets; the critical note says “All interpolation from the same source as vii. 3–8; viii. 1–3” | Preserve the printed verse-label markup in the formatted derivative, but record that the apparatus characterizes the verse as interpolated. This is distinct from the separately square-bracketed 9:7. |
| 10:1–3 | pp. 70–71 | The Noah instruction to Lamech appears with square-bracketed verse numbers | The formatted source and modernization preserve the three-verse interpolated block. |
| 10:7 | p. 72 | “Heal the earth which the angels have defiled…” appears as an ordinary numbered verse in the printed text | The formatted source and modernization do not add an interpolation marker to this verse. This distinction is kept separate from 10:1–3. |
| 13:1 | 79 | “(Rufael) shall put thee in bonds” | The modernization preserves the source form **Rufael**. |
| 14:11 | 81 | The printed text's apparatus gives the literal gloss “and their heaven was water” | The modernization retains the water image rather than recasting it as a sea above the scene. |

The 1893 section introduction itself warns that Section I is composite and contains extensive interpolations. That editorial context reinforces the need to preserve brackets and witness-specific readings instead of silently harmonizing them.


Additional selected readings were checked against the searchable text layer of the digitized 1893 Clarendon Press scan. This is **text-layer collation only**: it is not visual page-image proofing and it is not a complete chapter-by-chapter collation.

| Chapter / verse | 1893 printed reference | Text-layer reading checked | Editorial observation |
|---|---:|---|---|
| 20:3–4 | pp. 91–92 | Rufael is over human spirits; Raguel “takes vengeance on the world and on the luminaries” | Confirms the angel names and the vengeance role retained in the modernization. |
| 22:11 | p. 95 | “punishment and torture of the revilers for ever, and vengeance for their souls” | Confirms the source's difficult term **revilers** and the separate vengeance clause. The modernized verse now retains both. |
| 46:1 | p. 127 | “And there I saw One who had a head of days, and His head was white like wool” | The adaptation now retains the lower-case phrase “one who had a head of days,” avoiding an unsupported title decision. Whether the phrase functions as a formal title remains open for independent review. |
| 65:6 | p. 170 | “all the violence of the Satans and all their hidden power” | Confirms that “Satans” is the 1893 wording; the modernization retains the term and gives an explanatory gloss. |

The searchable scan text also exposes the edition's own critical apparatus and variant readings. A search hit is not a substitute for reading the complete printed context, and the quoted page references still require page-image proofing.

## Later witness for Chapters 105–108

The 1893 contents do not list Chapters 105–108 as a main translation section. A separately identified witness is now available:

- **Printed witness:** R. H. Charles, *The Book of Enoch*, with an introduction by W. O. E. Oesterley (London: SPCK, 1917).
- **Edition statement:** The 1917 front matter says the translation is reprinted from Charles's second edition of *The Book of Enoch* (1912). A 1962 impression is represented by Project Gutenberg eBook 77935.
- **Digital text:** [Project Gutenberg eBook 77935](https://www.gutenberg.org/ebooks/77935) and its [HTML transcription](https://www.gutenberg.org/files/77935/77935-h/77935-h.htm).
- **Scan comparator:** [1917 SPCK scan on Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/c/c9/The_book_of_Enoch._Robert_Charles._1917_%28IA_bookofenoch0000unse%29.pdf).

The 1917 introduction classifies Chapter CV (105) as a two-verse section of uncertain date, Chapters CVI–CVII (106–107) as the “Fragment of the Book of Noah,” and Chapter CVIII (108) as an appendix. It also states that the reprinted translation is that of Charles's 1912 second edition. This is a much better-defined witness for comparison than an unattributed assumption that these chapters belong to the 1893 main translation.

A verse-by-verse comparison of the available 1917 text layer for Chapters 105–108 confirms:
- 106:3 retains the newborn's opening of his mouth and his conversation with the Lord of Righteousness;
- 106:16 says that Noah's three children are saved with him;
- 107:1–3 form the three-verse concluding Noah-fragment unit;
- 108 is presented as an appendix-like closing book.

The modernization corrections to 106:3 and 106:16 preserve these source details. Chapter 107:3 has also been adjusted to retain the repository source's “cause the earth to rejoice in compensation for all the destruction” wording, rather than borrowing the later witness's shorter “comfort the earth” phrasing.

**Status:** A verse-by-verse comparison of all 105–108 source units against the searchable 1917 text layer is now complete. This remains text-layer collation, not visual page-image proofing. The following differences are explicitly retained rather than silently blended:

- **Chapter 105:** Both witnesses have two verses. The adaptation follows the repository transcription, retaining its “in those days” introduction and its singular “guide” wording rather than silently switching to the 1917 “the Lord bade (them)” and plural “guides.”
- **Chapter 106:** The 1917 text places verse 17 immediately after verse 14, then resumes verses 15–16, 18–19. The repository-formatted source places verses 15, 16, 17, 18, 19 in numerical order. The modernized file follows the repository source order and preserves the verse numbers; it does not import the 1917 rearrangement.
- **Chapter 106:3 and 106:16:** The 1917 text confirms “conversed with the Lord of righteousness” and “his three children.” The modernization retains both details.
- **Chapter 107:3:** The repository transcription says Noah will “cause the earth to rejoice in compensation for all destruction”; the 1917 witness says “he will comfort the earth after all the destruction.” The adaptation retains the repository-specific wording.
- **Chapter 108:3:** The repository has “the books of the holy ones”; the 1917 text has “the holy books.” The adaptation follows the repository wording.
- **Chapter 108:4:** The repository's “I could not look thereon” is now rendered “I could not look upon it,” avoiding the stronger interpretation “could not see through it.”

The 1917 front matter explicitly identifies the text as a reprint of Charles's 1912 second edition. It is therefore a separately identified witness for this comparison, not proof of the 1893 main translation wording. Do not label Chapters 105–108 “1893 Charles main text.”

The 1917 edition also preserves a different placement for the Apocalypse of Weeks material associated with Chapter 91. Its editorial arrangement places 91:12–17 after the material now numbered 93:1–10, rather than keeping those six verses in the Chapter 91 sequence. The modernized edition deliberately follows the selected repository transcription: Chapter 91 remains in its repository sequence, with 91:11 marked as interpolation and 91:12–17 left in place. This is a documented witness/arrangement variant, not a silent correction. The chapter files must therefore be described as a repository-sequence modernization, not as a reproduction of the 1917 order.

## 1917 witness cross-check of the Chapter 72 cycle counts

The 1917 Charles/Oesterley text layer was also checked for the repeated solar-cycle wording in Chapter 72. It reads “one and thirty mornings” at verses 13, 19, 25, and 31, and “thirty mornings” at verse 29. The modernized Chapter 72 now follows that pattern: 31 mornings at 13, 19, 25, and 31; 30 mornings at 29.

This is corroboration from the explicitly identified 1917 reprint of Charles's 1912 second edition. It is **not** cited as proof of what the 1893 printing says, and it does not replace a page-image collation of the 1893 Chapter 72.

## Scan inspection limitation

The accessible 1893 PDF text layer could be searched and opened, but the available page-image screenshot service rejected both accessible 1893 scan PDFs because their file sizes exceeded its capture limit. The text-layer samples above are therefore not described as visually proofread. A local download or smaller page-image segments will be needed for image-level collation.

## Collation procedure

A full collation must proceed in bounded batches and record evidence per chapter:

1. Identify the correct printed witness and printed page range for the chapter.
2. Compare chapter headings, verse divisions, ordering, interpolation brackets, and paragraph boundaries.
3. Compare each verse body against the repository source; do not silently replace repository wording with Charles wording.
4. Classify every difference as spelling/typography, OCR/transcription, lexical variant, omission, addition, relocation, or unresolved.
5. Record short evidence excerpts, printed page, repository chapter/verse, and decision.
6. If using 1912 or 1917 Charles material for a chapter absent or structurally different in 1893, identify it as a separate witness and do not label it 1893.
7. Mark the chapter as collated only after every verse and any relevant apparatus have been checked.

A PDF text layer is a search aid, not a substitute for checking the scanned page image where readings are uncertain. The initial online PDF page-image capture attempt was blocked by the provider's file-size limit; no scan image is claimed to have been visually reviewed in this pass.

## Open work

- [ ] Identify the exact source and lineage of the repository's combined transcription.
- [ ] Collate Chapters 1–36 against 1893 pages 57–105.
- [ ] Collate Chapters 37–71 against 1893 pages 110–186.
- [ ] Collate Chapters 72–82 against 1893 pages 191–219.
- [ ] Collate Chapters 83–90 against 1893 pages 223–259.
- [ ] Collate Chapters 91–104 against 1893 pages 265–308.
- [x] Compare Chapters 105–108 verse by verse against the explicitly identified 1917 Charles/Oesterley text layer; differences and the Chapter 106 rearrangement are recorded above.
- [ ] Visually collate Chapters 105–108 against the 1917 scan page images; do not infer them from the 1893 appendices.
- [ ] Record textual variants and interpolation boundaries without silently normalizing them.
- [ ] Have a second reviewer check unresolved or consequential readings.

**Current conclusion:** The source-attributed reading edition is a complete chapter-body transfer of the selected repository transcription according to the repository's recorded checks. It is not a verbatim Charles 1893 transcription, not a facsimile-verified critical edition, and not a reproduction of the complete 1893 scholarly volume.
