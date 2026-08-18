"""Unit tests for semantic CLI adapter and worker lifecycle."""
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from scripts.transcript_pipeline_v2.adapters.semantic_cli import (
    ProviderUnavailableError,
    SemanticCLIWorker,
    SemanticExecutionError,
    extract_json_block,
    get_sanitized_env,
)


class TestSemanticCLI(unittest.TestCase):

    def test_get_sanitized_env_removes_api_keys(self):
        with patch.dict(os.environ, {
            "OPENAI_API_KEY": "sk-test",
            "ANTHROPIC_API_KEY": "sk-ant",
            "ANTHROPIC_AUTH_TOKEN": "tok-ant",
            "ANTHROPIC_BASE_URL": "https://api.anthropic.com",
            "GEMINI_API_KEY": "gem-test",
            "GOOGLE_API_KEY": "goog-test",
            "PATH": "some_path"
        }):
            clean_env = get_sanitized_env()
            self.assertNotIn("OPENAI_API_KEY", clean_env)
            self.assertNotIn("ANTHROPIC_API_KEY", clean_env)
            self.assertNotIn("ANTHROPIC_AUTH_TOKEN", clean_env)
            self.assertNotIn("ANTHROPIC_BASE_URL", clean_env)
            self.assertNotIn("GEMINI_API_KEY", clean_env)
            self.assertNotIn("GOOGLE_API_KEY", clean_env)
            self.assertEqual(clean_env.get("PATH"), "some_path")

    def test_extract_json_block(self):
        # Direct json
        self.assertEqual(extract_json_block('{"a": 1}'), {"a": 1})
        # Fenced markdown
        self.assertEqual(extract_json_block('Here is the json:\n```json\n{"b": 2}\n```\nDone.'), {"b": 2})
        # Unfenced mixed text
        self.assertEqual(extract_json_block('Some text before {"c": 3} some text after'), {"c": 3})
        # Invalid
        with self.assertRaises(ValueError):
            extract_json_block("No json here")

    def test_provider_unavailable_raises(self):
        with self.assertRaises(ProviderUnavailableError):
            SemanticCLIWorker(provider="nonexistent_provider")

    @patch("shutil.which")
    def test_provider_which_check(self, mock_which):
        mock_which.return_value = None
        with self.assertRaises(ProviderUnavailableError):
            SemanticCLIWorker(provider="codex")

    @patch("shutil.which", return_value="/bin/claude")
    @patch.object(SemanticCLIWorker, "invoke_raw")
    def test_mock_subprocess_success_map(self, mock_invoke, mock_which):
        worker = SemanticCLIWorker(provider="claude")
        
        valid_map_result = {
            "schema": "ttk.map-result.v2",
            "packet_id": "test-pkt",
            "packet_sha256": "pkt-sha",
            "window_id": "win-001",
            "subtopics": [{"label": "Intro", "source_segment_ids": ["seg-1"]}],
            "key_points": [{"text": "Point 1", "source_segment_ids": ["seg-1"]}],
            "mechanisms": [],
            "protocols": [],
            "arguments": [],
            "candidate_claims": [
                {
                    "claim_text": "Point 1 verbatim",
                    "claim_kind": "fact",
                    "speaker": "Speaker 1",
                    "checkworthiness": "high",
                    "source_segment_ids": ["seg-1"],
                    "quote_evidence": [{"segment_id": "seg-1", "quote": "Point 1 verbatim"}]
                }
            ],
            "entities": [{"name": "Speaker 1", "source_segment_ids": ["seg-1"]}],
            "concepts": [],
            "open_questions": [],
            "contradictions_or_uncertainty": []
        }
        
        mock_invoke.return_value = (0, json.dumps(valid_map_result), "", 1.2)
        
        packet = {
            "packet_id": "test-pkt",
            "packet_sha256": "pkt-sha",
            "window_id": "win-001",
            "core_segment_ids": ["seg-1"]
        }
        lookup = {"seg-1": {"id": "seg-1", "text": "Point 1 verbatim and more text."}}
        
        with patch("ttk_map._packet_hash_valid", return_value=True):
            with tempfile.TemporaryDirectory() as tmpdir:
                receipt_path = Path(tmpdir) / "map-receipt.json"
                result = worker.execute_map(packet, lookup, receipt_path=receipt_path)
                
                self.assertEqual(result["schema"], "ttk.map-result.v2")
                self.assertTrue(receipt_path.exists())
                with open(receipt_path, "r", encoding="utf-8") as f:
                    r = json.load(f)
                self.assertEqual(r["status"], "PASS")
                self.assertEqual(r["provider"], "claude")

    @patch("shutil.which", return_value="/bin/claude")
    @patch.object(SemanticCLIWorker, "invoke_raw")
    def test_nonzero_cli_exit_triggers_retry_and_fails(self, mock_invoke, mock_which):
        worker = SemanticCLIWorker(provider="claude")
        mock_invoke.return_value = (1, "", "Process failed", 0.5)
        
        packet = {"packet_id": "p", "packet_sha256": "s", "window_id": "w", "core_segment_ids": ["seg-1"]}
        lookup = {"seg-1": {"id": "seg-1", "text": "text"}}
        
        with tempfile.TemporaryDirectory() as tmpdir:
            receipt_path = Path(tmpdir) / "map-receipt.json"
            with self.assertRaises(SemanticExecutionError):
                worker.execute_map(packet, lookup, receipt_path=receipt_path, max_retries=1)
            
            self.assertTrue(receipt_path.exists())
            with open(receipt_path, "r", encoding="utf-8") as f:
                r = json.load(f)
            self.assertEqual(r["status"], "FAIL")
            self.assertEqual(r["attempts"], 2)


if __name__ == "__main__":
    unittest.main()
