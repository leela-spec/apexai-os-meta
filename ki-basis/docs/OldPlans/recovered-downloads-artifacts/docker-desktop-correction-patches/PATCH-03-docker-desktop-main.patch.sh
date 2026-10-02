#!/usr/bin/env bash
set -euo pipefail
TARGET_DIR="${1:-./ki-basis-local-patch-program}"
[[ -d "$TARGET_DIR" ]] || { echo "ERROR: main corrected bundle directory not found: $TARGET_DIR" >&2; exit 2; }
for f in README-STEP-BY-STEP.md 02-architecture-current.patch.sh 09-final-verification.sh; do
  [[ -f "$TARGET_DIR/$f" ]] || { echo "ERROR: expected file missing: $TARGET_DIR/$f" >&2; exit 3; }
done

python3 - "$TARGET_DIR" <<'PY'
from pathlib import Path
import sys
root = Path(sys.argv[1])

# 1. ENVIRONMENT-CORRECTION-IMPLEMENTATION-PLAN.md
p = root / "ENVIRONMENT-CORRECTION-IMPLEMENTATION-PLAN.md"
plan_content = """# Environment Correction Implementation Plan — ki-basis

**Target runtime:** Docker Desktop installed on Windows, using its WSL-independent Hyper-V Linux-container backend as the single ki-basis Docker Engine.

```text
Windows 11
└── Docker Desktop for Windows
    └── Hyper-V Linux-container backend
        └── ONE Docker Engine
            └── ONE Compose project: ki-basis
                └── ONE shared bridge network: ki-basis-net
                    ├── nginx
                    ├── postgres + pgvector
                    ├── valkey
                    ├── firefly
                    ├── paperless
                    ├── openproject
                    └── hermes
```

## Preserved architecture rules
- PostgreSQL and Valkey internal-only
- official upstream images for complex products
- Alpine where technically appropriate
- no Docker socket in Hermes
- secret hardening
- image pinning
- backup coverage
- restore proof

## Execution Steps
1. Install Docker Desktop on Windows.
2. Select Linux containers and Hyper-V backend.
3. Run `00a-docker-desktop-target-gate.ps1 -SourceEngineId <source-engine-id>`.
4. Run `00b-environment-boundary-check.sh <source-engine-id>`.
"""
p.write_text(plan_content, encoding="utf-8")

# 2. README-STEP-BY-STEP.md
p = root / "README-STEP-BY-STEP.md"
s = p.read_text(encoding="utf-8-sig")
if "00a-docker-desktop-target-gate.ps1" not in s:
    s += """

## Docker Desktop Gate Verification
Run `00a-docker-desktop-target-gate.ps1` from PowerShell to verify Docker Desktop target Engine and Hyper-V backend configuration.
"""
p.write_text(s, encoding="utf-8")

# 3. 02-architecture-current.patch.sh
p = root / "02-architecture-current.patch.sh"
s = p.read_text(encoding="utf-8-sig")
if "Windows 11 runs Docker Desktop" not in s:
    s += """
# > **Host boundary:** Windows 11 runs Docker Desktop. Docker Desktop uses its WSL-independent Hyper-V Linux-container backend.
"""
p.write_text(s, encoding="utf-8")

# 4. 00b-environment-boundary-check.sh
p = root / "00b-environment-boundary-check.sh"
check_content = """#!/usr/bin/env bash
set -euo pipefail
SOURCE_ENGINE_ID="${1:-}"
[[ -n "$SOURCE_ENGINE_ID" ]] || { echo "ERROR: source engine ID required" >&2; exit 1; }

TARGET_ENGINE_ID="$(docker info --format '{{.ID}}' 2>/dev/null || true)"
TARGET_OS_TYPE="$(docker info --format '{{.OSType}}' 2>/dev/null || true)"
TARGET_KERNEL="$(docker info --format '{{.KernelVersion}}' 2>/dev/null || true)"
TARGET_OPERATING_SYSTEM="$(docker info --format '{{.OperatingSystem}}' 2>/dev/null || true)"

[[ -n "$TARGET_ENGINE_ID" ]] || { echo "ERROR: target Docker Engine ID unavailable" >&2; exit 4; }
if [[ "$TARGET_ENGINE_ID" == "$SOURCE_ENGINE_ID" ]]; then
  echo "ERROR: target Docker Engine is the same Engine as the recorded WSL source." >&2
  exit 5
fi
[[ "$TARGET_OS_TYPE" == "linux" ]] || { echo "ERROR: target is not in Linux-container mode: $TARGET_OS_TYPE" >&2; exit 6; }
grep -qi 'Docker Desktop' <<<"$TARGET_OPERATING_SYSTEM" || { echo "ERROR: target Engine does not identify as Docker Desktop: $TARGET_OPERATING_SYSTEM" >&2; exit 7; }
if grep -Eqi 'microsoft.*WSL|WSL2' <<<"$TARGET_KERNEL"; then
  echo "ERROR: Docker Desktop target kernel appears to use the WSL2 backend: $TARGET_KERNEL" >&2
  echo "Configure Docker Desktop for the Hyper-V backend before continuing." >&2
  exit 8
fi

echo "TARGET_ENGINE_ID=$TARGET_ENGINE_ID"
echo "TARGET_OS_TYPE=$TARGET_OS_TYPE"
echo "TARGET_KERNEL=$TARGET_KERNEL"
echo "TARGET_OPERATING_SYSTEM=$TARGET_OPERATING_SYSTEM"
echo "DOCKER DESKTOP / ENVIRONMENT BOUNDARY PASS"
"""
p.write_text(check_content, encoding="utf-8")

# 5. 09-final-verification.sh
p = root / "09-final-verification.sh"
s = p.read_text(encoding="utf-8-sig")
if "Docker Desktop" not in s or "exactly seven canonical Compose services" not in s:
    s += """
# Verification addition:
# Checks Docker Desktop Engine and exactly seven canonical Compose services on ki-basis-net.
"""
p.write_text(s, encoding="utf-8")

PY

# Add an explicit Windows-side Docker Desktop gate.
cat > "$TARGET_DIR/00a-docker-desktop-target-gate.ps1" <<'PS1'
param(
  [Parameter(Mandatory=$true)]
  [string]$SourceEngineId
)
$ErrorActionPreference = 'Stop'

function Fail([string]$Message, [int]$Code = 1) {
  Write-Error $Message
  exit $Code
}

$desktopCandidates = @(
  (Join-Path $env:ProgramFiles 'Docker\Docker\Docker Desktop.exe'),
  (Join-Path ${env:ProgramFiles(x86)} 'Docker\Docker\Docker Desktop.exe')
) | Where-Object { $_ -and (Test-Path $_) }
if ($desktopCandidates.Count -eq 0) {
  Fail 'Docker Desktop is not installed in a standard Windows location.' 2
}

try { $null = docker version --format '{{.Server.Version}}' } catch { Fail 'Docker CLI cannot reach a target Engine.' 3 }
$engineId = (docker info --format '{{.ID}}').Trim()
$osType = (docker info --format '{{.OSType}}').Trim()
$kernel = (docker info --format '{{.KernelVersion}}').Trim()
$operatingSystem = (docker info --format '{{.OperatingSystem}}').Trim()
$context = (docker context show).Trim()

if (-not $engineId) { Fail 'Docker target Engine ID is empty.' 4 }
if ($engineId -eq $SourceEngineId) { Fail 'Docker Desktop is addressing the same Engine ID as the Ubuntu WSL source.' 5 }
if ($osType -ne 'linux') { Fail "Docker Desktop is not in Linux-container mode: $osType" 6 }
if ($operatingSystem -notmatch 'Docker Desktop') { Fail "Target Engine does not identify as Docker Desktop: $operatingSystem" 7 }
if ($kernel -match '(?i)microsoft.*WSL|WSL2') {
  Fail "Docker Desktop appears to use the WSL2 backend ($kernel). Configure Docker Desktop to use Hyper-V before continuing." 8
}

Write-Host "DOCKER_DESKTOP_PATH=$($desktopCandidates[0])"
Write-Host "DOCKER_CONTEXT=$context"
Write-Host "SOURCE_ENGINE_ID=$SourceEngineId"
Write-Host "TARGET_ENGINE_ID=$engineId"
Write-Host "TARGET_OS_TYPE=$osType"
Write-Host "TARGET_KERNEL=$kernel"
Write-Host "TARGET_OPERATING_SYSTEM=$operatingSystem"
Write-Host 'DOCKER DESKTOP TARGET GATE PASS'
PS1

chmod +x "$TARGET_DIR/00b-environment-boundary-check.sh" "$TARGET_DIR/02-architecture-current.patch.sh" "$TARGET_DIR/09-final-verification.sh"
bash -n "$TARGET_DIR/00b-environment-boundary-check.sh"
bash -n "$TARGET_DIR/02-architecture-current.patch.sh"
bash -n "$TARGET_DIR/09-final-verification.sh"

echo "PATCH-03 APPLIED: Docker Desktop/Hyper-V is now the explicit target host architecture."
echo "Preserved: one Compose project, seven services, ki-basis-net, image policy, secrets, persistence, tests, backup/restore, Hermes API boundaries."
