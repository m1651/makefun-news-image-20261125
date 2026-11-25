#!/usr/bin/env python3
"""news-image-20261125: deliver the front page as /output/entry.png.

The picture this repository holds is the entry: a 1024 by 1024 PNG
drawn for Wednesday 25 November 2026. This script reads it and writes
the same bytes to the output directory, so both grading runs produce
identical files. Only the standard library is used, and nothing here
touches the network.
"""

from pathlib import Path


def entry_image() -> Path:
    """Return the path of the PNG shipped with this repository."""
    return Path(__file__).resolve().parent / "entry.png"


def output_dir() -> Path:
    """Return the directory the grader wants the image written to."""
    from os import environ

    return Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def run() -> int:
    """Copy the entry image to the output directory; 0 on success."""
    source = entry_image()
    if not source.is_file():
        print("entry.png is missing from the repository")
        return 1
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    payload = source.read_bytes()
    if payload[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file")
        return 1
    target.write_bytes(payload)
    if target.stat().st_size != len(payload):
        print("copied file size mismatch")
        return 1
    return 0


raise SystemExit(run())
