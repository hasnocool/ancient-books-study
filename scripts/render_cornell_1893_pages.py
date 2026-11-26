#!/usr/bin/env python3
# Filename: scripts/render_cornell_1893_pages.py
"""Render Cornell 1893 printed pages 85–94 from the committed source PDF.

The source PDF is never modified. Each page is exported twice:
  - raw grayscale render (the evidentiary rendering)
  - lightly normalized grayscale render (for easier viewing)

Printed pp.85–94 map to one-based PDF pages 107–116.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
from pathlib import Path
from typing import Any

import fitz  # PyMuPDF
from PIL import Image, ImageOps

LOGGER = logging.getLogger("render_cornell_1893")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def render_pages(pdf_path: Path, output_dir: Path, dpi: int) -> dict[str, Any]:
    if not pdf_path.is_file():
        raise FileNotFoundError(f"Source PDF not found: {pdf_path}")
    if dpi < 150 or dpi > 600:
        raise ValueError("DPI must be between 150 and 600.")

    output_dir.mkdir(parents=True, exist_ok=True)
    source_hash = sha256_file(pdf_path)
    matrix = fitz.Matrix(dpi / 72, dpi / 72)
    records: list[dict[str, Any]] = []

    with fitz.open(pdf_path) as document:
        if document.page_count < 116:
            raise ValueError(
                f"Expected at least 116 PDF pages; found {document.page_count}."
            )

        for pdf_page_number in range(107, 117):
            printed_page = pdf_page_number - 22
            page = document.load_page(pdf_page_number - 1)
            pixmap = page.get_pixmap(
                matrix=matrix,
                colorspace=fitz.csGRAY,
                alpha=False,
                annots=True,
            )
            image = Image.frombytes(
                "L", (pixmap.width, pixmap.height), pixmap.samples
            )

            stem = f"printed_p{printed_page:03d}_pdf{pdf_page_number:03d}"
            raw_path = output_dir / f"{stem}_raw.png"
            normalized_path = output_dir / f"{stem}_normalized.png"

            image.save(raw_path, format="PNG", optimize=True)

            # Keep this as a derivative. The raw export remains authoritative.
            normalized = ImageOps.autocontrast(image, cutoff=0.1)
            normalized.save(normalized_path, format="PNG", optimize=True)

            records.append(
                {
                    "printed_page": printed_page,
                    "pdf_page_1based": pdf_page_number,
                    "bookreader_leaf": f"n{printed_page + 21:03d}",
                    "width_px": pixmap.width,
                    "height_px": pixmap.height,
                    "dpi": dpi,
                    "raw_path": str(raw_path),
                    "raw_sha256": sha256_file(raw_path),
                    "normalized_path": str(normalized_path),
                    "normalized_sha256": sha256_file(normalized_path),
                    "normalization": "Pillow ImageOps.autocontrast cutoff=0.1",
                    "visual_proofing_status": "not_yet_human_inspected",
                }
            )
            LOGGER.info(
                "Rendered printed p.%s from PDF p.%s (%sx%s)",
                printed_page,
                pdf_page_number,
                pixmap.width,
                pixmap.height,
            )

    manifest = {
        "title": "Cornell 1893 printed pages 85–94 rendered from source PDF",
        "source_pdf": str(pdf_path),
        "source_pdf_sha256": source_hash,
        "mapping": {
            "printed_page_to_pdf_page": "PDF page = printed page + 22",
            "printed_page_to_bookreader_leaf": "leaf number = printed page + 21",
        },
        "dpi": dpi,
        "evidence_policy": (
            "Raw renders preserve the PDF rendering without contrast changes. "
            "Normalized renders are viewing derivatives only. Neither set "
            "counts as proofed until each page is opened and inspected."
        ),
        "pages": records,
    }
    manifest_path = output_dir / "render-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    LOGGER.info("Wrote manifest: %s", manifest_path)
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pdf",
        type=Path,
        default=Path("pdfs/enoch-editions/enoch-1893-clarendon-original.pdf"),
        help="Path to the committed Cornell 1893 source PDF.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/page-images/cornell-native/cornell_printed_pp85_94_rerendered"),
        help="Output directory for raw and normalized page PNGs.",
    )
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )
    try:
        render_pages(args.pdf, args.output, args.dpi)
    except (OSError, ValueError, RuntimeError) as exc:
        LOGGER.error("%s", exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
