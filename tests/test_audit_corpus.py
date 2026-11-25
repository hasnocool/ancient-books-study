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

    def test_parses_bracketed_verse_labels_used_in_later_source_books(self):
        text = "**[Verse 1]** First verse.\n\n**[Verse 2]** Second verse.\n"
        self.assertEqual([n for n, _ in audit_corpus.verse_units(text)], [1, 2])

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


if __name__ == "__main__":
    unittest.main()
