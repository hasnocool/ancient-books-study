# Local Audit Toolkit

The toolkit uses only the Python 3.12 standard library. Run commands from the repository root. These checks are intended to run locally against a complete checkout; no hosted CI service is required.

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

## Cornell 1893 page-image retrieval

The asynchronous standard-library downloader can reacquire the Cornell scan's BookReader JPEGs. It uses a bounded semaphore and runs blocking urllib requests and file writes through asyncio.to_thread, so network and disk I/O do not block the event loop. Each page is written atomically to a unique filename, JPEG bytes and dimensions are validated, and a JSON manifest records the final URL, HTTP status, SHA-256, dimensions, and failures.

```bash
# Default: printed pp.75–308, mapping printed page N to BookReader leaf n(N+21)
python3 tools/download_archive_pages.py

# Retry the full 254-page target range if needed
python3 tools/download_archive_pages.py --start-page 55 --end-page 308 --force

# Lower concurrency for rate-limited connections
python3 tools/download_archive_pages.py --concurrency 2 --retries 4 --timeout 60
```

By default, images are written to `artifacts/1-enoch-1893/page-images/bookreader-medium/`. The manifest is written to `artifacts/1-enoch-1893/manifests/bookreader-pages-START-END.json`, using the selected printed-page range. Both paths can be overridden with `--output-dir` and `--manifest`. Do not mark a page visually checked merely because it downloaded; open the image, verify the printed folio and content, then add an individual row to `IMAGE_PROOFING_LOG.md`. The script has not been run in this environment because direct access to the Archive.org image hosts failed.

## Safety and limits

- The tools are read-only unless an explicit report-output path is provided.
- They never delete duplicates, rewrite source documents, or normalize text in place.
- Normalized and near-duplicate results are candidates for manual review; different translations and editions must not be merged automatically.
- Provenance checks are keyword screens, not legal opinions or proof of bibliographic accuracy.
- Chapter sequence checks validate structure, not meaning.
- Normalized source-to-formatted text comparison validates transfer from the selected archive file, not fidelity to the historically attributed edition.
- Verse-length ratios flag unusual compression or expansion; they are not semantic-similarity scores.
- Humans must review source images and text variants before declaring a transcription verified.
