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
path = base / "00-START-HERE.md"
text = path.read_text(encoding="utf-8")
original = text

anchor = """This is **not** another architecture migration.

## Antigravity authority
"""
insert = """This is **not** another architecture migration.

## Current execution authority — one reasoning/routing logic

No earlier patch bundle from this chat has been applied. This program therefore defines the single current path directly from the existing baseline.

The final application skill sets will be supplied later.

Current canonical control path:

`heavy-reasoning CLI agent -> Hermes local API -> Hermes routing/skills -> product APIs`

Do not create a parallel permanent path where CLI agents independently implement Firefly/Paperless/OpenProject business logic.

Read before further execution:

1. `04A-DOCKER-BACKGROUND-RUNTIME.md`
2. `05A-CLI-REASONING-HERMES-ROUTING.md`

OpenRouter is intentionally configured as a Hermes routing/execution provider, while the upstream CLI agent may use its own model/provider for heavy reasoning.

Important: the upstream CLI agent does not literally replace Hermes' own inference model. Hermes still runs its own AIAgent for routing/tool execution.

The full product skill/bundle implementation in `05-HERMES-AI-CONTROL-STACK.md` is deferred until the real skill set is available.

## Antigravity authority
"""
text, _ = replace_once(text, anchor, insert, "single current control path")

pattern = r"""## Module order\n.*?\n## Required status vocabulary"""
replacement = """## Current state and remaining order

Already completed and retained:

1. M01 security / secret sanitation.
2. M02 backup fail-close hardening.
3. M03 independent Paperless restore SHA oracle.
4. M04 strict application-auth / topology verification.
5. M08 evidence-gated performance deferral.

Execute now:

1. `04A-DOCKER-BACKGROUND-RUNTIME.md`
2. `05A-CLI-REASONING-HERMES-ROUTING.md`
3. M06 only for concrete documentation/provenance updates created by this correction.
4. M07 lifecycle proof against the background runtime + Hermes bridge.
5. M09 independent closure of this bridge/platform phase.

Defer until the real skill set arrives:

- Firefly/Paperless/OpenProject Hermes skill implementation;
- `ki-basis-control` bundle;
- cross-application skill orchestration;
- selected write workflows.

Do not rerun M01-M04 for ceremony. Do not create placeholder skills or a direct-product CLI-agent architecture.

## Required status vocabulary"""
text, _ = regex_once(text, pattern, replacement, "current module order")
write_if_changed(path, original, text)
