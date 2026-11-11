#!/usr/bin/env python3
"""Build a byte-reproducible .tar.gz from a list of files.

Members are sorted by name, stored with mtime 0, uid and gid 0, mode 0644, and the gzip header carries mtime 0.
The same input bytes therefore always give the same archive hash.

Usage:
    python make_archive.py <output.tar.gz> <file> [<file> ...]
Members are stored under their base name, so give files with unique names.
"""
from __future__ import annotations

import gzip
import hashlib
import io
import sys
import tarfile
from pathlib import Path


def build(out: str, files: list[str]) -> str:
    names = [Path(f) for f in files]
    if len({p.name for p in names}) != len(names):
        raise SystemExit("duplicate base names")
    raw = io.BytesIO()
    with tarfile.open(fileobj=raw, mode="w", format=tarfile.PAX_FORMAT) as tar:
        for p in sorted(names, key=lambda x: x.name):
            data = p.read_bytes()
            info = tarfile.TarInfo(name=p.name)
            info.size, info.mtime, info.uid, info.gid, info.uname, info.gname, info.mode = len(data), 0, 0, 0, "", "", 0o644
            tar.addfile(info, io.BytesIO(data))
    with open(out, "wb") as f:
        with gzip.GzipFile(filename="", mode="wb", fileobj=f, mtime=0, compresslevel=9) as gz:
            gz.write(raw.getvalue())
    return hashlib.sha256(Path(out).read_bytes()).hexdigest()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        raise SystemExit(2)
    print(build(sys.argv[1], sys.argv[2:]), sys.argv[1])
