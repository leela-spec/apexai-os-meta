#!/usr/bin/env python3
"""Build the stage 1 base commit and the three arm repositories.

base  = copy of the Mindful Bar working tree (without .git), committed once in a scratch repository.
armA  = contract triggers only: blueprint pointer, blueprint file and every link to it removed.
armB  = blueprint pointer present, blueprint file restored from the real repository HEAD.
armC  = like A plus two placement sentences in AGENTS.md Layer 2.
All arms also drop the three sentences and the README bullet added after the blueprint existed.
Usage: python make_arms.py
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = Path(r"C:\GitDev\mindful-bar")
BASE = HERE / "base"

BP_SENTENCE = ("Use the [agent and authoring blueprint](systems/authoring-blueprint.md) to route specification, "
               "writing, procedure, and maintenance work. ")
ADDED_SENTENCE = (" Before you write or edit a governed file, read the [writing profile](systems/apex/specs/writing-profile.md) "
                  "and the [domain design](systems/design/02-INFORMATION-ARCHITECTURE.md) for its home. After the edit, run the "
                  "[conformance checks](systems/apex/README.md#check-and-refresh) and report the result.")
CONFLICTS = "current user directions and higher-priority instructions govern conflicts."
PLACEMENT = (" Before you choose a path or domain for a file, read the domain ownership table in "
             "[systems/design/02-INFORMATION-ARCHITECTURE.md](systems/design/02-INFORMATION-ARCHITECTURE.md). "
             "Filing, identity and status rules are in "
             "[systems/design/03-FILING-AND-IDENTITY.md](systems/design/03-FILING-AND-IDENTITY.md).")
README_BULLET = ("- [Agent and authoring blueprint](systems/authoring-blueprint.md): read before writing or editing any "
                 "governed file; it routes to the writing profile, domain design and conformance checks\n")
INDEX_LINE = "- [Agent and authoring blueprint](authoring-blueprint.md)\n"
APEX_PHRASE = "follow the routes in the [authoring blueprint](../authoring-blueprint.md)"
APEX_REPLACEMENT = "follow the routes in the contract's gated references"


def git(*args: str, cwd: Path | None = None, binary: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=not binary)


def rd(p: Path) -> str:
    return p.read_text(encoding="utf-8", newline="") if False else open(p, encoding="utf-8", newline="").read()


def wr(p: Path, s: str) -> None:
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(s)


def replace_once(path: Path, old: str, new: str) -> None:
    s = rd(path)
    assert old in s, f"missing text in {path}: {old[:60]!r}"
    wr(path, s.replace(old, new, 1))


def build_base() -> dict:
    if BASE.exists():
        shutil.rmtree(BASE, onerror=lambda f, p, e: (os.chmod(p, 0o700), f(p)))
    shutil.copytree(SRC, BASE, ignore=shutil.ignore_patterns(".git", "__pycache__", "node_modules"))
    git("init", "-q", cwd=BASE)
    for k, v in (("user.name", "stage1"), ("user.email", "stage1@example.invalid"), ("core.autocrlf", "false"), ("core.safecrlf", "false")):
        git("config", k, v, cwd=BASE)
    git("add", "-A", cwd=BASE)
    git("commit", "-q", "-m", "stage1 base: Mindful Bar working tree", cwd=BASE)
    sha = git("rev-parse", "HEAD", cwd=BASE).stdout.strip()
    real_head = git("rev-parse", "HEAD", cwd=SRC).stdout.strip()
    porcelain = git("status", "--porcelain", cwd=SRC).stdout
    return {"base_sha": sha, "real_head": real_head, "real_porcelain_sha256": hashlib.sha256(porcelain.encode()).hexdigest(),
            "tree_sha": git("rev-parse", "HEAD^{tree}", cwd=BASE).stdout.strip()}


def build_arm(name: str) -> str:
    d = HERE / f"arm{name}"
    if d.exists():
        shutil.rmtree(d, onerror=lambda f, p, e: (os.chmod(p, 0o700), f(p)))
    git("clone", "-q", "-c", "core.autocrlf=false", str(BASE), str(d))
    for k, v in (("user.name", "stage1"), ("user.email", "stage1@example.invalid"), ("core.autocrlf", "false")):
        git("config", k, v, cwd=d)
    agents, readme = d / "AGENTS.md", d / "README.md"
    replace_once(agents, ADDED_SENTENCE, "")
    replace_once(readme, README_BULLET, "")
    bp_file = d / "systems" / "authoring-blueprint.md"
    if name == "B":
        head_bp = git("show", "HEAD:systems/authoring-blueprint.md", cwd=SRC, binary=True).stdout
        bp_file.write_bytes(head_bp)
    else:
        replace_once(agents, BP_SENTENCE, "")
        bp_file.unlink()
        replace_once(d / "systems" / "index.md", INDEX_LINE, "")
        replace_once(d / "systems" / "apex" / "README.md", APEX_PHRASE, APEX_REPLACEMENT)
    if name == "C":
        replace_once(agents, CONFLICTS, CONFLICTS + PLACEMENT)
    git("add", "-A", cwd=d)
    git("commit", "-q", "-m", f"stage1 arm {name}", cwd=d)
    return git("rev-parse", "HEAD", cwd=d).stdout.strip()


def main() -> int:
    info = build_base()
    for name in "ABC":
        info[f"arm{name}_sha"] = build_arm(name)
    for name in "ABC":
        info[f"arm{name}_AGENTS_sha256"] = hashlib.sha256((HERE / f"arm{name}" / "AGENTS.md").read_bytes()).hexdigest()
    (HERE / "provenance.json").write_text(json.dumps(info, indent=2), encoding="utf-8")
    print(json.dumps(info, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
