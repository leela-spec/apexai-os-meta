from __future__ import annotations

from pathlib import Path

from apex_kb.io import atomic_json, load_json
from apex_kb.lifecycle import continue_once, initialize_update, load_run, status_snapshot
from apex_kb.retrieval import retrieval_health

from .helpers import initialize, satisfy_active_task
from .test_lifecycle import drive


def test_incremental_update_archives_prior_state_and_invalidates_only_affected_topic(tmp_path: Path):
    run_root, source_repo, _ = initialize(tmp_path, include_formats=False)
    drive(run_root)
    first = status_snapshot(run_root)
    assert first["lifecycle_status"] == "query_ready"
    skill_tree = source_repo / "LeelaAppDevelopment/01_Features/102 - Epics (Database + Skill Tree).md"
    skill_tree.write_text(skill_tree.read_text(encoding="utf-8") + "\nNew Skill Tree rule.\n", encoding="utf-8")
    initialized = initialize_update(run_root)
    assert Path(initialized["archive_root"]).joinpath("wiki/concepts/skill-tree.md").is_file()
    assert retrieval_health(run_root)["fresh"] is False
    continue_once(run_root)  # corpus + impact
    _, state = load_run(run_root)
    assert state["topics"]["skill-tree"]["affected"] is True
    assert state["topics"]["skill-tree"]["phase1"]["status"] == "pending"
    assert state["topics"]["sequencing"]["affected"] is False
    assert state["topics"]["sequencing"]["phase1"]["status"] == "reused"
    continue_once(run_root)  # affected phase1 packet
    _, state = load_run(run_root)
    packet = Path(state["active_task"]["packet_dir"])
    allowlist = __import__("json").loads((packet / "source-allowlist.json").read_text(encoding="utf-8"))
    assert any(item["reusable_capsule_path"] for item in allowlist["sources"] if item["repository_path"].endswith("Skill Tree v1.md"))
    drive(run_root)
    assert status_snapshot(run_root)["lifecycle_status"] == "query_ready"


def test_no_change_update_reuses_all_topics(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, include_formats=False)
    drive(run_root)
    initialize_update(run_root)
    continue_once(run_root)
    _, state = load_run(run_root)
    assert all(item["affected"] is False for item in state["topics"].values())
    assert all(item["phase1"]["status"] == "reused" for item in state["topics"].values())
    drive(run_root)
    assert status_snapshot(run_root)["lifecycle_status"] == "query_ready"


def test_legacy_update_migrates_then_initializes_a_safe_update_run(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", include_formats=False)
    drive(run_root)
    manifest = load_json(run_root / "run-manifest.json")
    state = load_json(run_root / "run-state.json")
    manifest["schema"] = "apex.kb.run-manifest.v1"
    state["schema"] = "apex.kb.run-state.v1"
    atomic_json(run_root / "run-manifest.json", manifest)
    atomic_json(run_root / "run-state.json", state)

    initialized = initialize_update(run_root)
    assert initialized["migration"]["migrated"] is True
    migrated_manifest, migrated_state = load_run(run_root)
    assert migrated_manifest["run_kind"] == "update"
    assert migrated_state["lifecycle_status"] == "running"
    assert list((run_root / "log/migrations").glob("*/migration-result.json"))
    assert continue_once(run_root)["stage"] == "corpus_intelligence"
