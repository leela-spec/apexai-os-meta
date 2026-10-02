#!/usr/bin/env bash
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "$ROOT" ]]; then echo "ERROR: run inside apexai-os-meta." >&2; exit 1; fi
cd "$ROOT"
echo "Repo: $ROOT"
echo "HEAD: $(git rev-parse HEAD)"
echo "Branch: $(git branch --show-current)"
if [[ -n "$(git status --porcelain)" ]]; then echo "ERROR: working tree is not clean." >&2; git status --short; exit 1; fi
required=(
  "ki-basis/compose.yaml"
  "ki-basis/.env.example"
  "ki-basis/docker/nginx/default.conf"
  "ki-basis/docker/postgres/init/01-init-databases.sh"
  "apex-meta/Alpine/ARCHITEKTUR-BASIS.md"
  "apex-meta/Alpine/ImplementationPlans/00-START-HERE.md"
  "apex-meta/Alpine/ImplementationPlans/01-META-IMPLEMENTATION-PLAN-ANTIGRAVITY.md"
  "apex-meta/Alpine/ImplementationPlans/00-META-IMPLEMENTATION-PLAN.md"
)
for f in "${required[@]}"; do [[ -f "$f" ]] || { echo "ERROR missing: $f" >&2; exit 1; }; done
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'
if [[ -f ki-basis/.env ]]; then
  git ls-files --error-unmatch ki-basis/.env >/dev/null 2>&1 && { echo "ERROR: ki-basis/.env is tracked." >&2; exit 1; } || true
  (cd ki-basis && docker compose --env-file .env config >/dev/null)
  echo "Compose renders with current local .env."
else
  echo "WARNING: ki-basis/.env is missing. Do not apply secret hardening until valid local secrets exist."
fi
echo "PRECHECK PASS"
