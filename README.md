# Ancient Books Study

A public text corpus for studying ancient literature, religious traditions, historical scholarship, archaeology, science, architecture, mythology, and esoteric traditions.

The repository is primarily a **document collection**, not an application. Most files are plain-text extracts or digitized book text. A few small files are placeholders or incomplete scans.

## Repository layout
 
| Directory | Contents |
|---|---|
| [`books_01/`](./books_01/) | Religious texts, translations, Enoch literature, Gnostic writings, epic literature, and historical/scientific works. |
| [`books_02/`](./books_02/) | Architecture and engineering, medicine, mathematics, mythology, religious texts, and historical scholarship. |
| [`books_03/`](./books_03/) | Pseudepigrapha, Egyptology, chemistry, mythology, classical texts, and comparative ancient literature. |
| [`books_04/`](./books_04/) | Enochic and Hermetic literature, ancient science and medicine, papyri, Kabbalah, archaeology, and astronautic or alternative-history works. |
| [`books_05/`](./books_05/) | A broader combined collection covering architecture, archaeology, ancient engineering, translations, religious texts, and esoteric studies. |
| [`copyrighted_works/`](./copyrighted_works/) | Rights and provenance records for selected works; archival source files remain in their original collection folders. |
| [`formatted_editions/`](./formatted_editions/) | Faithful formatted reading editions, editorial standards, templates, and progress catalog. |
| [`pdfs/`](./pdfs/) | Source PDFs and digitized 1 Enoch editions, with provenance notes and scan-verification status. |
| [`artifacts/`](./artifacts/) | Downloaded page-image batches, OCR extracts, manifests, and research/audit reports; see the artifact placement guide. |
| [`modernized_editions/`](./modernized_editions/) | Clearly labelled modern-language adaptations kept separate from archival and faithful formatted source texts. |
| [`docs/`](./docs/) | Usage guidance, audit standards, and repository maintenance documentation. |
## Example texts

- [`New King James Version 1982 NKJV.txt`](./books_01/New%20King%20James%20Version%201982%20NKJV.txt)
- [`Bhagavad_Gita.txt`](./books_01/Bhagavad_Gita.txt)
- [`Aramaic_Text_Vol1.txt`](./books_01/Aramaic_Text_Vol1.txt)
- [`ANCIENT EGYPTIAN MEDICINE THE PAPYRUS EBERS.txt`](./books_02/ANCIENT%20EGYPTIAN%20MEDICINE%20THE%20PAPYRUS%20EBERS.txt)
- [`The Old Testament Pseudepigrapha vol.1 Charlesworth 1983.txt`](./books_03/The_Old_Testament_Pseudepigrapha_vol.1_Charlesworth_1983.txt)
- [`Corpus_Hermeticum_Mead_1906.txt`](./books_04/Corpus_Hermeticum_Mead_1906.txt)
- [`The Rhind Papyrus Volume 1.txt`](./books_05/The_Rhind_Papyrus_Volume_1.txt)
- [`Voynich Manuscript.txt`](./books_05/Voynich_Manuscript.txt)

## Formatted reading editions

The original numbered source collections are preserved unchanged. Faithful formatted reading editions are maintained in [`formatted_editions/`](./formatted_editions/). Modern-language adaptations are maintained separately in [`modernized_editions/`](./modernized_editions/) and must not be confused with source transcriptions. Each derivative should identify its source, editorial method, and verification status.

## Using the collection

No install or build step is required. Clone or download the repository and open the `.txt` files with a text editor:

```bash
git clone https://github.com/hasnocool/ancient-books-study.git
cd ancient-books-study
```

Search across the collection with a local text-search tool, for example:

```bash
# macOS or Linux
grep -Rin "search phrase" books_01 books_02 books_03 books_04 books_05
```

```powershell
# Windows PowerShell
Select-String -Pattern "search phrase" -Path books_*, -Recurse
```

For substantial research, copy only the desired texts into a dedicated corpus directory and record the source, edition, and filename alongside extracted notes.

## Collection notes

- These are research texts, translations, OCR results, scans in text form, and secondary scholarship; the repository is not a canonical source database.
- Treat every file as a document requiring source verification. OCR, formatting, edition, and translation quality may vary.
- Titles with different filenames may represent duplicate content, revised extracts, or different editions.
- A number of entries are empty (`0` bytes), especially some scanner/OCR placeholders. Other files may contain incomplete or unusually formatted text.
- The collection includes conventional scholarship, alternative interpretations, religious polemic, pseudoscience, and disputed claims. Presence in this repository does not imply endorsement or factual accuracy.
- **Copyrighted works** are identified and documented in [`copyrighted_works/`](./copyrighted_works/) with full provenance metadata. These are preserved for archival/research purposes only and must not be redistributed or used for derivative works without permission.

## Reading and research guidance

See [`docs/USAGE.md`](./docs/USAGE.md) for practical search, citation, verification, and extraction guidance.

The 1 Enoch PDF scans and project reference PDFs are collected in [`pdfs/`](./pdfs/), with a file-by-file provenance and verification guide in [`pdfs/README.md`](./pdfs/README.md).

See [`docs/AUDIT_STANDARDS.md`](./docs/AUDIT_STANDARDS.md) for the repository's repeatable quality-control standards. The latest [repository remediation report](./docs/REPOSITORY_AUDIT_REPORT.md) and [five-folder corpus inventory / rights-risk report](./docs/CORPUS_INVENTORY_AUDIT.md) summarize known issues and verification status. Run the local, read-only audit toolkit with `python3 tools/audit_corpus.py --help`; no GitHub Actions workflow or paid CI service is required.

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for rules on adding or correcting documents.

## Rights and provenance
 
No repository-wide license is currently declared. Individual works may be public domain, licensed, copyrighted, or of uncertain status. Do not assume that any file is freely reusable merely because it is in this repository.
 
**Copyrighted works are catalogued in [`copyrighted_works/`](./copyrighted_works/) with detailed provenance, rights holder contacts, and public-domain alternative recommendations.**
 
Before redistributing or publishing text from this collection, verify:
 
1. the source and edition;
2. applicable copyright or public-domain status;
3. any restrictions on translations or modern scholarly editions;
4. the provenance and license of OCR or transcription data.
 
Report provenance or copyright concerns through a GitHub issue with the exact filename and relevant details.
 
## Contributing
 
Contributions are welcome, especially source metadata, duplicate identification, OCR corrections, and verified public-domain or appropriately licensed texts.
 
Please read [`CONTRIBUTING.md`](./CONTRIBUTING.md) before proposing changes.
