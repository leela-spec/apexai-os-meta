"""
Anti-synthetic evidence closure unit tests.
Verifies that fake scorecards, missing receipts, missing evidence_refs,
and simulated/mocked artifacts cannot produce a PASS.
"""
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

import yaml

from scripts.transcript_pipeline_v2.eval.verify_evidence_closure import EvidenceClosureValidator


class TestEvidenceClosure(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp(prefix="ttk_evidence_test_"))
        self.scorecards_dir = self.test_dir / "scorecards"
        self.raw_dir = self.test_dir / "raw"
        self.receipts_dir = self.test_dir / "receipts"
        self.scorecards_dir.mkdir(parents=True, exist_ok=True)
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.receipts_dir.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_scorecard_with_numeric_metric_without_evidence_refs_fails(self):
        fake_scorecard = self.scorecards_dir / "map-scorecard.yaml"
        with open(fake_scorecard, "w", encoding="utf-8") as f:
            yaml.dump({
                "schema": "test-scorecard.v1",
                "insight_recall": {
                    "value": 0.95  # Missing evidence_refs!
                }
            }, f)

        validator = EvidenceClosureValidator(self.test_dir)
        passed = validator.validate_closure()
        self.assertFalse(passed)
        self.assertTrue(any("without 'evidence_refs'" in err for err in validator.errors))

    def test_scorecard_with_missing_evidence_file_fails(self):
        fake_scorecard = self.scorecards_dir / "map-scorecard.yaml"
        with open(fake_scorecard, "w", encoding="utf-8") as f:
            yaml.dump({
                "schema": "test-scorecard.v1",
                "insight_recall": {
                    "value": 0.95,
                    "evidence_refs": ["artifacts/transcript_pipeline_v2/corrective-run/raw/nonexistent_raw.json"]
                }
            }, f)

        validator = EvidenceClosureValidator(self.test_dir)
        passed = validator.validate_closure()
        self.assertFalse(passed)
        self.assertTrue(any("evidence_ref does not exist" in err for err in validator.errors))

    def test_mock_semantic_receipt_is_rejected(self):
        mock_receipt = self.receipts_dir / "mock_semantic_receipt.json"
        with open(mock_receipt, "w", encoding="utf-8") as f:
            json.dump({
                "test_mode": "mock",
                "provider": "claude",
                "exit_code": 0
            }, f)

        validator = EvidenceClosureValidator(self.test_dir)
        valid = validator.validate_semantic_receipt(mock_receipt)
        self.assertFalse(valid)
        self.assertTrue(any("mock mode" in err for err in validator.errors))

    def test_forbidden_transport_in_semantic_receipt_is_rejected(self):
        forbidden_receipt = self.receipts_dir / "forbidden_receipt.json"
        with open(forbidden_receipt, "w", encoding="utf-8") as f:
            json.dump({
                "transport_class": "api_key_billing",
                "provider": "openai_api",
                "exit_code": 0
            }, f)

        validator = EvidenceClosureValidator(self.test_dir)
        valid = validator.validate_semantic_receipt(forbidden_receipt)
        self.assertFalse(valid)
        self.assertTrue(any("forbidden Trial-1 transport" in err for err in validator.errors))

    def test_simulation_identity_receipt_is_rejected(self):
        sim_receipt = self.receipts_dir / "gliner2_sim.json"
        with open(sim_receipt, "w", encoding="utf-8") as f:
            json.dump({
                "component_id": "preextract_gliner2",
                "is_simulation": True,
                "status": "PASS"
            }, f)

        validator = EvidenceClosureValidator(self.test_dir)
        valid = validator.validate_identity_receipt(sim_receipt, "preextract_gliner2")
        self.assertFalse(valid)
        self.assertTrue(any("simulation/mock" in err for err in validator.errors))

    def test_p20_without_per_source_receipts_fails(self):
        p20_file = self.scorecards_dir / "four-source-regression.yaml"
        with open(p20_file, "w", encoding="utf-8") as f:
            yaml.dump({
                "schema": "four-source.v1",
                "sources": {
                    "P-h5WSQG1Sw": {"status": "PASS", "semantic_receipts": []},
                    "CygwqaNg2PY": {"status": "PASS", "semantic_receipts": []},
                    "vFTuLylvYnA": {"status": "PASS", "semantic_receipts": []},
                    "oZIsMX6WgFs": {"status": "PASS", "semantic_receipts": []}
                }
            }, f)

        validator = EvidenceClosureValidator(self.test_dir)
        passed = validator.validate_closure()
        self.assertFalse(passed)
        self.assertTrue(any("no semantic invocation receipts" in err for err in validator.errors))

    def test_p21_reusing_old_transcript_fails(self):
        p21_file = self.scorecards_dir / "fresh-e2e-report.yaml"
        with open(p21_file, "w", encoding="utf-8") as f:
            yaml.dump({
                "schema": "fresh-e2e.v1",
                "runs": {
                    "CygwqaNg2PY": {
                        "status": "PASS",
                        "fresh_audio_sha256": "abc",
                        "fresh_transcript_sha256": "def",
                        "reused_old_transcript": True  # Forbidden
                    },
                    "vFTuLylvYnA": {
                        "status": "PASS",
                        "fresh_audio_sha256": "123",
                        "fresh_transcript_sha256": "456",
                        "reused_old_transcript": False
                    }
                }
            }, f)

        validator = EvidenceClosureValidator(self.test_dir)
        passed = validator.validate_closure()
        self.assertFalse(passed)
        self.assertTrue(any("reused old transcript" in err for err in validator.errors))


if __name__ == "__main__":
    unittest.main()
