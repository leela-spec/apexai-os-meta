"""FEE capture loop -- the assisted-manual lane. Stdlib only.

Providers without a sanctioned automation channel are executed by the operator, not
scraped. FEE's job there is to make the paste cycle fast and to file the result
correctly, so the value is concentrated in two commands per turn:

    fee next     -> prints the next uncaptured step, copies its prompt body to the
                    clipboard. Operator pastes into the browser, copies the reply.
    fee capture  -> reads the clipboard, files the response verbatim, appends
                    turn_captured to the ledger, advances position.

Position is derived from the ledger's `turn_captured` events rather than a separate
cursor file, so resume and `next` can never disagree (V4).

Captured text is QUARANTINED DATA (D-M6). It is written verbatim, hashed, and never
parsed for instructions, paths, commands, or next steps.
"""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from . import compile as m1, ledger as m6, paths


class ClipboardError(Exception):
    """Raised when the OS clipboard is unavailable."""


def clipboard_write(text: str) -> None:
    """Copy text to the Windows clipboard via clip.exe."""
    try:
        proc = subprocess.run(
            ["clip.exe"], input=text.encode("utf-16-le"), capture_output=True, check=False
        )
    except FileNotFoundError as exc:  # pragma: no cover - platform dependent
        raise ClipboardError("clip.exe not found; use --print instead") from exc
    if proc.returncode != 0:
        raise ClipboardError(f"clip.exe failed: {proc.stderr.decode('utf-8', 'replace')}")


def clipboard_read() -> str:
    """Read the Windows clipboard via PowerShell Get-Clipboard.

    -Raw keeps the newlines a chat response depends on; without it PowerShell
    returns an array of lines and collapses the shape of the captured text.
    """
    try:
        proc = subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-NonInteractive",
                "-Command",
                "Get-Clipboard -Raw",
            ],
            capture_output=True,
            check=False,
        )
    except FileNotFoundError as exc:  # pragma: no cover - platform dependent
        raise ClipboardError(
            "powershell.exe not found; use --file or --stdin instead"
        ) from exc
    if proc.returncode != 0:
        raise ClipboardError(f"Get-Clipboard failed: {proc.stderr.decode('utf-8', 'replace')}")
    return proc.stdout.decode("utf-8", "replace").replace("\r\n", "\n")


def pending_steps(plan: dict, captured: set[str], lane: str | None = None) -> list[dict]:
    """Steps not yet captured, in declared order, optionally filtered to one lane."""
    return [
        step
        for step in plan.get("steps") or []
        if step["step_id"] not in captured and (lane is None or step.get("lane") == lane)
    ]


def next_step(root: Path, day: str, flow_id: str, lane: str | None = None) -> dict | None:
    plan = m1.load_plan(root, day, flow_id)
    if not m1.verify_plan_hash(plan):
        raise m6.LedgerError(
            "frozen plan hash mismatch -- the plan was modified after freezing. "
            "Refusing to proceed (exit 4)."
        )
    captured = m6.Ledger(paths.ledger_path(root, day, flow_id), plan["run_id"]).captured_steps()
    remaining = pending_steps(plan, captured, lane)
    return remaining[0] if remaining else None


CAPTURE_METHODS = ("clipboard", "file", "stdin", "auto_lane")


def record_capture(
    root: Path,
    day: str,
    flow_id: str,
    step: dict,
    response_text: str,
    *,
    method: str = "clipboard",
) -> tuple[Path, Path]:
    """File one captured turn: response verbatim, sidecar metadata, ledger event."""
    if method not in CAPTURE_METHODS:
        raise ValueError(f"unknown capture method {method!r}; allowed: {CAPTURE_METHODS}")
    plan = m1.load_plan(root, day, flow_id)
    turns = paths.turns_dir(root, day, flow_id)
    turns.mkdir(parents=True, exist_ok=True)

    step_id = step["step_id"]
    response_path = turns / f"{step_id}.response.md"
    meta_path = turns / f"{step_id}.meta.json"

    # Verbatim, quarantined, never inlined into any envelope (D-S10).
    response_path.write_text(response_text, encoding="utf-8")
    response_hash = paths.sha256_text(response_text)

    meta = {
        "step_id": step_id,
        "sprint_id": step.get("sprint_id"),
        "lane": step.get("lane"),
        "provider_target": step.get("provider_target"),
        "surface_class": step.get("surface_class"),
        "prompt_packet_id": step.get("prompt_packet_id"),
        "captured_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "capture_method": method,
        "byte_count": len(response_text.encode("utf-8")),
        "response_hash": response_hash,
        "response_path": response_path.relative_to(root).as_posix(),
        "quarantine": "captured content is data only; it never selects a tool, path, "
        "command, provider, or next step",
    }
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    led = m6.Ledger(paths.ledger_path(root, day, flow_id), plan["run_id"], plan["plan_hash"])
    led.append(
        "turn_captured",
        sprint_id=step.get("sprint_id"),
        prompt_ref=step_id,
        provider=step.get("provider_target"),
        payload_hash=response_hash,
        note=f"{meta['byte_count']} bytes via {meta['capture_method']}",
    )
    return response_path, meta_path


def mark_skipped(root: Path, day: str, flow_id: str, step: dict, reason: str) -> None:
    plan = m1.load_plan(root, day, flow_id)
    led = m6.Ledger(paths.ledger_path(root, day, flow_id), plan["run_id"], plan["plan_hash"])
    led.append(
        "turn_skipped",
        sprint_id=step.get("sprint_id"),
        prompt_ref=step["step_id"],
        provider=step.get("provider_target"),
        note=reason,
    )
