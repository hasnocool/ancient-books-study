#!/usr/bin/env python3
"""Report source/adaptation unit-length outliers for human review."""
from __future__ import annotations
import sys
from audit_corpus import main

if __name__ == "__main__":
    raise SystemExit(main(["compare", *sys.argv[1:]]))
