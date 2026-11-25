# 1 Enoch — Historical Source Collation Log

**Status:** Sequential assistant-led searchable-text and critical-apparatus collation is recorded through the 1893 printed translation pages pp.55–308, including the distinct appended units CV–CVIII on pp.301–308. Page-image retrieval is recorded for pp.75–308, but individual visual inspection is recorded only for pp.55–74; the remaining retrieved images require page-by-page inspection. A Cornell/Internet Archive facsimile is stored at `pdfs/enoch-editions/enoch-1893-clarendon-original.pdf`. Chapters CV–CVIII are also compared against the 1917 Charles/Oesterley textual edition as a parallel later witness. Independent human approval and complete lexical/manuscript-variant collation remain open.  
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

The contents list Appendix D (additional notes on Chapters 37–108) and Appendix E (the New Latin fragment, Chapter 106:1–18). Separately, the searchable text layer shows CV.1–2 on p.301 and CVI–CVIII on pp.302–308, after the Section V core sequence XCI–CIV. Appendix E's Latin CVI fragment (pp.372–375) is a distinct witness and must not be conflated with the Ethiopic translation on pp.302–304.

**Editorial consequence:** Do not omit CV–CVIII from the 1893 printed-text collation: they appear on pp.301–308 as units appended after the Section V composition XCI–CIV. Preserve their distinct literary status—CV separate from XCI–CIV, CVI–CVII as the Noah fragment, and CVIII as an independent addition. The 1917 text remains a parallel later witness for comparison, not the only source for these chapters.

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


**Further verse-level wording corrections from the 1893 text layer:**

- **97:2:** The 1893 text explicitly says the Most High is “mindful of your destruction.” The modernization was corrected from the less precise “has taken account of what is being done to you” to “is mindful of your destruction.”
- **101:7:** The 1893 text says that at the Most High's reproof the sea is afraid and dries up. The modernization was corrected to remove the unsupported phrase “draws back” and to keep the reproof as the cause.
- **102:6–11:** The text-layer reading preserves the progression from the sinners' reported speech (6–8), to the author's reply (9–10), and the concluding statement about the righteous dead descending to Sheol (11). The repository's source labels keep this sequence; the modernization retains the speaker transitions and unit boundaries.
- **103:9–15:** Charles's apparatus notes extensive first-/third-person variation in manuscript G across this passage. The 1893 main-text wording and its narrative attribution should be kept distinct from the manuscript G alternative; the adaptation follows the selected main-text narrative perspective and does not merge the reported speech with the narrator's reply.

### What is still not complete for 1893

The expanded text-layer review materially improves the evidence for Chapters 91–104, but the checklist item “full historical collation” remains open. A complete collation still requires a line-by-line comparison of every verse and relevant critical note, explicit recording of every lexical/omission/addition/sequence difference, and visual proofing of the printed pages. The searchable OCR can contain recognition errors and displaced page text; page-image inspection is required where readings or punctuation are uncertain.

## Later witness for Chapters 105–108

The 1893 contents label Section V as XCI–CIV, while the printed translation continues on pp.301–308 with CV–CVIII as separately presented units. A separately identified parallel later witness is also available:

- **Printed witness:** R. H. Charles, *The Book of Enoch*, with an introduction by W. O. E. Oesterley (London: SPCK, 1917).
- **Edition statement:** The 1917 front matter says the translation is reprinted from Charles's second edition of *The Book of Enoch* (1912). A 1962 impression is represented by Project Gutenberg eBook 77935.
- **Digital text:** [Project Gutenberg eBook 77935](https://www.gutenberg.org/ebooks/77935) and its [HTML transcription](https://www.gutenberg.org/files/77935/77935-h/77935-h.htm).
- **Scan comparator:** [1917 SPCK scan on Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/c/c9/The_book_of_Enoch._Robert_Charles._1917_%28IA_bookofenoch0000unse%29.pdf).
- **Supplemental 1917 text/manuscript cross-check:** [Theosis Library: 1 Enoch 91–108](https://theosislibrary.com/library/verified-enoch-ethiopic-epistle). Its editorial provenance explicitly identifies the English text as Charles 1917 from Project Gutenberg eBook 77935, and displays the Dillmann 1851 Ethiopic text alongside mapped photographs of Rylands Ethiopic MS 23. The photos provide manuscript-level corroboration for chapter boundaries and the underlying Ethiopic tradition; they are not photographs of the 1917 SPCK printed pages and do not close the missing SPCK p.152 image.

The 1917 introduction classifies Chapter CV (105) as a two-verse section of uncertain date, Chapters CVI–CVII (106–107) as the “Fragment of the Book of Noah,” and Chapter CVIII (108) as an appendix. It also states that the reprinted translation is that of Charles's 1912 second edition. This is a useful parallel witness for comparison with the 1893 printed units, which are also present on pp.301–308.

A verse-by-verse comparison of the available 1917 text layer for Chapters 105–108 confirms:
- 106:3 retains the newborn's opening of his mouth and his conversation with the Lord of Righteousness;
- 106:16 says that Noah's three children are saved with him;
- 107:1–3 form the three-verse concluding Noah-fragment unit;
- 108 is presented as an appendix-like closing book.

The modernization corrections to 106:3 and 106:16 preserve these source details. Chapter 107:3 has also been adjusted to retain the repository source's “cause the earth to rejoice in compensation for all the destruction” wording, rather than borrowing the later witness's shorter “comfort the earth” phrasing.

**Status:** A verse-by-verse comparison of all 105–108 source units against the searchable 1917 text layer is now complete. This remains text-layer collation, not visual page-image proofing. The following differences are explicitly retained rather than silently blended:

- **Chapter 105:** Both witnesses have two verses. The adaptation follows the repository transcription, retaining its “in those days” introduction and its singular “guide” wording rather than silently switching to the 1917 “the Lord bade (them)” and plural “guides.”
- **Chapter 105:1–2:** 105:1 differs in agency and number: the 1917 text makes the Lord the one who bade them summon and testify, and calls the children plural “guides”; the repository makes “people” the caller and uses singular “guide.” Verse 105:2 also differs in syntax and uses “uprightness” where the adaptation uses “righteousness.”
- **Chapter 106:2–3:** Charles's 1917 notation marks the “long locks ... white as wool, and his eyes beautiful” expression in 106:2 as corrupt (†...†), and similarly marks “conversed with” in 106:3 as corrupt. The repository modernization renders both as ordinary text without disclosing the 1917 critical signs; this has now been explicitly added to Chapter 106's notes.
- **Chapter 106:8:** The 1917 text asks “wherefore hast thou come to me?”; the repository's “for you have come to me” is declarative. This changes the speech act and punctuation, not only archaic grammar.
- **Chapter 106:10–12:** The 1917 text's repeated report to Enoch gives several different formulations from the repository wording; 106:11 includes the action of rising in the midwife's hands and blessing the Lord of heaven. The repository's shorter wording is preserved.
- **Chapter 106:13–14:** The 1917 text explicitly says “some of the angels of heaven” transgressed and continues in the present tense “they commit sin”; the repository says “some from the heights of heaven” and uses past tense. This is a meaningful difference in identification and grammatical aspect.
- **Chapter 106:14 → 106:17a → 106:15–16:** Charles's 1917 translation prints the giants-production sentence immediately after 106:14 and marks it as verse 17a; his introduction recommends this order. The repository places verse 17 after 106:16 and changes the clause from active generation of giants to a statement about what giants are. Keep the repository sequence; record the witness relocation and subject/agency difference.
- **Chapter 106:16:** Charles adds the bracketed phrase “[he and his sons shall be saved]” after “when all mankind ... shall die.” The repository conveys the salvation of Noah and his three children in the verse body but does not include this bracketed supplement. It is a source-edition addition, not a missing repository verse.
- **Chapter 106:18:** 1917 says “he and his sons”; the repository uses “he and his children.” Keep the repository's general wording and disclose the form difference.
- **Chapter 107:3:** The repository says Noah will “cause the earth to rejoice in compensation for all the destruction”; the 1917 witness says “he will comfort the earth after all the destruction.” The repository-specific wording is retained.
- **Chapter 108:3:** The repository has “the books of the holy ones”; the 1917 text has “the holy books.”
- **Chapter 108:4:** The repository's “I could not look thereon” is rendered “I could not look upon it.” The 1917 edition marks the corresponding phrase as corrupt (†look over† in its searchable transcription); the p.153 scan visibly carries the daggered reading.
- **Chapter 108:6–8:** The 1917 text's angelic explanation explicitly identifies those cast into the place as sinners, blasphemers, and those who pervert God's prophetic words; verses 7–8 make the righteous record and bodily affliction more explicit. The repository wording is retained where it paraphrases these relations.
- **Chapter 108:9:** 1917 says the righteous “regarded everything as a passing breath”; the repository specifies that they regarded their bodies as a passing breath.
- **Chapter 108:10:** 1917 describes “all the blessings destined for them”; the repository says “all the blessings they received.”
- **Chapter 108:11:** 1917 says the faithful were not recompensed with the honour their faithfulness deserved; the repository recasts this as those who “did not seek honour” in the flesh. This changes agency and is noted as consequential.
- **Chapter 108:14:** 1917 says those born in darkness are “led into darkness”; the repository says they are “cast into darkness.”

The 1917 front matter explicitly identifies the text as a reprint of Charles's 1912 second edition. It is therefore a separately identified parallel witness for comparison with the 1893 printed text layer on pp.301–308. Chapters CV–CVIII are present in the 1893 volume as separately presented units after Section V's XCI–CIV composition.

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

### Initial 1917 page-image review — superseded by the expanded page audit below

The first visual pass inspected printed pp. 153–154 only. Printed p.153 contains the end of Chapter107 and the opening of Chapter108:1–7, including the daggered/corrupt token in108:4; printed p.154 contains Chapter108:8–15 through “Amen.” The later audit below additionally inspected printed pp.150–151 and mapped all checked pages to their zero-indexed PDF indices. Printed p.152 remains the one uninspected image.

At the time of this initial review, the earlier pages had returned cache-miss or retrieval errors. This was subsequently reduced to the single missing printed p.152 image; the later page map and results below supersede that older status.
### 1893 witness scope correction

The 1893 Clarendon Press volume labels its five core sections through Chapter CIV (104), but the translation pagination continues with CV–CVIII on pp.301–308 as distinct appended units. Appendix E separately prints a New Latin fragment of 106:1–18 on pp.372–375; that is a distinct witness and must not be conflated with the Ethiopic CVI translation on pp.302–304 or with the 1917 parallel witness.

The Cornell/Internet Archive searchable 1893 text-layer rendition is available at:
https://archive.org/stream/cu31924014590545/cu31924014590545_djvu.txt

A sequential assistant-led text-layer and critical-apparatus pass for Chapters 1–104 is now documented in the later dated entries in this log. That pass records the principal structural, interpolation, and consequential wording findings. It is not a complete word-by-word audit of every manuscript variant, a fresh diplomatic re-transcription, or visual proofing of the printed pages. Those more exhaustive collation tasks remain open.

## Scan inspection limitation

The 1893 Cornell PDF and OCR text layer can be searched, but the PDF screenshot service rejected the full-size scan because of its file-size limit. No systematic 1893 page-image proofing has been completed. The newly vendored `enoch-1893-clarendon-original.pdf` is the intended local source for that work.

For the 1917 SPCK scan, printed pp. 150–151 and 153–154 have since been visually checked. The earlier limitation below in this log is retained as history only; it has been superseded by the later visual page audit. Printed p. 152 remains uninspected, although its text layer is searchable.

## Collation procedure

A full collation must proceed in bounded batches and record evidence per chapter:

1. Identify the correct printed witness and printed page range for the chapter.
2. Compare chapter headings, verse divisions, ordering, interpolation brackets, and paragraph boundaries.
3. Compare each verse body against the repository source; do not silently replace repository wording with Charles wording.
4. Classify every difference as spelling/typography, OCR/transcription, lexical variant, omission, addition, relocation, or unresolved.
5. Record short evidence excerpts, printed page, repository chapter/verse, and decision.
6. If using 1912 or 1917 Charles material for a chapter absent or structurally different in 1893, identify it as a separate witness and do not label it 1893.
7. Mark the chapter as collated only after every verse and any relevant apparatus have been checked.

The 1917 searchable text layer was compared verse-by-verse for Chapters 105–108, and independently cross-checked against the Theosis Library's Charles 1917 digital text. The Theosis page also maps the 1917 English to manuscript photographs of Rylands Ethiopic MS 23, including the Chapter 106–108 folios; this is manuscript corroboration, not 1917 printed-page evidence. A PDF text layer is a search aid, not a substitute for checking the scanned page image where readings are uncertain. The 1893 page-image capture remains blocked by the provider's file-size limit. The later 1917 image audit inspected pp. 150–151 and 153–154; printed p. 152 remains the one missing page image. Earlier statements below that only pp. 153–154 were checked are historical snapshots and are superseded by the later audit.

## Open work

- [ ] Identify the exact intermediate source and textual lineage of the selected combined repository transcription.
- [ ] Complete page-image proofing and a full word-by-word collation of Chapters 1–36 against 1893 pages 57–105.
- [ ] Complete page-image proofing and a full word-by-word collation of Chapters 37–71 against 1893 pages 110–186.
- [ ] Complete page-image proofing and a full word-by-word collation of Chapters 72–82 against 1893 pages 191–219.
- [ ] Complete page-image proofing and a full word-by-word collation of Chapters 83–90 against 1893 pages 223–259.
- [ ] Complete page-image proofing and a full word-by-word collation of Chapters 91–104 against 1893 pages 265–308.
- [x] Complete the sequential assistant-led searchable-text / critical-apparatus pass for the 1893 printed translation pages pp.55–308, including appended units CV–CVIII; findings are recorded above. This is a targeted text-layer pass, not a complete manuscript-variant audit or visual proof.
- [x] Compare Chapters 105–108 verse by verse against the 1917 Charles/Oesterley text layer; differences and the Chapter 106 rearrangement are recorded above.
- [ ] Retrieve and inspect the missing 1917 printed p. 152 image; the checked images currently cover pp. 150–151 and 153–154.
- [ ] Have an independent second reviewer check all 108 modernized chapters and unresolved or consequential historical readings.

**Current conclusion:** The source-attributed reading edition is a complete chapter-body transfer of the selected repository transcription according to the repository's recorded checks. It is not a verbatim Charles 1893 transcription, not a facsimile-verified critical edition, and not a reproduction of the complete 1893 scholarly volume.


## Initial project-PDF acquisition — 25 November 2026

The two smaller files were the first PDFs in `pdfs/`: the 66-page modern 1893-labelled composite and the 101-page 2005 Word/PDFMaker 1917 transcription. They remain preserved as project artifacts and are not historical page-image witnesses.

## Historical scan addition — 25 November 2026

A later repository commit added the large historical scans: `enoch-1893-clarendon-original.pdf` (described in the commit as the Cornell 428-page 1893 scan) and `enoch-1917-spck-original.pdf` (described as the Claremont 160-page SPCK scan). The latter is a 1962 tenth impression of the edition first published in 1917. The four-file inventory, sizes, blob identifiers, and provenance distinctions are documented in [`pdfs/README.md`](../../../pdfs/README.md).

The historical scan files are now versioned with the project. The available GitHub connector does not expose their binary PDF bytes for local rasterization in this review session; page images were therefore checked through the public full-scan witness. This pass verified 1917 printed pp. 150–151 and 153–154, but not p. 152. No systematic 1893 page-image proofing was completed. Do not equate source acquisition with completion of visual collation.



## Direct inspection of the user-supplied PDFs — 25 November 2026

The user attached both PDFs directly to the review conversation. Their bytes were available for local extraction and page rendering, so the earlier note claiming that the binary files could not be rendered is superseded by this direct inspection.

### 1917 Charles/Oesterley file

File: `enoch-1917-charles-oesterley.pdf` (101 PDF pages).

The final three PDF pages were rendered and visually inspected:

| PDF page | Visible contents | Result |
|---:|---|---|
| 99 | End of 104, complete Chapter 105, heading for Chapter 106 | Checked |
| 100 | Chapter 106:1–14 | Checked |
| 101 | Chapter 106:17a, 106:15–19, and Chapter 107:1–3 | Checked |

The page images confirm the unusual printed order in Chapter 106: verse 17a appears immediately after verse 14, before verses 15 and 16. The page images also confirm the 1917 wording in 105:1 and 107:3 previously noted from the text layer.

**Important scope limitation:** the attached 1917 PDF ends after 107:3. It contains no Chapter 108 and no subsequent page. It therefore cannot be cited as a visual witness for Chapter 108. Earlier review notes about a different, fuller 1917 scan's pp. 153–154 must remain explicitly tied to that separate witness; they are not pages of this 101-page attachment.

### File labelled 1893 Charles/Dillmann

File: `enoch-1893-charles-dillmann.pdf` (66 PDF pages).

This is not a photographic facsimile of the 1893 Clarendon Press edition. Its own opening text identifies it as a compiled/combined text: “translated (Geez) by Professor Dillman, Charles 1893” and “integrated with The Book of the Secrets of Enoch (2Enoch) translated (Slavonic) by Professors Morfill and Sokoloff, Charles 1896.” It is modern typesetting, has internal headings “Book 1” through “Book 6,” and interleaves material explicitly labelled “Enoch Slavonic.” Its page 60 moves from 1 Enoch 105 into “Enoch Slavonic 49”; later pages include further Slavonic material and a separate “Book 6 - The Deluge” presentation of 106–108.

This PDF can be studied as a modern composite transcription, but it is not a page-image witness to the original 1893 Charles/Dillmann publication and cannot complete the requested historical facsimile collation for Chapters 1–104. Its exact textual lineage and editorial assembly require separate provenance work before its readings can be treated as a primary witness.

### Revised completion boundary

- Direct visual check of the attached 1917 file: PDF pp. 99–101, covering 105, 106 and 107:3, complete for the content actually present in that file.
- Chapter 108: absent from the attached 1917 file; a separately identified witness containing 108 is still required.
- 1893 Chapters 1–104: not historically collated, because the attached 66-page file is a modern composite rather than the original 1893 facsimile.
- No independent human semantic approval is implied by these mechanical or visual checks.


## Authentic 1893 Clarendon witness located — 25 November 2026

A separate, authentic digitized copy of the 1893 Clarendon Press volume has been located: [The Book of Enoch, R. H. Charles, 1893, Wikimedia Commons / Google Books scan](https://upload.wikimedia.org/wikipedia/commons/1/1d/The_book_of_Enoch._August_Dillmann%2C_Robert_Charles._1893_%28IA_bookenochtransl00dillgoog%29.pdf). The scan is 418 pages and its title page identifies the work as translated from Professor Dillmann's Ethiopic text, edited by R. H. Charles, Clarendon Press, 1893. The contents label Sections I–V as Chapters I–CIV and give pp.265–308 for Section V; the text layer then prints CV on p.301 and CVI–CVIII on pp.302–308 as separately presented units. Appendix E separately contains the New Latin fragment CVI.1–18, pp.372–375. The 1893 volume therefore includes these appended units, while Charles distinguishes their literary status from XCI–CIV.

The file attached in this conversation as `enoch-1893-charles-dillmann.pdf` is not this facsimile. It remains classified as a modern composite transcription, not a primary image witness. The authentic 1893 scan is therefore now available as an external primary witness, but its page images still require systematic inspection. The searchable text layer has been opened and the first chapter text compared; do not treat this discovery as completion of the 104-chapter collation.

### Initial 1893 text-layer collation: Chapters 1–5

The authentic 1893 text layer was examined at the start of Section I. Chapter 1 confirms that the repository's formatted source is a modernization/derivative rather than a verbatim transcription. Examples include:

- 1893 I.1 begins “The words of the blessing of Enoch, wherewith he blessed...” while the repository derivative begins “These are the words of blessing of Enoch...”.
- 1893 I.2 reads “And Enoch answered and spake—(Enoch) a righteous man...” while the repository derivative reads “Enoch answered and spoke: I, Enoch, a righteous...”. The parenthetical grammatical construction and the first-person restatement are not identical.
- 1893 I.4 begins “And going from thence...” and I.9 begins “And lo!”; the repository derivative drops those conjunctions in its corresponding clauses.
- Chapters 2–5 were spot-compared at the section opening. Their sense and sequence are broadly aligned, with modernization of diction and syntax. This is an initial text-layer pass, not a full word-by-word or visual collation of all verses in those chapters.

Continue the 1893 collation sequentially by chapter and record every substantive lexical, syntactic, verse-division, interpolation, and omission difference. Page-image verification remains a separate requirement.


## Authentic 1893 text-layer collation: Chapters 6–15 — 25 November 2026

**Witness consulted:** R. H. Charles, *The Book of Enoch*, Clarendon Press, 1893, Section I, translation and notes, printed pp. 62–84. The authentic 1893 facsimile is available at https://s3.us-west-1.wasabisys.com/luminist/EB/C/Charles_ed%20-%20Book%20of%20Enoch.pdf and the searchable Archive OCR at https://archive.org/stream/thebookofenoch00unknuoft/thebookofenoch00unknuoft_djvu.txt. This batch is a comparison of the searchable text layer and critical apparatus against the repository's formatted base and modernized chapters. Page-image proofing for these pages was not completed.

| Chapter | 1893 reading / apparatus | Repository treatment and decision |
|---|---|---|
| 6 | Charles brackets 6:3 as an interpolation. His printed 6:7 list has 18 names; the transliterations differ from the repository list (e.g. Semjaiza/Semjaza, Uraikibariméél/Urakibarameel, Rimuél/Ramuel, Danél/Danel, Zaqild/Zaqilo, Sariqujal/Saraqujal, Asdél/Asael, Armiaréis/Armaros, Anadni/Anani, Samsivéél/Samsaveel, Turél/Turel). | The selected formatted base does not mark 6:3 as an interpolation and uses its own transliterations. The modernization retains the base's verse status and spellings; the difference is documented in Chapter 6. Do not silently insert brackets or merge name lists. |
| 7 | The six numbered units correspond in order and substance to 1893 VII.1–6. | No substantive correction identified in this pass. This is text-layer comparison, not visual proof. |
| 8 | Charles brackets 8:1–3 as an interpolation. The 1893 errata explicitly corrects “eyebrows” to “eyelids” at printed p. 66, line 8. | The repository already brackets 8:1–3. The modernized 8:1 now follows the erratum's “eyelids”; the repository's literal base wording “eyebrows” remains unchanged. |
| 9 | Charles's apparatus says 9:2 is not found in the Greek witness; it also identifies 9:7 as an interpolation from the same source as 6:3–8 and 8:1–3. For 9:1, Charles discusses “Surjan” and “Urjan” as variants of “Suriel” and “Uriel” and suggests “Raphael” instead of “Surjan” according to the Greek. | The repository already marks 9:7 as an interpolation. Its 9:1 names are retained, but the critical alternatives and absence of 9:2 from the Greek witness are now disclosed in Chapter 9. |
| 10 | Charles marks 10:1–3 as a Noah fragment/interpolation and 10:11 as an interpolation; 10:7 is not bracketed. On 10:14 he states that the printed “whosoever shall be condemned” reading follows the Syncellus Greek, unlike the Ethiopic singular “he will burn,” which he considers corrupt in context. | The repository and modernization preserve the 1893 interpolation boundaries, including the unbracketed 10:7. Chapter 10 now records the Greek-supported 10:14 reading and the Ethiopic alternative. |
| 11 | The two numbered units correspond in sequence and substance to 1893 XI.1–2. | No substantive correction identified in this pass. |
| 12 | The six numbered units correspond in sequence and substance to 1893 XII.1–6. | No substantive correction identified in this pass. |
| 13 | 1893 XIII.7 locates Enoch at Dan “to the right (i.e. the south) of Hermon.” | The earlier modernization's “south-west” was more specific than the 1893 wording. Chapter 13:7 has been corrected to “south of Mount Hermon.” |
| 14 | 1893 XIV.11 preserves the literal clause “and their heaven was water” (the printed explanatory text also glosses it as a transparent heaven). At XIV.24 the translation reads “hear my holy word”; Charles notes “hear” is supported by the Gizeh Greek but absent from the Ethiopic manuscripts. | Chapter 14 now retains “their heaven was water” and the singular “hear my holy word,” rather than the earlier interpretive/pluralized wording. |
| 15 | 1893 XV.4 explicitly says the Watchers “have begotten (children) with the blood of flesh.” | The earlier modernization's “joined yourselves to mortal flesh” obscured the begetting action. Chapter 15:4 has been revised to retain it. |

Chapters 7, 11, and 12 were checked for their numbered sequence and basic wording; no substantive text correction was indicated in this pass. This does not establish that every line, apparatus entry, or page image has been independently proofread.

**Batch boundary:** Chapters 6–15 have now had a sequential 1893 searchable-text-layer comparison, with the findings above recorded. Do not mark these chapters as visually collated: page images for printed pp. 62–84 have not yet been systematically inspected. The text layer itself can contain OCR errors, and the 1893 critical apparatus sometimes records variant manuscript readings separately from Charles's printed translation.


## Authentic 1893 text-layer collation: Chapters 16–20 — 25 November 2026

**Witness:** R. H. Charles, *The Book of Enoch*, Clarendon Press, 1893, Section I, printed pp. 85–91. The searchable layer of the authentic 1893 scan was inspected at the chapter passages and Charles's adjacent critical notes. The page images were not available for visual proofing; the statements below are text-layer / printed-apparatus findings.

| Chapter | 1893 evidence | Repository treatment |
|---|---|---|
| 16 | 16:1 is a difficult reconstructed text: Charles explains that the Ethiopic is corrupt and restores it with the Book of Jubilees and the Syncellus Greek. The 1893 translation reads “when the spirits have gone forth from the souls of their flesh” and “in order to destroy without incurring judgment.” At 16:2 Charles prints “you knew worthless mysteries.” Charles then identifies the following Greek fragment as absent from the Ethiopic and probably belonging to the lost Apocalypse of Noah interwoven with Enoch. The printed numbering has 16:1, 16:2, 16:4; no 16:3 appears. | The repository preserves the same numbered sequence 1, 2, 4. Modernized 16:2 was corrected from “learned forbidden mysteries” to “knew worthless mysteries.” The Greek-only fragment boundary is noted as a witness/apparatus fact; it must not be mistaken for Ethiopic wording. |
| 17 | The 1893 edition places Chapter XVII within a square-bracketed interpolated block. | The repository and modernization do not mark the chapter as interpolated. The chapter is retained, but its 1893 bracket status is disclosed in Chapter 17. |
| 18 | The 1893 square-bracketed interpolated block continues through Chapter XVIII. | The repository and modernization do not mark the chapter as interpolated. The 1893 structural difference is disclosed in Chapter 18. |
| 19 | The 1893 square-bracketed block continues through Chapter XIX; Chapter XX begins outside that bracketed block. | The repository and modernization do not mark Chapter 19 as interpolated. The 1893 structural boundary is disclosed in Chapter 19. |
| 20 | The 1893 printing begins Chapter XX outside the Chapter XVII–XIX bracketed block and lists seven angels. Their roles and names align in sequence with the repository base. | No substantive correction identified in this pass. |

Charles's own introduction also lists XVII–XIX among interpolations. The modernization retains the selected repository base and does not silently delete or bracket these chapters. This is a witness-layout and source-critical difference; it is not independent evidence that these chapters should be omitted.

**Batch boundary:** This is a sequential text-layer check of Chapters 16–20, including the adjacent critical apparatus. Printed pp. 85–91 have not been visually checked against page images. The difficult reconstructed text at 16:1 and the Greek-only fragment context at 16:2 require continued apparatus-aware treatment.


## Authentic 1893 text-layer collation: Chapters 21–36 — 25 November 2026

**Witness:** R. H. Charles, *The Book of Enoch*, Clarendon Press, 1893, Section I, printed approximately pp. 91–106. The authentic scan's searchable text and notes were inspected at these passages. This is not visual page-image verification.

| Chapter range | Comparison result | Notes |
|---|---|---|
| 21–25 | The repository's numbered sequence and the modernization's sequence align with the 1893 translation in the reviewed passages. | No consequential wording correction identified in this pass. Charles's notes for 21:2, 21:5, 21:9 and the 24–25 tree description were considered separately from the verse text. |
| 26–27 | The Jerusalem/valley sequence and the division of the blessed and accursed places align in sequence and substance. | Charles's apparatus identifies the blessed place as Jerusalem and interprets the tree/branches allegorically; this is commentary, not additional verse text. |
| 28–30 | The eastern wilderness, streams, frankincense/myrrh trees, mastic-like tree, and cinnamon sequence align in the passages reviewed. | No consequential correction identified. |
| 31 | 1893 XXXI.3 says the taste of the fruit was better than all fragrant odours. | The modernization had changed this to “One of its fruits was more fragrant than every other perfume,” shifting taste into fragrance. Chapter 31:3 has been corrected to preserve the printed sense. |
| 32 | The northward journey, seven mountains, Erythraean Sea, angel Zutel, Garden of Righteousness, carob-like fruit, and expulsion all align in sequence. | No consequential correction identified in this pass. |
| 33–34 | The description of beasts/birds, the eastern gate of heaven, star portals, and the three north-wind portals aligns in sequence. | No consequential correction identified in this pass. |
| 35 | Charles prints the westward gate description as an unnumbered chapter passage. | The repository correctly retains Chapter 35 as unnumbered. |
| 36 | The south-wind portals and eastern star portals align in four numbered units. | No consequential correction identified in this pass. |

**Batch boundary:** The comparison was conducted through the searchable text and apparatus, not page images. The page-image captures for printed pp. 91–106 were not available through the PDF screenshot service. “No consequential correction identified” records the result of this textual pass, not independent human approval or a claim that every manuscript variant has been resolved.



## Authentic 1893 text-layer collation: Chapters 37–60 — 25 November 2026

**Witness:** R. H. Charles, *The Book of Enoch*, Clarendon Press, 1893, Section II, printed pp. 110–154. Comparison was made against the searchable text layer and Charles's critical apparatus; no page-image verification is claimed.

### Structural and interpolation findings

| Passage | 1893 printed/textual evidence | Repository treatment / correction |
|---|---|---|
| 37–38 | Chapter 37 opens the Similitudes and identifies three parables. Chapter 38 begins the first Similitude. | The modernized chapters retain the chapter/section transitions and their numbered units. No consequential correction identified in this pass. |
| 39:1–2 | Both opening units are visibly bracketed in the 1893 text. | The modernization already marks and brackets both verses as interpolations. |
| 40 | The four-presence passage is printed as the main text. Charles's note discusses variants in names/functions and the “Satans” language at 40:7. | The modernization retains the repository's names and order. “Adversaries” remains an explanatory gloss for “Satans,” not a replacement of the source term. |
| 41:3–8 | Charles brackets verses 3–8; his note calls them alien to the context and probably from the Noah Apocalypse. Verse 9 resumes the main passage. | The modernization correctly labels 3–8 as interpolations and leaves verse 9 outside the bracketed block. |
| 42:1–3 | The three-unit Wisdom fragment is printed without square brackets. Charles's apparatus treats it as a separate fragment out of context, not as part of the main visionary sequence. | The modernization preserves all three units and does not add an interpolation label unsupported by the printed brackets. |
| 43:1–4 | The entire chapter is square-bracketed in the 1893 text. | The modernization correctly marks and brackets all four verses. |
| 44 | The lightning sentence is unnumbered and printed without square brackets. Charles's apparatus nevertheless includes Chapter XLIV among the intrusive/interpolated passages. | The modernization was incorrectly making the square brackets appear to be in the 1893 print. That is corrected: the sentence stays unnumbered and unbracketed, with Charles's critical classification disclosed separately. |
| 45–49 | The second Similitude and its following material are printed as main text in the reviewed passages. | Numbered units and sequence broadly align; no additional consequential correction identified in this pass. |
| 50 | Charles's printed text opens Chapter L with a square-bracketed passage; his note says the chapter must be regarded as an interpolation. | The modernization's five verses remain bracketed as an interpolated chapter. |
| 51–53 | The resurrection of the dead, mountains, metals, and valley passages are presented in sequence. | No consequential correction identified in the reviewed passages. |
| 54:7–10 | Square-bracketed Noachic material follows the preceding chapter's judgment narrative. | The modernization correctly brackets verses 7–10 as interpolation material. |
| 55:1–2 | The Noahic continuation is bracketed; verses 3–4 resume the main Similitudes context. | The modernization correctly brackets verses 1–2 only. |
| 56:5–57:3 | Charles treats this inserted sequence as a Noachic interpolation, extending across the chapter boundary. | The modernization correctly marks 56:5–8 and 57:1–3 as interpolation material. |
| 58 | The third Similitude begins; the six numbered units form the main text. | Sequence and broad sense align in the reviewed passage. |
| 59 | The entire chapter is square-bracketed; Charles's apparatus describes it as an intrusion and links it with the interpolation group. | The modernization correctly retains its bracketed status. |
| 60 | The whole chapter begins with a square-bracketed heading and is identified in Charles's notes as one of the Noachic fragments. The date formula says “in the life of Enoch,” but the apparatus explicitly says “For Enoch we should read Noah.” | The modernization now marks all 25 units as one continuous bracketed Noachic interpolation. The printed Enoch wording is retained while Charles's recommended Noah emendation is disclosed; the emendation is not silently substituted. |

### Confirmed source-sensitive distinction

A critical-apparatus classification and square brackets in the printed text are not interchangeable. Chapters 43, 50, 59, and 60 have printed bracket marking; Chapters 42 and 44 are not square-bracketed in the translation text even though Charles treats these as out-of-context fragments/intrusions in his notes. The modernization now reflects that distinction in Chapter 44. Chapter 60's Noachic status is also made explicit in the modernized file.

**Batch boundary:** The source text layer and critical notes for Chapters 37–60 have been examined at the major chapter boundaries and interpolation zones. This pass is not a claim that every word in every verse has been proofread against the scan. The authentic 1893 pages in this span have not been visually checked.


## Authentic 1893 text-layer collation: Chapters 61–64 — 25 November 2026

**Witness:** R. H. Charles, *The Book of Enoch*, Clarendon Press, 1893, Section II, printed pp. 159–167. Text-layer and critical notes were consulted; no page-image verification is claimed.

| Chapter | 1893 evidence | Repository treatment |
|---|---|---|
| 61 | The angels take the cords and fly “towards the North”; Charles's note glosses this as “the North-West.” The main text has 13 units. The apparatus discusses a longer reading for the cords, variants in “strengthen righteousness,” and the exact wording of the host/angel catalogue. | The modernization preserves the printed direction “northward” and records Charles's NW gloss in Chapter 61 rather than rewriting the verse. Sequence and broad sense align. |
| 62:1 | Charles prints “Open your eyes and lift up your horns if ye are able to recognise the Elect One.” | The modernization's “raise your heads” flattened the horn image. It is corrected to “lift up your horns.” |
| 62:2 | Charles prints “the Lord of Spirits seated him”; the apparatus notes this requires an emendation of the underlying text because the spirit of righteousness poured upon “him” refers to the Messiah. | Modernization retains the printed “seated him” and records this is a Charles editorial emendation. |
| 62:3 | Charles prints “righteousness is judged before him.” The apparatus notes Greek and a family of manuscripts with the alternative “the righteous are judged,” and others with “the righteous are judged in righteousness.” | The modernization's generalized phrase “righteous judgment will be carried out” was too interpretive; it is corrected to “righteousness will be judged before him.” |
| 62:5 | Charles prints “that Son of Man” following the Greek; he notes later Ethiopic manuscripts read “Son of the Woman,” likely a scribal corruption. | Modernization retains “Son of Man” and discloses the alternative in Chapter 62. |
| 62:10–12 | The Lord presses the kings out of his presence, angels of punishment take charge of them, and the sword is “drunk with their blood.” | Broad sequence retained. No separate correction identified. |
| 63 | The kings' confession is presented as a last, despairing appeal; Charles's commentary explains the rhetorical function and discusses the meaning of Sheol. | Numbered sequence and broad sense align in the passages checked. |
| 64 | A short digression records Enoch's vision of forms and angels who descended and revealed hidden things to humanity. | The two-unit sequence aligns. |

**Batch boundary:** This text-layer comparison is not visual proof against printed page images. Chapters 61–64 have been examined for major readings and apparatus variants; that is not independent human sign-off.


## Authentic 1893 text-layer collation: Chapters 65–71 — 25 November 2026

**Witness:** R. H. Charles, *The Book of Enoch*, Clarendon Press, 1893, Noachic fragments and conclusion of Section II, printed pp. 170–185. Text and critical apparatus were checked through the authentic scan's searchable text layer. No page-image proofing is claimed.

| Passage | 1893 evidence | Repository treatment / action |
|---|---|---|
| 65–67:3 | Charles identifies 65:1–67:3 as Noachic material. Chapter 65 describes Noah's vision of the sinking earth and his call to his grandfather Enoch; 67:1–3 contains the divine word to Noah and the wooden structure. | Modernization already marks the corresponding opening verses as interpolation material. |
| 66 | Three units concerning the angels of punishment and the powers of the waters. | The complete chapter is bracketed and marked interpolation in the modernization. |
| 67:4–68 | Charles's commentary identifies 67:4 onward as a digression concerning the punishment of fallen angels; Chapter 68 continues the discussion between Michael and Rufael. | The modernized chapter is preserved under the 65–69:25 Noachic interpolation block; no text is removed. |
| 69:1 | Charles's printed translation reads “inspire fear and anger,” but his note says “anger” is unsuitable to the context and suggests “fear and trembling.” | Chapter 69:1 is corrected to “fear and trembling,” with the printed reading and apparatus correction both recorded. |
| 69:2 | The 1893 printed name list gives “Ansinel” at the fourteenth position. | The repository form “Ananel” is retained, with the 1893 transliteration variant disclosed in Chapter 69. |
| 69:2–25 | The Noahic interpolation continues through the names and oath material. Charles's bracket closes after verse 25; verses 26–29 return to the third Similitude. | The modernization correctly brackets 1–25 only and keeps 26–29 unbracketed. |
| 70 | Two-unit account of Enoch's name being taken up and his placement between the North and West. | Two-unit sequence retained. |
| 71:1–17 | Charles prints the entire Chapter LXXI in square brackets. His critical discussion calls it “certainly a later addition,” alien in thought and phraseology to the Similitudes, and probably by the same hand that interpolated the Noachic fragments. It also remarks that 71:14 applies “son of man” to Enoch himself. | The modernization previously left the chapter unmarked. All 17 verses are now bracketed as an interpolation, without deletion or rewriting of the chapter. |

Charles's note on 69:1 is important: a critical apparatus correction must not be mistaken for the actual wording of the printed translation. The modernization adopts the apparatus-supported sense but records the printed reading and why it has been changed.

**Batch boundary:** This is text-layer and apparatus collation, not page-image verification. The Noachic interpolations and the Chapter 71 square-bracket boundary have been checked in OCR; printed pp. 170–185 remain to be visually proofread. Independent human review remains necessary.


## Authentic 1893 text-layer collation: Chapters 72–82 — 25 November 2026

**Witness:** R. H. Charles, *The Book of Enoch*, Clarendon Press, 1893, Section III, printed pp. 189–219. The Cornell/Internet Archive full-text OCR was checked alongside the user-repository PDF. This is searchable text and apparatus comparison, not systematic page-image proofing.

| Chapter | 1893 evidence and critical apparatus | Repository treatment / decision |
|---|---|---|
| 72–79 | Charles's introduction defines 72–79 as a continuous “Book of Celestial Physics,” with 79:1 announcing the completion of the laws of the stars. The text records solar/lunar gates, measured periods and calendar arithmetic; his notes discuss textual variants in the solar/lunar calculations (notably 74:14) and the 364-day year. | The modernization retains the 37/8 etc. numeric sequences and verse order. No comprehensive word-by-word corrections are claimed for these chapters; anomalous astronomical figures should be retained as the witness's reading, not silently “fixed” to modern astronomy. |
| 80 | The complete chapter is square-bracketed in the 1893 printed translation. Charles's introduction calls it an addition giving an ethical turn to a scientific treatise, and his note questions 80:5 as inconsistent with 76:13. | The modernization correctly marks all eight units as interpolation. |
| 81 | The verse text itself is **not** square-bracketed in the 1893 printing. Charles's introduction says Chapter 81 cannot belong to the Book of Celestial Physics; the apparatus calls the chapter an interpolation. | The modernization had incorrectly put square brackets around every verse, making it look as though the brackets appeared in the original translation. It is corrected: verses remain unbracketed, with the critical classification disclosed separately. |
| 82:1–8 | Charles identifies 82:1–8 as the close of the Book of Celestial Physics and says they belong with 72–79. | Retained as main text. |
| 82:9–20 | Charles argues that 82:9–20 are also integral to the Book of Celestial Physics, contrary to Dillmann's view that they are a later addition. His note says these verses are necessary to complete the account of the stars. | Retained as main text; do not mark 82:9–20 as a Noachic insertion. |
| 82:13–14 | The 1893 text layer at printed p. 218 labels the four names of year-division leaders as 13 and the subordinate leaders as 14. [Searchable 1893 OCR](https://archive.org/stream/cu31924014590545/cu31924014590545_djvu.txt), around OCR lines 17054–17061. | The combined archive transcription duplicated the label 14. The formatted and modernized reading derivatives now correct the first instance to 13; the original combined archive file remains unchanged. |

**Batch boundary:** Chapters 72–82 have been checked for major section boundaries, interpolation status, apparatus positions, and the Chapter 82 numbering correction. A searchable text-layer confirmation of 82:13–14 is recorded above. The section has not received a full lexical collation of every verse or visual page-image verification; the 1893 pages still need systematic image proofing.


## Authentic 1893 text-layer collation: Chapters 83–90 — 25 November 2026

**Witness:** R. H. Charles, *The Book of Enoch*, Clarendon Press, 1893, Section IV, printed pp. 222–255. Cornell/Internet Archive OCR and the critical introduction/notes were checked. This is not page-image proofing.

| Chapter / passage | 1893 evidence | Repository treatment / decision |
|---|---|---|
| 83–84 | These chapters begin the first dream-vision. Charles's notes distinguish the “great judgment” of 84:4 as the Deluge, not the final judgment. | Chapter order and verse sequence retained. A clarification was added to Chapter 84 so the same phrase is not read as a universal eschatological term. |
| 85–88 | These chapters continue the second dream-vision from the primordial animals and fallen stars through the flood narrative. | The sequence and numbering in the modernization match the reviewed 1893 text passages. No textual alteration was warranted in this pass. |
| 89:48b | Charles's introduction recommends that the latter part of 89:48 (the second ram's falling asleep and the small sheep taking his place as prince and leader) be read after 89:49. The 1893 printed verse itself includes this clause within 89:48; Charles explains the Greek fragment ends at 89:49, so the clause's original placement may have been at the close of 49. | The modernization preserves the printed arrangement and records the alternative reading order in Chapter 89. No clause is omitted or duplicated. |
| 90:1 | The 1893 printed translation reads “thirty-six shepherds”; Charles's note says this is probably a manuscript error for thirty-five, which better sums the first two periods (12+23). | Printed “thirty-six” retained, with the likely emendation documented in Chapter 90. |
| 90:15 | Charles identifies this as the single interpolation in Section IV; the verse is bracketed in the printed translation. | Modernization correctly labels and brackets verse 15 only. |
| 90:19 | Charles's Section IV introduction recommends that 90:19 be read before 90:16. The printed order places 19 after 18. | Modernization keeps the printed order and records the critical transposition in Chapter 90 rather than silently altering the base sequence. |
| Section IV overall | Charles describes 83–90 as the most complete and self-consistent section, with one interpolation (90:15) and two dislocations (89:48b after 89:49; 90:19 before 90:16). | These findings are recorded without conflating print order, recommended reconstruction, or interpolated material. |

**Batch boundary:** Chapters 83–90 have been checked against the searchable text and Charles's critical introduction for section order, the single interpolation, and two dislocations. This is not a full word-by-word collation of every verse or page-image proofing.


## Authentic 1893 text-layer collation: Chapters 91–104 — 25 November 2026

**Witness:** R. H. Charles, *The Book of Enoch*, Clarendon Press, 1893, Section V, printed pp. 258–308. Searchable OCR and Charles's introduction/critical apparatus were checked. This is not visual page-image collation.

### Original order, interpolations, and dislocations

The 1893 printed order of Chapters 91–104 is not identical to Charles's reconstruction of the original composition. Charles identifies Chapter 92 as the real beginning of the independent book (91–104) and reconstructs its original opening sequence as:

1. 92:1–5
2. 91:1–10
3. 93:1–10
4. 91:12–19
5. 94–104

The principal critical boundaries are:

| Passage | 1893 printed / apparatus evidence | Repository treatment |
|---|---|---|
| 91:11 | Marked as an interpolation and interrupts the opening exhortation. | Modernization already marks 91:11; this status retained. |
| 91:12–19 | These are the eighth–tenth weeks of the Apocalypse of Weeks and belong after 93:1–10. | Kept in Chapter 91 to preserve the selected base and printed numbering; Charles's reconstructed order is now stated in Chapters 91–93. |
| 93:11–14 | Entire block is out of place; Charles says it would fit the Book of Celestial Physics (72–79, 82) better, but is foreign in tone and does not accurately describe any Enoch book. | Modernization already marks all four units as interpolations. They remain outside the reconstructed Apocalypse of Weeks sequence. |
| 96:2 | Charles's critical apparatus notes the textual difficulties and this verse is bracketed in the printed 1893 translation. | Modernization retains its interpolation marker. |
| 100:7 | Charles says the phrase “on the day of great trouble and burn them with fire” should probably follow “woe to you sinners” directly, making the reference to final judgment. | Existing repository sequence retained; the proposed attachment is recorded separately in Chapter 100. |
| 104:10–13 | Charles's commentary explains the warning against falsification of the righteous words and the promise that truthful books will be given to the righteous. | The modernization's 104:10–13 preserves the warning and promise sequence. No separate consequential wording correction was made in this pass. |

### Verse-level findings across the remaining section

- **91–93:** Compared the chapter opening, repeated “will arise” wording in 92:3, the interpolation boundary in 93:11–14, and the critical sequence for the Apocalypse of Weeks. Charles's apparatus notes the G manuscript alternative “wisdom will arise” in 92:3; the 1893 printed reading is retained.
- **94–99:** Compared the admonitions against oppression, wealth, idols and falsified words with the 1893 text layer. Charles's apparatus contains manuscript variants in this stretch; no modernized verse was silently altered based on a single variant. Chapter 98:4's creation/agency wording remains translated as in the repository base; no medical or factual endorsement is implied by the source's ancient explanation of childlessness in 98:5.
- **100–102:** Compared the violence, judgment, witnesses of the natural world, and consolation of righteous souls. Charles's notes explain that the “righteous” guarded in 100:5 are souls of the dead in the place of departed spirits, not simply the living; this interpretation is relevant to understanding the verse but does not justify rewriting its wording.
- **103–104:** Compared the promises to those dying in righteousness, the contrast between outward fate and final reward, and the warning that righteous words must not be falsified. The 104:10–13 sequence is retained.
 
**Batch boundary:** Chapters 91–104 have now had a sequential text-layer and critical-apparatus review, with the major interpolation and order findings recorded. This does not claim a complete word-by-word diplomatic transcription audit for every manuscript variant; the 1893 printed pages in this section have not been systematically visually proofread. The authentic 1893 page-image collation remains outstanding.


## Repository PDF provenance audit — 25 November 2026

The directory `pdfs/` now contains four PDFs, and they must not be treated as interchangeable:

| Repository file | Repository size / Git blob | Classification |
|---|---:|---|
| `enoch-1893-charles-dillmann.pdf` | 540,432 bytes; `398352f3010cd7f059c91a24e8c32b9f8b1539a6` | 66-page modern composite/re-typeset artifact. It combines 1 Enoch with Slavonic 2 Enoch/later material and is not a photographic 1893 Clarendon scan. |
| `enoch-1893-clarendon-original.pdf` | 16,777,301 bytes; `38be2b5e0e95779f92dcb19a745fc654b010b711` | Newly added large scan. The 25 November 2026 Git commit identifies it as the Cornell/Internet Archive 1893 Clarendon original (428 scanned pages). Independent catalog and title-page evidence identify the historical edition as Oxford, Clarendon Press, 1893. It is the repository's intended 1893 page-image witness. |
| `enoch-1917-charles-oesterley.pdf` | 438,198 bytes; `9bd830eafb560890c6c78d2f89d828b603d6a979` | 101-page Word/PDFMaker 2005 typeset transcription, not a scan of a 1917 impression; ends at 107:3 and contains no Chapter 108. |
| `enoch-1917-spck-original.pdf` | 7,051,515 bytes; `80523ea72dfed5c4159dce85420e9ab1496dd3d4` | Newly added full SPCK scan, described in the 25 November 2026 Git commit as a 160-page Claremont scan. The scanned copy is the tenth impression of 1962 and states “First published in 1917”; its preface identifies the text as a reprint of Charles's 1912 second edition. It is a facsimile witness to the 1917 textual edition, but this particular physical impression is from 1962, not 1917. |

The external Cornell/Internet Archive record identifies the 1893 scan as the Clarendon Press edition and the Cornell University Library copy (Internet Archive identifier `cu31924014590545`). The corresponding title page gives Charles, Oxford, Clarendon Press, and 1893. The external SPCK facsimile record shows 154 printed pages in a 160-page scan; the scanned title and preface identify the tenth impression as 1962, first published in 1917, reprinting the 1912 second edition. The repository copies are not asserted to be byte-identical to their public-hosted counterparts; their Git blobs and file sizes above identify the repository artifacts actually added.

The earlier two small PDFs remain valuable project artifacts and must be preserved. Their filenames do not establish that they are historical facsimiles. The two larger PDFs are the new scan sources and should be used for page-image work.

### Historical witness scope

- **1893 printed translation:** Sections I–V comprise Chapters 1–104, with Section V XCI–CIV. The printed translation pages continue with CV on p.301, CVI–CVII on pp.302–305, and CVIII on pp.305–308 as distinct appended literary units. Appendix E separately prints the New Latin fragment 106:1–18 on pp.372–375.
- **1917 Charles/Oesterley textual edition:** Chapters 105–108 are present. The scan stored in the repository is a 1962 tenth impression of the edition first published in 1917, and its preface describes the text as reprinted from Charles's 1912 second edition.
- Keep the repository's selected transcription and modernized derivative intact where they differ from these historical witnesses. Record the wording/order variants separately rather than silently substituting one edition for another.

### 1917 visual evidence boundary

The 1917 scan's actual page images have been visually inspected for printed pp. 150–151 and 153–154. Printed p. 152 remains an image-retrieval gap. The searchable text layer for Chapters 105–108 was examined, including the placement of 106:17a immediately after 106:14. Chapter 108 is present in the full SPCK scan and its ending is visible on pp. 153–154; its absence from the small 101-page repository transcription applies only to that older artifact.

### 1893 visual evidence boundary

The newly committed Cornell scan is the correct in-repository page-image witness for Chapters 1–104. The searchable OCR and critical apparatus have already been reviewed sequentially for those chapters, but printed pp. 55–308 have not yet received systematic page-by-page visual proofing. Do not report the 1893 image audit as complete.

## 1917 page-image audit clarification — 25 November 2026

To avoid conflating the repository's bundled PDF with the historical witness, the visual review is now explicitly recorded against the separate authentic 1917 Charles/Oesterley facsimile. The repository PDF (101 pages, Word/PDFMaker 2005) was also rendered at its final three pages, but it is only a modern typeset transcription and not a 1917 scan.

Authentic 1917 facsimile page-image status:
- Printed p. 150: inspected (Chapter 105:1–2 and the opening of 106:1).
- Printed p. 151: inspected (continuation of 106:1 through the beginning of 106:12).
- Printed p. 152: image retrieval failed; not inspected.
- Printed p. 153: inspected (end of 107 / start of 108).
- Printed p. 154: inspected (end of 108).

The authentic 1917 searchable text layer for 105–108 was examined. The image-based review of the whole 105–108 range remains incomplete because p. 152 is missing. Chapter 108's final two printed pages were inspected. This is distinct from the user-supplied repository PDF, which ends at 107:3.


### Charles 1912 second-edition scope clarification

The separately scanned 1912 second edition was examined as bibliographic/critical context for the later SPCK reprint. Charles's 1912 Introduction classifies 105 as an independent two-verse fragment, 106–107 as material from the Book of Noah, and 108 as a later appendix (see the searchable 1912 scan, pp. 34–35 / OCR lines 685–689: [1912 second-edition scan](https://iapsop.com/ssoc/1912__charles___book_of_enoch.pdf)). The 1912 contents list the translated sections through Chapter 104 and Appendix E as the Latin fragment 106:1–18; the 1912 volume does not provide a complete printed translation of 105–108 that could substitute for missing 1917 p.152. The 1917 preface explicitly says the SPCK translation reprints Charles's 1912 second edition, so its introduction and textual framing are relevant, but the full 105–108 reading sequence remains a separate 1917 witness.

## Follow-up visual page-image retrieval audit — 25 November 2026

This pass tested additional independently hosted image witnesses. **No new 1893 translation page has been counted as visually inspected.** The exact status is:

### 1893 Clarendon Press witnesses

- **Cornell / Internet Archive** (\`cu31924014590545\`): 428-page scan, 11.09 MB. The PDF and catalogue/title-page record identify the 1893 Clarendon edition. The page-rendering service rejected the original PDF as too large; attempts to retrieve internal page images did not return page pixels.
- **University of Michigan / Google Books** (\`bookenochtransl00dillgoog\`): distinct 418-page scan, 14.28 MB. The title page and bibliographic metadata identify the same 1893 Clarendon edition. The Commons PDF preview provides a title-page thumbnail, but attempts to render the translation pages (including the Section I/II boundary and representative later-section pages) returned content-size errors or cache misses. The title-page thumbnail is not evidence for the translation text.
- **Knox College / University of Toronto**: a third distinct digitization is mirrored as \"Charles_ed - Book of Enoch.pdf\" at the Luminist/Wasabi host. Its searchable PDF text identifies the Knox College copy and the Clarendon 1893 title page; the contents give the translation range as printed pp. 55–308. The page renderer refused the 30.5 MB PDF as too large, and a direct file download was unavailable in this environment. No internal page image from this witness was inspected.

These are three separate digitizations of the same bibliographic edition. They are not interchangeable file identities, and their scan-page counts differ. The currently available route exposes searchable text and some title-page previews, but not the actual translation-page images. Therefore visual collation of **all printed pp. 55–308 remains unstarted/unverified in this environment**; the previous searchable-text/apparatus review remains a separate form of evidence.

### 1917 SPCK witness — exact missing page re-tested

The 160-page Commons/Internet Archive PDF (\`bookofenoch0000unse\`) is independently identified as the SPCK edition first published in 1917; this scanned physical copy is the tenth impression of 1962 and its editors' preface states that the translation reprints Charles's 1912 second edition. The PDF-page mapping around the unresolved leaf is:

| Zero-based PDF index | Printed page | Visual result |
|---:|---:|---|
| 150 | 149 | Inspected as adjacent context |
| 151 | 150 | Inspected |
| 152 | 151 | Inspected |
| 153 | 152 | **Repeated cache miss; not inspected** |
| 154 | 153 | Inspected |
| 155 | 154 | Inspected |

The 1917 printed p.152 image was re-requested through the Commons-hosted 6.73 MB PDF as well as the earlier scan reference. Both attempts failed to return the image. A HathiTrust catalogue copy is listed as US-access-only; no second publicly retrievable page-image copy was found. Searchable text for the same passage is available, but it does not close the visual gap.

**Audit conclusion:** 1917 printed pp.149–151 and 153–154 have image evidence; p.152 remains open. For 1893, source identification and text-layer review are established, but there is still no visual proofing of pp.55–308. Do not label either visual task complete until the actual page pixels have been inspected and recorded against printed page numbers.


## Newly added edition PDFs inspected and classified — 25 November 2026

The \`pdfs/\` directory now contains seven PDFs. The newly added full scans are not merely extra copies of one source; they represent the following witness roles:

- **\`enoch-1893-opusmagnum.pdf\`** — 420-page, 11.6 MB OpusMagnum-hosted scan, per the addition commit. The hosted PDF text layer was opened and checked: its title page identifies R. H. Charles, Clarendon Press, 1893, and its contents identify the translated 1 Enoch range as printed pp. 55–308. Searchable text around printed p.57 includes Chapter I and its verse sequence. The new PDF is a better-sized first candidate for page imaging than the 34.95 MB Toronto file. However, page-image screenshot requests for the opened PDF returned cache misses (including the title/front pages and internal pages); **no translated page has been counted as visually inspected from this file**. The exact image lineage compared with the other scans is not yet established.
- **\`enoch-1893-utoronto.pdf\`** — 424-page, approximately 35 MB University of Toronto / Knox College digitization, per the addition commit. The Open Library record for the Toronto-held 1893 edition identifies the Clarendon Press 1893 title and Internet Archive identifier \`thebookofenoch00unknuoft\`. This establishes provenance but does not amount to visual inspection of its PDF pages in this environment.
- **\`enoch-1912-clarendon-2nd-edition.pdf\`** — 454-page University of Toronto / Robarts scan of Charles's revised second edition. The scanned title leaf records Oxford: Clarendon Press, 1912; the Source Library catalogue identifies the Robarts-held Internet Archive scan and its 454 page images. The contents place Chapters 91–104 in Section V, the separate Book of Noah fragment (106–107) at printed p.381, and Chapter 108 at p.385. This edition is a useful additional textual witness for portions of 106–108, but it is not the 1893 edition and cannot replace missing 1917 page images. Chapter 105 is not listed in its contents as a separate text section.

The updated [\`pdfs/README.md\`](../../../pdfs/README.md) now inventories all seven PDFs and distinguishes their evidentiary uses. The addition commits describe the OpusMagnum scan as “page-renderable”; I attempted to render its PDF pages directly, but the available screenshot service returned cache misses. The claim is therefore recorded as repository-provided acquisition metadata, not as an image inspection result from this audit.

**Visual status is unchanged:** the 1893 printed translation pages 55–308 still require actual page-image review. The 1917 scan's printed p.152 is still missing from the inspected image set (zero-based PDF page index 153). The new 1912 edition is a supplemental source only. Do not promote OCR or catalogue identification to visual verification.


## PDF directory relocation — 25 November 2026

The seven PDFs and their inventory README were moved from the former `enoch-editions/` directory to the top-level `pdfs/` directory. The move reused the existing Git blob objects, so the PDF contents and blob identifiers were preserved without downloading or re-uploading the binary files. Repository navigation, usage guidance, source notes, and review documentation now point to `pdfs/`. The former directory is no longer present.


## 1917 SPCK printed p.152 — successful image retrieval — 25 November 2026

**Supersedes the earlier failed-retrieval notes above for this one page only.** The Commons-hosted 160-page Internet Archive scan was opened successfully and zero-based PDF page index **153** was rendered. The printed leaf itself visibly carries page number **152**. Direct image: [1917 SPCK scan, PDF page index 153](https://upload.wikimedia.org/wikipedia/commons/c/c9/The_book_of_Enoch._Robert_Charles._1917_%28IA_bookofenoch0000unse%29.pdf).

Visual inspection confirms that the leaf continues the Noah birth narrative from 106:12, prints 106:13–19, places the giants-production clause immediately after 106:14, and begins Chapter 107 at the foot of the page. This is image evidence from the tenth impression (1962) of the SPCK edition first published in 1917. It closes the page-152 image gap; it does not constitute a full line-by-line collation of every reading on the page, and it does not alter the repository's selected wording or order.

The 1893 Clarendon page-image task remains separate and outstanding: printed pp.55–308 have not received systematic visual proofing.


## Repository PDF path and inventory correction — 25 November 2026

A live GitHub tree check confirms that the eight PDF artifacts are stored under `pdfs/enoch-editions/`, not directly under `pdfs/`. The inventory is maintained in `pdfs/README.md`. Earlier statements in this log that refer generically to files in `pdfs/` describe the parent collection, not the exact file paths. The Cornell 1893 scan used for this audit is `pdfs/enoch-editions/enoch-1893-clarendon-original.pdf` (Git blob `38be2b5e0e95779f92dcb19a745fc654b010b711`). The PDF's presence in GitHub does not by itself make its page pixels available to the current inspection tools; no additional page is marked image-checked by this path correction.


## Cornell 1893 searchable-text collation — printed pp.55–62 — 25 November 2026

A page-referenced searchable-text collation of Cornell extraction labels PAGE 77–84 (BookReader leaves n76–n83; printed pp.55–62) has been added in [`CORNELL_TEXT_LAYER_COLLATION_PP55-62.md`](CORNELL_TEXT_LAYER_COLLATION_PP55-62.md). It separates Charles's Section I introduction, English translation, critical apparatus, and the Greek Syncellus parallel; records representative differences from the repository's formatted Chapters 1–6; and lists OCR/layout defects separately from textual differences.

This is OCR/text-layer evidence only. It is not visual page-image proofing, does not establish a complete line-by-line collation, and does not change the 1893 image-proofing count or the repository transcription. In particular, V.8 (“Then too will wisdom…” / repository “Then to wisdom…”) and the VI.3 name require image confirmation before any correction is proposed.


## Chapter 89 editorial-identification audit and text-layer collation — printed pp.231–247 — 25 November 2026

The formatted Chapter 89 has been audited against the Cornell/Internet Archive searchable text and Charles's critical/exegetical notes. Thirteen repository-added parenthetical historical/geographical glosses were removed from the running translation and moved to a labelled editorial-identifications register after the chapter. Charles's own parenthetical clarification at 89:15 was retained. The audit corrected two misassigned identifications: 89:37 is Aaron (with the Exodus generation and Jordan context), while 89:38 is Moses; Joshua belongs among the later leaders at 89:39. The report records the identification register, evidence levels, and text-layer observations: [CHAPTER_89_IDENTIFICATION_AUDIT_AND_COLLATION_PP231-247.md](CHAPTER_89_IDENTIFICATION_AUDIT_AND_COLLATION_PP231-247.md).

**Evidence boundary:** searchable-text and commentary collation only; not page-image proofing or a complete diplomatic collation. The 1893 image-proofing ledger is unchanged. The verse wording itself was not rewritten beyond removing repository-added parenthetical glosses from the running text.


## Chapter 90 translation, variant, and commentary collation — printed pp.247–259 — 25 November 2026

A targeted collation of Chapter XC (90:1–42) has been recorded in [CHAPTER_90_COLLATION_PP247-259.md](CHAPTER_90_COLLATION_PP247-259.md). It distinguishes the repository translation, Charles's reported Ethiopic manuscript variants and emendations, and Charles's historical/exegetical commentary. The repository transcription was corrected for clear local artifacts at 90:1, 90:5, 90:14, and 90:40; repository-added parenthetical interpretations at 90:20 and 90:29 were moved out of the running translation and are attributed separately to commentary.

Key textual distinction: the 1893 translation prints **thirty-six** at 90:1, while Charles conjectures **thirty-five** from the arithmetic 12 + 23. The printed reading is retained; the conjecture is not silently substituted. Charles also brackets 90:15 as an interpolation and proposes interpreting 90:19 before 90:16; the repository retains the printed brackets and sequence. Charles's identifications (e.g. Judas Maccabaeus, Onias III, the Chasids, and the New Jerusalem) are recorded as commentary rather than translated wording.

**Evidence boundary:** Cornell OCR/text-layer and apparatus collation only. Printed pp.247–259 (BookReader indexes n268–n280) have not been visually inspected in this pass. No 1893 image-proofing count is increased; independent human review remains outstanding. This is not a complete diplomatic collation of every word or Ethiopic manuscript variant.

## Chapters 91–93 text-layer and apparatus collation — printed pp.260–273 — 25 November 2026

A sequential text-layer collation of Section V's introduction and Chapters XCI–XCIII is recorded in [CHAPTERS_91-93_COLLATION_PP260-273.md](CHAPTERS_91-93_COLLATION_PP260-273.md). The report separates the 1893 translation, manuscript variants and Charles's critical decisions, and Charles's historical/exegetical commentary. It records his proposed literary order XCII; XCI.1–10; XCIII.1–10; XCI.12–19; XCIV onward, while preserving the printed 1893 sequence and verse numbering.

Key apparatus points include the alternate word order in XCI.1; variants in XCI.3–9; the interpolation at XCI.11; the displacement of XCI.12–19; variants at XCI.13–19; the XCII.3 alternatives (G: “wisdom will arise” versus the printed “the righteous one will arise”); and variants in XCIII.2, 5–6, 9–10. Charles's interpretation of the ten weeks and his dating/authorship proposals are attributed to him rather than treated as textual readings or established historical facts.

**Evidence boundary:** Cornell searchable OCR/text-layer and commentary only. The direct image retrieval attempt for n268 failed; no pixels for n268–n280 were inspected. The image-proofing ledger was not changed and remains at 20 / 254 individually image-checked pages. Independent human review remains outstanding. This is a targeted collation, not a complete diplomatic transcription audit.

## Chapters 93–99 text-layer and apparatus collation — printed pp.274–288 — 25 November 2026

A sequential text-layer collation of XCIII.11–14, Chapters XCIV–XCIX, and the opening of Chapter C is recorded in [CHAPTERS_93-99_COLLATION_PP274-288.md](CHAPTERS_93-99_COLLATION_PP274-288.md). The report separates the 1893 translation, Charles's manuscript variants and critical decisions, and his historical/exegetical commentary. It records the four bracketed verses XCIII.11–14 as Charles's proposed interpolation from the Book of Celestial Physics, and XCVI.2 as a separate interpolation judgment.

The apparatus records variants in XCIV.1–11, XCV.1–7, XCVI.1–8, XCVII.2–10, XCVIII.1–16, and XCIX.1–16, including the G/G1 textual discontinuity beginning at XCVII.6b, the competing readings at XCIX.7 (“not according to knowledge” / “in idol temples”), and the variant “woe to them” / “woe to you” at XCIX.2. Two obvious repository transcription artifacts are identified against the printed OCR: “furnace of lire” at XCVIII.3 and “mean, into sinners” at XCIX.2. These corrections are limited to clear transcription errors; the report does not silently replace manuscript variants.

**Evidence boundary:** Cornell searchable OCR/text-layer and commentary only. No page pixels for pp.274–288 (BookReader n295–n309) were inspected. The image-proofing ledger remains unchanged at 20 / 254 individually image-checked pages. Independent human approval remains outstanding. This is a targeted collation, not a complete diplomatic transcription audit.


## Chapters C–CV text-layer and apparatus collation — printed pp.288–301 — 25 November 2026

The sequential collation of Chapters C–CV (100–105) is recorded in [CHAPTERS_100-105_COLLATION_PP288-301.md](CHAPTERS_100-105_COLLATION_PP288-301.md), completing the OCR/text-layer pass through the end of the repository's Book 5 scope. The report distinguishes the translation, Charles's apparatus, and his commentary, and records the major decisions at C.4–5, CI.4 (“sailors of the ships,” Charles's emendation), CII.4 bracket uncertainty, CIII.9–15 (Charles's deliberate third-person text against first-person witnesses), and CV (which Charles treats as outside XCI–CIV).

One clear transcription error was corrected in the formatted text at C.2: “his sons, and his sons” was corrected to “his sons and his sons’ sons.” The report also records the 1893 closing “Amen” after CV.2 as absent from the repository and pending facsimile confirmation; it does not silently insert it. Charles treats CVI–CVIII as a separate Noachian fragment, not part of the XCI–CV Book 5 scope.

**Evidence boundary:** Cornell searchable OCR/text-layer and commentary only. No page pixels for pp.288–301 (BookReader n309–n322) were inspected. The image-proofing ledger remains unchanged at 20 / 254 individually image-checked pages. Independent human approval remains outstanding. This is a targeted collation, not a complete diplomatic transcription audit.


## Scope clarification — 1893 Section V and appended chapters CV–CVIII

The 1893 contents label Section V as XCI–CIV, while the translation pagination runs through pp.265–308. The printed text continues after CIV with CV.1–2 on p.301, CVI–CVII on pp.302–305, and CVIII on pp.305–308. Charles explicitly treats CV as outside the literary composition XCI–CIV, CVI–CVII as a fragment of a Noah Apocalypse, and CVIII as an independent final addition. These chapters are nevertheless printed in the 1893 volume. Appendix E separately contains a Latin fragment of CVI.1–18 on pp.372–375; it is a distinct witness from the Ethiopic translation in the main pagination.

The earlier attempt to exclude CV–CVIII from the 1893 volume was incorrect and is superseded. The corrected report [CHAPTERS_100-105_COLLATION_PP288-301.md](CHAPTERS_100-105_COLLATION_PP288-301.md) records CV.1–2 and its printed closing “Amen.” The text-layer collation of pp.302–308 is recorded in [CHAPTERS_106-108_COLLATION_PP302-308.md](CHAPTERS_106-108_COLLATION_PP302-308.md). The 1917 Charles/Oesterley witness remains a parallel later witness for comparison, not the sole basis for these chapters.

This clarification does not establish full facsimile proofing. The IMAGE_PROOFING_LOG reports 234 images retrieved for pp.75–308, but they are not individually checked. In this session, attempts to reopen BookReader medium/large images, the IIIF manifest, and ArchiveLab page endpoints did not return pixels. The individually inspected count remains 20 / 254. Independent human approval remains outstanding.


## Chapters CVI–CVIII text-layer and apparatus collation — printed pp.302–308 — 25 November 2026

The collation is recorded in [CHAPTERS_106-108_COLLATION_PP302-308.md](CHAPTERS_106-108_COLLATION_PP302-308.md). The report distinguishes the 1893 Ethiopic translation on pp.302–308 from the separate Latin CVI.1–18 fragment in Appendix E (pp.372–375), and from the parallel 1917 Charles/Oesterley witness. It records Charles's explicit identification of CVI–CVII as a Noah Apocalypse fragment and CVIII as an independent addition. Textual decisions include the G/G1/M variants in CVI.9–16 and CVII.1–3, Charles's omission of unsupported Dillmann wording at CVI.16, the proposed relocation of the first half of CVI.17 after v.14, and variants in CVIII.2–3 and 11–15.

**Evidence boundary:** Cornell OCR/text-layer and apparatus only. No page pixels for pp.302–308 (BookReader n323–n329) were inspected. The IMAGE_PROOFING_LOG reports these images as retrieved but not individually checked. The visual proofing count remains 20 / 254. Independent human approval remains outstanding.


## Final proofing tracker

The remaining facsimile and independent-review requirements are tracked in [GitHub issue #1 — Complete 1 Enoch 1893 facsimile proofing and independent review](https://github.com/hasnocool/ancient-books-study/issues/1). This issue does not change the proofing ledger or imply that review has occurred.
