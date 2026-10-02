#!/usr/bin/env python3
from pathlib import Path
import re
import sys

if len(sys.argv) != 2:
    raise SystemExit('Usage: VERIFY-PATCHES.py <repo-root>')
root = Path(sys.argv[1]).resolve()

def txt(rel):
    p = root / rel
    if not p.exists():
        raise SystemExit(f'MISSING: {rel}')
    return p.read_text(encoding='utf-8-sig')

dossier = txt('apex-meta/Alpine/HANDOVER-REVIEWER-DOSSIER.md')
target = txt('apex-meta/Alpine/TARGET-ACCEPTANCE-REPORT.md')
arch = txt('apex-meta/Alpine/ARCHITEKTUR-BASIS.md')
old = txt('apex-meta/Alpine/Iteration2/VerificationAG.md')

checks = {
    'dossier token redacted': '<REDACTED_PAPERLESS_API_TOKEN>' in dossier,
    'no stale no-push headline': 'No Git Push Performed' not in dossier and 'NO PUSH ENFORCED' not in dossier,
    'no obvious Paperless 40-hex token on token line': re.search(r'Paperless API Token[^\n]*`[0-9a-fA-F]{40,}`', dossier) is None,
    'architecture points at target report': 'Current target acceptance: [`TARGET-ACCEPTANCE-REPORT.md`]' in arch,
    'historical source remains linked': 'Historical pre-migration source evidence' in arch,
    'Hermes data backup listed': 'hermes_data.tar.gz' in target,
    'Hermes workspace backup listed': 'hermes_workspaces.tar.gz' in target,
    'template DBs not treated as app acceptance': 'not treated as application acceptance targets' in target,
    'old verification marked historical': '> **Historical snapshot:**' in old,
    'performance tuning is deferred': '### Deferred performance tuning — measure first' in arch,
    'no speculative Valkey eviction instruction': 'do not apply Valkey `allkeys-lru`' in arch,
}
failed = [k for k,v in checks.items() if not v]
for k,v in checks.items():
    print(f"[{'PASS' if v else 'FAIL'}] {k}")
if failed:
    raise SystemExit(f'VERIFY FAIL: {len(failed)} check(s) failed')
print('VERIFY PASS: PATCH-06 and PATCH-08 landed as intended.')
