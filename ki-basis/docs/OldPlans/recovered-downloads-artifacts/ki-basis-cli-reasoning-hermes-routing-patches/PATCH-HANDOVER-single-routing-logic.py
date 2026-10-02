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
path = repo / "apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/HANDOVER-NEXT-CHAT.md"
text = path.read_text(encoding="utf-8")
original = text

text = text.replace(
    "**Current Git HEAD**: `02b0cd94` (pushed to `origin/main`)",
    "**Verified remote baseline before this correction set**: `bb9333f7` on `origin/main`; verify live before execution.",
    1
)

anchor = """## 4. Instructions for Next Chat (Executing Module 05)

"""
replacement = """## 4. Instructions for Next Chat — CLI reasoning / Hermes routing bridge

> **Current target:** do not build placeholder product skills. The operator will provide the real skill sets later. Establish one canonical bridge now: heavy-reasoning CLI agent -> authenticated local Hermes API -> Hermes provider-backed routing/tool layer -> future real skills.
>
> OpenRouter is intentionally configured for Hermes routing/execution, but it is not the upstream CLI agent's mandatory brain. Do not claim the CLI agent literally replaces Hermes' model.
>
> Read `04A-DOCKER-BACKGROUND-RUNTIME.md` and `05A-CLI-REASONING-HERMES-ROUTING.md`.

"""
text, _ = replace_once(text, anchor, replacement, "handover current bridge")
write_if_changed(path, original, text)
