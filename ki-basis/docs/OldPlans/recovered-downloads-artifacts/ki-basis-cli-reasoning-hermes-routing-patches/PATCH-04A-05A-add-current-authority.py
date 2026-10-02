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
base = repo / "apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization"
script_dir = Path(__file__).resolve().parent
for name in ["04A-DOCKER-BACKGROUND-RUNTIME.md", "05A-CLI-REASONING-HERMES-ROUTING.md"]:
    src = script_dir / "templates" / name
    dst = base / name
    content = src.read_text(encoding="utf-8")
    if dst.exists():
        if dst.read_text(encoding="utf-8") == content:
            print(f"[NO CHANGE] {dst}")
        else:
            raise SystemExit(f"[FAIL] {dst} already exists with different content")
    else:
        dst.write_text(content, encoding="utf-8")
        print(f"[CREATED] {dst}")
