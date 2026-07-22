from __future__ import annotations

import json
from pathlib import Path

import pytest

from apex_kb.errors import ApexKBError
from apex_kb.retrieval import build_retrieval, retrieval_health


def _retrieval_run(tmp_path: Path, *, status: str = "accepted") -> tuple[Path, dict]:
    run_root = tmp_path / "run"
    dossier = run_root / "wiki" / "concepts" / "skill-tree.md"
    atlas = run_root / "wiki" / "summaries" / "skill-tree-source-atlas.md"
    frontmatter = f"---\ntitle: Skill Tree\ntopic_id: skill-tree\npage_type: dossier\nstatus: {status}\n---\n"
    dossier.parent.mkdir(parents=True)
    atlas.parent.mkdir(parents=True)
    dossier.write_text(frontmatter + "# Skill Tree\n\nApex retrieval content.\n", encoding="utf-8")
    atlas.write_text(
        frontmatter.replace("page_type: dossier", "page_type: source_atlas")
        + "# Skill Tree source atlas\n\nApex source evidence.\n",
        encoding="utf-8",
    )
    (run_root / "runs" / "run-test" / "stage-results").mkdir(parents=True)
    manifest = {
        "run_id": "run-test",
        "config_hash": "a" * 64,
        "created_at": "2026-07-21T00:00:00Z",
        "artifact_layout": {"stage_results": "runs/run-test/stage-results"},
        "topics": [
            {
                "topic_id": "skill-tree",
                "name": "Skill Tree",
                "expected_routes": {
                    "dossier": "wiki/concepts/skill-tree.md",
                    "source_atlas": "wiki/summaries/skill-tree-source-atlas.md",
                },
            }
        ],
    }
    (run_root / "run-manifest.json").write_text(
        json.dumps(manifest, sort_keys=True), encoding="utf-8"
    )
    return run_root, manifest


def test_retrieval_rejects_accepted_pending_marker(tmp_path: Path):
    run_root, manifest = _retrieval_run(tmp_path, status="accepted_pending_evaluation")

    with pytest.raises(ApexKBError) as caught:
        build_retrieval(run_root, manifest, ["skill-tree"])

    assert caught.value.code == "page_not_accepted"


def test_retrieval_health_checks_sqlite_fts_and_identity(tmp_path: Path):
    run_root, manifest = _retrieval_run(tmp_path)
    built = build_retrieval(run_root, manifest, ["skill-tree"])

    health = built["health"]
    assert health["fresh"] is True
    assert health["integrity_ok"] is True
    assert health["sqlite_integrity_ok"] is True
    assert health["sqlite_integrity_result"] == ["ok"]
    assert health["fts5_healthy"] is True
    assert health["metadata_matches"] is True
    assert health["deterministic_identity_matches"] is True


def test_retrieval_health_rejects_manifest_metadata_drift(tmp_path: Path):
    run_root, manifest = _retrieval_run(tmp_path)
    build_retrieval(run_root, manifest, ["skill-tree"])
    index_path = run_root / "derived" / "search" / "index-manifest.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    index["chunk_count"] += 1
    index_path.write_text(json.dumps(index, sort_keys=True), encoding="utf-8")

    health = retrieval_health(run_root)

    assert health["metadata_matches"] is False
    assert health["deterministic_identity_matches"] is False
    assert health["integrity_ok"] is False
    assert health["fresh"] is False


def test_retrieval_rebuild_has_deterministic_database_identity(tmp_path: Path):
    run_root, manifest = _retrieval_run(tmp_path)

    first = build_retrieval(run_root, manifest, ["skill-tree"])["manifest"]["database_sha256"]
    second = build_retrieval(run_root, manifest, ["skill-tree"])["manifest"]["database_sha256"]

    assert second == first
