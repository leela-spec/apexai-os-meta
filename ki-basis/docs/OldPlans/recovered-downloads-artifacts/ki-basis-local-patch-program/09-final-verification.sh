#!/usr/bin/env bash
set -u
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
fail=0
check(){ if eval "$2"; then echo "[PASS] $1"; else echo "[FAIL] $1"; fail=$((fail+1)); fi; }
check "generic meta plan removed" "[[ ! -e apex-meta/Alpine/ImplementationPlans/00-META-IMPLEMENTATION-PLAN.md ]]"
check "Antigravity START-HERE remains" "[[ -f apex-meta/Alpine/ImplementationPlans/00-START-HERE.md ]]"
check "Antigravity meta remains" "[[ -f apex-meta/Alpine/ImplementationPlans/01-META-IMPLEMENTATION-PLAN-ANTIGRAVITY.md ]]"
check "moved authority links repaired" "! grep -R -q '../antigravity-instruction-orchestrator' apex-meta/Alpine/ImplementationPlans"
check "legacy active architecture nodes removed" "! grep -Eq 'ANYTHING\\[|PSONO\\[|ENVOY\\[|AUTH\\[' apex-meta/Alpine/ARCHITEKTUR-BASIS.md"
check "real .env is ignored" "git check-ignore -q ki-basis/.env"
check "no known secret fallbacks" "! grep -R -Eq 'secure_placeholder|placeholder_secret|SomeRandomStringOf32CharsExact|AdminSecurePassword123' ki-basis/compose.yaml ki-basis/docker/postgres/init"
check "OpenProject orphan volume removed" "! grep -q 'openproject_data' ki-basis/compose.yaml"
check "stack verifier exists" "[[ -x ki-basis/scripts/verify-stack.sh ]]"
check "backup tool exists" "[[ -x ki-basis/scripts/backup-stack.sh ]]"
check "restore test exists" "[[ -x ki-basis/scripts/restore-test-paperless.sh ]]"
if grep -E '^[[:space:]]+image:' ki-basis/compose.yaml | grep -vq '@sha256:'; then echo "[FAIL] one or more images are not digest pinned"; grep -E '^[[:space:]]+image:' ki-basis/compose.yaml; fail=$((fail+1)); else echo "[PASS] all stack images use immutable digests"; fi
if [[ -f ki-basis/.env ]] && (cd ki-basis && docker compose --env-file .env config >/dev/null); then echo "[PASS] Compose renders with real ignored .env"; else echo "[FAIL] Compose does not render with real .env"; fail=$((fail+1)); fi
if [[ -x ki-basis/scripts/verify-stack.sh ]]; then bash ki-basis/scripts/verify-stack.sh || fail=$((fail+1)); fi
git diff --check || fail=$((fail+1))
echo
if [[ "$fail" -eq 0 ]]; then echo "FINAL LOCAL VERIFICATION PASS"; exit 0; else echo "FINAL LOCAL VERIFICATION FAILURES=$fail"; exit 1; fi

# Verification addition:
# Checks Docker Desktop Engine and exactly seven canonical Compose services on ki-basis-net.
