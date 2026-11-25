"""Unit tests for the read-only corpus audit toolkit."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import audit_corpus


class NormalizationTests(unittest.TestCase):
    def test_whitespace_and_case_normalization_is_comparison_only(self):
        self.assertEqual(audit_corpus.normalized_text(" A  B\r\nC "), "a b c")

    def test_word_count_handles_apostrophes_and_hyphens(self):
        self.assertEqual(audit_corpus.word_count("Enoch's well-known text."), 3)


class VerseParsingTests(unittest.TestCase):
    def test_parses_bold_numbered_source_verses(self):
        text = "**1.** First verse.\n\n**2.** Second verse.\n"
        self.assertEqual([n for n, _ in audit_corpus.verse_units(text)], [1, 2])

    def test_parses_inline_bracketed_verse_labels_used_in_later_source_books(self):
        text = "**[Verse 1]** First verse.  **[Verse 2]** Second verse."
        self.assertEqual([n for n, _ in audit_corpus.verse_units(text)], [1, 2])

    def test_parses_bracketed_numeric_labels_with_periods(self):
        text = "**[1.]** First interpolation.  **[2.]** Second interpolation."
        self.assertEqual([n for n, _ in audit_corpus.verse_units(text)], [1, 2])

    def test_parses_interpolation_marker_inside_verse_label(self):
        text = "**[Verse 11 (interpolation)]** Interpolated unit."
        self.assertEqual([n for n, _ in audit_corpus.verse_units(text)], [11])

    def test_parses_dash_interpolation_marker_inside_verse_label(self):
        text = "**[Verse 2 — interpolation]** Interpolated unit."
        self.assertEqual([n for n, _ in audit_corpus.verse_units(text)], [2])

    def test_parses_modern_heading_verse_format_and_interpolation_suffix(self):
        text = "### Verse 1\nFirst verse.\n\n### Verse 2 — interpolation\nSecond verse.\n"
        self.assertEqual([n for n, _ in audit_corpus.verse_units(text)], [1, 2])

    def test_preserves_duplicate_and_missing_number_labels(self):
        text = "**[Verse 12]** A.\n**[Verse 14]** B.\n**[Verse 14]** C.\n**[Verse 15]** D.\n"
        self.assertEqual([n for n, _ in audit_corpus.verse_units(text)], [12, 14, 14, 15])

    def test_extracts_chapter_sections(self):
        text = "## Chapter 1\n**1.** A.\n## Chapter 2\n**1.** B.\n"
        sections = audit_corpus.chapter_sections(text)
        self.assertEqual(sorted(sections), [1, 2])
        self.assertEqual([n for n, _ in audit_corpus.verse_units(sections[2])], [1])


class EnochAuditTests(unittest.TestCase):
    def test_reports_missing_chapters_without_mutating_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_dir = root / "formatted_editions/books/book-of-enoch-charles-1893"
            modern_dir = root / "modernized_editions/books/1-enoch-repository-transcription"
            source_dir.mkdir(parents=True)
            modern_dir.mkdir(parents=True)
            (source_dir / "book-01-watchers-chapters-01-36.md").write_text(
                "## Chapter 1\n**1.** Source wording with enough words to compare.\n",
                encoding="utf-8",
            )
            modern_file = modern_dir / "chapter-001.md"
            modern_file.write_text(
                "# 1 Enoch — Chapter 1\n## Chapter 1\n### Verse 1\nModern wording with enough words to compare.\n",
                encoding="utf-8",
            )
            before = modern_file.read_text(encoding="utf-8")
            result = audit_corpus.audit_enoch(root)
            self.assertEqual(result["modernized_files_found"], 1)
            self.assertIn(2, result["missing_files"])
            self.assertEqual(result["numbered_unit_sequence_mismatches"], [])
            self.assertEqual(modern_file.read_text(encoding="utf-8"), before)


class RepositoryCheckTests(unittest.TestCase):
    def test_inventory_reports_empty_files_without_modifying_them(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            empty = root / "books_01" / "empty.txt"
            empty.parent.mkdir(parents=True)
            empty.write_bytes(b"")
            before = empty.read_bytes()
            result = audit_corpus.audit_inventory(root)
            self.assertEqual(result["empty_files"], ["books_01/empty.txt"])
            self.assertEqual(empty.read_bytes(), before)

    def test_exact_duplicate_detection_is_advisory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for folder in ("books_01", "books_02"):
                path = root / folder / "same.txt"
                path.parent.mkdir(parents=True)
                path.write_text("The same source text.\n", encoding="utf-8")
            result = audit_corpus.audit_duplicates(root)
            self.assertEqual(len(result["exact_duplicate_groups"]), 1)
            self.assertEqual(len(result["exact_duplicate_groups"][0]), 2)

    def test_markdown_validator_finds_missing_relative_target(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            doc = root / "docs" / "index.md"
            doc.parent.mkdir(parents=True)
            doc.write_text("[Missing](./missing.md)\n", encoding="utf-8")
            result = audit_corpus.audit_markdown(root)
            self.assertEqual(len(result["issues"]), 1)
            self.assertIn("does not exist", result["issues"][0]["message"])

    def test_catalog_preview_is_generated_without_overwriting_catalog(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            edition = root / "formatted_editions" / "books" / "sample"
            edition.mkdir(parents=True)
            (edition / "README.md").write_text(
                "# Sample Edition\n\n**Status:** Draft\n", encoding="utf-8"
            )
            catalog = root / "formatted_editions" / "CATALOG.md"
            catalog.parent.mkdir(parents=True, exist_ok=True)
            catalog.write_text("maintained catalog\n", encoding="utf-8")
            result = audit_corpus.audit_catalog(root)
            self.assertEqual(result["edition_count"], 1)
            self.assertIn("Sample Edition", result["markdown_preview"])
            self.assertEqual(result["editions"][0]["status_line"], "Draft")
            self.assertEqual(catalog.read_text(encoding="utf-8"), "maintained catalog\n")


class SourceTransferTests(unittest.TestCase):
    def test_raw_extractor_excludes_slavonic_and_preserves_opening_blessing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "books_02" / "The Book of Enoch.txt"
            source.parent.mkdir(parents=True)
            source.write_text(
                "These are the words of blessing of Enoch, for all the righteous removed.\n"
                "Enoch 1.\nFirst chapter body.\n"
                "Enoch Slavonic 1.\nSeparate Slavonic work.\n"
                "Chapt 2.\nSecond chapter body.\n",
                encoding="utf-8",
            )
            chapters = audit_corpus.load_raw_enoch_chapters(root)
            self.assertEqual(sorted(chapters), [1, 2])
            self.assertIn("words of blessing", chapters[1])
            self.assertNotIn("Slavonic work", chapters[1])
            self.assertIn("Second chapter body", chapters[2])

    def test_archival_to_formatted_transfer_compares_normalized_chapter_bodies(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "books_02" / "The Book of Enoch.txt"
            source.parent.mkdir(parents=True)
            source.write_text(
                "These are the words of blessing of Enoch, for all the righteous removed.\n"
                "Enoch 1.\nFirst chapter body.\n"
                "Chapt 2.\nSecond chapter body.\n",
                encoding="utf-8",
            )
            formatted = root / "formatted_editions" / "books" / "book-of-enoch-charles-1893"
            formatted.mkdir(parents=True)
            (formatted / "book-01-watchers-chapters-01-36.md").write_text(
                "## Chapter 1\nThese are the words of blessing of Enoch, for all the righteous removed.\n"
                "### Verse 1\nFirst chapter body.\n---\n"
                "## Chapter 2\n### Verse 1\nSecond chapter body.\n",
                encoding="utf-8",
            )
            result = audit_corpus.audit_enoch_source_transfer(root)
            self.assertEqual(result["raw_source_chapters_found"], 2)
            self.assertEqual(result["formatted_source_chapters_found"], 2)
            self.assertEqual(result["exact_normalized_chapter_matches"], 2)
            self.assertEqual(result["review_candidates"], [])



if __name__ == "__main__":
    unittest.main()
