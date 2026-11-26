# tests/test_proofing_dataset_integrity.py
"""Integrity tests for the 1 Enoch 1893 OCR/proofing evidence artifacts."""

import csv
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "artifacts/1-enoch-1893/reports/diplomatic_proofing_full/proofing_full_combined.json"
QUEUE = ROOT / "artifacts/1-enoch-1893/reports/diplomatic_proofing_full/verification_queue.csv"
IMAGE_LOG = ROOT / "formatted_editions/books/book-of-enoch-charles-1893/IMAGE_PROOFING_LOG.md"
AGENTS = ROOT / "AGENTS.md"


class ProofingDatasetIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dataset = json.loads(DATASET.read_text(encoding="utf-8"))
        with QUEUE.open(encoding="utf-8", newline="") as handle:
            cls.queue = list(csv.DictReader(handle))

    def test_section_ranges_cover_target_pages_exactly_once(self):
        metadata = self.dataset["metadata"]
        start = metadata["coverage_start_page"]
        end = metadata["coverage_end_page"]
        membership = {}

        for section_name, section in self.dataset["sections"].items():
            match = re.fullmatch(r"(\d+)-(\d+)", section["pages"])
            self.assertIsNotNone(match, f"Invalid page range for {section_name}")
            first, last = map(int, match.groups())
            self.assertLessEqual(first, last)
            for page in range(first, last + 1):
                membership[page] = membership.get(page, 0) + 1

        expected = set(range(start, end + 1))
        self.assertEqual(set(membership), expected)
        self.assertTrue(all(count == 1 for count in membership.values()))
        self.assertEqual(metadata["distinct_pages_covered"], len(expected))
        self.assertEqual(metadata["coverage_page_memberships"], len(expected))
        self.assertEqual(metadata["sections_processed"], len(self.dataset["sections"]))

    def test_unprocessed_pages_are_explicit_placeholders(self):
        metadata = self.dataset["metadata"]
        expected = metadata["unprocessed_printed_pages"]
        self.assertEqual(expected, [260, 261, 262, 263, 264])
        placeholder = self.dataset["sections"]["pp260-264"]
        self.assertEqual(placeholder["status"], "NOT_PROCESSED")
        self.assertEqual(placeholder["apparatus"], [])
        self.assertEqual(placeholder["discrepancies"], [])
        self.assertIsNone(placeholder["stats"]["total_discrepancies"])

    def test_duplicate_subrange_is_not_an_aggregate_section(self):
        sections = self.dataset["sections"]
        self.assertNotIn("pp301-308", sections)
        self.assertIn("pp301-308", self.dataset["metadata"]["subsection_aliases"])
        self.assertEqual(sections["pp285-308"]["pages"], "285-308")

    def test_automated_candidates_are_never_human_verified(self):
        self.assertTrue(self.queue)
        for row in self.queue:
            self.assertEqual(row["Verified"].upper(), "N")
            self.assertEqual(row["Reviewer"], "HUMAN_REVIEW_PENDING")
            self.assertNotIn("SIMULATED", row["Reviewer"].upper())

    def test_metadata_does_not_claim_completed_diplomatic_proofing(self):
        metadata = self.dataset["metadata"]
        self.assertEqual(
            metadata["audit_status"], "COVERAGE_MANIFEST_REPAIRED_CONTENT_INCOMPLETE"
        )
        self.assertEqual(metadata["discrepancy_summary_status"], "UNRECONCILED")
        self.assertEqual(metadata["human_verified_discrepancies"], 0)
        self.assertEqual(
            metadata["total_verses_definition"],
            "UNDEFINED_LEGACY_METADATA_NOT_VALIDATED",
        )

    def test_progress_summaries_agree_on_layout_and_textual_proofing(self):
        image_log = IMAGE_LOG.read_text(encoding="utf-8")
        agents = AGENTS.read_text(encoding="utf-8")
        self.assertIn("30/254 pages", image_log)
        self.assertIn("Page/layout-level visual inspection | 30 / 254", agents)
        self.assertIn("0/254 pages have completed full line-by-line", image_log)
        self.assertIn("Full high-resolution textual/apparatus proofing | 0 / 254", agents)


if __name__ == "__main__":
    unittest.main()
