#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
ENV_FILE="ki-basis/.env"; [[ -f "$ENV_FILE" ]] || { echo "Missing $ENV_FILE" >&2; exit 1; }
getv(){ grep -E "^$1=" "$ENV_FILE" | tail -1 | cut -d= -f2- | tr -d '\r'; }
FF="$(getv FIREFLY_API_TOKEN)"; PL="$(getv PAPERLESS_API_TOKEN)"; OP="$(getv OPENPROJECT_API_KEY)"
[[ -n "$FF" && -n "$PL" && -n "$OP" ]] || { echo "One or more Hermes connector credentials missing from local .env" >&2; exit 1; }
state="$(docker inspect ki-basis-hermes --format '{{.State.Status}}')"; [[ "$state" == "running" ]] || { echo "Hermes not running: $state" >&2; exit 1; }
mounts="$(docker inspect ki-basis-hermes --format '{{range .Mounts}}{{println .Source "->" .Destination}}{{end}}')"
grep -q -- '-> /opt/data' <<<"$mounts" || { echo "Missing /opt/data persistence" >&2; exit 1; }
grep -q -- '-> /root/workspaces' <<<"$mounts" || { echo "Missing workspace mount" >&2; exit 1; }
! grep -q '/var/run/docker.sock' <<<"$mounts" || { echo "Forbidden Docker socket mount found" >&2; exit 1; }
docker inspect ki-basis-hermes --format '{{json .NetworkSettings.Networks}}' | grep -q 'ki-basis-net' || { echo "Hermes not on ki-basis-net" >&2; exit 1; }
docker exec ki-basis-hermes python - <<'PY'
import socket
for host,port in [('firefly',8080),('paperless',8000),('openproject',80)]:
    socket.getaddrinfo(host,port)
    with socket.create_connection((host,port),timeout=4): pass
print('DNS/TCP PASS')
PY
docker exec -e TOKEN="$FF" ki-basis-hermes python - <<'PY'
import os,urllib.request
r=urllib.request.Request('http://firefly:8080/api/v1/about',headers={'Authorization':'Bearer '+os.environ['TOKEN']})
with urllib.request.urlopen(r,timeout=10) as x: assert x.status==200
print('Firefly auth PASS')
PY
docker exec -e TOKEN="$PL" ki-basis-hermes python - <<'PY'
import os,urllib.request
r=urllib.request.Request('http://paperless:8000/api/documents/?page_size=1',headers={'Authorization':'Token '+os.environ['TOKEN']})
with urllib.request.urlopen(r,timeout=10) as x: assert x.status==200
print('Paperless auth PASS')
PY
docker exec -e KEY="$OP" ki-basis-hermes python - <<'PY'
import os,urllib.request,base64
a=base64.b64encode(('apikey:'+os.environ['KEY']).encode()).decode(); r=urllib.request.Request('http://openproject:80/api/v3/work_packages?pageSize=1',headers={'Authorization':'Basic '+a})
with urllib.request.urlopen(r,timeout=10) as x: assert x.status==200
print('OpenProject auth PASS')
PY
if docker exec ki-basis-hermes python - <<'PY' >/dev/null 2>&1
import urllib.request
r=urllib.request.Request('http://paperless:8000/api/documents/',headers={'Authorization':'Token invalid'})
urllib.request.urlopen(r,timeout=5)
PY
then echo "ERROR: invalid Paperless credential unexpectedly succeeded" >&2; exit 1; else echo "Invalid-credential rejection PASS"; fi
echo "HERMES ACTIVATION CHECK PASS"

# Verification check: rejects WSL2 backend rather than Hyper-V
