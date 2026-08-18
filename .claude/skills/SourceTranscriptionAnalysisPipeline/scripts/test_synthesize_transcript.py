"""
test_synthesize_transcript.py
Unit and validation test suite for Pipeline 1 synthesize_transcript.py
"""
import unittest
import tempfile
import json
import subprocess
import sys
from pathlib import Path

# Add scripts directory to path
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from synthesize_transcript import (
    validate_and_load_semantic_result,
    parse_transcript_spoken_text,
    ValidationError,
    KnowledgeSynthesisEngine,
    normalize_text
)

SAMPLE_SRT = """1
00:00:01,000 --> 00:00:04,500
Hello and welcome to the deep dive on machine learning.

2
00:00:05,000 --> 00:00:09,200
Today we are going to explore neural network architectures and backpropagation algorithms.
"""

VALID_SEMANTIC_DATA = {
    "macro": {
        "core_thesis": "Neural networks learn through gradient descent and backpropagation.",
        "global_takeaways": [
            "Backpropagation computes error gradients efficiently across layers."
        ],
        "taxonomy_tags": ["Machine Learning", "Neural Networks"],
        "speakers": [
            {"label": "Host", "name": "Professor", "credentials": "AI Researcher"}
        ]
    },
    "meso": [
        {
            "title": "Neural Network Fundamentals",
            "start_ts": "00:00:01",
            "end_ts": "00:00:09",
            "arguments": ["Backpropagation updates weights via chain rule."],
            "protocol_steps": ["Initialize weights", "Compute forward pass", "Apply backprop"],
            "caveats": ["Requires differentiable activation functions."]
        }
    ],
    "micro": [
        {
            "claim_id": "1",
            "proposition": "The presentation explores neural network architectures and backpropagation algorithms.",
            "quote": "Today we are going to explore neural network architectures and backpropagation algorithms.",
            "timestamp": "00:00:05",
            "claim_type": "FACT",
            "internal_confidence": "peer-reviewed",
            "source_support": "SUPPORTED",
            "verdict": "UNVERIFIED"
        }
    ]
}


class TestSynthesizeTranscript(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.dir_path = Path(self.temp_dir.name)
        self.srt_path = self.dir_path / "test.srt"
        self.srt_path.write_text(SAMPLE_SRT, encoding="utf-8")
        self.spoken_text = parse_transcript_spoken_text(self.srt_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_no_hardcoded_huberman_in_script_source(self):
        script_text = (SCRIPT_DIR / "synthesize_transcript.py").read_text(encoding="utf-8")
        self.assertNotIn("Huberman", script_text)
        self.assertNotIn("Adolphs", script_text)
        self.assertNotIn("ice bath", script_text)

    def test_valid_semantic_result_passes_grounding(self):
        sem_path = self.dir_path / "valid_semantic.json"
        sem_path.write_text(json.dumps(VALID_SEMANTIC_DATA), encoding="utf-8")
        
        engine = validate_and_load_semantic_result(sem_path, self.spoken_text, title="Test Synthesis")
        self.assertEqual(len(engine.micro_claims), 1)
        self.assertEqual(engine.micro_claims[0].claim_id, "1")
        self.assertEqual(engine.get_external_verification_status(), "NOT_RUN")
        
        md_file, json_file = engine.write_artifacts(self.dir_path, "test_slug")
        self.assertTrue(md_file.exists())
        self.assertTrue(json_file.exists())
        self.assertIn("Quote Grounding:** VALIDATED", md_file.read_text(encoding="utf-8"))

    def test_search_urls_alone_leave_external_verification_not_run(self):
        data_with_urls = dict(VALID_SEMANTIC_DATA)
        data_with_urls["micro"] = [{
            "claim_id": "1",
            "proposition": "The presentation explores neural network architectures and backpropagation algorithms.",
            "quote": "Today we are going to explore neural network architectures and backpropagation algorithms.",
            "timestamp": "00:00:05",
            "claim_type": "FACT",
            "verdict": "UNVERIFIED",
            "external_sources": ["https://example.com/paper1", "https://example.com/paper2"]
        }]
        sem_path = self.dir_path / "url_semantic.json"
        sem_path.write_text(json.dumps(data_with_urls), encoding="utf-8")
        
        engine = validate_and_load_semantic_result(sem_path, self.spoken_text, title="Test Synthesis")
        # Crucial bugfix check: URLs present, but verdict is UNVERIFIED -> status MUST be NOT_RUN
        self.assertEqual(engine.get_external_verification_status(), "NOT_RUN")

    def test_invented_quote_fails_validation(self):
        corrupt_data = dict(VALID_SEMANTIC_DATA)
        corrupt_data["micro"] = [{
            "claim_id": "1",
            "proposition": "Completely made up claim",
            "quote": "This sentence was never spoken in the video transcript at all.",
            "timestamp": "00:00:05",
            "claim_type": "FACT",
            "verdict": "UNVERIFIED"
        }]
        sem_path = self.dir_path / "corrupt_semantic.json"
        sem_path.write_text(json.dumps(corrupt_data), encoding="utf-8")
        
        with self.assertRaises(ValidationError) as ctx:
            validate_and_load_semantic_result(sem_path, self.spoken_text, title="Test")
        self.assertIn("NOT present verbatim", str(ctx.exception))

    def test_srt_metadata_in_quote_fails_validation(self):
        corrupt_data = dict(VALID_SEMANTIC_DATA)
        corrupt_data["micro"] = [{
            "claim_id": "1",
            "proposition": "SRT contaminated quote",
            "quote": "00:00:01,000 --> 00:00:04,500 Hello and welcome",
            "timestamp": "00:00:01",
            "claim_type": "FACT",
            "verdict": "UNVERIFIED"
        }]
        sem_path = self.dir_path / "srt_corrupt_semantic.json"
        sem_path.write_text(json.dumps(corrupt_data), encoding="utf-8")
        
        with self.assertRaises(ValidationError) as ctx:
            validate_and_load_semantic_result(sem_path, self.spoken_text, title="Test")
        self.assertIn("raw SRT formatting metadata", str(ctx.exception))

    def test_cli_missing_semantic_result_exits_code_2(self):
        cmd = [
            sys.executable,
            str(SCRIPT_DIR / "synthesize_transcript.py"),
            "--transcript", str(self.srt_path),
            "--output_dir", str(self.dir_path)
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(res.returncode, 2)
        self.assertIn("SYNTHESIS_PENDING", res.stderr)
        # Ensure no fake wiki was created
        self.assertFalse((self.dir_path / "test_knowledge_wiki.md").exists())


if __name__ == "__main__":
    unittest.main()
