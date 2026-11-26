# Cornell printed pp.85–94 — OCR-only discrepancy ledger

**Date:** 2026-11-25  
**Primary scan:** Cornell / Internet Archive `cu31924014590545`  
**Target:** printed pp.85–94; BookReader leaves n106–n115; one-based PDF pages 107–116.  
**Comparison base:** `formatted_editions/books/book-of-enoch-charles-1893/book-01-watchers-chapters-01-36.md`, Chapters XV–XXII.

## Evidence boundary

This began as an OCR/text-layer comparison. On 2026-11-26, all ten corresponding Cornell BookReader JPEGs were also opened individually at 1360×2274 for page-identity/layout inspection. This does **not** constitute full diplomatic collation. Cornell OCR is present for pp.85–90 and 92–94. Cornell p.91 OCR is absent. Its text was independently recovered from the searchable text extraction of a separate 1893 Charles scan (Knox College/Toronto copy, hosted by Luminist/Wasabi). That parallel scan is not the Cornell witness and must not be represented as Cornell OCR. The Cornell page_0113_full.png exists in `cornell_all_pages/`, but its pixels are extremely dark and unreadable.

The formatted repository text explicitly disclaims verbatim identity with the 1893 Charles/Dillmann printing. Therefore wording differences below are **source-comparison flags**, not automatic corrections to the repository transcription. No transcription wording was changed.

## Per-page evidence

| Printed page | Cornell OCR | Supplement | Main content / coverage | Image status |
|---:|---|---|---|---|
| 85 | Present | — | End of XV.12; XVI.1; Greek parallel and critical apparatus | BookReader JPEG individually opened; native PNG unreadable |
| 86 | Present | — | Greek-only fragment noted as absent from Ethiopic version; XVI.2 and apparatus | BookReader JPEG individually opened; native PNG unreadable |
| 87 | Present | — | XVII.1–4; critical and exegetical notes | BookReader JPEG individually opened; native PNG unreadable |
| 88 | Present | — | XVII.4–XVIII.3; notes and Greek apparatus | BookReader JPEG individually opened; native PNG unreadable |
| 89 | Present | — | XVIII.4–12; notes and Greek apparatus | BookReader JPEG individually opened; native PNG unreadable |
| 90 | Present | — | XVIII.12–XIX.1; notes and commentary | BookReader JPEG individually opened; native PNG unreadable |
| 91 | Missing | Parallel scan OCR recovered | Remainder of XIX.1–3; XX.1–4; critical notes | BookReader JPEG individually opened; native PNG unreadable |
| 92 | Present | — | XX.5–7; XXI.1–5; notes | BookReader JPEG individually opened; native PNG unreadable |
| 93 | Present | — | XXI.5–10; XXII.1; notes | BookReader JPEG individually opened; native PNG unreadable |
| 94 | Present | — | XXII.1–5; notes | BookReader JPEG individually opened; native PNG unreadable |

## Discrepancy ledger

| ID | Page | Classification | Observation | Treatment |
|---|---:|---|---|---|
| OCR-085-01 | 85 | OCR defect | Heading OCR renders XVI as `XVTJ`; Greek lines and Ethiopic manuscript sigla are heavily corrupted. | Do not treat as a textual variant. Re-read from a legible image. |
| OCR-085-02 | 85 | OCR/layout defect | Words are joined or split across line endings (for example `goneforth` and `inordertode-`). | Normalize only in a derived OCR transcript; preserve diplomatic line evidence separately. |
| OCR-086-01 | 86 | OCR defect | Greek text and apparatus contain extensive character substitutions and broken line order. | No Greek/apparatus readings accepted from this OCR without image verification. |
| SCOPE-086-01 | 86 | Scope distinction | The page begins with a Greek fragment explicitly described as absent from the Ethiopic version. It is not present in the formatted narrative chapter text. | Not a missing narrative passage; record as Greek-fragment/apparatus material outside the reading-text file's scope. |
| OCR-087-01 | 87 | OCR defect | Greek apparatus and manuscript sigla are corrupted; several Greek words are rendered as Latin-like noise. | No apparatus emendation from OCR alone. |
| OCR-088-01 | 88 | OCR defect | Greek apparatus includes garbled forms such as `Tlupipreyébwy`; punctuation and sigla are unstable. | No apparatus emendation from OCR alone. |
| OCR-089-01 | 89 | OCR defect | `pulars` appears where the English context requires “pillars”; headings and Greek apparatus are also noisy. | Classify “pulars” as OCR corruption, not a source reading. |
| OCR-090-01 | 90 | OCR defect | The folio/header begins with stray `S,`; chapter heading is misrecognized as `XIX. x.`; Greek apparatus is corrupted. | Treat as OCR noise. |
| SRC-092-01 | 92 | Potential source/transcription difference | Cornell OCR reads “Paradise and the serpents and the Cherubin”; the formatted text reads “Paradise, the seraphim and the cherubim.” The searchable parallel scan also extracts “the serpents and the Cherubin.” | Material wording difference, not safely attributable to OCR. Flag for facsimile verification and source-lineage review; do not silently change the repository text. |
| SRC-092-02 | 92 | Transliteration/orthography | Cornell OCR gives “Saraqél”; formatted text has “Saraqael.” | Could reflect OCR diacritic handling or editorial transliteration. Retain as an unresolved spelling/transliteration flag pending image inspection. |
| SRC-093-01 | 93 | Potential source/transcription difference | Printed/OCR wording of XXI.5 has “Wherefore dost thou ask, and why dost thou enquire and art curious?”; the formatted text modernizes/recasts the question (“Wherefore do you ask, and why do you enquire, and are curious?”). | Likely modernization/recensional wording rather than a simple OCR defect. Keep in source-comparison notes; do not force a diplomatic match. |
| SRC-094-01 | 94 | Witness/OCR spelling difference | Cornell OCR reads “Rufael”; the separate Knox scan extraction reads “Rafael”; the formatted text has “Rufael.” | The Cornell OCR and formatted form agree, but the alternative scan differs. Not resolvable without readable Cornell pixels. |

## Page 91 recovery — parallel scan only

The searchable extraction of the separate Knox College/Toronto 1893 scan supplies the text for printed p.91. It confirms that the page contains the close of Chapter XIX (including the material on angels who lead humanity into sacrificing to demons), followed by XX.1–4 and the first four angel names: Uriel, Rufael, Raguel, and Michael. The Cornell page_0113_full.png remains unreadable, so this recovery fills the **text-layer gap only**; it does not establish Cornell's exact punctuation, spelling, lineation, or apparatus.

## Reconciliation of proofing and approval records

The repository's `IMAGE_PROOFING_LOG.md` opening summary claims 246/254 pages individually checked and says independent human approval was signed off on 2026-11-25. That conflicts with its own detailed pp.75–84 section (22/254 individually opened; independent approval pending), the pp.75–84 collation report, `SOURCE_COLLATION_LOG.md`, `SOURCE_NOTES.md`, `REVIEW_LOG.md`, and `docs/REPOSITORY_AUDIT_REPORT.md`, all of which describe independent approval as pending and/or pp.75–308 as not individually inspected.

No named second reviewer or signed review artifact substantiating the 246/254 and completed-approval claims was located in the repository search. The conservative, internally corroborated status is therefore:
- Individually opened page images: **40/254** (pp.55–94; pp.63–74 at 340×569, other checked batches at 1360×2274).
- Full line-by-line diplomatic page proofing: **0/254 complete**.
- Printed pp.85–94 page/layout visual inspection: **10/10**; full line-by-line diplomatic proofing: **0/10**.
- OCR/text comparison for pp.85–94: **9/10 Cornell pages**, plus p.91 recovered from a separate scan.
- Independent human approval: **pending**.

The unsupported 246/254 and signed-off claims should not be used as completion evidence. This ledger does not itself certify any page as visually checked.

## Next required work

1. Complete a line-by-line comparison of pp.85–94 against the derivative transcription, including English wording, Greek, Ethiopic sigla, punctuation, brackets, and apparatus.
2. Resolve the p.92 reading “the serpents and the Cherubin” against the derivative's “seraphim and the cherubim”; do not silently normalize the witness.
3. Preserve p.91's parallel-scan OCR provenance: Cornell page pixels are now visible, but Cornell's own OCR file remains missing.
4. Continue with pp.95–104 using the committed high-resolution BookReader JPEGs and record each page individually.
5. Keep independent human approval pending until a named second reviewer signs a page/chapter-specific record.

**Transcription changes:** none.  
**Visual proofing count increment:** none.  
**Independent approval:** not granted by this report.


**Visual inspection update — 2026-11-26:** The ten high-resolution JPEGs p085_n106.jpg–p094_n115.jpg were fetched from the repository and individually opened. The p.92 wording “the serpents and the Cherubin” is plainly visible in the Cornell image and is therefore a source/transcription discrepancy, not merely an OCR artefact. This visual check is page/layout-level only; full diplomatic proofing remains 0/10.
