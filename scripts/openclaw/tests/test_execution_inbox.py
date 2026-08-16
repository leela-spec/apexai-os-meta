from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
POWERSHELL = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
PROCESSOR = REPO_ROOT / "scripts" / "openclaw" / "process_execution_inbox.py"


class ExecutionInboxTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name).resolve()
        self.queue = self.root / "queue"
        self.inbox = self.queue / "inbox"
        self.processing = self.queue / "processing"
        self.completed = self.queue / "completed"
        self.failed = self.queue / "failed"
        self.inbox.mkdir(parents=True)
        self.counter = self.root / "dispatch-count.txt"
        self.dispatcher = self.root / "fake-dispatcher.ps1"
        self.dispatcher.write_text(
            "[CmdletBinding()]\n"
            "param([string]$RequestPath, [string]$ExecutorModel)\n"
            "$request = Get-Content -Raw -LiteralPath $RequestPath | ConvertFrom-Json\n"
            "$countPath = $env:APEX_TEST_DISPATCH_COUNT\n"
            "$count = if (Test-Path -LiteralPath $countPath) { [int](Get-Content -Raw -LiteralPath $countPath) } else { 0 }\n"
            "Set-Content -LiteralPath $countPath -Value ($count + 1) -NoNewline\n"
            "if ([int]$request.delay_ms -gt 0) { Start-Sleep -Milliseconds ([int]$request.delay_ms) }\n"
            "if ([int]$request.exit_code -ne 0) {\n"
            "  [Console]::Error.WriteLine('simulated dispatcher failure')\n"
            "  exit ([int]$request.exit_code)\n"
            "}\n"
            "if ([bool]$request.invalid_output) { Write-Output 'not-json'; exit 0 }\n"
            "[ordered]@{ status = 'completed'; execution_id = [string]$request.execution_id; duplicate = $false } | ConvertTo-Json -Compress\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def write_request(
        self,
        name: str,
        *,
        directory: Path | None = None,
        exit_code: int = 0,
        delay_ms: int = 0,
        invalid_output: bool = False,
    ) -> tuple[Path, bytes]:
        target_dir = directory or self.inbox
        target_dir.mkdir(parents=True, exist_ok=True)
        path = target_dir / name
        payload = {
            "execution_id": name.removesuffix(".request.json"),
            "exit_code": exit_code,
            "delay_ms": delay_ms,
            "invalid_output": invalid_output,
        }
        path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")
        return path, path.read_bytes()

    def run_processor(self, *, max_requests: int = 10) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment["APEX_TEST_DISPATCH_COUNT"] = str(self.counter)
        environment["PSModulePath"] = ""
        return subprocess.run(
            [
                sys.executable,
                str(PROCESSOR),
                "--queue-root",
                str(self.queue),
                "--dispatcher-path",
                str(self.dispatcher),
                "--max-requests",
                str(max_requests),
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
            env=environment,
        )

    def test_success_atomically_claims_request_and_writes_terminal_receipt(self) -> None:
        source, original = self.write_request("001.request.json")

        result = self.run_processor()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        summary = json.loads(result.stdout)
        self.assertEqual(summary, {"status": "ok", "claimed": 1, "completed": 1, "failed": 0})
        self.assertFalse(source.exists())
        terminal_request = self.completed / source.name
        self.assertEqual(terminal_request.read_bytes(), original)
        receipt = json.loads((self.completed / "001.receipt.json").read_text(encoding="utf-8"))
        self.assertEqual(receipt["schema_version"], "apex.execution-inbox-receipt/v1")
        self.assertEqual(receipt["status"], "completed")
        self.assertEqual(receipt["request_sha256"], hashlib.sha256(original).hexdigest())
        self.assertEqual(receipt["dispatcher_exit_code"], 0)
        self.assertEqual(receipt["dispatcher_payload"]["execution_id"], "001")
        self.assertEqual(self.counter.read_text(encoding="utf-8"), "1")

    def test_dispatch_failure_is_quarantined_without_failing_the_cron_tick(self) -> None:
        source, original = self.write_request("bad.request.json", exit_code=2)

        result = self.run_processor()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)["failed"], 1)
        self.assertFalse(source.exists())
        self.assertEqual((self.failed / source.name).read_bytes(), original)
        receipt = json.loads((self.failed / "bad.receipt.json").read_text(encoding="utf-8"))
        self.assertEqual(receipt["status"], "failed")
        self.assertEqual(receipt["dispatcher_exit_code"], 2)
        self.assertIn("simulated dispatcher failure", receipt["dispatcher_stderr"])

    def test_zero_exit_with_non_json_output_is_quarantined(self) -> None:
        self.write_request("invalid-output.request.json", invalid_output=True)

        result = self.run_processor()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        receipt = json.loads((self.failed / "invalid-output.receipt.json").read_text(encoding="utf-8"))
        self.assertEqual(receipt["status"], "failed")
        self.assertEqual(receipt["error_code"], "DISPATCH_OUTPUT_INVALID")
        self.assertEqual(self.counter.read_text(encoding="utf-8"), "1")

    def test_partial_files_are_ignored_and_max_requests_is_deterministic(self) -> None:
        partial = self.inbox / "000.request.json.tmp"
        partial.write_text("partial", encoding="utf-8")
        self.write_request("002.request.json")
        self.write_request("001.request.json")

        first = self.run_processor(max_requests=1)

        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        self.assertTrue(partial.exists())
        self.assertTrue((self.completed / "001.request.json").exists())
        self.assertTrue((self.inbox / "002.request.json").exists())
        self.assertEqual(self.counter.read_text(encoding="utf-8"), "1")

        second = self.run_processor(max_requests=1)
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        self.assertTrue((self.completed / "002.request.json").exists())
        self.assertEqual(self.counter.read_text(encoding="utf-8"), "2")

    def test_processing_file_is_reconciled_before_a_new_inbox_request(self) -> None:
        self.write_request("001.request.json", directory=self.processing)
        self.write_request("002.request.json")

        result = self.run_processor(max_requests=1)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((self.completed / "001.request.json").exists())
        self.assertTrue((self.inbox / "002.request.json").exists())
        self.assertEqual(self.counter.read_text(encoding="utf-8"), "1")

    def test_overlapping_ticks_dispatch_one_claim_once(self) -> None:
        self.write_request("slow.request.json", delay_ms=750)
        environment = os.environ.copy()
        environment["APEX_TEST_DISPATCH_COUNT"] = str(self.counter)
        environment["PSModulePath"] = ""
        command = [
            sys.executable,
            str(PROCESSOR),
            "--queue-root",
            str(self.queue),
            "--dispatcher-path",
            str(self.dispatcher),
            "--max-requests",
            "1",
        ]

        first = subprocess.Popen(
            command, cwd=REPO_ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=environment
        )
        time.sleep(0.15)
        second = subprocess.run(
            command, cwd=REPO_ROOT, text=True, capture_output=True, check=False, env=environment
        )
        first_stdout, first_stderr = first.communicate(timeout=20)

        self.assertEqual(first.returncode, 0, first_stdout + first_stderr)
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        summaries = [json.loads(first_stdout), json.loads(second.stdout)]
        self.assertEqual(sorted(item["status"] for item in summaries), ["busy", "ok"])
        self.assertEqual(self.counter.read_text(encoding="utf-8"), "1")
        self.assertTrue((self.completed / "slow.request.json").exists())


if __name__ == "__main__":
    unittest.main()
