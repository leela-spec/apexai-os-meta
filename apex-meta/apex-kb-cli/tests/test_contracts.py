from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from apex_kb.config import normalize_config, preview_config
from apex_kb.corpus import build_corpus_intelligence
from apex_kb.errors import ApexKBError
from apex_kb.io import atomic_json, load_json, load_yaml
from apex_kb.lifecycle import (
    continue_once,
    initialize_update,
    load_run,
    migrate_legacy_run,
    status_snapshot,
)
from apex_kb.retrieval import query_retrieval, retrieval_health

from .helpers import default_topics, initialize, make_workspace, satisfy_active_task
from .test_lifecycle import drive


def test_block_on_unsupported_fails_closed_after_accountability_artifacts(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", topics=[default_topics()[0]], include_formats=True)
    config = normalize_config(load_yaml(run_root / "run-config.yaml"))
    config["run_options"]["non_text"] = "block_on_unsupported"
    # Reinitialize a separate run because the config is frozen.
    run_root.unlink() if run_root.is_file() else None
    # Update the frozen config/identity through a clean workspace.
    second = tmp_path / "second"
    _, _, raw = make_workspace(second, output="analysis_only", topics=[default_topics()[0]], include_formats=True)
    raw["run_options"]["non_text"] = "block_on_unsupported"
    run_root2, _, preview = preview_config(raw)
    from apex_kb.lifecycle import create_manifest, initial_state, write_new_run
    manifest = create_manifest(raw, run_root2, preview)
    write_new_run(run_root2, raw, manifest, initial_state(manifest))
    with pytest.raises(ApexKBError) as error:
        continue_once(run_root2)
    assert error.value.code == "unsupported_files_blocked"
    assert (run_root2 / "manifests/source-inventory.ndjson").is_file()
    assert (run_root2 / "manifests/phase0/phase0-navigation-report.md").is_file()
    _, state = load_run(run_root2)
    assert state["corpus_intelligence"]["status"] == "pending"


def test_status_is_read_only_and_legacy_continue_migrates_with_backup(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", include_formats=False)
    manifest = load_json(run_root / "run-manifest.json")
    state = load_json(run_root / "run-state.json")
    manifest["schema"] = "apex.kb.run-manifest.v1"
    state["schema"] = "apex.kb.run-state.v1"
    atomic_json(run_root / "run-manifest.json", manifest)
    atomic_json(run_root / "run-state.json", state)
    before_manifest = (run_root / "run-manifest.json").read_bytes()
    before_state = (run_root / "run-state.json").read_bytes()
    snapshot = status_snapshot(run_root)
    assert snapshot["migration_required"] is True
    assert (run_root / "run-manifest.json").read_bytes() == before_manifest
    assert (run_root / "run-state.json").read_bytes() == before_state
    result = continue_once(run_root)
    assert result["stage"] == "migration"
    assert status_snapshot(run_root).get("migration_required", False) is False
    backups = list((run_root / "log/migrations").glob("*/migration-result.json"))
    assert backups


def test_git_last_change_metadata_is_collected_without_fetch_or_write(tmp_path: Path):
    run_root, source_repo, _ = initialize(tmp_path, output="analysis_only", topics=[default_topics()[0]], include_formats=False)
    subprocess.run(["git", "init"], cwd=source_repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=source_repo, check=True)
    subprocess.run(["git", "config", "user.name", "Apex Test"], cwd=source_repo, check=True)
    subprocess.run(["git", "add", "LeelaAppDevelopment"], cwd=source_repo, check=True)
    subprocess.run(["git", "commit", "-m", "Add sources"], cwd=source_repo, check=True, capture_output=True)
    config = normalize_config(load_yaml(run_root / "run-config.yaml"))
    config["run_options"]["git_metadata"] = True
    # Existing run has frozen git_metadata false; create a fresh root.
    destination = tmp_path / "apex-git"
    destination.mkdir()
    config["destination"]["root"] = str(destination)
    root, _, preview = preview_config(config)
    from apex_kb.lifecycle import create_manifest, initial_state, write_new_run
    manifest = create_manifest(config, root, preview)
    write_new_run(root, config, manifest, initial_state(manifest))
    result = build_corpus_intelligence(root, manifest)
    assert result["summary"]["git_metadata_error"] is None
    assert result["summary"]["git_dated_file_count"] > 0
    assert any(record["git_last_changed"] for record in result["records"])


def test_analysis_only_to_query_ready_reuses_phase1_but_schedules_compilation(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", include_formats=False)
    drive(run_root)
    config = normalize_config(load_yaml(run_root / "run-config.yaml"))
    config["run_options"]["output"] = "query_ready"
    initialize_update(run_root, config)
    continue_once(run_root)
    _, state = load_run(run_root)
    assert all(item["phase1"]["status"] == "reused" for item in state["topics"].values())
    assert all(item["phase2"]["status"] == "pending" for item in state["topics"].values())
    assert all(item["acceptance"]["status"] == "pending" for item in state["topics"].values())
    drive(run_root)
    assert status_snapshot(run_root)["lifecycle_status"] == "query_ready"


def test_semantic_depth_change_invalidates_all_phase1_topics(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", include_formats=False)
    drive(run_root)
    config = normalize_config(load_yaml(run_root / "run-config.yaml"))
    config["run_options"]["semantic_depth"] = "deep"
    initialize_update(run_root, config)
    continue_once(run_root)
    _, state = load_run(run_root)
    assert all(item["affected"] is True for item in state["topics"].values())
    assert all(item["phase1"]["status"] == "pending" for item in state["topics"].values())


def test_retrieval_detects_page_and_run_staleness(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, include_formats=False)
    drive(run_root)
    page = run_root / "wiki/concepts/skill-tree.md"
    page.write_text(page.read_text(encoding="utf-8") + "\nUnindexed edit.\n", encoding="utf-8")
    assert retrieval_health(run_root)["fresh"] is False
    with pytest.raises(ApexKBError) as error:
        query_retrieval(run_root, "Skill Tree")
    assert error.value.code == "retrieval_stale"


def test_topic_contract_change_invalidates_only_that_topic(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, include_formats=False)
    drive(run_root)
    config = normalize_config(load_yaml(run_root / "run-config.yaml"))
    config["topics"][0]["target_queries"][0]["question"] = "What changed in the current Skill Tree ownership model?"
    initialize_update(run_root, config)
    continue_once(run_root)
    _, state = load_run(run_root)
    assert state["topics"]["skill-tree"]["affected"] is True
    assert state["topics"]["sequencing"]["affected"] is False


def test_atomic_write_failure_preserves_original_and_cleans_temp(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    from apex_kb import io

    target = tmp_path / "state.json"
    target.write_text("original\n", encoding="utf-8")

    def fail_replace(_source, _target):
        raise OSError("simulated replace failure")

    monkeypatch.setattr(io.os, "replace", fail_replace)
    with pytest.raises(OSError, match="simulated replace failure"):
        io.atomic_text(target, "replacement\n")
    assert target.read_text(encoding="utf-8") == "original\n"
    assert not list(tmp_path.glob(".state.json.*.tmp"))


def test_config_drift_blocks_status_and_continue_without_mutating_state(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", include_formats=False)
    state_before = (run_root / "run-state.json").read_bytes()
    config = load_yaml(run_root / "run-config.yaml")
    config["run_options"]["semantic_depth"] = "deep"
    import yaml

    (run_root / "run-config.yaml").write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")
    with pytest.raises(ApexKBError) as status_error:
        status_snapshot(run_root)
    assert status_error.value.code == "config_drift"
    with pytest.raises(ApexKBError) as continue_error:
        continue_once(run_root)
    assert continue_error.value.code == "config_drift"
    assert (run_root / "run-state.json").read_bytes() == state_before


def test_fresh_python_process_reconstructs_status_and_resumes(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", include_formats=False)
    package_root = Path(__file__).resolve().parents[1]
    env = {**__import__("os").environ, "PYTHONPATH": str(package_root / "src")}
    status = subprocess.run(
        [__import__("sys").executable, "-m", "apex_kb.cli", "status", "--run-root", str(run_root), "--json-output"],
        cwd=package_root,
        env=env,
        text=True,
        capture_output=True,
        check=True,
    )
    assert '"lifecycle_status": "running"' in status.stdout
    continued = subprocess.run(
        [__import__("sys").executable, "-m", "apex_kb.cli", "continue", "--run-root", str(run_root), "--json-output"],
        cwd=package_root,
        env=env,
        text=True,
        capture_output=True,
        check=True,
    )
    assert '"stage": "corpus_intelligence"' in continued.stdout
    assert status_snapshot(run_root)["current_stage"] == "corpus_intelligence_complete"
