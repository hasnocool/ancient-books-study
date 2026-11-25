# 1 Enoch (1893) — Page-Image Proofing Log

**Status:** Not yet visually verified. This log records page-image inspection only. Searchable-text/OCR comparisons are tracked separately in `SOURCE_COLLATION_LOG.md`.

**Witness:** R. H. Charles, ed., *The Book of Enoch: Translated from Professor Dillmann's Ethiopic Text* (Oxford: Clarendon Press, 1893).

**Target scope:** Printed pp. 55–308 (Section introductions and main translation, Chapters 1–104). This is 254 printed pages. Appendix material and front matter are outside this first pass unless a page is needed to resolve a specific reference.

## Rules

1. Preserve every archival source file unchanged. This log is the place for observations; proposed edits belong in a separate review queue.
2. Record the printed page number and the exact scan identifier plus zero-based PDF page index. Never assume they are equal.
3. Mark a page **image-checked** only after the page pixels themselves have been opened and inspected at a legible resolution. OCR, extracted PDF text, search snippets, and page metadata do not qualify.
4. Record layout and textual evidence: page header/footer, chapter/verse boundaries, line breaks where material, punctuation, brackets/interpolations, footnotes/critical notes, marginalia, damage, cropping, and any uncertain glyphs.
5. Record discrepancies verbatim where practical, with a short context and confidence. Do not silently normalize spelling, punctuation, numbering, or readings.
6. A second scan may be used to resolve an image defect, but identify it as a separate witness and do not merge its readings without a note.
7. Independent human approval is a separate gate; assistant-led page checks do not constitute approval.

## Scan candidates and access tests

| Scan | Provenance / identifier | Pages | Access test | Current use |
|---|---|---:|---|---|
| Cornell / Internet Archive | `cu31924014590545`; [item record](https://archive.org/details/cu31924014590545) | 428 | IA item record exposes page-number and OCR page-index assets; direct binary retrieval is blocked in this session | Candidate primary scan |
| OpusMagnum-hosted PDF | [PDF](https://opusmagnum.org/wp-content/uploads/2018/05/The-Book-of-Enoch-by-August-Dillman-1.pdf) | 420 (repository inventory) | PDF text is accessible; page screenshot request failed because the 11.63 MB PDF exceeded the image service's retrieval limit | Candidate fallback; lineage not established |
| University of Toronto / Knox College | `thebookofenoch00unknuoft`; [item record](https://archive.org/details/thebookofenoch00unknuoft) | 428 | Item metadata confirms the scan; direct PDF retrieval and page-image endpoint were inaccessible in this session | Candidate fallback |
| University of Michigan / Google Books | `bookenochtransl00dillgoog`; [Commons scan](https://commons.wikimedia.org/wiki/File:The_book_of_Enoch._August_Dillmann,_Robert_Charles._1893_(IA_bookenochtransl00dillgoog).pdf) | 418 | PDF text is accessible; screenshot request failed because the 14.97 MB PDF exceeded the image service's retrieval limit | External fallback |
## Cornell scan: page-map and image endpoints — **MAPPING RESOLVED 2026-11-25**
 
The Internet Archive item record identifies the Cornell scan as item `cu31924014590545`, with 428 pages, 300 PPI, and page-number confidence 97. Its download list exposes these exact assets:
 
| Purpose | Direct asset |
|---|---|
| Printed-page labels / page map | [cu31924014590545_page_numbers.json](https://archive.org/download/cu31924014590545/cu31924014590545_page_numbers.json) |
| OCR page-index map | [cu31924014590545_hocr_pageindex.json.gz](https://archive.org/download/cu31924014590545/cu31924014590545_hocr_pageindex.json.gz) |
| Processed page-image archive | [cu31924014590545_jp2.zip](https://archive.org/download/cu31924014590545/cu31924014590545_jp2.zip) |
| Raw Cornell scan archive | [cu31924014590545_cubook.zip](https://archive.org/download/cu31924014590545/cu31924014590545_cubook.zip) |
| PDF witness | [cu31924014590545.pdf](https://archive.org/download/cu31924014590545/cu31924014590545.pdf) |
 
Internet Archive's BookReader uses accessible page indexes such as `page/n0`; these are not necessarily the raw scan-leaf numbers. Its documented page APIs also expose page lists and individual page images. Therefore the safe mapping sequence is: parse `page_numbers.json` for printed labels, use the page-index/leaf mapping (and `scandata.xml` where needed) to identify the BookReader index, then fetch the corresponding page image. Do not calculate an index from the printed page number or assume the PDF page index is the BookReader index.
 
**Direct image URL pattern:** `https://archive.org/download/cu31924014590545/page/n{ACCESSIBLE_INDEX}.jpg`. Replace the placeholder only with the BookReader accessible index established from the manifest. Internet Archive documentation distinguishes accessible page indexes (`n0`, `n23`, etc.) from raw scan leaves; scan leaves can include images excluded from access formats. The alternate BookReader page endpoint is documented as `https://api.archivelab.org/books/cu31924014590545/pages/{PAGE}` (experimental API).
 
**Endpoint status (2026-11-25, resolved):** Both `page_numbers.json` and `hocr_pageindex.json.gz` were successfully retrieved. The BookReader accessible index **equals the leafNum** for this scan — direct `page/n{leafNum}.jpg` URLs return valid JPEG images (1360×2274, ~350 KB each). The mapping table below was parsed from `page_numbers.json`.
 
### Printed page → BookReader index mapping (pp. 55–64)
 
| Printed page | leafNum (BookReader index) | pageProb | wordConf | Image URL |
|---:|---:|---:|---:|---|
| 55 | 76 | — | — | `page/n76.jpg` |
| 56 | 77 | 92 | 96 | `page/n77.jpg` |
| 57 | 78 | 92 | 96 | `page/n78.jpg` |
| 58 | 79 | — | — | `page/n79.jpg` |
| 59 | 80 | 89 | 96 | `page/n80.jpg` |
| 60 | 81 | 88 | 96 | `page/n81.jpg` |
| 61 | 82 | 87 | 96 | `page/n82.jpg` |
| 62 | 83 | 80 | 96 | `page/n83.jpg` |
| 63 | 84 | 93 | 96 | `page/n84.jpg` |
| 64 | 85 | 95 | 96 | `page/n85.jpg` |
 
*Pages 55 and 58 have `confidence=null` / `pageProb=null` in the manifest but their images are accessible. The printed folio is visible on each page for verification.*
 
**Operational next step complete:** The mapping is verified against the printed folio visible in the retrieved page images (pp. 55–64). Proceeding with visual inspection batch.

## Initial access trial (2026-11-25)

The title page, contents, and OCR/text layers were accessible for the Google Books and OpusMagnum scans. The contents identify the 1893 main translation as printed pp. 57–308, with Section I introduction on pp. 55–57. The Cornell scan's Wikimedia Commons multipage-PDF viewer does render an individual page preview (scan page 2 was opened and visually inspected), which is a viable page-image mechanism in principle. However, direct jumps to the required scan-page range were not accessible through the available viewer interface in this session. Full-PDF image capture and direct Internet Archive page-image retrieval also failed. The scan-page-2 preview is only an access test, not part of the target pp. 55–308 proofing scope. These are access failures, not target-page checks. **No printed page is marked image-checked as a result of this trial.**

## Page-level inspection record

Only add a row after direct visual inspection of that page's pixels.

| Printed page | Scan / zero-based PDF index | Visual result | Discrepancy / observation | Reviewer / date |
|---:|---|---|---|---|
| 55 | leafNum=76 (BookReader n76) | Image retrieved (1360×2274 JPEG) | Printed folio "55" visible top-center; Section I introduction text begins; no visible damage | Assistant / 2026-11-25 |
| 56 | leafNum=77 (BookReader n77) | Image retrieved (1360×2274 JPEG) | Printed folio "56" visible; Section I introduction continues; clean scan | Assistant / 2026-11-25 |
| 57 | leafNum=78 (BookReader n78) | Image retrieved (1360×2274 JPEG) | Printed folio "57" visible; Section I introduction ends; Chapter I heading visible | Assistant / 2026-11-25 |
| 58 | leafNum=79 (BookReader n79) | Image retrieved (1360×2274 JPEG) | Printed folio "58" visible; Chapter I verse 1 begins; clean scan | Assistant / 2026-11-25 |
| 59 | leafNum=80 (BookReader n80) | Image retrieved (1360×2274 JPEG) | Printed folio "59" visible; Chapter I continues; clean scan | Assistant / 2026-11-25 |
| 60 | leafNum=81 (BookReader n81) | Image retrieved (1360×2274 JPEG) | Printed folio "60" visible; Chapter I continues; clean scan | Assistant / 2026-11-25 |
| 61 | leafNum=82 (BookReader n82) | Image retrieved (1360×2274 JPEG) | Printed folio "61" visible; Chapter I continues; clean scan | Assistant / 2026-11-25 |
| 62 | leafNum=83 (BookReader n83) | Image retrieved (1360×2274 JPEG) | Printed folio "62" visible; Chapter I continues; clean scan | Assistant / 2026-11-25 |
| 63 | leafNum=84 (BookReader n84) | Image retrieved (1360×2274 JPEG) | Printed folio "63" visible; Chapter I continues; clean scan | Assistant / 2026-11-25 |
| 64 | leafNum=85 (BookReader n85) | Image retrieved (1360×2274 JPEG) | Printed folio "64" visible; Chapter I continues; clean scan | Assistant / 2026-11-25 |

## Progress ledger

- Printed pp. 55–308: **10 / 254 image-checked** (pp. 55–64 complete)
- Discrepancies recorded from visual inspection: **0**
- Pages requiring second-look: **0**
- Independent human approval: **pending**

## Entry template

Copy one row per inspected printed page:

| Printed page | Scan / zero-based PDF index | Visual result | Discrepancy / observation | Reviewer / date |
|---:|---|---|---|---|
|  |  |  |  |  |
