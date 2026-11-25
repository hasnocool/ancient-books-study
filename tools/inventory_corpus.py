#!/usr/bin/env python3
"""Inventory archival and derivative files."""
from __future__ import annotations
import sys
from audit_corpus import main

if __name__ == "__main__":
    raise SystemExit(main(["inventory", *sys.argv[1:]]))
