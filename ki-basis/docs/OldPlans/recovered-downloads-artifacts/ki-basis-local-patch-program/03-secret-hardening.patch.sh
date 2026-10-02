#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
[[ -z "$(git status --porcelain)" ]] || { echo "ERROR: clean working tree required." >&2; exit 1; }
[[ -f ki-basis/.env ]] || { echo "ERROR: working ki-basis/.env missing." >&2; exit 1; }
if git ls-files --error-unmatch ki-basis/.env >/dev/null 2>&1; then echo "ERROR: ki-basis/.env is tracked." >&2; exit 1; fi
python3 - <<'PY'
from pathlib import Path
p=Path('.gitignore'); s=p.read_text(encoding='utf-8-sig'); rule='/ki-basis/.env'
if rule not in s.splitlines():
    if not s.endswith('\n'): s+='\n'
    s+='\n# Local ki-basis runtime secrets\n/ki-basis/.env\n'; p.write_text(s,encoding='utf-8')
p=Path('ki-basis/compose.yaml'); s=p.read_text(encoding='utf-8-sig')
repls={
'${POSTGRES_PASSWORD:-postgres_secure_placeholder_password}':'${POSTGRES_PASSWORD:?POSTGRES_PASSWORD is required}',
'${FIREFLY_DB_PASSWORD:-firefly_secure_placeholder_password}':'${FIREFLY_DB_PASSWORD:?FIREFLY_DB_PASSWORD is required}',
'${PAPERLESS_DB_PASSWORD:-paperless_secure_placeholder_password}':'${PAPERLESS_DB_PASSWORD:?PAPERLESS_DB_PASSWORD is required}',
'${OPENPROJECT_DB_PASSWORD:-openproject_secure_placeholder_password}':'${OPENPROJECT_DB_PASSWORD:?OPENPROJECT_DB_PASSWORD is required}',
'${FIREFLY_APP_KEY:-SomeRandomStringOf32CharsExact!!}':'${FIREFLY_APP_KEY:?FIREFLY_APP_KEY is required}',
'${PAPERLESS_SECRET_KEY:-paperless_placeholder_secret_key_change_me}':'${PAPERLESS_SECRET_KEY:?PAPERLESS_SECRET_KEY is required}',
'${PAPERLESS_ADMIN_PASSWORD:-AdminSecurePassword123!}':'${PAPERLESS_ADMIN_PASSWORD:?PAPERLESS_ADMIN_PASSWORD is required}',
'${OPENPROJECT_SECRET_KEY_BASE:-openproject_placeholder_secret_key_base_change_me}':'${OPENPROJECT_SECRET_KEY_BASE:?OPENPROJECT_SECRET_KEY_BASE is required}',
'${HERMES_DASHBOARD_BASIC_AUTH_PASSWORD:-hermes_secure_placeholder_password}':'${HERMES_DASHBOARD_BASIC_AUTH_PASSWORD:?HERMES_DASHBOARD_BASIC_AUTH_PASSWORD is required}',
}
for old,new in repls.items():
    if old not in s: raise SystemExit(f'Expected Compose fallback not found: {old}')
    s=s.replace(old,new)
p.write_text(s,encoding='utf-8')
p=Path('ki-basis/docker/postgres/init/01-init-databases.sh'); s=p.read_text(encoding='utf-8-sig')
for old,new in {
'${FIREFLY_DB_PASSWORD:-firefly_secure_placeholder_password}':'${FIREFLY_DB_PASSWORD:?FIREFLY_DB_PASSWORD is required}',
'${PAPERLESS_DB_PASSWORD:-paperless_secure_placeholder_password}':'${PAPERLESS_DB_PASSWORD:?PAPERLESS_DB_PASSWORD is required}',
'${OPENPROJECT_DB_PASSWORD:-openproject_secure_placeholder_password}':'${OPENPROJECT_DB_PASSWORD:?OPENPROJECT_DB_PASSWORD is required}',
}.items():
    if old not in s: raise SystemExit(f'Expected init fallback not found: {old}')
    s=s.replace(old,new)
p.write_text(s,encoding='utf-8')
p=Path('ki-basis/.env.example'); s=p.read_text(encoding='utf-8-sig')
secret_keys={'POSTGRES_PASSWORD','FIREFLY_DB_PASSWORD','FIREFLY_APP_KEY','PAPERLESS_DB_PASSWORD','PAPERLESS_SECRET_KEY','PAPERLESS_ADMIN_PASSWORD','OPENPROJECT_DB_PASSWORD','OPENPROJECT_SECRET_KEY_BASE','HERMES_DASHBOARD_BASIC_AUTH_PASSWORD'}
out=[]
for line in s.splitlines():
    key=line.split('=',1)[0] if '=' in line else None
    out.append(f'{key}=' if key in secret_keys else line)
s='\n'.join(out)+'\n'
s=s.replace('# NEVER COMMIT REAL SECRETS TO VERSION CONTROL.','# NEVER COMMIT REAL SECRETS TO VERSION CONTROL.\n# Required secret values are intentionally blank. Fill them only in ignored ki-basis/.env.')
p.write_text(s,encoding='utf-8')
PY
git check-ignore -q ki-basis/.env || { echo "ERROR .env still not ignored" >&2; exit 1; }
(cd ki-basis && docker compose --env-file .env config >/dev/null)
! grep -R -nE 'secure_placeholder|placeholder_secret|SomeRandomStringOf32CharsExact|AdminSecurePassword123' ki-basis/compose.yaml ki-basis/docker/postgres/init >/dev/null || { echo "ERROR known runtime secret fallback remains" >&2; exit 1; }
git diff --check
echo "PATCH APPLIED LOCALLY. Real .env preserved."
