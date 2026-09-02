#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$ROOT"
BACKUP_DIR="${1:-}"
[[ -n "$BACKUP_DIR" && -d "$BACKUP_DIR" ]] || { echo "Usage: PAPERLESS_API_TOKEN=... PAPERLESS_RESTORE_EXPECT_TITLE=... $0 /path/to/backup" >&2; exit 1; }
BACKUP_DIR="$(realpath "$BACKUP_DIR")"
ENV_FILE="${ENV_FILE:-.env}"
if [[ ! -f "$ENV_FILE" && -f ".env.example" ]]; then
  ENV_FILE=".env.example"
fi
[[ -f "$ENV_FILE" ]] || { echo "Missing $ENV_FILE" >&2; exit 1; }
export DOCKER_API_VERSION="${DOCKER_API_VERSION:-1.47}"
export MSYS_NO_PATHCONV=1
TOKEN="${PAPERLESS_API_TOKEN:-}"; [[ -n "$TOKEN" ]] || { echo "PAPERLESS_API_TOKEN required." >&2; exit 1; }
EXPECT_TITLE="${PAPERLESS_RESTORE_EXPECT_TITLE:-Antigravity M5 Test Document}"
getenv_file(){ grep -E "^$1=" "$ENV_FILE" | tail -1 | cut -d= -f2- | tr -d '\r'; }
SECRET_KEY="${PAPERLESS_SECRET_KEY:-$(getenv_file PAPERLESS_SECRET_KEY)}"
[[ -n "$SECRET_KEY" ]] || { echo "PAPERLESS_SECRET_KEY required and cannot be empty (fail-closed)." >&2; exit 1; }

for f in "$BACKUP_DIR/postgres/paperless.dump" "$BACKUP_DIR/volumes/paperless_data.tar.gz" "$BACKUP_DIR/volumes/paperless_media.tar.gz" "$BACKUP_DIR/volumes/paperless_export.tar.gz" "$BACKUP_DIR/volumes/paperless_consume.tar.gz"; do [[ -f "$f" ]] || { echo "Missing backup artifact: $f" >&2; exit 1; }; done
SUFFIX="$(date +%s)-$$"; NET="kb-restore-$SUFFIX"; PG="kb-restore-pg-$SUFFIX"; VK="kb-restore-vk-$SUFFIX"; PL="kb-restore-paperless-$SUFFIX"
V_DATA="kb-restore-paperless-data-$SUFFIX"; V_MEDIA="kb-restore-paperless-media-$SUFFIX"; V_EXPORT="kb-restore-paperless-export-$SUFFIX"; V_CONSUME="kb-restore-paperless-consume-$SUFFIX"
PGPASS="restore-only-$SUFFIX"; APPDBPASS="restore-app-$SUFFIX"
PG_IMAGE="$(docker inspect ki-basis-postgres --format '{{.Config.Image}}')"; VK_IMAGE="$(docker inspect ki-basis-valkey --format '{{.Config.Image}}')"; PL_IMAGE="$(docker inspect ki-basis-paperless --format '{{.Config.Image}}')"; HELPER_IMAGE="$VK_IMAGE"
cleanup(){ docker rm -f "$PL" "$VK" "$PG" >/dev/null 2>&1 || true; docker network rm "$NET" >/dev/null 2>&1 || true; docker volume rm "$V_DATA" "$V_MEDIA" "$V_EXPORT" "$V_CONSUME" >/dev/null 2>&1 || true; }
trap cleanup EXIT
docker network create "$NET" >/dev/null
for v in "$V_DATA" "$V_MEDIA" "$V_EXPORT" "$V_CONSUME"; do docker volume create "$v" >/dev/null; done
docker run -d --name "$PG" --network "$NET" -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD="$PGPASS" -e POSTGRES_DB=postgres "$PG_IMAGE" >/dev/null
for _ in $(seq 1 60); do docker exec "$PG" pg_isready -U postgres >/dev/null 2>&1 && break; sleep 1; done
docker exec "$PG" pg_isready -U postgres >/dev/null
docker exec "$PG" psql -U postgres -d postgres -v ON_ERROR_STOP=1 -c "CREATE USER paperless_app WITH PASSWORD '$APPDBPASS';" -c "CREATE DATABASE paperless OWNER paperless_app;" >/dev/null
cat "$BACKUP_DIR/postgres/paperless.dump" | docker exec -i "$PG" pg_restore -U postgres -d paperless --no-owner --no-privileges
restore_volume(){ local vol="$1" tarfile="$2"; docker run --rm --entrypoint sh -v "$vol:/dst" -v "$BACKUP_DIR/volumes:/backup:ro" "$HELPER_IMAGE" -c "rm -rf /dst/* /dst/.[!.]* /dst/..?* 2>/dev/null || true; tar -C /dst -xzf /backup/$tarfile"; }
restore_volume "$V_DATA" paperless_data.tar.gz; restore_volume "$V_MEDIA" paperless_media.tar.gz; restore_volume "$V_EXPORT" paperless_export.tar.gz; restore_volume "$V_CONSUME" paperless_consume.tar.gz
docker run -d --name "$VK" --network "$NET" "$VK_IMAGE" >/dev/null
docker run -d --name "$PL" --network "$NET" -e PAPERLESS_REDIS="redis://$VK:6379" -e PAPERLESS_DBENGINE=postgresql -e PAPERLESS_DBHOST="$PG" -e PAPERLESS_DBPORT=5432 -e PAPERLESS_DBNAME=paperless -e PAPERLESS_DBUSER=paperless_app -e PAPERLESS_DBPASS="$APPDBPASS" -e PAPERLESS_SECRET_KEY="$SECRET_KEY" -e PAPERLESS_TIME_ZONE=Europe/Berlin -v "$V_DATA:/usr/src/paperless/data" -v "$V_MEDIA:/usr/src/paperless/media" -v "$V_EXPORT:/usr/src/paperless/export" -v "$V_CONSUME:/usr/src/paperless/consume" "$PL_IMAGE" >/dev/null
for _ in $(seq 1 120); do if docker exec "$PL" python - <<'PY' >/dev/null 2>&1
import urllib.request
try: urllib.request.urlopen('http://127.0.0.1:8000/',timeout=2)
except Exception as e:
    if 'Connection refused' in str(e): raise
PY
then break; fi; sleep 2; done

docker exec -e TEST_TOKEN="$TOKEN" -e EXPECT_TITLE="$EXPECT_TITLE" "$PL" python - <<'PY'
import os,urllib.request,urllib.parse,json,hashlib
token=os.environ['TEST_TOKEN']; title=os.environ['EXPECT_TITLE']; headers={'Authorization':'Token '+token}
q=urllib.parse.urlencode({'query':title,'page_size':20}); req=urllib.request.Request('http://127.0.0.1:8000/api/documents/?'+q,headers=headers)
with urllib.request.urlopen(req,timeout=20) as r: data=json.load(r)
matches=[x for x in data.get('results',[]) if x.get('title')==title]; assert matches, f'Restored document not found: {title!r}'
doc_id=matches[0]['id']; req=urllib.request.Request(f'http://127.0.0.1:8000/api/documents/{doc_id}/download/',headers=headers)
with urllib.request.urlopen(req,timeout=30) as r: body=r.read()
assert len(body)>0, 'Metadata restored but physical document download is empty'
sha256 = hashlib.sha256(body).hexdigest()
print(json.dumps({'id':doc_id,'title':title,'download_bytes':len(body),'sha256':sha256}))
PY

echo "RESTORE TEST PASS: actual Paperless API + physical document content and SHA256 verified in disposable restore."