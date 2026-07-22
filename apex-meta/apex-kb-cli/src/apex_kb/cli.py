from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path
from typing import Any

import click

from .config import normalize_config, preview_config
from .errors import ApexKBError
from .io import load_yaml, template
from .lifecycle import (
    continue_once,
    create_manifest,
    initial_state,
    initialize_update,
    load_run,
    next_action_text,
    status_snapshot,
    write_new_run,
)
from .retrieval import query_retrieval, retrieval_health


def emit(command: str, status: str, data: Any = None, error: ApexKBError | None = None, json_output: bool = False) -> None:
    envelope: dict[str, Any] = {"schema": "apex.kb.result.v2", "command": command, "status": status}
    if data is not None:
        envelope["data"] = data
    if error is not None:
        envelope["error"] = {"code": error.code, "message": error.message, "details": error.details}
    if json_output:
        click.echo(json.dumps(envelope, indent=2, ensure_ascii=False, sort_keys=True))
    elif error is not None:
        click.echo(f"ERROR [{error.code}]: {error.message}", err=True)
        if error.details:
            click.echo(json.dumps(error.details, indent=2, ensure_ascii=False, sort_keys=True), err=True)
    elif data is not None:
        click.echo(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True))


def abort(command: str, error: ApexKBError, json_output: bool) -> None:
    emit(command, "error", error=error, json_output=json_output)
    raise click.exceptions.Exit(2)


def csv_prompt(label: str, default: list[str] | None = None) -> list[str]:
    current = ", ".join(default or []) or None
    raw = click.prompt(label, default=current, show_default=current is not None)
    return [part.strip() for part in raw.split(",") if part.strip()]


def complete_missing(raw: dict[str, Any]) -> dict[str, Any]:
    config = dict(raw)
    source = config.setdefault("source", {})
    if not source.get("repository"):
        source["repository"] = click.prompt("Source repository (owner/name)")
    if not source.get("root"):
        source["root"] = click.prompt("Absolute source repository root")
    if not source.get("folders"):
        source["folders"] = csv_prompt("Source folders, comma-separated")
    destination = config.setdefault("destination", {})
    if not destination.get("repository"):
        destination["repository"] = click.prompt("Destination repository (owner/name)")
    if not destination.get("root"):
        destination["root"] = click.prompt("Absolute destination repository root")
    if not destination.get("folder"):
        destination["folder"] = click.prompt("Destination folder, relative to destination root")
    config.setdefault("exclusions", [])
    if not config.get("topics"):
        topic_name = click.prompt("First topic name")
        config["topics"] = [
            {
                "name": topic_name,
                "phrases": csv_prompt("Strong topic phrases, comma-separated"),
                "ambiguous_or_negative_terms": csv_prompt("Ambiguous or negative terms, comma-separated", []),
                "questions": csv_prompt("Target questions, comma-separated"),
            }
        ]
    options = config.setdefault("run_options", {})
    if not options.get("source_handling"):
        options["source_handling"] = click.prompt("Source handling", type=click.Choice(["pointer_only", "copy_into_kb", "snapshot_copy"]), default="pointer_only")
    if not options.get("semantic_depth"):
        options["semantic_depth"] = click.prompt("Semantic depth", type=click.Choice(["quick", "standard", "deep"]), default="standard")
    if not options.get("output"):
        options["output"] = click.prompt("Output", type=click.Choice(["analysis_only", "compiled_kb", "query_ready"]), default="query_ready")
    if not options.get("non_text"):
        options["non_text"] = click.prompt("Non-text policy", type=click.Choice(["inventory_and_report", "extract_when_supported", "block_on_unsupported"]), default="inventory_and_report")
    options.setdefault("git_metadata", True)
    options.setdefault("graph_depth", "links")
    options.setdefault("ai_help_after_preflight", False)
    options.setdefault("max_semantic_repairs", 2)
    return config


def reject_placeholders(value: Any) -> None:
    rendered = json.dumps(value, ensure_ascii=False).casefold()
    markers = ["velvet-vice", "<owner>", "<repository", " / copy_into_kb", " / standard", " / query_ready", " / true"]
    found = [marker for marker in markers if marker in rendered]
    if found:
        raise ApexKBError("configuration_contains_placeholders", "Replace all example values and slash alternatives before starting", found)


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli() -> None:
    """Apex KB deterministic lifecycle with bounded semantic workers."""


@cli.command()
@click.option("--config", "config_path", type=click.Path(path_type=Path))
@click.option("--yes", is_flag=True, help="Confirm the deterministic readback without prompting.")
@click.option("--non-interactive", is_flag=True, help="Reject missing configuration fields instead of prompting.")
@click.option("--json-output", is_flag=True, help="Emit a machine-readable result envelope after the fixed template/readback.")
@click.option("--template-only", is_flag=True, help="Print the canonical Start template and exit without reading or writing configuration.")
def start(config_path: Path | None, yes: bool, non_interactive: bool, json_output: bool, template_only: bool) -> None:
    """Render the canonical template, preview, confirm, and initialize a run."""
    click.echo(template("start-qa-option-a-v3-example-guidance.md"), nl=False)
    if template_only:
        return
    try:
        if config_path:
            raw = load_yaml(config_path)
        elif non_interactive:
            raise ApexKBError("config_required", "--config is required with --non-interactive")
        else:
            raw = {}
        if not isinstance(raw, dict):
            raise ApexKBError("config_root_invalid", "Configuration root must be a mapping")
        reject_placeholders(raw)
        if not non_interactive:
            raw = complete_missing(raw)
        config = normalize_config(raw)
        run_root, _, preview = preview_config(config)
        click.echo("\n# Apex KB deterministic readback")
        click.echo(json.dumps(preview, indent=2, ensure_ascii=False, sort_keys=True))
        if not (yes or click.confirm("Create the frozen manifest and initial state?", default=False)):
            emit("start", "ok", {"status": "preview_only", "run_root": str(run_root), "readback": preview}, json_output=json_output)
            return
        manifest = create_manifest(config, run_root, preview)
        state = initial_state(manifest)
        write_new_run(run_root, config, manifest, state)
        snapshot = status_snapshot(run_root)
        emit(
            "start",
            "ok",
            {
                "status": "initialized",
                "run_root": str(run_root),
                "run_id": manifest["run_id"],
                "config_hash": manifest["config_hash"],
                "next_action": snapshot["exact_next_action"],
            },
            json_output=json_output,
        )
    except ApexKBError as exc:
        abort("start", exc, json_output)


@cli.command()
@click.option("--run-root", type=click.Path(path_type=Path, exists=True, file_okay=False), required=True)
@click.option("--json-output", is_flag=True)
def status(run_root: Path, json_output: bool) -> None:
    """Reconstruct the complete status from durable files only."""
    try:
        emit("status", "ok", status_snapshot(run_root.resolve()), json_output=json_output)
    except ApexKBError as exc:
        abort("status", exc, json_output)


@cli.command(name="continue")
@click.option("--run-root", type=click.Path(path_type=Path, exists=True, file_okay=False), required=True)
@click.option("--json-output", is_flag=True)
def continue_command(run_root: Path, json_output: bool) -> None:
    """Execute exactly one legal deterministic action or import one bounded result."""
    root = run_root.resolve()
    try:
        result = continue_once(root)
        snapshot = status_snapshot(root)
        emit("continue", "ok", {"executed": result, "status": snapshot}, json_output=json_output)
    except ApexKBError as exc:
        abort("continue", exc, json_output)


@cli.command()
@click.option("--run-root", type=click.Path(path_type=Path, exists=True, file_okay=False), required=True)
@click.option("--query", "query_text", required=True)
@click.option("--topic", "topic_id")
@click.option("--limit", type=click.IntRange(1, 100), default=8, show_default=True)
@click.option("--allow-stale", is_flag=True, help="Allow exploratory use of a stale index; output remains marked stale.")
@click.option("--json-output", is_flag=True)
def query(run_root: Path, query_text: str, topic_id: str | None, limit: int, allow_stale: bool, json_output: bool) -> None:
    """Search accepted compiled pages through the derived local FTS5 index."""
    root = run_root.resolve()
    try:
        _, state = load_run(root)
        if state["lifecycle_status"] != "query_ready" and not allow_stale:
            raise ApexKBError("query_not_ready", "The run is not query_ready; complete acceptance and retrieval first", {"lifecycle_status": state["lifecycle_status"]})
        emit("query", "ok", query_retrieval(root, query_text, limit, allow_stale, topic_id), json_output=json_output)
    except ApexKBError as exc:
        abort("query", exc, json_output)


@cli.command()
@click.option("--run-root", type=click.Path(path_type=Path, exists=True, file_okay=False), required=True)
@click.option("--config", "config_path", type=click.Path(path_type=Path))
@click.option("--yes", is_flag=True)
@click.option("--json-output", is_flag=True)
def update(run_root: Path, config_path: Path | None, yes: bool, json_output: bool) -> None:
    """Create a controlled incremental run and selectively invalidate affected topics."""
    root = run_root.resolve()
    try:
        override = None
        if config_path:
            raw = load_yaml(config_path)
            reject_placeholders(raw)
            override = normalize_config(raw)
        current = status_snapshot(root)
        click.echo("# Apex KB update readback")
        click.echo(json.dumps({"run_root": str(root), "current": current, "config_override": str(config_path) if config_path else None}, indent=2, ensure_ascii=False, sort_keys=True))
        if not (yes or click.confirm("Archive the current control state/wiki and initialize an incremental update run?", default=False)):
            emit("update", "ok", {"status": "preview_only"}, json_output=json_output)
            return
        initialized = initialize_update(root, override)
        snapshot = status_snapshot(root)
        emit("update", "ok", {"status": "initialized", **initialized, "next_action": snapshot["exact_next_action"]}, json_output=json_output)
    except ApexKBError as exc:
        abort("update", exc, json_output)


@cli.command()
@click.option("--run-root", type=click.Path(path_type=Path, exists=True, file_okay=False))
@click.option("--json-output", is_flag=True)
def doctor(run_root: Path | None, json_output: bool) -> None:
    """Probe deterministic runtime capabilities without mutating a run."""
    try:
        connection = sqlite3.connect(":memory:")
        try:
            connection.execute("CREATE VIRTUAL TABLE probe USING fts5(body)")
            fts5 = True
        finally:
            connection.close()
        try:
            import pypdf  # noqa: F401
            pdf = True
        except ImportError:
            pdf = False
        data: dict[str, Any] = {"python": sys.version, "sqlite_version": sqlite3.sqlite_version, "fts5": fts5, "pypdf": pdf, "canonical_template_available": bool(template("start-qa-option-a-v3-example-guidance.md"))}
        if run_root:
            data["run_status"] = status_snapshot(run_root.resolve())
            data["retrieval_health"] = retrieval_health(run_root.resolve())
        emit("doctor", "ok", data, json_output=json_output)
    except (ApexKBError, sqlite3.Error) as exc:
        if isinstance(exc, ApexKBError):
            abort("doctor", exc, json_output)
        abort("doctor", ApexKBError("runtime_probe_failed", str(exc)), json_output)


def main() -> None:
    try:
        cli(standalone_mode=True)
    except BrokenPipeError:
        sys.exit(1)


if __name__ == "__main__":
    main()
