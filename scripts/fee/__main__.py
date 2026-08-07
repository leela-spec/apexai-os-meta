"""FEE command-line entrypoint.

    python -m scripts.fee plan   --day 20260713 --flow F1
    python -m scripts.fee status --day 20260713
    python -m scripts.fee next   --day 20260713 --flow F1
    python -m scripts.fee capture --day 20260713 --flow F1 [--file X | --stdin]
    python -m scripts.fee emit   --day 20260713 --flow F1

Exit codes (03-micro-implementation-map cli_contract):
    0 clean · 2 halted_needs_operator · 3 plan_invalid · 4 hash_mismatch
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__, artifacts, capture as cap, compile as m1, emit as m8, ledger as m6, paths


def _root(args) -> Path:
    return paths.repo_root(Path(args.root) if args.root else None)


def _print_plan_summary(plan: dict) -> None:
    identity = plan.get("identity") or {}
    print(f"  run_id            {plan.get('run_id')}")
    print(f"  plan_hash         {plan.get('plan_hash')}")
    print(f"  kind              {plan.get('kind')}")
    print(f"  execution_day     {identity.get('execution_day')}")
    print(f"  flow / project    {identity.get('flow_id')} / {identity.get('project')}")
    print(f"  plan_confidence   {plan.get('plan_confidence')}")
    print(f"  pre-run review    {plan.get('requires_pre_run_review')}")
    if plan.get("degraded_flags"):
        print(f"  degraded_flags    {', '.join(plan['degraded_flags'])}")

    if plan.get("kind") == "skip_flow":
        skip = plan.get("skip") or {}
        print("\n  SKIP PLAN -- no prompt pack or prompt body required")
        print(f"    skip_status         {skip.get('skip_status')}")
        print(f"    carry_forward       {skip.get('carry_forward_policy')}")
        print(f"    next_review_point   {skip.get('next_review_point')}")
        if skip.get("skip_reason"):
            print(f"    reason              {skip['skip_reason']}")
        return

    lanes = plan.get("lanes") or {}
    auto = lanes.get(m1.AUTO_LANE) or []
    operator = lanes.get(m1.OPERATOR_LANE) or []
    print(f"\n  lanes             auto={len(auto)} operator={len(operator)}")
    print(f"    {m1.AUTO_LANE:<14} unattended-eligible (Claude sanctioned channel)")
    print(f"    {m1.OPERATOR_LANE:<14} assisted worklist (operator present)")

    print("\n  Action set, in declared order:")
    for step in plan.get("steps") or []:
        body = step.get("prompt_body")
        body_state = f"{len(body)} chars" if body else "UNRESOLVED"
        print(
            f"    [{step.get('lane','?'):<13}] {step.get('step_id'):<16} "
            f"{str(step.get('provider_target')):<20} {str(step.get('surface_class')):<32} "
            f"body={body_state}"
        )
        if step.get("sprint_goal"):
            print(f"                      goal: {step['sprint_goal']}")


def _print_diagnostics(result: m1.CompileResult) -> None:
    if not result.diagnostics:
        return
    order = {"halt": 0, "degrade": 1, "info": 2}
    print("\n  Diagnostics:")
    for diagnostic in sorted(result.diagnostics, key=lambda d: order.get(d.severity, 9)):
        label = {"halt": "HALT", "degrade": "DEGRADE", "info": "info"}[diagnostic.severity]
        print(f"    {label:<8} {diagnostic.code}: {diagnostic.message}")


# Commands -------------------------------------------------------------------


def cmd_plan(args) -> int:
    root = _root(args)
    print(f"FEE {__version__} -- compile (M1). No network access.\n")
    print(f"  repo              {root}")
    try:
        result = m1.compile_flow(root, args.day, args.flow)
    except (paths.PathError, artifacts.ArtifactParseError, artifacts.UnsupportedConstruct) as exc:
        print(f"\n  HALT  {type(exc).__name__}: {exc}", file=sys.stderr)
        return m1.EXIT_PLAN_INVALID

    if result.plan:
        _print_plan_summary(result.plan)
    _print_diagnostics(result)

    if result.exit_code == m1.EXIT_OK and result.plan:
        target = m1.write_plan(root, args.day, args.flow, result.plan)
        led = m6.Ledger(
            paths.ledger_path(root, args.day, args.flow),
            result.plan["run_id"],
            result.plan["plan_hash"],
        )
        led.append("plan_frozen", note=f"kind={result.plan['kind']}")
        print(f"\n  frozen plan       {target.relative_to(root).as_posix()}")
        print(f"  ledger            {led.path.relative_to(root).as_posix()}")
        print("\n  Status: COMPILED. Inspect the action set above before running.")
    else:
        report = m1.write_halt_report(root, args.day, args.flow, result)
        print(f"\n  halt report       {report.relative_to(root).as_posix()}")
        print("\n  Status: HALTED. No plan committed, no default invented.")
    return result.exit_code


def cmd_status(args) -> int:
    root = _root(args)
    folder = paths.day_dir(root, args.day)
    print(f"FEE {__version__} -- status for {args.day}\n")
    if not folder.is_dir():
        print(f"  no flow-packet directory: {folder.relative_to(root).as_posix()}")
        return m1.EXIT_OK

    packets = sorted(p for p in folder.glob("*.md") if "flow_packet" in p.name)
    if not packets:
        print("  no flow packets found")
        return m1.EXIT_OK

    print(f"  {'flow':<6} {'packet status':<22} {'plan':<10} {'hash ok':<8} events")
    for packet in packets:
        flow = packet.stem.split("-")[-1]
        try:
            data, _ = artifacts.load_artifact(packet)
            status = artifacts.dig(data, "flow_packet", "flow_identity", "flow_status") or "?"
        except Exception as exc:  # noqa: BLE001 - status must never crash on one bad file
            print(f"  {flow:<6} unreadable: {type(exc).__name__}")
            continue
        plan_path = paths.frozen_plan_path(root, args.day, flow)
        if plan_path.exists():
            plan = m1.load_plan(root, args.day, flow)
            plan_state = plan.get("kind", "?")
            hash_ok = "yes" if m1.verify_plan_hash(plan) else "NO"
        else:
            plan_state, hash_ok = "-", "-"
        events = len(m6.read_events(paths.ledger_path(root, args.day, flow)))
        print(f"  {flow:<6} {status:<22} {plan_state:<10} {hash_ok:<8} {events}")
    return m1.EXIT_OK


def cmd_next(args) -> int:
    root = _root(args)
    lane = args.lane
    try:
        step = cap.next_step(root, args.day, args.flow, lane)
    except m6.LedgerError as exc:
        print(f"FEE: {exc}", file=sys.stderr)
        return m1.EXIT_HASH_MISMATCH

    if step is None:
        scope = f" in {lane}" if lane else ""
        print(f"No uncaptured steps remain{scope} for {args.day} {args.flow}.")
        print("Next: python -m scripts.fee emit --day %s --flow %s" % (args.day, args.flow))
        return m1.EXIT_OK

    body = step.get("prompt_body")
    print(f"FEE -- next step for {args.day} {args.flow}\n")
    print(f"  step_id     {step['step_id']}")
    print(f"  lane        {step.get('lane')}")
    print(f"  provider    {step.get('provider_target')}   ({step.get('surface_class')})")
    if step.get("sprint_goal"):
        print(f"  goal        {step['sprint_goal']}")
    for hint in step.get("capture_hints") or []:
        print(f"  capture     {hint}")

    if not body:
        print("\n  PROMPT BODY UNRESOLVED -- nothing to copy.")
        print("  Expected at:", step.get("prompt_body_ref") or "(no packet id declared)")
        return m1.EXIT_NEEDS_OPERATOR

    if args.print_body:
        print("\n" + "-" * 72)
        print(body)
        print("-" * 72)
    else:
        try:
            cap.clipboard_write(body)
            print(f"\n  Prompt body ({len(body)} chars) copied to the clipboard.")
        except cap.ClipboardError as exc:
            print(f"\n  clipboard unavailable ({exc}); body follows:\n")
            print("-" * 72)
            print(body)
            print("-" * 72)

    print(
        f"\n  Paste into {step.get('provider_target')}, copy the reply, then:\n"
        f"    python -m scripts.fee capture --day {args.day} --flow {args.flow}"
    )
    return m1.EXIT_OK


def cmd_capture(args) -> int:
    root = _root(args)
    try:
        step = cap.next_step(root, args.day, args.flow, args.lane)
    except m6.LedgerError as exc:
        print(f"FEE: {exc}", file=sys.stderr)
        return m1.EXIT_HASH_MISMATCH
    if step is None:
        print("Nothing pending to capture.")
        return m1.EXIT_OK

    if args.skip:
        cap.mark_skipped(root, args.day, args.flow, step, args.skip)
        print(f"  {step['step_id']} marked turn_skipped: {args.skip}")
        return m1.EXIT_OK

    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")
        method, source = "file", args.file
    elif args.stdin:
        text = sys.stdin.read()
        method = source = "stdin"
    else:
        try:
            text = cap.clipboard_read()
            method = source = "clipboard"
        except cap.ClipboardError as exc:
            print(f"FEE: {exc}", file=sys.stderr)
            return m1.EXIT_NEEDS_OPERATOR

    if not text.strip():
        print(
            f"FEE: {source} is empty -- refusing to file an empty capture for "
            f"{step['step_id']}.",
            file=sys.stderr,
        )
        return m1.EXIT_NEEDS_OPERATOR

    response_path, _ = cap.record_capture(
        root, args.day, args.flow, step, text, method=method
    )
    print(f"FEE -- captured {step['step_id']} from {source}")
    print(f"  {len(text.encode('utf-8'))} bytes -> {response_path.relative_to(root).as_posix()}")
    remaining = cap.pending_steps(
        m1.load_plan(root, args.day, args.flow),
        m6.Ledger(paths.ledger_path(root, args.day, args.flow), "-").captured_steps(),
        args.lane,
    )
    print(f"  {len(remaining)} step(s) still pending.")
    return m1.EXIT_OK


def cmd_emit(args) -> int:
    root = _root(args)
    plan = m1.load_plan(root, args.day, args.flow)
    if not m1.verify_plan_hash(plan):
        print("FEE: frozen plan hash mismatch; refusing to emit.", file=sys.stderr)
        return m1.EXIT_HASH_MISMATCH

    if plan.get("kind") == "skip_flow":
        target = m8.emit_skip_marker(root, args.day, args.flow)
        print(f"FEE -- emitted skipped_flow_marker")
        print(f"  {target.relative_to(root).as_posix()}")
        print("\n  Next: G3 (human gate), then apex-evidence-normalize.")
        return m1.EXIT_OK

    print(
        "FEE: evidence-bundle emission is Phase 2. The skip path is available now;\n"
        "     captured turns live under turns/ and are ready for the bundle assembler.",
        file=sys.stderr,
    )
    return m1.EXIT_NEEDS_OPERATOR


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m scripts.fee",
        description="FEE -- execution substrate for step 4 of the Weekly Orchestrator. "
        "Not an orchestration system.",
    )
    parser.add_argument("--root", help="repo root (default: discovered from cwd)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan_parser = subparsers.add_parser(
        "plan", help="compile + freeze + validate a flow. No network."
    )
    plan_parser.add_argument("--day", required=True, help="execution day, YYYYMMDD")
    plan_parser.add_argument("--flow", required=True, help="flow id, F1-F4")
    plan_parser.set_defaults(func=cmd_plan)

    status_parser = subparsers.add_parser("status", help="loop position for a day")
    status_parser.add_argument("--day", required=True, help="execution day, YYYYMMDD")
    status_parser.set_defaults(func=cmd_status)

    next_parser = subparsers.add_parser(
        "next", help="print the next uncaptured step and copy its prompt body"
    )
    next_parser.add_argument("--day", required=True)
    next_parser.add_argument("--flow", required=True)
    next_parser.add_argument(
        "--lane", choices=[m1.AUTO_LANE, m1.OPERATOR_LANE], help="restrict to one lane"
    )
    next_parser.add_argument(
        "--print-body", action="store_true", help="print the body instead of copying it"
    )
    next_parser.set_defaults(func=cmd_next)

    capture_parser = subparsers.add_parser(
        "capture", help="file the response for the next pending step"
    )
    capture_parser.add_argument("--day", required=True)
    capture_parser.add_argument("--flow", required=True)
    capture_parser.add_argument(
        "--lane", choices=[m1.AUTO_LANE, m1.OPERATOR_LANE], help="restrict to one lane"
    )
    source = capture_parser.add_mutually_exclusive_group()
    source.add_argument("--file", help="read the response from a file")
    source.add_argument("--stdin", action="store_true", help="read the response from stdin")
    capture_parser.add_argument(
        "--skip", metavar="REASON", help="mark the step turn_skipped instead of capturing"
    )
    capture_parser.set_defaults(func=cmd_capture)

    emit_parser = subparsers.add_parser(
        "emit", help="emit the step-5 input (skipped_flow_marker, or the evidence bundle)"
    )
    emit_parser.add_argument("--day", required=True)
    emit_parser.add_argument("--flow", required=True)
    emit_parser.set_defaults(func=cmd_emit)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except paths.PathError as exc:
        print(f"FEE: {exc}", file=sys.stderr)
        return m1.EXIT_PLAN_INVALID


if __name__ == "__main__":
    sys.exit(main())
