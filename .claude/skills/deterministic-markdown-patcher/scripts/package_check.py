#!/usr/bin/env python3
"""Validate the deterministic‑markdown‑patcher package structure.

This script performs a series of checks on a skill package directory to
ensure that required files are present and conform to basic rules.  It
is intended to be run during development before packaging the skill.
"""

import os
import sys
import re
import yaml

EXPECTED_FILES = [
    'SKILL.md',
    'agents/openai.yaml',
    'references/source-ledger.okf.md',
    'references/patching-process-contract.md',
    'references/action-decision-matrix.md',
    'references/skill-package-rules.md',
    'references/hook-policy.md',
    'references/failure-modes-and-recovery.md',
    'templates/patch-intent.okf.md',
    'templates/fixture-spec.json',
    'templates/final-report.okf.md',
    'examples/small-section-edit.example.md',
    'examples/frontmatter-edit.example.md',
    'examples/patch-pack-run.example.md',
    'scripts/patch_executor.py',
    'scripts/fixture_runner.py',
    'scripts/package_check.py',
    'package-manifest.md'
]


def load_front_matter(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not lines or not lines[0].startswith('---'):
        raise ValueError("missing front matter")
    end = None
    for i in range(1, len(lines)):
        if lines[i].startswith('---'):
            end = i
            break
    if end is None:
        raise ValueError("unterminated front matter")
    yaml_str = ''.join(lines[1:end])
    return yaml.safe_load(yaml_str) or {}


def check_skill_md(package_root: str) -> bool:
    skill_path = os.path.join(package_root, 'SKILL.md')
    front = load_front_matter(skill_path)
    keys = list(front.keys())
    if keys != ['name', 'description']:
        print(f"Front matter keys incorrect: {keys}")
        return False
    desc = front.get('description', '')
    if not str(desc).startswith('Use this skill when'):
        print("Description does not start with 'Use this skill when'")
        return False
    # Check supporting files read_when markers
    with open(skill_path, 'r', encoding='utf-8') as f:
        text = f.read()
    if 'read_when' not in text:
        print("SKILL.md missing read_when markers in supporting files section")
        return False
    return True


def check_files_exist(package_root: str) -> bool:
    ok = True
    for rel in EXPECTED_FILES:
        path = os.path.join(package_root, rel)
        if not os.path.exists(path):
            print(f"Missing required file: {rel}")
            ok = False
    return ok


def check_script_syntax(package_root: str) -> bool:
    import subprocess
    scripts = [
        os.path.join(package_root, 'scripts/patch_executor.py'),
        os.path.join(package_root, 'scripts/fixture_runner.py'),
        os.path.join(package_root, 'scripts/package_check.py'),
    ]
    for script in scripts:
        try:
            subprocess.check_call([sys.executable, '-m', 'py_compile', script])
        except subprocess.CalledProcessError:
            print(f"Syntax error in {script}")
            return False
    return True


def main(argv: list) -> None:
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <package_root>")
        sys.exit(1)
    root = argv[1]
    ok = True
    if not check_files_exist(root):
        ok = False
    if not check_skill_md(root):
        ok = False
    if not check_script_syntax(root):
        ok = False
    if ok:
        print("Package check passed")
    else:
        print("Package check failed")
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)