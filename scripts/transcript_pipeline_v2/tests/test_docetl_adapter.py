"""Unit tests for DocETL adapter."""
import unittest
from scripts.transcript_pipeline_v2.adapters.docetl_runner import DocETLAdapter


class TestDocETLAdapter(unittest.TestCase):

    def test_docetl_blocked_for_trial1(self):
        adapter = DocETLAdapter()
        res = adapter.run_pipeline({})
        self.assertEqual(res["status"], "BLOCKED_FOR_TRIAL1")
        self.assertIn("LiteLLM", res["reason"])


if __name__ == "__main__":
    unittest.main()
