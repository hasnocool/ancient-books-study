# tools/download_archive_pages.py
"""Download Internet Archive BookReader page images without blocking the asyncio event loop.

The default mapping for the Cornell 1893 Enoch scan is printed page N -> BookReader
leaf n(N + 21). Images are written outside the repository by default; do not commit
hundreds of large page JPEGs unless that is an explicit project decision.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
import sys
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


USER_AGENT = "ancient-books-study-page-retriever/1.0 (+https://github.com/hasnocool/ancient-books-study)"
DEFAULT_IDENTIFIER = "cu31924014590545"


def jpeg_dimensions(data: bytes) -> tuple[int, int] | None:
    """Read JPEG dimensions from a Start Of Frame segment."""
    if len(data) < 4 or data[:2] != b"\xff\xd8":
        return None

    sof_markers = {
        0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
        0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF,
    }
    offset = 2

    while offset + 4 <= len(data):
        if data[offset] != 0xFF:
            offset += 1
            continue

        while offset < len(data) and data[offset] == 0xFF:
            offset += 1
        if offset >= len(data):
            break

        marker = data[offset]
        offset += 1

        if marker in {0xD8, 0xD9, 0x01} or 0xD0 <= marker <= 0xD7:
            continue

        if offset + 2 > len(data):
            break

        segment_length = int.from_bytes(data[offset : offset + 2], "big")
        if segment_length < 2 or offset + segment_length > len(data):
            break

        if marker in sof_markers and segment_length >= 7:
            height = int.from_bytes(data[offset + 3 : offset + 5], "big")
            width = int.from_bytes(data[offset + 5 : offset + 7], "big")
            if width > 0 and height > 0:
                return width, height

        offset += segment_length

    return None


def has_jpeg_eoi(data: bytes) -> bool:
    """Return whether a JPEG byte stream ends with its required EOI marker."""
    return data.endswith(bytes((0xFF, 0xD9)))


def fetch_jpeg_sync(url: str, timeout: float) -> dict[str, Any]:
    """Blocking urllib request; always call this function via asyncio.to_thread."""
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "image/jpeg,image/*;q=0.9,*/*;q=0.5",
        },
    )

    with urlopen(request, timeout=timeout) as response:
        body = response.read()
        content_type = response.headers.get_content_type()
        final_url = response.geturl()
        status = getattr(response, "status", 200)

    if not body.startswith(b"\xff\xd8"):
        raise ValueError(
            f"Response was not a JPEG (content-type={content_type}, bytes={len(body)})"
        )
    if len(body) < 1024:
        raise ValueError(f"JPEG response is suspiciously small ({len(body)} bytes)")
    if not has_jpeg_eoi(body):
        raise ValueError("JPEG response is missing the end-of-image marker")

    dimensions = jpeg_dimensions(body)
    if dimensions is None:
        raise ValueError("JPEG dimensions could not be parsed")

    return {
        "body": body,
        "url": final_url,
        "http_status": status,
        "content_type": content_type,
        "width": dimensions[0],
        "height": dimensions[1],
    }


def inspect_existing_sync(path: Path) -> dict[str, Any] | None:
    """Validate an existing local JPEG before deciding whether to skip it."""
    try:
        body = path.read_bytes()
    except OSError:
        return None

    dimensions = jpeg_dimensions(body)
    if not body.startswith(b"\xff\xd8") or not has_jpeg_eoi(body) or dimensions is None:
        return None

    return {
        "sha256": hashlib.sha256(body).hexdigest(),
        "bytes": len(body),
        "width": dimensions[0],
        "height": dimensions[1],
    }


def atomic_write_sync(path: Path, body: bytes) -> None:
    """Write to a unique temporary file, then atomically replace the destination."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".part")
    try:
        temporary.write_bytes(body)
        os.replace(temporary, path)
    finally:
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            pass


def candidate_urls(identifier: str, leaf: int, prefer_large: bool = False) -> list[str]:
    """Build BookReader size fallbacks, optionally prioritizing proofing resolution."""
    base = f"https://archive.org/download/{identifier}/page/n{leaf}"
    sizes = ("large", "medium", "original", "small") if prefer_large else (
        "medium", "large", "original", "small"
    )
    return [f"{base}_{size}.jpg" if size != "original" else f"{base}.jpg" for size in sizes]


async def download_one(
    *,
    printed_page: int,
    leaf: int,
    identifier: str,
    output_dir: Path,
    semaphore: asyncio.Semaphore,
    timeout: float,
    retries: int,
    force: bool,
    prefer_large: bool,
) -> dict[str, Any]:
    filename = f"p{printed_page:03d}_n{leaf:03d}.jpg"
    destination = output_dir / filename

    if destination.exists() and not force:
        existing = await asyncio.to_thread(inspect_existing_sync, destination)
        if existing is not None:
            return {
                "printed_page": printed_page,
                "bookreader_leaf": leaf,
                "filename": filename,
                "status": "already_present",
                **existing,
            }

    attempts: list[dict[str, Any]] = []
    for url in candidate_urls(identifier, leaf, prefer_large=prefer_large):
        for attempt_number in range(1, retries + 2):
            started = time.monotonic()
            try:
                async with semaphore:
                    result = await asyncio.to_thread(fetch_jpeg_sync, url, timeout)
                body = result.pop("body")
                await asyncio.to_thread(atomic_write_sync, destination, body)
                return {
                    "printed_page": printed_page,
                    "bookreader_leaf": leaf,
                    "filename": filename,
                    "status": "downloaded",
                    "source_url": result["url"],
                    "http_status": result["http_status"],
                    "content_type": result["content_type"],
                    "sha256": hashlib.sha256(body).hexdigest(),
                    "bytes": len(body),
                    "width": result["width"],
                    "height": result["height"],
                    "attempts": attempts,
                }
            except HTTPError as exc:
                error = f"HTTP {exc.code}: {exc.reason}"
                http_status = exc.code
            except (URLError, TimeoutError, OSError, ValueError) as exc:
                error = f"{type(exc).__name__}: {exc}"
                http_status = None
            except Exception as exc:  # Keep one failed page from cancelling the batch.
                error = f"Unexpected {type(exc).__name__}: {exc}"
                http_status = None

            attempts.append(
                {
                    "url": url,
                    "attempt": attempt_number,
                    "http_status": http_status,
                    "error": error,
                    "elapsed_seconds": round(time.monotonic() - started, 3),
                }
            )
            if attempt_number <= retries:
                await asyncio.sleep(min(2 ** (attempt_number - 1), 8))

    return {
        "printed_page": printed_page,
        "bookreader_leaf": leaf,
        "filename": filename,
        "status": "failed",
        "attempts": attempts,
    }


def write_manifest_sync(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".part")
    try:
        temporary.write_text(
            json.dumps(records, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


async def run(args: argparse.Namespace) -> int:
    if args.start_page < 1 or args.end_page < args.start_page:
        raise ValueError("Require 1 <= start-page <= end-page")
    if args.concurrency < 1:
        raise ValueError("concurrency must be at least 1")
    if args.retries < 0:
        raise ValueError("retries cannot be negative")

    output_dir = Path(args.output_dir).expanduser().resolve()
    manifest_value = args.manifest or (
        f"artifacts/1-enoch-1893/manifests/"
        f"bookreader-pages-{args.start_page}-{args.end_page}.json"
    )
    manifest_path = Path(manifest_value).expanduser().resolve()
    await asyncio.to_thread(output_dir.mkdir, parents=True, exist_ok=True)

    semaphore = asyncio.Semaphore(args.concurrency)
    jobs = [
        download_one(
            printed_page=page,
            leaf=page + args.leaf_offset,
            identifier=args.identifier,
            output_dir=output_dir,
            semaphore=semaphore,
            timeout=args.timeout,
            retries=args.retries,
            force=args.force,
            prefer_large=args.prefer_large,
        )
        for page in range(args.start_page, args.end_page + 1)
    ]

    records = await asyncio.gather(*jobs)
    records.sort(key=lambda item: item["printed_page"])
    await asyncio.to_thread(write_manifest_sync, manifest_path, records)

    downloaded = sum(item["status"] == "downloaded" for item in records)
    present = sum(item["status"] == "already_present" for item in records)
    failed = sum(item["status"] == "failed" for item in records)

    print(
        f"Pages: {len(records)} | downloaded: {downloaded} | "
        f"already present: {present} | failed: {failed}"
    )
    print(f"Images: {output_dir}")
    print(f"Manifest: {manifest_path}")
    return 1 if failed else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Retrieve Internet Archive BookReader JPEGs for printed pages."
    )
    parser.add_argument("--identifier", default=DEFAULT_IDENTIFIER)
    parser.add_argument("--start-page", type=int, default=75)
    parser.add_argument("--end-page", type=int, default=308)
    parser.add_argument(
        "--leaf-offset",
        type=int,
        default=21,
        help="BookReader leaf = printed page + offset (Cornell map: +21).",
    )
    parser.add_argument(
        "--output-dir",
        default="artifacts/1-enoch-1893/page-images/bookreader-medium",
    )
    parser.add_argument(
        "--manifest",
        default=None,
        help=(
            "Manifest output path (default: artifacts/1-enoch-1893/manifests/"
            "bookreader-pages-START-END.json)."
        ),
    )
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--timeout", type=float, default=45.0)
    parser.add_argument(
        "--prefer-large",
        action="store_true",
        help="Try the large BookReader JPEG before medium (recommended for textual proofing).",
    )
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        return asyncio.run(run(args))
    except KeyboardInterrupt:
        print("Interrupted; completed image files remain on disk.", file=sys.stderr)
        return 130
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
