# Text-Layer Collation Report: Printed pp. 63–74

**Source:** Cornell / Internet Archive scan `enoch-1893-clarendon-original.pdf` (identifier: `cu31924014590545`)
**BookReader leaves:** n84–n95
**Committed image files:** 12/12 BookReader JPEGs (340×569, medium quality), with manifest and SHA-256 hashes
**OCR basis:** Embedded PDF text layer; page summaries and OCR statistics are reported here, but individual `printed_p063.txt`–`printed_p074.txt` files are not committed in this directory.

## Page Mapping & File Inventory

| Printed p. | BookReader leaf | PDF p. | BookReader JPEG | PDF full PNG | OCR text |
|------------|-----------------|--------|-----------------|--------------|----------|
| 63 | n84 | 85 | p063_n084.jpg | printed_p063_full.png | printed_p063.txt |
| 64 | n85 | 86 | p064_n085.jpg | printed_p064_full.png | printed_p064.txt |
| 65 | n86 | 87 | p065_n086.jpg | printed_p065_full.png | printed_p065.txt |
| 66 | n87 | 88 | p066_n087.jpg | printed_p066_full.png | printed_p066.txt |
| 67 | n88 | 89 | p067_n088.jpg | printed_p067_full.png | printed_p067.txt |
| 68 | n89 | 90 | p068_n089.jpg | printed_p068_full.png | printed_p068.txt |
| 69 | n90 | 91 | p069_n090.jpg | printed_p069_full.png | printed_p069.txt |
| 70 | n91 | 92 | p070_n091.jpg | printed_p070_full.png | printed_p070.txt |
| 71 | n92 | 93 | p071_n092.jpg | printed_p071_full.png | printed_p071.txt |
| 72 | n93 | 94 | p072_n093.jpg | printed_p072_full.png | printed_p072.txt |
| 73 | n94 | 95 | p073_n094.jpg | printed_p073_full.png | printed_p073.txt |
| 74 | n95 | 96 | p074_n095.jpg | printed_p074_full.png | printed_p074.txt |

## OCR Text Statistics

| Page | Char Count | Lines | Content Summary |
|------|------------|-------|-----------------|
| 63 | 2536 | 108 | Ch. VI oath on Mount Hermon, leaders named |
| 64 | 2583 | 107 | Mount Hermon naming, 20 leaders listed |
| 65 | 2511 | 116 | Azazel teaches charms, giants born (3000 ells) |
| 66 | 2629 | 112 | Metals, weapons, cosmetics, corruption |
| 67 | 2574 | 118 | Amzarak, Armares, root-cutters, astrologers |
| 68 | 1298 | 64 | Greek fragments, Watchers' petition |
| 69 | 2523 | 160 | Souls complain to holy ones, Semjaza |
| 70 | 2712 | 141 | Semjaza's authority, enchantments revealed |
| 71 | 2264 | 94 | Ch. IX.7–X.2, Most High sends Arsjalaljar |
| 72 | 2802 | 130 | Noah instructed, Raphael binds Azazel |
| 73 | 2451 | 111 | Heal earth, bind watchers, destroy each other |
| 74 | 2277 | 123 | Watchers led out, destruction, length of days |

## OCR Defects Noted

1. **Page 68**: Low text count (1298 chars) — Greek fragments dominate, heavy garbling
2. **Pages 65, 71**: Printed page numbers not detected by OCR (confirmed by content continuity)
3. **Greek fragments**: Systematically garbled (e.g., `ow evtvyydvovta Kal A€yovra`)
4. **Ligatures broken**: fi, fl, ff → separate characters
5. **Hyphenation artifacts**: Line-end hyphens remain in text layer
6. **Critical apparatus**: Mixed with main text, not separated

## Image Evidence Status

| Page | BookReader JPEG | PDF Native Scan | Visual Inspection |
|------|-----------------|-----------------|-------------------|
| 63–74 | ✅ Downloaded and individually opened (340×569) | Higher-resolution PNGs are referenced as local extraction outputs but are not present in this committed directory | Page identity and broad layout checked 12/12; fine-text/apparatus proofing pending |

**Note:** BookReader images are medium-quality JPEGs (340×569). The repository tree at this commit contains the 12 JPEGs, manifest, and this report; it does not contain the referenced `printed_p063_full.png`–`printed_p074_full.png` files or per-page OCR `.txt` files. If those files exist in a local working directory, they must be added or otherwise made available before they can be independently checked from the repository. Higher-resolution scans (1360×2274) are still required for detailed apparatus and diplomatic verification.

## Verification Protocol

For each page, the following must be confirmed by human inspection:

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

1. ✅ Open each of the 12 committed BookReader JPEGs individually; printed folios 63–74 and broad layout are visible
2. **High-resolution inspection**: Obtain and inspect all 12 native PDF page images; the small apparatus and Greek glyphs are not reliably readable in the medium JPEGs
3. **OCR comparison**: Compare 3–5 lines per page against high-resolution images; per-page OCR text files are not currently committed
4. **Record defects**: Log textual, punctuation, Greek, apparatus, and layout discrepancies separately
5. **Update ledger**: Do not treat the medium-resolution page/layout checks as full diplomatic proofing