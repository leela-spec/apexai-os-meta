"""FEE module M8 -- the dump emitter. Stdlib only, per D-I2.

Assembles captured turns into an evidence bundle shaped for step 5
(`apex-evidence-normalize`), or a `skipped_flow_marker` when a flow was skipped.

Ownership boundary, non-negotiable: FEE prepares step 5's *input*. It never writes
`normalized-raw-flow-dump-<flow_id>.md`, and it never sets `operator_validation`,
`authority.state` beyond `candidate`, or any gate field. The independent
normalization pass stays independent.

Only three fields must survive for step 5 to resolve context -- `flow_id`,
`execution_day`, `source_flow_packet_ref` -- plus `produced_outputs` kept distinct
from the narrative. Everything else is structure the engine has for free.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from . import compile as m1, ledger as m6, paths

COMPLETION_STATES = (
    "completed",
    "partially_completed",
    "skipped",
    "blocked",
    "abandoned",
    "unknown",
)


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# Strings YAML would silently coerce to a non-string type must be quoted. This
# matters concretely: `execution_day: 2026-07-13` unquoted becomes a date object,
# and execution_day is one of the three fields step 5 requires to resolve context.
_YAML_COERCIBLE = re.compile(
    r"""^(?:
          \d{4}-\d{2}-\d{2}(?:[T ].*)?    # date / timestamp
        | [-+]?\d+                        # int
        | [-+]?\d*\.\d+(?:[eE][-+]?\d+)?  # float
        | 0[xXoObB][0-9a-fA-F_]+          # hex / octal / binary
        | [-+]?\.(?:inf|Inf|INF)|\.(?:nan|NaN|NAN)
        | (?:true|True|TRUE|false|False|FALSE)
        | (?:null|Null|NULL|~)
        | (?:yes|Yes|YES|no|No|NO|on|On|ON|off|Off|OFF)   # YAML 1.1 booleans
        )$""",
    re.VERBOSE,
)


def _yaml_scalar(value) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    needs_quoting = (
        text == ""
        or text.strip() != text
        or any(ch in text for ch in ':"\n')
        # Only space-hash opens a comment, mirroring the reader's _strip_comment.
        # That keeps `../handoff/F.md#F1` unquoted, as the live artifacts write it.
        or " #" in text
        or text.startswith("#")
        or text[0] in "-?*&!|>%@`[]{},'"
        or bool(_YAML_COERCIBLE.match(text))
    )
    if needs_quoting:
        escaped = text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
        return f'"{escaped}"'
    return text


def _yaml_block(data: dict, indent: int = 0) -> list[str]:
    """Render a nested dict as block YAML. Emitter-side only; no parser needed."""
    lines: list[str] = []
    pad = " " * indent
    for key, value in data.items():
        if isinstance(value, dict):
            lines.append(f"{pad}{key}:")
            lines.extend(_yaml_block(value, indent + 2))
        elif isinstance(value, list):
            if not value:
                lines.append(f"{pad}{key}: []")
                continue
            lines.append(f"{pad}{key}:")
            for item in value:
                if isinstance(item, dict):
                    rendered = _yaml_block(item, indent + 4)
                    first = rendered[0].lstrip()
                    lines.append(f"{pad}  - {first}")
                    lines.extend(rendered[1:])
                else:
                    lines.append(f"{pad}  - {_yaml_scalar(item)}")
        else:
            lines.append(f"{pad}{key}: {_yaml_scalar(value)}")
    return lines


def emit_skip_marker(root: Path, day: str, flow_id: str) -> Path:
    """Emit a skipped_flow_marker -- M8's `emits_instead_when_no_evidence` path."""
    plan = m1.load_plan(root, day, flow_id)
    if not m1.verify_plan_hash(plan):
        raise m6.LedgerError("frozen plan hash mismatch; refusing to emit (exit 4)")
    if plan.get("kind") != "skip_flow":
        raise ValueError(
            f"plan kind is {plan.get('kind')!r}, not skip_flow; use `emit` for evidence bundles"
        )

    identity = plan.get("identity") or {}
    skip = plan.get("skip") or {}
    execution_day = identity.get("execution_day") or day

    resolved_flow_id = identity.get("flow_id") or flow_id
    packet_ref = identity.get("source_flow_packet_ref") or {}

    # Envelope-first, matching every other artifact in this family.
    envelope = {
        "envelope_version": 1,
        "packet_type": "skipped_flow_marker",
        "gate": "G3",
        "packet_id": f"skipped_flow_marker-{execution_day}-{resolved_flow_id}",
        "produced_by": "fee",
        "accountability": "meta_ops",
        "lifecycle_stage": "proposal",
        "status": "skipped",
        "target_surface": "none",
        "next_state": (
            f"{resolved_flow_id} recorded as a skip for {execution_day}; this marker is the "
            "G3 evidence, independently dispatchable to normalize/recap."
        ),
        "prerequisites": [packet_ref.get("flow_packet_path_or_label")]
        if packet_ref.get("flow_packet_path_or_label")
        else [],
        "expected_action": "operator reviews at G3, then dispatches apex-evidence-normalize",
        "sources": [packet_ref.get("flow_packet_path_or_label")]
        if packet_ref.get("flow_packet_path_or_label")
        else [],
        "uncertainties": [],
        "unresolved_risk": "none",
        "stop_condition": (
            "Halt skip handling if the operator names urgent work for this flow -- "
            "convert to an executed flow instead."
        ),
        "authority": {"state": "candidate", "basis_digest": None, "verification_ref": None},
        "operator_validation": "not_requested",
    }

    marker = {
        "artifact_name": "skipped_flow_marker",
        "marker_id": skip.get("marker_id") or f"skipped_flow_marker_{execution_day}_{flow_id}",
        # The three fields step 5 requires to resolve context.
        "flow_id": identity.get("flow_id") or flow_id,
        "execution_day": execution_day,
        "source_flow_packet_ref": identity.get("source_flow_packet_ref") or {},
        "project": identity.get("project"),
        "skip_status": skip.get("skip_status") or "planned_skip",
        "skip_reason": skip.get("skip_reason"),
        "carry_forward_policy": skip.get("carry_forward_policy"),
        "next_review_point": skip.get("next_review_point"),
        "produced_outputs": [],
        "completion_state": "skipped",
        "produced_by": "fee",
        "emitted_at": _now(),
        "run_id": plan.get("run_id"),
        "plan_hash": plan.get("plan_hash"),
        # FEE never advances authority or touches a gate field.
        "authority": {"state": "candidate", "basis_digest": None, "verification_ref": None},
        "operator_validation": "not_requested",
    }

    lines = [
        f"# skipped_flow_marker -- {execution_day} {resolved_flow_id}",
        "",
        "> Emitted by FEE (execution substrate for step 4 of the Weekly Orchestrator). "
        "G3 remains a human gate; this artifact is `candidate` and unvalidated.",
        "",
        "```yaml",
        *_yaml_block({"handoff_envelope": envelope}),
        "```",
        "",
        "```yaml",
        *_yaml_block({"skipped_flow_marker": marker}),
        "```",
        "",
    ]

    target = paths.skip_marker_path(root, day, flow_id)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines), encoding="utf-8")

    led = m6.Ledger(paths.ledger_path(root, day, flow_id), plan["run_id"], plan["plan_hash"])
    led.append("run_completed", note="skipped_flow_marker emitted")
    return target


def collect_turns(root: Path, day: str, flow_id: str) -> list[dict]:
    """Read every captured turn's sidecar metadata, in step order."""
    turns = paths.turns_dir(root, day, flow_id)
    if not turns.is_dir():
        return []
    metas: list[dict] = []
    for meta_path in sorted(turns.glob("*.meta.json")):
        metas.append(json.loads(meta_path.read_text(encoding="utf-8")))
    return metas


def derive_completion_state(plan: dict, captured: set[str]) -> str:
    """Completion is evidence-derived, never asserted by a model (D-M5)."""
    steps = plan.get("steps") or []
    if not steps:
        return "unknown"
    total = {step["step_id"] for step in steps}
    if captured >= total:
        return "completed"
    if captured:
        return "partially_completed"
    return "unknown"
