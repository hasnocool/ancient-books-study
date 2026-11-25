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
| 10:11 | p. 74, critical note p. 75 | The printed verse number is square-bracketed; the critical note explicitly says “This verse is an interpolation” | The formatted source and modernization now mark verse 11 as an interpolation. This is separate from the interpolated Noah block in 10:1–3 and from ordinary verse 10:7. |
| 13:1 | 79 | “(Rufael) shall put thee in bonds” | The modernization preserves the source form **Rufael**. |
| 14:11 | 81 | The printed text's apparatus gives the literal gloss “and their heaven was water” | The modernization retains the water image rather than recasting it as a sea above the scene. |
| 11:1–2 | p. 77 | The store chambers of blessing are in heaven and are sent down upon human labour; peace and justice are “wedded” through all generations | The modernization retains both units and updates “store chambers” and “wedded” without changing their sequence. |
| 12:1–6 | pp. 77–78 | Enoch is hidden; his activities concern the holy ones and Watchers; the Watchers address him as scribe and request an announcement of their sentence | The modernization retains the six-unit sequence and the Watchers' address. The 1893 commentary connects “hidden” with Enoch receiving the revelation, rather than implying that he had died or disappeared permanently. |
| 13:6 | p. 78 | “the prayer on behalf of their spirit” and deeds for which they seek “forgiveness, and forbearance” | The modernization was corrected to the singular “their spirit” and “forbearance,” avoiding pluralization and a narrowed “patience.” |
| 13:7 | p. 78 | Enoch sits at the waters of Dan “to the right (i.e. the south) of the west of Hermon” | The modernization now retains the directional detail as “south-west of Mount Hermon,” using the 1893 explanatory note for the orientation. |
| 13:9 | p. 79, textual note | Main text: the Watchers were “sitting together”; manuscript G reads “were talking” | The modernization follows the main printed reading “sitting together”; the alternative is recorded as a manuscript variant. |
| 14:4 | p. 80, textual note | The main text ends its sentence after the judgment and refusal of indulgence; manuscript G adds a sentence about friendship ending and judgment being passed | The modernization follows the main reading and does not silently import the G-only addition. |
| 14:18 | p. 80 | The throne's appearance is “as hoarfrost”; “its circuit” is “as a shining sun” | The modernization now preserves “circuit” rather than turning it into surrounding brilliance. |

The 1893 section introduction itself warns that Section I is composite and contains extensive interpolations. That editorial context reinforces the need to preserve brackets and witness-specific readings instead of silently harmonizing them.


Additional selected readings were checked against the searchable text layer of the digitized 1893 Clarendon Press scan. This is **text-layer collation only**: it is not visual page-image proofing and it is not a complete chapter-by-chapter collation.

| Chapter / verse | 1893 printed reference | Text-layer reading checked | Editorial observation |
|---|---:|---|---|
| 20:3–4 | pp. 91–92 | Rufael is over human spirits; Raguel “takes vengeance on the world and on the luminaries” | Confirms the angel names and the vengeance role retained in the modernization. |
| 22:11 | p. 95 | “punishment and torture of the revilers for ever, and vengeance for their souls” | Confirms the source's difficult term **revilers** and the separate vengeance clause. The modernized verse now retains both. |
| 46:1 | p. 127 | “And there I saw One who had a head of days, and His head was white like wool” | The adaptation now retains the lower-case phrase “one who had a head of days,” avoiding an unsupported title decision. Whether the phrase functions as a formal title remains open for independent review. |
| 65:6 | p. 170 | “all the violence of the Satans and all their hidden power” | Confirms that “Satans” is the 1893 wording; the modernization retains the term and gives an explanatory gloss. |

The searchable scan text also exposes the edition's own critical apparatus and variant readings. A search hit is not a substitute for reading the complete printed context, and the quoted page references still require page-image proofing.

## Expanded 1893 text-layer comparison: Chapters 91–104

A complete searchable text layer of the 1893 Clarendon Press volume is now accessible through the Internet Archive DjVu text rendition:

- **Witness:** R. H. Charles, *The Book of Enoch: Translated from Professor Dillmann's Ethiopic Text* (Oxford: Clarendon Press, 1893).
- **Digital text layer:** https://archive.org/stream/thebookofenoch00unknuoft/thebookofenoch00unknuoft_djvu.txt
- **Printed range for this section:** pp. 265–308 (Section V, Chapters 91–104).
- **Nature of check:** searchable text-layer comparison, including selected chapter text, printed verse units, and Charles's printed critical notes. This is not visual page-image proofreading and does not replace comparison with Ethiopic manuscripts or the Greek/Latin fragments.

### Textual findings confirmed from the 1893 witness

| Passage | 1893 printed reading / apparatus | Editorial consequence |
|---|---|---|
| 91:11 | The verse is printed as an interpolation. Charles's note calls it an interpolation added by the final editor and says it was used to introduce verses 12–19, which had been removed from their original context. | Retain 91:11 as marked interpolation; do not blend it with the preceding judgment narrative. |
| 91:12–19 | Charles's note says these verses should be read after 93:1–10, the account of the first seven weeks. The 1893 printed body retains the verse sequence under Chapter 91, but its apparatus explicitly recommends the earlier placement. | Record this as a Charles 1893 critical-order instruction. It is distinct from the 1917 printed layout, which physically places the 91:12–17 section after the 93 material. The repository modernization continues to follow the selected repository's numeric chapter order. |
| 92:1 | The 1893 text prints the full opening, “Written by Enoch the scribe, this complete doctrine of wisdom…,” without the long interpolation brackets found in the 1917 witness. | The repository's unbracketed 92:1 is consistent with the 1893 printed body on this point; preserve the 1917 difference as a separate witness variant. |
| 92:3 | The 1893 main text prints “the righteous one will arise from sleep, will arise and walk”; the note records MS G's alternative “wisdom will arise.” | Keep the repeated “will arise” in the 1893-based comparison; record the G alternative in the apparatus, not as a silent correction. The 1917 printing brackets the repetition, a later witness difference. |
| 93:1–10 | The 1893 text begins “And after that Enoch began to recount from the books,” followed by Enoch's speech about the children of righteousness and the weeks. | Preserve the two-part narrative transition and keep the repository's verse sequence. The modernized file's “He said” transition is a stylistic bridge; it should not be confused with a separate source verse. |
| 93:11–14 | The 1893 printed text encloses the four questions in square brackets; Charles's commentary says these verses are out of place in this section. | Retain all four units but visibly mark them as interpolation. Do not delete them from a complete transcription. |
| 94:1–11 | Charles says Chapter 94 followed 91:12–19 in the original text. The 1893 main text prints 94:7's gold-and-silver clause as ordinary, unbracketed text. | Retain repository sequence and its unbracketed 94:7 clause for the selected source; record the 1917 witness's later square brackets as a variant. |
| 95:1, 95:3 | The 1893 apparatus records a Greek G alternative for the water/cloud image in 95:1 and a wording variant around “your hands” / judgment according to desire in 95:3. | Keep the repository-based wording where it follows the 1893 main text; keep Greek readings in apparatus rather than harmonizing them into the verse. |
| 96:2 | The 1893 printed text encloses the “children ... rise as eagles” passage in square brackets; Charles's note calls the verse an interpolation and comments that it disrupts the context. | Preserve the passage as a clearly marked interpolation, not as a seamless continuation of verse 1. |
| 97:2 | The 1893 main text reads that the Most High is “mindful of your destruction,” followed by the angels rejoicing over the destruction. | Chapter 97:2 was corrected to retain this exact sense rather than the softened “taken account of what is being done to you.” |
| 98:12–13 | The printed text includes the explicit execution language against the wicked and says that no grave of theirs will be seen; the apparatus notes a variant “no grave will be dug for you.” | Keep the main-text wording and do not replace it with the alternative reading from other manuscripts. |
| 99:15 | The 1893 apparatus records differences in the phrase about transgressing against one's neighbour; the witness readings differ in the final wording. | Retain the selected main text and record the apparatus rather than forcing one variant into the modernization without a witness label. |
| 100:1–2 | The main text explicitly describes fathers and sons being struck down together, brothers killing brothers, and a man not withholding his hand from killing his sons. | Preserve the actual kinship sequence; do not reverse the actors or simplify the relationships. |
| 101:1–9 | The section moves from the heavenly witnesses and withheld rain/dew to the sea, its boundary, and the sailors' fear. | Preserve the argumentative sequence and distinguish the sea's created limits from the moral warning addressed to sinners. |
| 102:1–11 | The text contrasts the terror of sinners with the reassurance to righteous souls, then records the sinners' claim that righteous and wicked share the same fate. | Keep the distinct speaker shifts and the closing counterclaim about the righteous dead; do not collapse 102:6–11 into one narrator's speech. |
| 103:1–15 | The chapter begins with the solemn oath and heavenly records, then stages the righteous assurance and the reported speech of the wicked about the suffering righteous. | Preserve the speech boundaries and the distinction between the narrator's assurance and the wicked speakers' claims. |
| 104:1–13 | The closing exhortation assures the righteous that the angels remember them, then warns about corrupting written words and promises books to the righteous. | Preserve the transition from consolation to the warning about textual corruption and the promise of books. |

### Structural check on the repository modernization, Chapters 91–104

The complete formatted source file for Chapters 91–105 was compared with the corresponding modernized files for Chapters 91–104. Their numbered-unit sequences match exactly, with **167 source verse markers and 167 modernized verse headings** across the fourteen chapters:

- 91: 19; 92: 5; 93: 14; 94: 11; 95: 7; 96: 8; 97: 10.
- 98: 16; 99: 16; 100: 13; 101: 9; 102: 11; 103: 15; 104: 13.

This checks the selected repository source against the modernization's structural labels. It does **not** prove the semantic accuracy of every sentence or establish that the selected repository text is identical to the 1893 witness.

### What is still not complete for 1893

The expanded text-layer review materially improves the evidence for Chapters 91–104, but the checklist item “full historical collation” remains open. A complete collation still requires a line-by-line comparison of every verse and relevant critical note, explicit recording of every lexical/omission/addition/sequence difference, and visual proofing of the printed pages. The searchable OCR can contain recognition errors and displaced page text; page-image inspection is required where readings or punctuation are uncertain.

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

## 1917 Charles/Oesterley witness: Chapters 91–94 and image-verification scope

The 1917 SPCK printing (a reprint of Charles's 1912 second edition, first published in 1917) was checked against the repository sequence for Chapters 91–94. This is a separately identified witness; it must not be described as the 1893 main-text reading.

| Passage | 1917 printed evidence | Repository-based editorial treatment |
|---|---|---|
| 91:1–11, 18–19 | The 1917 printing groups 91:1–11 and 18–19 under Chapter XCII/XCI's admonition section. | The modernized edition retains the repository's Chapter 91 numbering. |
| 91:11 | The 1917 printing places the passage in square brackets. | Retain the repository's explicit interpolation marker. |
| 91:12–17 | The 1917 printing places these six units after the Chapter 93:1–14 sequence under the heading “XCI. 12–17. The Last Three Weeks.” | Retain 91:12–17 in Chapter 91 because that is the selected repository sequence. Do not move or renumber it without a separately approved witness-specific edition. |
| 92:1 | The 1917 printing reads “The book written by Enoch—” and brackets the longer clause beginning “Enoch indeed wrote this complete doctrine of wisdom…”. | Keep the complete repository wording but make the 1917 interpolation boundary explicit in the Chapter 92 editorial note. |
| 92:3 | The 1917 printing brackets a repeated “Shall arise”. | Keep the repository wording and record the additional bracket as a 1917 witness variant. |
| 93:1 | The 1917 printing uses dagger marks around a corrupt token in “both †gave† and began to recount…”. The 1917 notation guide defines daggers as corruption in the text. | The modernization omits the repository's stray terminal “l” and does not invent a replacement for the 1917 corrupt token. |
| 93:11–14 | The 1917 printing encloses this four-verse question sequence in square brackets. | Preserve the repository's interpolation markers and record the matching 1917 boundary. |
| 94:7 | The 1917 printing brackets the final clause about those who acquire gold and silver perishing in judgment. | Keep the unbracketed repository clause in the modernization; disclose that the 1917 witness marks it as interpolated. |

The bracket convention is explicit in the 1917 preliminaries: square brackets enclose interpolations, whereas other bracket forms indicate Greek/Ethiopic differences, editorial restorations, or supplied words. Daggers indicate corruption. These marks must not be conflated.

### 1917 scan page-image verification

A page-image screenshot was obtained and visually inspected for printed page 154 of the 1917 scan. It shows the closing Chapter 108 text, verses 8–15, and confirms that this portion is present on that printed page. This is a **single-page visual check only**. Attempts to retrieve the other relevant 1917 page images through the available PDF screenshot service returned cache-miss or retrieval errors. Accordingly:

- Chapter 105–108 text-layer comparison remains recorded as complete in the existing row above.
- Visual collation of Chapters 105–108 is **not complete**.
- Only the displayed page 154 was visually checked in this pass; no claim is made that pages containing Chapters 105–107 or the earlier part of Chapter 108 were visually proofread.

The 1917 PDF is the Wikimedia Commons scan titled *The book of Enoch. Robert Charles. 1917*; its front matter identifies the translation as reprinted from Charles's second edition (1912), and states that the work was first published in 1917. It is therefore a 1917 publication witness, not the 1893 source.

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
