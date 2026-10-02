#!/usr/bin/env python3
from pathlib import Path
import shutil
import sys

if len(sys.argv) != 2:
    raise SystemExit('Usage: INSTALL-PLAN-FILES.py <repo-root>')
root = Path(sys.argv[1]).resolve()
src = Path(__file__).resolve().parent / 'plans'
dst = root / 'apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization'
if dst.exists() and any(dst.iterdir()):
    raise SystemExit(f'Target already exists and is non-empty: {dst}\nRefusing to overwrite.')
dst.mkdir(parents=True, exist_ok=True)
for p in sorted(src.glob('*.md')):
    shutil.copy2(p, dst / p.name)
shutil.copy2(Path(__file__).resolve().parent / 'HANDOVER-NEXT-CHAT.md', dst / 'HANDOVER-NEXT-CHAT.md')
print(f'Installed plan files into: {dst}')
print('No commit or push performed. Review git diff before committing.')
