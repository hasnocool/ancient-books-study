# Contributing

Thank you for helping improve the ancient texts corpus. Contributions should make the collection easier to study while preserving its research provenance.

## What to contribute

Useful contributions include:

- source, edition, translator, author, publication, or URL metadata;
- corrections to OCR or text extraction;
- identification of duplicate or near-duplicate files;
- removal or replacement of empty or placeholder files;
- clearer filenames that preserve the original title and edition;
- notes about provenance, copyright, or uncertain text quality;
- scripts that validate encoding or inventory the collection.

## Adding a text

Before uploading, verify all of the following:

1. **Rights:** the work is public domain or has an applicable license permitting repository distribution.
2. **Source:** the book or text was obtained from a trustworthy archive or published edition.
3. **Identity:** the title, author, translator, edition, and publication year are known when available.
4. **Completeness:** the file is not a placeholder and has been checked for truncation or severe OCR corruption.
5. **Encoding:** prefer UTF-8 plain text with Unix-style line endings where practical.

Include a short metadata note in the pull request, covering:

- original title;
- author or compiler;
- translator or editor, if applicable;
- edition or publication date;
- source URL;
- license or public-domain basis;
- extraction or OCR method;
- known limitations.

Do not add DRM-controlled exports, pirated editions, private databases, or documents for which redistribution rights are unclear.

## Choosing a directory

The `books_01` through `books_05` directories represent collection batches and are not currently category-based folders.

- Add to the directory requested by the maintainer or use `books_05` for an additional batch only when batch numbering is appropriate.
- Do not create a large renaming or restructuring change inside a small text correction.
- Preserve existing filenames unless there is a clear duplicate or ambiguity issue. If renaming is necessary, document both the old and new names in the pull request.

## Correcting text

For OCR corrections:

- avoid silently changing interpretation or adding modernized wording;
- distinguish the transcribed text from editorial notes;
- identify the source page or section for corrections that may be disputed;
- do not replace complete passages when the source text is incomplete or illegible.

For destructive renames or deletions, open an issue first so that links and duplicate relationships can be reviewed.

## Reviewing duplicates

Two files may look different because they contain:

- a different edition or translation;
- a different OCR extraction;
- a split or duplicated section;
- the same title with different formatting;
- one intact copy and one corrupt or empty copy.

Compare sizes and representative passages before merging or deleting anything.

## Pull requests

- keep changes focused;
- explain the reason for each text or filename change;
- link to source or provenance information;
- list known limitations;
- do not claim that a disputed text or theory is factually established;
- add or update documentation when repository conventions change.

## Local quality checks

Before submitting changes to text editions or repository documentation, run the read-only local audit toolkit from the repository root (Python 3.12+):

```bash
python3 tools/audit_corpus.py all --json-out /tmp/ancient-books-audit.json
python3 -m unittest discover -s tests -v
```

For a focused review, run one of the commands in [tools/README.md](./tools/README.md). Review warnings manually. Duplicate candidates, word-count outliers, and provenance keyword matches are not automatic grounds for deleting or changing a text.

Do not commit generated reports unless they are intended as maintained documentation. Do not add paid hosted CI workflows as a prerequisite for these checks.

## Reporting issues

Open a GitHub issue for:

- missing or empty text files;
- OCR or encoding problems;
- questionable provenance;
- copyright or licensing concerns;
- broken links or misleading metadata;
- suggestions for collection organization.

Include the exact path, for example `books_03/The Gospel Of Thomas.txt`, and a short reproducible description.
