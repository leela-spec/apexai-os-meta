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
path = repo / "apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/07-COLD-REBOOT-AND-OFFHOST-BACKUP.md"
text = path.read_text(encoding="utf-8")
original = text

pattern = r"""## Part A — Windows cold reboot\n.*?\n## Part B — second-copy/off-host backup"""
replacement = """## Part A — background-runtime + Hermes-bridge lifecycle proof

A forced Windows reboot is not required for the current phase.

Required now:

1. keep Docker Dashboard closed;
2. record seven-service state;
3. restart Docker Desktop through the supported CLI/background path;
4. verify all seven services recover;
5. verify Hermes API server recovers on loopback;
6. run `ki-basis/scripts/invoke-hermes.ps1` with a non-sensitive prompt;
7. re-run existing isolation checks.

At the next natural Windows reboot, run the same proof once. Open a correction only if the natural reboot exposes a real startup/persistence defect.

## Part B — second-copy/off-host backup"""
text, _ = regex_once(text, pattern, replacement, "bridge lifecycle proof")

pattern2 = r"""## Part B — second-copy/off-host backup\n.*?\n## Overengineering guard"""
replacement2 = """## Part B — second-copy/off-host backup

Keep as a future resilience requirement, not a blocker for the current bridge phase.

When the operator selects an already-trusted encrypted second failure domain, copy one verified backup plus checksum manifest there and verify it.

Do not install a new backup platform, cloud-sync daemon, retention service or encryption product merely to close this phase.

## Overengineering guard"""
text, _ = regex_once(text, pattern2, replacement2, "offhost balance")

old = """## Acceptance

- cold reboot target acceptance PASS;
- one verified second-copy backup exists outside the laptop's primary storage failure domain.

Runtime evidence only unless a small sanitized receipt is explicitly required. STOP.
"""
new = """## Acceptance

Blocking now:

- Docker Dashboard remained closed during normal operation;
- supported Docker Desktop restart PASS;
- seven services recovered;
- authenticated Hermes API bridge recovered;
- non-sensitive bridge invocation succeeded;
- isolation boundaries remained intact.

Future, non-blocking:

- natural Windows reboot check;
- encrypted second-copy backup after operator selects a destination;
- final real-skill persistence/cross-app proof after the skill set is installed.

Runtime evidence only unless a small sanitized receipt is explicitly required. STOP.
"""
text, _ = replace_once(text, old, new, "M07 acceptance")
write_if_changed(path, original, text)
