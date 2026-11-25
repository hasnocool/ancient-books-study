#!/usr/bin/env python3
"""Check 1 Enoch chapter-file coverage and verse-label sequences."""
from __future__ import annotations
import sys
from audit_corpus import main

if __name__ == "__main__":
    raise SystemExit(main(["enoch", *sys.argv[1:]]))
