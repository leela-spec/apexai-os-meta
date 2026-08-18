"""Unit tests for LangExtract adapter."""
import unittest
from scripts.transcript_pipeline_v2.adapters.langextract_map import LangExtractMapAdapter


class TestLangExtractAdapter(unittest.TestCase):

    def test_extract_map_result(self):
        adapter = LangExtractMapAdapter()
        packet = {
            "packet_id": "pkt-01",
            "packet_sha256": "sha-01",
            "window_id": "win-001",
            "source_segments": [
                {
                    "id": "seg-01",
                    "role": "core",
                    "text": "The amygdala processes fear signals rapidly and projects to autonomic nuclei."
                }
            ]
        }
        lookup = {"seg-01": {"id": "seg-01", "text": packet["source_segments"][0]["text"]}}
        result = adapter.extract_map_result(packet, lookup)
        
        self.assertEqual(result["schema"], "ttk.map-result.v2")
        self.assertEqual(result["packet_id"], "pkt-01")
        self.assertTrue(len(result["candidate_claims"]) > 0)
        self.assertEqual(result["candidate_claims"][0]["quote_evidence"][0]["segment_id"], "seg-01")


if __name__ == "__main__":
    unittest.main()
