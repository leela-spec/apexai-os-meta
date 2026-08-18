"""Unit tests for AgentSemanticEngine and agent semantic worker."""
import json
import tempfile
import unittest
from pathlib import Path

from scripts.transcript_pipeline_v2.adapters.agent_semantic_engine import AgentSemanticEngine
from scripts.transcript_pipeline_v2.adapters.semantic_cli import SemanticCLIWorker
import ttk
import ttk_map
import ttk_verify


class TestAgentSemanticEngine(unittest.TestCase):

    def setUp(self):
        self.packet = {
            "schema": "ttk.map-packet.v2",
            "packet_id": "test-pkt-001",
            "packet_sha256": "sha256-test",
            "window_id": "window-0001",
            "core_segment_ids": ["seg-000001", "seg-000002"],
            "source_segments": [
                {
                    "id": "seg-000001",
                    "start": 0.0,
                    "end": 10.0,
                    "text": "The amygdala coordinates physiological arousal and threat responses in mammalian brains.",
                    "speaker": "Dr. Adolphs",
                    "role": "core"
                },
                {
                    "id": "seg-000002",
                    "start": 10.0,
                    "end": 20.0,
                    "text": "Emotions evolved to adaptively coordinate behavior across diverse ecological environments.",
                    "speaker": "Dr. Huberman",
                    "role": "core"
                }
            ]
        }
        self.lookup = {
            "seg-000001": self.packet["source_segments"][0],
            "seg-000002": self.packet["source_segments"][1]
        }

    def test_map_extraction_valid(self):
        result = AgentSemanticEngine.process_map_packet(self.packet, self.lookup)
        self.assertEqual(result["schema"], ttk.MAP_RESULT_SCHEMA)
        self.assertEqual(result["window_id"], "window-0001")
        
        errors = ttk_map.validate_map_result(self.packet, result, self.lookup)
        # Note: _packet_hash_valid checks internally, but the structural errors should be 0
        structural_errors = [e for e in errors if "map packet hash is internally invalid" not in e]
        self.assertEqual(structural_errors, [])
        self.assertGreater(len(result["subtopics"]), 0)
        self.assertGreater(len(result["candidate_claims"]), 0)

    def test_worker_agent_execution(self):
        worker = SemanticCLIWorker(provider="antigravity_agent")
        with tempfile.TemporaryDirectory() as tmpdir:
            receipt_path = Path(tmpdir) / "receipt.json"
            
            # Monkeypatch _packet_hash_valid for unit test
            import unittest.mock as mock
            with mock.patch("ttk_map._packet_hash_valid", return_value=True):
                result = worker.execute_map(self.packet, self.lookup, receipt_path=receipt_path)
                self.assertEqual(result["schema"], ttk.MAP_RESULT_SCHEMA)
                self.assertTrue(receipt_path.exists())
                with open(receipt_path, "r", encoding="utf-8") as f:
                    r = json.load(f)
                self.assertEqual(r["status"], "PASS")
                self.assertEqual(r["provider"], "antigravity_agent")
                self.assertEqual(r["transport"], "agent_worker")


if __name__ == "__main__":
    unittest.main()
