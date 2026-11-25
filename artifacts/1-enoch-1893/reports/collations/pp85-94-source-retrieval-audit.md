# Cornell printed pp.85–94 — source retrieval audit

**Date:** 2026-11-25  
**Scan:** Cornell / Internet Archive `cu31924014590545`  
**Target mapping:** printed pp.85–94 = BookReader leaves n106–n115 = one-based PDF pages 107–116.

## Finding

The earlier statement that no corresponding source assets existed was too broad. A recursive repository check found an existing native-scan directory:

`artifacts/page-images/cornell-native/cornell_printed_pp75_308/`

It contains nine page-specific OCR text files and nine `printed_pNNN_full.png` files for printed pp.85–90 and 92–94. No p.91-named image or OCR text file is present in that printed-page directory. However, the separate `cornell_all_pages/page_0113_full.png` file maps to PDF page 113 / printed p.91; it exists but its pixels are extremely dark and unreadable. The PNG files were fetched from GitHub and opened; they render as very dark, unreadable page images in the current image viewer, matching the previously documented native-PNG rendering problem. They are not usable proofing witnesses and are not counted as retrieved/inspected high-resolution page images.

The separate `cornell_pages_85_106` directory contains PDF ordinals 85–106, which correspond to printed pp.63–84, not the target printed pp.85–94. Its clear page_0085.png is printed p.63 and must not be mistaken for target p.85.

No BookReader JPEGs `p085_n106.jpg` through `p094_n115.jpg` are present under the expected `bookreader-large` directory. Attempts to retrieve them directly from Internet Archive still did not return usable image bytes.

## Per-page asset status

| Printed page | PDF page | BookReader leaf | Native PNG | OCR TXT |
|---:|---:|---:|---|---|
| 85 | 107 | n106 | Present, unreadable in viewer | Present |
| 86 | 108 | n107 | Present, unreadable in viewer | Present |
| 87 | 109 | n108 | Present, unreadable in viewer | Present |
| 88 | 110 | n109 | Present, unreadable in viewer | Present |
| 89 | 111 | n110 | Present, unreadable in viewer | Present |
| 90 | 112 | n111 | Present, unreadable in viewer | Present |
| 91 | 113 | n112 | Missing | Missing |
| 92 | 114 | n113 | Present, unreadable in viewer | Present |
| 93 | 115 | n114 | Present, unreadable in viewer | Present |
| 94 | 116 | n115 | Present, unreadable in viewer | Present |

The exact paths, Git blob SHAs, and repository byte sizes are recorded in `artifacts/1-enoch-1893/manifests/cornell-printed-pages-85-94-source-audit.json`. Cornell p.91's OCR gap has since been filled provisionally from a separate searchable 1893 Knox College/Toronto scan; this is a parallel witness, not Cornell OCR. The OCR-only comparison is recorded in `artifacts/1-enoch-1893/reports/collations/pp85-94-ocr-only-discrepancy-ledger.md`.

## Status and next operation

- Cornell OCR/text assets: 9/10 present; p.91 missing in the Cornell text-layer batch.
- Parallel p.91 text: recovered from a separate 1893 Knox College/Toronto scan; not a substitute for Cornell's own text layer.
- Native PNG blobs: 10/10 located across the two Cornell-native directories, but all ten are visually unusable in this environment.
- Valid high-resolution page images: 0/10 acquired in this operation.
- BookReader JPEG batch: 0/10 present.
- Visual inspection and diplomatic collation: 0/10.
- Transcription: unchanged.
- Independent human approval: outstanding.

**Next required operation:** repair/re-export the native PNGs from the source PDF or obtain the original BookReader JPEGs for leaves n106–n115. Reconcile the flagged OCR/source differences against legible Cornell pixels. Do not treat the OCR-only pages or the parallel p.91 text as image proofing or increment the visual-inspection ledger.
