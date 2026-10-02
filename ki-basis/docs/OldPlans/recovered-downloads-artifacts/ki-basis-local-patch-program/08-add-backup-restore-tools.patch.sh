#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
[[ -z "$(git status --porcelain)" ]] || { echo "ERROR: clean working tree required." >&2; exit 1; }
mkdir -p ki-basis/scripts
for f in ki-basis/scripts/backup-stack.sh ki-basis/scripts/restore-test-paperless.sh; do [[ ! -e "$f" ]] || { echo "ERROR: $f already exists; refusing overwrite." >&2; exit 1; }; done

cat > ki-basis/scripts/backup-stack.sh <<'SCRIPT'
#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$ROOT"
ENV_FILE="${ENV_FILE:-.env}"
[[ -f "$ENV_FILE" ]] || { echo "Missing $ROOT/$ENV_FILE" >&2; exit 1; }
BACKUP_ROOT="${BACKUP_ROOT:-$HOME/ki-basis-backups}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"; DEST="${1:-$BACKUP_ROOT/$STAMP}"
mkdir -p "$DEST"/{postgres,volumes,hermes,config}
compose(){ docker compose --env-file "$ENV_FILE" "$@"; }
PGUSER="$(grep -E '^POSTGRES_USER=' "$ENV_FILE" | tail -1 | cut -d= -f2- | tr -d '\r' || true)"; PGUSER="${PGUSER:-postgres}"
HELPER_IMAGE="$(docker inspect ki-basis-valkey --format '{{.Config.Image}}')"
apps=(firefly paperless openproject hermes); restarted=0
cleanup(){ if [[ "$restarted" -eq 0 ]]; then compose start "${apps[@]}" >/dev/null 2>&1 || true; restarted=1; fi; }
trap cleanup EXIT

echo "Stopping application writers for bounded snapshot..."
compose stop "${apps[@]}"; sleep 2
compose exec -T postgres pg_dumpall -U "$PGUSER" --globals-only > "$DEST/postgres/globals.sql"
for db in firefly paperless openproject; do compose exec -T postgres pg_dump -U "$PGUSER" -Fc "$db" > "$DEST/postgres/$db.dump"; done
archive_volume(){ local vol="$1" name="$2"; docker run --rm --entrypoint sh -v "$vol:/src:ro" -v "$DEST/volumes:/backup" "$HELPER_IMAGE" -c "tar -C /src -czf /backup/$name.tar.gz ."; }
archive_volume ki-basis-valkey-data valkey_data
archive_volume ki-basis-firefly-upload firefly_upload
archive_volume ki-basis-paperless-data paperless_data
archive_volume ki-basis-paperless-media paperless_media
archive_volume ki-basis-paperless-export paperless_export
archive_volume ki-basis-paperless-consume paperless_consume
archive_volume ki-basis-openproject-assets openproject_assets

docker run --rm --entrypoint sh -v /root/.hermes:/src:ro -v "$DEST/hermes:/backup" "$HELPER_IMAGE" -c "tar -C /src -czf /backup/hermes_state.tar.gz ."
cp compose.yaml "$DEST/config/compose.yaml"; cp .env.example "$DEST/config/.env.example"; cp docker/nginx/default.conf "$DEST/config/nginx-default.conf"; cp docker/postgres/init/01-init-databases.sh "$DEST/config/postgres-init.sh"
cat > "$DEST/BACKUP-COVERAGE.txt" <<'TXT'
Logical DB: PostgreSQL globals, firefly, paperless, openproject.
Filesystem/state: Valkey, Firefly upload, Paperless data/media/export/consume, OpenProject assets, Hermes /root/.hermes.
Config snapshot: compose.yaml, .env.example, nginx config, postgres init.
Excluded: real plaintext ki-basis/.env.
TXT
compose start "${apps[@]}"; restarted=1; trap - EXIT
(cd "$DEST" && find . -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS)
echo "Backup complete: $DEST"
echo "Checksum manifest: $DEST/SHA256SUMS"
SCRIPT

cat > ki-basis/scripts/restore-test-paperless.sh <<'SCRIPT'
#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$ROOT"
BACKUP_DIR="${1:-}"
[[ -n "$BACKUP_DIR" && -d "$BACKUP_DIR" ]] || { echo "Usage: PAPERLESS_API_TOKEN=... PAPERLESS_RESTORE_EXPECT_TITLE=... $0 /path/to/backup" >&2; exit 1; }
BACKUP_DIR="$(realpath "$BACKUP_DIR")"
ENV_FILE="${ENV_FILE:-.env}"; [[ -f "$ENV_FILE" ]] || { echo "Missing $ENV_FILE" >&2; exit 1; }
TOKEN="${PAPERLESS_API_TOKEN:-}"; [[ -n "$TOKEN" ]] || { echo "PAPERLESS_API_TOKEN required." >&2; exit 1; }
EXPECT_TITLE="${PAPERLESS_RESTORE_EXPECT_TITLE:-Antigravity M5 Test Document}"
getenv_file(){ grep -E "^$1=" "$ENV_FILE" | tail -1 | cut -d= -f2- | tr -d '\r'; }
SECRET_KEY="$(getenv_file PAPERLESS_SECRET_KEY)"; [[ -n "$SECRET_KEY" ]] || { echo "PAPERLESS_SECRET_KEY missing from .env" >&2; exit 1; }
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
import os,urllib.request,urllib.parse,json
token=os.environ['TEST_TOKEN']; title=os.environ['EXPECT_TITLE']; headers={'Authorization':'Token '+token}
q=urllib.parse.urlencode({'query':title,'page_size':20}); req=urllib.request.Request('http://127.0.0.1:8000/api/documents/?'+q,headers=headers)
with urllib.request.urlopen(req,timeout=20) as r: data=json.load(r)
matches=[x for x in data.get('results',[]) if x.get('title')==title]; assert matches, f'Restored document not found: {title!r}'
doc_id=matches[0]['id']; req=urllib.request.Request(f'http://127.0.0.1:8000/api/documents/{doc_id}/download/',headers=headers)
with urllib.request.urlopen(req,timeout=30) as r: body=r.read()
assert len(body)>0, 'Metadata restored but physical document download is empty'
print(json.dumps({'id':doc_id,'title':title,'download_bytes':len(body)}))
PY

echo "RESTORE TEST PASS: actual Paperless API + physical document content recovered in disposable restore."
SCRIPT

chmod +x ki-basis/scripts/backup-stack.sh ki-basis/scripts/restore-test-paperless.sh
bash -n ki-basis/scripts/backup-stack.sh
bash -n ki-basis/scripts/restore-test-paperless.sh
git diff --check
echo "PATCH APPLIED LOCALLY. Review added backup/restore tooling before running."
