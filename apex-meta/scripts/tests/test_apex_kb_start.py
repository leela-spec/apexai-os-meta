from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "apex_kb_start.py"
SPEC = importlib.util.spec_from_file_location("apex_kb_start_under_test", SCRIPT)
assert SPEC and SPEC.loader
start = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(start)


class ApexKbStartTests(unittest.TestCase):
    def test_skill_routes_new_kb_requests_through_public_start(self):
        repo_root = SCRIPT.parents[2]
        skill = (repo_root / ".claude/skills/apex-kb/SKILL.md").read_text(encoding="utf-8")
        agents = (repo_root / "AGENTS.md").read_text(encoding="utf-8")
        package = (repo_root / ".claude/skills/apex-kb/package-manifest.md").read_text(encoding="utf-8")
        workflow = repo_root / ".claude/skills/apex-kb/references/start-workflow.md"
        template = repo_root / ".claude/skills/apex-kb/templates/start-config-template.yaml"
        self.assertIn("apex_kb.py start", skill)
        self.assertIn("Do not author `manifests/topic-registry.json` or invoke `control init` freehand for a new KB", skill)
        self.assertIn(".claude/skills/apex-kb/SKILL.md", agents)
        self.assertIn("start_frontend: apex-meta/scripts/apex_kb_start.py", package)
        self.assertTrue(workflow.is_file())
        self.assertTrue(template.is_file())

    def test_output_mapping_is_explicit(self):
        self.assertEqual(start.OUTPUT_MAP["analysis_only"], "analysis_only")
        self.assertEqual(start.OUTPUT_MAP["compiled_kb"], "compiled_full")
        self.assertEqual(start.OUTPUT_MAP["query_ready"], "query_ready")

    def test_semantic_depth_does_not_reduce_deterministic_phase_capability(self):
        self.assertEqual(start.COMPAT_PHASE1_MIN_COVERAGE, 0.6)
        self.assertNotIn("DETAIL_COVERAGE", vars(start))

    def test_topic_registry_generates_machine_ids_and_multiple_queries(self):
        registry = start.topic_registry(
            [
                {
                    "name": "Consent and safety",
                    "phrases": ["explicit consent", "safe word"],
                    "ambiguous_or_negative_terms": ["joke punishment"],
                    "questions": ["How is consent established?", "How can consent be withdrawn?"],
                }
            ]
        )
        topic = registry["topics"][0]
        self.assertEqual(topic["slug"], "consent-and-safety")
        self.assertEqual(topic["negative_terms"], ["joke punishment"])
        self.assertEqual(len(topic["target_queries"]), 2)
        self.assertEqual(topic["target_queries"][1]["query_id"], "consent-and-safety-q2")

    def test_duplicate_topic_names_receive_collision_safe_slugs(self):
        topic = {
            "name": "Operations",
            "phrases": ["operations"],
            "ambiguous_or_negative_terms": [],
            "questions": ["What are the operations?"],
        }
        registry = start.topic_registry([topic, dict(topic)])
        self.assertEqual([item["slug"] for item in registry["topics"]], ["operations", "operations-2"])

    def test_worktree_parser_preserves_primary_order(self):
        parsed = start.parse_worktrees(
            "worktree C:/GitDev/main\nHEAD aaaa\nbranch refs/heads/main\n\n"
            "worktree C:/GitDev/linked\nHEAD bbbb\nbranch refs/heads/feature\n\n"
        )
        self.assertEqual(parsed[0]["branch"], "main")
        self.assertEqual(parsed[1]["branch"], "feature")

    def test_remote_slug_supports_https_and_ssh(self):
        self.assertEqual(start.remote_slug("https://github.com/leela-spec/apexai-os-meta.git"), "leela-spec/apexai-os-meta")
        self.assertEqual(start.remote_slug("git@github.com:leela-spec/apexai-os-meta.git"), "leela-spec/apexai-os-meta")

    def test_repository_paths_reject_parent_escape(self):
        with self.assertRaises(start.StartError) as raised:
            start.repo_path(Path.cwd(), "../outside", "source_folders")
        self.assertEqual(raised.exception.code, "start_path_invalid")


if __name__ == "__main__":
    unittest.main()
