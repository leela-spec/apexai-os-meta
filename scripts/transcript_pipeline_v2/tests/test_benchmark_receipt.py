"""Unit tests for truthful batch benchmark receipt logic."""
import json
import tempfile
import unittest
from pathlib import Path

REQUIRED_STAGE_KEYS = [
    "SOURCE_ACQUIRED",
    "ASR_COMPLETE",
    "SOURCE_CUSTODY_VALID",
    "MAP_COMPLETE",
    "MAP_VALID",
    "REDUCE_COMPLETE",
    "REDUCE_VALID",
    "VERIFICATION_ROUTED",
    "OPERATOR_ARTIFACT_COMPLETE",
    "COMPLETE_VALIDATION_PASS"
]


def evaluate_run_truthfulness(source_data: dict) -> dict:
    """Evaluate whether a run receipt satisfies stage-truthfulness."""
    stages = source_data.get("stages", {})
    all_stages_pass = all(stages.get(k) is True for k in REQUIRED_STAGE_KEYS)
    has_receipts = source_data.get("semantic_receipts_verified", False)
    
    return {
        "is_truthful": all_stages_pass and has_receipts,
        "missing_stages": [k for k in REQUIRED_STAGE_KEYS if not stages.get(k)],
        "has_receipts": has_receipts
    }


class TestBenchmarkReceipt(unittest.TestCase):

    def test_incomplete_stages_marked_false(self):
        source_data = {
            "id": "test-src",
            "semantic_receipts_verified": True,
            "stages": {
                "SOURCE_ACQUIRED": True,
                "ASR_COMPLETE": True,
                "SOURCE_CUSTODY_VALID": True,
                "MAP_COMPLETE": True,
                "MAP_VALID": True,
                "REDUCE_COMPLETE": False, # Failed reduce
                "REDUCE_VALID": False,
                "VERIFICATION_ROUTED": False,
                "OPERATOR_ARTIFACT_COMPLETE": False,
                "COMPLETE_VALIDATION_PASS": False
            }
        }
        res = evaluate_run_truthfulness(source_data)
        self.assertFalse(res["is_truthful"])
        self.assertIn("REDUCE_COMPLETE", res["missing_stages"])

    def test_complete_stages_with_receipts_marked_true(self):
        source_data = {
            "id": "test-src",
            "semantic_receipts_verified": True,
            "stages": {k: True for k in REQUIRED_STAGE_KEYS}
        }
        res = evaluate_run_truthfulness(source_data)
        self.assertTrue(res["is_truthful"])
        self.assertEqual(len(res["missing_stages"]), 0)


if __name__ == "__main__":
    unittest.main()
