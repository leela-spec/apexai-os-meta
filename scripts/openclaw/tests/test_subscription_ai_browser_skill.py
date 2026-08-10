from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
SKILL_ROOT = REPO_ROOT / "apex-meta" / "openclaw" / "skills" / "subscription-ai-browser"


class SubscriptionAiBrowserSkillTests(unittest.TestCase):
    def test_skill_is_closed_world_and_routes_each_provider(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("apex.execution-request/v2", skill)
        self.assertIn("Never infer, improve, or substitute", skill)
        self.assertIn("exactly one shared browser tab", skill)
        for provider in ("chatgpt", "perplexity", "gemini"):
            self.assertIn(f"references/{provider}.md", skill)
            self.assertTrue((SKILL_ROOT / "references" / f"{provider}.md").is_file())

    def test_perplexity_requires_joint_setting_verification(self) -> None:
        procedure = (SKILL_ROOT / "references" / "perplexity.md").read_text(encoding="utf-8")
        self.assertIn("native browser `type` action", procedure)
        self.assertIn("Never use browser JavaScript evaluation", procedure)
        self.assertNotIn("document.execCommand", procedure)
        self.assertIn("hidden model control", procedure)
        self.assertIn("combined state cannot be verified, stop", procedure)


if __name__ == "__main__":
    unittest.main()
