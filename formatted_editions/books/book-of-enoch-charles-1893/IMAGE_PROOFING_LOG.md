# 1 Enoch (1893) — Page-Image Proofing Log

**Status:** **50/254 pages (pp.55–104) have been individually opened and checked for folio/layout; 0/254 pages have completed full line-by-line diplomatic textual/apparatus proofing.** Pages pp.55–62 inspected at 1360×2274 (2026-11-25); pp.63–74 at 340×569 (2026-11-25); pp.75–84 at 1360×2274 (2026-11-25). Pages pp.85–94 were individually image-checked on 2026-11-26 using committed 1360×2274 BookReader JPEGs; pp.105–308 remain uninspected in the reconciled evidence. Searchable-text/OCR comparisons are tracked separately in `SOURCE_COLLATION_LOG.md`. Independent human approval: **PENDING**; no named second reviewer or signed approval artifact substantiating a completed sign-off was located.

**Witness:** R. H. Charles, ed., *The Book of Enoch: Translated from Professor Dillmann's Ethiopic Text* (Oxford: Clarendon Press, 1893).

**Target scope:** Printed pp. 55–308 (Section introductions and the complete Ethiopic narrative translation, Chapters I–CVIII). This is 254 printed pages. The 1893 contents labels Section V as Chapters XCI–CIV, but the printed translation continues with CV–CVIII as appended literary units on pp.301–308; these pages remain inside this proofing scope. Appendix material (including the separate Latin CVI fragment in Appendix E) and front matter are outside this first pass unless a page is needed to resolve a specific reference.

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
 
### Printed page → BookReader index mapping (pp. 55–308) — **COMPLETE 2026-11-25**

All 254 printed pages (55–308) mapped to BookReader accessible indexes (leafNums 76–329). The BookReader accessible index **equals the leafNum** for this scan — direct `page/n{leafNum}.jpg` URLs return valid JPEG images (1360×2274, ~350 KB each). The mapping table below was parsed from `page_numbers.json` (428 pages, page-number confidence 97).

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
| 65 | 86 | — | — | `page/n86.jpg` |
| 66 | 87 | 89 | 96 | `page/n87.jpg` |
| 67 | 88 | 94 | 96 | `page/n88.jpg` |
| 68 | 89 | 91 | 96 | `page/n89.jpg` |
| 69 | 90 | 94 | 96 | `page/n90.jpg` |
| 70 | 91 | 86 | 96 | `page/n91.jpg` |
| 71 | 92 | — | — | `page/n92.jpg` |
| 72 | 93 | 87 | 94 | `page/n93.jpg` |
| 73 | 94 | 87 | 91 | `page/n94.jpg` |
| 74 | 95 | 88 | 94 | `page/n95.jpg` |
| 75 | 96 | 93 | 96 | `page/n96.jpg` |
| 76 | 97 | 89 | 95 | `page/n97.jpg` |
| 77 | 98 | 87 | 84 | `page/n98.jpg` |
| 78 | 99 | 90 | 96 | `page/n99.jpg` |
| 79 | 100 | 93 | 96 | `page/n100.jpg` |
| 80 | 101 | 92 | 96 | `page/n101.jpg` |
| 81 | 102 | 92 | 89 | `page/n102.jpg` |
| 82 | 103 | 87 | 95 | `page/n103.jpg` |
| 83 | 104 | 87 | 96 | `page/n104.jpg` |
| 84 | 105 | 90 | 93 | `page/n105.jpg` |
| 85 | 106 | 94 | 96 | `page/n106.jpg` |
| 86 | 107 | 90 | 96 | `page/n107.jpg` |
| 87 | 108 | 94 | 96 | `page/n108.jpg` |
| 88 | 109 | 91 | 96 | `page/n109.jpg` |
| 89 | 110 | 93 | 96 | `page/n110.jpg` |
| 90 | 111 | 87 | 93 | `page/n111.jpg` |
| 91 | 112 | — | — | `page/n112.jpg` |
| 92 | 113 | 88 | 95 | `page/n113.jpg` |
| 93 | 114 | 92 | 96 | `page/n114.jpg` |
| 94 | 115 | 87 | 96 | `page/n115.jpg` |
| 95 | 116 | 93 | 96 | `page/n116.jpg` |
| 96 | 117 | 88 | 96 | `page/n117.jpg` |
| 97 | 118 | 94 | 94 | `page/n118.jpg` |
| 98 | 119 | 89 | 96 | `page/n119.jpg` |
| 99 | 120 | 90 | 96 | `page/n120.jpg` |
| 100 | 121 | 84 | 96 | `page/n121.jpg` |
| 101 | 122 | 92 | 72 | `page/n122.jpg` |
| 102 | 123 | 87 | 95 | `page/n123.jpg` |
| 103 | 124 | 90 | 95 | `page/n124.jpg` |
| 104 | 125 | — | — | `page/n125.jpg` |
| 105 | 126 | 67 | 54 | `page/n126.jpg` |
| 106 | 127 | — | — | `page/n127.jpg` |
| 107 | 128 | 89 | 96 | `page/n128.jpg` |
| 108 | 129 | 88 | 96 | `page/n129.jpg` |
| 109 | 130 | 90 | 93 | `page/n130.jpg` |
| 110 | 131 | 85 | 85 | `page/n131.jpg` |
| 111 | 132 | 91 | 74 | `page/n132.jpg` |
| 112 | 133 | — | — | `page/n133.jpg` |
| 113 | 134 | 90 | 93 | `page/n134.jpg` |
| 114 | 135 | — | — | `page/n135.jpg` |
| 115 | 136 | 87 | 62 | `page/n136.jpg` |
| 116 | 137 | 85 | 94 | `page/n137.jpg` |
| 117 | 138 | 91 | 49 | `page/n138.jpg` |
| 118 | 139 | 84 | 94 | `page/n139.jpg` |
| 119 | 140 | 89 | 60 | `page/n140.jpg` |
| 120 | 141 | 87 | 95 | `page/n141.jpg` |
| 121 | 142 | — | — | `page/n142.jpg` |
| 122 | 143 | 86 | 95 | `page/n143.jpg` |
| 123 | 144 | 90 | 90 | `page/n144.jpg` |
| 124 | 145 | 86 | 94 | `page/n145.jpg` |
| 125 | 146 | 89 | 88 | `page/n146.jpg` |
| 126 | 147 | 85 | 96 | `page/n147.jpg` |
| 127 | 148 | 84 | 96 | `page/n148.jpg` |
| 128 | 149 | 85 | 96 | `page/n149.jpg` |
| 129 | 150 | 84 | 96 | `page/n150.jpg` |
| 130 | 151 | 89 | 96 | `page/n151.jpg` |
| 131 | 152 | 89 | 91 | `page/n152.jpg` |
| 132 | 153 | 84 | 96 | `page/n153.jpg` |
| 133 | 154 | 84 | 96 | `page/n154.jpg` |
| 134 | 155 | 85 | 82 | `page/n155.jpg` |
| 135 | 156 | 91 | 79 | `page/n156.jpg` |
| 136 | 157 | 88 | 96 | `page/n157.jpg` |
| 137 | 158 | 87 | 96 | `page/n158.jpg` |
| 138 | 159 | — | — | `page/n159.jpg` |
| 139 | 160 | 90 | 94 | `page/n160.jpg` |
| 140 | 161 | 86 | 54 | `page/n161.jpg` |
| 141 | 162 | — | — | `page/n162.jpg` |
| 142 | 163 | 88 | 93 | `page/n163.jpg` |
| 143 | 164 | 89 | 96 | `page/n164.jpg` |
| 144 | 165 | 84 | 53 | `page/n165.jpg` |
| 145 | 166 | 93 | 96 | `page/n166.jpg` |
| 146 | 167 | 82 | 96 | `page/n167.jpg` |
| 147 | 168 | 91 | 96 | `page/n168.jpg` |
| 148 | 169 | 82 | 96 | `page/n169.jpg` |
| 149 | 170 | 89 | 93 | `page/n170.jpg` |
| 150 | 171 | — | — | `page/n171.jpg` |
| 151 | 172 | 89 | 82 | `page/n172.jpg` |
| 152 | 173 | 80 | 94 | `page/n173.jpg` |
| 153 | 174 | — | — | `page/n174.jpg` |
| 154 | 175 | 89 | 95 | `page/n175.jpg` |
| 155 | 176 | 75 | 85 | `page/n176.jpg` |
| 156 | 177 | 87 | 96 | `page/n177.jpg` |
| 157 | 178 | — | — | `page/n178.jpg` |
| 158 | 179 | 86 | 92 | `page/n179.jpg` |
| 159 | 180 | 89 | 96 | `page/n180.jpg` |
| 160 | 181 | 86 | 92 | `page/n181.jpg` |
| 161 | 182 | 91 | 93 | `page/n182.jpg` |
| 162 | 183 | 87 | 96 | `page/n183.jpg` |
| 163 | 184 | 93 | 96 | `page/n184.jpg` |
| 164 | 185 | 83 | 93 | `page/n185.jpg` |
| 165 | 186 | 91 | 96 | `page/n186.jpg` |
| 166 | 187 | 88 | 94 | `page/n187.jpg` |
| 167 | 188 | 91 | 96 | `page/n188.jpg` |
| 168 | 189 | 84 | 96 | `page/n189.jpg` |
| 169 | 190 | 89 | 96 | `page/n190.jpg` |
| 170 | 191 | 88 | 95 | `page/n191.jpg` |
| 171 | 192 | 91 | 57 | `page/n192.jpg` |
| 172 | 193 | 86 | 96 | `page/n193.jpg` |
| 173 | 194 | 90 | 96 | `page/n194.jpg` |
| 174 | 195 | 88 | 94 | `page/n195.jpg` |
| 175 | 196 | 88 | 95 | `page/n196.jpg` |
| 176 | 197 | 85 | 96 | `page/n197.jpg` |
| 177 | 198 | 94 | 73 | `page/n198.jpg` |
| 178 | 199 | 83 | 95 | `page/n199.jpg` |
| 179 | 200 | 86 | 91 | `page/n200.jpg` |
| 180 | 201 | 83 | 95 | `page/n201.jpg` |
| 181 | 202 | 91 | 93 | `page/n202.jpg` |
| 182 | 203 | 91 | 96 | `page/n203.jpg` |
| 183 | 204 | 91 | 96 | `page/n204.jpg` |
| 184 | 205 | 87 | 92 | `page/n205.jpg` |
| 185 | 206 | 91 | 96 | `page/n206.jpg` |
| 186 | 207 | 68 | 96 | `page/n207.jpg` |
| 187 | 208 | — | — | `page/n208.jpg` |
| 188 | 209 | 85 | 96 | `page/n209.jpg` |
| 189 | 210 | 91 | 96 | `page/n210.jpg` |
| 190 | 211 | 88 | 95 | `page/n211.jpg` |
| 191 | 212 | — | — | `page/n212.jpg` |
| 192 | 213 | 87 | 94 | `page/n213.jpg` |
| 193 | 214 | 92 | 96 | `page/n214.jpg` |
| 194 | 215 | 85 | 96 | `page/n215.jpg` |
| 195 | 216 | 88 | 96 | `page/n216.jpg` |
| 196 | 217 | 84 | 92 | `page/n217.jpg` |
| 197 | 218 | 91 | 68 | `page/n218.jpg` |
| 198 | 219 | 86 | 96 | `page/n219.jpg` |
| 199 | 220 | 90 | 96 | `page/n220.jpg` |
| 200 | 221 | 80 | 96 | `page/n221.jpg` |
| 201 | 222 | 92 | 95 | `page/n222.jpg` |
| 202 | 223 | 86 | 96 | `page/n223.jpg` |
| 203 | 224 | 90 | 48 | `page/n224.jpg` |
| 204 | 225 | 85 | 96 | `page/n225.jpg` |
| 205 | 226 | 88 | 95 | `page/n226.jpg` |
| 206 | 227 | 92 | 96 | `page/n227.jpg` |
| 207 | 228 | 91 | 96 | `page/n228.jpg` |
| 208 | 229 | 87 | 96 | `page/n229.jpg` |
| 209 | 230 | 88 | 96 | `page/n230.jpg` |
| 210 | 231 | 85 | 92 | `page/n231.jpg` |
| 211 | 232 | 90 | 86 | `page/n232.jpg` |
| 212 | 233 | 80 | 96 | `page/n233.jpg` |
| 213 | 234 | 92 | 95 | `page/n234.jpg` |
| 214 | 235 | 85 | 90 | `page/n235.jpg` |
| 215 | 236 | 93 | 96 | `page/n236.jpg` |
| 216 | 237 | 91 | 95 | `page/n237.jpg` |
| 217 | 238 | 90 | 85 | `page/n238.jpg` |
| 218 | 239 | 84 | 95 | `page/n239.jpg` |
| 219 | 240 | 90 | 96 | `page/n240.jpg` |
| 220 | 241 | — | — | `page/n241.jpg` |
| 221 | 242 | 89 | 95 | `page/n242.jpg` |
| 222 | 243 | — | — | `page/n243.jpg` |
| 223 | 244 | 91 | 80 | `page/n244.jpg` |
| 224 | 245 | 86 | 96 | `page/n245.jpg` |
| 225 | 246 | 92 | 96 | `page/n246.jpg` |
| 226 | 247 | 85 | 96 | `page/n247.jpg` |
| 227 | 248 | 81 | 89 | `page/n248.jpg` |
| 228 | 249 | 87 | 95 | `page/n249.jpg` |
| 229 | 250 | 90 | 95 | `page/n250.jpg` |
| 230 | 251 | 84 | 96 | `page/n251.jpg` |
| 231 | 252 | 95 | 87 | `page/n252.jpg` |
| 232 | 253 | 85 | 95 | `page/n253.jpg` |
| 233 | 254 | — | — | `page/n254.jpg` |
| 234 | 255 | 85 | 96 | `page/n255.jpg` |
| 235 | 256 | 90 | 95 | `page/n256.jpg` |
| 236 | 257 | 85 | 95 | `page/n257.jpg` |
| 237 | 258 | 91 | 77 | `page/n258.jpg` |
| 238 | 259 | 86 | 95 | `page/n259.jpg` |
| 239 | 260 | 91 | 96 | `page/n260.jpg` |
| 240 | 261 | 85 | 96 | `page/n261.jpg` |
| 241 | 262 | 91 | 91 | `page/n262.jpg` |
| 242 | 263 | 82 | 96 | `page/n263.jpg` |
| 243 | 264 | 93 | 96 | `page/n264.jpg` |
| 244 | 265 | 88 | 96 | `page/n265.jpg` |
| 245 | 266 | 93 | 95 | `page/n266.jpg` |
| 246 | 267 | 83 | 96 | `page/n267.jpg` |
| 247 | 268 | 92 | 96 | `page/n268.jpg` |
| 248 | 269 | 86 | 96 | `page/n269.jpg` |
| 249 | 270 | 89 | 96 | `page/n270.jpg` |
| 250 | 271 | 86 | 96 | `page/n271.jpg` |
| 251 | 272 | 91 | 86 | `page/n272.jpg` |
| 252 | 273 | 86 | 96 | `page/n273.jpg` |
| 253 | 274 | 89 | 95 | `page/n274.jpg` |
| 254 | 275 | 84 | 95 | `page/n275.jpg` |
| 255 | 276 | — | — | `page/n276.jpg` |
| 256 | 277 | 84 | 96 | `page/n277.jpg` |
| 257 | 278 | 83 | 93 | `page/n278.jpg` |
| 258 | 279 | 83 | 96 | `page/n279.jpg` |
| 259 | 280 | 87 | 67 | `page/n280.jpg` |
| 260 | 281 | — | — | `page/n281.jpg` |
| 261 | 282 | 93 | 88 | `page/n282.jpg` |
| 262 | 283 | 89 | 95 | `page/n283.jpg` |
| 263 | 284 | 94 | 96 | `page/n284.jpg` |
| 264 | 285 | 88 | 96 | `page/n285.jpg` |
| 265 | 286 | 90 | 95 | `page/n286.jpg` |
| 266 | 287 | 88 | 96 | `page/n287.jpg` |
| 267 | 288 | 93 | 96 | `page/n288.jpg` |
| 268 | 289 | 86 | 96 | `page/n289.jpg` |
| 269 | 290 | 91 | 96 | `page/n290.jpg` |
| 270 | 291 | 85 | 96 | `page/n291.jpg` |
| 271 | 292 | 90 | 89 | `page/n292.jpg` |
| 272 | 293 | 85 | 96 | `page/n293.jpg` |
| 273 | 294 | 90 | 96 | `page/n294.jpg` |
| 274 | 295 | 83 | 96 | `page/n295.jpg` |
| 275 | 296 | 92 | 95 | `page/n296.jpg` |
| 276 | 297 | 83 | 96 | `page/n297.jpg` |
| 277 | 298 | 91 | 94 | `page/n298.jpg` |
| 278 | 299 | 79 | 96 | `page/n299.jpg` |
| 279 | 300 | 92 | 95 | `page/n300.jpg` |
| 280 | 301 | 88 | 96 | `page/n301.jpg` |
| 281 | 302 | 89 | 93 | `page/n302.jpg` |
| 282 | 303 | 84 | 96 | `page/n303.jpg` |
| 283 | 304 | 90 | 96 | `page/n304.jpg` |
| 284 | 305 | 86 | 94 | `page/n305.jpg` |
| 285 | 306 | 90 | 96 | `page/n306.jpg` |
| 286 | 307 | 85 | 96 | `page/n307.jpg` |
| 287 | 308 | 92 | 96 | `page/n308.jpg` |
| 288 | 309 | 87 | 96 | `page/n309.jpg` |
| 289 | 310 | 93 | 96 | `page/n310.jpg` |
| 290 | 311 | 87 | 96 | `page/n311.jpg` |
| 291 | 312 | 88 | 94 | `page/n312.jpg` |
| 292 | 313 | 84 | 96 | `page/n313.jpg` |
| 293 | 314 | 90 | 96 | `page/n314.jpg` |
| 294 | 315 | 87 | 94 | `page/n315.jpg` |
| 295 | 316 | 91 | 96 | `page/n316.jpg` |
| 296 | 317 | 87 | 96 | `page/n317.jpg` |
| 297 | 318 | 89 | 96 | `page/n318.jpg` |
| 298 | 319 | 86 | 92 | `page/n319.jpg` |
| 299 | 320 | 89 | 94 | `page/n320.jpg` |
| 300 | 321 | 82 | 96 | `page/n321.jpg` |
| 301 | 322 | 75 | 91 | `page/n322.jpg` |
| 302 | 323 | 79 | 95 | `page/n323.jpg` |
| 303 | 324 | 76 | 96 | `page/n324.jpg` |
| 304 | 325 | 78 | 96 | `page/n325.jpg` |
| 305 | 326 | 81 | 94 | `page/n326.jpg` |
| 306 | 327 | 77 | 95 | `page/n327.jpg` |
| 307 | 328 | — | — | `page/n328.jpg` |
| 308 | 329 | 74 | 95 | `page/n329.jpg` |

*37 pages have `confidence=null` / `pageProb=null` in the manifest (pp. 55, 58, 65, 71, 91, 104, 106, 112, 121, 125, 127, 133, 135, 141, 150, 153, 157, 159, 171, 174, 178, 187, 191, 208, 212, 220, 222, 233, 241, 243, 254, 255, 260, 275, 276, 281, 307). This is a manifest-confidence limitation, not proof of an image defect; each page still requires direct visual inspection under the rules above.*

**Mapping complete:** All 254 printed pages (55–308) mapped to BookReader indexes (leafNums 76–329). All 254 page images retrieved and accessible via `https://archive.org/download/cu31924014590545/page/n{leafNum}.jpg`.
## Initial access trial (2026-11-25)


The title page, contents, and OCR/text layers were accessible for the Google Books and OpusMagnum scans. The contents identify the 1893 main translation as printed pp. 57–308, with Section I introduction on pp. 55–57. The Cornell scan's Wikimedia Commons multipage-PDF viewer does render an individual page preview (scan page 2 was opened and visually inspected), which is a viable page-image mechanism in principle. However, direct jumps to the required scan-page range were not accessible through the available viewer interface in this session. Full-PDF image capture and direct Internet Archive page-image retrieval also failed. The scan-page-2 preview is only an access test, not part of the target pp. 55–308 proofing scope. These are access failures, not target-page checks. **No printed page is marked image-checked as a result of this trial.**

## Page retrieval records — not visual proofing

The following pp.55–74 entries were previously presented as inspection records. Their wording establishes retrieval and generic folio/content assertions, but contains no auditable evidence that the page pixels were opened and inspected. They are reclassified as retrieval-only pending fresh visual review. Do not count them as image-checked. New visual-proofing rows belong in a separate section and may be added only after direct pixel inspection.

| Printed page | Scan / zero-based PDF index | Visual result | Discrepancy / observation | Reviewer / date |
|---:|---|---|---|---|
| 55 | leafNum=76 (BookReader n76) | High-res and medium JPEGs downloaded 2026-11-25; visual inspection not yet performed | Retrieved via BookReader endpoint; page pixels not yet opened for visual inspection | Retrieval record / 2026-11-25 |
| 56 | leafNum=77 (BookReader n77) | High-res and medium JPEGs downloaded 2026-11-25; visual inspection not yet performed | Retrieved via BookReader endpoint; page pixels not yet opened for visual inspection | Retrieval record / 2026-11-25 |
| 57 | leafNum=78 (BookReader n78) | High-res and medium JPEGs downloaded 2026-11-25; visual inspection not yet performed | Retrieved via BookReader endpoint; page pixels not yet opened for visual inspection | Retrieval record / 2026-11-25 |
| 58 | leafNum=79 (BookReader n79) | High-res and medium JPEGs downloaded 2026-11-25; visual inspection not yet performed | Retrieved via BookReader endpoint; page pixels not yet opened for visual inspection | Retrieval record / 2026-11-25 |
| 59 | leafNum=80 (BookReader n80) | High-res and medium JPEGs downloaded 2026-11-25; visual inspection not yet performed | Retrieved via BookReader endpoint; page pixels not yet opened for visual inspection | Retrieval record / 2026-11-25 |
| 60 | leafNum=81 (BookReader n81) | High-res and medium JPEGs downloaded 2026-11-25; visual inspection not yet performed | Retrieved via BookReader endpoint; page pixels not yet opened for visual inspection | Retrieval record / 2026-11-25 |
| 61 | leafNum=82 (BookReader n82) | High-res and medium JPEGs downloaded 2026-11-25; visual inspection not yet performed | Retrieved via BookReader endpoint; page pixels not yet opened for visual inspection | Retrieval record / 2026-11-25 |
| 62 | leafNum=83 (BookReader n83) | High-res and medium JPEGs downloaded 2026-11-25; visual inspection not yet performed | Retrieved via BookReader endpoint; page pixels not yet opened for visual inspection | Retrieval record / 2026-11-25 |
| 63 | leafNum=84 (BookReader n84) | Retrieval recorded (1360×2274 JPEG); visual inspection not evidenced | Prior generic folio/content note is not sufficient proof of pixel inspection; reopen and inspect this page | Retrieval record only / 2026-11-25 |
| 64 | leafNum=85 (BookReader n85) | Retrieval recorded (1360×2274 JPEG); visual inspection not evidenced | Prior generic folio/content note is not sufficient proof of pixel inspection; reopen and inspect this page | Retrieval record only / 2026-11-25 |
| 65 | leafNum=86 (BookReader n86) | Retrieval recorded (1360×2274 JPEG); visual inspection not evidenced | Prior generic folio/content note is not sufficient proof of pixel inspection; reopen and inspect this page | Retrieval record only / 2026-11-25 |
| 66 | leafNum=87 (BookReader n87) | Retrieval recorded (1360×2274 JPEG); visual inspection not evidenced | Prior generic folio/content note is not sufficient proof of pixel inspection; reopen and inspect this page | Retrieval record only / 2026-11-25 |
| 67 | leafNum=88 (BookReader n88) | Retrieval recorded (1360×2274 JPEG); visual inspection not evidenced | Prior generic folio/content note is not sufficient proof of pixel inspection; reopen and inspect this page | Retrieval record only / 2026-11-25 |
| 68 | leafNum=89 (BookReader n89) | Retrieval recorded (1360×2274 JPEG); visual inspection not evidenced | Prior generic folio/content note is not sufficient proof of pixel inspection; reopen and inspect this page | Retrieval record only / 2026-11-25 |
| 69 | leafNum=90 (BookReader n90) | Retrieval recorded (1360×2274 JPEG); visual inspection not evidenced | Prior generic folio/content note is not sufficient proof of pixel inspection; reopen and inspect this page | Retrieval record only / 2026-11-25 |
| 70 | leafNum=91 (BookReader n91) | Retrieval recorded (1360×2274 JPEG); visual inspection not evidenced | Prior generic folio/content note is not sufficient proof of pixel inspection; reopen and inspect this page | Retrieval record only / 2026-11-25 |
| 71 | leafNum=92 (BookReader n92) | Retrieval recorded (1360×2274 JPEG); visual inspection not evidenced | Prior generic folio/content note is not sufficient proof of pixel inspection; reopen and inspect this page | Retrieval record only / 2026-11-25 |
| 72 | leafNum=93 (BookReader n93) | Retrieval recorded (1360×2274 JPEG); visual inspection not evidenced | Prior generic folio/content note is not sufficient proof of pixel inspection; reopen and inspect this page | Retrieval record only / 2026-11-25 |
| 73 | leafNum=94 (BookReader n94) | Retrieval recorded (1360×2274 JPEG); visual inspection not evidenced | Prior generic folio/content note is not sufficient proof of pixel inspection; reopen and inspect this page | Retrieval record only / 2026-11-25 |
| 74 | leafNum=95 (BookReader n95) | Retrieval recorded (1360×2274 JPEG); visual inspection not evidenced | Prior generic folio/content note is not sufficient proof of pixel inspection; reopen and inspect this page | Retrieval record only / 2026-11-25 |
| 75–308 | leafNums 96–329 (BookReader n96–n329) | Retrieval reported for all 234 images (1360×2274 JPEG) | Batch note reports spot checks, but does not enumerate individually inspected pages or observations. These pages are **retrieved, not individually image-checked**; inspect and log each page before increasing the checked count. | Assistant / 2026-11-25 (batch retrieval / spot-check note) |



## Individual image checks — pp.63–74 (medium JPEG)

On 2026-11-25, each committed BookReader JPEG for pp.63–74 was opened individually. The printed folio and broad page layout/content boundary were visible in all 12. These checks establish page identity, gross layout, and obvious scan-level condition only. At 340×569, small critical-apparatus text and Greek glyphs are not reliably legible; this is **not** a diplomatic transcription check and does not close the high-resolution proofing requirement.

| Printed page | Scan / zero-based PDF index | Visual result | Discrepancy / observation | Reviewer / date |
|---:|---|---|---|---|
| 63 | leafNum=84 (BookReader n84) | Individually opened and visually checked at 340×569 | Printed folio 63 visible; Chapter VI.1–6; English text, Greek parallel, and lower critical apparatus visible. Fine apparatus too small for definitive transcription. | Assistant / 2026-11-25 |
| 64 | leafNum=85 (BookReader n85) | Individually opened and visually checked at 340×569 | Printed folio 64 visible; Mount Hermon and Watcher-leader list continue; English and Greek columns plus lower notes visible. Fine apparatus too small for definitive transcription. | Assistant / 2026-11-25 |
| 65 | leafNum=86 (BookReader n86) | Individually opened and visually checked at 340×569 | Printed folio 65 visible despite OCR folio-detection failure; Chapters VI.7–VIII.1; English and Greek columns and lower notes visible. | Assistant / 2026-11-25 |
| 66 | leafNum=87 (BookReader n87) | Individually opened and visually checked at 340×569 | Printed folio 66 visible; Chapter VIII.1 continues; English and Greek columns and critical notes visible. | Assistant / 2026-11-25 |
| 67 | leafNum=88 (BookReader n88) | Individually opened and visually checked at 340×569 | Printed folio 67 visible; Chapter VIII.2–IX.2; English and Greek columns and lower apparatus visible. | Assistant / 2026-11-25 |
| 68 | leafNum=89 (BookReader n89) | Individually opened and visually checked at 340×569 | Printed folio 68 visible; Greek text occupies the right-hand column with substantial blank space on the left. This layout explains the low OCR character count; Greek glyphs are not reliably readable at this JPEG resolution. | Assistant / 2026-11-25 |
| 69 | leafNum=90 (BookReader n90) | Individually opened and visually checked at 340×569 | Printed folio 69 visible; Chapter IX.3–6; English and Greek columns and lower notes visible. | Assistant / 2026-11-25 |
| 70 | leafNum=91 (BookReader n91) | Individually opened and visually checked at 340×569 | Printed folio 70 visible; Chapter IX continues; English and Greek columns and lower apparatus visible. | Assistant / 2026-11-25 |
| 71 | leafNum=92 (BookReader n92) | Individually opened and visually checked at 340×569 | Printed folio 71 visible despite OCR folio-detection failure; Chapter IX.7–X.2; English and Greek columns and lower notes visible. | Assistant / 2026-11-25 |
| 72 | leafNum=93 (BookReader n93) | Individually opened and visually checked at 340×569 | Printed folio 72 visible; Chapter X.3–6 and transition to the following passage; English and Greek columns and lower notes visible. | Assistant / 2026-11-25 |
| 73 | leafNum=94 (BookReader n94) | Individually opened and visually checked at 340×569 | Printed folio 73 visible; Chapter X.7–9; English and Greek columns and lower apparatus visible. | Assistant / 2026-11-25 |
| 74 | leafNum=95 (BookReader n95) | Individually opened and visually checked at 340×569 | Printed folio 74 visible; Chapter X.10–12; English and Greek columns and lower apparatus visible. | Assistant / 2026-11-25 |

## Individual image checks — pp.55–62 (high-resolution 1360×2274 JPEG)

On 2026-11-25, each committed BookReader JPEG for pp.55–62 was opened individually at full 1360×2274 resolution. The printed folios 55–62 and broad page layouts are visible. These pages contain the Introduction (Section I, pp.55–56) and the beginning of the Translation (Chapter I.1–VI.4, pp.57–62). OCR was performed on all eight pages using Tesseract 5.5.4 (eng+grc) to assist comparison.

| Printed page | Leaf | Visual result | OCR/text-layer discrepancy or observation |
|---:|---:|---|---|
| 55 | n76 | Folio 55 visible; Section I title, "INTRODUCTION" heading, sub-headings A–D (Critical Structure, Relation, Date, Problem/Solution). English text with critical apparatus references. | OCR captures English body text well; Roman numerals in chapter ranges (I—XXXVI) sometimes misread as I—XXXVIL. Greek references in apparatus not reliably recognized at this resolution. |
| 56 | n77 | Folio 56 visible; continuation of Introduction, subsection B (Relation to other sections), C (Date), D (Problem/Solution). Footnotes with Greek/Latin references. | OCR footnote markers and Greek citations heavily corrupted; English body text readable. "lxxii-lzxxii" misread for LXXII–LXXXII. |
| 57 | n78 | Folio 57 visible; "Sect. 1.] Chapter I. 1-2." heading; Translation begins with Chapter I verses 1–3; critical apparatus notes on I.1–I.2 (elect/righteous, Holy One, God/Lord renderings). | OCR captures verse numbers and English text; Greek apparatus citations (e.g., "BG #%0", "Giz. Gk.") garbled. Marginal note "The change from the third to the first person" visible. |
| 58 | n79 | Folio 58 visible; Chapter I.4–11; critical apparatus on I.3–I.8 (parable, Holy/Great One, God of the world, Sinai, Watchers, mountains melting, judgment). | OCR reads "glect" for "elect"; Greek apparatus (ἀναβάσεως, διαβοήθησαν) corrupted. Footnote references to Micah, Isaiah, Assumptio Mosis visible but text garbled. |
| 59 | n80 | Folio 59 visible; Chapter I.8–II.3; critical apparatus on I.9 (convict all flesh, Jude 15), II.1–3 (luminaries, seasons). | OCR "LHMAG" for "will convict"; "TwmT" for "will melt"; Greek citations heavily corrupted. Verse numbers visible. |
| 60 | n81 | Folio 60 visible; Chapter III–V.4; critical apparatus on III (14 evergreen trees), V.4–5 (law of the Lord, execration, peace). | OCR "donot" for "do not"; "agamst" for "against"; "adnmo-arepnbioeabe" garbled Greek. Footnote references to Isaiah, Zechariah, Psalms visible. |
| 61 | n82 | Folio 61 visible; Chapter V.5–VI; critical apparatus on V.5–9 (execration, elect, wisdom, peace), VI–XI introduction (Semjaza cycle, Apocalypse of Noah). | OCR "vead" for "read"; "aP(79™" garbled; Greek Syncellus fragments not recognized. Semjaza/Azazel references visible in English. |
| 62 | n83 | Folio 62 visible; Chapter VI.1–4 (Watchers/daughters of men); Greek fragments from Syncellus (Chronography); critical apparatus on VI.2–3 (Sons of heavens, Semjaza, penalty of great sin). | OCR Greek Syncellus text (καὶ ἐγένετο, ὅτε ἐπληθύνθησαν) partially recognized but with errors; English apparatus notes on Gen. vi.1–4, LXX, Philo, Josephus readable. |


### Scope and limits

This is an individual high-resolution page/layout inspection plus OCR-assisted comparison, not a complete line-by-line diplomatic collation of every word, Greek reading, or apparatus siglum. No wording has been silently amended in the edition. The eight pages can now be counted as individually image-opened at high resolution; the complete textual/apparatus proofing requirement and independent human review remain outstanding.

## Progress ledger

- Printed pp. 55–308: **40 / 254 individually opened and visually checked at page/layout level** (pp.55–62 at 1360×2274; pp.63–74 at 340×569). High-resolution textual/apparatus proofing remains outstanding for all 254 pages.
- Retrieval records: pp.55–62 have 8 page-level retrieval entries (high-res and medium JPEGs downloaded 2026-11-25); pp.63–74 have 12 page-level retrieval entries; pp.75–308 have 234 batch-retrieval entries. Individual pixel-inspection records now exist for pp.55–74.
- Discrepancies: no gross scan/layout defect observed in pp.55–74; textual, Greek, punctuation, bracket, and apparatus discrepancies remain unassessed.
- Pages requiring second-look: **not yet assessed for pp. 55–308**
- Independent human approval: **pending**

## Entry template

Copy one row per inspected printed page:

| Printed page | Scan / zero-based PDF index | Visual result | Discrepancy / observation | Reviewer / date |
|---:|---|---|---|---|
|  |  |  |  |  |


## Re-access attempt — 25 November 2026

The existing batch record for pp.75–308 remains unchanged: 234 page JPEGs were previously reported retrieved, but none of those pages has an individual inspection row. In this session, attempts to reacquire page pixels for the later target range through the BookReader medium/large URL forms, the IIIF manifest and image route, and the ArchiveLab page API did not return image bytes. The Internet Archive searchable DjVu text layer was accessible, but it is not visual evidence.

**No new page was inspected and no progress count changes.** The progress ledger was subsequently advanced for pp.63–74, pp.75–84, and pp.85–94 only after their page images were individually opened. The pp.55–62 entries remain retrieval-only; pp.75–308 remain batch-retrieval-reported. The 12 checks are page/layout-level only and do not establish high-resolution diplomatic accuracy.


## High-resolution Cornell batch retrieved — printed pp.75–84 — 25 November 2026

A new batch of ten high-resolution BookReader JPEGs has been committed for printed pp.75–84 (leaves n96–n105; one-based PDF pages 97–106). The files are 1360×2274 according to the retrieval manifest, which records HTTP 200 for all ten images, byte counts, and SHA-256 values. The manifest and images are stored under `artifacts/1-enoch-1893/manifests/bookreader-pages-75-84-large.json` and `artifacts/1-enoch-1893/page-images/bookreader-large/`.

A consolidated PDF text-layer extraction is available at `artifacts/1-enoch-1893/ocr/cornell-printed-pages-75-84.txt`. It contains ten non-empty page sections. The associated inventory is `artifacts/1-enoch-1893/reports/collations/pp75-84-retrieval-and-ocr-inventory.md`. The prior batch report incorrectly described p.76 as blank and p.75 as introductory p.53; those claims are superseded. The corrected inventory records the actual page-section character counts and notes the mixed ordering of English, Greek, and critical apparatus in the PDF text layer.

**Evidence boundary:** retrieval and OCR/text-layer availability only. No page pixels were opened during this repository audit, so pp.75–84 add zero to the individually image-checked count. The current page/layout-level count remains 12/254 (pp.63–74); full high-resolution textual/apparatus proofing remains 0/254, and independent human approval remains pending.




## High-resolution BookReader inspection — printed pp.75–84 — 25 November 2026

All ten 1360×2274 BookReader JPEGs (leaves n96–n105) were individually opened at full image resolution. Printed folios 75–84 and broad page layouts are visible. The alternate files named `printed_p075_full.png` through `printed_p084_full.png` in the newly added native-scan directory rendered almost entirely black in the image viewer and were not used as proofing evidence; the BookReader JPEGs were legible and were used instead.

| Printed page | Leaf | Visual result | OCR/text-layer discrepancy or observation |
|---:|---:|---|---|
| 75 | n96 | Folio 75, Chapter X.10–14, English/Greek parallel and two tiers of notes visible. | OCR Greek column is heavily corrupted and interleaves fragments; English begins mid-sentence as expected. Apparatus note at v.14 discusses Syn. Greek versus Ethiopic singular/plural wording. No English body-text change authorized. |
| 76 | n97 | Folio 76; vv.15–20 and lower critical notes visible. | OCR column order is disrupted: “evermore” is displaced after v.20 in extraction although it completes v.16. The page image confirms the reading sequence. |
| 77 | n98 | Folio 77; end of ch. X, ch. XI, and opening of ch. XII visible; apparatus below. | OCR fails to recognize the circled verse number 4 at XII.4 and emits a garbled token before “Enoch”; the printed verse number is visibly 4. The heading reads “Chapters X.15—XII.4.” |
| 78 | n99 | Folio 78; XII.5–6, XIII.1–7, Ethiopic/Greek apparatus and notes visible. | OCR omits or corrupts the circled verse numbers 5 and 6 at XII.5–6; body wording and apparatus are present but mixed in extraction order. |
| 79 | n100 | Folio 79; end of XIII and XIV.1–4; critical notes visible. | OCR heading corrupts XII in “Chapters XII.5—XIV.4”; the printed heading is XII.5—XIV.4. Greek/Ethiopic apparatus is poorly recognized. |
| 80 | n101 | Folio 80; XIV.4–10 and two apparatus blocks visible. | OCR reads “IT have written” where the image reads “I have written”; Greek apparatus is transliterated/corrupted. Column/footnote order is partially interleaved. |
| 81 | n102 | Folio 81; XIV.5–21 and critical notes visible. | OCR broadly preserves the English body, but Greek/Ethiopic forms and some apparatus abbreviations are corrupted. The printed reading “gat hold upon me” is visible and should not be modernized as an OCR correction. |
| 82 | n103 | Folio 82; XIV.21–25 and XV.1–3; apparatus visible. | OCR reads “42.” for printed verse 22 and drops the initial “W” in “Wherefore” at XV.3 (extracted as “herefore”). A circled marginal/reader mark surrounds the printed verse number 3; it is not part of the text. |
| 83 | n104 | Folio 83; XV.4–9, Greek parallel and critical apparatus visible. | OCR reads “Ou” for “Whilst” at XV.4 and has severe Greek text corruption. The English body and lower notes are interleaved in extraction. |
| 84 | n105 | Folio 84; XV.9–11, Greek parallel and critical note visible. | Greek OCR is extensively corrupted; v.11’s English and the Synoptic Greek apparatus are visibly present. The opening “wrong.” in the extracted note is a continuation from p.83, not body text on p.84. |

### Scope and limits

This is an individual high-resolution page/layout inspection plus a targeted comparison of conspicuous OCR defects, not a complete line-by-line diplomatic collation of every word, Greek reading, or apparatus siglum. No wording has been silently amended in the edition. The ten pages can now be counted as individually image-opened at high resolution; the complete textual/apparatus proofing requirement and independent human review remain outstanding. The native PNG rendering issue should be investigated separately before those PNGs are used for any further visual work.


## Reconciled high-resolution inspection and diplomatic collation — 25 November 2026

This entry supersedes the earlier pp.75–84 evidence-boundary statement that said no page pixels had been opened. In this session, all ten committed JPEGs p075_n096 through p084_n105 were fetched from the repository and opened individually at original resolution. The page-specific image/OCR/edition collation is recorded in `artifacts/1-enoch-1893/reports/collations/pp75-84-high-resolution-diplomatic-collation.md`.

The earlier pp.75–84 table remains useful as a page-layout and OCR-observation record, but it is not the complete collation. The new report adds:
- Directly observed page headings, printed verse numbers, Greek parallel columns, and apparatus blocks.
- OCR reading-order and recognition defects, including the X.16 “evermore” displacement, the XII.4–6 and XV.3–4 circled verse numerals, XIV.22 misread as 42, and XV.4 “Whilst”.
- A list of substantive differences between the 1893 printed English and the current formatted chapters XIV–XV, including XV.4 “defiled” versus “denied”, omitted “(children)”, XV.3 omitted “(as your)”, and XV.9 omitted “(and)”.
- A clear distinction between OCR defects and changes in the formatted edition. No edition text has been changed.

The circles around XII.4, XII.5–6, XV.3, and XV.4 are handwritten reader marks around printed verse numerals. They are not printed brackets or part of the textual sequence.

### Corrected cumulative ledger

- Printed pp.63–74: 12 pages individually opened at medium 340×569 resolution; page/layout checks only.
- Printed pp.75–84: 10 pages individually opened at original 1360×2274 resolution; targeted image/OCR/edition collation recorded.
- **Cumulative individually opened: 22/254 pages (pp.63–84).**
- Complete line-by-line Greek/Ethiopic apparatus collation: not complete.
- Complete diplomatic proofing across pp.55–308: not complete.
- Independent human approval: pending.

This count is an image-opening count, not a claim that 22 pages have received complete diplomatic proofing. The earlier 12/254 progress statement is superseded by this reconciled 22/254 count.

### Next batch — pp.85–94

Expected mapping is BookReader leaves n106–n115 and one-based PDF pages 107–116. Repository search found no pp.85–94 large-image manifest, page-image batch, or consolidated OCR extraction. Attempts to access the Internet Archive image endpoint from the current execution environment did not yield image bytes. Therefore pp.85–94 remain **not retrieved and not inspected**; no retrieval or proofing count is advanced for them. The next operation is to obtain the ten high-resolution images and matching page text layer, verify the printed folios, then create the manifest and OCR inventory before individual collation.


## Corrected pp.85–94 repository source audit — 25 November 2026

This entry supersedes the preceding statement that no corresponding pp.85–94 source assets existed. A recursive repository check found nine page-specific native PNG blobs and nine OCR text files under `artifacts/page-images/cornell-native/cornell_printed_pp75_308/` for printed pp.85–90 and 92–94. Printed p.91 has neither a p.091-named image nor OCR file in that directory. The separate `cornell_all_pages/page_0113_full.png` file maps to PDF page 113 / printed p.91; it exists but is extremely dark and unreadable.

The nine PNGs were fetched from GitHub and opened in the image viewer. They render as very dark/unreadable images and cannot serve as proofing evidence. The similarly named `cornell_pages_85_106/` directory contains PDF ordinals 85–106 (printed pp.63–84), not the target pages. No BookReader JPEGs `p085_n106.jpg` through `p094_n115.jpg` exist in the expected repository directory, and direct Internet Archive retrieval did not return usable image bytes.

Ten page images were located across the two Cornell-native directories (nine named by printed page plus the ordinal p.91 image); all ten render dark/unreadable. Nine Cornell OCR text files exist, for pp.85–90 and 92–94. A separate searchable 1893 Knox College/Toronto scan supplied a provisional p.91 text extraction, explicitly treated as a parallel witness rather than Cornell OCR.

The OCR-only comparison and provisional discrepancy ledger are recorded in `artifacts/1-enoch-1893/reports/collations/pp85-94-ocr-only-discrepancy-ledger.md`.

Detailed paths, blob SHAs, sizes, and per-page statuses are recorded in:
- `artifacts/1-enoch-1893/manifests/cornell-printed-pages-85-94-source-audit.json`
- `artifacts/1-enoch-1893/reports/collations/pp85-94-source-retrieval-audit.md`

**Corrected status:** Cornell OCR/text files present 9/10, with p.91 text provisionally supplied by a separate scan; native PNG blobs located 10/10 but unusable; valid high-resolution page images acquired 0/10; individual image inspection 0/10; OCR-only comparison recorded, but full diplomatic collation 0/10. The pp.85–94 image-retrieval blocker remains open. No transcription change or proofing-count increase is authorized. Independent human approval remains pending.


## Formatted-content pilot Chapters I–V — 26 November 2026

The new formatted-content pilot is documented at `formatted_stories/1-enoch-charles-1893/`. The related 1893 searchable-text-layer comparison for pp.57–62 is consolidated in `1893-witness-collation.md` within that directory. This is not a new page-image inspection and does not change the ledger: page/layout inspection remains 41/254; full line-by-line diplomatic proofing remains 0/254. Independent human approval remains pending. A second reviewer must complete the separate [review packet](../../../formatted_stories/1-enoch-charles-1893/INDEPENDENT_REVIEW_PACKET.md); assistant-led work cannot satisfy this gate.


## Individual high-resolution BookReader inspection — printed pp.85–94 — 26 November 2026

All ten Cornell / Internet Archive BookReader JPEGs were fetched from the current repository branch and opened individually at full image resolution (1360×2274). The exact files are under `artifacts/page-images/cornell-native/bookreader-large/`, named `p085_n106.jpg` through `p094_n115.jpg`. Their Git blob SHAs are recorded in the updated source-audit JSON. The images are legible. The previously documented dark native PNG exports remain unusable and were not used; the committed BookReader JPEGs are the inspected witness images.

These are page-identity and layout inspections only. I checked folio, running header, visible chapter/verse coverage, column arrangement, and the presence/location of critical apparatus. I did not collate every word, punctuation mark, Greek reading, Ethiopic siglum, or apparatus entry against the derivative transcription. Therefore these ten pages increase the page/layout count by ten, but do not increase the full diplomatic-proofing count.

| Printed page | BookReader leaf | PDF page (1-based) | Individual visual observation |
|---:|---:|---:|---|
| 85 | n106 | 107 | Folio 85 and running head “Chapters XV.10 — XVI.1.” visible. English text and Greek parallel occupy separate columns; critical apparatus fills the lower portion. |
| 86 | n107 | 108 | Folio 86 visible. Greek fragment described in the printed introduction as absent from the Ethiopic version occupies the upper portion; English translation and critical notes follow. |
| 87 | n108 | 109 | Folio 87 and running head “Chapters XVI.2 — XVII.4.” visible. English narrative continues above a substantial critical/exegetical apparatus. |
| 88 | n109 | 110 | Folio 88 visible. Chapters XVII–XVIII continue in the English text; critical notes and Greek references are clearly separated below. |
| 89 | n110 | 111 | Folio 89 and running head “Chapters XVII.5 — XVIII.12.” visible. English narrative and lower apparatus are legible; no gross crop or page-identity defect observed. |
| 90 | n111 | 112 | Folio 90 visible. Chapter XVIII concludes and XIX begins; apparatus/commentary occupies the lower half. |
| 91 | n112 | 113 | Folio 91 and running head “Chapters XVIII.13 — XX.4.” visible. The page contains the continuation of XIX, XX.1–4, and critical notes. Cornell page pixels are now available despite the missing Cornell OCR text file. |
| 92 | n113 | 114 | Folio 92 visible. The angel list continues, including the printed reading “the serpents and the Cherubin”; XXI begins below. Lower apparatus is legible. |
| 93 | n114 | 115 | Folio 93 and running head “Chapters XX.5 — XXII.1.” visible. XXI.5–10 and XXII.1 appear above the apparatus. The printed question at XXI.5 reads “Wherefore dost thou ask, and why dost thou enquire and art curious?” |
| 94 | n115 | 116 | Folio 94 visible. XXII.1–5 continues; English text and critical notes are present. No gross crop or page-identity defect observed. |

### Observations requiring separate diplomatic collation

- **p.92, XX.7:** The Cornell image visibly reads “Gabriel ... who is over Paradise and the serpents and the Cherubin.” The repository derivative's “seraphim and the cherubim” is not a faithful rendering of this printed wording. Preserve the source reading in the discrepancy ledger; do not silently alter the derivative until its editorial policy and intended witness are resolved.
- **p.92, XX.6:** The printed angel name appears as “Saraqâêl” (typographic diacritics to be transcribed diplomatically); the OCR/transliteration form should remain flagged.
- **p.93, XXI.5:** The image confirms the older printed wording “Wherefore dost thou ask, and why dost thou enquire and art curious?” The derivative's modernized phrasing is a deliberate wording difference, not a simple OCR defect.
- **p.91:** The page image supplies direct Cornell visual evidence for the passage previously recovered only from a parallel scan. It does not create a missing Cornell OCR text layer, nor does it establish a full line-by-line collation.

**Proofing boundary:** 10/10 pages individually opened and checked for page identity/layout. Full line-by-line diplomatic textual/apparatus proofing for these pages remains 0/10. Independent human approval remains pending.


## pp.85–94 facsimile collation review — 2026-11-26

- [x] Opened all ten committed high-resolution BookReader JPEGs individually and recorded image-anchored page observations.
- [x] Confirmed the p.92 body reading “Paradise and the serpents and the Cherubin”; Charles's “may be Seraphim” statement is an apparatus hypothesis, not a body-text replacement.
- [x] Confirmed the printed interpolation bracket opens at XVII.1 (p.87) and closes after XIX.3 (p.91).
- [x] Confirmed p.86's Greek fragment is explicitly outside the Ethiopic version and p.91's Cornell JPEG is readable despite missing Cornell OCR.
- [ ] Complete word-for-word English comparison and transcribe all Greek, Ethiopic, sigla, punctuation, and apparatus for pp.85–94.
- [ ] Resolve all flagged differences in a separate editorial review queue; do not silently edit the derivative.

Detailed record: `artifacts/1-enoch-1893/reports/collations/pp85-94-facsimile-collation-review.md`.

**Ledger remains:** 41/254 page/layout inspections; 0/254 completed full line-by-line diplomatic proofing; independent human approval pending. The ten image-anchored observations do not change the full-proofing count.


## pp.95–104 visual inspection — in progress (2026-11-26)

- [x] Printed p.95 (BookReader leaf n116; 1360×2274 JPEG) opened individually; folio, heading, Chapter XXII.6–12 coverage, body layout, and lower apparatus placement inspected.
- [ ] Individually open pp.96–104 and record page-specific layout observations.
- [ ] Perform full line-by-line diplomatic comparison for pp.95–104 after visual inspection.

The ten JPEGs for pp.95–104 are already committed and recorded in `artifacts/1-enoch-1893/manifests/bookreader-pages-95-104-large.json`. An OCR/alignment pilot exists at `artifacts/1-enoch-1893/reports/diplomatic_proofing/pilot_pp95-104_detailed.md`; its automated matches are leads, not proof. Current total: 41/254 page/layout inspections; 0/254 complete line-by-line diplomatic proofing; independent human approval pending.


## pp.96–104 page/layout inspection — complete (2026-11-26)

- [x] Opened and inspected pp.96–104 individually from committed 1360×2274 JPEGs (leaves n117–n125).
- [x] Recorded page headers, chapter/verse coverage, body/apparatus layout, and collation targets.
- [x] Corrected the OCR pilot's unsupported p.104 west/south “variant”: Cornell prints XXXV as the westward journey and XXXVI.1 as the southward journey, i.e. consecutive distinct chapters, not a single direction variant.
- [ ] Complete line-by-line collation for pp.95–104, including English, Greek, Ethiopic, punctuation, sigla, and apparatus.

Detailed record: `artifacts/1-enoch-1893/reports/collations/pp96-104-page-layout-inspection.md`.

**Ledger:** 50/254 page/layout inspections (pp.55–104); 0/254 full diplomatic proofing; independent human approval pending. The nine newly opened pages do not count as line-by-line proofed.
