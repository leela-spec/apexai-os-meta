from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
RELAY = REPO_ROOT / "scripts" / "openclaw" / "ttk_v3_relay.py"
CURRENT_WORK = Path(
    "SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/CURRENT-WORK.md"
)
M00_RESULT = Path(
    "SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/results/M00-RESULT.md"
)
M00_SEED = Path(
    "SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/results/M00-PROVEN-SYSTEMS-SEED.md"
)


def run(*args: str, cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=False)
    if check and result.returncode != 0:
        raise AssertionError(result.stdout + result.stderr)
    return result


def git(cwd: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return run("git", *args, cwd=cwd, check=check)


def commit_all(repo: Path, message: str) -> str:
    git(repo, "add", "-A")
    git(repo, "commit", "-m", message)
    return git(repo, "rev-parse", "HEAD").stdout.strip()


def relay(repo: Path, state: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return run(
        sys.executable,
        str(RELAY),
        "--repo",
        str(repo),
        "--state-path",
        str(state),
        *args,
        cwd=REPO_ROOT,
        check=False,
    )


def relay_state(
    *,
    status: str,
    active_module: str | None,
    on_pass_status: str | None,
    on_pass_module: str | None,
    review_gate: str | None,
    stop_marker: str,
) -> str:
    payload = {
        "schema_version": "ttk.current-work/v1",
        "status": status,
        "active_module": active_module,
        "on_pass": {"status": on_pass_status, "active_module": on_pass_module},
        "review_gate": review_gate,
        "stop_marker": stop_marker,
    }
    return (
        "# CURRENT WORK — V3\n\n"
        "<!-- ttk-relay-state\n"
        + json.dumps(payload, sort_keys=True)
        + "\n-->\n"
    )


class RelayRepoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.remote = self.root / "remote.git"
        self.seed = self.root / "seed"
        self.work = self.root / "work"
        self.state = self.root / "state" / "relay.json"

        git(self.root, "init", "--bare", str(self.remote))
        git(self.root, "clone", str(self.remote), str(self.seed))
        git(self.seed, "config", "user.name", "Seed")
        git(self.seed, "config", "user.email", "seed@example.invalid")
        git(self.seed, "checkout", "-b", "main")
        (self.seed / CURRENT_WORK).parent.mkdir(parents=True)
        (self.seed / CURRENT_WORK).write_text(
            relay_state(
                status="READY_FOR_M00",
                active_module="execution-modules/M00-ORCHESTRATION-SMOKE.md",
                on_pass_status="READY_FOR_M01",
                on_pass_module="execution-modules/M01-PROVEN-SYSTEMS-LANDSCAPE-AND-BASELINES.md",
                review_gate=None,
                stop_marker="STOP_AFTER_M00",
            ),
            encoding="utf-8",
        )
        modules = self.seed / CURRENT_WORK.parent / "execution-modules"
        modules.mkdir(parents=True)
        (modules / "M00-ORCHESTRATION-SMOKE.md").write_text("# M00\n", encoding="utf-8")
        (modules / "M01-PROVEN-SYSTEMS-LANDSCAPE-AND-BASELINES.md").write_text(
            "# M01\n", encoding="utf-8"
        )
        (modules / "M05-EVALUATION-AND-SELECTION.md").write_text("# M05\n", encoding="utf-8")
        initial = commit_all(self.seed, "initial authority")
        git(self.seed, "push", "-u", "origin", "main")
        git(self.root, "clone", "--branch", "main", str(self.remote), str(self.work))
        git(self.work, "config", "user.name", "Executor")
        git(self.work, "config", "user.email", "executor@example.invalid")
        self.initial = initial

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_sync_fast_forwards_to_actual_remote_main(self) -> None:
        (self.seed / "authority.txt").write_text("next\n", encoding="utf-8")
        remote_head = commit_all(self.seed, "remote authority")
        git(self.seed, "push", "origin", "main")

        result = relay(self.work, self.state, "sync")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "synced")
        self.assertEqual(payload["head"], remote_head)
        self.assertEqual(git(self.work, "rev-parse", "HEAD").stdout.strip(), remote_head)

    def test_sync_refuses_a_dirty_worktree_without_fetching_side_effects(self) -> None:
        (self.work / "local.txt").write_text("dirty\n", encoding="utf-8")

        result = relay(self.work, self.state, "sync")

        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stderr)["error_code"], "DIRTY_WORKTREE")
        self.assertEqual(git(self.work, "rev-parse", "HEAD").stdout.strip(), self.initial)

    def test_sync_refuses_diverged_main(self) -> None:
        (self.work / "local.txt").write_text("local\n", encoding="utf-8")
        commit_all(self.work, "local commit")
        (self.seed / "remote.txt").write_text("remote\n", encoding="utf-8")
        commit_all(self.seed, "remote commit")
        git(self.seed, "push", "origin", "main")

        result = relay(self.work, self.state, "sync")

        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stderr)["error_code"], "DIVERGED_MAIN")

    def write_m00_pass(self, *, unexpected: bool = False) -> str:
        base = self.work / CURRENT_WORK.parent
        results = base / "results"
        results.mkdir(parents=True, exist_ok=True)
        (self.work / M00_RESULT).write_text("# M00 Result\n\nPASS\n", encoding="utf-8")
        (self.work / M00_SEED).write_text(
            "# Seed\n\n- https://example.com/a\n- https://example.com/b\n- https://example.com/c\n",
            encoding="utf-8",
        )
        (self.work / CURRENT_WORK).write_text(
            relay_state(
                status="READY_FOR_M01",
                active_module="execution-modules/M01-PROVEN-SYSTEMS-LANDSCAPE-AND-BASELINES.md",
                on_pass_status="WAITING_FOR_R1",
                on_pass_module=None,
                review_gate="R1",
                stop_marker="M00_COMPLETE",
            ),
            encoding="utf-8",
        )
        if unexpected:
            (self.work / "unexpected.txt").write_text("must not ship\n", encoding="utf-8")
        head = commit_all(self.work, "M00 result")
        git(self.work, "push", "origin", "main")
        return head

    def test_verify_m00_accepts_only_the_bounded_antigravity_result(self) -> None:
        result_head = self.write_m00_pass()

        result = relay(self.work, self.state, "verify-result", "--module", "M00", "--before-sha", self.initial)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "verified")
        self.assertEqual(payload["result_sha"], result_head)
        saved = json.loads(self.state.read_text(encoding="utf-8"))
        self.assertEqual(saved["module"], "M00")
        self.assertEqual(saved["result_sha"], result_head)

    def test_verify_m00_rejects_an_unexpected_committed_path(self) -> None:
        self.write_m00_pass(unexpected=True)

        result = relay(self.work, self.state, "verify-result", "--module", "M00", "--before-sha", self.initial)

        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stderr)["error_code"], "UNEXPECTED_RESULT_PATH")

    def test_gate_event_is_idempotent_and_binds_the_exact_result_sha(self) -> None:
        first = relay(
            self.work,
            self.state,
            "prepare-gate",
            "--gate",
            "R1",
            "--result-sha",
            self.initial,
        )
        second = relay(
            self.work,
            self.state,
            "prepare-gate",
            "--gate",
            "R1",
            "--result-sha",
            self.initial,
        )

        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        first_payload = json.loads(first.stdout)
        second_payload = json.loads(second.stdout)
        self.assertEqual(first_payload["event_id"], f"R1:{self.initial}")
        self.assertEqual(second_payload["status"], "duplicate")
        self.assertIn(f"[TTK_RELAY_GATE event_id=R1:{self.initial}]", first_payload["message"])
        self.assertIn("ChatGPT must create and push", first_payload["message"])

    def test_gate_submission_can_only_mark_the_prepared_event_once(self) -> None:
        event_id = f"R1:{self.initial}"
        relay(
            self.work,
            self.state,
            "prepare-gate",
            "--gate",
            "R1",
            "--result-sha",
            self.initial,
        )

        first = relay(self.work, self.state, "mark-gate-submitted", "--event-id", event_id)
        second = relay(self.work, self.state, "mark-gate-submitted", "--event-id", event_id)

        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        self.assertEqual(json.loads(first.stdout)["status"], "submitted")
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        self.assertEqual(json.loads(second.stdout)["status"], "duplicate")

    def test_verify_authority_scans_past_unrelated_commits_and_fast_forwards(self) -> None:
        (self.seed / "unrelated.txt").write_text("unrelated\n", encoding="utf-8")
        commit_all(self.seed, "unrelated")
        (self.seed / CURRENT_WORK).write_text(
            relay_state(
                status="READY_FOR_M05",
                active_module="execution-modules/M05-EVALUATION-AND-SELECTION.md",
                on_pass_status="WAITING_FOR_R2",
                on_pass_module=None,
                review_gate="R2",
                stop_marker="R1_REVIEWED",
            ),
            encoding="utf-8",
        )
        authority_head = commit_all(self.seed, "GPT authority")
        git(self.seed, "push", "origin", "main")

        result = relay(
            self.work,
            self.state,
            "verify-authority",
            "--gate",
            "R1",
            "--after-sha",
            self.initial,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "authority_verified")
        self.assertEqual(payload["authority_sha"], authority_head)
        self.assertEqual(git(self.work, "rev-parse", "HEAD").stdout.strip(), authority_head)

    def test_unknown_commit_operation_is_rejected_without_changing_head(self) -> None:
        before = git(self.work, "rev-parse", "HEAD").stdout.strip()

        result = relay(self.work, self.state, "commit")

        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(git(self.work, "rev-parse", "HEAD").stdout.strip(), before)


if __name__ == "__main__":
    unittest.main()
