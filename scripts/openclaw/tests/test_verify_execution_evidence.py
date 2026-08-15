from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
VERIFIER = REPO_ROOT / "scripts" / "openclaw" / "verify-execution-evidence.py"


class ExecutionEvidenceVerifierTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name).resolve()
        self.prompt = self.root / "frozen-prompt.md"
        self.result = self.root / "result.md"
        self.request_path = self.root / "normalized-request.json"
        self.receipt_path = self.root / "executor-receipt.json"
        self.raw_result_path = self.root / "openclaw-result.json"
        self.dispatch_state_path = self.root.parent / f"dispatch-{self.root.name}.json"
        self.verified_path = self.root / "verified-receipt.json"
        self.prompt.write_bytes(b"exact prompt\n")
        self.result.write_text("captured answer", encoding="utf-8")
        prompt_hash = hashlib.sha256(self.prompt.read_bytes()).hexdigest()
        self.request = {
            "execution_id": "exec-test-001",
            "provider": "chatgpt",
            "provider_settings": {
                "browser_profile": "openclaw",
                "hostname": "chatgpt.com",
                "mode": "standard",
                "model": "default",
                "reasoning_mode": "off",
                "session_policy": "new_conversation",
            },
            "prompt_ref": {"path": str(self.prompt), "sha256": prompt_hash},
            "result_path": str(self.result),
            "evidence_dir": str(self.root),
        }
        self.receipt = {
            "schema_version": "apex.executor-receipt/v1",
            "execution_id": "exec-test-001",
            "status": "completed",
            "provider": "chatgpt",
            "browser_profile": "openclaw",
            "hostname": "chatgpt.com",
            "mode": "standard",
            "web_model": "default",
            "reasoning_mode": "off",
            "session_policy": "new_conversation",
            "conversation_url": "https://chatgpt.com/c/example",
            "prompt_sha256": prompt_hash,
            "prompt_body_bytes_submitted": len(self.prompt.read_bytes()),
            "captured_characters": len(self.result.read_text(encoding="utf-8")),
            "result_path": str(self.result),
            "near_page_cap": False,
            "reload_performed": False,
            "instruction_shaped_content_observed": False,
            "notes": [],
        }
        calls = [
            ("tabs", {"action": "tabs"}),
            ("snapshot-before", {"action": "snapshot", "targetId": "t1"}),
            (
                "type",
                {
                    "action": "act",
                    "targetId": "t1",
                    "request": {"kind": "type", "ref": "e1", "text": self.prompt.read_text(encoding="utf-8")},
                },
            ),
            (
                "submit",
                {"action": "act", "targetId": "t1", "request": {"kind": "press", "key": "Enter"}},
            ),
            ("snapshot-result", {"action": "snapshot", "targetId": "t1"}),
        ]
        transcript = []
        parent = None
        for call_id, arguments in calls:
            message_id = f"message-{call_id}"
            transcript.append({
                "type": "message",
                "id": message_id,
                "parentId": parent,
                "message": {
                    "role": "assistant",
                    "content": [{"type": "toolCall", "id": call_id, "name": "browser", "arguments": arguments}],
                },
            })
            result_text = (
                "captured answer"
                if call_id == "snapshot-result"
                else "https://chatgpt.com/c/example"
            )
            result_id = f"result-{call_id}"
            transcript.append({
                "type": "message",
                "id": result_id,
                "parentId": message_id,
                "message": {
                    "role": "toolResult",
                    "toolCallId": call_id,
                    "toolName": "browser",
                    "content": [{"type": "text", "text": result_text}],
                    "isError": False,
                },
            })
            parent = result_id
        self.session_path = self.root.parent / f"session-{self.root.name}.jsonl"
        self.session_path.write_text("\n".join(json.dumps(item) for item in transcript) + "\n", encoding="utf-8")
        self.raw_result = {
            "runId": "run-test-001",
            "status": "ok",
            "summary": "completed",
            "result": {
                "meta": {
                    "agentMeta": {
                        "sessionFile": str(self.session_path),
                        "provider": "openai",
                        "model": "gpt-4.1-nano",
                    }
                }
            },
        }

    def tearDown(self) -> None:
        self.session_path.unlink(missing_ok=True)
        self.dispatch_state_path.unlink(missing_ok=True)
        self.tempdir.cleanup()

    def verify(self, *, executor_model: str = "openai/gpt-4.1-nano") -> subprocess.CompletedProcess[str]:
        self.request_path.write_text(json.dumps(self.request), encoding="utf-8")
        self.receipt_path.write_text(json.dumps(self.receipt), encoding="utf-8")
        self.raw_result_path.write_text(json.dumps(self.raw_result), encoding="utf-8")
        return subprocess.run(
            [
                sys.executable,
                str(VERIFIER),
                str(self.request_path),
                str(self.receipt_path),
                str(self.raw_result_path),
                executor_model,
                str(self.dispatch_state_path),
                str(self.verified_path),
            ],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_writes_verified_receipt_with_deterministic_result_hash(self) -> None:
        result = self.verify()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        verified = json.loads(self.verified_path.read_text(encoding="utf-8"))
        self.assertEqual(verified["schema_version"], "apex.verified-executor-receipt/v1")
        self.assertEqual(verified["status"], "completed")
        self.assertEqual(verified["executor_model"], "openai/gpt-4.1-nano")
        self.assertEqual(verified["prompt_sha256"], self.request["prompt_ref"]["sha256"])
        self.assertEqual(verified["result_sha256"], hashlib.sha256(self.result.read_bytes()).hexdigest())
        self.assertEqual(verified["source_receipt_sha256"], hashlib.sha256(self.receipt_path.read_bytes()).hexdigest())
        self.assertEqual(verified["raw_result_sha256"], hashlib.sha256(self.raw_result_path.read_bytes()).hexdigest())
        self.assertEqual(verified["dispatch_state_file"], str(self.dispatch_state_path))
        self.assertEqual(verified["browser_submission_count"], 1)

    def test_rejects_blocked_receipt_or_missing_result(self) -> None:
        self.receipt["status"] = "blocked"
        blocked = self.verify()
        self.assertNotEqual(blocked.returncode, 0)
        self.assertIn("RECEIPT_STATUS", blocked.stderr)
        self.receipt["status"] = "completed"
        self.result.unlink()
        missing = self.verify()
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("RESULT_MISSING", missing.stderr)

    def test_rejects_setting_count_url_or_prompt_mismatch(self) -> None:
        cases = [
            ("web_model", "wrong", "RECEIPT_SETTINGS"),
            ("captured_characters", 999, "RESULT_CHARACTERS"),
            ("conversation_url", "https://example.com/", "CONVERSATION_HOSTNAME"),
            ("prompt_sha256", "0" * 64, "PROMPT_HASH"),
        ]
        for field, value, code in cases:
            with self.subTest(field=field):
                original = self.receipt[field]
                self.receipt[field] = value
                result = self.verify()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(code, result.stderr)
                self.receipt[field] = original

    def test_rejects_fabricated_capture_without_browser_origin(self) -> None:
        transcript = [json.loads(line) for line in self.session_path.read_text(encoding="utf-8").splitlines()]
        transcript[-1]["message"]["content"][0]["text"] = "https://chatgpt.com/c/example\na different answer"
        self.session_path.write_text("\n".join(json.dumps(item) for item in transcript) + "\n", encoding="utf-8")
        result = self.verify()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("RESULT_NOT_BROWSER_ORIGIN", result.stderr)

    def test_rejects_missing_exact_browser_submission_or_duplicate_submit(self) -> None:
        transcript = [json.loads(line) for line in self.session_path.read_text(encoding="utf-8").splitlines()]
        type_call = next(
            item for item in transcript
            if item.get("message", {}).get("role") == "assistant"
            and any(content.get("id") == "type" for content in item["message"].get("content", []))
        )
        type_call["message"]["content"][0]["arguments"]["request"]["text"] = "fabricated prompt"
        self.session_path.write_text("\n".join(json.dumps(item) for item in transcript) + "\n", encoding="utf-8")
        wrong = self.verify()
        self.assertNotEqual(wrong.returncode, 0)
        self.assertIn("BROWSER_PROMPT", wrong.stderr)

        type_call["message"]["content"][0]["arguments"]["request"]["text"] = self.prompt.read_text(encoding="utf-8")
        submit = next(
            item for item in transcript
            if item.get("message", {}).get("role") == "assistant"
            and any(content.get("id") == "submit" for content in item["message"].get("content", []))
        )
        duplicate = json.loads(json.dumps(submit))
        duplicate["id"] = "message-submit-duplicate"
        duplicate["message"]["content"][0]["id"] = "submit-duplicate"
        transcript.append(duplicate)
        self.session_path.write_text("\n".join(json.dumps(item) for item in transcript) + "\n", encoding="utf-8")
        repeated = self.verify()
        self.assertNotEqual(repeated.returncode, 0)
        self.assertIn("BROWSER_SUBMISSION_COUNT", repeated.stderr)


if __name__ == "__main__":
    unittest.main()
