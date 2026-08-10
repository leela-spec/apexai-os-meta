from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR = REPO_ROOT / "scripts" / "openclaw" / "validate-execution-request.py"


class ExecutionRequestValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name).resolve()
        self.trusted = self.root / "trusted"
        self.outputs = self.root / "outputs"
        self.git_repo = self.outputs / "repo"
        self.trusted.mkdir()
        self.outputs.mkdir()
        self.git_repo.mkdir()
        self.prompt = self.trusted / "prompt.md"
        self.prompt.write_text("bounded prompt", encoding="utf-8")
        self.script = self.trusted / "worker.ps1"
        self.script.write_text("Write-Output 'ok'\n", encoding="utf-8")
        self.powershell = Path(
            r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
        )
        self.request_path = self.root / "request.json"

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def request(self) -> dict:
        return {
            "schema_version": "apex.execution-request/v1",
            "execution_id": "exec-20260810-001",
            "idempotency_key": "flow-F1-step-3-attempt-1",
            "origin": {
                "repo": str(REPO_ROOT),
                "workflow": "PrecapNextDay",
                "step": "capture-research",
            },
            "instruction": "apex-flow-executor",
            "provider": "chatgpt",
            "prompt_ref": {
                "path": str(self.prompt),
                "sha256": hashlib.sha256(self.prompt.read_bytes()).hexdigest(),
            },
            "roots": [
                {"path": str(self.trusted), "mode": "read"},
                {"path": str(self.outputs), "mode": "read_write"},
            ],
            "grants": {
                "tools": ["browser", "read", "write", "exec"],
                "scripts": [
                    {
                        "id": "worker",
                        "executable": str(self.powershell),
                        "executable_sha256": hashlib.sha256(self.powershell.read_bytes()).hexdigest(),
                        "path": str(self.script),
                        "sha256": hashlib.sha256(self.script.read_bytes()).hexdigest(),
                        "argv": ["--mode", "safe"],
                    }
                ],
                "commands": [],
                "git": {
                    "repo": str(self.git_repo),
                    "remote": "origin",
                    "remote_url": "https://github.com/leela-spec/apexai-os-meta.git",
                    "branch": "main",
                    "operations": ["status", "diff"],
                    "add_paths": [],
                    "commit_message": None,
                },
            },
            "success_criteria": ["response captured verbatim"],
            "stop_conditions": ["provider hostname differs"],
            "result_path": str(self.outputs / "result.md"),
            "evidence_dir": str(self.outputs / "evidence"),
        }

    def run_validator(self, request: dict) -> subprocess.CompletedProcess[str]:
        self.request_path.write_text(json.dumps(request), encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(self.request_path)],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def assert_rejected(self, request: dict, code: str) -> None:
        result = self.run_validator(request)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertFalse(payload["valid"])
        self.assertEqual(payload["code"], code)

    def test_valid_request_emits_normalized_contract(self) -> None:
        result = self.run_validator(self.request())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["valid"])
        self.assertEqual(payload["request"]["execution_id"], "exec-20260810-001")
        self.assertTrue(Path(payload["request"]["result_path"]).is_absolute())

    def test_rejects_unknown_schema_tool_and_root_mode(self) -> None:
        request = self.request()
        request["schema_version"] = "apex.execution-request/v2"
        self.assert_rejected(request, "SCHEMA_VERSION")

        request = self.request()
        request["grants"]["tools"].append("subagents")
        self.assert_rejected(request, "UNKNOWN_TOOL")

        request = self.request()
        request["roots"][0]["mode"] = "admin"
        self.assert_rejected(request, "ROOT_MODE")

    def test_rejects_missing_success_or_stop_conditions(self) -> None:
        request = self.request()
        request["success_criteria"] = []
        self.assert_rejected(request, "SUCCESS_CRITERIA")

        request = self.request()
        request["stop_conditions"] = []
        self.assert_rejected(request, "STOP_CONDITIONS")

    def test_rejects_prompt_hash_mismatch(self) -> None:
        request = self.request()
        request["prompt_ref"]["sha256"] = "0" * 64
        self.assert_rejected(request, "PROMPT_HASH")

    def test_rejects_output_outside_read_write_root(self) -> None:
        request = self.request()
        request["result_path"] = str(self.root.parent / "escape.md")
        self.assert_rejected(request, "PATH_OUTSIDE_ROOTS")

        request = self.request()
        request["roots"][1]["mode"] = "read"
        self.assert_rejected(request, "WRITE_REQUIRES_READ_WRITE")

    def test_rejects_reparse_evidence_path(self) -> None:
        real_evidence = self.outputs / "real-evidence"
        real_evidence.mkdir()
        linked_evidence = self.outputs / "evidence-link"
        try:
            os.symlink(real_evidence, linked_evidence, target_is_directory=True)
        except OSError as exc:
            self.skipTest(f"directory symlink unavailable: {exc}")
        request = self.request()
        request["evidence_dir"] = str(linked_evidence)
        self.assert_rejected(request, "EVIDENCE_REPARSE")

    def test_rejects_script_outside_roots_and_inline_execution(self) -> None:
        request = self.request()
        request["grants"]["scripts"][0]["path"] = str(REPO_ROOT / "AGENTS.md")
        self.assert_rejected(request, "PATH_OUTSIDE_ROOTS")

        request = self.request()
        request["grants"]["scripts"][0]["argv"] = ["-c", "print('evil')"]
        self.assert_rejected(request, "INLINE_EXECUTION")

    def test_rejects_inline_or_malformed_exact_argv_command(self) -> None:
        request = self.request()
        request["grants"]["commands"] = [{
            "id": "inline",
            "executable": str(self.powershell),
            "executable_sha256": hashlib.sha256(self.powershell.read_bytes()).hexdigest(),
            "argv": ["-EncodedCommand", "AAAA"],
        }]
        self.assert_rejected(request, "COMMAND_INTERPRETER")

        request = self.request()
        request["grants"]["commands"] = [{
            "id": "bad-argv",
            "executable": str(self.powershell),
            "executable_sha256": hashlib.sha256(self.powershell.read_bytes()).hexdigest(),
            "argv": "status",
        }]
        self.assert_rejected(request, "COMMAND_ARGV")

    def test_rejects_interpreter_commands_even_with_joined_or_abbreviated_options(self) -> None:
        for option in ("--eval=payload", "-enc", "/c"):
            request = self.request()
            request["grants"]["commands"] = [{
                "id": "interpreter",
                "executable": str(self.powershell),
                "executable_sha256": hashlib.sha256(self.powershell.read_bytes()).hexdigest(),
                "argv": [option, "payload"],
            }]
            self.assert_rejected(request, "COMMAND_INTERPRETER")

    def test_rejects_renamed_or_unreviewed_command_identity(self) -> None:
        renamed = self.trusted / "reviewed-helper.exe"
        shutil.copyfile(self.powershell, renamed)
        request = self.request()
        request["grants"]["commands"] = [{
            "id": "renamed-interpreter",
            "executable": str(renamed),
            "executable_sha256": hashlib.sha256(renamed.read_bytes()).hexdigest(),
            "argv": ["anything"],
        }]
        self.assert_rejected(request, "COMMAND_IDENTITY")

    def test_rejects_mutable_script_root_and_identity_mismatch(self) -> None:
        request = self.request()
        request["roots"][0]["mode"] = "read_write"
        self.assert_rejected(request, "SCRIPT_ROOT_MODE")

        request = self.request()
        request["grants"]["scripts"][0]["sha256"] = "0" * 64
        self.assert_rejected(request, "SCRIPT_HASH")

    def test_rejects_git_authority_widening(self) -> None:
        request = self.request()
        request["grants"]["git"]["operations"].append("force-push")
        self.assert_rejected(request, "GIT_OPERATION")

        request = self.request()
        request["grants"]["git"]["branch"] = "feature"
        self.assert_rejected(request, "GIT_BRANCH")

        request = self.request()
        request["grants"]["git"]["remote_url"] = "ssh://github.com/leela-spec/apex.git"
        self.assert_rejected(request, "GIT_REMOTE")

    def test_rejects_unknown_top_level_fields(self) -> None:
        request = self.request()
        request["autonomy"] = "full"
        self.assert_rejected(request, "UNKNOWN_FIELD")


if __name__ == "__main__":
    unittest.main()
