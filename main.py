#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261125 competition.

The image is an original front page drawn in this session, summing up
the world news of Wednesday 25 November 2026. It ships in this repository
as entry.png, and this program copies it to the output directory.

Standard library only. No network access. The copy is byte for byte
identical on every run, so two runs always write identical bytes.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("entry.png is missing from the repository", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    if os.path.getsize(target) != os.path.getsize(source):
        print("copied file size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
