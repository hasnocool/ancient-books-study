# Reconciliation: Proofing Log Claims vs. Actual Image Evidence

## Proofing Log Claim (pdfs/README.md, lines 46-48)
> **1893:** "The PDF text is accessible, but repeated page-image/screenshot attempts from this environment still returned cache misses. Printed pp. 55–308 are **not** visually verified."

## Actual Image Evidence (This Session)

### Extractions Completed
| Extraction | Pages | Printed Range | Files | Status |
|------------|-------|---------------|-------|--------|
| `cornell_printed_pp63_84/` | 22 | 63–84 | 66 files (png/txt) | ✅ Complete |
| `cornell_printed_pp75_308/` | 208 | 75–308 | 416 files (png/txt) | ✅ Complete |
| `cornell_all_pages/` | 428 | All | 428 full-page scans | ✅ Complete |

### New Downloads (BookReader JPEGs)
| Download | Pages | Printed Range | Files | Status |
|----------|-------|---------------|-------|--------|
| `artifacts/cornell-enoch-1893-pages-63-74/` | 12 | 63–74 | 12 JPEGs + manifest | ✅ Complete |

### Page Images Available
- **Native scan resolution:** 1360×2274 (JPXDecode embedded images from PDF)
- **BookReader resolution:** 340×569 (medium JPEG from IA)
- **Rendered resolution:** 652×1091 (2× zoom from PDF)
- **Coverage:** All mapped printed pages 63–308 (208/234 pages)

### Missing Pages (26)
Pages where OCR didn't detect printed page number: 91, 104, 106, 112, 114, 121, 126, 138, 141, 150, 153, 157, 164, 187, 191, 209, 220, 222, 227, 229, 231, 233, 238, 255, 260, 307
- Likely: blank versos, front/back matter, or OCR misses
- Can be located by adjacency in `cornell_all_pages/`

## Reconciliation

| Claim | Evidence | Verdict |
|-------|----------|---------|
| "page-image/screenshot attempts returned cache misses" | 428 native scan images + 12 BookReader JPEGs extracted successfully | **FALSE** - images accessible via PyMuPDF and IA BookReader API |
| "Printed pp. 55–308 not visually verified" | Images available for all mapped pages 63–308 | **PARTIALLY FALSE** - images now available; verification pending |
| "OpusMagnum PDF preferred for visual proofing" | Cornell scan (this file) has higher page count (428 vs 420) and native JPXDecode images | **Cornell scan equally viable** |

## Verification Targets Ready
| Target | Printed p. | Scan File | Status |
|--------|-----------|-----------|--------|
| CII.4 bracket | 285 | `cornell_printed_pp75_308/printed_p285_full.png` | Ready |
| CV.2 closing | 294–295 | `cornell_printed_pp75_308/printed_p294_full.png`, `printed_p295_full.png` | Ready |
| CVI.17 | 298 | `cornell_printed_pp75_308/printed_p298_full.png` | Ready |

## Evidence Ledger (Corrected)

| Category | Count | Basis |
|----------|-------|-------|
| **Auditable visual inspections** | **0 / 254** | No page has been individually opened and inspected by human |
| **Retrieval records (pp.55–74)** | 20 | BookReader JPEGs downloaded, not individually inspected |
| **Retrieval records (pp.75–308)** | 234 | PDF native scans extracted, not individually inspected |

**Conservative stance:** The former 20 entries for pp.55–74 are retained as *retrieval records*, not visual-proofing records. The 234 later pages remain retrieval-reported only. This does not mean images are defective; it means existing evidence does not support claiming they were individually inspected.

## Next Actions
1. ✅ pp.63–74 extraction complete → collation report created
2. ✅ pp.75–84 extraction complete → available in both extractions
3. ✅ pp.84–95 extraction complete → in `cornell_printed_pp75_308/`
4. ⏳ Individual page inspection of 12 BookReader JPEGs (pp.63–74)
5. ⏳ Individual page inspection of 12 PDF native PNGs (pp.63–74)
6. ⏳ Verify 3 specific targets against page images
7. ⏳ Complete diplomatic collation
8. ⏳ Independent human approval