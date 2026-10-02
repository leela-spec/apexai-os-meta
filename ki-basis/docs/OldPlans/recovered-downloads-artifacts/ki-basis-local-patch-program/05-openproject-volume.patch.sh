#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
[[ -z "$(git status --porcelain)" ]] || { echo "ERROR: clean working tree required." >&2; exit 1; }
docker inspect ki-basis-openproject >/dev/null 2>&1 || { echo "ABORT: live OpenProject unavailable." >&2; exit 2; }
mounts="$(docker inspect ki-basis-openproject --format '{{range .Mounts}}{{println .Name "->" .Destination}}{{end}}')"
echo "$mounts"
if grep -q 'ki-basis-openproject-data' <<<"$mounts"; then echo "ABORT: live OpenProject uses openproject_data." >&2; exit 2; fi
python3 - <<'PY'
from pathlib import Path
p=Path('ki-basis/compose.yaml'); s=p.read_text(encoding='utf-8-sig')
block='  openproject_data:\n    name: ki-basis-openproject-data\n'
if block not in s: raise SystemExit('Expected orphaned openproject_data declaration not found')
p.write_text(s.replace(block,'',1),encoding='utf-8')
PY
! grep -q 'openproject_data' ki-basis/compose.yaml || { echo "ERROR openproject_data still present" >&2; exit 1; }
(cd ki-basis && docker compose --env-file .env config >/dev/null)
git diff --check
echo "PATCH APPLIED LOCALLY. Only unused OpenProject volume declaration removed."
