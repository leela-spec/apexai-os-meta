#!/usr/bin/env bash
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
ENV_FILE="${ENV_FILE:-.env}"
STRICT_AUTH="${STRICT_AUTH:-0}"
export DOCKER_CONTEXT="${DOCKER_CONTEXT:-default}"
export MSYS_NO_PATHCONV=1
PASS=0; WARN=0; FAIL=0
ok(){ echo "[PASS] $*"; PASS=$((PASS+1)); }
warn(){ echo "[WARN] $*"; WARN=$((WARN+1)); }
fail(){ echo "[FAIL] $*"; FAIL=$((FAIL+1)); }
env_get(){ local key="$1" v; [[ -f "$ENV_FILE" ]] || return 0; v="$(grep -E "^${key}=" "$ENV_FILE" | tail -n1 | cut -d= -f2- || true)"; v="${v%$'\r'}"; v="${v#\"}"; v="${v%\"}"; v="${v#\'}"; v="${v%\'}"; printf '%s' "$v"; }
port_or_default(){ local key="$1" default="$2" v; v="$(env_get "$key")"; [[ -n "$v" ]] && printf '%s' "$v" || printf '%s' "$default"; }
compose(){ if [[ -f "$ENV_FILE" ]]; then docker compose --env-file "$ENV_FILE" "$@"; else docker compose "$@"; fi; }

echo "== ki-basis real seven-service verification =="
compose config >/dev/null 2>&1 && ok "docker compose config" || fail "docker compose config"
check_running(){ local name="$1" state; state="$(docker inspect "$name" --format '{{.State.Status}}' 2>/dev/null || true)"; [[ "$state" == "running" ]] && ok "$name running" || fail "$name state=$state"; }
for c in ki-basis-postgres ki-basis-valkey ki-basis-firefly ki-basis-paperless ki-basis-openproject ki-basis-nginx ki-basis-hermes; do
  check_running "$c"
  if docker inspect "$c" --format '{{json .NetworkSettings.Networks}}' 2>/dev/null | grep -q '"ki-basis-net"'; then
    ok "$c attached to ki-basis-net"
  else
    fail "$c not attached to ki-basis-net"
  fi
done

PGUSER="$(env_get POSTGRES_USER)"; PGUSER="${PGUSER:-postgres}"
PGDB="$(env_get POSTGRES_DB)"; PGDB="${PGDB:-postgres}"
docker exec ki-basis-postgres pg_isready -U "$PGUSER" >/dev/null 2>&1 && ok "PostgreSQL pg_isready" || fail "PostgreSQL pg_isready"
vec="$(docker exec ki-basis-postgres psql -U "$PGUSER" -d "$PGDB" -tAc "SELECT extversion FROM pg_extension WHERE extname='vector';" 2>/dev/null | tr -d '[:space:]' || true)"
[[ -n "$vec" ]] && ok "PostgreSQL pgvector extension ready in designated $PGDB ($vec)" || fail "pgvector extension missing in $PGDB"
pong="$(docker exec ki-basis-valkey valkey-cli ping 2>/dev/null | tr -d '\r\n' || true)"
[[ "$pong" == "PONG" ]] && ok "Valkey PONG" || fail "Valkey PING -> $pong"

FIREFLY_PORT="$(port_or_default FIREFLY_HOST_PORT 8086)"
PAPERLESS_PORT="$(port_or_default PAPERLESS_HOST_PORT 8010)"
OPENPROJECT_PORT="$(port_or_default OPENPROJECT_HOST_PORT 8082)"
NGINX_PORT="$(port_or_default NGINX_HOST_PORT 8084)"
HGW_PORT="$(port_or_default HERMES_GATEWAY_HOST_PORT 8642)"
HDASH_PORT="$(port_or_default HERMES_DASHBOARD_HOST_PORT 9119)"
http_check(){ local label="$1" url="$2" code; code="$(curl -L -sS -m 15 -o /dev/null -w '%{http_code}' "$url" 2>/dev/null | tr -d '\r\n[:space:]' || true)"; [[ "$code" =~ ^[23] ]] && ok "$label HTTP $code" || fail "$label HTTP $code ($url)"; }
http_check "Firefly UI" "http://127.0.0.1:${FIREFLY_PORT}/"
http_check "Paperless UI" "http://127.0.0.1:${PAPERLESS_PORT}/"
http_check "OpenProject health" "http://127.0.0.1:${OPENPROJECT_PORT}/health_checks/default"
http_check "nginx edge /healthz" "http://127.0.0.1:${NGINX_PORT}/healthz"
http_check "nginx edge /" "http://127.0.0.1:${NGINX_PORT}/"
docker exec ki-basis-nginx nginx -t >/dev/null 2>&1 && ok "nginx config syntax" || fail "nginx config syntax"
http_check "Hermes dashboard surface" "http://127.0.0.1:${HDASH_PORT}/"

[[ -z "$(docker port ki-basis-postgres 5432/tcp 2>/dev/null || true)" ]] && ok "PostgreSQL has no host-published 5432" || fail "PostgreSQL 5432 is host-published"
[[ -z "$(docker port ki-basis-valkey 6379/tcp 2>/dev/null || true)" ]] && ok "Valkey has no host-published 6379" || fail "Valkey 6379 is host-published"
if docker inspect ki-basis-hermes --format '{{range .Mounts}}{{println .Source "->" .Destination}}{{end}}' | grep -q '/var/run/docker.sock'; then fail "Hermes has Docker socket mounted"; else ok "Hermes Docker socket absent"; fi
if docker inspect ki-basis-hermes --format '{{range .Mounts}}{{println .Source}}{{end}}' 2>/dev/null | grep -Eq '(/mnt/c|wsl\$|docker-desktop-data)'; then
  fail "Hermes has legacy WSL host bind mounts"
else
  ok "Hermes has no legacy WSL host bind mounts"
fi

if docker exec ki-basis-hermes python - <<'PY' >/dev/null 2>&1
import socket
for host,port in [('firefly',8080),('paperless',8000),('openproject',80),('nginx',80),('postgres',5432),('valkey',6379)]:
    socket.getaddrinfo(host,port)
    with socket.create_connection((host,port),timeout=4): pass
PY
then ok "Hermes execution context resolves/reaches all internal services"; else fail "Hermes execution context Docker DNS/TCP crossing"; fi

FIREFLY_TOKEN="$(env_get FIREFLY_API_TOKEN)"
PAPERLESS_TOKEN="$(env_get PAPERLESS_API_TOKEN)"
OPENPROJECT_KEY="$(env_get OPENPROJECT_API_KEY)"

# Paperless: reject invalid, accept valid
if [[ -n "$PAPERLESS_TOKEN" ]]; then
  if docker exec ki-basis-hermes python - <<'PY' >/dev/null 2>&1
import urllib.request, urllib.error
req = urllib.request.Request('http://paperless:8000/api/documents/?page_size=1', headers={'Authorization': 'Token invalid_token_negative_test_123'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        raise SystemExit(1)
except urllib.error.HTTPError as e:
    assert e.code in (401, 403), f'Expected 401/403, got {e.code}'
PY
  then ok "Hermes -> Paperless rejects invalid token"; else fail "Hermes -> Paperless accepted invalid token"; fi

  if docker exec -e TOKEN="$PAPERLESS_TOKEN" ki-basis-hermes python - <<'PY' >/dev/null 2>&1
import os, urllib.request
r = urllib.request.Request('http://paperless:8000/api/documents/?page_size=1', headers={'Authorization': 'Token ' + os.environ['TOKEN']})
with urllib.request.urlopen(r, timeout=10) as x: assert x.status == 200
PY
  then ok "Hermes -> Paperless authenticated API"; else fail "Hermes -> Paperless authenticated API"; fi
else
  if [[ "$STRICT_AUTH" == "1" ]]; then fail "PAPERLESS_API_TOKEN missing from local .env"; else warn "PAPERLESS_API_TOKEN not set"; fi
fi

# Firefly: reject invalid, accept valid
if [[ -n "$FIREFLY_TOKEN" ]]; then
  if docker exec ki-basis-hermes python - <<'PY' >/dev/null 2>&1
import urllib.request, urllib.error
req = urllib.request.Request('http://firefly:8080/api/v1/about', headers={'Authorization': 'Bearer invalid_token_negative_test_123', 'Accept': 'application/json'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        raise SystemExit(1)
except urllib.error.HTTPError as e:
    assert e.code in (401, 403), f'Expected 401/403, got {e.code}'
PY
  then ok "Hermes -> Firefly rejects invalid token"; else fail "Hermes -> Firefly accepted invalid token"; fi

  if docker exec -e TOKEN="$FIREFLY_TOKEN" ki-basis-hermes python - <<'PY' >/dev/null 2>&1
import os, urllib.request
r = urllib.request.Request('http://firefly:8080/api/v1/about', headers={'Authorization': 'Bearer ' + os.environ['TOKEN'], 'Accept': 'application/json'})
with urllib.request.urlopen(r, timeout=10) as x: assert x.status == 200
PY
  then ok "Hermes -> Firefly authenticated API"; else fail "Hermes -> Firefly authenticated API"; fi
else
  if [[ "$STRICT_AUTH" == "1" ]]; then fail "FIREFLY_API_TOKEN missing from local .env"; else warn "FIREFLY_API_TOKEN not set"; fi
fi

# OpenProject: reject invalid, accept valid
if [[ -n "$OPENPROJECT_KEY" ]]; then
  if docker exec ki-basis-hermes python - <<'PY' >/dev/null 2>&1
import urllib.request, urllib.error, base64
auth = base64.b64encode(b'apikey:invalid_key_negative_test_123').decode()
req = urllib.request.Request('http://openproject:80/api/v3/work_packages?pageSize=1', headers={'Authorization': 'Basic ' + auth})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        raise SystemExit(1)
except urllib.error.HTTPError as e:
    assert e.code in (401, 403), f'Expected 401/403, got {e.code}'
PY
  then ok "Hermes -> OpenProject rejects invalid API key"; else fail "Hermes -> OpenProject accepted invalid API key"; fi

  if docker exec -e KEY="$OPENPROJECT_KEY" ki-basis-hermes python - <<'PY' >/dev/null 2>&1
import os, urllib.request, base64
a = base64.b64encode(('apikey:' + os.environ['KEY']).encode()).decode()
r = urllib.request.Request('http://openproject:80/api/v3/work_packages?pageSize=1', headers={'Authorization': 'Basic ' + a})
with urllib.request.urlopen(r, timeout=10) as x: assert x.status == 200
PY
  then ok "Hermes -> OpenProject authenticated API v3"; else fail "Hermes -> OpenProject authenticated API v3"; fi
else
  if [[ "$STRICT_AUTH" == "1" ]]; then fail "OPENPROJECT_API_KEY missing from local .env"; else warn "OPENPROJECT_API_KEY not set"; fi
fi

if [[ "$STRICT_AUTH" == "1" ]]; then
  if [[ -z "$FIREFLY_TOKEN" || -z "$PAPERLESS_TOKEN" || -z "$OPENPROJECT_KEY" ]]; then
    fail "STRICT_AUTH=1 gate: cannot PASS while any of the three authenticated product checks is skipped"
  fi
fi

echo; echo "Summary: PASS=$PASS WARN=$WARN FAIL=$FAIL"; [[ "$FAIL" -eq 0 ]]