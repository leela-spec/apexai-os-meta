#!/usr/bin/env python3
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("Usage: PATCH-08-performance-tuning-deferred.py <repo-root>")
root = Path(sys.argv[1]).resolve()
path = root / 'apex-meta/Alpine/ARCHITEKTUR-BASIS.md'
if not path.exists():
    raise SystemExit(f'Missing expected file: {path}')
raw = path.read_bytes()
bom = raw.startswith(b'\xef\xbb\xbf')
text = raw.decode('utf-8-sig')
marker = '### Deferred performance tuning — measure first'
if marker in text:
    print('[NOCHANGE] Deferred performance tuning section already present.')
    raise SystemExit(0)
anchor = '### Current authority / evidence'
if anchor not in text:
    raise SystemExit('Architecture evidence anchor not found; refusing broad rewrite.')
section = '''### Deferred performance tuning — measure first\n\n**Status:** future candidate / no runtime change now.\n\nDo not add hard container CPU/RAM ceilings, reduce Paperless/OpenProject workers, or tune PostgreSQL/Valkey solely from generic recommendations. Open a dedicated tuning module only after measurements show a real bottleneck. Minimum evidence: `docker stats --no-stream` and product symptoms during idle, normal Hermes use, Paperless OCR, OpenProject use, backup, and restore. If no bottleneck is observed, the correct outcome is `NO_CHANGE_REQUIRED`. In particular, do not apply Valkey `allkeys-lru` eviction merely to cap memory because Valkey participates in Paperless' operational path.\n\n'''
text = text.replace(anchor, section + anchor, 1)
out = text.encode('utf-8')
if bom:
    out = b'\xef\xbb\xbf' + out
path.write_bytes(out)
print('[PATCHED] apex-meta/Alpine/ARCHITEKTUR-BASIS.md')
print('PATCH-08 COMPLETE: documentation only; no Compose/runtime tuning performed.')
