#!/usr/bin/env python3
"""Screen formatted and modernized edition indexes for provenance fields."""
from __future__ import annotations
import sys
from audit_corpus import main

if __name__ == "__main__":
    raise SystemExit(main(["provenance", *sys.argv[1:]]))
