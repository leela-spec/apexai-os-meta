"""Unit tests for resumable TTK lifecycle execution."""
import json
import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
TTK_SCRIPTS = REPO_ROOT / ".claude" / "skills" / "transcript-to-knowledge" / "scripts"
import sys
sys.path.insert(0, str(TTK_SCRIPTS))
sys.path.insert(0, str(REPO_ROOT / "scripts" / "transcript_pipeline_v2"))

import execute_ttk_lifecycle
import ttk


class TestResumableRunner(unittest.TestCase):

    @patch("adapters.semantic_cli.SemanticCLIWorker.invoke_raw")
    @patch("shutil.which", return_value="/bin/claude")
    def test_clean_room_resume_and_idempotency(self, mock_which, mock_invoke):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            source_file = tmp / "test_source.json"
            source_file.write_text(json.dumps({
                "segments": [
                    {"start": 0.0, "end": 10.0, "text": "First concept discussion in detail.", "speaker": "Alice"},
                    {"start": 10.0, "end": 20.0, "text": "Second concept and conclusion.", "speaker": "Bob"}
                ]
            }), encoding="utf-8")
            
            output_dir = tmp / "run_test"
            
            def mock_invoke_fn(prompt):
                # Extract packet from prompt (last json block)
                matches = re.findall(r"```json\s*(\{.*?\})\s*```", prompt, re.DOTALL)
                pkt = json.loads(matches[-1]) if matches else {}
                
                if "map" in pkt.get("schema", "").lower() or "source_segments" in pkt:
                    core_ids = [s["id"] for s in pkt.get("source_segments", []) if s.get("role") == "core"]
                    if not core_ids:
                        core_ids = [s["id"] for s in pkt.get("source_segments", [])]
                    first_id = core_ids[0] if core_ids else "seg-000001"
                    first_text = next((s["text"] for s in pkt.get("source_segments", []) if s["id"] == first_id), "First concept discussion in detail.")
                    
                    res = {
                        "schema": ttk.MAP_RESULT_SCHEMA,
                        "packet_id": pkt.get("packet_id"),
                        "packet_sha256": pkt.get("packet_sha256"),
                        "window_id": pkt.get("window_id"),
                        "subtopics": [{"label": "Concept", "source_segment_ids": core_ids}],
                        "key_points": [{"text": first_text, "source_segment_ids": [first_id]}],
                        "mechanisms": [],
                        "protocols": [],
                        "arguments": [],
                        "candidate_claims": [{
                            "claim_text": first_text,
                            "claim_kind": "fact",
                            "speaker": "Alice",
                            "checkworthiness": "medium",
                            "source_segment_ids": [first_id],
                            "quote_evidence": [{"segment_id": first_id, "quote": first_text}]
                        }],
                        "entities": [],
                        "concepts": [],
                        "open_questions": [],
                        "contradictions_or_uncertainty": []
                    }
                    return (0, json.dumps(res), "", 0.1)
                else:  # reduce
                    first_id = "seg-000001"
                    first_text = "First concept discussion in detail."
                    res = {
                        "schema": ttk.REDUCE_RESULT_SCHEMA,
                        "packet_id": pkt.get("packet_id"),
                        "packet_sha256": pkt.get("packet_sha256"),
                        "macro": {
                            "thesis": "Comprehensive thesis on concept.",
                            "summary": "Summary of concepts.",
                            "takeaways": [{"text": "First takeaway.", "source_segment_ids": [first_id], "meso_refs": ["meso-001"]}],
                            "taxonomy": ["Test"],
                            "speaker_context": ["Alice and Bob"],
                            "contradictions_or_uncertainty": []
                        },
                        "meso": [{
                            "meso_ref": "meso-001",
                            "title": "Module 1",
                            "summary": "Summary 1",
                            "source_segment_ids": [first_id],
                            "concepts": [],
                            "entities": [],
                            "mechanisms": [],
                            "protocols": [],
                            "arguments": [],
                            "caveats": [],
                            "claim_refs": ["micro-001"]
                        }],
                        "micro": [{
                            "claim_ref": "micro-001",
                            "claim_text": first_text,
                            "claim_kind": "fact",
                            "source_support": "SUPPORTED",
                            "checkworthiness": "medium",
                            "source_segment_ids": [first_id],
                            "quote_evidence": [{"segment_id": first_id, "quote": first_text}],
                            "topics": ["Test"],
                            "entities": []
                        }],
                        "rejected_or_unresolved_candidates": []
                    }
                    return (0, json.dumps(res), "", 0.1)

            mock_invoke.side_effect = mock_invoke_fn
            
            with patch("ttk_map._packet_hash_valid", return_value=True), \
                 patch("ttk_verify._packet_hash_valid", return_value=True):
                
                # First run: Map and Reduce are called
                res1 = execute_ttk_lifecycle.execute_full_ttk_run(source_file, output_dir, provider="claude")
                self.assertEqual(res1["status"], "PASS")
                first_call_count = mock_invoke.call_count
                self.assertGreater(first_call_count, 0)
                
                # Second run with no changes: zero additional invocations
                res2 = execute_ttk_lifecycle.execute_full_ttk_run(source_file, output_dir, provider="claude")
                self.assertEqual(res2["status"], "PASS")
                self.assertEqual(mock_invoke.call_count, first_call_count)


if __name__ == "__main__":
    unittest.main()
