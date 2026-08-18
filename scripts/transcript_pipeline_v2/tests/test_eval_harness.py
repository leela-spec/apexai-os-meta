"""Unit tests for semantic eval harness."""
import unittest
from scripts.transcript_pipeline_v2.eval.run_eval import run_evaluation
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent


class TestEvalHarness(unittest.TestCase):

    def test_run_eval_outputs_exist(self):
        run_evaluation()
        eval_yaml = REPO_ROOT / "artifacts" / "transcript_pipeline_v2" / "comparisons" / "semantic-eval.yaml"
        base_yaml = REPO_ROOT / "artifacts" / "transcript_pipeline_v2" / "comparisons" / "product-baselines.yaml"
        self.assertTrue(eval_yaml.exists())
        self.assertTrue(base_yaml.exists())


if __name__ == "__main__":
    unittest.main()
