# Text-Layer Collation Report: Printed pp. 75–84

**Source:** Cornell / Internet Archive scan `enoch-1893-clarendon-original.pdf` (identifier: `cu31924014590545`)
**BookReader leaves:** n96–n105
**Downloaded:** 10/10 high-resolution JPEG images (1360×2274)
**OCR text:** Extracted from embedded PDF text layer
**Consolidated OCR:** `artifacts/1-enoch-1893/ocr/cornell-printed-pages-75-84.txt`

## Page Mapping & File Inventory

| Printed p. | BookReader leaf | PDF p. | BookReader JPEG (1360×2274) | PDF native PNG (1360×2274) | OCR text |
|------------|-----------------|--------|-----------------------------|----------------------------|----------|
| 75 | n96 | 97 | p075_n096.jpg | printed_p075_full.png | printed_p075.txt |
| 76 | n97 | 98 | p076_n097.jpg | printed_p076_full.png | printed_p076.txt |
| 77 | n98 | 99 | p077_n098.jpg | printed_p077_full.png | printed_p077.txt |
| 78 | n99 | 100 | p078_n099.jpg | printed_p078_full.png | printed_p078.txt |
| 79 | n100 | 101 | p079_n100.jpg | printed_p079_full.png | printed_p079.txt |
| 80 | n101 | 102 | p080_n101.jpg | printed_p080_full.png | printed_p080.txt |
| 81 | n102 | 103 | p081_n102.jpg | printed_p081_full.png | printed_p081.txt |
| 82 | n103 | 104 | p082_n103.jpg | printed_p082_full.png | printed_p082.txt |
| 83 | n104 | 105 | p083_n104.jpg | printed_p083_full.png | printed_p083.txt |
| 84 | n105 | 106 | p084_n105.jpg | printed_p084_full.png | printed_p084.txt |

## OCR Text Statistics

| Page | Char Count | Lines | Content Summary |
|------|------------|-------|-----------------|
| 75 | 793 | 20 | General Introduction (p.53) — Satan discussion |
| 76 | 0 | 0 | Blank page — no text layer, images only |
| 77 | 1713 | 78 | Section I Introduction — Critical Structure, Date |
| 78 | 2599 | 117 | Section I continued — Relations to other sections |
| 79 | 2311 | 107 | Chapter I.1-2 — Translation begins |
| 80 | 2888 | 130 | Chapter I.3-5 — Critical notes on Holy One, Watchers |
| 81 | 2574 | 117 | Chapter I.6-9, II.1-3 — Judgment, nature order |
| 82 | 2367 | 107 | Chapter III-IV — Trees, seasons, summer heat |
| 83 | 2610 | 117 | Chapter V-VI — Execration, blessings, angels |
| 84 | 2787 | 123 | Chapter VI.1-4 — Sons of heaven, daughters of men |

## OCR Defects Noted

1. **Page 76**: Blank page — no OCR text layer, contains 2 embedded JPXDecode images only
2. **Page 75**: Printed page number "53" detected (Introduction section, not main translation)
3. **Page 77**: Section header "THE BOOK OF ENOCH — SECTION I" — start of main translation
4. **Page 79**: Printed page number "57" detected — Chapter I begins
5. **Page 80**: Printed page number "53" detected (likely OCR error — should be 58)
6. **Greek fragments**: Systematically garbled (e.g., `é£eddeiv dad mpoodmov rev ent`)
7. **Ligatures broken**: fi, fl, ff → separate characters
8. **Hyphenation artifacts**: Line-end hyphens remain in text layer

## Image Evidence Status

| Page | BookReader JPEG | PDF Native Scan | Visual Inspection |
|------|-----------------|-----------------|-------------------|
| 75–84 | ✅ Downloaded (1360×2274) | ✅ Extracted (1360×2274) | ⏳ Pending |

## Verification Protocol

For each page, human inspection must confirm:

- [ ] Page image opens without corruption
- [ ] Printed page number visible in scan
- [ ] Text content matches OCR layer (spot-check)
- [ ] Critical apparatus legible
- [ ] No missing lines or columns
- [ ] Greek fragments readable (where present)

## Evidence Distinction

| Evidence Type | Source | Use For |
|---------------|--------|---------|
| **Visual proofing** | Page images (BookReader JPEG or PDF native PNG) | Confirming text, layout, pagination |
| **OCR collation** | Embedded PDF text layer | Search, comparison, defect detection |
| **Retrieval record** | Manifest + SHA256 | Provenance, completeness |

**Do not conflate:** Successful download ≠ visual verification. Each page must be individually opened and inspected to count toward the proofing ledger.

## Next Steps

1. **Visual inspection**: Open all 10 BookReader JPEGs and 10 PDF native PNGs
2. **Spot-check OCR**: Compare 3–5 lines per page against image
3. **Record defects**: Log any discrepancies in a page-level defect log
4. **Update ledger**: Only after individual inspection, increment visual proofing count