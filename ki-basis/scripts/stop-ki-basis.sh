#!/usr/bin/env bash
# =============================================================================
# stop-ki-basis.sh: Dual-Instance Stack Shutdown for Linux / WSL2
# =============================================================================
set -euo pipefail

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
