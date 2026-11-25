#!/usr/bin/env python3
"""Find exact, normalized, and conservative near-duplicate candidates."""
from __future__ import annotations
import sys
from audit_corpus import main

if __name__ == "__main__":
    raise SystemExit(main(["duplicates", *sys.argv[1:]]))
