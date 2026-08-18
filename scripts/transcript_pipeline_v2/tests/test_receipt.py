"""Unit tests for V2 receipt logging helper."""
import json
import tempfile
import unittest
from pathlib import Path

from scripts.transcript_pipeline_v2.receipt import (
    ExecutionReceipt,
    sanitize_no_secrets,
    write_atomic_receipt,
)


class TestReceipt(unittest.TestCase):

    def test_sanitize_redacts_api_keys(self):
        dirty = {
            "api_key": "sk-secret-12345",
            "openai_api_key": "sk-proj-9999",
            "nested": {
                "anthropic_api_key": "secret",
                "safe_param": "valid_value"
            },
            "token_list": [
                {"token": "xyz", "name": "test"}
            ]
        }
        clean = sanitize_no_secrets(dirty)
        self.assertEqual(clean["api_key"], "[REDACTED_SECRET]")
        self.assertEqual(clean["openai_api_key"], "[REDACTED_SECRET]")
        self.assertEqual(clean["nested"]["anthropic_api_key"], "[REDACTED_SECRET]")
        self.assertEqual(clean["nested"]["safe_param"], "valid_value")
        self.assertEqual(clean["token_list"][0]["token"], "[REDACTED_SECRET]")

    def test_atomic_receipt_lifecycle(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            receipt_path = Path(tmpdir) / "test-receipt.json"
            receipt = ExecutionReceipt(receipt_path, task_id="P1", config={"test_mode": True})
            
            self.assertEqual(receipt.status, "IN_PROGRESS")
            self.assertTrue(receipt.started_at)
            
            data = receipt.complete(
                exit_code=0,
                input_hash="hash-in-123",
                output_hash="hash-out-456",
                status="PASS",
                records_processed=42
            )
            
            self.assertTrue(receipt_path.exists())
            with open(receipt_path, "r", encoding="utf-8") as f:
                on_disk = json.load(f)
                
            self.assertEqual(on_disk["task_id"], "P1")
            self.assertEqual(on_disk["status"], "PASS")
            self.assertEqual(on_disk["exit_code"], 0)
            self.assertEqual(on_disk["input_hash"], "hash-in-123")
            self.assertEqual(on_disk["output_hash"], "hash-out-456")
            self.assertEqual(on_disk["records_processed"], 42)
            self.assertGreaterEqual(on_disk["wall_time_seconds"], 0.0)


if __name__ == "__main__":
    unittest.main()
