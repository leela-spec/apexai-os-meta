#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
[[ -z "$(git status --porcelain)" ]] || { echo "ERROR: clean working tree required." >&2; exit 1; }
tmp8642="$(mktemp)"; tmp9119="$(mktemp)"; trap 'rm -f "$tmp8642" "$tmp9119"' EXIT
code8642="$(curl -sS -m 5 -o "$tmp8642" -w '%{http_code}' http://127.0.0.1:8642/ || true)"
code9119="$(curl -sS -m 5 -o "$tmp9119" -w '%{http_code}' http://127.0.0.1:9119/ || true)"
echo "8642 HTTP $code8642: $(tr '\n' ' ' < "$tmp8642" | head -c 180)"; echo
echo "9119 HTTP $code9119: $(tr '\n' ' ' < "$tmp9119" | head -c 180)"; echo
dash8642=0; dash9119=0
grep -Eqi 'dashboard|<html|<!doctype|<title' "$tmp8642" && dash8642=1 || true
grep -Eqi 'dashboard|<html|<!doctype|<title' "$tmp9119" && dash9119=1 || true
if [[ "$dash8642" -eq 1 && "$dash9119" -eq 0 ]]; then echo "ABORT: live evidence suggests 8642 is dashboard." >&2; exit 2; fi
if [[ "$dash9119" -eq 0 && "${FORCE_HERMES_LABEL_PATCH:-0}" != "1" ]]; then
  echo "ABORT: ambiguous. Manually confirm 8642=gateway and 9119=dashboard, then rerun with FORCE_HERMES_LABEL_PATCH=1" >&2; exit 2
fi
python3 - <<'PY'
from pathlib import Path
p=Path('ki-basis/.env.example'); s=p.read_text(encoding='utf-8-sig')
old='HERMES_DASHBOARD_HOST_PORT=8642\nHERMES_GATEWAY_HOST_PORT=9119'; new='HERMES_GATEWAY_HOST_PORT=8642\nHERMES_DASHBOARD_HOST_PORT=9119'
if old not in s: raise SystemExit('Expected old Hermes labels not found in .env.example')
p.write_text(s.replace(old,new),encoding='utf-8')
p=Path('ki-basis/compose.yaml'); s=p.read_text(encoding='utf-8-sig')
old1='"127.0.0.1:${HERMES_DASHBOARD_HOST_PORT:-8642}:8642"'; old2='"127.0.0.1:${HERMES_GATEWAY_HOST_PORT:-9119}:9119"'
if old1 not in s or old2 not in s: raise SystemExit('Expected old Compose labels not found')
s=s.replace(old1,'"127.0.0.1:${HERMES_GATEWAY_HOST_PORT:-8642}:8642"').replace(old2,'"127.0.0.1:${HERMES_DASHBOARD_HOST_PORT:-9119}:9119"')
p.write_text(s,encoding='utf-8')
p=Path('ki-basis/docker/nginx/default.conf'); s=p.read_text(encoding='utf-8-sig')
old='<li><a href="http://127.0.0.1:8642">Hermes Dashboard (AI) — :8642</a></li>'
new='<li><a href="http://127.0.0.1:8642">Hermes Gateway/API (AI) — :8642</a></li><li><a href="http://127.0.0.1:9119">Hermes Dashboard (AI) — :9119</a></li>'
if old not in s: raise SystemExit('Expected nginx Hermes label not found')
p.write_text(s.replace(old,new),encoding='utf-8')
PY
git diff --check
echo "PATCH APPLIED LOCALLY. Physical ports unchanged; labels corrected."
