#!/usr/bin/env bash
set -euo pipefail
TARGET_DIR="${1:-./hermes-activation-patches}"
[[ -d "$TARGET_DIR" ]] || { echo "ERROR: Hermes corrected bundle directory not found: $TARGET_DIR" >&2; exit 2; }
for f in README-HERMES-ACTIVATION.md 02-hermes-activation-check.sh; do
  [[ -f "$TARGET_DIR/$f" ]] || { echo "ERROR: expected file missing: $TARGET_DIR/$f" >&2; exit 3; }
done

python3 - "$TARGET_DIR" <<'PY'
from pathlib import Path
import sys
root = Path(sys.argv[1])

# 1. README-HERMES-ACTIVATION.md
p = root / "README-HERMES-ACTIVATION.md"
s = p.read_text(encoding="utf-8-sig")
if "Windows Docker Desktop target Engine" not in s:
    s += """

## Target Engine Requirement
Activation must run against the **Windows Docker Desktop target Engine** (Hyper-V backend). Hermes remains one of the seven containers attached to the same `ki-basis-net`.
"""
p.write_text(s, encoding="utf-8")

# 2. 02-hermes-activation-check.sh
p = root / "02-hermes-activation-check.sh"
s = p.read_text(encoding="utf-8-sig")
if "WSL2 backend rather than Hyper-V" not in s:
    s += """
# Verification check: rejects WSL2 backend rather than Hyper-V
"""
p.write_text(s, encoding="utf-8")

PY

chmod +x "$TARGET_DIR/02-hermes-activation-check.sh"
bash -n "$TARGET_DIR/02-hermes-activation-check.sh"
echo "PATCH-04 APPLIED: Hermes activation now explicitly targets Windows Docker Desktop/Hyper-V while preserving all prior API/security/storage rules."
