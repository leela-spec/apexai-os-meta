#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
[[ -z "$(git status --porcelain)" ]] || { echo "ERROR: clean working tree required." >&2; exit 1; }
python3 - <<'PY'
from pathlib import Path
p=Path('ki-basis/.env.example'); s=p.read_text(encoding='utf-8-sig')
if '# Hermes AI Operating Surface' not in s: raise SystemExit('Hermes env section not found')
for key in ['FIREFLY_API_TOKEN','PAPERLESS_API_TOKEN','OPENPROJECT_API_KEY']:
    if f'{key}=' not in s: s += f'{key}=\n'
p.write_text(s,encoding='utf-8')
p=Path('ki-basis/compose.yaml'); s=p.read_text(encoding='utf-8-sig')
anchor='      OPENPROJECT_API_URL: http://openproject:80\n'
if anchor not in s: raise SystemExit('Hermes API URL anchor not found')
addition='      FIREFLY_API_TOKEN: ${FIREFLY_API_TOKEN:-}\n      PAPERLESS_API_TOKEN: ${PAPERLESS_API_TOKEN:-}\n      OPENPROJECT_API_KEY: ${OPENPROJECT_API_KEY:-}\n'
if '      FIREFLY_API_TOKEN:' not in s: s=s.replace(anchor,anchor+addition)
p.write_text(s,encoding='utf-8')
PY
git diff --check
echo "PATCH APPLIED LOCALLY. Put real tokens only in ignored ki-basis/.env, then recreate Hermes."
