# Formatted Editions

This directory contains clean, structured reading editions derived from texts in the repository's numbered source collections.

The original files in `books_01/` through `books_05/` are archival inputs and must remain unchanged. A formatted edition is a separate derivative document with its source, edition, editorial decisions, and verification status recorded.

## What “formatted” means

The default product is a **faithful formatted transcription**:

- preserve the wording of the identified source translation or edition;
- restore meaningful title, book, chapter, section, verse, and paragraph structure;
- remove obvious scan-page furniture and OCR layout noise;
- normalize whitespace and Markdown typography without silently modernizing the language;
- retain translator-supplied brackets, ellipses, notes, and uncertainty markers;
- record any correction or emendation rather than concealing it.

A modern-language rewrite, paraphrase, commentary, or study guide is a different editorial layer. It must be labelled as such and must not be presented as the historical source text.

## Directory layout

```text
formatted_editions/
  README.md
  CATALOG.md
  STYLE_GUIDE.md
  TEMPLATE.md
  books/
    <work-id>/
      <work-or-part>.md
```

A work may be divided into several Markdown files when that makes navigation, review, and maintenance easier.

## Current editions

- [Corpus Hermeticum — all 15 tractates and supplementary texts](./books/corpus-hermeticum-mead-1906/README.md)
- [The Book of Enoch (1 Enoch) — R. H. Charles, 1893](./books/book-of-enoch-charles-1893/README.md)

See the [catalog](./CATALOG.md) for progress and the exact source files used.

## Workflow

1. Identify the work, author/compiler, translator/editor, edition, publication date, and source file.
2. Check source quality, completeness, provenance, and redistribution rights.
3. Separate the historical text from modern introductions, notes, or website boilerplate.
4. Format the source text without changing its meaning or wording.
5. Compare the result against a trustworthy scan or a second reliable transcription.
6. Record unresolved OCR issues and publish only with a clear verification status.

## Rights and attribution

The repository does not declare a blanket license for every source file. Rights must be assessed for each work and each translation or editorial contribution. The fact that a historical work is old does not automatically make a modern translation, introduction, notes, or digital edition free to redistribute.

Do not copy modern copyrighted editorial material into a formatted edition unless its license permits it. When rights are unclear, limit the derivative to bibliographic metadata, original commentary, and appropriately brief quotations.

## Status labels

- **Queued** — identified but not yet processed.
- **Formatting** — structure and layout work is in progress.
- **Formatted draft** — a first formatting pass exists but has not been fully checked.
- **Verified** — checked against the stated source edition or a reliable facsimile.
- **Needs source** — source identity, completeness, or provenance is inadequate.
- **Rights review** — redistribution status needs further research.
