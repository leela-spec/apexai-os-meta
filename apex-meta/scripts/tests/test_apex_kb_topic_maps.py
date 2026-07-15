import argparse
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "apex_kb.py"
SPEC = importlib.util.spec_from_file_location("apex_kb_under_test", MODULE_PATH)
assert SPEC and SPEC.loader
apex_kb = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(apex_kb)


def args(kb_root: Path, **overrides):
    values = {
        "kb_root": str(kb_root),
        "allow_write": True,
        "dry_run": False,
        "strict": False,
        "json": True,
        "output_json": None,
        "init": False,
        "title": "Topic Map Fixture",
        "topic_title": None,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def write_registry(kb_root: Path, topic: dict) -> None:
    (kb_root / "manifests").mkdir(parents=True, exist_ok=True)
    registry = {"schema": "apex.kb.topic-registry.v2", "topics": [topic]}
    (kb_root / "manifests" / "topic-registry.json").write_text(json.dumps(registry), encoding="utf-8")


class TopicMapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.kb = Path(self.temp.name) / "topic-map-fixture"
        (self.kb / "raw" / "notes").mkdir(parents=True)
        (self.kb / "manifests").mkdir(parents=True, exist_ok=True)
        (self.kb / "manifests" / "source-manifest.json").write_text(
            json.dumps({"schema_version": "1.0", "kb_slug": self.kb.name, "sources": []}), encoding="utf-8"
        )

    def tearDown(self):
        self.temp.cleanup()

    def run_phase0(self):
        return apex_kb.cmd_phase0(args(self.kb))

    def rankings(self):
        return json.loads((self.kb / "manifests" / "phase0" / "topic-source-rankings.json").read_text(encoding="utf-8"))

    def test_no_top_n_truncation_beyond_thirty(self):
        # 35 files with the phrase in a heading -- old code capped at 30.
        notes = self.kb / "raw" / "notes"
        for i in range(35):
            (notes / f"doc{i}.md").write_text(f"# General {i}\n\n## Skill Tree Details\n\nBody text {i}.\n", encoding="utf-8")
        write_registry(self.kb, {
            "name": "Skill Tree", "slug": "skill-tree", "status": "draft", "target_page": "wiki/summaries/skill-tree.md",
            "phrases": ["skill tree"],
        })
        self.run_phase0()
        st = self.rankings()["skill-tree"]
        self.assertEqual(st["candidate_count"], 35)
        self.assertEqual(len(st["candidates"]), 35)

    def test_filename_h1_heading_body_tiering_order(self):
        notes = self.kb / "raw" / "notes"
        (notes / "skill tree in filename.md").write_text("# Something\n\nBody.\n", encoding="utf-8")
        (notes / "h1doc.md").write_text("# Skill Tree\n\nBody.\n", encoding="utf-8")
        (notes / "headingdoc.md").write_text("# Other\n\n## Skill Tree\n\nBody.\n", encoding="utf-8")
        (notes / "bodydoc.md").write_text("# Other\n\nMentions skill tree once in the body.\n", encoding="utf-8")
        write_registry(self.kb, {
            "name": "Skill Tree", "slug": "skill-tree", "status": "draft", "target_page": "wiki/summaries/skill-tree.md",
            "phrases": ["skill tree"],
        })
        self.run_phase0()
        st = self.rankings()["skill-tree"]
        by_path = {c["path"]: c for c in st["candidates"]}
        self.assertEqual(by_path["raw/notes/skill tree in filename.md"]["tier"], "filename")
        self.assertEqual(by_path["raw/notes/h1doc.md"]["tier"], "h1")
        self.assertEqual(by_path["raw/notes/headingdoc.md"]["tier"], "heading")
        self.assertEqual(by_path["raw/notes/bodydoc.md"]["tier"], "body_strong")
        # Sorted output must rank filename/h1/heading strictly ahead of body.
        tiers_in_order = [c["tier"] for c in st["candidates"]]
        self.assertLess(tiers_in_order.index("filename"), tiers_in_order.index("body_strong"))

    def test_every_candidate_has_why_and_pointer(self):
        notes = self.kb / "raw" / "notes"
        (notes / "a.md").write_text("# Skill Tree\n\nBody.\n", encoding="utf-8")
        write_registry(self.kb, {
            "name": "Skill Tree", "slug": "skill-tree", "status": "draft", "target_page": "wiki/summaries/skill-tree.md",
            "phrases": ["skill tree"],
        })
        self.run_phase0()
        st = self.rankings()["skill-tree"]
        for c in st["candidates"]:
            self.assertIn("why", c)
            self.assertTrue(c["pointers"], f"candidate {c['path']} has no pointer")
            self.assertIn("field", c["pointers"][0])
            self.assertIn("line", c["pointers"][0])

    def test_negative_term_suppresses_only_body_only_weak_match(self):
        notes = self.kb / "raw" / "notes"
        # "tree" only, buried in body, single section, no co-occurrence -- must suppress.
        (notes / "suppressed.md").write_text("# Unrelated\n\n## Section\n\nA tree is mentioned once here.\n", encoding="utf-8")
        # "tree" in the heading -- must NOT suppress (only body-only matches are suppressible).
        (notes / "not-suppressed-heading.md").write_text("# Family Tree\n\nUnrelated body text.\n", encoding="utf-8")
        write_registry(self.kb, {
            "name": "Skill Tree", "slug": "skill-tree", "status": "draft", "target_page": "wiki/summaries/skill-tree.md",
            "phrases": ["skill tree"], "supporting_terms": ["tree"], "negative_terms": ["tree"],
        })
        self.run_phase0()
        st = self.rankings()["skill-tree"]
        candidate_paths = {c["path"] for c in st["candidates"]}
        self.assertNotIn("raw/notes/suppressed.md", candidate_paths)
        self.assertIn("raw/notes/suppressed.md", st["zero_signal_custody"])
        self.assertIn("raw/notes/not-suppressed-heading.md", candidate_paths)

    def test_negative_term_never_suppresses_phrase_or_filename_match(self):
        notes = self.kb / "raw" / "notes"
        # Phrase match in body plus the negative term elsewhere -- must survive as body_strong.
        (notes / "phrase-and-negative.md").write_text(
            "# Unrelated\n\nThis mentions skill tree directly, and also a tree elsewhere.\n", encoding="utf-8"
        )
        write_registry(self.kb, {
            "name": "Skill Tree", "slug": "skill-tree", "status": "draft", "target_page": "wiki/summaries/skill-tree.md",
            "phrases": ["skill tree"], "supporting_terms": ["tree"], "negative_terms": ["tree"],
        })
        self.run_phase0()
        st = self.rankings()["skill-tree"]
        by_path = {c["path"]: c for c in st["candidates"]}
        self.assertIn("raw/notes/phrase-and-negative.md", by_path)
        self.assertEqual(by_path["raw/notes/phrase-and-negative.md"]["tier"], "body_strong")

    def test_elbow_cut_keeps_all_of_a_uniformly_strong_body_pool(self):
        notes = self.kb / "raw" / "notes"
        # 25 body-only matches, all equally strong -- no fixed count should cut this down.
        for i in range(25):
            (notes / f"body{i}.md").write_text(f"# Doc {i}\n\nMentions skill tree once, item {i}.\n", encoding="utf-8")
        write_registry(self.kb, {
            "name": "Skill Tree", "slug": "skill-tree", "status": "draft", "target_page": "wiki/summaries/skill-tree.md",
            "phrases": ["skill tree"],
        })
        self.run_phase0()
        st = self.rankings()["skill-tree"]
        self.assertEqual(st["candidate_count"], 25)
        self.assertEqual(st["gap_cut"]["held_in_custody_count"], 0, "uniform scores should not be arbitrarily cut")

    def test_custody_accounts_for_every_scanned_source(self):
        notes = self.kb / "raw" / "notes"
        (notes / "matches.md").write_text("# Skill Tree\n\nBody.\n", encoding="utf-8")
        (notes / "no-match.md").write_text("# Unrelated\n\nNothing relevant here.\n", encoding="utf-8")
        write_registry(self.kb, {
            "name": "Skill Tree", "slug": "skill-tree", "status": "draft", "target_page": "wiki/summaries/skill-tree.md",
            "phrases": ["skill tree"],
        })
        result = self.run_phase0()
        st = self.rankings()["skill-tree"]
        accounted = set(c["path"] for c in st["candidates"]) | set(st["zero_signal_custody"])
        self.assertEqual(len(accounted), st["considered_source_count"])
        self.assertEqual(st["considered_source_count"], result["source_file_count"])

    def test_absent_registry_produces_no_rankings_or_workpacks(self):
        notes = self.kb / "raw" / "notes"
        (notes / "a.md").write_text("# Doc\n\nBody.\n", encoding="utf-8")
        result = self.run_phase0()
        self.assertEqual(result["topic_registry_entries"], 0)
        self.assertEqual(result["work_pack_count"], 0)
        rankings = self.rankings()
        self.assertEqual(rankings, {})


if __name__ == "__main__":
    unittest.main()
