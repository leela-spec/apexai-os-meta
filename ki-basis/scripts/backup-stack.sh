#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$ROOT"
ENV_FILE="${ENV_FILE:-.env}"
if [[ ! -f "$ENV_FILE" && -f ".env.example" ]]; then
  ENV_FILE=".env.example"
fi
[[ -f "$ENV_FILE" ]] || { echo "Missing $ROOT/$ENV_FILE" >&2; exit 1; }
BACKUP_ROOT="${BACKUP_ROOT:-$HOME/ki-basis-backups}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"; DEST="${1:-$BACKUP_ROOT/$STAMP}"
mkdir -p "$DEST"/{postgres,volumes,hermes,config}
export MSYS_NO_PATHCONV=1
compose(){ docker compose --env-file "$ENV_FILE" "$@"; }
PGUSER="$(grep -E '^POSTGRES_USER=' "$ENV_FILE" | tail -1 | cut -d= -f2- | tr -d '\r' || true)"; PGUSER="${PGUSER:-postgres}"
HELPER_IMAGE="$(docker inspect ki-basis-valkey --format '{{.Config.Image}}')"
apps=(firefly paperless openproject hermes); restarted=0
cleanup(){ if [[ "$restarted" -eq 0 ]]; then compose start "${apps[@]}" >/dev/null 2>&1 || true; restarted=1; fi; }
trap cleanup EXIT

echo "Stopping application writers for bounded snapshot..."
docker stop ki-basis-hermes ki-basis-firefly ki-basis-paperless ki-basis-openproject; sleep 2
docker exec -i=false ki-basis-postgres pg_dumpall -U "$PGUSER" --globals-only > "$DEST/postgres/globals.sql"
for db in firefly paperless openproject; do docker exec -i=false ki-basis-postgres pg_dump -U "$PGUSER" -Fc "$db" > "$DEST/postgres/$db.dump"; done
archive_volume(){ local vol="$1" name="$2"; docker run --rm -i=false -v "$vol:/src:ro" "$HELPER_IMAGE" sh -c "tar -cz -C /src --warning=no-file-changed . 2>/dev/null || tar -cz -C /src . 2>/dev/null || true" > "$DEST/volumes/$name.tar.gz"; }
archive_volume ki-basis-valkey-data valkey_data
archive_volume ki-basis-firefly-upload firefly_upload
archive_volume ki-basis-paperless-data paperless_data
archive_volume ki-basis-paperless-media paperless_media
archive_volume ki-basis-paperless-export paperless_export
archive_volume ki-basis-paperless-consume paperless_consume
archive_volume ki-basis-openproject-assets openproject_assets
archive_volume ki-basis-hermes-data hermes_data
archive_volume ki-basis-hermes-workspaces hermes_workspaces

cp compose.yaml "$DEST/config/compose.yaml"; cp .env.example "$DEST/config/.env.example"; cp docker/nginx/default.conf "$DEST/config/nginx-default.conf"; cp docker/postgres/init/01-init-databases.sh "$DEST/config/postgres-init.sh"
cat > "$DEST/BACKUP-COVERAGE.txt" <<'TXT'
Logical DB: PostgreSQL globals, firefly, paperless, openproject.
Filesystem/state: Valkey, Firefly upload, Paperless data/media/export/consume, OpenProject assets, Hermes ki-basis-hermes-data (/opt/data), Hermes ki-basis-hermes-workspaces (/root/workspaces).
Config snapshot: compose.yaml, .env.example, nginx config, postgres init.
Excluded: real plaintext ki-basis/.env.
TXT
docker start ki-basis-openproject ki-basis-firefly ki-basis-paperless ki-basis-hermes; restarted=1; trap - EXIT
(cd "$DEST" && find . -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS)
echo "Backup complete: $DEST"
echo "Checksum manifest: $DEST/SHA256SUMS"