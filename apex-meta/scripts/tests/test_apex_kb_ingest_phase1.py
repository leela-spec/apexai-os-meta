import argparse
import importlib.util
import re
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "apex_kb.py"
SPEC = importlib.util.spec_from_file_location("apex_kb_under_test_p1", MODULE_PATH)
assert SPEC and SPEC.loader
apex_kb = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(apex_kb)


def args(kb_root: Path, **overrides):
    values = {
        "kb_root": str(kb_root),
        "allow_write": True,
        "dry_run": False,
        "source_path": None,
        "topic_slug": None,
        "source_slug": None,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class IngestPhase1TopicScopedTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.kb = Path(self.temp.name) / "kb"
        self.kb.mkdir(parents=True)
        (self.kb / "manifests").mkdir()
        (self.kb / "manifests" / "source-manifest.json").write_text("{\"schema_version\": \"1.0\", \"sources\": []}", encoding="utf-8")
        (self.kb / "kb-schema.md").write_text("# schema\n", encoding="utf-8")

        self.raw = Path(self.temp.name) / "raw"
        self.raw.mkdir()
        self.source_a = self.raw / "Source A.md"
        self.source_a.write_text("Source A content\n", encoding="utf-8")
        self.source_b = self.raw / "Source B.md"
        self.source_b.write_text("Source B content\n", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_missing_topic_slug_is_blocked(self):
        result = apex_kb.cmd_ingest_phase1(args(self.kb, source_path=str(self.source_a)))
        self.assertEqual(result["status"], "blocked")

    def test_first_source_creates_one_topic_scoped_file(self):
        result = apex_kb.cmd_ingest_phase1(args(self.kb, source_path=str(self.source_a), topic_slug="rhythm"))
        self.assertEqual(result["status"], "operator_review_needed")
        self.assertFalse(result["already_present"])
        path = self.kb / "ingest-analysis" / "rhythm.analysis.md"
        self.assertTrue(path.exists())
        self.assertFalse((self.kb / "ingest-analysis" / "source-a.analysis.md").exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("topic_slug: \"rhythm\"", text)
        self.assertIn("source_count: 1", text)
        self.assertEqual(len(re.findall(r"^### \S+ - authority:", text, re.MULTILINE)), 1)

    def test_second_source_appends_to_same_topic_file(self):
        apex_kb.cmd_ingest_phase1(args(self.kb, source_path=str(self.source_a), topic_slug="rhythm"))
        result = apex_kb.cmd_ingest_phase1(args(self.kb, source_path=str(self.source_b), topic_slug="rhythm"))
        self.assertFalse(result["already_present"])
        path = self.kb / "ingest-analysis" / "rhythm.analysis.md"
        text = path.read_text(encoding="utf-8")
        self.assertIn("source_count: 2", text)
        self.assertIn("### source-a - authority:", text)
        self.assertIn("### source-b - authority:", text)
        self.assertEqual(len(re.findall(r"^### \S+ - authority:", text, re.MULTILINE)), 2)
        # Only one topic file should exist for this topic - no per-source files.
        self.assertEqual(sorted(p.name for p in (self.kb / "ingest-analysis").glob("*.md")), ["rhythm.analysis.md"])

    def test_rerun_with_same_source_is_idempotent_noop(self):
        apex_kb.cmd_ingest_phase1(args(self.kb, source_path=str(self.source_a), topic_slug="rhythm"))
        path = self.kb / "ingest-analysis" / "rhythm.analysis.md"
        before = path.read_text(encoding="utf-8")
        result = apex_kb.cmd_ingest_phase1(args(self.kb, source_path=str(self.source_a), topic_slug="rhythm"))
        self.assertTrue(result["already_present"])
        after = path.read_text(encoding="utf-8")
        self.assertEqual(before, after)

    def test_preflight_finds_source_inside_topic_scoped_file(self):
        apex_kb.cmd_ingest_phase1(args(self.kb, source_path=str(self.source_a), topic_slug="rhythm"))
        result = apex_kb.cmd_preflight(args(self.kb, source_path=str(self.source_a)))
        self.assertIn("ingest-analysis/rhythm.analysis.md", result["checks"]["existing_phase_1_analysis"])

    def test_preflight_reports_no_analysis_for_unanalyzed_source(self):
        apex_kb.cmd_ingest_phase1(args(self.kb, source_path=str(self.source_a), topic_slug="rhythm"))
        result = apex_kb.cmd_preflight(args(self.kb, source_path=str(self.source_b)))
        self.assertEqual(result["checks"]["existing_phase_1_analysis"], [])


if __name__ == "__main__":
    unittest.main()
