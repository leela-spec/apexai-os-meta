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
script_dir = Path(__file__).resolve().parent
source = script_dir / "sources/Docker-Desktop-Windows.md"
header = (script_dir / "templates/Docker-Desktop-Windows-HEADER.md").read_text(encoding="utf-8")
target = repo / "apex-meta/Alpine/research/Docker-Desktop-Windows.md"
target.parent.mkdir(parents=True, exist_ok=True)
content = header + source.read_text(encoding="utf-8")
if target.exists():
    if target.read_text(encoding="utf-8") == content:
        print(f"[NO CHANGE] {target}")
    else:
        raise SystemExit(f"[FAIL] {target} already exists with different content")
else:
    target.write_text(content, encoding="utf-8")
    print(f"[CREATED] {target}")

arch = repo / "apex-meta/Alpine/ARCHITEKTUR-BASIS.md"
text = arch.read_text(encoding="utf-8")
original = text
anchor = """> **Target host:** Windows 11 running Docker Desktop with Hyper-V Linux-container backend (ONE dedicated Docker Engine).
>"""
replacement = """> **Target host/runtime:** Windows 11 with Docker Desktop's Hyper-V Linux-container backend and one Docker Engine. Routine operation is CLI-first/background-only: the Docker Dashboard is kept closed. Fully stopping Docker Desktop stops the current managed Linux runtime; a genuine no-Desktop Docker Engine would require a separate Linux-VM migration.
>"""
text, _ = replace_once(text, anchor, replacement, "background runtime architecture")

anchor2 = """> **Hermes role:** Hermes is the AI operating surface and reaches Firefly, Paperless and OpenProject through supported application APIs. It does not mount a Docker socket or rely on Ubuntu WSL filesystem binds.
>"""
replacement2 = """> **Hermes role:** Hermes is the canonical local routing/execution plane for future application skills. heavy-reasoning CLI agents call Hermes through its authenticated loopback API server; Hermes then performs its own provider-backed routing/tool execution. The final product skill set is intentionally deferred until the real skills are supplied. Hermes does not mount a Docker socket or rely on Ubuntu WSL filesystem binds.
>"""
text, _ = replace_once(text, anchor2, replacement2, "Hermes routing role")

anchor3 = """- Alpine image-build reference: [`2026-09-01-alpine-image-build.md`](2026-09-01-alpine-image-build.md)
"""
replacement3 = """- Alpine image-build reference: [`2026-09-01-alpine-image-build.md`](2026-09-01-alpine-image-build.md)
- Docker Desktop/Windows performance research input (non-authoritative): [`research/Docker-Desktop-Windows.md`](research/Docker-Desktop-Windows.md)
"""
text, _ = replace_once(text, anchor3, replacement3, "research provenance")
write_if_changed(arch, original, text)
