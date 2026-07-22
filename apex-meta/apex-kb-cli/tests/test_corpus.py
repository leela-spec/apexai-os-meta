from __future__ import annotations

from pathlib import Path

from apex_kb.corpus import build_corpus_intelligence, check_source_drift
from apex_kb.io import iter_ndjson, load_json
from apex_kb.lifecycle import load_run

from .helpers import default_topics, initialize


def test_whole_corpus_inventory_exclusions_duplicates_and_untruncated_rankings(tmp_path: Path):
    topic = default_topics()[0]
    run_root, source_repo, _ = initialize(tmp_path, output="analysis_only", topics=[topic], include_formats=False)
    source = source_repo / "LeelaAppDevelopment" / "Bulk"
    source.mkdir()
    for index in range(35):
        (source / f"skill-tree-{index:02d}.md").write_text(f"# Skill Tree {index}\nSkill Tree Epic Block Chunk.\n", encoding="utf-8")
    manifest, _ = load_run(run_root)
    result = build_corpus_intelligence(run_root, manifest)
    topic_map = result["topic_maps"]["skill-tree"]
    assert topic_map["candidate_set_truncated"] is False
    assert topic_map["candidate_count"] >= 39
    assert topic_map["candidates"][30]["rank"] == 31
    rows = list(iter_ndjson(run_root / "manifests/source-inventory.ndjson"))
    assert any(row["inclusion_state"] == "excluded" and row["repository_path"].endswith("skill-tree-generated.md") for row in rows)
    duplicates = load_json(run_root / "manifests/phase0/duplicate-map.json")
    assert duplicates["exact_hash_groups"]
    report = (run_root / "manifests/phase0/phase0-navigation-report.md").read_text(encoding="utf-8")
    assert "Canonical set truncated: **no**" not in report  # report states the rule globally rather than repeating the projection marker
    assert "never top-N truncated" in report


def test_ambiguous_term_alone_does_not_surface_unrelated_tree_file(tmp_path: Path):
    topic = default_topics()[0]
    run_root, _, _ = initialize(tmp_path, output="analysis_only", topics=[topic], include_formats=False)
    manifest, _ = load_run(run_root)
    result = build_corpus_intelligence(run_root, manifest)
    paths = {item["repository_path"] for item in result["topic_maps"]["skill-tree"]["candidates"]}
    assert "LeelaAppDevelopment/Notes/tree-care.md" not in paths


def test_matching_is_boundary_aware_and_normalizes_hyphenated_phrases(tmp_path: Path):
    topic = {
        **default_topics()[0],
        "primary_phrases": ["skill tree"],
        "aliases": [],
        "supporting_terms": ["tree"],
        "ambiguous_terms": [],
        "negative_terms": [],
    }
    run_root, source_repo, _ = initialize(tmp_path, output="analysis_only", topics=[topic], include_formats=False)
    notes = source_repo / "LeelaAppDevelopment" / "Notes"
    (notes / "street-map.md").write_text("# Street map\nA street map for navigation.\n", encoding="utf-8")
    (notes / "skill-tree-route.md").write_text("# Route\nThe skill-tree route is current.\n", encoding="utf-8")
    manifest, _ = load_run(run_root)
    result = build_corpus_intelligence(run_root, manifest)
    paths = {item["repository_path"] for item in result["topic_maps"]["skill-tree"]["candidates"]}
    assert "LeelaAppDevelopment/Notes/street-map.md" not in paths
    assert "LeelaAppDevelopment/Notes/skill-tree-route.md" in paths


def test_copy_and_snapshot_modes_preserve_source_hashes(tmp_path: Path):
    for mode in ("copy_into_kb", "snapshot_copy"):
        case = tmp_path / mode
        run_root, source_repo, _ = initialize(case, output="analysis_only", handling=mode, topics=[default_topics()[0]], include_formats=False)
        original = source_repo / "LeelaAppDevelopment/01_Features/102 - Epics (Database + Skill Tree).md"
        before = original.read_bytes()
        manifest, _ = load_run(run_root)
        result = build_corpus_intelligence(run_root, manifest)
        records = result["records"]
        copied = [item for item in records if item["custody_path"]]
        assert copied and all((run_root / item["custody_path"]).is_file() for item in copied)
        assert all("\\" not in item["custody_path"] for item in copied)
        assert original.read_bytes() == before


def test_source_drift_detects_complete_tree_changes_without_crashing(tmp_path: Path, monkeypatch):
    run_root, source_repo, _ = initialize(tmp_path, output="analysis_only", topics=[default_topics()[0]], include_formats=False)
    manifest, _ = load_run(run_root)
    build_corpus_intelligence(run_root, manifest)
    source = source_repo / "LeelaAppDevelopment"
    changed = source / "01_Features/102 - Epics (Database + Skill Tree).md"
    changed.write_text(changed.read_text(encoding="utf-8") + "\nDrift.\n", encoding="utf-8")
    (source / "Notes/tree-care.md").unlink()
    (source / "Notes/added.md").write_text("# Added\n", encoding="utf-8")

    from apex_kb.corpus import engine

    real_sha256_file = engine.sha256_file
    unreadable = source / "Archive/Skill Tree v1.md"

    def fail_one_path(path: Path):
        if path == unreadable:
            raise PermissionError("simulated unreadable source")
        return real_sha256_file(path)

    monkeypatch.setattr(engine, "sha256_file", fail_one_path)
    report = check_source_drift(run_root, manifest)
    assert report["fresh"] is False
    assert report["added"] == ["LeelaAppDevelopment/Notes/added.md"]
    assert report["deleted"] == ["LeelaAppDevelopment/Notes/tree-care.md"]
    assert [item["repository_path"] for item in report["changed"]] == [
        "LeelaAppDevelopment/01_Features/102 - Epics (Database + Skill Tree).md"
    ]
    assert report["newly_unreadable"] == ["LeelaAppDevelopment/Archive/Skill Tree v1.md"]
