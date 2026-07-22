from __future__ import annotations

import json
from pathlib import Path

import yaml
from click.testing import CliRunner

from apex_kb.cli import cli
from apex_kb.io import load_json, template
from apex_kb.lifecycle import configure_semantic_acceptance, continue_once, drive_until_boundary, load_run, status_snapshot
from apex_kb.retrieval import query_retrieval, retrieval_health

from .helpers import initialize, satisfy_active_task


def drive(run_root: Path, max_steps: int = 80) -> None:
    for _ in range(max_steps):
        snapshot = status_snapshot(run_root)
        if snapshot["lifecycle_status"] in {"query_ready", "compiled_accepted", "analysis_complete"}:
            return
        satisfy_active_task(run_root)
        continue_once(run_root)
    raise AssertionError("lifecycle did not complete")


def test_complete_multi_topic_query_ready_lifecycle(tmp_path: Path):
    run_root, source_repo, _ = initialize(tmp_path)
    source_before = {path: path.read_bytes() for path in (source_repo / "LeelaAppDevelopment").rglob("*") if path.is_file()}
    drive(run_root)
    snapshot = status_snapshot(run_root)
    assert snapshot["lifecycle_status"] == "query_ready"
    assert all(item["phase1"]["status"] == "completed" for item in snapshot["topics"].values())
    assert all(item["acceptance"]["status"] == "not_required" for item in snapshot["topics"].values())
    assert retrieval_health(run_root)["fresh"] is True
    assert (run_root / "wiki/concepts/skill-tree.md").is_file()
    assert (run_root / "wiki/summaries/skill-tree-source-atlas.md").is_file()
    assert {path: path.read_bytes() for path in (source_repo / "LeelaAppDevelopment").rglob("*") if path.is_file()} == source_before
    result = query_retrieval(run_root, "Skill Tree Epic Block", limit=5)
    assert result["result_count"] >= 1 and result["retrieval_fresh"] is True


def test_analysis_only_skips_phase2_acceptance_and_retrieval(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", include_formats=False)
    drive(run_root)
    snapshot = status_snapshot(run_root)
    assert snapshot["lifecycle_status"] == "analysis_complete"
    assert all(item["phase2"]["status"] == "not_required" for item in snapshot["topics"].values())
    assert retrieval_health(run_root)["available"] is False


def test_invalid_semantic_result_produces_bounded_numbered_repair(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", include_formats=False)
    continue_once(run_root)  # corpus
    continue_once(run_root)  # phase1 packet
    _, state = load_run(run_root)
    incoming = Path(state["active_task"]["incoming_path"])
    incoming.parent.mkdir(parents=True, exist_ok=True)
    incoming.write_text("{}", encoding="utf-8")
    result = continue_once(run_root)
    assert result["stage"] == "semantic_repair"
    assert incoming.with_suffix(".repair.json").is_file()
    continue_once(run_root)
    _, repaired_state = load_run(run_root)
    assert repaired_state["active_task"]["task_id"].endswith("-a02")


def test_fresh_acceptance_context_is_enforced(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, include_formats=False)
    _, initial = load_run(run_root)
    configure_semantic_acceptance(run_root, initial, True)
    # Drive until the first acceptance packet.
    for _ in range(30):
        _, state = load_run(run_root)
        active = state.get("active_task")
        if active and active["task_kind"] == "acceptance":
            task = load_json(Path(active["packet_dir"]) / "task.json")
            incoming = Path(active["incoming_path"])
            from .helpers import _acceptance_result
            value = _acceptance_result(task)
            value["evaluator_context_id"] = task["drafting_context_id"]
            incoming.parent.mkdir(parents=True, exist_ok=True)
            incoming.write_text(json.dumps(value), encoding="utf-8")
            result = continue_once(run_root)
            assert result["stage"] == "semantic_repair"
            return
        satisfy_active_task(run_root)
        continue_once(run_root)
    raise AssertionError("acceptance packet not reached")


def test_public_cli_start_status_continue_and_exact_template(tmp_path: Path):
    from .helpers import make_workspace
    _, _, config = make_workspace(tmp_path, output="analysis_only", include_formats=False)
    draft = tmp_path / "run-config.yaml"
    draft.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")
    runner = CliRunner()
    result = runner.invoke(cli, ["start", "--config", str(draft), "--non-interactive", "--yes"])
    assert result.exit_code == 0
    assert result.output.startswith(template("start-qa-option-a-v3-example-guidance.md"))
    run_root = Path(config["destination"]["root"]) / config["destination"]["folder"]
    status_result = runner.invoke(cli, ["status", "--run-root", str(run_root), "--json-output"])
    assert status_result.exit_code == 0 and '"lifecycle_status": "running"' in status_result.output
    continue_result = runner.invoke(cli, ["continue", "--run-root", str(run_root), "--json-output"])
    assert continue_result.exit_code == 0 and '"stage": "corpus_intelligence"' in continue_result.output


def test_drive_runs_to_semantic_boundary(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", include_formats=False)
    result = drive_until_boundary(run_root)
    assert result["status"]["next_action"]["kind"] == "semantic_wait"
    assert result["status"]["active_task"]["task_kind"] == "phase1"
