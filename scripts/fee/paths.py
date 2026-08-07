"""Path resolution for FEE's write surface (stdlib only, per D-I2).

FEE's entire write surface is `artifacts/flow-packets/<day>/execution/<flow_id>/`.
It never writes `normalized-raw-flow-dump-*.md` (step 5 owns that), never touches
`state/`, and never calls apex-session. Every helper here either points inside the
execution directory or points at an upstream file opened read-only.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

DAY_RE = re.compile(r"^\d{8}$")
FLOW_RE = re.compile(r"^(?:F[1-4]|operator_defined)$")


class PathError(Exception):
    """Raised when a day/flow identifier is malformed or a required input is absent."""


def validate_day(day: str) -> str:
    if not DAY_RE.match(day):
        raise PathError(f"execution_day must be YYYYMMDD, got {day!r}")
    return day


def validate_flow(flow_id: str) -> str:
    if not FLOW_RE.match(flow_id):
        raise PathError(f"flow_id must be F1-F4 or operator_defined, got {flow_id!r}")
    return flow_id


def repo_root(start: Path | None = None) -> Path:
    """Walk up from `start` to the directory holding both artifacts/ and .claude/."""
    here = (start or Path.cwd()).resolve()
    for candidate in (here, *here.parents):
        if (candidate / "artifacts").is_dir() and (candidate / ".claude").is_dir():
            return candidate
    raise PathError(
        f"could not locate the APEX repo root above {here} "
        "(expected a directory containing both artifacts/ and .claude/)"
    )


def day_dir(root: Path, day: str) -> Path:
    return root / "artifacts" / "flow-packets" / validate_day(day)


def flow_packet_path(root: Path, day: str, flow_id: str) -> Path:
    """Locate the flow packet for a day/flow.

    Live naming is `flow_packet-<day>-<flow_id>.md`; the glob keeps this working if
    the prefix convention shifts, and a multiple match is an error rather than a
    silent first-wins pick.
    """
    validate_flow(flow_id)
    folder = day_dir(root, day)
    if not folder.is_dir():
        raise PathError(f"no flow-packet directory for day {day}: {folder}")
    matches = sorted(p for p in folder.glob(f"*{flow_id}.md") if "flow_packet" in p.name)
    if not matches:
        raise PathError(f"no flow packet for {flow_id} in {folder}")
    if len(matches) > 1:
        raise PathError(
            f"ambiguous flow packet for {flow_id}: {[m.name for m in matches]}"
        )
    return matches[0]


def execution_dir(root: Path, day: str, flow_id: str) -> Path:
    """FEE's entire write surface for one flow."""
    return day_dir(root, day) / "execution" / validate_flow(flow_id)


def frozen_plan_path(root: Path, day: str, flow_id: str) -> Path:
    return execution_dir(root, day, flow_id) / "execution-plan.frozen.json"


def ledger_path(root: Path, day: str, flow_id: str) -> Path:
    return execution_dir(root, day, flow_id) / "run-ledger.jsonl"


def turns_dir(root: Path, day: str, flow_id: str) -> Path:
    return execution_dir(root, day, flow_id) / "turns"


def produced_dir(root: Path, day: str, flow_id: str) -> Path:
    return execution_dir(root, day, flow_id) / "produced"


def unresolved_refs_path(root: Path, day: str, flow_id: str) -> Path:
    return execution_dir(root, day, flow_id) / "unresolved-refs.md"


def skip_marker_path(root: Path, day: str, flow_id: str) -> Path:
    return execution_dir(root, day, flow_id) / "skipped-flow-marker.md"


def evidence_bundle_path(root: Path, day: str, flow_id: str) -> Path:
    return execution_dir(root, day, flow_id) / "evidence-bundle.md"


def halt_report_path(root: Path, day: str, flow_id: str) -> Path:
    return execution_dir(root, day, flow_id) / "halt-report.md"


def lock_path(root: Path, day: str, flow_id: str) -> Path:
    return execution_dir(root, day, flow_id) / ".run.lock"


def prompt_body_path(root: Path, day: str, packet_id: str) -> Path:
    """Where a materialized prompt body is expected to live.

    Gate-batch item 1. Until PrecapNextDay writes these, M1 halts with an
    unresolved-refs report rather than inventing a body.
    """
    return day_dir(root, day) / "prompt-packs" / "bodies" / f"{packet_id}.md"


def resolve_repo_relative(root: Path, ref: str) -> Path:
    """Resolve a repo-relative artifact reference, refusing escapes from the root."""
    candidate = (root / ref).resolve()
    if root.resolve() not in (candidate, *candidate.parents):
        raise PathError(f"reference escapes the repo root: {ref!r}")
    return candidate


def sha256_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()
