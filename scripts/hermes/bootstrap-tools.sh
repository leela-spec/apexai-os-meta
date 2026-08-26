#!/usr/bin/env bash
# =============================================================================
# APEX shared tool bootstrap  (ARCH-IMP-02: Hermes single-container runtime)
# -----------------------------------------------------------------------------
# Installs the deterministic document/knowledge tools that Hermes uses across
# ALL repos. Idempotent + self-verifying: safe to run any number of times, and
# it repairs itself after a container rebuild.
#
# Run it inside the Hermes container (terminal.backend: local):
#     bash scripts/hermes/bootstrap-tools.sh
#
# It also works on a plain Ubuntu/Debian host (e.g. to give the same tools to a
# Windows-side CLI agent) — set APEX_TOOLS_VENV to a writable path first.
# =============================================================================
set -u

# Where the persistent Python venv lives. Default = the container's /opt/data
# volume so it survives restarts. Override for host use: APEX_TOOLS_VENV=~/apex-venv
VENV="${APEX_TOOLS_VENV:-/opt/data/tools/venv}"
REQ_FILE="$(cd "$(dirname "$0")" && pwd)/tools-requirements.txt"

log()  { printf '[bootstrap] %s\n' "$*"; }
fail() { printf '[bootstrap][FAIL] %s\n' "$*" >&2; exit 1; }

# --- 1. Operating-system tools (need root; the Hermes container runs as root) -
need=()
command -v pandoc    >/dev/null 2>&1 || need+=(pandoc)
command -v pdftotext >/dev/null 2>&1 || need+=(poppler-utils)   # pdftotext + pdftoppm
command -v unzip     >/dev/null 2>&1 || need+=(unzip)
command -v zip       >/dev/null 2>&1 || need+=(zip)

if [ "${#need[@]}" -gt 0 ]; then
  log "installing OS packages: ${need[*]}"
  apt-get update -qq            || fail "apt-get update failed (are you root / online?)"
  apt-get install -y --no-install-recommends "${need[@]}" || fail "apt-get install failed"
else
  log "OS tools already present (pandoc, poppler-utils, zip, unzip)"
fi

# --- 2. Python virtual environment + pinned packages -------------------------
if [ ! -x "$VENV/bin/python" ]; then
  log "creating Python venv at: $VENV"
  mkdir -p "$(dirname "$VENV")" || fail "cannot create $(dirname "$VENV")"
  python3 -m venv "$VENV"        || fail "python venv creation failed"
fi

"$VENV/bin/pip" install --quiet --upgrade pip || fail "pip self-upgrade failed"

if [ -f "$REQ_FILE" ]; then
  log "installing Python packages from $REQ_FILE"
  "$VENV/bin/pip" install --quiet -r "$REQ_FILE" || fail "pip install (requirements) failed"
else
  log "no tools-requirements.txt found; installing default set"
  "$VENV/bin/pip" install --quiet docx2python || fail "pip install docx2python failed"
fi

# --- 3. Verify + print EXACT versions (this is the evidence of success) -------
log "verifying tools and versions:"
echo   "  - $(pandoc --version | head -1)"                      || fail "pandoc not runnable"
echo   "  - pdftotext: $(pdftotext -v 2>&1 | head -1)"          || fail "pdftotext not runnable"
echo   "  - pdftoppm:  $(pdftoppm  -v 2>&1 | head -1)"          || fail "pdftoppm not runnable"
"$VENV/bin/python" - <<'PY' || fail "docx2python import failed"
import docx2python
v = getattr(docx2python, "__version__", "unknown")
print(f"  - docx2python {v}  (python: {__import__('sys').version.split()[0]})")
PY

# Record exact resolved versions so they can be pinned into tools-requirements.txt
"$VENV/bin/pip" freeze > "$(dirname "$VENV")/tools-resolved-versions.txt" 2>/dev/null || true

log "OK — all tools present and verified."
log "Canonical Python for scripts:  $VENV/bin/python"
