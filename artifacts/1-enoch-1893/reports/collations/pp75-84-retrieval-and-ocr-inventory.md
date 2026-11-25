# Cornell 1893 — Printed pp.75–84 retrieval and OCR inventory

**Witness:** R. H. Charles, *The Book of Enoch* (Oxford: Clarendon Press, 1893), Cornell / Internet Archive scan `cu31924014590545`.
**Printed pages:** 75–84 inclusive.
**BookReader leaves:** n96–n105.
**PDF page indices:** 97–106 (one-based PDF page numbers).
**Image batch:** `artifacts/1-enoch-1893/page-images/bookreader-large/`.
**Manifest:** `artifacts/1-enoch-1893/manifests/bookreader-pages-75-84-large.json`.
**Consolidated text layer:** `artifacts/1-enoch-1893/ocr/cornell-printed-pages-75-84.txt`.

## Retrieval inventory

The committed manifest records 10/10 HTTP 200 image responses, all declared as JPEG, each 1360×2274. The manifest byte counts agree with the Git tree file sizes. SHA-256 values are retained in the manifest. This verifies the repository's recorded retrieval metadata and file-size consistency; it is not a fresh byte-for-byte re-download or image-pixel inspection in this audit.

| Printed page | BookReader leaf | PDF page (1-based) | Image | Bytes | Dimensions |
|---:|---:|---:|---|---:|---:|
| 75 | n96 | 97 | `p75_n96.jpg` | 462,465 | 1360×2274 |
| 76 | n97 | 98 | `p76_n97.jpg` | 505,060 | 1360×2274 |
| 77 | n98 | 99 | `p77_n98.jpg` | 495,841 | 1360×2274 |
| 78 | n99 | 100 | `p78_n99.jpg` | 502,698 | 1360×2274 |
| 79 | n100 | 101 | `p79_n100.jpg` | 489,423 | 1360×2274 |
| 80 | n101 | 102 | `p80_n101.jpg` | 487,782 | 1360×2274 |
| 81 | n102 | 103 | `p81_n102.jpg` | 494,471 | 1360×2274 |
| 82 | n103 | 104 | `p82_n103.jpg` | 490,429 | 1360×2274 |
| 83 | n104 | 105 | `p83_n104.jpg` | 518,900 | 1360×2274 |
| 84 | n105 | 106 | `p84_n105.jpg` | 485,239 | 1360×2274 |

## OCR/text-layer inventory

The consolidated extraction contains a page marker for every printed page 75–84. All ten sections contain text; in particular, printed p.76 is **not** blank in this extraction. The page-75 section begins mid-continuation and includes Chapter X.10–14; the following sections continue through Chapters X–XV and their accompanying notes/apparatus. The PDF text layer interleaves English translation, Greek text, and critical notes in places, so the extraction order must not be treated as a reliable reading order without visual comparison.

| Printed page | Extracted characters | Extracted lines |
|---:|---:|---:|
| 75 | 2,341 | 111 |
| 76 | 2,588 | 78 |
| 77 | 2,534 | 86 |
| 78 | 2,344 | 75 |
| 79 | 2,364 | 78 |
| 80 | 2,395 | 77 |
| 81 | 2,422 | 85 |
| 82 | 2,250 | 78 |
| 83 | 2,593 | 95 |
| 84 | 2,280 | 92 |

## Known OCR/text-layer limitations

- Greek fragments are systematically corrupted or transliterated inconsistently.
- English words, Greek text, and lower-page critical apparatus may be interleaved.
- Line-end hyphenation and column-order artifacts remain.
- Ligatures and letterforms are inconsistently represented.
- Folio recognition in OCR should not be used as the page-mapping authority; the mapping above is based on the BookReader leaf sequence and printed-page labels used in the batch.
- The extraction is one consolidated text-layer file. Separate per-page OCR text files are not present in the tracked batch.

## Evidence status

| Evidence | Status | What it establishes |
|---|---|---|
| Retrieval manifest | 10/10 recorded HTTP 200 | Source URL, response metadata, dimensions, byte counts, SHA-256 |
| High-resolution JPEGs | 10 files committed | Page-image files are present in Git at 1360×2274 per manifest |
| Consolidated OCR | 10/10 page markers and non-empty sections | Searchable text-layer material for printed pp.75–84 |
| PDF-native PNGs | Not present in tracked batch | No claim of extracted native PNGs |
| Individual visual inspection | Pending | No page is counted as image-checked from retrieval alone |
| Line-by-line diplomatic collation | Pending | OCR is not a substitute for facsimile comparison |
| Independent human review | Pending | No independent approval recorded |

## Next proofing actions

1. Open each of the ten high-resolution JPEGs and confirm its printed folio against the leaf mapping.
2. Compare English translation, Greek parallel, and critical apparatus against the consolidated text layer page by page.
3. Record page-specific OCR and transcription discrepancies, especially Greek readings, brackets, punctuation, and column-order issues.
4. Add individual rows to `IMAGE_PROOFING_LOG.md` only after actual image inspection.
5. Obtain independent human review separately; do not infer approval from automated retrieval or OCR checks.

**Important:** successful download, a valid manifest, and searchable text do not equal visual proofing. This batch increases retrieval coverage, not the individually inspected-page count.
