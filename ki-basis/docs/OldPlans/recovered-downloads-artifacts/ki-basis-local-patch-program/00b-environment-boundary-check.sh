#!/usr/bin/env bash
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
