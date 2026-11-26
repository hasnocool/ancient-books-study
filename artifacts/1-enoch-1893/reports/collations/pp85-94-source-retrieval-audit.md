# Cornell printed pp.85–94 — source retrieval audit

**Date:** 2026-11-25  
**Scan:** Cornell / Internet Archive `cu31924014590545`  
**Target mapping:** printed pp.85–94 = BookReader leaves n106–n115 = one-based PDF pages 107–116.

## Finding

The earlier statement that no usable target image files existed was incorrect for the current repository state. The committed high-resolution BookReader JPEGs are present in:

`artifacts/page-images/cornell-native/cornell_printed_pp75_308/`

It contains nine page-specific OCR text files and nine `printed_pNNN_full.png` files for printed pp.85–90 and 92–94. No p.91-named image or OCR text file is present in that printed-page directory. However, the separate `cornell_all_pages/page_0113_full.png` file maps to PDF page 113 / printed p.91; it exists but its pixels are extremely dark and unreadable. The PNG files were fetched from GitHub and opened; they render as very dark, unreadable page images in the current image viewer, matching the previously documented native-PNG rendering problem. They are not usable proofing witnesses and are not counted as retrieved/inspected high-resolution page images.

The separate `cornell_pages_85_106` directory contains PDF ordinals 85–106, which correspond to printed pp.63–84, not the target printed pp.85–94. Its clear page_0085.png is printed p.63 and must not be mistaken for target p.85.

All ten BookReader JPEGs `p085_n106.jpg` through `p094_n115.jpg` are present under `artifacts/page-images/cornell-native/bookreader-large/`. Each file was fetched from the current GitHub branch and opened individually at 1360×2274. The images are legible and suitable for page-identity/layout inspection. The repository does, however, contain the original Cornell PDF at `pdfs/enoch-editions/enoch-1893-clarendon-original.pdf` (16,777,301 bytes; Git blob `38be2b5e0e95779f92dcb19a745fc654b010b711`). A reproducible renderer has been added at `scripts/render_cornell_1893_pages.py`; it exports PDF pages 107–116 as raw grayscale PNGs plus separate contrast-normalized viewing derivatives. The renderer has not yet been executed in this environment. It is not needed to inspect this batch because the committed BookReader JPEGs are already legible.

## Per-page asset status

| Printed page | PDF page | BookReader leaf | Native PNG | OCR TXT |
|---:|---:|---:|---|---|
| 85 | 107 | n106 | Present, unreadable in viewer | Present |
| 86 | 108 | n107 | Present, unreadable in viewer | Present |
| 87 | 109 | n108 | Present, unreadable in viewer | Present |
| 88 | 110 | n109 | Present, unreadable in viewer | Present |
| 89 | 111 | n110 | Present, unreadable in viewer | Present |
| 90 | 112 | n111 | Present, unreadable in viewer | Present |
| 91 | 113 | n112 | Present in `cornell_all_pages/page_0113_full.png`, unreadable | Cornell OCR missing; parallel scan text recovered |
| 92 | 114 | n113 | Present, unreadable in viewer | Present |
| 93 | 115 | n114 | Present, unreadable in viewer | Present |
| 94 | 116 | n115 | Present, unreadable in viewer | Present |

The exact paths, Git blob SHAs, and repository byte sizes are recorded in `artifacts/1-enoch-1893/manifests/cornell-printed-pages-85-94-source-audit.json`. Cornell p.91's OCR gap has since been filled provisionally from a separate searchable Knox College/Toronto copy of the 1893 edition (printed 1897); this is a parallel witness, not Cornell OCR. The OCR-only comparison is recorded in `artifacts/1-enoch-1893/reports/collations/pp85-94-ocr-only-discrepancy-ledger.md`.

## Status and next operation

- Cornell OCR/text assets: 9/10 present; p.91 missing in the Cornell text-layer batch.
- Parallel p.91 text: recovered from a separate Knox College/Toronto copy of the 1893 edition (printed 1897); not a substitute for Cornell's own text layer.
- Native PNG blobs: 10/10 located across the two Cornell-native directories, but all ten are visually unusable in this environment.
- Valid high-resolution BookReader JPEGs: 10/10 present and individually opened; native PNG exports remain unreadable.
- BookReader JPEG batch: 10/10 present and individually inspected for page identity/layout.
- Page/layout visual inspection: 10/10. Full line-by-line diplomatic collation: 0/10.
- Transcription: unchanged.
- Independent human approval: outstanding.

**Completed operation (2026-11-26):** all ten committed BookReader JPEGs were opened and checked individually for folio, running head, chapter/verse coverage, broad layout, and apparatus placement. The page/layout ledger is now 40/254. **Next required operation:** perform the full line-by-line diplomatic collation for pp.85–94, resolving the p.92 “serpents and the Cherubin” reading and the flagged transliterations against the images; then continue with pp.95–104. The renderer remains useful for reproducible raw exports but is not a prerequisite for this already-legible JPEG batch. Do not treat the OCR-only pages or the parallel p.91 text as image proofing or increment the visual-inspection ledger.


**Correction dated 2026-11-26:** This report's earlier finding that the target BookReader JPEGs were absent is superseded. All ten are committed and visually opened as documented above. The dark native PNG finding remains valid only for those PNG exports.
