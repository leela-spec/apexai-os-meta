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
path = repo / "apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/09-FINAL-INDEPENDENT-CLOSURE.md"
text = path.read_text(encoding="utf-8")
original = text

old = """Fresh independent audit after Modules 01–08. Implementation agents do not certify themselves.
"""
new = """Fresh independent audit of the current platform + CLI-reasoning/Hermes-routing bridge. The final product skill library is explicitly outside this closure because the operator will supply it later. Implementation agents do not certify themselves.
"""
text, _ = replace_once(text, old, new, "M09 bridge phase")

pattern = r"""## Final acceptance\n.*?\nReturn only:"""
replacement = """## Final acceptance

Verify independently:

1. accepted Windows/Hyper-V Linux-container runtime remains intact;
2. Docker Dashboard is not required for routine operation;
3. seven canonical services remain on `ki-basis-net`;
4. PostgreSQL/Valkey remain internal-only;
5. Hermes has no Docker socket or legacy WSL bind;
6. no tracked real secrets;
7. backup/restore/auth hardening from M01-M04 remains intact;
8. Hermes official API server is enabled, authenticated and published loopback-only on port 8642;
9. invalid Hermes API key is rejected;
10. `invoke-hermes.ps1` succeeds with valid key and does not contain product business logic;
11. Hermes has one configured provider and can answer a non-sensitive API request;
12. architecture clearly distinguishes upstream CLI reasoning from Hermes' own provider-backed routing/tool execution;
13. no permanent parallel direct-product CLI-agent control logic has been created;
14. full Firefly/Paperless/OpenProject skill implementation and `ki-basis-control` are explicitly deferred until real skills arrive;
15. Docker Desktop restart restores the bridge and seven-service runtime;
16. Docker Desktop/Windows research provenance is preserved;
17. performance tuning remains evidence-gated;
18. privacy documentation does not falsely claim OpenRouter is private merely because an upstream CLI agent performs heavy reasoning.

Not required for current PASS:

- final product skills;
- `ki-basis-control` bundle;
- cross-application skill proof;
- write-capable skills;
- fully local model runtime;
- manual Hyper-V Linux-VM migration;
- forced Windows reboot before the next natural reboot;
- off-host backup platform;
- speculative resource tuning.

Return only:"""
text, _ = regex_once(text, pattern, replacement, "M09 bridge acceptance")
write_if_changed(path, original, text)
