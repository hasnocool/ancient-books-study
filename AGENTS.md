# Ancient Books Study — Project Paths & Artifacts Layout

## Root
`/home/hyperion/Projects/ancient-books-study/`

## Canonical Source PDFs (never modify)
`pdfs/enoch-editions/`
- `enoch-1893-clarendon-original.pdf` — Cornell / IA scan (identifier: `cu31924014590545`), 428 pages
- Other 1893/1912/1917 editions also present

## Research Artifacts
`artifacts/`

### 1 Enoch — R. H. Charles, 1893
`artifacts/1-enoch-1893/`

| Subdirectory | Contents |
|--------------|----------|
| `manifests/bookreader-pages-63-74.json` | Retrieval manifest for pp.63–74 |
| `manifests/bookreader-pages-75-84-large.json` | Retrieval manifest for pp.75–84 |
| `ocr/cornell-pdf-ordinals-75-84.txt` | OCR text layer — PDF ordinals 75–84 (printed p.53, pp.55–62; PAGE 76 blank). **Not** printed pp.75–84 |
| `ocr/cornell-printed-pages-75-84.txt` | Consolidated OCR text for printed pp.75–84 |
| `reports/collations/` | Collation reports, inventories, verification targets report |
| `reports/historical/` | Superseded reconciliation reports |

### Page Images — BookReader JPEGs (Internet Archive)
`artifacts/page-images/cornell-native/bookreader-medium/`
- 12 medium-res JPEGs (340×569), printed pp.63–74, leaves n84–n95

`artifacts/page-images/cornell-native/bookreader-large/`
- 10 high-res JPEGs (1360×2274), printed pp.75–84, leaves n96–n105

### Page Images — Cornell Native Scans (1360×2274 JPXDecode from PDF)
`artifacts/page-images/cornell-native/cornell_printed_pp63_84/`
- Printed pp.63–84 → PDF pages 85–106
- Files per page: `_full.png` + `.png` + `.txt`

`artifacts/page-images/cornell-native/cornell_printed_pp75_308/`
- Printed pp.75–308 → PDF pages 97–330
- Files per page: `_full.png` + `.png` + `.txt`

`artifacts/page-images/cornell-native/cornell_pages_75_84/`
- PDF ordinals 75–84 → PDF pages 75–84
- Files per page: `_full.png` + `.png` + `.txt`

`artifacts/page-images/cornell-native/cornell_pages_85_106/`
- PDF ordinals 85–106 → PDF pages 85–106
- Files per page: `_full.png` + `.png` + `.txt`

`artifacts/page-images/cornell-native/cornell_all_pages/`
- All 428 PDF pages → PDF pages 1–428
- Files per page: `_full.png` only

## Key Files

| File | Purpose |
|------|---------|
| `AGENTS.md` | This file — project paths and artifacts layout |
| `formatted_editions/books/book-of-enoch-charles-1893/IMAGE_PROOFING_LOG.md` | Authoritative proofing log: page map (pp.55–308 → leafNums 76–329), inspection rules, progress ledger |
| `artifacts/1-enoch-1893/reports/collations/VERIFICATION_TARGETS_REPORT.md` | 3 verification targets: CII.4 (p.291), CV.2 (p.301), CVI.17 (p.305) |
| `artifacts/1-enoch-1893/reports/collations/pp75-84-retrieval-and-ocr-inventory.md` | pp.75–84 retrieval + OCR inventory |
| `artifacts/1-enoch-1893/reports/collations/pp63-74-ocr-inventory.md` | pp.63–74 OCR inventory |
| `artifacts/1-enoch-1893/reports/collations/pp55-62-text-layer-collation.md` | pp.55–62 text-layer collation |

## Proofing Ledger Status (see IMAGE_PROOFING_LOG.md for full detail)

| Tier | Count | Basis |
|------|-------|-------|
| Page/layout-level visual inspection | 12 / 254 | pp.63–74 individually opened at 340×569 medium JPEG |
| Full high-resolution textual/apparatus proofing | 0 / 254 | No page completed at 1360×2274 resolution |
| Retrieval records (pp.55–74) | 20 | BookReader JPEGs downloaded; reclassified as retrieval-only |
| Retrieval records (pp.75–308) | 234 | Batch-retrieved; not individually image-checked |

**Rule:** Successful download ≠ visual verification. Each page must be individually opened and inspected at legible resolution before incrementing any proofing count. OCR, extracted PDF text, search snippets, and page metadata do not qualify.

## Downloader

`tools/download_archive_pages.py` — Internet Archive BookReader page image downloader

Example usage (requires network access):
```
python tools/download_archive_pages.py \
  --start-page 63 \
  --end-page 74 \
  --prefer-large \
  --force \
  --output-dir artifacts/page-images/cornell-native/bookreader-large \
  --manifest artifacts/1-enoch-1893/manifests/bookreader-pages-63-74-large.json
```

## Git

- Remote: `https://github.com/hasnocool/ancient-books-study.git`
- Branch: `main`
- Large image directories under `artifacts/` are tracked in git (JPEG + PNG files committed with SHA256 manifests)