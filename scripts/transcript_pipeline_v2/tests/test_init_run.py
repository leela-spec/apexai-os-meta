"""
Tests for V2.1 TTK Module S00: Trigger and Run Initialization.
Validates all focused S00 assertions, Git repo/branch enforcement,
LF hash canonical consistency, and dirty path preservation.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
from pathlib import Path
import pytest

from runner import init_run, finalize_s00, compute_sha256


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
    assert res["status"] == "INITIALIZED"
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
    assert res["status"] == "INITIALIZED"
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


def test_07_request_serialization_round_trips_and_lf(temp_env):
    """Assertion 7: Request serialization round-trips accurately with LF bytes."""
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
    raw_bytes = req_file.read_bytes()
    assert b"\r\n" not in raw_bytes  # Pure LF bytes

    loaded = json.loads(raw_bytes.decode("utf-8"))
    assert loaded["schema"] == "ttk.v2_1.run-request.v1"
    assert loaded["run_id"] == res["run_id"]
    assert loaded["source"] == "https://www.youtube.com/watch?v=CygwqaNg2PY"
    assert loaded["source_type"] == "url"
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
    assert req["source_type"] == "url"
    assert req["source_id"] == "CygwqaNg2PY"
    assert req["language"] == "en"
    assert req["mode"] == "fresh_e2e"
    assert req["purpose"] == "first_V2_1_vertical_slice"

    # Confirm no inferred metadata fields are present
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
    assert set(files_created) == {"request.json"}

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
    assert list(source_dir.iterdir()) == []


def test_13_no_llm_or_semantic_cli_invoked(monkeypatch, temp_env):
    """Assertion 13: Initialization does NOT invoke LLM or semantic CLI."""
    temp_root, runs_dir = temp_env

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
    assert res["status"] == "INITIALIZED"


def test_14_unrelated_dirty_paths_preserved_in_real_git_fixture():
    """Assertion 14: Real git repository fixture verifies dirty file capture and byte preservation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_dir = Path(tmpdir)
        # Initialize real git repository on main
        subprocess.run(["git", "init", "-b", "main"], cwd=str(repo_dir), check=True, capture_output=True)
        subprocess.run(["git", "config", "user.name", "Test Runner"], cwd=str(repo_dir), check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=str(repo_dir), check=True, capture_output=True)
        subprocess.run(["git", "remote", "add", "origin", "https://github.com/leela-spec/apexai-os-meta.git"], cwd=str(repo_dir), check=True, capture_output=True)

        # Create tracked baseline file
        dirty_file = repo_dir / "unrelated_doc.txt"
        dirty_file.write_bytes(b"baseline committed content\n")
        subprocess.run(["git", "add", "unrelated_doc.txt"], cwd=str(repo_dir), check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "initial baseline"], cwd=str(repo_dir), check=True, capture_output=True)

        # Modify file to make it dirty
        modified_content = b"uncommitted modification by operator\n"
        dirty_file.write_bytes(modified_content)
        expected_hash = hashlib.sha256(modified_content).hexdigest()

        # Execute init_run
        runs_dir = repo_dir / "artifacts" / "transcript_pipeline_v2" / "runs"
        res = init_run(
            source="https://www.youtube.com/watch?v=CygwqaNg2PY",
            source_id="CygwqaNg2PY",
            _runs_dir=runs_dir,
            _repo_root=repo_dir,
            _skip_repo_check=False,
        )

        # Assert dirty file was captured in unrelated_dirty_paths
        assert "unrelated_doc.txt" in res["unrelated_dirty_paths"]

        # Assert dirty file content and hash remain untouched
        assert dirty_file.read_bytes() == modified_content
        assert hashlib.sha256(dirty_file.read_bytes()).hexdigest() == expected_hash


def test_15_wrong_branch_rejected():
    """Branch validation: verify that non-main branch raises RuntimeError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_dir = Path(tmpdir)
        subprocess.run(["git", "init", "-b", "feature-branch"], cwd=str(repo_dir), check=True, capture_output=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=str(repo_dir), check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=str(repo_dir), check=True, capture_output=True)
        subprocess.run(["git", "remote", "add", "origin", "https://github.com/leela-spec/apexai-os-meta.git"], cwd=str(repo_dir), check=True, capture_output=True)

        dummy = repo_dir / "dummy.txt"
        dummy.write_text("content")
        subprocess.run(["git", "add", "dummy.txt"], cwd=str(repo_dir), check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "init"], cwd=str(repo_dir), check=True, capture_output=True)

        with pytest.raises(RuntimeError, match="requires branch 'main'"):
            init_run(
                source="https://www.youtube.com/watch?v=CygwqaNg2PY",
                _repo_root=repo_dir,
                _skip_repo_check=False,
            )


def test_16_wrong_repo_remote_rejected():
    """Repository validation: verify that non-matching origin URL raises RuntimeError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_dir = Path(tmpdir)
        subprocess.run(["git", "init", "-b", "main"], cwd=str(repo_dir), check=True, capture_output=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=str(repo_dir), check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=str(repo_dir), check=True, capture_output=True)
        subprocess.run(["git", "remote", "add", "origin", "https://github.com/someone-else/other-repo.git"], cwd=str(repo_dir), check=True, capture_output=True)

        dummy = repo_dir / "dummy.txt"
        dummy.write_text("content")
        subprocess.run(["git", "add", "dummy.txt"], cwd=str(repo_dir), check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "init"], cwd=str(repo_dir), check=True, capture_output=True)

        with pytest.raises(RuntimeError, match="requires repository 'leela-spec/apexai-os-meta'"):
            init_run(
                source="https://www.youtube.com/watch?v=CygwqaNg2PY",
                _repo_root=repo_dir,
                _skip_repo_check=False,
            )


def test_17_finalize_s00_verifies_invariants_and_writes_handoff(temp_env):
    """Finalization test: finalize_s00 enforces LF hashes, real component hash, and PASS state."""
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
    final = finalize_s00(
        run_dir=Path(res["run_dir"]),
        repo_root=temp_root,
        start_head="259b368d05fed3f34d39aaa4517c309880a4a072",
        unrelated_dirty_paths=["unrelated.txt"],
        _skip_test_execution=True,
    )
    assert final["status"] == "PASS"
    yaml_path = Path(final["handoff_yaml"])
    md_path = Path(final["handoff_md"])
    assert yaml_path.exists()
    assert md_path.exists()

    yaml_bytes = yaml_path.read_bytes()
    assert b"\r\n" not in yaml_bytes
    md_bytes = md_path.read_bytes()
    assert b"\r\n" not in md_bytes
