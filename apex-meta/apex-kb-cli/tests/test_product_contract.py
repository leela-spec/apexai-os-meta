from __future__ import annotations

import json
from pathlib import Path

import pytest

from apex_kb.config import normalize_config, preview_config
from apex_kb.corpus import build_corpus_intelligence
from apex_kb.corpus.engine import _change_report
from apex_kb.errors import ApexKBError
from apex_kb.extractors import extract_for_policy
from apex_kb.io import iter_ndjson, load_json, sha256_file
from apex_kb.lifecycle import (
    continue_once,
    create_manifest,
    derive_next_action,
    initial_state,
    load_run,
    status_snapshot,
    write_new_run,
)
from apex_kb.retrieval import build_retrieval, query_retrieval

from .helpers import default_topics, initialize, make_workspace, satisfy_active_task, write_docx
from .test_lifecycle import drive


def _new_run(config: dict, destination_suffix: str | None = None):
    config = normalize_config(config)
    if destination_suffix:
        config["destination"]["folder"] += f"-{destination_suffix}"
    run_root, _, preview = preview_config(config)
    manifest = create_manifest(config, run_root, preview)
    write_new_run(run_root, config, manifest, initial_state(manifest))
    return run_root, manifest


def test_source_custody_preserves_relative_paths_and_refuses_collision(tmp_path: Path):
    run_root, source_repo, _ = initialize(
        tmp_path,
        output="analysis_only",
        handling="copy_into_kb",
        topics=[default_topics()[0]],
        include_formats=False,
    )
    manifest, _ = load_run(run_root)
    result = build_corpus_intelligence(run_root, manifest)
    original_path = "LeelaAppDevelopment/01_Features/102 - Epics (Database + Skill Tree).md"
    record = next(item for item in result["records"] if item["repository_path"] == original_path)
    assert record["custody_path"] == f"raw/sources/{original_path}"
    target = run_root / record["custody_path"]
    assert target.read_bytes() == (source_repo / original_path).read_bytes()
    target.write_text("different content", encoding="utf-8")
    with pytest.raises(ApexKBError) as error:
        build_corpus_intelligence(run_root, manifest)
    assert error.value.code == "custody_collision"


def test_non_text_policies_are_materially_distinct(tmp_path: Path):
    policy_status = {}
    for policy in ("inventory_and_report", "extract_when_supported"):
        case = tmp_path / policy
        _, _, config = make_workspace(case, output="analysis_only", topics=[default_topics()[0]], include_formats=True)
        config["run_options"]["non_text"] = policy
        run_root, manifest = _new_run(config)
        result = build_corpus_intelligence(run_root, manifest)
        docx = next(item for item in result["records"] if item["repository_path"].endswith("skill-tree.docx"))
        policy_status[policy] = docx["extraction_status"]
    assert policy_status == {"inventory_and_report": "metadata_only", "extract_when_supported": "success"}

    case = tmp_path / "blocked"
    _, _, config = make_workspace(case, output="analysis_only", topics=[default_topics()[0]], include_formats=True)
    config["run_options"]["non_text"] = "block_on_unsupported"
    run_root, manifest = _new_run(config)
    with pytest.raises(ApexKBError) as error:
        build_corpus_intelligence(run_root, manifest)
    assert error.value.code == "unsupported_files_blocked"
    rows = list(iter_ndjson(run_root / "manifests/source-inventory.ndjson"))
    assert next(item for item in rows if item["repository_path"].endswith("skill-tree.docx"))["extraction_status"] == "success"
    assert next(item for item in rows if item["repository_path"].endswith("skill-tree.png"))["extraction_status"] == "metadata_only"


def test_configured_authority_hints_are_inspectable_and_not_implicit(tmp_path: Path):
    source_repo, _, config = make_workspace(tmp_path, output="analysis_only", topics=[default_topics()[0]], include_formats=False)
    source = source_repo / "LeelaAppDevelopment"
    (source / "Current").mkdir()
    (source / "Current/current-skill-tree.md").write_text("# Skill Tree\nCurrent contract.\n", encoding="utf-8")
    (source / "Notes/generic-long.md").write_text(("Skill Tree. " * 80) + "\n", encoding="utf-8")
    config["lifecycle_hint_rules"] = [
        {"path": "LeelaAppDevelopment/Current/**", "hint": "current_candidate", "rule_id": "current-path"}
    ]
    config["authority_hint_rules"] = [
        {"path": "LeelaAppDevelopment/Current/**", "hint": "operator_designated_current", "score": 100, "rule_id": "authority-current"}
    ]
    run_root, manifest = _new_run(config)
    result = build_corpus_intelligence(run_root, manifest)
    candidates = {item["repository_path"]: item for item in result["topic_maps"]["skill-tree"]["candidates"]}
    current = candidates["LeelaAppDevelopment/Current/current-skill-tree.md"]
    generic = candidates["LeelaAppDevelopment/Notes/generic-long.md"]
    assert current["rank"] < generic["rank"]
    assert current["authority_hints"] == [
        {"rule_id": "authority-current", "path": "LeelaAppDevelopment/Current/**", "hint": "operator_designated_current", "score": 100}
    ]
    assert current["lifecycle_hint_evidence"][0]["rule_id"] == "current-path"
    archived = next(item for item in result["records"] if item["repository_path"].endswith("Archive/Skill Tree v1.md"))
    assert archived["lifecycle_hints"] == []  # path names never become unconfigured semantic authority


def test_topic_map_separates_fields_and_records_identifier_cooccurrence(tmp_path: Path):
    topic = {
        "topic_id": "field-map",
        "name": "Field Map",
        "primary_phrases": ["front phrase", "h1 phrase"],
        "aliases": ["heading phrase"],
        "supporting_terms": ["body phrase", "second identifier", "link phrase", "reference phrase"],
        "negative_terms": [],
        "ambiguous_terms": [],
        "target_queries": [],
        "expected_routes": {"dossier": "wiki/concepts/field-map.md", "source_atlas": "wiki/summaries/field-map-source-atlas.md"},
    }
    source_repo, _, config = make_workspace(tmp_path, output="analysis_only", topics=[topic], include_formats=False)
    path = source_repo / "LeelaAppDevelopment/Notes/field-source.md"
    path.write_text(
        "---\ntitle: Front Phrase\n---\n# H1 Phrase\n\n## Heading Phrase\n\nBody Phrase combines Second Identifier.\n\n[Link Phrase](Docs/link-phrase.md)\n\n`Docs/reference-phrase.md`\n",
        encoding="utf-8",
    )
    run_root, manifest = _new_run(config)
    result = build_corpus_intelligence(run_root, manifest)
    candidate = next(item for item in result["topic_maps"]["field-map"]["candidates"] if item["repository_path"].endswith("field-source.md"))
    fields = {item["field"] for item in candidate["match_reasons"]}
    assert {"frontmatter_title", "h1", "heading", "body", "link", "reference", "identifier_co_occurrence"} <= fields
    # A frontmatter title and H1 are not double-counted as body lines.
    assert not any(item["field"] == "body" and item["term"] in {"front phrase", "h1 phrase", "heading phrase"} for item in candidate["match_reasons"])
    postings = list(iter_ndjson(run_root / "manifests/phase0/term-postings.ndjson"))
    assert any(item["field"] == "identifier_co_occurrence" and item.get("topic_id") == "field-map" for item in postings)


def test_phase0_and_retrieval_rebuilds_are_byte_identical(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, output="analysis_only", topics=[default_topics()[0]], include_formats=False)
    manifest, _ = load_run(run_root)
    build_corpus_intelligence(run_root, manifest)
    phase0_paths = sorted(
        [path for path in (run_root / "manifests").rglob("*") if path.is_file()]
        + [path for path in (run_root / manifest["artifact_layout"]["run_dir"]).rglob("*") if path.is_file()]
    )
    before = {str(path.relative_to(run_root)): sha256_file(path) for path in phase0_paths}
    build_corpus_intelligence(run_root, manifest)
    after = {str(path.relative_to(run_root)): sha256_file(path) for path in phase0_paths}
    assert before == after

    query_root, _, _ = initialize(tmp_path / "query", include_formats=False)
    drive(query_root)
    query_manifest, state = load_run(query_root)
    db = query_root / "derived/search/search.sqlite"
    db_hash = sha256_file(db)
    page_hashes = {str(path.relative_to(query_root)): sha256_file(path) for path in (query_root / "wiki").rglob("*.md")}
    accepted = [topic_id for topic_id, item in state["topics"].items() if item["acceptance"]["verdict"] == "semantic_pass"]
    build_retrieval(query_root, query_manifest, accepted)
    assert sha256_file(db) == db_hash
    assert {str(path.relative_to(query_root)): sha256_file(path) for path in (query_root / "wiki").rglob("*.md")} == page_hashes


def test_postflight_precedes_retrieval_and_completion_is_durable(tmp_path: Path, monkeypatch):
    run_root, source_repo, _ = initialize(tmp_path, include_formats=False)
    for _ in range(80):
        manifest, state = load_run(run_root)
        action = derive_next_action(manifest, state)
        if action == {"kind": "deterministic", "stage": "postflight"}:
            assert state["retrieval"]["status"] == "pending"
            break
        satisfy_active_task(run_root)
        continue_once(run_root)
    else:
        raise AssertionError("postflight boundary not reached")
    continue_once(run_root)
    manifest, state = load_run(run_root)
    assert state["postflight"]["status"] == "completed"
    assert derive_next_action(manifest, state) == {"kind": "deterministic", "stage": "retrieval"}
    source_path = source_repo / "LeelaAppDevelopment/01_Features/102 - Epics (Database + Skill Tree).md"
    source_bytes = source_path.read_bytes()
    source_path.write_bytes(source_bytes + b"\nLate source drift.\n")
    with pytest.raises(ApexKBError) as drift_error:
        continue_once(run_root)
    assert drift_error.value.code == "completion_source_drift"
    source_path.write_bytes(source_bytes)
    from apex_kb import lifecycle

    monkeypatch.setattr(lifecycle, "utc_now", lambda: "2099-01-02T03:04:05Z")
    continue_once(run_root)
    snapshot = status_snapshot(run_root)
    assert snapshot["lifecycle_status"] == "query_ready"
    assert snapshot["completion"]["status"] == "completed"
    certificate = load_json(run_root / "completion.json")
    assert certificate["lifecycle_status"] == "query_ready" and certificate["blockers"] == []
    assert certificate["completed_at"] == "2099-01-02T03:04:05Z"
    assert certificate["source_integrity"]["fresh"] is True
    assert certificate["source_repository_mutated"] is False


def test_update_report_detects_moves_and_newly_unreadable_sources():
    old_rows = [
        {"repository_path": "docs/old.md", "sha256": "a" * 64, "inclusion_state": "included", "extraction_status": "success"},
        {"repository_path": "docs/spec.docx", "sha256": "b" * 64, "inclusion_state": "included", "extraction_status": "success"},
    ]
    new_rows = [
        {"repository_path": "docs/new.md", "sha256": "a" * 64, "inclusion_state": "included", "extraction_status": "success"},
        {"repository_path": "docs/spec.docx", "sha256": "c" * 64, "inclusion_state": "included", "extraction_status": "error"},
    ]
    old_map = {"schema": "apex.kb.topic-map.v2", "topic": {"topic_id": "t"}, "candidates": [{"repository_path": "docs/old.md"}, {"repository_path": "docs/spec.docx"}]}
    new_map = {"schema": "apex.kb.topic-map.v2", "topic": {"topic_id": "t"}, "candidates": [{"repository_path": "docs/new.md"}, {"repository_path": "docs/spec.docx"}]}
    report = _change_report(old_rows, new_rows, {"t": old_map}, {"t": new_map})
    assert report["moved"] == [{"from": "docs/old.md", "to": "docs/new.md", "sha256": "a" * 64}]
    assert report["newly_unreadable"] == ["docs/spec.docx"]
    assert report["affected_topics"]["t"]["affected"] is True


def test_query_packet_contains_identity_precise_pointers_and_source_atlas(tmp_path: Path):
    run_root, _, _ = initialize(tmp_path, include_formats=False)
    drive(run_root)
    result = query_retrieval(run_root, "Skill Tree ownership", limit=5)
    assert result["backend"] == "sqlite_fts5"
    assert result["run_id"] and result["config_hash"]
    assert result["raw_source_reopen_guidance"]
    assert result["results"]
    row = result["results"][0]
    assert row["evidence_pointer"].startswith(row["path"] + "#L")
    assert row["page_hash"]
    assert row["source_atlas_path"].endswith("-source-atlas.md")
