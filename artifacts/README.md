# Research artifacts

Generated, intermediate, and audit-supporting files belong here. Canonical editions, source PDFs, and live project control logs remain in their domain directories.

## 1 Enoch — R. H. Charles, 1893

- `page-images/bookreader-medium/`: medium-resolution BookReader JPEGs. These support folio and broad-layout checks, not detailed apparatus transcription.
- `manifests/`: retrieval metadata and integrity hashes for image batches.
- `ocr/`: source text-layer/OCR extracts. Filenames identify the original PDF ordinal range; consult batch notes before treating ordinals as printed folios.
- `reports/collations/`: OCR/text-layer inventories and chapter/page-specific audit reports. These are research reports, not necessarily completed diplomatic collations.
- `reports/historical/`: superseded or historical reconciliation reports. Read their scope and date before relying on their claims.

### Current batch: printed pp.63–74

The 12 BookReader JPEGs are under `1-enoch-1893/page-images/bookreader-medium/`, with the manifest in `1-enoch-1893/manifests/bookreader-pages-63-74.json`. The page/layout review is recorded in the image-proofing log. The OCR inventory is in `1-enoch-1893/reports/collations/pp63-74-ocr-inventory.md`. These images are 340×569 and are not sufficient for detailed Greek or critical-apparatus proofing.

### OCR extraction: PDF ordinals 75–84

`1-enoch-1893/ocr/cornell-pdf-ordinals-75-84.txt` is the recovered text-layer extraction. Its PDF ordinals correspond to printed p.53 and pp.55–62 (PAGE 76 is blank); the filename does not mean printed pp.75–84.

## Placement rules

1. Keep final formatted/modernized text in `formatted_editions/` or `modernized_editions/`.
2. Keep authoritative, continuously maintained proofing and source-control logs beside the edition they govern.
3. Put downloaded page-image batches, OCR dumps, manifests, temporary extraction outputs, and one-off research/collation reports here.
4. Never treat an OCR inventory or retrieval manifest as visual proofing.
5. Preserve source identifiers, printed-page ranges, scan/leaf mappings, resolution, and evidence limitations in each batch report.


### High-resolution batch: printed pp.75–84

- JPEGs: `1-enoch-1893/page-images/bookreader-large/` (10 files, 1360×2274 per manifest; leaves n96–n105).
- Manifest: `1-enoch-1893/manifests/bookreader-pages-75-84-large.json`.
- Consolidated text layer: `1-enoch-1893/ocr/cornell-printed-pages-75-84.txt` (ten non-empty page sections).
- Inventory: `1-enoch-1893/reports/collations/pp75-84-retrieval-and-ocr-inventory.md`.

This batch is retrieval/OCR evidence only. The pages have not yet been individually opened and checked; do not increase the visual-proofing count until their pixels have been inspected.


### High-resolution inspection: printed pp.75–84

The ten BookReader JPEGs in `1-enoch-1893/page-images/bookreader-large/` (leaves n96–n105, 1360×2274) were individually opened. Folios and layouts are confirmed; targeted OCR defects are logged in `1-enoch-1893/reports/collations/pp75-84-retrieval-and-ocr-inventory.md` and the edition's image-proofing log. This is not a complete line-by-line diplomatic collation. The separate native PNGs under `page-images/cornell-native/cornell_printed_pp75_308/` rendered nearly black in the viewer and were not used for this inspection.
