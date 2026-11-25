#!/usr/bin/env python3
"""Check relative Markdown links and heading anchors."""
from __future__ import annotations
import sys
from audit_corpus import main

if __name__ == "__main__":
    raise SystemExit(main(["markdown", *sys.argv[1:]]))
