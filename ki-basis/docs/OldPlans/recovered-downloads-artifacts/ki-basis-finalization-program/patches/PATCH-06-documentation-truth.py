#!/usr/bin/env python3
from pathlib import Path
import re
import sys

if len(sys.argv) != 2:
    raise SystemExit("Usage: PATCH-06-documentation-truth.py <repo-root>")
root = Path(sys.argv[1]).resolve()


def read_preserve(path: Path):
    raw = path.read_bytes()
    bom = raw.startswith(b'\xef\xbb\xbf')
    return raw.decode('utf-8-sig'), bom


def write_preserve(path: Path, text: str, bom: bool):
    data = text.encode('utf-8')
    if bom:
        data = b'\xef\xbb\xbf' + data
    path.write_bytes(data)


def patch(path_rel, transform):
    path = root / path_rel
    if not path.exists():
        raise SystemExit(f"Missing expected file: {path}")
    text, bom = read_preserve(path)
    new = transform(text)
    if new == text:
        print(f"[NOCHANGE] {path_rel}")
    else:
        write_preserve(path, new, bom)
        print(f"[PATCHED] {path_rel}")


def dossier(text: str) -> str:
    # Redact any value on the known Paperless token evidence line without knowing the secret.
    text, n = re.subn(
        r'(\*\*Paperless API Token \(Rotated in C1\)\*\*:\s*)`[^`]*`',
        r'\1`<REDACTED_PAPERLESS_API_TOKEN>`',
        text,
        count=1,
    )
    if n == 0 and '<REDACTED_PAPERLESS_API_TOKEN>' not in text:
        raise SystemExit('Dossier token line not found; refusing broad rewrite.')

    text = text.replace(
        '; No Git Push Performed.',
        '; repository-state claims must be verified against live Git; this dossier is tracked and must not be used as no-push evidence.'
    )
    text = re.sub(
        r'\* \*\*Remote Status\*\*: \*\*NO PUSH ENFORCED\*\*[^\n]*',
        '* **Remote Status**: Historical no-push intent is superseded. Verify current branch/remote state with live Git; this dossier itself is tracked and therefore is not evidence that no push occurred.',
        text,
        count=1,
    )
    text = text.replace(
        '| **9** | Multi-DB pgvector (6 Databases active with pgvector 0.8.6) | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:27-32` |',
        '| **9** | pgvector acceptance scope (current designated/application DB checks; template DBs are not an application requirement) | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:27-32` |'
    )
    return text


def target_report(text: str) -> str:
    text = text.replace(
        '**Requirement**: `pgvector` extension must be loaded and available across all active PostgreSQL databases.',
        '**Requirement**: the pinned PostgreSQL service must be pgvector-capable, and the extension must be verified in the databases required by current workload/acceptance. Template databases are not application acceptance targets.'
    )
    text = text.replace(
        '- Queried databases: `postgres`, `template1`, `template0`, `firefly`, `paperless`, `openproject`.',
        '- Acceptance databases: `postgres`, `firefly`, `paperless`, `openproject`. `template0`/`template1` are not treated as application acceptance targets.'
    )
    old = '- Volume archives: `valkey_data.tar.gz`, `firefly_upload.tar.gz`, `paperless_data.tar.gz`, `paperless_media.tar.gz`, `paperless_export.tar.gz`, `paperless_consume.tar.gz`, `openproject_assets.tar.gz`.'
    new = '- Volume archives: `valkey_data.tar.gz`, `firefly_upload.tar.gz`, `paperless_data.tar.gz`, `paperless_media.tar.gz`, `paperless_export.tar.gz`, `paperless_consume.tar.gz`, `openproject_assets.tar.gz`, `hermes_data.tar.gz`, `hermes_workspaces.tar.gz`.'
    if old in text:
        text = text.replace(old, new, 1)
    elif 'hermes_data.tar.gz' not in text or 'hermes_workspaces.tar.gz' not in text:
        raise SystemExit('Target report volume list changed unexpectedly; refusing broad rewrite.')
    return text


def architecture(text: str) -> str:
    old = '- Integration evidence: [`INTEGRATION-ACCEPTANCE-REPORT.md`](INTEGRATION-ACCEPTANCE-REPORT.md)'
    new = ('- Current target acceptance: [`TARGET-ACCEPTANCE-REPORT.md`](TARGET-ACCEPTANCE-REPORT.md)\n'
           '- Historical pre-migration source evidence: [`INTEGRATION-ACCEPTANCE-REPORT.md`](INTEGRATION-ACCEPTANCE-REPORT.md)')
    if old in text:
        text = text.replace(old, new, 1)
    elif 'TARGET-ACCEPTANCE-REPORT.md' not in text:
        raise SystemExit('Architecture evidence anchor changed unexpectedly; refusing broad rewrite.')
    return text


def old_verification(text: str) -> str:
    marker = '> **Historical snapshot:** This file records an earlier migration verification state. Do not use its branch/head or remote-status statements as current repository authority; verify live Git and use `../TARGET-ACCEPTANCE-REPORT.md` for the current target.\n\n'
    if marker in text:
        return text
    lines = text.splitlines(keepends=True)
    if not lines:
        return text
    # Insert after first heading line, preserving the rest.
    return lines[0] + '\n' + marker + ''.join(lines[1:])

patch('apex-meta/Alpine/HANDOVER-REVIEWER-DOSSIER.md', dossier)
patch('apex-meta/Alpine/TARGET-ACCEPTANCE-REPORT.md', target_report)
patch('apex-meta/Alpine/ARCHITEKTUR-BASIS.md', architecture)
patch('apex-meta/Alpine/Iteration2/VerificationAG.md', old_verification)
print('PATCH-06 COMPLETE: review git diff; no commit or push performed.')
