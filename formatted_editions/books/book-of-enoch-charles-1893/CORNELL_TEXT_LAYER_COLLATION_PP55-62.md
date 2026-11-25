# Cornell 1893 text-layer collation — printed pp. 55–62

**Date:** 25 November 2026  
**Repository base:** `main` at commit `bdfd4219ea9b6bb9d6e75b22414a40a6e51694b1`  
**OCR input:** `pdfs/extracted/cornell_pages_75_84_text.txt`  
**Formatted comparison text:** `book-01-watchers-chapters-01-36.md`  
**Witness:** R. H. Charles, *The Book of Enoch* (Oxford: Clarendon Press, 1893), Cornell copy, Internet Archive identifier `cu31924014590545`.



**OCR extraction location:** The original tracked extraction was restored from the parent commit after a later commit removed it without the stated replacement appearing in the tree. The restored file contains PDF ordinals PAGE 75–84: printed p.53, a blank PAGE 76, and printed pp.55–62. The filename refers to PDF ordinals, not printed folios. It does **not** supply OCR for printed pp.63–74.

## Scope and evidentiary limits

This is a **searchable-text collation**, not visual page-image proofing. The OCR file's labels are one-based PDF page ordinals. The Cornell BookReader page indices are zero-based. For this batch, extraction labels PAGE 77–84 correspond to BookReader leaves n76–n83 and printed pages 55–62. PAGE 75 is printed p.53; PAGE 76 is empty and falls outside this printed-page batch.

The OCR layer is imperfect and mixes the two-column page layout. It frequently interleaves translation, footnotes, critical notes, and (on p.62) a Greek parallel text. A line's position in the extracted text is not by itself sufficient to classify it as part of the translation. The printed folio read as “53” in PAGE 80 is inconsistent with the neighboring folios 57 and 59 and with the established leaf mapping; for this batch it is treated as an OCR folio-recognition error, not as a change to the page map.

The formatted file explicitly says its wording is not a verbatim transcription of the 1893 printing. Accordingly, differences below are **witness differences**, not automatic corrections to either text. No wording in the formatted transcription has been changed.

## Page map and content classification

| Printed page | OCR label / BookReader leaf | Main printed content | Text-layer observations |
|---:|---|---|---|
| 55 | PAGE 77 / n76 | Section I heading and critical introduction; opening of “Critical Structure” | OCR corrupts the contents list and several Roman numerals; no translation begins on this page. |
| 56 | PAGE 78 / n77 | Continuation of Section I introduction: relations to other sections, date, and problem/solution | Critical/editorial prose, not Enoch's translated narrative. |
| 57 | PAGE 79 / n78 | End of the introduction; translation begins at I.1; notes on I.2 | Two-column interleaving begins. Translation and apparatus must be separated. |
| 58 | PAGE 80 / n79 | Continuation of I.3–8; critical notes on I.3–8 | OCR interleaves the translation with variant readings and Charles's comments. The displayed folio “53” is erroneous in this extraction sequence. |
| 59 | PAGE 81 / n80 | I.8–9; II.1–3; beginning of III.1; notes on I.9 and II | Contains translation and extensive apparatus; OCR column order is scrambled. |
| 60 | PAGE 82 / n81 | Continuation of III.1; IV; V.1–5; notes on III–V | OCR includes a likely duplicated/misrecognized verse numeral before V.3; do not use OCR line order to infer verse numbering. |
| 61 | PAGE 83 / n82 | V.5–9; notes on V.5–9 and the VI–XI unit | Apparatus discusses textual readings and the Semjaza / Noah-cycle material. |
| 62 | PAGE 84 / n83 | VI.1–4 begins; Greek version of Enoch from Syncellus (6.1–9.4); notes on VI | Three distinct textual zones are present: Ethiopic-based English translation, Greek parallel, and critical apparatus. The OCR truncates the English text at VI.4. |

## Comparison with the formatted repository transcription

The formatted comparison file covers Chapters 1–6 in this range. Its editorial statement already identifies it as a repository wording derivative, with verse structure restored from Charles as a structural reference. The following examples are visible in the OCR and are not a complete diplomatic collation of every word.

| Passage | 1893 text layer (OCR reading) | Formatted repository reading | Classification |
|---|---|---|---|
| I.1 | “The words of the blessing of Enoch” | “These are the words of blessing of Enoch” | Lexical / clause-level difference; not an OCR-only punctuation issue. |
| I.2 | “And Enoch answered and spake—(Enoch) a righteous man” | “Enoch answered and spoke: I, Enoch, a righteous” | Substantive phrasing and syntax difference. |
| I.3 | “Concerning the elect I spake”; “the Holy and Great One” | “Concerning the elect I spoke”; “the Holy, and Great One” | Modernized verb form and punctuation difference. |
| I.4 | “And going from thence He” | “Going from thence He” | Omission of “And” in repository wording. |
| I.8 | “But to the righteous He will give peace and will protect the elect” | “But to the righteous, He will give peace, and will protect the elect” | Punctuation difference. |
| I.9 | “And lo! He comes with ten thousands of (His) holy ones” | “Lo! He comes with ten thousands of His holy ones” | Opening conjunction and supplied “(His)” differ. |
| II.1 | “I observed everything that took place in the heaven, how…” | “I observed everything that took place in the heaven; how…” | Punctuation difference. |
| II.2 | “Behold ye the earth” | “Behold you the earth” | Pronoun modernization. |
| II.3 | “Behold the summer and the winter, how (in the winter season)…” | “Behold the summer, and the winter, how…” | Charles's parenthetical clarification is absent from the repository wording. |
| III.1 | “all the trees” / “till the new comes” | “all the trees” / “until the new comes” | Minor wording modernization; OCR line break is not a textual omission. |
| IV | “And again I observed…” | “Again, I observed…” | Opening conjunction and punctuation differ. |
| V.1 | “wherefore give ye heed”; “He who liveth for ever” | “Wherefore give you heed”; “He who lives for ever” | Pronoun and verb modernization. |
| V.4 | “ye have not continued steadfast”; “ye will find no peace” | “you have not continued steadfast”; “you will find no peace” | Pronoun modernization; most of the clause is otherwise aligned in this OCR sample. |
| V.5 | “be bereft of the years of your life” | “be deprived of the years of your life” | Lexical difference. |
| V.6 | “you together with (all other) sinners” | “you together with sinners” | Parenthetical qualification present in Charles's printed translation is absent from repository wording. |
| V.8 | “Then too will wisdom be bestowed on the elect” | “Then to wisdom will be bestowed on the elect” | Apparent substantive wording/grammar difference; verify against page pixels before proposing a correction. |
| V.9 | “And they will not be punished…” | “They will not be punished…” | Opening conjunction omitted in repository wording. |
| VI.1 | “And it came to pass…” | “It came to pass…” | Opening conjunction omitted in repository wording. |
| VI.2 | “And the angels… saw and lusted… and spake” | “The angels… saw, and lusted… spoke” | Opening conjunction, punctuation, and verb modernization. |
| VI.3 | OCR reads “Semjizi”; the printed English translation brackets this verse | Repository uses “[3.] Semjaza…” | Name is OCR-uncertain; bracketed status agrees, but spelling must not be normalized from OCR alone. |

**Important:** The table records observed differences, not a verdict that Charles's 1893 wording must replace the repository text. The source transcription's own declared editorial policy is to preserve its wording pending collation. The apparent V.8 reading “Then to wisdom” is especially worth checking against the image because OCR can misrecognize short words and punctuation.

## Translation versus apparatus versus Greek parallel

The OCR extraction should be parsed into separate evidence classes:

1. **Charles's English translation:** The running numbered text beginning at I.1 on p.57, continuing through I–V on pp.57–61, and beginning VI.1–4 on p.62.
2. **Charles's critical apparatus and commentary:** Material keyed to verse numbers, including the discussions of “God” / “Lord” and “Vision of the Holy One” (p.57); the alternative reading in I.3, “earth will be rent” in I.7, “Watchers,” and the interpretation of the judgment (p.58); the “will convict / will plead” variant in I.9 and explanatory notes on II (p.59); notes on the fourteen evergreen trees and V.4–5 (p.60); the textual discussion of V.5–6, the reading supported by G and the Greek, and Charles's analysis of the VI–XI units (p.61); and the notes on VI.2–3 (p.62).
3. **Greek parallel text:** The heading on p.62 identifies “Fragments of the Greek Version of Enoch preserved in the Chronography of G. Syncellus,” edited by Dindorf (1829). Its Greek text is a separate witness, beginning with a parallel to Enoch 6:1–9:4. It is not part of Charles's English translation and must not be merged into the repository's English reading text.
4. **Sectional / editorial introduction:** The prose on pp.55–57 before the “TRANSLATION” heading is Charles's introduction to Section I, not a passage of 1 Enoch.

## OCR defects and unresolved readings

Record these as OCR or layout issues unless the page image establishes a printed anomaly:

- PAGE 77 contents list: “lxxii- / Ixxxti,” “Ixxxi,” “C Ixxxti,” and “C. [és Date” are visibly corrupted Roman numerals / headings.
- PAGE 78: several Roman numerals and bibliographic references are misrecognized (e.g. “Ixxxiii-xe,” “161 B.c.” capitalization, and broken hyphenation).
- PAGE 79: “G. 1.” is OCR for the chapter/verse heading “I. 1.”; the column sequence mixes translation and notes.
- PAGE 80: folio “53” conflicts with the adjacent printed-page sequence; “prote c…” is a line/column truncation; the Ethiopic and Greek transliteration strings are heavily corrupted.
- PAGE 81: “SHAG” is an OCR corruption in the note's Ethiopic transliteration; the Greek words are noisy; note columns are interleaved with II.1–3.
- PAGE 82: “themselvese” is an OCR artifact for “themselves”; the V.3 numbering appears duplicated or displaced in OCR; “mul-” continues on p.61.
- PAGE 83: “the.” in “inherit the. earth,” “g.” before “And they will not be punished,” and split “sin.” are layout/OCR artifacts; the apparatus is interleaved with the translation.
- PAGE 84: “Semjizi” may be a recognition error or reflect the printed transliteration and requires image confirmation; Greek polytonic text is severely degraded; the OCR stops during VI.4.

## Status and next actions

- [x] Confirmed extraction file and formatted comparison file at the stated repository commit.
- [x] Established page-ordinal / BookReader / printed-page relationship for this batch.
- [x] Identified representative lexical, syntactic, and punctuation differences between the 1893 text layer and the repository wording.
- [x] Separated the English translation, Charles's apparatus, Section I introduction, and Greek Syncellus parallel as distinct source layers.
- [x] Recorded OCR and two-column layout defects separately from textual differences.
- [ ] Verify the uncertain readings (especially V.8, the VI.3 name, and the page-80 folio) against actual page pixels.
- [ ] Complete a full line-by-line collation of every verse and note on pp.55–62.
- [ ] Conduct page-image proofing. No new page is marked visually inspected by this report.

**Proofing count:** unchanged. This report uses the OCR text layer only and does not increase the 1893 image-proofing total.
