from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "apex_kb_start.py"
LIFECYCLE = SCRIPT.with_name("apex_kb.py")
SPEC = importlib.util.spec_from_file_location("apex_kb_start_under_test", SCRIPT)
assert SPEC and SPEC.loader
start = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(start)

LIFECYCLE_SPEC = importlib.util.spec_from_file_location("apex_kb_lifecycle_under_test", LIFECYCLE)
assert LIFECYCLE_SPEC and LIFECYCLE_SPEC.loader
lifecycle = importlib.util.module_from_spec(LIFECYCLE_SPEC)
LIFECYCLE_SPEC.loader.exec_module(lifecycle)


class ApexKbStartTests(unittest.TestCase):
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

    def test_worktree_resolution_is_read_only(self):
        responses = {
            ("rev-parse", "--show-toplevel"): subprocess.CompletedProcess([], 0, "/repo\n", ""),
            ("worktree", "list", "--porcelain"): subprocess.CompletedProcess([], 0, "worktree /repo\nHEAD abc123\nbranch refs/heads/main\n\n", ""),
            ("remote", "get-url", "origin"): subprocess.CompletedProcess([], 0, "https://github.com/test/fixture.git\n", ""),
            ("rev-parse", "HEAD"): subprocess.CompletedProcess([], 0, "abc123\n", ""),
        }
        calls = []

        def fake_git(_cwd, *args):
            calls.append(args)
            return responses[args]

        control = mock.Mock()
        control.classify_git_state.return_value = {
            "safe_for_kb_write": True,
            "head": "abc123",
            "classification": "clean",
            "changed_paths": [],
        }
        with mock.patch.object(start, "git", side_effect=fake_git):
            result = start.resolve_primary_worktree(Path("/repo"), "test/fixture", control)
        self.assertEqual(result["policy"], "primary_main_read_only")
        self.assertEqual(result["primary_head"], "abc123")
        self.assertFalse(any(call and call[0] in {"fetch", "pull", "merge"} for call in calls))

    def test_global_flag_normalizer_recognizes_start(self):
        normalized = list(
            lifecycle.normalize_global_flag_placement(
                ["start", "--config", "config.yaml", "--repo-root", "C:/repo", "--json", "--dry-run"]
            )
        )
        self.assertEqual(normalized[:2], ["--json", "--dry-run"])
        self.assertEqual(normalized[2], "start")

    def test_public_start_help_exposes_documented_flags(self):
        completed = subprocess.run(
            [sys.executable, str(LIFECYCLE), "start", "--help"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, f"{completed.stderr}\nSTDOUT:\n{completed.stdout}")
        for flag in ("--config", "--repo-root", "--allow-write", "--dry-run", "--strict", "--json"):
            self.assertIn(flag, completed.stdout)

    @unittest.skipIf(start.yaml is None, "PyYAML unavailable")
    def test_public_start_preview_accepts_post_subcommand_flags_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-b", "main", str(root)], check=True, capture_output=True, text=True)
            subprocess.run(["git", "-C", str(root), "config", "user.email", "test@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name", "Apex KB Test"], check=True)
            subprocess.run(["git", "-C", str(root), "remote", "add", "origin", "https://github.com/test/fixture.git"], check=True)
            (root / "sources").mkdir()
            (root / "sources" / "source.md").write_text("# Fixture Source\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", "."], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-m", "fixture"], check=True, capture_output=True, text=True)
            config = root / "start.yaml"
            config.write_text(
                "repository: test/fixture\n"
                "source_folders:\n  - sources\n"
                "exclusions: []\n"
                "kb_destination:\n  folder: generated-kb\n"
                "topics:\n"
                "  - name: Fixture\n"
                "    phrases: [fixture]\n"
                "    ambiguous_or_negative_terms: []\n"
                "    questions: [\"What is the fixture?\"]\n"
                "run_options:\n"
                "  source_handling: pointer_only\n"
                "  semantic_depth: standard\n"
                "  output: analysis_only\n"
                "  non_text: inventory_and_report\n"
                "  ai_help_after_preflight: false\n",
                encoding="utf-8",
            )
            completed = subprocess.run(
                [
                    sys.executable,
                    str(LIFECYCLE),
                    "start",
                    "--config",
                    str(config),
                    "--repo-root",
                    str(root),
                    "--json",
                    "--dry-run",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, f"{completed.stderr}\nSTDOUT:\n{completed.stdout}")
            payload = json.loads(completed.stdout)
            self.assertEqual(payload["status"], "planned")
            self.assertFalse((root / "generated-kb").exists())


if __name__ == "__main__":
    unittest.main()
