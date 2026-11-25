# Full Diplomatic Proofing Framework — 1 Enoch (Charles 1893)

**Scope:** All 254 printed pages (pp.55–308) — Chapters I–CVIII + CV–CVIII
**Source:** Cornell/IA scan `cu31924014590545` (428 pages, 300 PPI)
**Repository edition:** `formatted_editions/books/book-of-enoch-charles-1893/` (Markdown chapters)
**OCR layers:** 
- High-res BookReader JPEGs (1360×2274) — pp.55–84, 75–308 (batch)
- Native Cornell PNGs (1360×2274) — all 428 pages (extracted from PDF JPXDecode)
- Tesseract OCR (eng+grc) — pp.55–62, 75–84 done
- PDF text layer — pp.75–84 consolidated

---

## Proofing Methodology (per IMAGE_PROOFING_LOG.md Rules)

### 1. Page-Level Verification
- [ ] Printed folio visible and correct
- [ ] Chapter/verse boundaries match edition
- [ ] Layout: English column, Greek parallel, critical apparatus tiers
- [ ] No gross scan defects (cropping, skew, darkness, missing lines)

### 2. Line-by-Line Textual Collation
For each verse/paragraph unit:
| Element | Check | Classification |
|---|---|---|
| English body text | Word-for-word vs. repository Markdown | Spelling/typography / OCR error / Lexical variant / Omission / Addition / Relocation / Unresolved |
| Greek parallel | Glyph-by-glyph where legible | Same classifications |
| Critical apparatus | Sigla, lemmas, witnesses, readings | Same classifications |
| Footnotes/endnotes | Content and placement | Same classifications |
| Interpolation brackets | Presence, position, content | Structural |
| Verse numbers | Circled/marginal vs. printed | Structural |

### 3. Evidence Recording
Each discrepancy recorded with:
- Printed page, leafNum, PDF page
- Repository chapter/verse/section
- Exact excerpt (printed) vs. exact excerpt (repository)
- Classification + confidence (high/medium/low)
- Decision: accept repository / accept printed / flag for human review

### 4. Completion Criteria per Chapter
- [ ] Every verse body checked
- [ ] Every apparatus entry checked
- [ ] Every interpolation bracket checked
- [ ] Every footnote checked
- [ ] Chapter marked `✅ Proofed` in ledger

---

## Pilot Section: pp.55–62 (Introduction + Chapter I.1–VI.4)

### Repository Files to Compare
- `formatted_editions/books/book-of-enoch-charles-1893/introduction.md` (if exists)
- `formatted_editions/books/book-of-enoch-charles-1893/chapter-01.md` through `chapter-06.md`

### OCR Source
- `artifacts/1-enoch-1893/ocr/pp55-62/` — 8 page OCR files
- `artifacts/1-enoch-1893/ocr/cornell-printed-pages-55-62.txt` — consolidated

### Visual Source
- `artifacts/page-images/cornell-native/bookreader-large/p055_n076.jpg` through `p062_n083.jpg`

---

## Automation Assistants

### 1. OCR → Text Alignment
```python
# Align OCR lines to repository verses using fuzzy matching
# Flag: verse boundaries, missing/extra lines, Greek column detection
```

### 2. Apparatus Extraction
```python
# Parse OCR for: [A], [B], (a), (b), G, M, S, Gr., Lat., Syr., Arm., Eth.
# Cross-reference with repository apparatus formatting
```

### 3. Interpolation Bracket Detection
```python
# Find: [ ], { }, 〈 〉, +...+, †...† in OCR and repository
# Verify position matches printed page
```

---

## Progress Ledger Template

| Pages | Chapter(s) | Status | Proofed by | Date | Notes |
|---|---|---|---|---|---|
| 55–56 | Introduction A–D | 🔄 In progress | | | |
| 57–58 | Chapter I.1–11 | ⏳ Pending | | | |
| 59–60 | Chapter II–V.4 | ⏳ Pending | | | |
| 61–62 | Chapter V.5–VI.4 | ⏳ Pending | | | |
| 63–74 | Chapter VI–X | ⏳ Pending | | | |
| 75–84 | Chapter X–XV | ⏳ Pending | | | |
| 85–94 | Chapter XV–XX | ⏳ Pending | | | |
| ... | ... | ... | | | |

---

## Quality Gates

1. **Automated pre-check:** OCR vs. repository diff → flag candidates
2. **Human verification:** Each flagged candidate reviewed against page image
3. **Second review:** Independent reviewer checks 10% sample
4. **Sign-off:** Chapter marked complete only after both reviews

---

## Tooling

- **OCR:** Tesseract 5.5.4 (eng+grc) — already run on pp.55–62, 75–84
- **Image viewing:** PIL/Pillow for programmatic crop/zoom
- **Diff:** `difflib.SequenceMatcher` for line alignment
- **Greek normalization:** `unicodedata` + custom sigla map
- **Output:** Markdown tables per chapter + JSON ledger

---

## Next Actions

1. [ ] Map repository chapter files to printed page ranges
2. [ ] Run pilot on pp.55–56 (Introduction) — smallest, well-defined scope
3. [ ] Build alignment script for verse-level comparison
4. [ ] Process Chapter I (pp.57–59) as first narrative chapter
5. [ ] Scale to full 254 pages in batches of ~20 pages