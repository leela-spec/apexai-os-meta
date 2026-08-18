#!/usr/bin/env python3
"""Backward-compatible entrypoint for the standalone TTK v2 CLI."""
from ttk import main

if __name__ == "__main__":
    raise SystemExit(main())
