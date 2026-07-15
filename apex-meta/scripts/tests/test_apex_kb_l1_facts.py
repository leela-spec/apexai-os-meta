import argparse
import importlib.util
import json
import subprocess
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
        "title": "L1 Facts Fixture",
        "topic_title": None,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class SectionSpanTests(unittest.TestCase):
    def test_span_runs_to_next_same_or_shallower_heading(self):
        text = "# Title\n\n## A\n\nbody a\n\n### A1\n\nnested\n\n## B\n\nbody b\n"
        with tempfile.TemporaryDirectory() as td:
            kb = Path(td)
            p = kb / "doc.md"
            p.write_text(text, encoding="utf-8")
            structure = apex_kb.parse_markdown_structure(p, kb)
        spans = {s["heading"]: s for s in structure["section_spans"]}
        # "A" should end right before "B" starts (i.e. include its nested "A1").
        self.assertLess(spans["A"]["end_line"], spans["B"]["start_line"])
        self.assertGreaterEqual(spans["A"]["end_line"], spans["A1"]["end_line"])
        # "B" runs to end of file since nothing follows it.
        self.assertEqual(spans["B"]["end_line"], len(text.splitlines()))


class DuplicateAndVersionFamilyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.kb = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_exact_and_normalized_duplicate_groups(self):
        (self.kb / "a.md").write_text("# Doc\n\nSame content here.\n", encoding="utf-8")
        (self.kb / "b.md").write_text("# Doc\n\nSame content here.\n", encoding="utf-8")  # exact dup of a
        (self.kb / "c.md").write_text("#   Doc\n\nsame   CONTENT here.\n", encoding="utf-8")  # normalized dup only
        files = [self.kb / "a.md", self.kb / "b.md", self.kb / "c.md"]
        hash_groups = apex_kb.compute_hash_groups(self.kb, files)
        exact_dupes = [v for v in hash_groups.values() if len(v) > 1]
        self.assertEqual(len(exact_dupes), 1)
        self.assertEqual(sorted(exact_dupes[0]), ["a.md", "b.md"])
        normalized = apex_kb.normalized_duplicate_groups(self.kb, files)
        self.assertEqual(len(normalized), 1)
        self.assertEqual(sorted(normalized[0]), ["a.md", "b.md", "c.md"])

    def test_version_family_candidates_group_by_stripped_filename_token(self):
        (self.kb / "plan_v1.md").write_text("# Plan v1\n\nBody.\n", encoding="utf-8")
        (self.kb / "plan_v2.md").write_text("# Plan v2\n\nBody.\n", encoding="utf-8")
        (self.kb / "unrelated.md").write_text("# Unrelated\n\nBody.\n", encoding="utf-8")
        files = [self.kb / "plan_v1.md", self.kb / "plan_v2.md", self.kb / "unrelated.md"]
        families = apex_kb.version_family_candidates(self.kb, files)
        self.assertEqual(len(families), 1)
        self.assertEqual(sorted(families[0]["members"]), ["plan_v1.md", "plan_v2.md"])
        self.assertEqual(families[0]["confidence"], "possible")

    def test_never_auto_resolves_supersession(self):
        # version_family_candidates only ever returns discovery evidence --
        # no field claims one member supersedes another.
        (self.kb / "doc_old.md").write_text("# Doc\n\nOld.\n", encoding="utf-8")
        (self.kb / "doc_new.md").write_text("# Doc\n\nNew.\n", encoding="utf-8")
        families = apex_kb.version_family_candidates(self.kb, [self.kb / "doc_old.md", self.kb / "doc_new.md"])
        self.assertEqual(len(families), 1)
        self.assertNotIn("supersedes", families[0])
        self.assertNotIn("current", families[0])


class FreshnessTests(unittest.TestCase):
    def test_git_history_takes_priority_when_available(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td)
            subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
            kb = repo / "kb"
            (kb / "raw").mkdir(parents=True)
            (kb / "raw" / "doc.md").write_text("# Doc\n\nBody.\n", encoding="utf-8")
            subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-q", "-m", "add doc"], cwd=repo, check=True)
            git_map, git_available = apex_kb.git_last_change_map(kb)
            self.assertTrue(git_available)
            self.assertIn("raw/doc.md", git_map)

    def test_mtime_fallback_when_no_git_repo(self):
        with tempfile.TemporaryDirectory() as td:
            kb = Path(td)  # not a git repo
            git_map, git_available = apex_kb.git_last_change_map(kb)
            self.assertFalse(git_available)
            self.assertEqual(git_map, {})


class BlockedFileVisibilityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.kb = Path(self.temp.name) / "blocked-fixture"
        (self.kb / "raw" / "other").mkdir(parents=True)
        (self.kb / "manifests").mkdir(parents=True)
        (self.kb / "manifests" / "source-manifest.json").write_text(
            json.dumps({"schema_version": "1.0", "kb_slug": self.kb.name, "sources": []}), encoding="utf-8"
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_non_text_file_is_inventoried_not_dropped(self):
        (self.kb / "raw" / "other" / "readable.md").write_text("# Doc\n\nBody.\n", encoding="utf-8")
        (self.kb / "raw" / "other" / "image.png").write_bytes(b"\x89PNG\r\n\x1a\n binary content")
        result = apex_kb.cmd_phase0(args(self.kb))
        facts = json.loads((self.kb / "manifests" / "phase0" / "source-facts.json").read_text(encoding="utf-8"))
        by_path = {f["path"]: f for f in facts}
        self.assertIn("raw/other/image.png", by_path)
        self.assertFalse(by_path["raw/other/image.png"]["text_readable"])
        self.assertEqual(by_path["raw/other/image.png"]["blocked_reason"], "non_text")
        self.assertTrue(by_path["raw/other/readable.md"]["text_readable"])
        self.assertIsNone(by_path["raw/other/readable.md"]["blocked_reason"])
        self.assertEqual(result["blocked_file_counts"]["non_text"], 1)
        # Scope closure: every scanned file appears, blocked or not.
        self.assertEqual(len(by_path), 2)


if __name__ == "__main__":
    unittest.main()
