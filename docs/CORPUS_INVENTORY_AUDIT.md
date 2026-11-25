# Corpus Inventory and Risk Audit

**Audit date:** 2026-11-25  
**Repository:** `hasnocool/ancient-books-study`  
**Scope:** Git-tree inventory of the five archival directories `books_01`–`books_05`, exact-byte duplicate groups, empty placeholders, and targeted provenance / rights / OCR signal checks.

## Method and limitations

The inventory was calculated from the complete, untruncated Git tree for the default branch at tree SHA:

`867210a4e1898fba0155ae0885a7d35b7810e3e0`

The tree contains only 165 files under the five numbered archival directories, all with a `.txt` extension. File sizes and Git blob SHA values were read from the tree metadata. Files with identical blob SHAs are byte-for-byte identical; this is stronger evidence than matching filenames or similar titles.

A targeted sample of file contents and repository search matches was inspected for rights notices, title-page metadata, and OCR damage. This was a **remote metadata and targeted content audit**, not a complete local execution of the project's Python toolkit. Attempts to obtain a local clone failed because the runtime could not resolve `github.com`. The required local commands remain outstanding:

```bash
python3 tools/audit_corpus.py all --json-out /tmp/ancient-books-audit.json
python3 -m unittest discover -s tests -v
```

No archival files were edited, deleted, merged, renamed, or normalized during this audit. The numbers below describe the repository tree at the recorded SHA; any new commits can change them.

## Inventory summary

| Directory | Files | Bytes | Empty files |
|---|---:|---:|---:|
| `books_01` | 24 | 57,790,592 | 2 |
| `books_02` | 39 | 58,897,259 | 4 |
| `books_03` | 27 | 52,443,399 | 0 |
| `books_04` | 34 | 17,769,006 | 4 |
| `books_05` | 41 | 16,804,622 | 14 |
| **Total** | **165** | **203,704,878** | **24** |

All 165 files are text files. No PDF or EPUB files occur directly in these five archival directories in the inspected tree.

### Empty placeholders

The following 24 files have a Git blob size of zero bytes:

| Directory | Empty path |
|---|---|
| `books_01` | `Lost_Realms.txt` |
| `books_01` | `Manual_of_Vampyric_Alchemy.txt` |
| `books_02` | `2015.325544.Samarangana-sutradhara.txt` |
| `books_02` | `2015.345259.Samarangana-Sutradhara.txt` |
| `books_02` | `2015.513517.Yukti-Kalpataru.txt` |
| `books_02` | `ABridgeOfTheRomanHistoriesFromTitusLiviusToCorneliusTacitus.txt` |
| `books_04` | `10 megaton Mike crater filled with Pentagons DECEPTIVE PROPAGANDA FILM STILL Eniwetok coral is more easily cratered than continental geology 374-ANT-21-CLI-01-001.txt` |
| `books_04` | `10689.16618.txt` |
| `books_04` | `Ancient_Indian_Aviation_CIA.txt` |
| `books_04` | `Popol_Vuh_Dresden_Codex.txt` |
| `books_05` | `10 megaton Mike crater filled with Pentagons DECEPTIVE PROPAGANDA FILM STILL Eniwetok coral is more easily cratered than continental geology 374-ANT-21-CLI-01-001.txt` |
| `books_05` | `10689.16618.txt` |
| `books_05` | `2015.325544.Samarangana-sutradhara.txt` |
| `books_05` | `2015.345259.Samarangana-Sutradhara.txt` |
| `books_05` | `2015.513517.Yukti-Kalpataru.txt` |
| `books_05` | `ABridgeOfTheRomanHistoriesFromTitusLiviusToCorneliusTacitus.txt` |
| `books_05` | `Ancient_Indian_Aviation_CIA.txt` |
| `books_05` | `Lost_Realms.txt` |
| `books_05` | `Manual_of_Vampyric_Alchemy.txt` |
| `books_05` | `Popol_Vuh_Dresden_Codex.txt` |
| `books_05` | `The_Rhind_Papyrus_Volume_1.txt` |
| `books_05` | `Voynich_Manuscript.txt` |
| `books_05` | `Wars_of_Gods_and_Men.txt` |
| `books_05` | `cia-rdp79-01194a000100460001-5.txt` |

These are empty placeholders, not evidence that the titled works are unavailable elsewhere in the repository or that the titles themselves are invalid. The duplicate zero-byte entries likely reflect collection-batch mirroring. Do not remove them until their intended role and replacement references are checked.

## Exact-byte duplicate candidates

The 43 groups below contain 100 non-empty files. Each member of a group has the same Git blob SHA, meaning the file bytes are identical. The groups therefore account for 57 extra copies beyond one representative per group.

There is one additional exact-hash group consisting of the 24 empty placeholders listed above. That group is not repeated here.

These are preservation and organization candidates, not automatic deletion instructions. The archive directories are collection batches; retaining copies may have historical or workflow value even when their bytes match. A future deduplication proposal should choose a canonical path, preserve a manifest of former locations, and update every inbound link before any removal.

### Group 1 — *Parallels: Ancient Insights Into Modern UFO Phenomena*
- `books_01/Parallels Ancient Insights Into Modern UFO Phenomena - Richard L. Thompson.txt`
- `books_02/Parallels Ancient Insights Into Modern UFO Phenomena - Richard L. Thompson_1.txt`
- `books_02/Parallels Ancient Insights Into Modern UFO Phenomena - Richard L. Thompson_2.txt`
- `books_03/Parallels Ancient Insights Into Modern UFO Phenomena - Richard L. Thompson_3.txt`
- `books_03/Parallels_UFO_Phenomena.txt`
- `books_05/Parallels Ancient Insights Into Modern UFO Phenomena - Richard L. Thompson.txt`
- `books_05/Parallels Ancient Insights Into Modern UFO Phenomena - Richard L. Thompson_3.txt`

### Group 2 — *Al-Zahrawi the Founder of Surgery*
- `books_01/Al-Zahrawi the founder of Surgery_compressed_1.txt`
- `books_02/Al-Zahrawi the founder of Surgery_compressed.txt`
- `books_03/Al-Zahrawi the founder of Surgery_compressed_1.txt`
- `books_05/Al-Zahrawi the founder of Surgery_compressed.txt`

### Group 3 — *India's Glorious Scientific Tradition*
- `books_01/India_s Glorious Scientific Tradition - Suresh Soni.txt`
- `books_02/India's Glorious Scientific Tradition - Suresh Soni.txt`
- `books_04/India_s Glorious Scientific Tradition - Suresh Soni_1.txt`
- `books_04/Indias_Glorious_Scientific_Tradition.txt`

### Group 4 — *Ancient Egypt and Paris*
- `books_02/Ancient Egypt and Paris_ the influence of Ancient Egypt on Paris from the goddess Isis to Ramses II_ Champollion_ Parisian pyramids and obelisks_.txt`
- `books_02/Ancient Egypt and Paris_ the influence of Ancient Egypt on Paris from the goddess Isis to Ramses II_ Champollion_ Parisian pyramids and obelisks__1.txt`
- `books_03/Ancient Egypt and Paris_ the influence of Ancient Egypt on Paris from the goddess Isis to Ramses II_ Champollion_ Parisian pyramids and obelisks__1.txt`
- `books_05/Ancient Egypt and Paris_ the influence of Ancient Egypt on Paris from the goddess Isis to Ramses II_ Champollion_ Parisian pyramids and obelisks_.txt`

### Group 5 — *Ancient Indian Aviation / CIA document text*
- `books_02/Ancient_Indian_Aviation_06928824.txt`
- `books_03/06928824.txt`
- `books_04/06928824.txt`
- `books_05/Ancient_Indian_Aviation_06928824.txt`

### Group 6 — Jay Winter *Complete Book of Enoch*
- `books_01/Complete_Book_of_Enoch_Jay_Winter.txt`
- `books_01/The Complete Book of Enoch_ Standard English Version by Jay Winter.txt`
- `books_03/Complete_Book_of_Enoch_Jay_Winter.txt`

### Group 7 — *A Planned Deception*
- `books_01/APlannedDeception.txt`
- `books_02/APlannedDeception.txt`

### Group 8 — Aramaic Text, Volume 1
- `books_01/Aramaic_Text_Vol1.txt`
- `books_03/Aramaic_Text_Vol1.txt`

### Group 9 — *Bhagavad Gita*
- `books_01/Bhagavad_Gita.txt`
- `books_02/Bhagavad_Gita.txt`

### Group 10 — *Book of Enoch* (screen transcription)
- `books_01/Book-of-Enoch (screen).txt`
- `books_03/Book-of-Enoch (screen).txt`

### Group 11 — *Genesis Revisited*
- `books_01/Genesis_Revisited.txt`
- `books_03/Genesis_Revisited.txt`

### Group 12 — *Giza Power Plant*
- `books_01/Giza_Power_Plant.txt`
- `books_02/Giza_Power_Plant.txt`

### Group 13 — *The Kybalion*
- `books_01/Kybalion_Three_Initiates.txt`
- `books_05/Kybalion_Three_Initiates.txt`

### Group 14 — *Temple of the Ancients*
- `books_01/Temple of the Ancients.txt`
- `books_05/Temple of the Ancients.txt`

### Group 15 — *The Book of Jasher* (1887)
- `books_01/The Book Of Jasher - 1887.txt`
- `books_02/The Book Of Jasher - 1887.txt`

### Group 16 — *The Nag Hammadi Library*
- `books_01/The Nag Hammadi Library - Gnostic gospels and texts.txt`
- `books_04/The Nag Hammadi Library - Gnostic gospels and texts.txt`

### Group 17 — Valmiki *Ramayanam*
- `books_01/Valmiki_Ramayanam.txt`
- `books_02/Valmiki Ramayanam.txt`

### Group 18 — *Samarangana Sutradhara* identifier 2015.552563
- `books_02/2015.552563.samarangana-sutradhara.txt`
- `books_05/2015.552563.samarangana-sutradhara.txt`

### Group 19 — *Acta Latomorum*, Volume II (1815)
- `books_02/Acta Latomorum ou Chronologie de L_Histoire de la Franc-Maconnerie Vol II - 1815.txt`
- `books_05/Acta Latomorum ou Chronologie de L_Histoire de la Franc-Maconnerie Vol II - 1815.txt`

### Group 20 — *Ancient Egyptian Medicine: The Papyrus Ebers*
- `books_02/ANCIENT EGYPTIAN MEDICINE THE PAPYRUS EBERS.txt`
- `books_04/ANCIENT EGYPTIAN MEDICINE THE PAPYRUS EBERS.txt`

### Group 21 — Ancient Egyptian medical text, archive identifier `ancientegyptianm00garl`
- `books_02/ancientegyptianm00garl.txt`
- `books_03/ancientegyptianm00garl_1.txt`

### Group 22 — Rhind Mathematical Papyrus, Volume II
- `books_02/Arnold Buffum Chace, Ludlow Bull, Henry Parker Manning - The Rhind Mathematical Papyrus. Volume II. Photographs, Transcription, Transliteration, Literal Translation. 2-Mathematical Association of Amer.txt`
- `books_04/Arnold Buffum Chace, Ludlow Bull, Henry Parker Manning - The Rhind Mathematical Papyrus. Volume II. Photographs, Transcription, Transliteration, Literal Translation. 2-Mathematical Association of Amer.txt`

### Group 23 — Jaffe, *Crucibles* (1957)
- `books_02/Bernard Jaffe - Crucibles_ The Story of Chemistry - From Ancient Alchemy to Nuclear Fission _1957_.txt`
- `books_03/Bernard Jaffe - Crucibles_ The Story of Chemistry - From Ancient Alchemy to Nuclear Fission _1957_.txt`

### Group 24 — *Book of Jasher* (1887)
- `books_02/Book_of_Jasher_1887.txt`
- `books_05/Book_of_Jasher_1887.txt`

### Group 25 — *Earth Chronicles Handbook*
- `books_02/Earth_Chronicles_Handbook.txt`
- `books_04/Earth_Chronicles_Handbook.txt`

### Group 26 — *Enochian Keys Rewritten*
- `books_02/Enochian Keys ReWriten.txt`
- `books_03/Enochian Keys ReWriten.txt`

### Group 27 — Ethiopic Version
- `books_02/Ethiopic_Version.txt`
- `books_03/Ethiopic_Version.txt`

### Group 28 — *Introduction to the Zohar*
- `books_02/Intro_To_Zohar.txt`
- `books_05/Intro_To_Zohar.txt`

### Group 29 — *Journeys in the Mythical Past*
- `books_02/Journeys_Mythical_Past.txt`
- `books_03/Journeys_Mythical_Past.txt`

### Group 30 — *Prayagraj Yatra: The King of Thirthas*
- `books_02/Prayagraj Yatra - The King of Thirthas_1.txt`
- `books_04/Prayagraj Yatra - The King of Thirthas.txt`

### Group 31 — *The Book of Enoch*
- `books_02/The Book of Enoch.txt`
- `books_05/The Book of Enoch.txt`

### Group 32 — Morfill, *The Book of the Secrets of Enoch* (1896)
- `books_02/The Book of the Secrets of Enoch translated from the Slavonic by W R Morfill 1896.txt`
- `books_05/The Book of the Secrets of Enoch translated from the Slavonic by W R Morfill 1896.txt`

### Group 33 — *The Vimanika Shastra*
- `books_02/the_vimanika_shastra.txt`
- `books_05/Vimanika_Shastra.txt`

### Group 34 — Archive identifier `9781787359154`
- `books_03/9781787359154.txt`
- `books_04/9781787359154.txt`

### Group 35 — *Divine Encounters*
- `books_03/Divine_Encounters.txt`
- `books_04/Divine_Encounters.txt`

### Group 36 — Sushruta text, archive identifier `englishtranslati00susruoft`
- `books_03/englishtranslati00susruoft_1.txt`
- `books_05/englishtranslati00susruoft.txt`

### Group 37 — *The Gospel of Thomas*
- `books_03/The Gospel Of Thomas.txt`
- `books_04/Gospel_of_Thomas.txt`

### Group 38 — Sitchin, *The King Who Refused to Die*
- `books_03/The King Who Refused to Die- Zecharia Sitchin.txt`
- `books_05/The King Who Refused to Die- Zecharia Sitchin.txt`

### Group 39 — Charlesworth, *The Old Testament Pseudepigrapha*, Volume 1 (1983)
- `books_03/The_Old_Testament_Pseudepigrapha_vol.1_Charlesworth_1983.txt`
- `books_05/The_Old_Testament_Pseudepigrapha_vol.1_Charlesworth_1983.txt`

### Group 40 — Archive identifier `132_7Mai2013b`
- `books_04/132_7Mai2013b.txt`
- `books_05/132_7Mai2013b.txt`

### Group 41 — *There Were Giants Upon the Earth*
- `books_04/7-There Were Giants Upon the Earth.txt`
- `books_05/7-There Were Giants Upon the Earth.txt`

### Group 42 — *Guide to Kabbalah*
- `books_04/Guide_To_Kabbalah.txt`
- `books_05/Guide_To_Kabbalah.txt`

### Group 43 — Pingree, *TAPS 2014 Ancient Science*
- `books_04/TAPS_Pingree_2014_Ancient_Science.txt`
- `books_05/TAPS_Pingree_2014_Ancient_Science.txt`

## Rights and provenance signals requiring review

The following were found through targeted inspection of title pages, front matter, copyright pages, or repository search. They are **triage leads**, not legal opinions. A rights determination must consider the exact edition, translation, commentary, publication country/date, applicable jurisdiction, and any license. The repository has no blanket license.

| File or group | Signal observed | Recommended disposition |
|---|---|---|
| `books_01/Bhagavad_Gita.txt`, byte-identical to `books_02/Bhagavad_Gita.txt` | Eknath Easwaran translation; chapter introductions by Diane Morrison; ©1985/2007 Blue Mountain Center of Meditation; “All rights reserved.” | Mark redistribution rights unresolved/restricted; do not assume the ancient underlying work's public-domain status makes this translation free to redistribute. |
| `books_03/Upanishads.txt` | Eknath Easwaran translation; chapter introductions/afterword by Michael N. Nagler; ©1987/2007 Blue Mountain Center of Meditation; “All rights reserved.” | Rights review before further formatting or redistribution. |
| `books_02/Journeys_Mythical_Past.txt`, byte-identical to `books_03/Journeys_Mythical_Past.txt` | ©2007 Zecharia Sitchin; “All rights reserved.” | Restrict reuse pending permission or a documented license. |
| `books_04/Gospel_of_Mary_Magdalene.txt` | The 2002 English translation, commentary, and notes identify Inner Traditions International copyright. | Do not reproduce or create a derivative of the modern translation/commentary without permission; consider an independently sourced public-domain or licensed edition. |
| `books_03/Ringmakers of Saturn by Norman R. Bergrun.txt` | ©1986 Norman R. Bergrun; “All rights reserved”; the book also says excerpts may be made in furtherance of knowledge and understanding. | Clarify the scope of that statement; do not treat it as blanket permission to reproduce the book. |
| `books_05/Vimanika_Shastra.txt`, related to `books_02/the_vimanika_shastra.txt` | The included attribution notice says the e-text is “NOT in the public domain in any country” and specifies archival/research purposes and non-commercial use. | Treat as rights-restricted until the notice's source, authority, and permissions are checked. Do not commercially redistribute. |
| `books_05/Temple of the Ancients.txt`, byte-identical to `books_01/Temple of the Ancients.txt` | Copyright notices include ©2005 Temple of the Ancients and ©2004 Amber K. material. | Identify individual contributors and rights holders; review the compilation as multi-authored content. |
| `books_05/The_Sekhmet_Heka_Hypothesis.txt` | Modern 2026 paper with © Sefy Levy, DOI and ORCID in the front matter. | Confirm publication license / repository permission before redistribution. |
| `books_03/The_Old_Testament_Pseudepigrapha_vol.1_Charlesworth_1983.txt`, byte-identical to `books_05` copy | Modern scholarly volume published in 1983; translation and editorial apparatus require separate rights analysis. | Treat as rights review, not public-domain text. |
| Jay Winter *Complete Book of Enoch* group (3 exact copies) | Translation/source lineage and redistribution license not established by this metadata pass. | Identify edition, copyright holder and license; keep separate from the Charles/Dillmann-derived 1 Enoch files. |
| Three-part *Grand Bible*, 2021 | Large modern edition files present as parts 1–3. | Verify publisher, translation and license before formatting or publishing derivatives. |
| Google Books-ingest files in archival folders | Google digitization notices ask for personal/non-commercial use, no automated querying, and watermark attribution. | Treat these as provider-use terms to review, not proof of underlying book copyright. Avoid automated bulk querying of Google Books content. |

## OCR and text-quality leads

- The exact duplicate group `Ancient_Indian_Aviation_06928824.txt` / `06928824.txt` contains replacement-character and OCR-fragmentation signals. A sampled search excerpt includes a U+FFFD replacement marker and broken phrases such as “ll Inte i ence Re ort”. A human should compare this against the source PDF/page image before treating it as faithful text.
- The four exact duplicate files in the group are:
  - `books_02/Ancient_Indian_Aviation_06928824.txt`
  - `books_03/06928824.txt`
  - `books_04/06928824.txt`
  - `books_05/Ancient_Indian_Aviation_06928824.txt`
- The Al-Zahrawi group contains four identical files of only 483 bytes. This is an unusually short record for a full work and needs identification: it may be a stub, note, citation, or incomplete extraction.
- The three *Grand Bible* segments are each over 33 MB; they require streaming/chunked local analysis and should not be fetched wholesale through a connector as a first pass.
- This audit did not run a full byte-by-byte OCR character scan across all 165 files. The local script and tests must be run on a local checkout, then text-quality exceptions manually inspected.

## Suggested triage order

1. Run the local audit script and test suite from a complete clone; save the JSON report outside the repository.
2. Review the 24 zero-byte placeholders and decide which should remain as intentional stubs, receive source files, or be tracked as missing-source issues.
3. Manually inspect the 43 non-empty exact-duplicate groups and choose canonical paths without deleting archival copies until links/provenance are mapped.
4. Run normalized-text and near-duplicate comparisons; exact-byte groups do not reveal translated editions, OCR variants, or textually similar files with changed line endings.
5. Resolve rights leads first for modern translations, commentaries, recent scholarly books, and items explicitly claiming they are not public domain.
6. Inspect OCR flags against original scans, prioritizing replacement characters, 483-byte records, unusual file lengths, and page-number contamination.
7. Add a per-file provenance record (title, edition, author/translator, source URL, extraction method, rights/license basis, and confidence) before declaring any archival item verified.

## Status

- **Completed:** Remote tree inventory; directory totals; zero-byte list; exact-byte duplicate groups.
- **Partially completed:** Targeted rights/provenance and OCR signal checks.
- **Not completed:** Whole-corpus local toolkit run; full OCR scan; normalized and near-duplicate scan; manual disposition of duplicate candidates; item-by-item rights decisions; facsimile inspection of suspect OCR.
- **Preservation:** No archival file was modified, removed, or automatically deduplicated.
