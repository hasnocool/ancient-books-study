# Proofing Dataset Integrity Audit and Remediation

**Date:** 2026-11-26  
**Scope:** `artifacts/1-enoch-1893/reports/diplomatic_proofing_full/` and repository progress metadata.

## Corrections applied

1. Reclassified all 18 rows in `verification_queue.csv` from `Verified=Y, Reviewer=AUTO-SIMULATED` to `Verified=N, Reviewer=HUMAN_REVIEW_PENDING`. These rows are automated fuzzy-match candidates only. No human approval is implied.
2. Added explicit integrity metadata to `proofing_full_combined.json`: `audit_status=INCOMPLETE_UNVALIDATED`, missing pages, overlapping pages, zero human-verified discrepancies, and the queue reclassification status.
3. Reconciled the page/layout inspection count in `AGENTS.md` to the authoritative image-proofing log: 30/254, not 12/254.

## Coverage audit

The combined JSON declares 254 pages and 16 sections. Its section ranges do **not** provide complete, non-overlapping coverage of printed pp.55–308.

- Missing from all section ranges: **pp.260–264**.
- Counted in two section ranges: **pp.301–308** (the broad pp.285–308 range and a separate pp.301–308 range).
- Therefore, the ranges represent 249 distinct covered pages, not 254 distinct pages.

 the union of the listed ranges covers pp.55–259 (205 pages) and pp.265–308 (44 pages), for **249 distinct pages**; the eight pp.301–308 duplicates are repeated section membership, not additional distinct pages. Five pages are missing. The 16 section records contain 257 page memberships in total.

The combined dataset currently reports zero discrepancies in every section, while the separate 18-row verification queue contains automated fuzzy-match candidates. These are not necessarily all true textual discrepancies, but the outputs are inconsistent and must not be combined into a claim of zero discrepancy. The metadata field `total_verses=130` has no documented counting definition and is not accepted as proof of verse-level completeness.

## What this dataset is—and is not

The combined JSON is an OCR-derived section/apparatus extraction artifact. It is **not** a complete diplomatic collation, page-image proof, or independently reviewed edition. Its apparatus entries include OCR-corrupted and incomplete material and require a separate quality-control pass. No new OCR or apparatus generation was performed in this remediation.

## Remaining remediation

- Rebuild the section manifest with exact page membership, filling pp.260–264 and removing the duplicate pp.301–308 section or explicitly marking it as a subrange that is excluded from aggregate counts.
- Reconcile the zero-discrepancy section summaries with the 18 automated candidate records; preserve candidate evidence and avoid treating fuzzy similarity as a confirmed variant.
- Define and recompute all aggregate counts (pages, chapters, verses, apparatus entries, candidate discrepancies) from validated records rather than undocumented metadata.
- Have a human reviewer inspect and disposition each candidate. Keep reviewer identity and approval date in separate fields.
- Run schema and coverage tests in CI and record actual test results.
- Continue facsimile proofing independently; OCR and metadata checks do not increment image-proofing counts.

## Verification boundary

This remediation changed status labels and audit metadata only. It did not alter archival source texts, translation wording, apparatus readings, or image-proofing counts. No local test suite or page-image inspection was run as part of this remote GitHub correction.
