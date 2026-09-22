#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
docker --context desktop-linux compose -p ki-basis --project-directory "$ROOT" -f "$ROOT/compose.yaml" --env-file "$ROOT/.env.private" stop
