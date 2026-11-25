# tests/test_download_archive_pages.py
"""Unit tests for the Internet Archive page-image downloader."""

from __future__ import annotations

import unittest

from tools.download_archive_pages import candidate_urls, has_jpeg_eoi, jpeg_dimensions


class JpegDimensionsTests(unittest.TestCase):
    def test_reads_dimensions_from_baseline_sof_segment(self) -> None:
        # Minimal JPEG marker stream with a SOF0 segment (width=1360, height=2276).
        sample = bytes.fromhex(
            "FFD8"          # SOI
            "FFC0"          # SOF0
            "000B"          # segment length
            "08"            # precision
            "08E4"          # height = 2276
            "0550"          # width = 1360
            "03"            # component count
            "011100"        # component descriptor
            "FFD9"          # EOI
        )
        self.assertEqual(jpeg_dimensions(sample), (1360, 2276))

    def test_requires_end_of_image_marker(self) -> None:
        self.assertTrue(has_jpeg_eoi(b"\xff\xd8payload\xff\xd9"))
        self.assertFalse(has_jpeg_eoi(b"\xff\xd8payload"))

    def test_rejects_non_jpeg_data(self) -> None:
        self.assertIsNone(jpeg_dimensions(b"not a jpeg"))

    def test_rejects_jpeg_without_sof_segment(self) -> None:
        self.assertIsNone(jpeg_dimensions(bytes.fromhex("FFD8FFD9")))


class CandidateUrlTests(unittest.TestCase):
    def test_builds_medium_first_fallbacks_by_default(self) -> None:
        self.assertEqual(
            candidate_urls("cu31924014590545", 323),
            [
                "https://archive.org/download/cu31924014590545/page/n323_medium.jpg",
                "https://archive.org/download/cu31924014590545/page/n323_large.jpg",
                "https://archive.org/download/cu31924014590545/page/n323.jpg",
                "https://archive.org/download/cu31924014590545/page/n323_small.jpg",
            ],
        )

    def test_large_first_fallbacks_for_proofing(self) -> None:
        self.assertEqual(
            candidate_urls("cu31924014590545", 323, prefer_large=True),
            [
                "https://archive.org/download/cu31924014590545/page/n323_large.jpg",
                "https://archive.org/download/cu31924014590545/page/n323_medium.jpg",
                "https://archive.org/download/cu31924014590545/page/n323.jpg",
                "https://archive.org/download/cu31924014590545/page/n323_small.jpg",
            ],
        )


if __name__ == "__main__":
    unittest.main()
