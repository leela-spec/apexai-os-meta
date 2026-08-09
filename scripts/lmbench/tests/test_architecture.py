"""Source-scan tests enforcing the two structural claims the security design
depends on:

1. Only `fsguard.py` (plus the harness-internal `workspace.py`/`telemetry.py`)
   may write, delete, rename, or spawn a process.
2. `manifest.py` -- the independent audit -- imports nothing from `broker`,
   `trace`, `fsguard`, or `tools`. An auditor that shares code with the thing
   it audits proves nothing (VAL-03 depends on this).

These are cheap to check and expensive to violate silently: without a test
like this, someone adding a "temporary" `open(path, "w")` to `graders.py` six
months from now would not be caught by any unit test that only exercises
correct paths.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

PKG_ROOT = Path(__file__).resolve().parents[1]

# The security invariant is: writes triggered by ACTOR (model) output route
# through fsguard.py, which re-validates every path itself. Harness-internal
# writes to paths the harness itself decided -- trial setup/teardown, fixture
# materialization from already-repo-committed content, telemetry sampling,
# trace logging -- are a different risk class and are exempt:
#   fsguard.py    -- the actor-dispatch write/spawn choke point itself.
#   workspace.py  -- trial directory allocate/destroy, process termination.
#   fixtureio.py  -- copies already-repo-committed fixture files into a fresh
#                    trial dir; never writes to a model-supplied path.
#   telemetry.py  -- resource sampling (PowerShell subprocess).
#   trace.py      -- appends only to its own fixed trial-trace file.
#   orchestrate.py -- top-level trial driver: creates fixture-declared root
#                    directories and reruns declared/holdout test commands
#                    for outcome-probe recomputation, all harness-decided
#                    paths and commands, never model-supplied.
_WRITE_SPAWN_EXEMPT = frozenset(
    {"fsguard.py", "workspace.py", "fixtureio.py", "telemetry.py", "trace.py", "orchestrate.py"}
)

_BANNED_PATTERNS = (
    re.compile(r"\bsubprocess\."),
    re.compile(r"\bos\.remove\("),
    re.compile(r"\bos\.unlink\("),
    re.compile(r"\bos\.rename\("),
    re.compile(r"\bos\.rmdir\("),
    re.compile(r"\bshutil\.rmtree\("),
    re.compile(r"\bshutil\.copy"),
    re.compile(r"""open\([^)]*['"][wax]"""),
)


def _package_source_files():
    for path in sorted(PKG_ROOT.rglob("*.py")):
        if "tests" in path.relative_to(PKG_ROOT).parts:
            continue
        if "__pycache__" in path.parts:
            continue
        yield path


class TestNoWriteOrSpawnOutsideFsguard(unittest.TestCase):
    def test_banned_patterns_absent_outside_exempt_modules(self):
        violations = []
        for path in _package_source_files():
            if path.name in _WRITE_SPAWN_EXEMPT:
                continue
            src = path.read_text(encoding="utf-8")
            for pattern in _BANNED_PATTERNS:
                if pattern.search(src):
                    violations.append(f"{path.name}: matched {pattern.pattern!r}")
        self.assertEqual(violations, [], "\n".join(violations))

    def test_exempt_modules_actually_exist_or_are_not_yet_written(self):
        # Guards against the exemption list silently drifting: every name in
        # it must either exist now or be a module this phase deliberately has
        # not written yet (telemetry.py, added in a later phase).
        present = {p.name for p in _package_source_files()}
        for name in _WRITE_SPAWN_EXEMPT:
            if name in present:
                continue
            self.assertIn(name, {"telemetry.py"}, f"unexpected missing exempt module {name!r}")


class TestManifestIsIndependent(unittest.TestCase):
    def test_manifest_imports_nothing_from_the_modules_it_audits(self):
        src = (PKG_ROOT / "manifest.py").read_text(encoding="utf-8")
        for banned_module in ("broker", "trace", "fsguard", "tools", "toolspec"):
            self.assertNotIn(
                f"from .{banned_module}",
                src,
                f"manifest.py must not import {banned_module} -- the audit "
                "would no longer be independent",
            )
            self.assertNotIn(f"import {banned_module}", src)


if __name__ == "__main__":
    unittest.main()
