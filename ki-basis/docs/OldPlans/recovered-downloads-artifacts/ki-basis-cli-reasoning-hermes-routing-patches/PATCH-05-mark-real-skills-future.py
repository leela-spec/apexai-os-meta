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
path = repo / "apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/05-HERMES-AI-CONTROL-STACK.md"
text = path.read_text(encoding="utf-8")
original = text
anchor = """# Module 05 — Hermes as the AI Control Stack

## Purpose
"""
replacement = """# Module 05 — Hermes as the AI Control Stack

> **Execution status:** FUTURE REAL-SKILL INTEGRATION. The operator will supply the actual skill sets later. Do not execute the product-skill implementation from this file during the current bridge phase. Current authority is `05A-CLI-REASONING-HERMES-ROUTING.md`.
>
> Preserve this file as design/research for the later phase, especially: supported app APIs, Hermes secret handling, `ki-basis-control`, read/write safety, and operator acceptance.

## Purpose
"""
text, _ = replace_once(text, anchor, replacement, "mark M05 future real-skill integration")
write_if_changed(path, original, text)
