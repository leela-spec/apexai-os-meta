from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
SKILL_ROOT = REPO_ROOT / "apex-meta" / "openclaw" / "skills" / "subscription-ai-browser"
OPENCLAW_TEMPLATE = REPO_ROOT / "apex-meta" / "openclaw" / "openclaw.json"
FLOW_SKILL = REPO_ROOT / "apex-meta" / "openclaw" / "skills" / "apex-flow-executor" / "SKILL.md"
DISPATCHER = REPO_ROOT / "scripts" / "openclaw" / "dispatch-execution-request.ps1"


class SubscriptionAiBrowserSkillTests(unittest.TestCase):
    def test_skill_is_closed_world_and_routes_each_provider(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("apex.execution-request/v2", skill)
        self.assertIn("Never infer, improve, or substitute", skill)
        # The managed browser keeps one tab per provider, so the skill selects the
        # tab matching the declared hostname rather than requiring a single shared tab.
        self.assertIn("hostname matches the declared", skill)
        # Refs must come from a fresh snapshot; guessed refs were a real failure mode.
        self.assertIn("Copy a ref **verbatim**", skill)
        # Fabricating an answer instead of reading it from the page is a failure.
        self.assertIn("Never report an answer you did not read", skill)
        for provider in ("chatgpt", "perplexity", "gemini"):
            self.assertIn(f"references/{provider}.md", skill)
            self.assertTrue((SKILL_ROOT / "references" / f"{provider}.md").is_file())

    def test_flow_executor_consumes_execution_request_v2_not_legacy_packet_fields(self) -> None:
        flow_skill = FLOW_SKILL.read_text(encoding="utf-8")
        self.assertIn("apex.execution-request/v2", flow_skill)
        self.assertIn("prompt_ref", flow_skill)
        self.assertIn("result_path", flow_skill)
        self.assertIn("evidence_dir", flow_skill)
        self.assertIn("apex.executor-receipt/v1", flow_skill)
        self.assertIn("prompt_sha256", flow_skill)
        self.assertIn("browser_profile", flow_skill)
        self.assertIn("reasoning_mode", flow_skill)
        self.assertNotIn("prompt_body_path", flow_skill)
        self.assertNotIn("capture_path", flow_skill)
        self.assertNotIn("verification_prompt_path", flow_skill)

    def test_perplexity_requires_joint_setting_verification(self) -> None:
        procedure = (SKILL_ROOT / "references" / "perplexity.md").read_text(encoding="utf-8")
        self.assertIn("#ask-input", procedure)
        self.assertIn("Never use browser JavaScript evaluation", procedure)
        self.assertNotIn("document.execCommand", procedure)
        self.assertIn("hidden model control", procedure)
        self.assertIn("combined state cannot be verified, stop", procedure)

    def test_chatgpt_uses_installed_managed_browser_action_contract(self) -> None:
        procedure = (SKILL_ROOT / "references" / "chatgpt.md").read_text(encoding="utf-8")
        self.assertNotIn("exactly one shared tab", procedure)
        self.assertIn("hostname is `chatgpt.com`", procedure)
        self.assertIn("open `https://chatgpt.com/`", procedure)
        self.assertIn('"kind": "type"', procedure)
        self.assertIn('"ref": "<fresh composer ref>"', procedure)
        self.assertIn('"text": "<exact prompt>"', procedure)
        self.assertIn('"kind": "press", "key": "Enter"', procedure)
        self.assertIn("fresh snapshot before retrying", procedure)
        self.assertIn("never submit the prompt twice", procedure)

    def test_repo_template_matches_cloud_first_pilot_topology(self) -> None:
        template = OPENCLAW_TEMPLATE.read_text(encoding="utf-8")
        self.assertIn('defaultProfile: "openclaw"', template)
        self.assertIn('snapshotDefaults: { mode: "efficient" }', template)
        self.assertIn('model: "openai/gpt-4.1-nano"', template)
        self.assertIn('thinkingDefault: "medium"', template)
        self.assertIn('reasoningDefault: "on"', template)
        self.assertIn('contextTokens: 32768', template)
        self.assertIn('contextWindow: 32768', template)
        self.assertIn('timeoutSeconds: 600', template)
        self.assertIn('"openai"', template)
        self.assertIn('"apex-browser-policy": {\n        enabled: false,', template)

    def test_managed_browser_can_open_the_declared_provider_tab(self) -> None:
        dispatcher = DISPATCHER.read_text(encoding="utf-8")
        self.assertNotIn("New-BrowserPolicy -Request", dispatcher)
        self.assertNotIn("apex-browser-policy is not enabled", dispatcher)
        self.assertNotIn("--thinking off", dispatcher)
        self.assertIn("--timeout 600", dispatcher)
        self.assertIn("Join-Path $PSScriptRoot 'validate-execution-request.py'", dispatcher)
        self.assertNotIn("Resolve-ProtectedValidator", dispatcher)
        self.assertIn("'openai/gpt-4.1-nano', 'apex-local/qwen3-8b-q4km'", dispatcher)
        self.assertIn("--model $ExecutorModel", dispatcher)
        self.assertIn("- Executor model: $ExecutorModel", dispatcher)
        self.assertIn("executor-receipt.json", dispatcher)
        self.assertIn("verified-receipt.json", dispatcher)
        self.assertIn("CloudControlReceiptPath", dispatcher)

        flow_skill = FLOW_SKILL.read_text(encoding="utf-8")
        self.assertIn("open the declared provider URL", flow_skill)

        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("open one at the declared provider URL", skill)
        self.assertNotIn("declared_provider_tab_unavailable", skill)


if __name__ == "__main__":
    unittest.main()
