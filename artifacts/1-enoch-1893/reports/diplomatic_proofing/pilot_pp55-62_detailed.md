# Diplomatic Proofing Pilot Report — pp.55–62

**Date:** 2026-11-25  
**Scope:** Printed pp.55–62 (Introduction + Chapter I.1–VI.4)  
**OCR:** Tesseract 5.5.4 (eng+grc) on 1360×2274 BookReader JPEGs  
**Repository:** `book-01-watchers-chapters-01-36.md` (Chapters 1–36, verse-restored)  
**Status:** Pilot — automated alignment + manual verification needed

---

## Page-to-Chapter Mapping

| Printed Page | Leaf | Content (per OCR + visual) | Repository Chapters |
|---|---|---|---|
| 55 | n76 | Introduction: Section I title, Critical Structure (A), Relation (B), Date (C), Problem/Solution (D) | — (front matter) |
| 56 | n77 | Introduction continued: Relation to LXXII–LXXXII, LXXXIII–XC, XCI–CIV; Date; Problem/Solution | — (front matter) |
| 57 | n78 | **Chapter I.1–3** + apparatus on I.1–2 (elect/righteous, Holy One, God/Lord) | Chapter 1, v.1–3 |
| 58 | n79 | **Chapter I.4–11** + apparatus on I.3–8 (parable, Holy/Great One, Sinai, Watchers, judgment) | Chapter 1, v.4–9 |
| 59 | n80 | **Chapter I.9–II.3** + apparatus on I.9 (Jude 15), II.1–3 (luminaries, seasons) | Chapter 1 v.9, Chapter 2 v.1–3 |
| 60 | n81 | **Chapter III–V.4** + apparatus on III (14 trees), V.4–5 (law, execration, peace) | Chapter 3–4, Chapter 5 v.1–4 |
| 61 | n82 | **Chapter V.5–VI** + apparatus on V.5–9, VI–XI intro (Semjaza cycle, Noah Apocalypse) | Chapter 5 v.5–9, Chapter 6 intro |
| 62 | n83 | **Chapter VI.1–4** + Syncellus Greek fragments + apparatus on VI.2–3 | Chapter 6 v.1–4 |

---

## Automated Alignment Results (8 matches)

| Page | Repo Chapter.Verse | Similarity | Status | Key Discrepancy |
|---|---|---|---|---|
| 57 | 1.1 | 89% | matched | OCR: "Q 1." vs Repo: "1."; "the elect and righ..." vs "the elect and rig..." |
| 58 | 1.3 | 77% | partial | OCR: "the glect I spake" vs Repo: "Concerning the elect I spoke" |
| 59 | 1.8 | 64% | partial | OCR starts mid-verse; apparatus interleaved |
| 59 | 2.1 | 88% | matched | OCR: "T observed" vs Repo: "I observed"; punctuation differences |
| 60 | 3.1 | 83% | matched | OCR: "themselvese" vs Repo: "themselves"; "agamst" vs "against" |
| 60 | 5.1 | 91% | matched | OCR: "cover themselvese" vs Repo: "cover themselves" |
| 61 | 5.6 | 75% | partial | OCR: "tiplied" (truncated); "ye" vs "you" |
| 62 | 6.1 | 77% | partial | OCR line breaks differ; "Semjizd" vs "Semjaza" |

---

## Systematic Discrepancy Categories (Pilot)

### 1. OCR Errors (to be corrected from page image)
| Type | Examples | Action |
|---|---|---|
| Ligature misread | "interpolatioﬁ" → "interpolation" | Fix from image |
| Greek corruption | "BG #%0", "LHMAG", "TwmT" | Flag — requires Greek specialist |
| Word fusion | "donot", "themselvese", "agamst" | Fix from image |
| Truncation | "tiplied" for "multiplied" | Fix from image |
| Name corruption | "Semjizd" for "Semjaza" | Fix from image |

### 2. Repository vs. Charles 1893 Wording (intentional, not errors)
| Location | Charles 1893 (OCR) | Repository | Classification |
|---|---|---|---|
| Ch1.1 | "These are the words of the blessing of Enoch..." | "These are the words of blessing of Enoch..." | Lexical variant (article) |
| Ch1.2 | "Enoch answered and spake—(Enoch) a righteous..." | "Enoch answered and spoke: I, Enoch, a righteous..." | Structural (dash/colon, pronoun) |
| Ch1.3 | "the Holy, and Great One" | "the Holy, and Great One" | Match |
| Ch1.4 | "Going from thence He will tread..." | "Going from thence He will tread..." | Match |
| Ch1.9 | "will convict all flesh" | "will convict all flesh" | Match |
| Ch2.1 | "how the luminaries which are in the heaven do not deviate..." | "how the luminaries, which are in the heaven, do not deviate..." | Punctuation |
| Ch5.4 | "O ye hard hearted ye will find no peace" | "O you hard hearted: you will find no peace!" | Spelling/punctuation |
| Ch5.5 | "be bereft of the years of your life" | "be deprived of the years of your life" | Lexical variant |
| Ch6.2 | "sons of the heavens" | "sons of the heavens" | Match |
| Ch6.3 | "Semjaza" | "Semjaza" | Match (OCR had "Semjizd") |

### 3. Critical Apparatus (present in Charles, absent/minimal in repository)
| Page | Apparatus Element | Repository Status |
|---|---|---|
| 57 | I.1: "elect and righteous" — refs to xxxvii.2, xxxix.6, xlviii.1, lviii.1, lxi.13, lxii.12, lxx.3 | Not in repo |
| 57 | I.2: "God" rendering — 2ZH.AAMC = "God", &7H.& = "Lord" | Not in repo |
| 57 | I.2: "Vision of the Holy One" — Yo BG #%0, Giz. Gk. | Not in repo |
| 58 | I.3: "Uttered a parable" — G omitting H, Giz. Gk. ἀναβάσεως | Not in repo |
| 58 | I.4: "Holy and Great One" — refs to x.1, xiv.1, xxv.3, lxxxiv.1, xcii.2 | Not in repo |
| 58 | I.5: "Watchers" — refs to x.9,15; xii.2,4; xiii.10; xiv.1,3; xv.2; xvi.1,2; xci.15 | Not in repo |
| 59 | I.9: "convict all flesh" — LHMAG, Jude 15, Giz. Gk. | Not in repo |
| 60 | V.4: "law of the Lord" — refs to xcix.2, xci.5, xciv.9, xcvi.7, xcviii.9 | Not in repo |
| 61 | V.5: "execration" — Isaiah lxv.15, Giz. Gk. | Not in repo |
| 62 | VI.2: "Sons of the heavens" — refs to xii.8, xiv.3, xxxix.1, xv.1-7, lxxi.1 | Not in repo |
| 62 | VI.3: "penalty of a great sin" — G M, Giz. Gk., Syn. Gk. | Not in repo |

### 4. Interpolation Brackets (Charles 1893 marks these; repo has them)
| Chapter | Verses | Charles Marking | Repo Marking |
|---|---|---|---|
| VI | 3–8 | Bracketed as interpolation (Semjaza cycle) | **[Bracketed in repo]** |
| VIII | 1–3 | Bracketed | **[Bracketed in repo]** |
| IX | 7 | Bracketed | **[Bracketed in repo]** |
| X | 1–3 | Bracketed (Noah Apocalypse) | **[Bracketed in repo]** |
| XVII–XIX | all | Bracketed (geography) | **[Bracketed in repo]** |

---

## Pilot Conclusions

1. **Alignment works** — 8/52 OCR segments matched to repository verses (15% hit rate). Low because:
   - OCR mixes body text + apparatus + footnotes
   - Repository lacks apparatus entirely
   - Pages 55–56 are front matter (no repo counterpart)

2. **Repository is not verbatim Charles 1893** — Confirmed: wording differs systematically (modernized spelling, punctuation, pronoun changes). This is *expected* per repo editorial statement.

3. **Apparatus gap** — Charles 1893 has extensive critical apparatus (Greek variants, manuscript sigla, cross-refs); repository has none. This is the major collation task.

4. **Next step** — Build apparatus-aware alignment that:
   - Separates body text from apparatus in OCR
   - Maps Charles verse numbers to repo verse numbers (they align for Ch1–6)
   - Flags each apparatus entry for human verification against page image

---

## Recommended Proofing Workflow per Chapter

```python
# For each chapter:
1. Extract OCR body text (filter out apparatus/footnotes via layout detection)
2. Align to repo verses using verse numbers as anchors
3. Diff body text: classify each difference
4. Extract apparatus entries from OCR (pattern: sigla + lemma + witnesses)
5. Verify each apparatus entry against page image
6. Check interpolation brackets: position, content, nesting
7. Output: Markdown table + JSON ledger
```

---

## Files Generated

- `tools/diplomatic_proofing_pilot.py` — alignment script
- `artifacts/1-enoch-1893/reports/diplomatic_proofing/pilot_pp55-62_matches.json` — raw matches
- `artifacts/1-enoch-1893/reports/diplomatic_proofing/pilot_pp55-62_detailed.md` — this report