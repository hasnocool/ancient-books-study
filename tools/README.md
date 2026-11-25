# Local Audit Toolkit

The toolkit uses only the Python 3.12 standard library. Run commands from the repository root. No GitHub Actions, hosted runners, third-party packages, or paid CI are required.

## Full audit

```bash
python3 tools/audit_corpus.py all --json-out audit-report.json
python3 -m unittest discover -s tests -v
```

The audit prints a human-readable summary. The JSON report includes detailed findings and paths. An error-level finding makes the command exit with status 1; warnings and informational duplicate candidates do not.

## Individual checks

```bash
python3 tools/inventory_corpus.py
python3 tools/audit_duplicates.py
python3 tools/audit_markdown.py
python3 tools/audit_provenance.py
python3 tools/audit_chapters.py
python3 tools/compare_source_text.py
python3 tools/generate_catalog.py --catalog-out /tmp/formatted-catalog-preview.md
```

The equivalent subcommands are available through audit_corpus.py: inventory, duplicates, markdown, provenance, enoch, compare, and catalog.

Use --root PATH to audit a different local checkout. Use --json-out PATH for machine-readable results. The catalog generator writes only when --catalog-out is explicitly supplied; it does not overwrite the maintained formatted_editions/CATALOG.md.

## Safety and limits

- The tools are read-only unless an explicit report-output path is provided.
- They never delete duplicates, rewrite source documents, or normalize text in place.
- Normalized and near-duplicate results are candidates for manual review; different translations and editions must not be merged automatically.
- Provenance checks are keyword screens, not legal opinions or proof of bibliographic accuracy.
- Chapter sequence checks validate structure, not meaning.
- Verse-length ratios flag unusual compression or expansion; they are not semantic-similarity scores.
- Humans must review source images and text variants before declaring a transcription verified.
