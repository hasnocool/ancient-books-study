#!/usr/bin/env python3
"""Generate a reviewable formatted-edition catalog preview."""
from __future__ import annotations
import sys
from audit_corpus import main

if __name__ == "__main__":
    raise SystemExit(main(["catalog", *sys.argv[1:]]))
