#!/usr/bin/env python3
"""Report drift between a vendored copy of the Apex instruction layer and its master.

Single source: apexai-os-meta/apex-meta/informatics/final/tools/check_vendor_drift.py. Every repo that
carries a copy vendors this file byte for byte into the folder that holds its MANIFEST.sha256 (Leela:
docs/apex/, Mindful Bar: systems/apex/). tools/apex_carrier_sync.py checks that each copy equals this file.

Per vendored .md file (README.md excluded) it prints OK, DRIFTED (master changed), LOCAL-EDIT (differs from
MANIFEST.sha256), MISSING (master moved), DELETED (in the manifest, gone here) or ASSEMBLED (apex-contract.md,
built locally). The contract block
itself is compared by tools/apex_carrier_sync.py, not here.

Content is compared with line endings normalized. The master is read from branch `main` of the meta repo
when that is a git checkout, so the result does not depend on which branch is checked out; it falls back
to the working file. Without the meta repo the check prints SKIPPED and exits 0: "nothing to compare",
not "in sync". Set APEX_META to use another meta checkout.

Exit 0 = in sync or skipped. Exit 1 = drift. `--write` rewrites MANIFEST.sha256 from the current files.
"""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path

VENDOR = Path(__file__).resolve().parent
MANIFEST = VENDOR / "MANIFEST.sha256"
META = Path(os.environ.get("APEX_META", "C:/GitDev/apexai-os-meta"))
FINAL = "apex-meta/informatics/final"


def digest(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def master_bytes(rel: str) -> bytes | None:
    r = subprocess.run(["git", "-C", str(META), "show", f"main:{FINAL}/{rel}"], capture_output=True)
    if r.returncode == 0:
        return r.stdout
    p = META / FINAL / rel
    return p.read_bytes() if p.is_file() else None


def vendored_files() -> list[str]:
    out = []
    for p in sorted(VENDOR.rglob("*.md")):
        rel = p.relative_to(VENDOR).as_posix()
        if rel != "README.md":
            out.append(rel)
    return out


def write_manifest() -> int:
    lines = [f"{digest((VENDOR / rel).read_bytes())}  {rel}" for rel in vendored_files()]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {MANIFEST} ({len(lines)} files)")
    return 0


def check() -> int:
    if not (META / FINAL).is_dir():
        print(f"SKIPPED  canonical master not present at {META / FINAL}")
        print("         (a clone without apexai-os-meta is supported; nothing to compare)")
        return 0
    if not MANIFEST.is_file():
        print(f"no manifest at {MANIFEST}; run with --write first")
        return 1

    recorded = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if line.strip():
            h, rel = line.split("  ", 1)
            recorded[rel] = h

    drift = 0
    present = set(vendored_files())
    for rel in sorted(set(recorded) - present):
        print(f"DELETED     {rel}  (in the manifest, missing here)")
        drift += 1
    for rel in vendored_files():
        local = (VENDOR / rel).read_bytes()
        if recorded.get(rel) != digest(local):
            print(f"LOCAL-EDIT  {rel}  (differs from manifest -- edited in place?)")
            drift += 1
            continue
        if rel == "apex-contract.md" or not rel.startswith("specs/"):
            print(f"ASSEMBLED   {rel}")
            continue
        master = master_bytes(rel)
        if master is None:
            print(f"MISSING     {rel}  (master moved or renamed)")
            drift += 1
        elif digest(master) != digest(local):
            print(f"DRIFTED     {rel}  (master changed; re-copy)")
            drift += 1
        else:
            print(f"OK          {rel}")

    print()
    print("in sync" if not drift else f"{drift} file(s) need attention")
    return 1 if drift else 0


if __name__ == "__main__":
    sys.exit(write_manifest() if "--write" in sys.argv else check())
