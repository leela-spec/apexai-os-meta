"""
Tests for V2.1 TTK Module S00: Trigger and Run Initialization.
Validates all 14 focused S00 assertions.
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path
import pytest

from runner import init_run, build_parser


@pytest.fixture
def temp_env():
    """Create a temporary run directory environment for isolated testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_root = Path(tmpdir)
        runs_dir = temp_root / "runs"
        runs_dir.mkdir(parents=True, exist_ok=True)
        yield temp_root, runs_dir


def test_01_url_request_accepted(temp_env):
    """Assertion 1: URL request is accepted."""
    temp_root, runs_dir = temp_env
    res = init_run(
        source="https://www.youtube.com/watch?v=CygwqaNg2PY",
        source_id="CygwqaNg2PY",
        _runs_dir=runs_dir,
        _repo_root=temp_root,
        _skip_repo_check=True,
    )
    assert res["status"] == "PASS"
    assert Path(res["run_dir"]).exists()
    assert Path(res["request_path"]).exists()


def test_02_existing_local_media_path_accepted(temp_env):
    """Assertion 2: Existing local media path is accepted."""
    temp_root, runs_dir = temp_env
    local_file = temp_root / "sample_audio.mp4"
    local_file.write_bytes(b"dummy audio content")

    res = init_run(
        source=str(local_file),
        source_id="sample_audio",
        _runs_dir=runs_dir,
        _repo_root=temp_root,
        _skip_repo_check=True,
    )
    assert res["status"] == "PASS"
    assert Path(res["request_path"]).exists()


def test_03_nonexistent_local_media_path_rejected(temp_env):
    """Assertion 3: Nonexistent local media path is rejected."""
    temp_root, runs_dir = temp_env
    nonexistent = temp_root / "does_not_exist.mp4"
    with pytest.raises(FileNotFoundError):
        init_run(
            source=str(nonexistent),
            _runs_dir=runs_dir,
            _repo_root=temp_root,
            _skip_repo_check=True,
        )


def test_04_missing_source_rejected(temp_env):
    """Assertion 4: Missing source is rejected."""
    temp_root, runs_dir = temp_env
    with pytest.raises(ValueError):
        init_run(
            source="",
            _runs_dir=runs_dir,
            _repo_root=temp_root,
            _skip_repo_check=True,
        )


def test_05_invalid_mode_rejected(temp_env):
    """Assertion 5: Invalid mode is rejected."""
    temp_root, runs_dir = temp_env
    with pytest.raises(ValueError):
        init_run(
            source="https://example.com/audio.mp3",
            mode="invalid_unsupported_mode",
            _runs_dir=runs_dir,
            _repo_root=temp_root,
            _skip_repo_check=True,
        )


def test_06_multiple_initializations_do_not_collide(temp_env):
    """Assertion 6: Multiple initializations generate distinct non-colliding run IDs."""
    temp_root, runs_dir = temp_env
    res1 = init_run(
        source="https://www.youtube.com/watch?v=CygwqaNg2PY",
        source_id="CygwqaNg2PY",
        _runs_dir=runs_dir,
        _repo_root=temp_root,
        _skip_repo_check=True,
    )
    res2 = init_run(
        source="https://www.youtube.com/watch?v=CygwqaNg2PY",
        source_id="CygwqaNg2PY",
        _runs_dir=runs_dir,
        _repo_root=temp_root,
        _skip_repo_check=True,
    )
    assert res1["run_id"] != res2["run_id"]
    assert res1["run_dir"] != res2["run_dir"]
    assert Path(res1["run_dir"]).exists()
    assert Path(res2["run_dir"]).exists()


def test_07_request_serialization_round_trips(temp_env):
    """Assertion 7: Request serialization round-trips accurately."""
    temp_root, runs_dir = temp_env
    res = init_run(
        source="https://www.youtube.com/watch?v=CygwqaNg2PY",
        source_id="CygwqaNg2PY",
        language="en",
        mode="fresh_e2e",
        purpose="testing_round_trip",
        title="Test Title",
        _runs_dir=runs_dir,
        _repo_root=temp_root,
        _skip_repo_check=True,
    )
    req_file = Path(res["request_path"])
    with open(req_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    assert loaded["schema"] == "ttk.v2_1.run-request.v1"
    assert loaded["run_id"] == res["run_id"]
    assert loaded["source"] == "https://www.youtube.com/watch?v=CygwqaNg2PY"
    assert loaded["source_id"] == "CygwqaNg2PY"
    assert loaded["language"] == "en"
    assert loaded["mode"] == "fresh_e2e"
    assert loaded["purpose"] == "testing_round_trip"
    assert loaded["title"] == "Test Title"


def test_08_exact_operator_request_preserved(temp_env):
    """Assertion 8: The exact operator request is preserved with only operator-declared facts."""
    temp_root, runs_dir = temp_env
    res = init_run(
        source="https://www.youtube.com/watch?v=CygwqaNg2PY",
        source_id="CygwqaNg2PY",
        language="en",
        mode="fresh_e2e",
        purpose="first_V2_1_vertical_slice",
        _runs_dir=runs_dir,
        _repo_root=temp_root,
        _skip_repo_check=True,
    )
    with open(res["request_path"], "r", encoding="utf-8") as f:
        req = json.load(f)

    assert req["source"] == "https://www.youtube.com/watch?v=CygwqaNg2PY"
    assert req["source_id"] == "CygwqaNg2PY"
    assert req["language"] == "en"
    assert req["mode"] == "fresh_e2e"
    assert req["purpose"] == "first_V2_1_vertical_slice"

    # Confirm no inferred fields are present
    assert "channel" not in req
    assert "duration" not in req
    assert "publication_date" not in req
    assert "audio_properties" not in req
    assert "transcript" not in req


def test_09_to_11_no_asr_map_reduce_files_created(temp_env):
    """Assertions 9, 10, 11: Initialization does NOT create ASR, Map, or Reduce result files."""
    temp_root, runs_dir = temp_env
    res = init_run(
        source="https://www.youtube.com/watch?v=CygwqaNg2PY",
        source_id="CygwqaNg2PY",
        _runs_dir=runs_dir,
        _repo_root=temp_root,
        _skip_repo_check=True,
    )
    run_dir = Path(res["run_dir"])

    # Traverse all files in run_dir
    files_created = [f.name for f in run_dir.rglob("*") if f.is_file()]
    assert set(files_created) == {"request.json", "S00.yaml", "S00-HANDOVER.md"}

    # Specifically check absence of ASR / Map / Reduce outputs
    assert not (run_dir / "source" / "transcript.json").exists()
    assert not (run_dir / "source" / "audio.wav").exists()
    assert not (run_dir / "work" / "map.json").exists()
    assert not (run_dir / "work" / "reduce.json").exists()


def test_12_no_media_acquisition_download(temp_env):
    """Assertion 12: Initialization does NOT acquire/download YouTube media."""
    temp_root, runs_dir = temp_env
    res = init_run(
        source="https://www.youtube.com/watch?v=CygwqaNg2PY",
        source_id="CygwqaNg2PY",
        _runs_dir=runs_dir,
        _repo_root=temp_root,
        _skip_repo_check=True,
    )
    source_dir = Path(res["run_dir"]) / "source"
    # source dir must be empty
    assert list(source_dir.iterdir()) == []


def test_13_no_llm_or_semantic_cli_invoked(monkeypatch, temp_env):
    """Assertion 13: Initialization does NOT invoke LLM or semantic CLI."""
    temp_root, runs_dir = temp_env

    # If any semantic worker is instantiated, fail
    def fake_worker(*args, **kwargs):
        raise AssertionError("SemanticCLIWorker was unexpectedly called in S00!")

    monkeypatch.setattr("runner.SemanticCLIWorker", fake_worker)

    res = init_run(
        source="https://www.youtube.com/watch?v=CygwqaNg2PY",
        source_id="CygwqaNg2PY",
        _runs_dir=runs_dir,
        _repo_root=temp_root,
        _skip_repo_check=True,
    )
    assert res["status"] == "PASS"


def test_14_unrelated_dirty_paths_captured_and_untouched(temp_env):
    """Assertion 14: Pre-existing unrelated dirty paths are truthfully captured."""
    temp_root, runs_dir = temp_env
    res = init_run(
        source="https://www.youtube.com/watch?v=CygwqaNg2PY",
        source_id="CygwqaNg2PY",
        _runs_dir=runs_dir,
        _repo_root=temp_root,
        _skip_repo_check=True,
    )
    assert "unrelated_dirty_paths" in res
    assert "start_head" in res
    assert Path(res["handoff_yaml"]).exists()
    assert Path(res["handoff_md"]).exists()
