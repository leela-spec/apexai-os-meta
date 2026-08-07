"""FEE module M1 -- the pack compiler. Stdlib only, no network access, ever.

Reads a flow packet plus its flow_prompt_pack, resolves every ref to concrete
content, and emits `execution-plan.frozen.json` with a stable hash. Then stops.

This is the load-bearing half of D-M6: the complete set of possible actions is
enumerated *before* any network contact, so nothing captured later can add a step.
`prompt_body` is fully resolved here and `declared_follow_ups` is a closed list.

Halt discipline (no silent defaults, ever):
  * provider_unspecified                       -> exit 3, ask the operator
  * pack_status blocked_by_missing_operator_decision -> exit 3
  * a prompt body that does not exist on disk  -> exit 3 + unresolved-refs.md
  * supplemental_api_low_cost                  -> exit 3 (M2 refuses this class)

Lane partitioning answers the night-run collision: only the Claude lane has a
sanctioned automation channel, so only it can run unattended. Everything else
becomes an operator worklist.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from . import artifacts, paths

SCHEMA_VERSION = 1

EXIT_OK = 0
EXIT_NEEDS_OPERATOR = 2
EXIT_PLAN_INVALID = 3
EXIT_HASH_MISMATCH = 4

AUTO_LANE = "auto_lane"
OPERATOR_LANE = "operator_lane"

# Surface classes the Claude sanctioned channel can drive unattended.
_AUTOMATABLE_SURFACES = frozenset(
    {"subscription_frontier_chat", "subscription_frontier_reasoning", "long_context_surface"}
)
# Executable by a human, but never unattended.
_OPERATOR_SURFACES = frozenset(
    {"deep_research_surface", "code_agent_surface", "agent_run_surface"}
)
# M2 refuses this class outright rather than silently metering spend.
_REFUSED_SURFACES = frozenset({"supplemental_api_low_cost"})

_SKIPPED_FLOW_STATES = frozenset({"skipped", "planned_skip"})

DEFAULT_TIMEOUT_S = 600
DEFAULT_RETRY_BUDGET = 1


@dataclass
class Diagnostic:
    code: str
    severity: str  # halt | degrade | info
    message: str
    where: str | None = None

    def as_dict(self) -> dict:
        return {
            "code": self.code,
            "severity": self.severity,
            "message": self.message,
            "where": self.where,
        }


@dataclass
class CompileResult:
    status: str  # compiled | compiled_skip | halted
    exit_code: int
    plan: dict | None = None
    diagnostics: list[Diagnostic] = field(default_factory=list)

    @property
    def halts(self) -> list[Diagnostic]:
        return [d for d in self.diagnostics if d.severity == "halt"]

    @property
    def degradations(self) -> list[Diagnostic]:
        return [d for d in self.diagnostics if d.severity == "degrade"]


# Pack shape helpers ---------------------------------------------------------


def _pack_root(pack_data: dict) -> dict:
    """Live packs nest their identity under `flow_prompt_pack_status`.

    The contract describes top-level keys; the on-disk artifacts and the template
    both wrap them. Accept either rather than depending on which one is current.
    """
    for key in ("flow_prompt_pack", "flow_prompt_pack_status"):
        node = pack_data.get(key)
        if isinstance(node, dict):
            return node
    return {}


def _sprint_rows_from_tables(tables: list[list[dict]]) -> list[dict]:
    """Recover sprint rows from the pack's markdown pipe table.

    The live packs carry sprint sequences as a table, not YAML, so the table is a
    first-class input rather than a fallback.
    """
    for table in tables:
        if not table:
            continue
        headers = set(table[0])
        if any(h.lower().startswith("sprint") for h in headers) and len(headers) >= 3:
            return table
    return []


def _row_get(row: dict, *needles: str) -> str | None:
    """Fetch a table cell by fuzzy header match, since headers are prose."""
    for header, value in row.items():
        lowered = header.lower()
        if any(needle in lowered for needle in needles):
            text = (value or "").strip()
            return text or None
    return None


def _classify_lane(provider: str, surface: str) -> tuple[str | None, Diagnostic | None]:
    """Decide which lane a step belongs to, or refuse it."""
    if surface in _REFUSED_SURFACES:
        return None, Diagnostic(
            "surface_refused",
            "halt",
            f"surface_class {surface!r} is refused: it crosses the PrecapNextDay "
            "API-frontier boundary. Ask the operator to re-route.",
        )
    if provider == "provider_unspecified" or surface == "provider_unspecified":
        return None, Diagnostic(
            "provider_unspecified",
            "halt",
            "provider_unspecified reached the compiler; routing must be resolved "
            "upstream by AIRouting. No silent default is applied.",
        )
    if provider == "OpenRouter_later":
        return None, Diagnostic(
            "provider_placeholder",
            "halt",
            "provider_target OpenRouter_later is a placeholder, not a live target "
            "(AIRouting OpenRouter_policy.current_status: later_placeholder).",
        )
    if surface in _OPERATOR_SURFACES:
        return OPERATOR_LANE, None
    if provider == "Claude" and surface in _AUTOMATABLE_SURFACES:
        return AUTO_LANE, None
    return OPERATOR_LANE, None


# Compilation ---------------------------------------------------------------


def compile_flow(root: Path, day: str, flow_id: str) -> CompileResult:
    """Compile one flow into a frozen execution plan. Never touches the network."""
    diagnostics: list[Diagnostic] = []

    packet_path = paths.flow_packet_path(root, day, flow_id)
    packet_data, _ = artifacts.load_artifact(packet_path)
    packet = packet_data.get("flow_packet")
    if not isinstance(packet, dict):
        return CompileResult(
            "halted",
            EXIT_PLAN_INVALID,
            diagnostics=[
                Diagnostic(
                    "packet_shape",
                    "halt",
                    "flow packet has no `flow_packet` block",
                    packet_path.name,
                )
            ],
        )

    identity = packet.get("flow_identity") or {}
    execution_day = str(packet.get("execution_day") or day)
    project = identity.get("project")
    flow_status = identity.get("flow_status")
    sprint_plan = packet.get("flow_sprint_plan") or {}

    source_flow_packet_ref = {
        "flow_packet_id": packet.get("packet_id"),
        "flow_packet_path_or_label": packet_path.relative_to(root).as_posix(),
        "source_status": packet.get("review_status") or packet.get("validation_status"),
    }

    plan_identity = {
        "execution_day": execution_day,
        "flow_id": identity.get("flow_id") or flow_id,
        "project": project,
        "source_flow_packet_ref": source_flow_packet_ref,
        "flow_prompt_pack_ref": None,
    }

    # --- Skip path. Available today against real data; needs no pack and no body.
    if flow_status in _SKIPPED_FLOW_STATES or sprint_plan.get("sprint_policy") == "skipped":
        marker = packet_data.get("skipped_flow_marker_template") or {}
        diagnostics.append(
            Diagnostic(
                "flow_skipped",
                "info",
                f"flow_status={flow_status!r}, sprint_policy="
                f"{sprint_plan.get('sprint_policy')!r}: compiling a skip plan. "
                "No prompt pack or prompt body is required.",
                packet_path.name,
            )
        )
        plan = _assemble_plan(
            day=day,
            flow_id=flow_id,
            kind="skip_flow",
            identity=plan_identity,
            steps=[],
            plan_confidence="normal",
            requires_pre_run_review=False,
            degraded_flags=[],
            diagnostics=diagnostics,
            skip={
                "skip_status": marker.get("skip_status") or "planned_skip",
                "skip_reason": marker.get("skip_reason"),
                "carry_forward_policy": marker.get("carry_forward_policy"),
                "next_review_point": marker.get("next_review_point"),
                "marker_id": marker.get("marker_id"),
            },
        )
        return CompileResult("compiled_skip", EXIT_OK, plan, diagnostics)

    # --- Executable path. Resolve the pack by following the packet's own ref (F3).
    pack_ref = packet.get("prompt_pack_ref") or {}
    pack_rel = pack_ref.get("flow_prompt_pack_path")
    pack_status_in_packet = pack_ref.get("prompt_pack_status")

    if not pack_rel:
        diagnostics.append(
            Diagnostic(
                "pack_ref_missing",
                "halt",
                "flow packet declares no prompt_pack_ref.flow_prompt_pack_path, so "
                "the pack cannot be located. FEE does not guess a path by convention.",
                packet_path.name,
            )
        )
        return CompileResult("halted", EXIT_PLAN_INVALID, None, diagnostics)

    plan_identity["flow_prompt_pack_ref"] = {
        "flow_prompt_pack_path": pack_rel,
        "prompt_pack_status": pack_status_in_packet,
    }

    pack_path = paths.resolve_repo_relative(root, pack_rel)
    if not pack_path.exists():
        diagnostics.append(
            Diagnostic(
                "pack_missing",
                "halt",
                f"prompt pack does not exist: {pack_rel}. PrecapNextDay has not "
                "written it (filesystem_write_required is false upstream).",
                packet_path.name,
            )
        )
        return CompileResult("halted", EXIT_PLAN_INVALID, None, diagnostics)

    pack_data, pack_tables = artifacts.load_artifact(pack_path)
    pack = _pack_root(pack_data)
    routing = pack_data.get("routing_usage_summary") or {}

    pack_status = pack.get("pack_status")
    generation_mode = pack.get("generation_mode")
    surface_class = routing.get("primary_surface_class") or "provider_unspecified"

    if pack_status == "blocked_by_missing_operator_decision":
        diagnostics.append(
            Diagnostic(
                "pack_blocked",
                "halt",
                "pack_status is blocked_by_missing_operator_decision; M1 refuses to run.",
                pack_path.name,
            )
        )
        return CompileResult("halted", EXIT_PLAN_INVALID, None, diagnostics)

    plan_confidence = "normal"
    degraded_flags: list[str] = []
    if generation_mode == "degraded_generic_prompt_mode":
        plan_confidence = "low"
        degraded_flags.append("degraded_generic_prompt_mode")
        diagnostics.append(
            Diagnostic(
                "degraded_generation_mode",
                "degrade",
                "generation_mode is degraded_generic_prompt_mode: plan_confidence low.",
                pack_path.name,
            )
        )

    requires_pre_run_review = False
    if pack_status in ("low_confidence_auto_generated", "operator_review_recommended"):
        requires_pre_run_review = True
        degraded_flags.append(str(pack_status))
        diagnostics.append(
            Diagnostic(
                "pack_needs_review",
                "degrade",
                f"pack_status is {pack_status}: requires_pre_run_review set true.",
                pack_path.name,
            )
        )

    # Sprint rows: YAML sequence if present, otherwise the pack's pipe table.
    sprint_rows = pack_data.get("sprint_prompt_sequences")
    if not isinstance(sprint_rows, list) or not sprint_rows:
        sprint_rows = _sprint_rows_from_tables(pack_tables)
        source_note = "pipe table"
    else:
        source_note = "yaml sequence"

    if not sprint_rows:
        diagnostics.append(
            Diagnostic(
                "no_sprints",
                "halt",
                "pack declares no sprint_prompt_sequences and no sprint table was found.",
                pack_path.name,
            )
        )
        return CompileResult("halted", EXIT_PLAN_INVALID, None, diagnostics)

    diagnostics.append(
        Diagnostic(
            "sprints_source",
            "info",
            f"{len(sprint_rows)} sprint row(s) read from the {source_note}.",
            pack_path.name,
        )
    )

    steps: list[dict] = []
    unresolved: list[dict] = []

    for index, row in enumerate(sprint_rows, start=1):
        sprint_id = (
            row.get("sprint_id")
            or _row_get(row, "sprint")
            or f"S{index}"
        )
        # A table's Sprint cell is just "S1"; a YAML row carries an explicit role.
        sprint_role = row.get("sprint_role")
        sprint_status = row.get("sprint_status")
        if sprint_status == "blocked":
            diagnostics.append(
                Diagnostic(
                    "sprint_blocked",
                    "info",
                    f"{sprint_id}: sprint_status blocked -- skipping this sprint only, "
                    "not aborting the flow.",
                    pack_path.name,
                )
            )
            continue

        packet_id = (
            row.get("prompt_packet_id")
            or row.get("start_prompt_ref")
            or _row_get(row, "packet", "prompt")
        )
        provider = (
            row.get("provider_target")
            or _row_get(row, "provider", "surface")
            or "provider_unspecified"
        )
        capture_hint = _row_get(row, "capture")
        goal = row.get("sprint_goal") or _row_get(row, "goal")

        lane, refusal = _classify_lane(str(provider), str(surface_class))
        if refusal is not None:
            refusal.where = f"{pack_path.name} :: {sprint_id}"
            diagnostics.append(refusal)
            continue

        step_id = f"{sprint_id}-start"
        body_path = None
        prompt_body = None
        if packet_id:
            body_path = paths.prompt_body_path(root, day, str(packet_id))
            if body_path.exists():
                prompt_body = body_path.read_text(encoding="utf-8").strip()
            else:
                unresolved.append(
                    {
                        "step_id": step_id,
                        "sprint_id": sprint_id,
                        "packet_id": str(packet_id),
                        "expected_path": body_path.relative_to(root).as_posix(),
                    }
                )
        else:
            unresolved.append(
                {
                    "step_id": step_id,
                    "sprint_id": sprint_id,
                    "packet_id": None,
                    "expected_path": None,
                }
            )

        steps.append(
            {
                "step_id": step_id,
                "sprint_id": sprint_id,
                "sprint_role": sprint_role,
                "sprint_goal": goal,
                "kind": "browser_turn",
                "lane": lane,
                "surface_class": surface_class,
                "provider_target": provider,
                "prompt_packet_id": str(packet_id) if packet_id else None,
                "prompt_body": prompt_body,
                "prompt_body_ref": (
                    body_path.relative_to(root).as_posix() if body_path else None
                ),
                "timeout_s": DEFAULT_TIMEOUT_S,
                "retry_budget": DEFAULT_RETRY_BUDGET,
                "capture_hints": [capture_hint] if capture_hint else [],
                "declared_follow_ups": [],
            }
        )

    if not steps:
        diagnostics.append(
            Diagnostic(
                "no_executable_steps",
                "halt",
                "every sprint was refused or blocked; there is nothing to execute.",
                pack_path.name,
            )
        )
        return CompileResult("halted", EXIT_PLAN_INVALID, None, diagnostics)

    if unresolved:
        for item in unresolved:
            diagnostics.append(
                Diagnostic(
                    "unresolved_ref",
                    "halt",
                    (
                        f"{item['step_id']}: no prompt body for packet "
                        f"{item['packet_id']!r}"
                        + (
                            f"; expected at {item['expected_path']}"
                            if item["expected_path"]
                            else " (the pack names no packet id at all)"
                        )
                    ),
                    pack_path.name,
                )
            )
        plan = _assemble_plan(
            day=day,
            flow_id=flow_id,
            kind="flow_execution",
            identity=plan_identity,
            steps=steps,
            plan_confidence=plan_confidence,
            requires_pre_run_review=requires_pre_run_review,
            degraded_flags=degraded_flags,
            diagnostics=diagnostics,
        )
        return CompileResult("halted", EXIT_PLAN_INVALID, plan, diagnostics)

    plan = _assemble_plan(
        day=day,
        flow_id=flow_id,
        kind="flow_execution",
        identity=plan_identity,
        steps=steps,
        plan_confidence=plan_confidence,
        requires_pre_run_review=requires_pre_run_review,
        degraded_flags=degraded_flags,
        diagnostics=diagnostics,
    )
    return CompileResult("compiled", EXIT_OK, plan, diagnostics)


def _assemble_plan(
    *,
    day: str,
    flow_id: str,
    kind: str,
    identity: dict,
    steps: list[dict],
    plan_confidence: str,
    requires_pre_run_review: bool,
    degraded_flags: list[str],
    diagnostics: list[Diagnostic],
    skip: dict | None = None,
) -> dict:
    plan = {
        "schema_version": SCHEMA_VERSION,
        "run_id": f"fee-{day}-{flow_id}-01",
        "plan_hash": None,
        "compiled_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "kind": kind,
        "identity": identity,
        "plan_confidence": plan_confidence,
        "requires_pre_run_review": requires_pre_run_review,
        "lanes": {
            AUTO_LANE: [s["step_id"] for s in steps if s.get("lane") == AUTO_LANE],
            OPERATOR_LANE: [s["step_id"] for s in steps if s.get("lane") == OPERATOR_LANE],
        },
        "steps": steps,
        "fallback_surface": "subscription_frontier_chat",
        "degraded_flags": degraded_flags,
        "diagnostics": [d.as_dict() for d in diagnostics],
    }
    if skip is not None:
        plan["skip"] = skip
    plan["plan_hash"] = plan_hash(plan)
    return plan


def canonical_payload(plan: dict) -> str:
    """The exact bytes the plan hash covers.

    `compiled_at` is excluded so replaying identical inputs reproduces an identical
    hash (V1). Everything else is included, so any tampering with the frozen action
    set is detected (V2).
    """
    payload = {k: v for k, v in plan.items() if k not in ("plan_hash", "compiled_at")}
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def plan_hash(plan: dict) -> str:
    return paths.sha256_text(canonical_payload(plan))


def verify_plan_hash(plan: dict) -> bool:
    recorded = plan.get("plan_hash")
    return bool(recorded) and recorded == plan_hash(plan)


def write_plan(root: Path, day: str, flow_id: str, plan: dict) -> Path:
    target = paths.frozen_plan_path(root, day, flow_id)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return target


def load_plan(root: Path, day: str, flow_id: str) -> dict:
    target = paths.frozen_plan_path(root, day, flow_id)
    if not target.exists():
        raise paths.PathError(f"no frozen plan at {target}; run `fee plan` first")
    return json.loads(target.read_text(encoding="utf-8"))


def write_halt_report(root: Path, day: str, flow_id: str, result: CompileResult) -> Path:
    """Write the operator-facing halt report. No silent defaults, ever.

    One report file per flow covering every halt class, not just unresolved refs --
    a `pack_missing` halt filed under `unresolved-refs.md` would misname itself.
    """
    target = paths.halt_report_path(root, day, flow_id)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# FEE compile halted -- {day} {flow_id}",
        "",
        "```yaml",
        "halt_report:",
        f"  execution_day: \"{day}\"",
        f"  flow_id: {flow_id}",
        f"  status: {result.status}",
        f"  exit_code: {result.exit_code}",
        "  authority:",
        "    state: candidate",
        "  operator_validation: not_requested",
        "```",
        "",
        "## Blocking findings",
        "",
    ]
    for diagnostic in result.halts:
        where = f" _({diagnostic.where})_" if diagnostic.where else ""
        lines.append(f"- **{diagnostic.code}** -- {diagnostic.message}{where}")
    unresolved = [d for d in result.halts if d.code == "unresolved_ref"]
    if unresolved:
        lines += [
            "",
            "## Unresolved prompt-body refs",
            "",
            "Expected location (gate-batch item 1): "
            "`artifacts/flow-packets/<day>/prompt-packs/bodies/<packet_id>.md`",
            "",
            "PrecapNextDay does not write prompt bodies to disk today "
            "(`filesystem_write_required: false`), so this halt is expected until "
            "that upstream change is gated in.",
            "",
        ]
    if result.degradations:
        lines += ["", "## Degradations (not blocking)", ""]
        for diagnostic in result.degradations:
            lines.append(f"- **{diagnostic.code}** -- {diagnostic.message}")
    lines += [
        "",
        "## What FEE did not do",
        "",
        "- No network contact. M1 has no network access by contract.",
        "- No default provider, surface, or prompt body was invented.",
        "- No frozen plan was committed for execution.",
        "",
    ]
    target.write_text("\n".join(lines), encoding="utf-8")
    return target
