from __future__ import annotations

from pathlib import Path

import pytest

from apex_kb.errors import ApexKBError
from apex_kb.io import atomic_json, load_json
from apex_kb.corpus import build_corpus_intelligence
from apex_kb.lifecycle import configure_semantic_acceptance, continue_once, load_run
from apex_kb.semantic.engine import create_phase1_packet

from .helpers import _acceptance_result, _phase1_result, _phase2_result, initialize, satisfy_active_task


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


@pytest.mark.parametrize("case", ["ranked_source_pointer", "route_coverage"])
def test_phase2_rejects_uncited_ranked_sources_and_incomplete_routes(tmp_path: Path, case: str):
    run_root, _, _ = initialize(tmp_path, include_formats=False)
    _, state = _advance_to_task(run_root, "phase2")
    active = state["active_task"]
    task = load_json(Path(active["packet_dir"]) / "task.json")
    value = _phase2_result(run_root, task)
    if case == "ranked_source_pointer":
        value["dossier"]["adaptive_ranked_sources"][0]["citations"][0]["pointer"] = "line:999999"
    else:
        value["dossier"]["route_by_question"][0]["query_id"] = "not-a-real-query"
    repair = _submit_invalid(run_root, state, value)
    assert repair["reason_code"] in {"citation_pointer_invalid", "route_coverage_incomplete", "schema_validation_failed"}


def test_phase1_rejects_capsule_pointer_absent_from_review(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, include_formats=False)
    _, state = _advance_to_task(run_root, "phase1")
    active = state["active_task"]
    task = load_json(Path(active["packet_dir"]) / "task.json")
    allowlist = load_json(Path(active["packet_dir"]) / "source-allowlist.json")
    value = _phase1_result(run_root, task, allowlist)
    assert value["source_capsules"], "fixture must produce at least one capsule"
    value["source_capsules"][0]["pointers"] = list(value["source_capsules"][0]["pointers"]) + ["line:999999"]
    repair = _submit_invalid(run_root, state, value)
    assert repair["reason_code"] in {"capsule_pointer_not_in_review", "schema_validation_failed"}


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


def test_candidate_selection_bounds_work_pack_and_records_exclusions(tmp_path: Path):
    """Phase 0 ranking must be usable as a bound on the Phase 1 work pack.

    Before this, every candidate scoring above zero — including a single body-only mention of one
    supporting term — became a mandatory Phase 1 disposition. On a real corpus that produced work
    packs far past a worker's usable context, which is the practical cause of thin, averaged
    semantic output. The bound must never be silent: excluded candidates are recorded with rank,
    score, class, and the rule that excluded them.
    """
    from apex_kb.semantic.engine import select_candidates

    candidates = [
        {"source_id": "src-core", "repository_path": "a/core.md", "rank": 1, "score": 90, "candidate_class": "core"},
        {"source_id": "src-ctx", "repository_path": "a/ctx.md", "rank": 2, "score": 30, "candidate_class": "contextual"},
        {"source_id": "src-inc1", "repository_path": "a/inc1.md", "rank": 3, "score": 3, "candidate_class": "incidental"},
        {"source_id": "src-inc2", "repository_path": "a/inc2.md", "rank": 4, "score": 3, "candidate_class": "incidental"},
        {"source_id": "src-blocked", "repository_path": "a/scan.pdf", "rank": 5, "score": 1, "candidate_class": "blocked"},
    ]

    # Default = prior behaviour: nothing bounded out.
    kept, excluded = select_candidates(candidates, {"min_candidate_class": "incidental", "max_candidates_per_topic": None})
    assert len(kept) == 5 and excluded == []

    # Class floor drops body-only incidental matches but must retain blocked ones, so an
    # extraction failure stays visible rather than vanishing because its text could not be scored.
    kept, excluded = select_candidates(candidates, {"min_candidate_class": "contextual", "max_candidates_per_topic": None})
    kept_ids = {item["source_id"] for item in kept}
    assert kept_ids == {"src-core", "src-ctx", "src-blocked"}
    assert {item["source_id"] for item in excluded} == {"src-inc1", "src-inc2"}
    assert all(item["excluded_by"] == "min_candidate_class" for item in excluded)
    assert all(item["rank"] and item["candidate_class"] and "rule_detail" in item for item in excluded)

    # Cap keeps the best-ranked and records the rest; blocked is exempt from the cap.
    kept, excluded = select_candidates(candidates, {"min_candidate_class": "incidental", "max_candidates_per_topic": 2})
    assert [item["source_id"] for item in kept] == ["src-core", "src-ctx", "src-blocked"]
    assert {item["source_id"] for item in excluded} == {"src-inc1", "src-inc2"}
    assert all(item["excluded_by"] == "max_candidates_per_topic" for item in excluded)


def test_bounded_phase1_packet_declares_and_writes_its_exclusions(tmp_path: Path):
    """A bounded pack must be auditable end-to-end: task fields plus an on-disk exclusion list."""
    run_root, source_repo, _ = initialize(tmp_path, output="analysis_only")
    bulk = source_repo / "LeelaAppDevelopment" / "Bulk"
    bulk.mkdir()
    for index in range(12):
        # Body-only supporting-term mentions => low-scoring incidental candidates.
        (bulk / f"note-{index:02d}.md").write_text(f"# Note {index}\nAn epic mention in prose.\n", encoding="utf-8")
    manifest, state = load_run(run_root)
    manifest["run_options"]["max_candidates_per_topic"] = 3
    build_corpus_intelligence(run_root, manifest)

    packet = create_phase1_packet(run_root, manifest, "skill-tree", 1, None)

    task = load_json(Path(packet["packet_dir"]) / "task.json")
    allowlist = load_json(Path(packet["packet_dir"]) / "source-allowlist.json")
    assert task["candidate_count"] == len(allowlist["sources"])
    assert task["phase0_candidate_count"] >= task["candidate_count"]
    if task["excluded_candidate_count"]:
        excluded_path = Path(packet["packet_dir"]) / "excluded-candidates.json"
        assert excluded_path.is_file(), "exclusions must be written, never silent"
        payload = load_json(excluded_path)
        assert payload["excluded_count"] == task["excluded_candidate_count"]
        assert payload["selected_count"] == task["candidate_count"]
        assert all("excluded_by" in item and "rule_detail" in item for item in payload["excluded"])
        assert "excluded-candidates.json" in (Path(packet["packet_dir"]) / "TASK.md").read_text(encoding="utf-8")
