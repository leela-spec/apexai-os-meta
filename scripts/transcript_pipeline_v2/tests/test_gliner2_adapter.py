"""Unit tests for GLiNER2 pre-extraction adapter."""
import unittest
from scripts.transcript_pipeline_v2.adapters.gliner2_preextract import GLiNER2PreExtractor


class TestGLiNER2Adapter(unittest.TestCase):

    def test_extract_hints_en_and_de(self):
        extractor = GLiNER2PreExtractor()
        
        # English packet
        en_packet = {
            "packet_id": "pkt-en",
            "window_id": "win-001",
            "source_segments": [
                {
                    "id": "seg-001",
                    "role": "core",
                    "text": "Dr. Ralph Adolphs at Caltech discussed the amygdala and fear circuitry."
                }
            ]
        }
        en_hints = extractor.extract_hints(en_packet)
        self.assertEqual(en_hints["schema"], "ttk.preextract-hints.v2")
        names = [e["name"] for e in en_hints["entity_hints"]]
        self.assertTrue(any("Ralph Adolphs" in n or "Caltech" in n for n in names))
        
        # German packet
        de_packet = {
            "packet_id": "pkt-de",
            "window_id": "win-002",
            "source_segments": [
                {
                    "id": "seg-002",
                    "role": "core",
                    "text": "Markus Koch berichtet über den Nasdaq und die Wall Street."
                }
            ]
        }
        de_hints = extractor.extract_hints(de_packet)
        de_names = [e["name"] for e in de_hints["entity_hints"]]
        self.assertTrue(any("Markus Koch" in n or "Nasdaq" in n or "Wall Street" in n for n in de_names))


if __name__ == "__main__":
    unittest.main()
