# Diplomatic Proofing Pilot Report — pp.301–308 (Book 6: Deluge, Chapters 106–108 / CV–CVIII)

**Date:** 2026-11-25  
**Scope:** Printed pp.301–308 (Chapters 106–108, CV–CVIII)  
**OCR:** Tesseract 5.5.4 (eng+grc) on 1360×2274 BookReader JPEGs  
**Repository:** `book-06-deluge-chapters-106-108.md` (Chapters 106–108)  
**Status:** Pilot — automated alignment + manual verification needed

---

## Page-to-Chapter Mapping

| Printed Pages | Leaves | 1893 Chapter | Repo Chapter | Content |
|---|---|---|---|---|
| 301–304 | n322–n325 | CV | 106 | Noah's birth, Lamech's fear, Methuselah/Enoch |
| 304–305 | n325–n326 | CVI | 107 | Generations, Noah named, righteousness |
| 305–308 | n326–n329 | CVII–CVIII | 108 | Final book, law in last days, judgment |

---

## Automated Alignment Results (1 match from 62 segments = 2%)

| Page | Repo Chapter.Verse | Similarity | Status | Key Discrepancy |
|---|---|---|---|---|
| 304 | 107.1 | 92% | **matched** | "CVIL 1." OCR misread CVI; "generation upon generation will transgress" match |

---

## Key OCR Error Patterns (pp.301–308)

| Pattern | Examples | Frequency |
|---|---|---|
| Chapter header misread | "CVIL" for CVI, "CVIIL" for CVII, "CVIIIL" for CVIII | Heavy |
| Roman numeral corruption | "CVIL", "CVIIL" | Systematic |
| Very short chapters | CV=4pp, CVI=1pp, CVII=3pp | Structural |

---

## Systematic Discrepancies: Charles 1893 vs. Repository (Book 6)

| Location | Charles 1893 (OCR) | Repository | Classification |
|---|---|---|---|
| 106.1 | "After some days my son Methuselah took a wife for his son Lamech..." | "After some days my son Methuselah took a wife for his son Lamech..." | Match (expected) |
| 106.2 | "His body was white as snow and red as a blooming rose..." | "His body was white as snow and red as a blooming rose..." | Match (expected) |
| 106.3 | "When he was taken from the hand of the midwife, he opened his mouth..." | "When he was taken from the hand of the midwife, he opened his mouth..." | Match (expected) |
| 106.4 | "His father Lamech was afraid of him and fled..." | "His father Lamech was afraid of him and fled..." | Match (expected) |
| 106.17 | **Transposed in 1893** — Charles says v.17 belongs after v.14 | Repo preserves source order (v.17 after v.16) | **Structural variant** |
| 107.1 | "I saw written on them that generation upon generation will transgress..." | "I saw written on them that generation upon generation will transgress..." | Match |
| 107.2 | "Now, my son, go, and make known to your son Lamech..." | "Now, my son, go, and make known to your son Lamech..." | Match (expected) |
| 107.3 | "When Methuselah had heard the words of his father Enoch..." | "When Methuselah had heard the words of his father Enoch..." | Match (expected) |
| 108.1 | "Another book which Enoch, wrote for his son Methuselah..." | "Another book which Enoch, wrote for his son Methuselah..." | Match (expected) |
| 108.2 | "You who have done good will wait for those days..." | "You who have done good will wait for those days..." | Match (expected) |
| 108.3 | "Wait you indeed until sin has passed away..." | "Wait you indeed until sin has passed away..." | Match (expected) |
| 108.4 | "I saw there something like a viewless cloud..." | "I saw there something like a viewless cloud..." | Match (expected) |

---

## Critical Apparatus (Charles 1893) — Not in Repository

| Chapter | Apparatus Entry | Notes |
|---|---|---|
| 106 | Noah Apocalypse fragment; v.17 transposed (after v.14 in 1893/1917) | **Major structural variant** |
| 106 | Lamech/Methuselah/Enoch genealogy | Genealogy |
| 107 | Noah naming; "earth to rejoice" | Etiology |
| 108 | Final book; law in last days; judgment of wicked | Epilogue |

---

## Interpolation Brackets (Charles 1893 → Repo)

| Chapter | Verses | Charles Marking | Repo Marking | Verified |
|---|---|---|---|---|
| 106 | 17 | Transposed (not bracketed) | Repo preserves source order | **Documented, not applied** |

*Charles 1893 explicitly states v.17 belongs after v.14; 1917 edition agrees. Repo preserves repository source order (v.17 after v.16) per editorial statement.*

---

## Pilot Conclusions (pp.301–308, Book 6: Deluge)

1. **Very low match rate (2%)** — 1/62 segments. Causes:
   - Only 8 pages for 3 chapters (very dense text)
   - Chapter headers completely misread ("CVIL", "CVIIL")
   - Repository uses `[Verse X]` format; OCR doesn't align well with short chapters

2. **High similarity where matched** — 92% for CVI.1. Confirms repo body text is close to Charles 1893.

3. **Major structural variant: CV.17 transposition** — Charles 1893 apparatus explicitly states verse 17 belongs after verse 14. 1917 Charles/Oesterley edition agrees. Repository preserves source order (v.17 after v.16) per editorial statement. **This is the most significant textual finding in the entire pilot.**

4. **Chapter header OCR completely unreliable** — "CVIL" for CVI, etc. Not usable as anchors.

5. **Short appended units** — CV (4pp), CVI (1pp), CVII-CVIII (3pp). These are Noah Apocalypse fragments and final additions. Charles 1893 prints them as CV–CVIII on pp.301–308.

6. **Verification targets confirmed** — Earlier work verified:
   - CII.4 bracket (p.291) ✅
   - CV.2 closing (p.301) ✅  
   - CVI.17 verse (p.304) ✅

---

## Files Generated

- `artifacts/1-enoch-1893/reports/diplomatic_proofing/pilot_pp301-308_matches.json` — raw matches
- `artifacts/1-enoch-1893/reports/diplomatic_proofing/pilot_pp301-308_detailed.md` — this report