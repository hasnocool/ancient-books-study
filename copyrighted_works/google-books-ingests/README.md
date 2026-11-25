# Google Books Ingests & Provider-Digitized Works

## Copyright Status: **VARIABLE — Provider Terms Apply / Underlying Work Status Determines Rights**

## Overview

These files are digital copies scanned/digitized by Google Books, Internet Archive, Arya Samaj Foundation/eGangotri, or similar providers. The **underlying works** may be public domain, but the **specific digital files** are subject to provider terms of service.

## Inventory

| File | Provider | Underlying Work | Likely PD Status | Notes |
|------|----------|-----------------|------------------|-------|
| `books_02/Acta Latomorum...1815.txt` (≡ `books_05/...`) | Google Book Search | *Acta Latomorum*, Vol II (1815) | **Likely PD** (1815 publication) | French text; Google scan notice present |
| `books_03/heronisalexandr02schogoog.txt` | Google | Hero of Alexandria works | **Likely PD** (ancient) | German/Latin; Google scan notice |
| `books_03/heronsvonalexandhero.txt` | Internet Archive | Hero of Alexandria | **Likely PD** | IA digitization |
| `books_04/Loeb.001.ApolloniusRhodius.Argonautica.txt` | Google | Apollonius Rhodius, *Argonautica* (Loeb) | **Loeb translation copyrighted** | Loeb Classical Library translations still under copyright |
| `books_05/Yukti Kalpataru...txt` | Arya Samaj / eGangotri | *Yukti Kalpataru* (1995 ed.) | **Uncertain** (1995 publication) | Modern edition; may be copyrighted |

## Provider Terms Summary

### Google Books / Google Book Search
- **Notice**: "Google Book Search helps readers discover the world's books... digitized by Google as part of a project..."
- **Terms**: Personal/non-commercial use only; no automated querying; watermark attribution required
- **Digital copy**: Google's scan/OCR layer is proprietary; underlying PD work can be re-sourced
- **URL reference**: `http://books.google.com/`

### Internet Archive
- **Notice**: "Digitized by the Internet Archive"
- **Terms**: Generally "for research and private study"; more permissive than Google
- **Digital copy**: IA's scan/OCR; underlying PD work can be re-sourced from IA or other

### Arya Samaj Foundation / eGangotri
- **Notice**: "Digitized by Arya Samaj Foundation Chennai and eGangotri"
- **Terms**: Indic digital library; typically non-commercial research use
- **Digital copy**: Their scan/OCR; underlying work status varies

## Rights Analysis per File

### 1. Acta Latomorum Vol II (1815) — Google Scan
- **Underlying work**: 1815 French publication → **Public Domain** (author dead >70 years, published >95 years ago)
- **Google scan**: Proprietary OCR/scan layer
- **Action**: Text content is PD; re-extract from clean source (HathiTrust, IA, Gallica) for formatted editions

### 2. Hero of Alexandria (Heron) — Google Scan
- **Underlying work**: Ancient Greek (1st century CE) → **Public Domain**
- **Translation**: If Loeb or modern scholarly translation → **Copyrighted**
- **File `heronisalexandr02schogoog.txt`**: Appears to be German/Latin edition — check if translation is PD
- **File `heronsvonalexandhero.txt`**: IA scan — check translation status
- **Action**: Source public-domain translations (e.g., 19th century scholarly editions)

### 3. Apollonius Rhodius, Argonautica (Loeb) — Google Scan
- **Underlying work**: Ancient Greek (3rd century BCE) → **Public Domain**
- **Loeb translation**: **Copyrighted** (Loeb Classical Library translations are modern, still under copyright)
- **File**: `Loeb.001.ApolloniusRhodius.Argonautica.txt` — contains Loeb translation
- **Action**: **Do not use Loeb translation** for formatted editions. Use public-domain translations (e.g., Seaton 1912, Rieu 1959 — check status).

### 4. Yukti Kalpataru (1995 edition) — Arya Samaj / eGangotri
- **Underlying work**: *Yukti Kalpataru* (ancient Sanskrit text on architecture/shipbuilding) → **Public Domain**
- **1995 edition**: Modern critical edition by Shakir Ali, published by Preeti Prakashan (Bhojpur) → **Likely Copyrighted**
- **File**: `Yukti Kalpataru by Shakir Ali 1995 Bhojpur - Preeti Prakashan.txt`
- **Action**: Source the ancient Sanskrit text + public-domain translation (if exists); do not use 1995 critical edition

## General Policy for Provider-Digitized Works

| Scenario | Formatted Edition Allowed? | Action |
|----------|---------------------------|--------|
| Underlying work PD, provider scan only | ✅ Yes (re-source text) | Extract text from clean PD source (HathiTrust, IA, Gallica, etc.) |
| Underlying work PD, but translation copyrighted | ❌ No (for that translation) | Use PD translation (pre-1928 typically) |
| Underlying work copyrighted | ❌ No | Obtain permission or use different work |
| Provider terms prohibit redistribution | ⚠️ Case-by-case | Do not redistribute provider's digital file; re-source content |

## Recommended Clean Public-Domain Sources

| Work | Recommended PD Source |
|------|----------------------|
| Acta Latomorum (1815) | Gallica (BnF), HathiTrust, Google Books (view-only, re-type) |
| Hero of Alexandria | Greek text: Thesaurus Linguae Graecae; Translations: 19th c. scholarly (Bennett, Woodcroft) |
| Apollonius Rhodius | Greek text: TLG; Translations: Seaton 1912 (Loeb predecessor), Rieu 1959 (check) |
| Yukti Kalpataru | Sanskrit text: Digital Sanskrit Buddhist Canon, GRETIL; Translation: check 19th c. Indology |

## Audit Trail

- **Identified**: 2026-11-25 (triple-agent review)
- **Method**: Provider notice detection (Google, IA, Arya Samaj/eGangotri)
- **Duplicate groups**: 
  - Group 19: Acta Latomorum (books_02/books_05)
  - Others: Single copies in books_03/books_04/books_05
- **Status**: Archived in `copyrighted_works/google-books-ingests/`; archival copies retained in original locations
- **Next step**: For each, verify underlying work PD status and source clean PD edition for formatted pipeline