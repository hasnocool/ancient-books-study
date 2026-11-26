# Formatted Content Production Pipeline

## Status

**Workflow specification established; first manual production pilot completed for 1 Enoch 1–5. Automated extraction and validation are not yet implemented.** The pilot outputs and its validation record are in `formatted_stories/1-enoch-charles-1893/`. Story and meaning documents produced under this workflow must not be counted as diplomatic transcription, image proofing, or independent human approval.

## Current pilot

The first manual pilot covers 1 Enoch, chapters 1–5, using the repository transcription in `formatted_editions/books/book-of-enoch-charles-1893/book-01-watchers-chapters-01-36.md`. Five story adaptations and five meaning explanations were created. All remain provisional because the repository source warns that its wording has not been verified as a verbatim copy of the 1893 Charles/Dillmann printing. See `formatted_stories/1-enoch-charles-1893/README.md` for the extraction scope, unit coverage, validation performed, and outstanding checks.

## Purpose and outputs

This pipeline creates two derivative outputs from a traceable source passage:

1. **Formatted story** — a readable narrative summary of the source passage.
2. **Formatted meaning** — a plain-language explanation of what the passage says and the interpretations its evidence supports.

The diplomatic transcription remains the textual control. Facsimile inspection and the existing proofing ledger remain separate scholarly verification activities.

## Source-of-truth hierarchy

Use sources in this order, recording exactly which source was used:

1. Verified diplomatic transcription for the relevant edition and passage, when available.
2. Corrected OCR/text extraction, clearly marked provisional until collated.
3. Facsimile image for resolving wording, layout, punctuation, and apparatus questions.

Never silently repair uncertain OCR from memory or general knowledge. If the transcription is not yet verified, label the derivative as provisional and carry forward the uncertainty.

## Production stages

### 1. Select and identify a passage

Record:

- Work/book and stable book slug.
- Author/editor and edition/publication year.
- Chapter, section, paragraph identifiers, and printed page range.
- Source file path(s), including transcription/OCR and facsimile paths where applicable.
- Source revision or commit when practical.
- Text status: verified, provisional, or unresolved.

Do not infer printed page numbers from PDF ordinals. Preserve both mappings when both are needed.

### 2. Extract the source text

Extract only the selected passage, preserving paragraph boundaries and any meaningful headings, quotations, lists, or apparatus references. Do not combine non-contiguous passages without explicitly recording the gaps.

Keep the extracted source text or a stable reference to it available for review. Do not overwrite canonical PDFs, diplomatic transcriptions, OCR, or proofing records.

### 3. Create the story adaptation

Summarize the selected passage as connected, readable prose.

- Preserve the sequence and central claims/events.
- Retain names, relationships, places, important numbers, and qualifications.
- Use transitions only to improve readability.
- Do not invent dialogue, scenes, motives, chronology, or facts.
- Mark unavoidable editorial reconstruction.
- Do not collapse ambiguity into certainty.

The story is a derivative summary, not a replacement for the source text.

### 4. Create the meaning explanation

Explain the same passage independently of the story adaptation.

- Give a concise overview.
- Explain paragraph-by-paragraph or theme-by-theme.
- Clarify difficult terms, references, symbols, and argument structure.
- Separate explicit statements from interpretation and historical context.
- Identify plausible alternative readings where the text permits them.
- Cite the textual basis for each substantive interpretive claim.
- Flag unresolved textual or historical questions.

Do not treat the story adaptation as evidence for the meaning explanation; both outputs must be grounded in the source.

### 5. Validate both outputs

Run a source-alignment review before marking an output ready:

- Every output identifies the exact source passage and edition.
- No names, events, claims, relationships, or details have been added without support.
- No important source qualification or contradiction has been erased.
- Sequence and paragraph coverage are accurate.
- Ambiguities and unresolved OCR/transcription issues remain visible.
- Story and meaning documents agree on basic source facts.
- Meaning claims distinguish textual evidence from interpretation.
- Page references use printed pages, with PDF ordinals/leaf numbers separately labelled where useful.

A validation checklist is a review aid, not proof of independent human approval. Record who reviewed an output and when only when a real review occurred.

## Document status values

Use these status values consistently:

- **draft** — initial derivative; not yet checked against the source.
- **provisional** — source text or one or more material readings remain unverified.
- **reviewed** — source-alignment checklist completed; reviewer and date recorded.
- **approved** — explicitly approved by an identified human reviewer. Never assign this automatically.

Automated checks may report pass/fail for mechanical conditions, but must not assign reviewed or approved status.

## Directory and filename conventions

Keep each work in its own directory and use matching identifiers for the story and meaning pair:

`formatted_stories/<book-slug>/chapters/chapter-<NN>-story.md`

`formatted_meanings/<book-slug>/chapters/chapter-<NN>-meaning.md`

For paragraph-level work, include a stable paragraph range in the filename, for example `chapter-03-paragraphs-04-08-story.md`. Avoid filenames based only on titles that may change.

## Recommended document metadata

Every derivative should include:

- Work and edition
- Chapter/section and paragraph range
- Printed page range
- Source transcription/OCR path
- Facsimile path or image manifest, if used
- Source text verification status
- Derivative status
- Created/updated date
- Reviewer and review date, only if applicable

Use the templates in `formatted_stories/_templates/` and `formatted_meanings/_templates/`.

## Relationship to existing scholarly workflow

This pipeline does not:

- Change canonical source PDFs or diplomatic transcription.
- Mark pages as visually inspected or line-by-line proofed.
- Resolve critical apparatus or textual variants without evidence.
- Replace independent human review.
- Increase any existing proofing or verification count.

Where the source passage has an unresolved reading, retain a note in both derivatives and link it to the relevant collation/proofing record.

## Completion criteria for a passage pair

A passage pair is complete for derivative production when both files exist, identify the same source passage, pass their respective source-alignment checks, and carry accurate statuses. Human approval remains a separate, explicit state.
