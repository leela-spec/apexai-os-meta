from __future__ import annotations

from pathlib import Path

import pytest

from apex_kb.errors import ApexKBError
from apex_kb.lifecycle import continue_once, load_run

from .helpers import commit_destination_paths, initialize, satisfy_active_task


def _activate_phase2a(run_root: Path) -> dict:
    continue_once(run_root)  # deterministic corpus intelligence
    result = continue_once(run_root)  # Phase 2A task construction and deterministic publication
    assert result["stage"] == "phase1_packet"
    _, state = load_run(run_root)
    return state["active_task"]


def test_phase2a_prompt_is_complete_and_bound_to_published_main(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", include_formats=False)
    active = _activate_phase2a(run_root)
    prompt = Path(active["prompt_path"]).read_text(encoding="utf-8")

    assert active["transport"] == "direct_main"
    assert active["branch"] == "main"
    assert active["base_commit"] in prompt
    assert "Perform the bounded Apex KB Phase 2A semantic analysis" in prompt
    assert "Push the commit directly to main" in prompt
    assert "WRITE ONLY" in prompt
    assert all(path in prompt for path in active["expected_output_paths"])
    assert "{base_commit}" not in prompt
    assert "{destination_repository}" not in prompt


def test_phase2a_direct_main_commit_is_pulled_validated_and_completed(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", include_formats=False)
    active = _activate_phase2a(run_root)
    satisfy_active_task(run_root)

    result = continue_once(run_root)
    assert result["stage"] == "phase1_import"
    imported = result["result"]
    assert imported["base_commit"] == active["base_commit"]
    assert imported["result_commit"] != active["base_commit"]
    assert imported["changed_paths"] == sorted(active["expected_output_paths"])

    _, state = load_run(run_root)
    assert state["topics"][active["topic_id"]]["phase1"]["status"] == "completed"
    assert state["active_task"] is None


def test_phase2a_rejects_any_changed_path_outside_exact_output_contract(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", include_formats=False)
    active = _activate_phase2a(run_root)
    satisfy_active_task(run_root)

    destination = Path(active["destination_root"])
    rogue = destination / "unexpected-semantic-write.md"
    rogue.write_text("not allowed\n", encoding="utf-8")
    commit_destination_paths(run_root, ["unexpected-semantic-write.md"], "Add unexpected semantic path")

    with pytest.raises(ApexKBError) as error:
        continue_once(run_root)
    assert error.value.code == "semantic_result_invalid"
    assert "exactly the declared output paths" in error.value.message
