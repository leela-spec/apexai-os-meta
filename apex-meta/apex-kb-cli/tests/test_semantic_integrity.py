from __future__ import annotations

from pathlib import Path

import pytest

from apex_kb.errors import ApexKBError
from apex_kb.io import atomic_json, load_json
from apex_kb.lifecycle import configure_semantic_acceptance, continue_once, load_run

from .helpers import _acceptance_result, _phase2_result, initialize, satisfy_active_task


def _advance_to_task(run_root: Path, task_kind: str) -> tuple[dict, dict]:
    for _ in range(80):
        manifest, state = load_run(run_root)
        active = state.get("active_task")
        if active and active["task_kind"] == task_kind:
            return manifest, state
        satisfy_active_task(run_root)
        continue_once(run_root)
    raise AssertionError(f"{task_kind} packet not reached")


def _submit_invalid(run_root: Path, state: dict, value: dict) -> dict:
    active = state["active_task"]
    incoming = Path(active["incoming_path"])
    atomic_json(incoming, value)
    result = continue_once(run_root)
    assert result["stage"] == "semantic_repair"
    return load_json(incoming.with_suffix(".repair.json"))


@pytest.mark.parametrize("case", ["empty_macro", "question_text", "source_id", "pointer"])
def test_phase2_rejects_empty_content_and_unlocked_or_unreviewed_evidence(tmp_path: Path, case: str):
    run_root, _, _ = initialize(tmp_path, include_formats=False)
    _, state = _advance_to_task(run_root, "phase2")
    active = state["active_task"]
    task = load_json(Path(active["packet_dir"]) / "task.json")
    value = _phase2_result(run_root, task)
    if case == "empty_macro":
        value["dossier"]["macro"] = ""
    elif case == "question_text":
        value["dossier"]["target_answers"][0]["question"] += " changed"
    elif case == "source_id":
        value["dossier"]["target_answers"][0]["citations"][0]["source_id"] = "src-0000000000000000"
    elif case == "pointer":
        value["dossier"]["target_answers"][0]["citations"][0]["pointer"] = "line:999999"
    repair = _submit_invalid(run_root, state, value)
    assert repair["reason_code"] in {
        "schema_validation_failed",
        "target_question_text_mismatch",
        "citation_source_invalid",
        "citation_pointer_invalid",
    }


def test_acceptance_packet_is_topic_scoped_and_states_independence_limit(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, include_formats=False)
    _, state = load_run(run_root)
    configure_semantic_acceptance(run_root, state, True)
    _, state = _advance_to_task(run_root, "acceptance")
    active = state["active_task"]
    task = load_json(Path(active["packet_dir"]) / "task.json")
    phase1 = load_json(run_root / "ingest-analysis" / "topics" / f"{task['topic_id']}.analysis.json")
    expected = sorted(
        {
            str(run_root / "ingest-analysis" / "sources" / f"{review['content_hash']}.analysis.json")
            for review in phase1["source_reviews"]
            if (run_root / "ingest-analysis" / "sources" / f"{review['content_hash']}.analysis.json").is_file()
        }
    )
    assert task["evidence_paths"] == expected
    assert "verifies only" in task["fresh_context_contract"]
    assert "genuinely independent fresh evaluator context" in task["fresh_context_contract"]
    packet = load_json(Path(active["packet_dir"]) / "source-allowlist.json")
    assert packet["resolved_evidence"] == expected


@pytest.mark.parametrize("case", ["empty_claim_sample", "duplicate_question", "page_pointer", "evidence_pointer"])
def test_acceptance_rejects_unproven_pass_and_out_of_packet_pointers(tmp_path: Path, case: str):
    run_root, _, _ = initialize(tmp_path, include_formats=False)
    _, state = load_run(run_root)
    configure_semantic_acceptance(run_root, state, True)
    _, state = _advance_to_task(run_root, "acceptance")
    active = state["active_task"]
    task = load_json(Path(active["packet_dir"]) / "task.json")
    value = _acceptance_result(task)
    if case == "empty_claim_sample":
        value["claim_checks"] = []
    elif case == "duplicate_question":
        value["question_evaluations"].append(dict(value["question_evaluations"][0]))
    elif case == "page_pointer":
        value["question_evaluations"][0]["page_pointers"] = [str(run_root / "outside.md") + "#answer"]
    else:
        value["claim_checks"][0]["evidence_pointers"] = [str(run_root / "outside.json")]
    repair = _submit_invalid(run_root, state, value)
    assert repair["reason_code"] in {
        "schema_validation_failed",
        "acceptance_question_set_invalid",
        "semantic_pointer_outside_packet",
    }
