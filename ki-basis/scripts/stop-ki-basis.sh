#!/usr/bin/env bash
# =============================================================================
# stop-ki-basis.sh: Dual-Instance Stack Shutdown for Linux / WSL2
# =============================================================================
set -euo pipefail

# --- FAIL-CLOSED GUARD (T10 / ADR-002) — added 2026-09-28 -------------------
# SUPERSEDED: this script targets the pre-consolidation compose.yaml (local
# postgres, no shared-db-net) via .env.private/.env.community + project names
# ki-basis-private/community. The LIVE stack runs from compose.shared-db.yaml on
# the single WSL2-native "Apex" engine (ADR-002); running this would recreate the
# private stack onto the retired topology. See FINDINGS-t10-hermes-compose-drift-2026-09-28.md.
echo "REFUSING TO RUN: superseded by ADR-002 (see guard comment / FINDINGS-t10)." >&2
echo "Private (inside WSL2): cd ki-basis && docker compose -f compose.shared-db.yaml --env-file .env.shared-db -p ki-basis up -d   # stop/down to halt" >&2
echo "Community: managed from C:\\GitDev\\lika-community (compose.wsl.yaml --env-file .env.wsl -p community)." >&2
exit 2
# --- end guard -------------------------------------------------------------


INSTANCE="all"
ACTION="stop"

print_usage() {
    cat <<EOF
Usage: $0 [-i private|community|all] [-d]
       $0 [private|community|all]

Options:
  -i, --instance   Target instance: private, community, or all (default: all)
  -d, --down       Tear down containers and network (docker compose down) instead of stop
  -h, --help       Show this help message
EOF
    exit 1
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -i|--instance)
            INSTANCE="$2"
            shift 2
            ;;
        -d|--down)
            ACTION="down"
            shift
            ;;
        -h|--help)
            print_usage
            ;;
        private|community|all)
            INSTANCE="$1"
            shift
            ;;
        *)
            echo "ERROR: Unknown argument: $1" >&2
            print_usage
            ;;
    esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
KI_BASIS_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
COMPOSE_FILE="${KI_BASIS_DIR}/compose.yaml"
ENV_PRIVATE="${KI_BASIS_DIR}/.env.private"
ENV_COMMUNITY="${KI_BASIS_DIR}/.env.community"

if [[ ! -f "$COMPOSE_FILE" ]]; then
    echo "ERROR: Compose file not found at $COMPOSE_FILE" >&2
    exit 1
fi

stop_stack() {
    local project_name="$1"
    local env_file="$2"

    if [[ ! -f "$env_file" ]]; then
        echo "WARNING: Environment file not found: $env_file. Skipping $project_name." >&2
        return 0
    fi

    echo "==> Gracefully ${ACTION}ping stack: $project_name using $env_file..."
    if [[ "$ACTION" == "down" ]]; then
        docker compose -p "$project_name" -f "$COMPOSE_FILE" --env-file "$env_file" down
    else
        docker compose -p "$project_name" -f "$COMPOSE_FILE" --env-file "$env_file" stop
    fi
    echo "[PASS] $project_name containers ${ACTION}ped successfully."
}

if [[ "$INSTANCE" == "private" || "$INSTANCE" == "all" ]]; then
    stop_stack "ki-basis-private" "$ENV_PRIVATE"
fi

if [[ "$INSTANCE" == "community" || "$INSTANCE" == "all" ]]; then
    stop_stack "ki-basis-community" "$ENV_COMMUNITY"
fi

echo ""
echo "==> Requested instances processed successfully."
