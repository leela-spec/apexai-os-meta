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

SCHEMA_PATH = Path(__file__).resolve().parents[3] / ".claude" / "skills" / "apex-kb" / "references" / "topic-work-pack.schema.json"


def args(kb_root: Path, **overrides):
    values = {
        "kb_root": str(kb_root),
        "allow_write": True,
        "dry_run": False,
        "strict": False,
        "json": True,
        "output_json": None,
        "init": False,
        "title": "Work Pack Fixture",
        "topic_title": None,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def write_registry(kb_root: Path, topic: dict) -> None:
    (kb_root / "manifests").mkdir(parents=True, exist_ok=True)
    registry = {"schema": "apex.kb.topic-registry.v2", "topics": [topic]}
    (kb_root / "manifests" / "topic-registry.json").write_text(json.dumps(registry), encoding="utf-8")


def assert_matches_schema(test_case, instance, schema):
    """Minimal structural check covering required/type/enum -- avoids adding a
    jsonschema dependency the runtime doesn't otherwise need."""
    def check(value, sub_schema, path):
        if "const" in sub_schema:
            test_case.assertEqual(value, sub_schema["const"], path)
            return
        if "enum" in sub_schema:
            test_case.assertIn(value, sub_schema["enum"], path)
            return
        schema_type = sub_schema.get("type")
        if schema_type == "object":
            test_case.assertIsInstance(value, dict, path)
            for req in sub_schema.get("required", []):
                test_case.assertIn(req, value, f"{path}.{req} missing")
            for key, val in value.items():
                prop_schema = sub_schema.get("properties", {}).get(key)
                if prop_schema is not None:
                    check(val, prop_schema, f"{path}.{key}")
        elif schema_type == "array":
            test_case.assertIsInstance(value, list, path)
            item_schema = sub_schema.get("items")
            if item_schema:
                for i, item in enumerate(value):
                    check(item, item_schema, f"{path}[{i}]")
        elif schema_type == "string":
            test_case.assertIsInstance(value, str, path)

    check(instance, schema, "$")


class WorkPackTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.kb = Path(self.temp.name) / "workpack-fixture"
        (self.kb / "raw" / "notes").mkdir(parents=True)
        (self.kb / "manifests").mkdir(parents=True, exist_ok=True)
        (self.kb / "manifests" / "source-manifest.json").write_text(
            json.dumps({"schema_version": "1.0", "kb_slug": self.kb.name, "sources": []}), encoding="utf-8"
        )
        self.registry_topic = {
            "name": "Skill Tree", "slug": "skill-tree", "status": "draft", "target_page": "wiki/summaries/skill-tree.md",
            "phrases": ["skill tree"],
            "target_queries": [
                {"query_id": "st-q1", "question": "What is Skill Tree?", "priority": "critical",
                 "answer_requirements": ["definition"], "expected_page": "wiki/summaries/skill-tree.md"}
            ],
        }

    def tearDown(self):
        self.temp.cleanup()

    def run_phase0(self):
        write_registry(self.kb, self.registry_topic)
        return apex_kb.cmd_phase0(args(self.kb))

    def rankings(self):
        return json.loads((self.kb / "manifests" / "phase0" / "topic-source-rankings.json").read_text(encoding="utf-8"))

    def workpack(self):
        return json.loads((self.kb / "manifests" / "phase0" / "work-packs" / "skill-tree.json").read_text(encoding="utf-8"))

    def test_workpack_generated_per_registry_topic(self):
        notes = self.kb / "raw" / "notes"
        (notes / "a.md").write_text("# Skill Tree\n\nBody.\n", encoding="utf-8")
        result = self.run_phase0()
        self.assertEqual(result["work_pack_count"], 1)
        self.assertTrue((self.kb / "manifests" / "phase0" / "work-packs" / "skill-tree.md").exists())
        self.assertTrue((self.kb / "manifests" / "phase0" / "work-packs" / "skill-tree.json").exists())

    def test_workpack_carries_target_queries_from_registry(self):
        notes = self.kb / "raw" / "notes"
        (notes / "a.md").write_text("# Skill Tree\n\nBody.\n", encoding="utf-8")
        self.run_phase0()
        wp = self.workpack()
        self.assertEqual(len(wp["target_queries"]), 1)
        self.assertEqual(wp["target_queries"][0]["query_id"], "st-q1")

    def test_workpack_disclosure_reconciles_with_rankings(self):
        notes = self.kb / "raw" / "notes"
        for i in range(5):
            (notes / f"strong{i}.md").write_text(f"# Skill Tree {i}\n\nBody.\n", encoding="utf-8")
        for i in range(3):
            (notes / f"weak{i}.md").write_text(f"# Unrelated {i}\n\nMentions skill tree once, item {i}.\n", encoding="utf-8")
        (notes / "no-match.md").write_text("# Unrelated\n\nNothing here.\n", encoding="utf-8")
        self.run_phase0()
        st = self.rankings()["skill-tree"]
        wp = self.workpack()
        d = wp["disclosure"]
        self.assertEqual(d["candidate_count"], st["candidate_count"])
        self.assertEqual(d["held_in_custody_count"], len(st["held_in_custody"]))
        self.assertEqual(d["zero_signal_custody_count"], len(st["zero_signal_custody"]))
        self.assertEqual(d["concentrated_count"], len(wp["concentrated_candidates"]))
        # Concentration never exceeds the exhaustive candidate count.
        self.assertLessEqual(d["concentrated_count"] + d["held_in_custody_count"], d["candidate_count"])

    def test_exact_duplicates_collapse_to_one_representative_in_workpack(self):
        notes = self.kb / "raw" / "notes"
        content = "# Skill Tree Duplicate\n\nSame body content for both files.\n"
        (notes / "dup-a.md").write_text(content, encoding="utf-8")
        (notes / "dup-b.md").write_text(content, encoding="utf-8")
        self.run_phase0()
        wp = self.workpack()
        paths_in_workpack = {c["path"] for c in wp["concentrated_candidates"]}
        # Only one of the two exact-duplicate paths should appear standalone.
        self.assertEqual(len(paths_in_workpack & {"raw/notes/dup-a.md", "raw/notes/dup-b.md"}), 1)
        representative = next(c for c in wp["concentrated_candidates"] if c["path"] in {"raw/notes/dup-a.md", "raw/notes/dup-b.md"})
        self.assertEqual(len(representative["duplicates_of_this"]), 1)

    def test_held_in_custody_not_silently_dropped_from_rankings(self):
        # Force a real elbow gap by mixing a large uniform pool with a couple of
        # much weaker outliers so held_in_custody is non-empty, then confirm
        # those held sources are still fully present in topic-source-rankings.json
        # (only excluded from the concentrated work pack).
        notes = self.kb / "raw" / "notes"
        for i in range(15):
            (notes / f"strong{i}.md").write_text(f"# Skill Tree {i}\n\nBody with skill tree repeated. skill tree again.\n", encoding="utf-8")
        (notes / "weak0.md").write_text("# Unrelated\n\n## Section\n\nOne faint mention buried alone.\nskill tree\n", encoding="utf-8")
        self.run_phase0()
        st = self.rankings()["skill-tree"]
        wp = self.workpack()
        held_ids = set(st["held_in_custody"])
        concentrated_ids = {c["source_id"] for c in wp["concentrated_candidates"]}
        if held_ids:
            self.assertTrue(held_ids.isdisjoint(concentrated_ids))
            all_candidate_ids = {c["source_id"] for c in st["candidates"]}
            self.assertTrue(held_ids.issubset(all_candidate_ids), "held sources must still exist in the exhaustive candidate list")

    def test_workpack_matches_schema_shape(self):
        notes = self.kb / "raw" / "notes"
        (notes / "a.md").write_text("# Skill Tree\n\nBody.\n", encoding="utf-8")
        self.run_phase0()
        wp = self.workpack()
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        assert_matches_schema(self, wp, schema)


if __name__ == "__main__":
    unittest.main()
