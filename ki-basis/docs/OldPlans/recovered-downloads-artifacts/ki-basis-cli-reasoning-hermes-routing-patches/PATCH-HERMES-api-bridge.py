from pathlib import Path
import re, sys

def repo_root():
    if len(sys.argv) != 2:
        raise SystemExit(f"Usage: python {Path(sys.argv[0]).name} C:\\GitDev\\apexai-os-meta")
    p = Path(sys.argv[1])
    if not p.exists():
        raise SystemExit(f"Repository path not found: {p}")
    return p

def replace_once(text, old, new, label):
    count = text.count(old)
    if count == 0:
        if new in text:
            print(f"[SKIP] {label}: already applied")
            return text, False
        raise SystemExit(f"[FAIL] {label}: anchor not found; refusing broad rewrite")
    if count != 1:
        raise SystemExit(f"[FAIL] {label}: expected one anchor, found {count}")
    return text.replace(old, new, 1), True

def regex_once(text, pattern, replacement, label):
    matches = list(re.finditer(pattern, text, flags=re.S))
    if not matches:
        if replacement.strip() in text:
            print(f"[SKIP] {label}: already applied")
            return text, False
        raise SystemExit(f"[FAIL] {label}: section not found; refusing broad rewrite")
    if len(matches) != 1:
        raise SystemExit(f"[FAIL] {label}: expected one section, found {len(matches)}")
    return re.sub(pattern, replacement, text, count=1, flags=re.S), True

def write_if_changed(path, old, new):
    if old == new:
        print(f"[NO CHANGE] {path}")
        return
    path.write_text(new, encoding="utf-8")
    print(f"[PATCHED] {path}")

repo = repo_root()

compose = repo / "ki-basis/compose.yaml"
text = compose.read_text(encoding="utf-8")
original = text
anchor = """      HERMES_DISABLE_LAZY_INSTALLS: "1"
      HERMES_LAZY_INSTALL_TARGET: /opt/data/lazy-packages
      FIREFLY_API_URL: http://firefly:8080
"""
replacement = """      HERMES_DISABLE_LAZY_INSTALLS: "1"
      HERMES_LAZY_INSTALL_TARGET: /opt/data/lazy-packages
      API_SERVER_ENABLED: "true"
      API_SERVER_HOST: "0.0.0.0"
      API_SERVER_KEY: ${HERMES_API_SERVER_KEY:?HERMES_API_SERVER_KEY is required}
      FIREFLY_API_URL: http://firefly:8080
"""
text, _ = replace_once(text, anchor, replacement, "Hermes official API server env")
write_if_changed(compose, original, text)

envex = repo / "ki-basis/.env.example"
text = envex.read_text(encoding="utf-8")
original = text
anchor = """HERMES_DASHBOARD_BASIC_AUTH_USERNAME=admin
HERMES_DASHBOARD_BASIC_AUTH_PASSWORD=

# Optional Authenticated API Tokens for verification
"""
replacement = """HERMES_DASHBOARD_BASIC_AUTH_USERNAME=admin
HERMES_DASHBOARD_BASIC_AUTH_PASSWORD=
# Local machine-to-machine key for CLI agents -> Hermes API server.
HERMES_API_SERVER_KEY=

# Optional Authenticated API Tokens for verification
"""
text, _ = replace_once(text, anchor, replacement, "Hermes API server key template")
write_if_changed(envex, original, text)

script = repo / "ki-basis/scripts/invoke-hermes.ps1"
template = Path(__file__).resolve().parent / "templates/invoke-hermes.ps1"
content = template.read_text(encoding="utf-8")
if script.exists():
    if script.read_text(encoding="utf-8") == content:
        print(f"[NO CHANGE] {script}")
    else:
        raise SystemExit(f"[FAIL] {script} already exists with different content")
else:
    script.write_text(content, encoding="utf-8")
    print(f"[CREATED] {script}")
