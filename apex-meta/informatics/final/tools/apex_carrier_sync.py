#!/usr/bin/env python3
"""Keep every carrier of the Apex always-on block equal to its master.

Question this answers: which files carry a copy of the always-on block, and does each still match
`specs/apex_contract_v1.0_ultra.xml` on the `main` branch of apexai-os-meta?

  python apex-meta/informatics/final/tools/apex_carrier_sync.py                     # check, exit 1 on drift
  python apex-meta/informatics/final/tools/apex_carrier_sync.py --sync              # rewrite drifted carriers (backup first)
  python apex-meta/informatics/final/tools/apex_carrier_sync.py --source worktree   # compare against the uncommitted master

Scope: the <apex_contract>...</apex_contract> span, plus the shared Layer 2 sections listed in specs/carrier-layer2-shared.md for the three global files. Module files (specs/**) are checked by
tools/check_vendor_drift.py (vendored into Leela and Mindful Bar), which this script runs and reports. Nothing here edits the
master. Hand-written text around the block in a carrier is never touched. Not wired into any gate: it reads
files outside any one repo, so a gate would be red on a clean clone (see operations/18-APEX-CARRIER-MAP.md).
"""
import argparse, os, re, subprocess, sys, shutil

HOME = os.path.expanduser("~")
META = "C:/GitDev/apexai-os-meta"
META_SRC = os.environ.get("APEX_META_SRC", META)  # only for testing --source worktree against another checkout
LEELA = "C:/GitDev/Leela-Cloud-2026"
MB = "C:/GitDev/mindful-bar"
# repos that vendor the instruction layer: (name, repo root, folder holding MANIFEST.sha256)
VENDORS = [("Leela", LEELA, f"{LEELA}/docs/apex"), ("Mindful Bar", MB, f"{MB}/systems/apex")]
TOOL_REL = "apex-meta/informatics/final/tools/check_vendor_drift.py"
MASTER_REL = "apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml"
SPAN = re.compile(r"<apex_contract[^>]*>.*?</apex_contract>", re.S)

# Every carrier holds an inline copy of the block. allowed = deliberate departures from the master (base_ref,
# per-tag ref attribute). optional = a launch may select this config dir (CLAUDE_CONFIG_DIR, CODEX_HOME);
# absence is reported, not failed, because whether it is launched is not knowable from the files.
ABS = f"{META}/apex-meta/informatics/final/"
CARRIERS = [
    dict(name="Claude global", path=f"{HOME}/.claude/CLAUDE.md", kind="inline", layer2=True, base_ref=ABS, ref_override={}),
    dict(name="Gemini/Antigravity global", path=f"{HOME}/.gemini/GEMINI.md", kind="inline", layer2=True, base_ref=ABS, ref_override={}),
    dict(name="Codex global", path=f"{HOME}/.codex/AGENTS.md", kind="inline", layer2=True, base_ref=ABS, ref_override={}),
    dict(name="Leela vendored copy", path=f"{LEELA}/docs/apex/apex-contract.md", kind="inline",
         base_ref="docs/apex/", ref_override={"authoring": "specs/file-architecture.md"}),
    dict(name="Mindful Bar AGENTS.md", path=f"{MB}/AGENTS.md", kind="inline", base_ref="systems/apex/",
         ref_override={"authoring": "specs/file-architecture.md"}, root=MB, optional=True),
    dict(name="Claude account agehm", path=f"{HOME}/.claude-agehm/CLAUDE.md", kind="inline", base_ref=ABS, ref_override={}, optional=True),
    dict(name="Claude account wimmer", path=f"{HOME}/.claude-wimmer/CLAUDE.md", kind="inline", base_ref=ABS, ref_override={}, optional=True),
    dict(name="Antigravity config/GEMINI.md", path=f"{HOME}/.gemini/config/GEMINI.md", kind="inline", base_ref=ABS, ref_override={}, optional=True),
    dict(name="Codex account 1", path=f"{HOME}/.codex-acc1/AGENTS.md", kind="inline", base_ref=ABS, ref_override={}, optional=True),
    dict(name="Codex account 2", path=f"{HOME}/.codex-acc2/AGENTS.md", kind="inline", base_ref=ABS, ref_override={}, optional=True),
]


_BACKED = set()


def backup(path):
    """One .apex-sync.bak per file per run, holding the state before this run touched it."""
    if path not in _BACKED:
        shutil.copyfile(path, path + ".apex-sync.bak")
        _BACKED.add(path)


SHARED_REL = "apex-meta/informatics/final/specs/carrier-layer2-shared.md"


def sections(text):
    """{heading: normalized body} for every '## ' section after the contract block."""
    t = text.replace("\r\n", "\n")
    k = t.find("</apex_contract>")
    t = t[k + len("</apex_contract>"):] if k >= 0 else t
    out = {}
    for m in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", t, re.S | re.M):
        out[m.group(1).strip()] = "\n".join(l.strip() for l in m.group(2).splitlines() if l.strip())
    return out


def shared_layer2(source):
    if source == "worktree":
        raw = open(f"{META_SRC}/{SHARED_REL}", encoding="utf-8").read()
    else:
        r = subprocess.run(["git", "-C", META, "show", "main:" + SHARED_REL], capture_output=True, text=True, encoding="utf-8")
        if r.returncode:
            sys.exit("cannot read shared Layer 2 spec from git: " + r.stderr.strip())
        raw = r.stdout
    return sections("</apex_contract>\n" + raw)


def layer2_sync(path, text, shared):
    """Replace or append each shared section in the carrier text; keeps the carrier's line endings."""
    eol = "\r\n" if "\r\n" in text else "\n"
    for head, body in shared.items():
        block = f"## {head}{eol}{eol}" + eol.join(body.splitlines()) + eol
        pat = re.compile(r"^## " + re.escape(head) + r"[ \t]*\r?\n.*?(?=^## |\Z)", re.S | re.M)
        if pat.search(text):
            text = pat.sub(lambda m: block + (eol if not m.group(0).endswith(eol + eol) else ""), text, count=1)
        else:
            text = text.rstrip() + eol + eol + block
    return text


def norm_bytes(b):
    return b.replace(b"\r\n", b"\n")


def tool_master(source):
    if source == "worktree":
        return open(f"{META_SRC}/{TOOL_REL}", "rb").read()
    r = subprocess.run(["git", "-C", META, "show", "main:" + TOOL_REL], capture_output=True)
    if r.returncode:
        sys.exit("cannot read tools/check_vendor_drift.py from git: " + r.stderr.decode(errors="replace").strip())
    return r.stdout


def master_text(source):
    if source == "worktree":
        return open(f"{META_SRC}/{MASTER_REL}", encoding="utf-8").read()
    r = subprocess.run(["git", "-C", META, "show", "main:" + MASTER_REL], capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        sys.exit("cannot read master from git: " + r.stderr.strip())
    return r.stdout


def tags(block):
    inner = re.sub(r"^<apex_contract[^>]*>|</apex_contract>\s*$", "", block.strip())
    out = {}
    for m in re.finditer(r"<(\w+)([^>]*)>(.*?)</\1>", inner, re.S):
        out[m.group(1)] = (re.sub(r"\s+", " ", m.group(2).strip()), re.sub(r"\s+", " ", m.group(3).strip()))
    return out


def expected_block(master_block, c):
    """The master block with this carrier's allowed departures applied."""
    b = master_block
    if c["base_ref"]:
        b = re.sub(r'base_ref="[^"]*"', f'base_ref="{c["base_ref"]}"', b, count=1)
    for tag, ref in c["ref_override"].items():
        b = re.sub(rf'(<{tag}\b[^>]*\bref=")[^"]*(")', rf"\g<1>{ref}\g<2>", b, count=1)
    return b


def diff(expected, actual):
    e, a, out = tags(expected), tags(actual), []
    for k in e:
        if k not in a: out.append(f"missing <{k}>")
        elif a[k][1] != e[k][1]: out.append(f"<{k}> body differs")
        elif a[k][0] != e[k][0]: out.append(f"<{k}> attributes differ ({a[k][0]!r} vs {e[k][0]!r})")
    out += [f"extra <{k}>" for k in a if k not in e]
    ba = re.search(r'base_ref="([^"]*)"', actual); be = re.search(r'base_ref="([^"]*)"', expected)
    if ba and be and ba.group(1).lower() != be.group(1).lower(): out.append(f"base_ref {ba.group(1)!r} vs {be.group(1)!r}")
    return out


def unresolved_refs(block, cwd_roots):
    """Refs that cannot be opened from any known working root (base_ref relative or absolute)."""
    base = re.search(r'base_ref="([^"]*)"', block).group(1)
    bad = []
    for m in re.finditer(r'<(\w+)[^>]*\bref="([^"]+)"', block):
        roots = [base] if re.match(r"^[A-Za-z]:|^/", base) else [os.path.join(r, base) for r in cwd_roots]
        if not any(os.path.exists(os.path.join(r, m.group(2))) for r in roots):
            bad.append(f"<{m.group(1)}> ref={m.group(2)}")
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sync", action="store_true")
    ap.add_argument("--source", choices=["main", "worktree"], default="main")
    args = ap.parse_args()
    master = master_text(args.source)
    mblock = SPAN.search(master).group(0)
    bad = 0
    print(f"master: {MASTER_REL} ({args.source}), {len(tags(mblock))} rules; meta repo checked out on "
          + subprocess.run(["git", "-C", META, "branch", "--show-current"], capture_output=True, text=True).stdout.strip())
    sha = lambda ref: subprocess.run(["git", "-C", META, "rev-parse", ref], capture_output=True, text=True).stdout.strip()
    if sha("main") != sha("origin/main"):
        print("  WARN local main differs from origin/main: run `git fetch origin main:main` (or push) so carriers follow the shared master")
    st = subprocess.run(["git", "-C", META, "status", "--short", "--", MASTER_REL.rsplit('/', 1)[0]], capture_output=True, text=True).stdout.strip()
    if st: print("  master repo has uncommitted spec changes (not yet in any carrier unless --source worktree):\n   " + st.replace("\n", "\n   "))
    for c in CARRIERS:
        p = c["path"]
        if not os.path.exists(p):
            if c.get("optional"): print(f"ABSENT   {c['name']}: {p} (optional; an agent launched with this config dir gets no always-on block)")
            else: print(f"MISSING  {c['name']}: {p}"); bad += 1
            continue
        text = open(p, encoding="utf-8").read()
        found = SPAN.search(text)
        if c.get("optional") and c["kind"] == "inline" and not found:
            print(f"ABSENT   {c['name']}: file exists but carries no <apex_contract> block ({p})"); continue
        exp = expected_block(mblock, c)
        if not found:
            print(f"DRIFT    {c['name']}: no <apex_contract> block in {p}"); bad += 1; continue
        d = diff(exp, found.group(0))
        refs = unresolved_refs(found.group(0), [c.get("root", LEELA)])
        print(("OK       " if not d else "DRIFT    ") + f"{c['name']}: " + ("identical to master" + (" (allowed departures applied)" if c['base_ref'] or c['ref_override'] else "") if not d else "; ".join(d)))
        if refs: print(f"  WARN   {len(refs)} ref(s) do not resolve when the agent works in {c.get("root", LEELA)}, e.g. {refs[0]}")
        if d:
            bad += 1
            if args.sync:
                backup(p)
                open(p, "w", encoding="utf-8", newline="").write(text[:found.start()] + exp + text[found.end():])
                print(f"  SYNCED {p} (backup: {p}.apex-sync.bak)")
    shared = shared_layer2(args.source)
    for c in CARRIERS:
        if not c.get("layer2") or not os.path.exists(c["path"]):
            continue
        text = open(c["path"], encoding="utf-8").read()
        have = sections(text)
        d2 = [f"## {h}: " + ("missing" if h not in have else "differs") for h, b in shared.items() if have.get(h) != b]
        print(("OK       " if not d2 else "DRIFT    ") + f"{c['name']} layer 2: " + ("shared sections identical" if not d2 else "; ".join(d2)))
        if d2:
            bad += 1
            if args.sync:
                backup(c["path"])
                open(c["path"], "w", encoding="utf-8", newline="").write(layer2_sync(c["path"], text, shared))
                print(f"  SYNCED {c['path']} layer 2 (backup: {c['path']}.apex-sync.bak)")
    tool = tool_master(args.source)
    for vname, _root, vdir in VENDORS:
        checker = f"{vdir}/check_vendor_drift.py"
        if not os.path.isdir(vdir):
            print(f"ABSENT   {vname} vendor folder {vdir} (repo not on this machine)")
            continue
        if not os.path.exists(checker):
            print(f"DRIFT    {vname}: {checker} is missing"); bad += 1
        else:
            same = norm_bytes(open(checker, "rb").read()) == norm_bytes(tool)
            print(("OK       " if same else "DRIFT    ") + f"{vname} checker: " + ("identical to tools/check_vendor_drift.py" if same else "differs from tools/check_vendor_drift.py"))
            if not same:
                bad += 1
                if args.sync:
                    backup(checker)
                    open(checker, "wb").write(tool)
                    print(f"  SYNCED {checker} (backup: {checker}.apex-sync.bak)")
        r = subprocess.run([sys.executable, checker], capture_output=True, text=True)
        tail = [l for l in r.stdout.splitlines() if l.strip() and not l.startswith("OK")]
        print(f"modules ({vname}): " + ("all OK" if not tail else "; ".join(tail)))
        bad += any(l.startswith(("DRIFTED", "MISSING", "LOCAL-EDIT")) for l in tail)
    return 1 if bad and not args.sync else 0


if __name__ == "__main__":
    sys.exit(main())
