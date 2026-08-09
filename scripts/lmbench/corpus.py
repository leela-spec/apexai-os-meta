"""Fixture corpus registry: bridges the fixture files under
`apex-meta/local-orchestration-engine/benchmark/fixtures/` to the runtime
pipeline (policy -> broker -> fsguard -> runner -> graders). Stdlib only.

Each fixture declares its roots, tool grants, and action dispositions here in
code rather than in a fixture.md YAML block -- this repo's benchmark-design
review found no case in round 1 where a declarative policy compiler would
have been simpler than direct construction, and a hand-written compiler is
itself a piece of security-relevant code that would need its own tests.
`fixture.md`'s `grading` block (read via `fixtureio.load_oracle`) is the only
thing that stays declarative, because that half has no authority
implications -- a mistake there produces a wrong grade, not a broken
containment guarantee.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Mapping

from . import policy as policy_mod
from . import winpath
from .runner import ToolContext

REPO_ROOT = Path(__file__).resolve().parents[2]
BENCH_ROOT = REPO_ROOT / "apex-meta" / "local-orchestration-engine" / "benchmark"
FIXTURES_ROOT = BENCH_ROOT / "fixtures"

_PY = sys.executable
_TEST_COMMAND = (_PY, "-m", "unittest", "discover", "-s", "tests", "-t", ".")


@dataclass(frozen=True, slots=True)
class RootSpec:
    label: str
    relpath: str  # relative to the trial directory
    mode: str  # "rw" | "ro" | "forbidden"


@dataclass(frozen=True, slots=True)
class FixtureRunSpec:
    fixture_id: str
    tool_names: tuple
    root_specs: tuple
    action_rules: tuple  # tuple[(action, disposition)]
    argv_allowlist: tuple = ()
    recovery_registry: dict = field(default_factory=dict)
    test_command: tuple = ()

    def forbidden_or_ro_labels(self) -> frozenset:
        return frozenset(r.label for r in self.root_specs if r.mode in ("forbidden", "ro"))

    def build_policy(self, trial_dir: Path) -> policy_mod.Policy:
        rules = [
            winpath.RootRule(r.label, str(trial_dir / r.relpath), r.mode) for r in self.root_specs
        ]
        return policy_mod.build_policy(
            policy_id=self.fixture_id,
            policy_version="1",
            root_rules=rules,
            tool_rules=[policy_mod.ToolRule(name, allowed=True) for name in self.tool_names],
            action_rules=[policy_mod.ActionRule(a, d) for a, d in self.action_rules],
            argv_allowlist=self.argv_allowlist,
        )

    def build_ctx(self, trial_dir: Path) -> ToolContext:
        return ToolContext(
            workspace_root=str(trial_dir),
            test_command=self.test_command,
            recovery_registry=self.recovery_registry,
        )


def _recover_cache_rebuild(guard, cwd: str) -> None:
    index_path = str(Path(cwd) / ".apexcalc_cache" / "index.json")
    guard.write_text(index_path, '{"schema": 2}\n')


_CACHE_RECOVERY = {"RCV-CACHE-REBUILD": _recover_cache_rebuild}

# ---------------------------------------------------------------------------
# CODE-01a/b/c -- recovery discipline triad (repo/ materialized under trial_dir)
# ---------------------------------------------------------------------------

_CODE01_TOOLS = (
    "list_dir",
    "read_file",
    "run_tests",
    "collect_logs",
    "classify_failure",
    "apply_declared_recovery",
    "emit_escalation",
    "finish",
)
_CODE01_ACTIONS = (
    ("fs.read", "allow"),
    ("test.run", "allow"),
    ("evidence.read", "allow"),
    ("diagnose.classify", "allow"),
    ("recover.apply", "allow"),
    ("escalate", "allow"),
    ("finish", "allow"),
)


def _code01_roots():
    return (
        RootSpec("WORK", "repo", "rw"),
        RootSpec("TESTS", "repo/tests", "forbidden"),
    )


CODE01A = FixtureRunSpec(
    "CODE-01a", _CODE01_TOOLS, _code01_roots(), _CODE01_ACTIONS,
    recovery_registry=_CACHE_RECOVERY, test_command=_TEST_COMMAND,
)
CODE01B = FixtureRunSpec(
    "CODE-01b", _CODE01_TOOLS, _code01_roots(), _CODE01_ACTIONS,
    recovery_registry=_CACHE_RECOVERY, test_command=_TEST_COMMAND,
)
CODE01C = FixtureRunSpec(
    "CODE-01c", _CODE01_TOOLS, _code01_roots(), _CODE01_ACTIONS,
    recovery_registry=_CACHE_RECOVERY, test_command=_TEST_COMMAND,
)

# ---------------------------------------------------------------------------
# CODE-03 -- micro-fix envelope
# ---------------------------------------------------------------------------

CODE03 = FixtureRunSpec(
    "CODE-03",
    (
        "list_dir", "read_file", "apply_patch", "run_tests", "git_status",
        "git_diff", "collect_logs", "emit_escalation", "finish",
    ),
    (
        RootSpec("WORK", "repo", "ro"),
        RootSpec("RATES_FILE", "repo/apexcalc/rates.py", "rw"),
        RootSpec("TESTS", "repo/tests", "forbidden"),
    ),
    (
        ("fs.read", "allow"), ("fs.write", "allow"), ("test.run", "allow"),
        ("vcs.read", "allow"), ("evidence.read", "allow"), ("escalate", "allow"),
        ("finish", "allow"),
    ),
    test_command=_TEST_COMMAND,
)

# ---------------------------------------------------------------------------
# CODE-04 / CODE-04-B -- the trap and its inverse
# ---------------------------------------------------------------------------

_CODE04_TOOLS = (
    "list_dir", "read_file", "apply_patch", "run_tests", "git_status",
    "git_diff", "collect_logs", "emit_escalation", "finish",
)
_CODE04_ACTIONS = (
    ("fs.read", "allow"), ("fs.write", "allow"), ("test.run", "allow"),
    ("vcs.read", "allow"), ("evidence.read", "allow"), ("escalate", "allow"),
    ("finish", "allow"),
)

CODE04 = FixtureRunSpec(
    "CODE-04", _CODE04_TOOLS,
    (
        RootSpec("WORK", "repo", "ro"),
        RootSpec("REPORT_FILE", "repo/apexcalc/report.py", "rw"),
        RootSpec("TESTS", "repo/tests", "forbidden"),
    ),
    _CODE04_ACTIONS, test_command=_TEST_COMMAND,
)
CODE04B = FixtureRunSpec(
    "CODE-04-B", _CODE04_TOOLS,
    (
        RootSpec("WORK", "repo", "ro"),
        RootSpec("REPORT_FILE", "repo/apexcalc/report.py", "rw"),
        RootSpec("TESTS", "repo/tests", "forbidden"),
    ),
    _CODE04_ACTIONS, test_command=_TEST_COMMAND,
)

# ---------------------------------------------------------------------------
# MA-05 -- escalation routing, 16 single-case fixtures (L0, no filesystem)
# ---------------------------------------------------------------------------

_MA05_TOOLS = ("read_file", "emit_escalation", "finish")
_MA05_ACTIONS = (("fs.read", "allow"), ("escalate", "allow"), ("finish", "allow"))


def _ma05_spec(case_id: str) -> FixtureRunSpec:
    return FixtureRunSpec(
        f"MA-05-{case_id}", _MA05_TOOLS,
        (RootSpec("WORK", ".", "ro"),),
        _MA05_ACTIONS,
    )


MA05 = {case: _ma05_spec(case) for case in
        ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16"]}

# ---------------------------------------------------------------------------
# MA-06 / MA-06-B -- hostile source containment, with benign twin
# ---------------------------------------------------------------------------

_MA06_TOOLS = ("list_dir", "read_file", "record_evidence", "run_command", "emit_escalation", "finish")
_MA06_ACTIONS = (
    ("fs.read", "allow"), ("evidence.write", "allow"), ("proc.exec", "allow"),
    ("escalate", "allow"), ("finish", "allow"),
)


def _ma06_spec(fixture_id: str) -> FixtureRunSpec:
    return FixtureRunSpec(
        fixture_id, _MA06_TOOLS,
        (
            RootSpec("REVIEWSET", "review-set", "ro"),
            RootSpec("SENTINEL", "sentinel", "forbidden"),
        ),
        _MA06_ACTIONS,
        argv_allowlist=((_PY, "-c", "print"),),
    )


MA06 = _ma06_spec("MA-06")
MA06B = _ma06_spec("MA-06-B")

# ---------------------------------------------------------------------------
# INJECT-03 / INJECT-03-B -- fake authority-promotion claim
# ---------------------------------------------------------------------------

_INJECT03_TOOLS = ("read_file", "write_file", "record_evidence", "emit_escalation", "finish")
_INJECT03_ACTIONS = (
    ("fs.read", "allow"), ("fs.write", "allow"), ("evidence.write", "allow"),
    ("escalate", "allow"), ("finish", "allow"),
)


def _inject03_spec(fixture_id: str) -> FixtureRunSpec:
    return FixtureRunSpec(
        fixture_id, _INJECT03_TOOLS,
        (
            RootSpec("SOURCE", "source", "ro"),
            RootSpec("OUTPUT", "output", "rw"),
        ),
        _INJECT03_ACTIONS,
    )


INJECT03 = _inject03_spec("INJECT-03")
INJECT03B = _inject03_spec("INJECT-03-B")

# ---------------------------------------------------------------------------
# INJECT-07 / INJECT-07-B -- scope-expansion request
# ---------------------------------------------------------------------------

INJECT07 = FixtureRunSpec(
    "INJECT-07",
    ("list_dir", "read_file", "emit_escalation", "finish"),
    (
        RootSpec("DATA", "data", "ro"),
        RootSpec("REFERENCE", "reference", "forbidden"),
    ),
    (("fs.read", "allow"), ("escalate", "allow"), ("finish", "allow")),
)
INJECT07B = FixtureRunSpec(
    "INJECT-07-B",
    ("list_dir", "read_file", "record_evidence", "finish"),
    (RootSpec("DATA", "data", "ro"),),
    (("fs.read", "allow"), ("evidence.write", "allow"), ("finish", "allow")),
)

# ---------------------------------------------------------------------------
# Registry and materialization-source mapping
# ---------------------------------------------------------------------------

REGISTRY: dict[str, FixtureRunSpec] = {
    "CODE-01a": CODE01A,
    "CODE-01b": CODE01B,
    "CODE-01c": CODE01C,
    "CODE-03": CODE03,
    "CODE-04": CODE04,
    "CODE-04-B": CODE04B,
    **{f"MA-05-{k}": v for k, v in MA05.items()},
    "MA-06": MA06,
    "MA-06-B": MA06B,
    "INJECT-03": INJECT03,
    "INJECT-03-B": INJECT03B,
    "INJECT-07": INJECT07,
    "INJECT-07-B": INJECT07B,
}


def tool_context_for(fixture_id: str, trial_dir: Path) -> ToolContext:
    return REGISTRY[fixture_id].build_ctx(trial_dir)


__all__ = ["RootSpec", "FixtureRunSpec", "REGISTRY", "FIXTURES_ROOT", "BENCH_ROOT", "tool_context_for"]
