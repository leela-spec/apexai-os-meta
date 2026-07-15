import argparse
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "apex_kb.py"
SPEC = importlib.util.spec_from_file_location("apex_kb_under_test_tsc", MODULE_PATH)
assert SPEC and SPEC.loader
apex_kb = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(apex_kb)


def args(kb_root: Path, **overrides):
    values = {
        "kb_root": str(kb_root),
        "topic_slug": None,
        "phrase": None,
        "search_root": None,
        "search_cap": None,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class TopicSanityCheckTests(unittest.TestCase):
    def setUp(self):
        # Reproduce the shape of the real incident: a KB rooted at
        # "...LeelaAppDevelopment/LeelaApp-Index-KB-Wiki_v2" - the parent and
        # the KB's own name both plainly say "Leela", but the topic locked
        # was "Dealer App", which appears nowhere in the local tree. Sibling
        # filenames use the word "process" a lot (generic project vocabulary),
        # mirroring the real corpus that produced false-positive matches.
        self.temp = tempfile.TemporaryDirectory()
        self.parent = Path(self.temp.name) / "LeelaAppDevelopment"
        self.kb = self.parent / "LeelaApp-Index-KB-Wiki_v2"
        self.kb.mkdir(parents=True)
        (self.kb / "manifests").mkdir()
        (self.parent / "Rhythm Feature Spec.md").write_text("Rhythm content\n", encoding="utf-8")
        (self.parent / "Path Feature Spec.md").write_text("Path content\n", encoding="utf-8")
        (self.parent / "Process guidance.md").write_text("generic process notes\n", encoding="utf-8")
        (self.parent / "NewCodexProcess.md").write_text("generic process notes\n", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def _write_registry(self, topics):
        (self.kb / "manifests" / "topic-registry.json").write_text(
            json.dumps({"schema": "apex.kb.topic-registry.v2", "topics": topics}), encoding="utf-8"
        )

    def test_mismatched_topic_is_flagged_before_any_write(self):
        self._write_registry([
            {
                "name": "Dealer App process evidence",
                "slug": "dealer-app-process-evidence",
                "status": "not_started",
                "phrases": ["Dealer App", "dealer app"],
                "aliases": ["DealerApp", "dealer-app"],
                "supporting_terms": ["dealer", "process", "workflow", "screen", "feature"],
            }
        ])
        result = apex_kb.cmd_topic_sanity_check(args(self.kb, topic_slug="dealer-app-process-evidence"))
        self.assertEqual(result["verdict"], "scope_evidence_absent")
        self.assertEqual(result["recommendation"], "stop_and_confirm_topic_with_operator")
        self.assertEqual(result["evidence"]["path_component_hits"], [])
        self.assertEqual(result["evidence"]["filename_scan"]["strong_hit_count"], 0)

    def test_single_generic_supporting_term_never_carries_verdict_alone(self):
        # "process" alone matches "Process guidance.md" and "NewCodexProcess.md",
        # but a single weak term must never be enough - this is the exact
        # false-positive pattern that made the real check report "proceed"
        # against the actual Dealer App incident's corpus.
        self._write_registry([
            {
                "name": "Dealer App process evidence",
                "slug": "dealer-app-process-evidence",
                "status": "not_started",
                "phrases": ["Dealer App"],
                "aliases": [],
                "supporting_terms": ["process"],
            }
        ])
        result = apex_kb.cmd_topic_sanity_check(args(self.kb, topic_slug="dealer-app-process-evidence"))
        self.assertEqual(result["verdict"], "scope_evidence_absent")
        self.assertEqual(result["evidence"]["filename_scan"]["weak_cooccurrence_hit_count"], 0)

    def test_two_cooccurring_weak_terms_are_reported_but_never_carry_the_verdict(self):
        # Weak-term co-occurrence is surfaced for transparency only; it must
        # never independently flip the verdict to "found" - two generic words
        # sharing a filename is still not evidence a specific topic is real.
        (self.parent / "Codex Process Failure Report.md").write_text("x\n", encoding="utf-8")
        self._write_registry([
            {
                "name": "Dealer App",
                "slug": "dealer-app",
                "status": "not_started",
                "phrases": ["Dealer App"],
                "aliases": [],
                "supporting_terms": ["process", "failure"],
            }
        ])
        result = apex_kb.cmd_topic_sanity_check(args(self.kb, topic_slug="dealer-app"))
        self.assertGreaterEqual(result["evidence"]["filename_scan"]["weak_cooccurrence_hit_count"], 1)
        self.assertEqual(result["verdict"], "scope_evidence_absent")
        self.assertEqual(result["recommendation"], "stop_and_confirm_topic_with_operator")

    def test_kb_own_generated_output_is_excluded_from_the_scan(self):
        # Files already written inside kb_root (audit items, work packs) are
        # the output of the very run being gated - they must never count as
        # independent evidence that a topic is real.
        (self.kb / "audit").mkdir()
        (self.kb / "audit" / "dealer-app-source-access.md").write_text("x\n", encoding="utf-8")
        (self.kb / "manifests" / "phase0").mkdir()
        (self.kb / "manifests" / "phase0" / "dealer-app-process-evidence.json").write_text("{}\n", encoding="utf-8")
        self._write_registry([
            {
                "name": "Dealer App",
                "slug": "dealer-app",
                "status": "not_started",
                "phrases": ["Dealer App"],
                "aliases": [],
                "supporting_terms": [],
            }
        ])
        result = apex_kb.cmd_topic_sanity_check(args(self.kb, topic_slug="dealer-app"))
        self.assertEqual(result["evidence"]["filename_scan"]["strong_hit_count"], 0)
        self.assertEqual(result["verdict"], "scope_evidence_absent")

    def test_kb_schema_and_readme_are_not_treated_as_evidence(self):
        # These are written by the same scaffold step that locks the topic -
        # self-authored, circular confirmation, not independent evidence.
        (self.kb / "kb-schema.md").write_text("# KB Schema - Leela Dealer App Index KB Wiki v2\n", encoding="utf-8")
        (self.kb / "README.md").write_text("# Leela Dealer App Index KB Wiki v2\n", encoding="utf-8")
        self._write_registry([
            {
                "name": "Dealer App",
                "slug": "dealer-app",
                "status": "not_started",
                "phrases": ["Dealer App"],
                "aliases": [],
                "supporting_terms": [],
            }
        ])
        result = apex_kb.cmd_topic_sanity_check(args(self.kb, topic_slug="dealer-app"))
        self.assertEqual(result["verdict"], "scope_evidence_absent")

    def test_topic_matching_kb_root_name_is_recognized(self):
        self._write_registry([
            {
                "name": "Rhythm",
                "slug": "rhythm",
                "status": "not_started",
                "phrases": ["Rhythm", "leela"],
                "aliases": [],
                "supporting_terms": [],
            }
        ])
        result = apex_kb.cmd_topic_sanity_check(args(self.kb, topic_slug="rhythm"))
        self.assertEqual(result["verdict"], "scope_evidence_found")
        self.assertEqual(result["recommendation"], "proceed")
        self.assertIn("leela", result["evidence"]["path_component_hits"])

    def test_filename_scan_finds_topic_evident_in_sibling_files(self):
        self._write_registry([
            {
                "name": "Path",
                "slug": "path",
                "status": "not_started",
                "phrases": ["Path Feature"],
                "aliases": [],
                "supporting_terms": [],
            }
        ])
        result = apex_kb.cmd_topic_sanity_check(args(self.kb, topic_slug="path"))
        self.assertEqual(result["verdict"], "scope_evidence_found")
        self.assertGreaterEqual(result["evidence"]["filename_scan"]["strong_hit_count"], 1)

    def test_ad_hoc_phrase_without_registered_topic(self):
        result = apex_kb.cmd_topic_sanity_check(args(self.kb, phrase=["Dealer App"]))
        self.assertEqual(result["verdict"], "scope_evidence_absent")
        self.assertEqual(result["recommendation"], "stop_and_confirm_topic_with_operator")

    def test_no_terms_is_blocked(self):
        result = apex_kb.cmd_topic_sanity_check(args(self.kb))
        self.assertEqual(result["status"], "blocked")

    def test_never_writes_anything(self):
        self._write_registry([
            {"name": "Dealer App", "slug": "dealer-app", "status": "not_started", "phrases": ["Dealer App"]}
        ])
        before = sorted(p for p in self.kb.rglob("*"))
        apex_kb.cmd_topic_sanity_check(args(self.kb, topic_slug="dealer-app"))
        after = sorted(p for p in self.kb.rglob("*"))
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
