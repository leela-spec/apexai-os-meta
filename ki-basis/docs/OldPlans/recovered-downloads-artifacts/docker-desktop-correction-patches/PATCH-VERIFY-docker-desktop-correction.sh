#!/usr/bin/env bash
set -euo pipefail
MAIN="${1:-./ki-basis-local-patch-program}"
HERMES="${2:-./hermes-activation-patches}"
fail=0
ok(){ echo "[PASS] $*"; }
bad(){ echo "[FAIL] $*"; fail=$((fail+1)); }
check_grep(){ local label="$1" pat="$2" file="$3"; if grep -Eq "$pat" "$file"; then ok "$label"; else bad "$label"; fi; }
check_not(){ local label="$1" pat="$2" file="$3"; if grep -Eq "$pat" "$file"; then bad "$label"; else ok "$label"; fi; }

check_grep "plan requires Docker Desktop on Windows" 'Docker Desktop installed on Windows' "$MAIN/ENVIRONMENT-CORRECTION-IMPLEMENTATION-PLAN.md"
check_grep "plan requires Hyper-V backend" 'Hyper-V Linux-container backend' "$MAIN/ENVIRONMENT-CORRECTION-IMPLEMENTATION-PLAN.md"
check_grep "plan keeps one target Docker Engine" 'ONE Docker Engine' "$MAIN/ENVIRONMENT-CORRECTION-IMPLEMENTATION-PLAN.md"
check_grep "plan keeps one Compose project" 'ONE Compose project: ki-basis' "$MAIN/ENVIRONMENT-CORRECTION-IMPLEMENTATION-PLAN.md"
check_grep "plan keeps shared network" 'ONE shared bridge network: ki-basis-net' "$MAIN/ENVIRONMENT-CORRECTION-IMPLEMENTATION-PLAN.md"
check_not "generic manually-managed VM fallback removed" 'conventional dedicated Hyper-V Linux VM' "$MAIN/ENVIRONMENT-CORRECTION-IMPLEMENTATION-PLAN.md"
check_grep "README has Windows Docker Desktop gate" '00a-docker-desktop-target-gate.ps1' "$MAIN/README-STEP-BY-STEP.md"
[[ -f "$MAIN/00a-docker-desktop-target-gate.ps1" ]] && ok "PowerShell Docker Desktop gate exists" || bad "PowerShell Docker Desktop gate exists"
check_grep "shell boundary check rejects WSL2 backend" 'microsoft.*WSL.*WSL2|WSL2' "$MAIN/00b-environment-boundary-check.sh"
check_grep "final verification checks Docker Desktop" 'Docker Desktop' "$MAIN/09-final-verification.sh"
check_grep "final verifier checks seven canonical services" 'exactly seven canonical Compose services' "$MAIN/09-final-verification.sh"
check_grep "architecture patch writes Docker Desktop host" 'Windows 11 runs Docker Desktop' "$MAIN/02-architecture-current.patch.sh"
check_grep "Hermes README targets Docker Desktop" 'Windows Docker Desktop target Engine' "$HERMES/README-HERMES-ACTIVATION.md"
check_grep "Hermes remains a service on ki-basis-net" 'one of the seven containers attached to the same `ki-basis-net`' "$HERMES/README-HERMES-ACTIVATION.md"
check_grep "Hermes runtime check rejects WSL2 backend" 'WSL2 backend rather than Hyper-V' "$HERMES/02-hermes-activation-check.sh"

# Non-overcorrection checks: previous correct architecture must still be present.
for token in 'PostgreSQL and Valkey internal-only' 'official upstream images for complex products' 'Alpine where technically appropriate' 'no Docker socket in Hermes' 'secret hardening' 'image pinning' 'backup coverage' 'restore proof'; do
  if grep -Fq "$token" "$MAIN/ENVIRONMENT-CORRECTION-IMPLEMENTATION-PLAN.md"; then ok "preserved: $token"; else bad "preserved: $token"; fi
done

bash -n "$MAIN/00b-environment-boundary-check.sh" || bad "00b bash syntax"
bash -n "$MAIN/02-architecture-current.patch.sh" || bad "02 architecture patch bash syntax"
bash -n "$MAIN/09-final-verification.sh" || bad "09 final verifier bash syntax"
bash -n "$HERMES/02-hermes-activation-check.sh" || bad "Hermes verifier bash syntax"

if [[ "$fail" -eq 0 ]]; then
  echo "DOCKER DESKTOP CORRECTION VERIFY PASS"
else
  echo "DOCKER DESKTOP CORRECTION VERIFY FAILURES=$fail" >&2
  exit 1
fi
