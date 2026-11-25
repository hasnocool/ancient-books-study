# Corpus Usage Guide

This repository is a research-oriented collection of text files. The guides below describe safe, reproducible ways to work with it.

## 1. Find a text

Use GitHub's file browser or a local search:

```bash
find books_* -type f | sort | grep -i "subject or title"
```

To search file contents:

```bash
rg -n -i "phrase" books_01 books_02 books_03 books_04 books_05
```

`grep` can be used instead on systems without `ripgrep`.

## 2. Find and cite PDF editions

The repository's Enoch scans and related PDF source artifacts are stored in [`pdfs/`](../pdfs/). Start with [`pdfs/README.md`](../pdfs/README.md) before citing a file: it distinguishes historical facsimiles from later impressions and modern re-typeset project transcriptions, records bibliographic provenance, and states which page images have or have not been visually checked. Do not infer that a PDF is a historical facsimile from its filename alone.

For reproducible citations, record the textual edition date separately from the physical scan/impression date, and distinguish printed page numbers from PDF page indices.

## 3. Check file quality

Before relying on a text, check its size and encoding:

```bash
wc -c "books_01/Bhagavad_Gita.txt"
file "books_01/Bhagavad_Gita.txt"
```

Any file whose size is `0` bytes is empty. Other files may contain OCR errors, page headers, footers, missing punctuation, or incomplete sections.

When possible, confirm the text against:

- a second transcription;
- a scan or facsimile;
- a named published edition;
- a reputable scholarly archive;
- the original language source.

## 4. Create study notes

Keep research notes separate from source texts:

```text
notes/
  work_name/
    source.md
    bibliography.md
    observations.md
```

A source note should capture:

```markdown
# Source: [Document title]

- Repository path:
- Author/compiler:
- Translator/editor:
- Edition/publication:
- Original source URL:
- License or public-domain status:
- Extraction method:
- OCR quality:
- Known omissions or transformations:
- Verification status:
```

## 5. Cite carefully

Do not cite the repository by itself when the underlying edition can be identified. Record the author or editor, title, edition, publisher or archive, publication year, and the exact repository file used.

Example format:

```text
Author or Editor. _Title_. Edition or translation. Publisher or archive, year.
Repository transcription: books_01/example.txt.
```

For web publications, also record the archive URL and access date.

## 6. Compare editions

When comparing translations or OCR copies:

- normalize whitespace only in a working copy;
- preserve the original text in the source file;
- compare section, chapter, verse, or page identifiers;
- document changed wording and the reason;
- test claims against more than one edition;
- note differences between textual criticism and modern commentary.

## 7. Work with disputed material

The collection includes religious, pseudepigraphic, archaeological, and alternative-history material. A useful study workflow is to label claims without conflating categories:

| Label | Meaning |
|---|---|
| **Source text** | A primary or historical document represented in the collection. |
| **Translation** | An interpretation of the source language. |
| **OCR transcription** | A mechanically extracted representation, which may contain errors. |
| **Secondary scholarship** | An argument or synthesis by a later author. |
| **Alternative claim** | A theory or interpretation that may not have scholarly consensus. |

Presence in this repository does not establish historical, scientific, theological, or archaeological accuracy.

## 8. Export or process data

Keep original files unchanged. Create derived files in a separate directory or branch. Prefer lossless UTF-8 text, and record the command or script used to produce it.

Example structure:

```text
notes/
derived/
  normalized/
  extracted_passages/
  search_indexes/
```

Avoid committing generated indexes or caches unless they are intentionally maintained and documented.

## 9. Rights and redistribution

Check rights before publishing, translating, repackaging, or commercially redistributing a document. A repository-wide license has not been declared; the status of individual texts may differ.

When in doubt, ask for a source and license before redistribution.
