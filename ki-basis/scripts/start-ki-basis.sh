#!/usr/bin/env bash
# =============================================================================
# start-ki-basis.sh: Dual-Instance Stack Launcher for Linux / WSL2
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
TIMEOUT=90

print_usage() {
    echo "Usage: $0 [-i private|community|all] [-t timeout_seconds]"
    echo "  -i    Target instance: private, community, or all (default: all)"
    echo "  -t    Timeout in seconds for engine/health checks (default: 90)"
    exit 1
}

while getopts "i:t:h" opt; do
    case "$opt" in
        i) INSTANCE="$OPTARG" ;;
        t) TIMEOUT="$OPTARG" ;;
        h|*) print_usage ;;
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

echo "==> Checking Docker engine..."
if ! docker info >/dev/null 2>&1; then
    echo "ERROR: Docker engine is not running or unreachable." >&2
    exit 1
fi

start_stack() {
    local project_name="$1"
    local env_file="$2"
    local nginx_port="$3"

    if [[ ! -f "$env_file" ]]; then
        echo "ERROR: Environment file not found: $env_file" >&2
        exit 1
    fi

    echo ""
    echo "==> Launching stack: $project_name using $env_file..."
    docker compose -p "$project_name" -f "$COMPOSE_FILE" --env-file "$env_file" up -d

    echo "==> Verifying loopback endpoint for $project_name (Nginx :$nginx_port, timeout: ${TIMEOUT}s)..."
    local ready=0
    local max_attempts=$(( (TIMEOUT + 1) / 2 ))
    for ((attempt=1; attempt<=max_attempts; attempt++)); do
        if curl -fs -s -o /dev/null "http://127.0.0.1:${nginx_port}/healthz" 2>/dev/null; then
            ready=1
            break
        fi
        sleep 2
    done

    if [[ "$ready" -eq 1 ]]; then
        echo "[PASS] $project_name reverse proxy is responsive at http://127.0.0.1:${nginx_port}"
    else
        echo "[WARNING] $project_name started, but Nginx /healthz did not respond within ${TIMEOUT}s timeout."
    fi

    docker compose -p "$project_name" -f "$COMPOSE_FILE" --env-file "$env_file" ps
}

if [[ "$INSTANCE" == "private" || "$INSTANCE" == "all" ]]; then
    start_stack "ki-basis-private" "$ENV_PRIVATE" "8084"
fi

if [[ "$INSTANCE" == "community" || "$INSTANCE" == "all" ]]; then
    start_stack "ki-basis-community" "$ENV_COMMUNITY" "9084"
fi

echo ""
echo "==> All requested instances processed successfully."
