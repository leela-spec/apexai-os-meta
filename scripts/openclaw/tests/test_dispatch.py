from __future__ import annotations

import hashlib
import json
import os
import base64
import subprocess
import tempfile
import time
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
POWERSHELL = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
DISPATCHER = Path(
    os.environ.get(
        "APEX_DISPATCHER_PATH",
        REPO_ROOT / "scripts" / "openclaw" / "dispatch-execution-request.ps1",
    )
).resolve()


class DispatchPreparationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name).resolve()
        self.trusted = self.root / "trusted"
        self.work = self.root / "work"
        self.trusted.mkdir()
        self.work.mkdir()
        self.prompt = self.trusted / "prompt.md"
        self.prompt_text = "Copy this exact harmless prompt."
        self.prompt.write_text(self.prompt_text, encoding="utf-8")
        self.request_path = self.root / "request.json"
        self.idempotency_key = "dispatch-" + hashlib.sha256(str(self.root).encode()).hexdigest()[:24]

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def request(self) -> dict:
        return {
            "schema_version": "apex.execution-request/v1",
            "execution_id": "exec-dispatch-001",
            "idempotency_key": self.idempotency_key,
            "origin": {"repo": str(REPO_ROOT), "workflow": "fixture", "step": "browser-capture"},
            "instruction": "apex-flow-executor",
            "provider": "chatgpt",
            "prompt_ref": {
                "path": str(self.prompt),
                "sha256": hashlib.sha256(self.prompt.read_bytes()).hexdigest(),
            },
            "roots": [
                {"path": str(self.trusted), "mode": "read"},
                {"path": str(self.work), "mode": "read_write"},
            ],
            "grants": {
                "tools": ["browser", "write"],
                "scripts": [],
                "commands": [],
                "git": {
                    "repo": str(self.work),
                    "remote": "origin",
                    "remote_url": str(self.work),
                    "branch": "main",
                    "operations": [],
                    "add_paths": [],
                    "commit_message": None,
                },
            },
            "success_criteria": ["response captured verbatim"],
            "stop_conditions": ["authentication required"],
            "result_path": str(self.work / "result.md"),
            "evidence_dir": str(self.work / "evidence"),
        }

    def dispatch(self, request: dict) -> subprocess.CompletedProcess[str]:
        self.request_path.write_text(json.dumps(request), encoding="utf-8")
        return subprocess.run(
            [
                POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                "-File", str(DISPATCHER), "-RequestPath", str(self.request_path), "-PrepareOnly",
            ],
            cwd=REPO_ROOT, text=True, capture_output=True, check=False,
        )

    def invoke(self, request: dict) -> subprocess.CompletedProcess[str]:
        self.request_path.write_text(json.dumps(request), encoding="utf-8")
        return subprocess.run(
            [
                POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                "-File", str(DISPATCHER), "-RequestPath", str(self.request_path),
            ],
            cwd=REPO_ROOT, text=True, capture_output=True, check=False, timeout=180,
        )

    def test_prepare_freezes_normalized_request_and_exact_prompt(self) -> None:
        result = self.dispatch(self.request())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "prepared")
        message = Path(payload["message_file"]).read_text(encoding="utf-8")
        self.assertIn(self.prompt_text, message)
        self.assertIn(hashlib.sha256(self.prompt.read_bytes()).hexdigest(), message)
        normalized = json.loads(Path(payload["normalized_request_file"]).read_text(encoding="utf-8"))
        self.assertEqual(normalized["execution_id"], "exec-dispatch-001")
        self.assertEqual(Path(payload["workspace"]), self.work / "evidence")
        self.assertFalse(Path(payload["state_file"]).is_relative_to(self.work))

    def test_prepare_is_idempotent_for_identical_request(self) -> None:
        first = self.dispatch(self.request())
        second = self.dispatch(self.request())
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        self.assertEqual(json.loads(first.stdout)["request_hash"], json.loads(second.stdout)["request_hash"])

    def test_prepare_rejects_same_idempotency_key_with_changed_request(self) -> None:
        first = self.dispatch(self.request())
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        changed = self.request()
        changed["success_criteria"] = ["different authority"]
        second = self.dispatch(changed)
        self.assertNotEqual(second.returncode, 0)
        self.assertIn("IDEMPOTENCY_CONFLICT", second.stderr + second.stdout)

    def test_prepare_rejects_exec_until_exact_approval_integration_exists(self) -> None:
        request = self.request()
        request["grants"]["tools"].append("exec")
        result = self.dispatch(request)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("UNSUPPORTED_DISPATCH_GRANT", result.stderr + result.stdout)

    def test_prepare_rejects_tampered_materialized_message(self) -> None:
        first = self.dispatch(self.request())
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        payload = json.loads(first.stdout)
        Path(payload["message_file"]).write_text("tampered", encoding="utf-8")
        second = self.dispatch(self.request())
        self.assertNotEqual(second.returncode, 0)
        self.assertIn("PREPARED_EVIDENCE_CHANGED", second.stderr + second.stdout)

    def test_prepare_rejects_precreated_child_symlink(self) -> None:
        evidence = self.work / "evidence"
        evidence.mkdir()
        external = self.work / "external.json"
        external.write_text("outside", encoding="utf-8")
        try:
            os.symlink(external, evidence / "normalized-request.json")
        except OSError as exc:
            self.skipTest(f"file symlink unavailable: {exc}")
        result = self.dispatch(self.request())
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(external.read_text(encoding="utf-8"), "outside")

    def test_prepare_rejects_reused_hard_link_artifact(self) -> None:
        first = self.dispatch(self.request())
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        payload = json.loads(first.stdout)
        message = Path(payload["message_file"])
        external = self.work / "external-message.md"
        external.write_bytes(message.read_bytes())
        message.unlink()
        os.link(external, message)
        second = self.dispatch(self.request())
        self.assertNotEqual(second.returncode, 0)
        self.assertIn("EVIDENCE_FILE_LINK", second.stderr + second.stdout)

    def test_completed_duplicate_rejects_tampered_result_evidence(self) -> None:
        prepared = self.dispatch(self.request())
        self.assertEqual(prepared.returncode, 0, prepared.stdout + prepared.stderr)
        payload = json.loads(prepared.stdout)
        raw_result = self.work / "evidence" / "openclaw-result.json"
        raw_result.write_text("original", encoding="utf-8")
        state_path = Path(payload["state_file"])
        state = json.loads(state_path.read_text(encoding="utf-8"))
        state["status"] = "completed"
        state["raw_result_file"] = str(raw_result)
        state["raw_result_sha256"] = hashlib.sha256(raw_result.read_bytes()).hexdigest()
        state_path.write_text(json.dumps(state), encoding="utf-8")
        raw_result.write_text("tampered", encoding="utf-8")
        duplicate = self.invoke(self.request())
        self.assertNotEqual(duplicate.returncode, 0)
        self.assertIn("COMPLETED_EVIDENCE_CHANGED", duplicate.stderr + duplicate.stdout)

    @unittest.skipUnless(os.environ.get("APEX_OPENCLAW_INTEGRATION") == "1", "live OpenClaw integration")
    def test_live_turn_completes_and_restores_exact_config_bytes(self) -> None:
        request = self.request()
        request["grants"]["tools"] = ["session_status"]
        config_path = Path.home() / ".openclaw" / "openclaw.json"
        before = hashlib.sha256(config_path.read_bytes()).hexdigest()
        result = self.invoke(request)
        after = hashlib.sha256(config_path.read_bytes()).hexdigest()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "completed")
        self.assertTrue(Path(payload["raw_result_file"]).is_file())
        self.assertEqual(after, before)

    @unittest.skipUnless(os.environ.get("APEX_OPENCLAW_INTEGRATION") == "1", "live config recovery integration")
    def test_recover_only_restores_journaled_config_bytes(self) -> None:
        config_path = Path.home() / ".openclaw" / "openclaw.json"
        journal_path = Path(os.environ["LOCALAPPDATA"]) / "ApexExecutor" / "openclaw-config-journal.json"
        original = config_path.read_bytes()
        config = json.loads(original.decode("utf-8"))
        config["agents"]["list"][1]["workspace"] = str(self.work / "evidence")
        shaped = json.dumps(config, separators=(",", ":")).encode("utf-8")
        journal = {
            "schema_version": "apex.openclaw-config-journal/v1",
            "config_path": str(config_path),
            "original_sha256": hashlib.sha256(original).hexdigest(),
            "original_base64": base64.b64encode(original).decode("ascii"),
            "shaped_sha256": hashlib.sha256(shaped).hexdigest(),
        }
        journal_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            journal_path.write_text(json.dumps(journal), encoding="utf-8")
            config_path.write_bytes(shaped)
            result = subprocess.run(
                [
                    POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                    "-File", str(DISPATCHER), "-RecoverConfigOnly",
                ],
                cwd=REPO_ROOT, text=True, capture_output=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(config_path.read_bytes(), original)
            self.assertFalse(journal_path.exists())
        finally:
            config_path.write_bytes(original)
            journal_path.unlink(missing_ok=True)

    @unittest.skipUnless(os.environ.get("APEX_OPENCLAW_INTEGRATION") == "1", "live recovery race integration")
    def test_recovery_waits_for_active_live_turn(self) -> None:
        request = self.request()
        request["grants"]["tools"] = ["session_status"]
        self.request_path.write_text(json.dumps(request), encoding="utf-8")
        journal_path = Path(os.environ["LOCALAPPDATA"]) / "ApexExecutor" / "openclaw-config-journal.json"
        live_command = [
            POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
            "-File", str(DISPATCHER), "-RequestPath", str(self.request_path),
        ]
        recovery_command = [
            POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
            "-File", str(DISPATCHER), "-RecoverConfigOnly",
        ]
        live = subprocess.Popen(live_command, cwd=REPO_ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        recovery = None
        try:
            deadline = time.monotonic() + 30
            while not journal_path.exists() and live.poll() is None and time.monotonic() < deadline:
                time.sleep(0.1)
            self.assertTrue(journal_path.exists(), "live turn never reached shaped-config stage")
            recovery = subprocess.Popen(
                recovery_command, cwd=REPO_ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            time.sleep(1)
            self.assertIsNone(recovery.poll(), "recovery ran concurrently with the active live turn")
            live_stdout, live_stderr = live.communicate(timeout=180)
            recovery_stdout, recovery_stderr = recovery.communicate(timeout=60)
            self.assertEqual(live.returncode, 0, live_stdout + live_stderr)
            self.assertEqual(recovery.returncode, 0, recovery_stdout + recovery_stderr)
        finally:
            for process in (live, recovery):
                if process is not None and process.poll() is None:
                    process.kill()
                    process.communicate()


if __name__ == "__main__":
    unittest.main()
