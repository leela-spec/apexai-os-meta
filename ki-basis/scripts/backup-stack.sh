#!/usr/bin/env bash
# =============================================================================
# backup-stack.sh: Dual-Instance Backup Engine for ki-basis
# Supports: -i private | community | all (or positional argument)
# Strictly uses docker exec -i (no pseudo-TTY) to prevent binary dump corruption.
# =============================================================================
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

export MSYS_NO_PATHCONV=1

BACKUP_ROOT="${BACKUP_ROOT:-$HOME/ki-basis-backups}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
TARGET_INSTANCE="all"
CUSTOM_DEST=""

print_usage() {
    cat <<EOF
Usage: $0 [-i private|community|all] [-d destination_dir]
       $0 [private|community|all] [destination_dir]

Options:
  -i, --instance     Target instance: private, community, or all (default: all)
  -d, --destination  Custom backup destination directory (single-instance only)
  -h, --help         Show this help message
EOF
}

# Parse flags and positional arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        -i|--instance)
            TARGET_INSTANCE="$2"
            shift 2
            ;;
        -d|--destination)
            CUSTOM_DEST="$2"
            shift 2
            ;;
        -h|--help)
            print_usage
            exit 0
            ;;
        private|community|all)
            TARGET_INSTANCE="$1"
            shift
            ;;
        *)
            if [[ -z "$CUSTOM_DEST" ]]; then
                CUSTOM_DEST="$1"
                shift
            else
                echo "ERROR: Unknown argument: $1" >&2
                print_usage
                exit 1
            fi
            ;;
    esac
done

backup_instance() {
    local instance="$1"
    local project_name="ki-basis-${instance}"
    local env_file=".env.${instance}"

    if [[ ! -f "$env_file" ]]; then
        echo "ERROR: Environment file not found: $ROOT/$env_file" >&2
        return 1
    fi

    local dest
    if [[ -n "$CUSTOM_DEST" && "$TARGET_INSTANCE" != "all" ]]; then
        dest="$CUSTOM_DEST"
    else
        dest="${BACKUP_ROOT}/${project_name}/${STAMP}"
    fi

    echo ""
    echo "========================================================================"
    echo "Starting backup for instance: ${instance} (${project_name})"
    echo "Destination: ${dest}"
    echo "========================================================================"

    mkdir -p "$dest"/{postgres,volumes,hermes,config}

    # Extract database user
    local pguser
    pguser="$(grep -E '^POSTGRES_USER=' "$env_file" | tail -1 | cut -d= -f2- | tr -d '\r' || true)"
    pguser="${pguser:-postgres}"

    # Determine helper image for volume extraction
    local helper_image
    helper_image="$(docker inspect "${project_name}-valkey" --format '{{.Config.Image}}' 2>/dev/null | tr -d '\r\n' || true)"
    if [[ -z "$helper_image" ]]; then
        helper_image="$(docker inspect "${project_name}-postgres" --format '{{.Config.Image}}' 2>/dev/null | tr -d '\r\n' || true)"
    fi
    helper_image="${helper_image:-alpine:3.20}"

    local apps=(
        "${project_name}-firefly"
        "${project_name}-paperless"
        "${project_name}-openproject"
        "${project_name}-hermes"
    )

    local restarted=0
    cleanup_instance() {
        if [[ "$restarted" -eq 0 ]]; then
            echo "Restarting application writers after backup interrupt/failure..."
            docker start "${apps[@]}" >/dev/null 2>&1 || true
            restarted=1
        fi
    }
    trap cleanup_instance EXIT

    echo "==> Quiescing application writers for bounded snapshot..."
    docker stop "${apps[@]}" 2>/dev/null || true
    sleep 2

    echo "==> Dumping PostgreSQL logical cluster (globals)..."
    # STRICT INVARIANT: -i only, strictly NO -t to prevent PTY CRLF stream corruption
    docker exec -i "${project_name}-postgres" pg_dumpall -U "$pguser" --globals-only > "$dest/postgres/globals.sql"

    echo "==> Dumping individual PostgreSQL databases (-Fc custom binary format)..."
    for db in firefly paperless openproject; do
        echo "    Dumping database: $db..."
        docker exec -i "${project_name}-postgres" pg_dump -U "$pguser" -Fc "$db" > "$dest/postgres/${db}.dump"
    done

    archive_vol() {
        local vol_name="$1"
        local archive_name="$2"
        local archive_file="$dest/volumes/${archive_name}.tar.gz"
        local -a tar_args=()

        if [[ "$archive_name" == "hermes_data" ]]; then
            tar_args+=(--exclude=./.env)
        fi

        if docker volume inspect "$vol_name" >/dev/null 2>&1; then
            echo "    Archiving volume: ${vol_name} -> ${archive_name}.tar.gz..."
            docker run --rm -i --entrypoint sh -v "${vol_name}:/src:ro" "$helper_image" \
                -c 'tar -cz -C /src "$@" .' sh "${tar_args[@]}" > "$archive_file"
            
            if [[ ! -s "$archive_file" ]]; then
                echo "ERROR: Archive is missing or empty: $archive_file" >&2
                return 1
            fi
            tar -tzf "$archive_file" >/dev/null
        else
            echo "    [SKIP] Volume ${vol_name} does not exist on host."
        fi
    }

    echo "==> Archiving persistent named volumes..."
    archive_vol "${project_name}-valkey-data" "valkey_data"
    archive_vol "${project_name}-firefly-upload" "firefly_upload"
    archive_vol "${project_name}-paperless-data" "paperless_data"
    archive_vol "${project_name}-paperless-media" "paperless_media"
    archive_vol "${project_name}-paperless-export" "paperless_export"
    archive_vol "${project_name}-paperless-consume" "paperless_consume"
    archive_vol "${project_name}-openproject-assets" "openproject_assets"
    archive_vol "${project_name}-hermes-data" "hermes_data"
    archive_vol "${project_name}-hermes-workspaces" "hermes_workspaces"

    echo "==> Capturing configuration snapshot..."
    cp compose.yaml "$dest/config/compose.yaml"
    cp .env.example "$dest/config/.env.example"
    cp "$env_file" "$dest/config/${env_file}.sanitized"
    sed -i -E 's/(PASSWORD|SECRET|KEY)=.*/\1=[REDACTED_FOR_SECURITY]/' "$dest/config/${env_file}.sanitized" 2>/dev/null || true
    cp docker/nginx/default.conf "$dest/config/nginx-default.conf"
    cp docker/postgres/init/01-init-databases.sh "$dest/config/postgres-init.sh"

    cat > "$dest/BACKUP-COVERAGE.txt" <<TXT
Instance: ${instance}
Project Namespace: ${project_name}
Timestamp: ${STAMP}
Logical DB: PostgreSQL globals, firefly, paperless, openproject (via docker exec -i, no -t).
Persistent Volumes: Valkey, Firefly upload, Paperless data/media/export/consume, OpenProject assets, Hermes data (/opt/data), Hermes workspaces (/root/workspaces).
Config Snapshot: compose.yaml, .env.example, ${env_file} (credentials redacted), nginx config, postgres init.
TXT

    echo "==> Restarting application writers..."
    docker start "${apps[@]}" >/dev/null 2>&1 || true
    restarted=1
    trap - EXIT

    echo "==> Generating SHA256 integrity manifest..."
    (cd "$dest" && find . -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS)

    echo "[SUCCESS] Backup complete for ${instance}: $dest"
    echo "Manifest: $dest/SHA256SUMS"
}

if [[ "$TARGET_INSTANCE" == "private" || "$TARGET_INSTANCE" == "all" ]]; then
    backup_instance "private"
fi

if [[ "$TARGET_INSTANCE" == "community" || "$TARGET_INSTANCE" == "all" ]]; then
    backup_instance "community"
fi

echo ""
echo "==> All requested backups completed successfully."
