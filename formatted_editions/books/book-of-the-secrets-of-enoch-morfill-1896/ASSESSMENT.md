# 2 Enoch (Morfill/Charles 1896) — Source and Provenance Assessment

**Assessment date:** 2026-11-27  
**Work identity:** 2 Enoch / The Book of the Secrets of Enoch / Slavonic Enoch  
**Selected edition:** W. R. Morfill, translator; R. H. Charles, editor, Oxford: Clarendon Press, 1896  
**Assessment status:** Source structure reviewed; derivative production not yet started by this assessment.

## 1. Work identity and scope

2 Enoch is a distinct work and must not be merged with 1 Enoch. The selected edition's repository directory is:

`formatted_editions/books/book-of-the-secrets-of-enoch-morfill-1896/`

The formatted main text comprises:

- A separately displayed prologue (one numbered verse).
- 68 main chapters.
- 360 numbered verses across the 68 chapters.
- A separate five-section Melchizedekian appendix (104 verse entries).

The four main-text files are:

| File | Coverage |
|---|---|
| `chapters-01-17.md` | Prologue and chapters 1–17 |
| `chapters-18-34.md` | Chapters 18–34 |
| `chapters-35-51.md` | Chapters 35–51 |
| `chapters-52-68.md` | Chapters 52–68 |

The appendix is maintained separately in `melchizedek-appendix-sections-i-v.md`. Do not silently renumber its sections as chapters 69–73: that numbering occurs in some later retypes, whereas the 1896 edition presents sections I–V.

## 2. Selected source and provenance

The main chapter/verse text is based on the structured USFM transcription `texts/jewish-morfill/2-enoch.usfm` in `rewtraw/anagnosis-texts`:

https://github.com/rewtraw/anagnosis-texts/blob/main/texts/jewish-morfill/2-enoch.usfm

The USFM source note identifies the 1896 Morfill/Charles edition and says its character-level OCR was collated and corrected by hand from two scans:

- Internet Archive item `bookofsecretsofe00morf`
- Internet Archive item `cu31924014633568`

The USFM source explicitly excludes Charles's introduction, critical apparatus, commentary, and the Melchizedek appendix. It identifies the translated work as public domain (published 1896).

The repository's own standalone OCR comparison witness is:

`books_05/The Book of the Secrets of Enoch translated from the Slavonic by W R Morfill 1896.txt`

A second comparison file, `books_02/The Book of Enoch.txt`, interleaves Slavonic 2 Enoch material with 1 Enoch and is not a safe direct extraction base without careful filtering. The standalone `books_05` file is the preferable in-repository OCR witness for future comparisons.

## 3. Structural transfer evidence

The existing edition README records an automated comparison against the selected USFM source:

- All 68 chapter headings were found.
- All 361 verse labels were found (one prologue verse plus 360 main-text verses).
- After removal of USFM markers and Markdown labels, all 361 verse bodies matched the USFM source exactly and in sequence.
- No main-text body mismatches were reported in that transfer comparison.

This establishes structural and textual transfer from the selected USFM transcription into the four Markdown files. It does **not** establish that the USFM transcription itself is correct against the 1896 facsimile. The repository's formatted edition remains a transcription draft, not an independently facsimile-collated or critical edition.

## 4. Melchizedekian appendix

The appendix is formatted separately from the standalone repository OCR. Its five sections contain:

| Section | Entries |
|---|---:|
| I | 19 |
| II | 26 |
| III | 37 (including bracketed manuscript variant III.31) |
| IV | 11 |
| V | 11 |
| **Total** | **104** |

The appendix README records that section and verse boundaries were cross-checked against a clean retype. The appendix wording has not been collated line by line against page images.

The printed introduction itself describes the fragment as a Melchizedekian addition found in a particular manuscript tradition, notes that it is absent from other manuscripts, and calls the text corrupt in many places. These are important editorial qualifications and must accompany any later derivative. The appendix is not simply an undisputed continuation of the 68-chapter main text.

The OCR contains visibly suspect readings and typographic/transcription noise. Examples in the current formatted appendix include forms such as “Laraech,” “thq,” “flom,” “tlie,” and “3 ears,” as well as inconsistent names and punctuation. These are review targets, not authorized corrections. Preserve the printed/OCR reading until checked against the scan; do not silently normalize names, chronology, measures, or theological language.

## 5. Rights and redistribution

The selected translation was published in 1896. The USFM source and the repository README identify the 1896 translation as public domain in the United States. The Cornell OCR front matter also states that there are no known US copyright restrictions on use of the text.

However:

- No repository-specific rights record for this 2 Enoch edition was found under `copyrighted_works/`.
- Public-domain status of the 1896 printed translation does not automatically establish the licensing terms of a modern digital transcription or the third-party USFM compilation in every jurisdiction.
- The third-party USFM source documents its scan provenance and public-domain assertion, but its digital-transcription reuse terms should be checked before copying substantial transcription text into derivative or redistributed files.
- Any derivative should identify the 1896 translation as its textual basis and avoid implying that the work is a modern translation or a critical edition.

**Rights decision:** The historical translation is a strong public-domain candidate in the United States. Derivative production should proceed only with explicit attribution and a documented jurisdiction/digital-transcription rights note; do not assume a repository-wide license.

## 6. Editorial production recommendations

1. Keep 2 Enoch under its own stable slug, separate from 1 Enoch.
2. Preserve the four main-text chapter files and their verse numbering as the source references.
3. Keep the Melchizedekian appendix in its own directory/file identity and assess it separately from chapters 1–68.
4. Treat the main text as structurally transferred from a manually collated third-party USFM transcription, but not facsimile-verified by this project.
5. Treat the appendix as an OCR-derived draft with a higher visible transcription-risk profile.
6. If chapter-level derivatives are created, identify exact chapter coverage and source file, preserve sequence and qualifications, and mark them provisional.
7. Do not create a continuous narrative that merges the main text and appendix. The appendix's manuscript status and editorial introduction are material.
8. Do not silently repair suspect names, measurements, chronology, or OCR readings. Carry unresolved readings into source notes for later image collation.

## 7. Current completion boundary

**Completed by this assessment:** work identity, selected edition identification, repository file map, chapter/verse counts as recorded in the edition README, source-transcription provenance, transfer-validation claims, appendix structure, and initial rights-risk assessment.

**Not completed:** independent verification of the USFM text against the 1896 page images; line-by-line collation of the appendix; jurisdiction-specific legal review of digital-transcription reuse terms; creation or review of story/meaning derivatives; independent human approval.

No facsimile verification, derivative completion, or human approval is claimed by this assessment.
