# High-Level Repository Review and Remediation Plan

**Review date:** 2026-11-26  
**Repository:** https://github.com/hasnocool/ancient-books-study  
**Reviewed ref:** `main`  
**Review type:** Remote repository-level review; not a local execution or complete content/legal audit.

## Executive assessment

The repository has evolved beyond a loose text archive into a substantial digital humanities research workspace. It contains five archival text batches, source PDFs, formatted editions, modernized editions, narrative and meaning derivatives, interpretive studies, OCR/page-image artifacts, audit tooling, tests, and project issues.

The strongest existing practice is its explicit separation of source text from derivatives and its unusually careful distinction between retrieval, page/layout inspection, diplomatic proofing, and independent human approval. Those distinctions should remain non-negotiable.

The principal weakness is operational consistency: documentation does not fully describe the current repository structure, the root agent guide contains machine-specific and stale path details, automated validation is too narrow, and repository-wide research state is spread across several reports/issues. The repository also has unresolved rights and archival-quality risks that prevent a blanket publication/reuse claim.

**Overall: promising research corpus with strong emerging editorial controls; not yet a fully reproducible, continuously validated, rights-cleared digital edition platform.**

## Findings and priorities

### P0 — Preserve evidence and prevent false verification

1. Keep source files immutable and keep all derivative classes distinct.
2. Maintain a single authoritative status ledger for each major proofing stream; reconcile issue descriptions and agent instructions with it.
3. Do not count retrieval, OCR transfer, page/layout inspection, or automated matching as line-by-line proofing or human approval.
4. Preserve explicit placeholders for unprocessed ranges and unknown provenance rather than filling gaps by inference.

**Current 1 Enoch boundary (as recorded in issue #1 and the proofing ledger):** 50/254 page/layout inspections; 0/254 full line-by-line diplomatic textual/apparatus proofing; independent human approval pending. The pp.63–74 images are medium-resolution and do not support detailed apparatus/Greek proofing.

### P1 — Make automated validation reliable

1. Add a general CI workflow for the complete standard-library audit and all unit tests on relevant pushes and pull requests.
2. Keep the focused proofing-integrity workflow, but do not mistake it for repository-wide quality assurance.
3. Require regression tests for corpus manifest/schema changes, catalog consistency, path/link integrity, proofing dataset invariants, and source-to-derivative transfer logic.
4. Keep network retrieval and external-source checks out of required deterministic tests; make them explicit opt-in tasks.
5. Publish CI artifacts only when useful, and avoid committing transient machine-specific audit output.

### P1 — Reconcile documentation and governance

1. Keep the root README as the human entry point and AGENTS.md as repository-relative working instructions.
2. Ensure every root directory is represented in README navigation.
3. Remove local absolute checkout paths and stale artifact paths from standing instructions.
4. Establish a compact current-state page that links to authoritative ledgers instead of copying changing counts into multiple documents.
5. Give every report a review date, scope, evidence boundary, and explicit pending/unverified section.

### P1 — Rights and provenance controls

1. No repository-wide content license is currently declared. Do not add a blanket license that purports to cover third-party texts.
2. Treat the records in copyrighted_works/ as preliminary rights-risk documentation, not legal clearance.
3. Add a machine-readable per-work provenance/rights record before expanding derivatives or external distribution.
4. Distinguish rights in the underlying ancient work from rights in a modern translation, introduction, notes, edition, scan, or OCR transcription.
5. Keep unresolved/restricted works blocked from derivative publication until the exact source and intended use are reviewed.

### P2 — Corpus structure and discovery

1. Preserve books_01–books_05 as archival intake batches; do not rename/reorganize them in a bulk pass.
2. Build a canonical catalog/index over stable work IDs, editions, witnesses, source files, derivatives, and rights status.
3. Record exact-byte duplicates and empty placeholders as candidates; do not delete them automatically.
4. Add stable identifiers and explicit relationships for alternate translations, reprints, extracts, and parallel witnesses.
5. Consider a searchable static index only after metadata consistency is established.

### P2 — Research workflow quality

1. Standardize source-to-derivative traceability at chapter/section/page level.
2. Use a controlled vocabulary for status values and verification tiers.
3. Separate machine-generated candidate discrepancies from reviewer-confirmed readings.
4. Require independent review packets to include reviewer, date, pages/units reviewed, evidence, decisions, and unresolved items.
5. Keep interpretive/speculative content clearly separated from historical claims and textual evidence.

## Repository observations

- Root README describes the collection but did not enumerate all current derivative workspaces.
- Root AGENTS.md contained an absolute local path and artifact paths that do not match the current canonical layout.
- README and tools documentation said no GitHub Actions workflow/hosted CI was required, while a focused workflow already exists.
- The existing workflow runs only `test_proofing_dataset_integrity.py` on a limited set of path filters; it does not run the complete corpus audit or full test suite.
- The GitHub Actions API returned 23 workflow runs. The latest observed run on 2026-11-26 failed; no successful full-repository CI result was established by this review.
- The repository currently has no published GitHub releases returned by the Releases API.
- The repository's own audit report records a remote metadata inventory of 165 archival text files, 24 zero-byte placeholders, and 43 non-empty exact-byte duplicate groups involving 100 paths. These are historical audit findings from the report, not newly recomputed local file-content results in this review.
- Open issues #1 and #2 already contain substantial project plans and explicit evidence boundaries. They should remain the task-tracking source of truth until consolidated deliberately.

## Changes included with this review

- Updated README navigation to represent the current repository layers and explain verification boundaries.
- Replaced machine-specific AGENTS.md paths with repository-relative working rules and explicit preservation/verification requirements.
- Corrected tools documentation so it acknowledges the existing focused Actions workflow.
- Added a general CI workflow to run the full standard-library corpus audit and test suite.

## Not performed / remaining limitations

- No complete local checkout was available for executing the audit or unit tests during this remote review.
- No source PDFs or page images were visually inspected as part of this high-level review.
- No legal determination was made for any work.
- No archival source files, OCR files, page images, or derivative text were modified.
- No issue was closed, proofing count advanced, release published, or branch merged.

## Recommended next execution sequence

1. Run the new CI workflow and repair any actual failures.
2. Run the complete local audit and unit suite from a fresh checkout; preserve raw results.
3. Reconcile the README, AGENTS.md, issue #1, issue #2, and the proofing ledger.
4. Create the machine-readable work/provenance/rights catalog schema and validate it against existing records.
5. Resolve empty files, duplicate candidates, and rights leads by documented human decisions only.
6. Continue 1 Enoch facsimile acquisition and diplomatic proofing without changing the evidence boundary until each criterion is met.
7. Expand formatted derivatives only where source identity, rights, and source coverage are clear.
