from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "apex_kb_control.py"
SPEC = importlib.util.spec_from_file_location("apex_kb_control_under_test", SCRIPT)
assert SPEC and SPEC.loader
control = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(control)


SEMANTIC_LEDGER_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "apex.kb.semantic-run-ledger.v1",
    "type": "object",
    "required": ["schema", "run_id", "topic_slug", "target_queries", "sources", "page_decisions", "candidate_dispositions", "completion_blockers"],
    "properties": {
        "schema": {"const": "apex.kb.semantic-run-ledger.v1"},
        "run_id": {"type": "string", "minLength": 1},
        "topic_slug": {"type": "string", "minLength": 1},
        "target_queries": {"type": "array"},
        "sources": {"type": "array"},
        "page_decisions": {"type": "array"},
        "candidate_dispositions": {"type": "array"},
        "completion_blockers": {"type": "array"},
    },
    "additionalProperties": True,
}

SEMANTIC_ACCEPTANCE_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "apex.kb.semantic-acceptance.v1",
    "type": "object",
    "required": ["schema", "run_id", "topic_slug", "semantic_contract_version", "evaluator_context", "query_results", "claim_reviews", "repairs", "verdict"],
    "properties": {
        "schema": {"const": "apex.kb.semantic-acceptance.v1"},
        "run_id": {"type": "string"},
        "topic_slug": {"type": "string"},
        "semantic_contract_version": {"const": "2"},
        "evaluator_context": {"type": "string"},
        "query_results": {"type": "array"},
        "claim_reviews": {"type": "array"},
        "repairs": {"type": "array"},
        "verdict": {"enum": ["semantic_pass", "semantic_partial", "semantic_fail", "insufficient_evidence"]},
    },
    "additionalProperties": True,
}


class FakeCore:
    def __init__(self) -> None:
        self.calls: list[str] = []

    def mapping(self):
        return {
            "cmd_scaffold": self.cmd_scaffold,
            "cmd_preflight": self.cmd_preflight,
            "cmd_source_intake": self.cmd_source_intake,
            "cmd_generate_source_payload_manifest": self.cmd_generate_source_payload_manifest,
            "cmd_phase0": self.cmd_phase0,
            "cmd_postflight": self.cmd_postflight,
            "cmd_topic_sanity_check": self.cmd_topic_sanity_check,
            "candidate_disposition_findings": lambda _root: [],
            "_quality_page_metrics": lambda _root, _page: {"repair_reasons": []},
        }

    def _root(self, args):
        return control.resolve_kb_root(args.kb_root)

    def cmd_scaffold(self, args):
        self.calls.append("scaffold")
        root = self._root(args)
        for rel in ["wiki", "raw/notes", "manifests", "semantic-contract", "audit", "ingest-analysis", "log"]:
            (root / rel).mkdir(parents=True, exist_ok=True)
        (root / "README.md").write_text("# Test\n", encoding="utf-8")
        (root / "kb-schema.md").write_text("# Schema\n", encoding="utf-8")
        (root / "wiki/index.md").write_text("# Index\n", encoding="utf-8")
        (root / "raw/notes/source.md").write_text("# Topic\n\nSource evidence.\n", encoding="utf-8")
        manifest = {"schema_version": "1.0", "kb_slug": root.name, "sources": [{"source_id": "source-1", "source_path": "raw/notes/source.md"}]}
        (root / "manifests/source-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        (root / "semantic-contract/semantic-execution-contract.md").write_text("# Contract\n", encoding="utf-8")
        (root / "semantic-contract/phase1-analysis-template.md").write_text("# Phase 1\n", encoding="utf-8")
        (root / "semantic-contract/phase2-wiki-page-templates.md").write_text("# Phase 2\n", encoding="utf-8")
        return {"command": "scaffold", "status": "ok"}

    def cmd_preflight(self, args):
        self.calls.append("preflight")
        return {"command": "preflight", "status": "ok", "checks": {}}

    def cmd_source_intake(self, args):
        self.calls.append("source-intake")
        root = self._root(args)
        manifest_path = root / "manifests/source-manifest.json"
        value = json.loads(manifest_path.read_text(encoding="utf-8"))
        source_id = args.source_id or Path(args.source_path or args.pointer or "source").stem
        if any(item.get("source_id") == source_id for item in value.get("sources", [])):
            return {"command": "source-intake", "status": "blocked", "reason": "source id exists"}
        entry = {
            "source_id": source_id,
            "source_storage_mode": args.storage_mode,
            "source_path": args.pointer or args.source_path,
            "original_source_path": args.source_path or args.pointer,
            "source_hash": "NA",
        }
        value.setdefault("sources", []).append(entry)
        manifest_path.write_text(json.dumps(value), encoding="utf-8")
        return {"command": "source-intake", "status": "ok", "entry": entry}

    def cmd_generate_source_payload_manifest(self, args):
        self.calls.append("payload")
        root = self._root(args)
        value = {"schema": "apex.kb.source-payload-manifest.v1", "aggregate": {"file_count": 1, "sha256": "a" * 64}, "source_groups": []}
        (root / "manifests/source-payload-manifest.json").write_text(json.dumps(value), encoding="utf-8")
        return {"command": "generate-source-payload-manifest", "status": "ok"}

    def cmd_phase0(self, args):
        self.calls.append("phase0")
        root = self._root(args)
        phase0 = root / "manifests/phase0"
        packs = phase0 / "work-packs"
        packs.mkdir(parents=True, exist_ok=True)
        rankings = {"schema": "apex.kb.topic-source-rankings.v2", "topics": {"topic-a": {}}}
        (phase0 / "topic-source-rankings.json").write_text(json.dumps(rankings), encoding="utf-8")
        workpack = {
            "topic_slug": "topic-a",
            "concentrated_candidates": [{"path": "raw/notes/source.md", "source_id": "source-1"}],
            "held_in_custody": [],
        }
        (packs / "topic-a.json").write_text(json.dumps(workpack), encoding="utf-8")
        (packs / "topic-a.md").write_text("# Work Pack\n", encoding="utf-8")
        return {"command": "phase0", "status": "ok"}

    def cmd_postflight(self, args):
        self.calls.append("postflight")
        return {"command": "postflight", "status": "pass"}

    def cmd_topic_sanity_check(self, args):
        self.calls.append("topic-sanity-check")
        return {"command": "topic-sanity-check", "status": "ok", "verdict": "scope_evidence_found", "recommendation": "proceed", "message": "evidence found", "evidence": {}}


class ApexKbControlTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name)
        self.kb_rel = "apex-meta/kb/test-kb"
        self.kb = self.repo / self.kb_rel
        self.kb.mkdir(parents=True)
        self.source_repo = Path(__file__).resolve().parents[3]
        src_skill = self.source_repo / ".claude/skills/apex-kb"
        dst_skill = self.repo / ".claude/skills/apex-kb"
        shutil.copytree(src_skill, dst_skill, dirs_exist_ok=True)
        refs = dst_skill / "references"
        refs.mkdir(parents=True, exist_ok=True)
        (refs / "semantic-run-ledger.schema.json").write_text(json.dumps(SEMANTIC_LEDGER_SCHEMA), encoding="utf-8")
        (refs / "semantic-acceptance.schema.json").write_text(json.dumps(SEMANTIC_ACCEPTANCE_SCHEMA), encoding="utf-8")
        registry = {
            "schema": "apex.kb.topic-registry.v2",
            "topics": [
                {
                    "slug": "topic-a",
                    "name": "Topic A",
                    "phrases": ["topic a"],
                    "aliases": [],
                    "supporting_terms": ["source", "evidence"],
                    "negative_terms": [],
                    "ambiguous_terms": [],
                    "target_page": "wiki/summaries/topic-a.md",
                    "target_queries": [
                        {
                            "query_id": "q1",
                            "priority": "critical",
                            "question": "What is Topic A?",
                            "answer_requirements": ["definition"],
                            "expected_page": "wiki/summaries/topic-a.md#Macro",
                            "raw_source_required": False,
                        }
                    ],
                    "status": "not_started",
                }
            ],
        }
        (self.kb / "manifests").mkdir(parents=True)
        (self.kb / "manifests/topic-registry.json").write_text(json.dumps(registry), encoding="utf-8")
        self.repo_patch = mock.patch.object(control, "repository_root", lambda: self.repo)
        self.repo_patch.start()
        self.core = FakeCore()

    def tearDown(self):
        self.repo_patch.stop()
        self.temp.cleanup()

    def args(self, **updates):
        values = {
            "kb_root": self.kb_rel,
            "allow_write": True,
            "dry_run": False,
            "strict": False,
            "control_action": "init",
            "run_id": "run-001",
            "mode": "compile",
            "operator_intent": "Compile Topic A",
            "kb_identity": "Test KB",
            "source_locus": "Existing source manifest",
            "source_root": [],
            "source_spec": [],
            "out_of_scope": ["unrelated topics"],
            "success_definition": "Accepted Topic A page",
            "output_tier": "query_ready",
            "output_tier_rationale": "Need accepted compiled knowledge and retrieval readiness",
            "execution_route": "terminal_backed",
            "corpus_breadth": "narrow",
            "broad_breadth_reason": None,
            "topic_slug": ["topic-a"],
            "target_repository": "leela-spec/apexai-os-meta",
            "target_commit": None,
            "title": "Test KB",
            "replace_unconfirmed": False,
            "confirmation_quote": "Confirmed: compile Topic A",
            "accept_input_change": False,
            "repo_root": None,
        }
        values.update(updates)
        return SimpleNamespace(**values)

    def init(self):
        return control.control_init(self.args())

    def run_until_phase1_packet(self):
        self.init()
        for expected in ["scaffold", "intent_lock"]:
            result = control.control_run(self.args(control_action="run"), self.core.mapping())
            self.assertEqual(result["stage"], expected)
        confirm = control.control_confirm(self.args(control_action="confirm"))
        self.assertEqual(confirm["status"], "ok")
        for expected in ["preflight", "source_intake", "phase0", "phase1:topic-a"]:
            result = control.control_run(self.args(control_action="run"), self.core.mapping())
            self.assertEqual(result["stage"], expected)
        return control.load_state(self.kb)

    def write_phase1_outputs(self):
        analysis = self.kb / "ingest-analysis/topic-a.analysis.md"
        analysis.parent.mkdir(parents=True, exist_ok=True)
        analysis.write_text(
            """---\nstatus: analysis_complete\n---\n# Topic A Analysis\n\n## Compile Decision\n\n```yaml\nphase_2_ready: true\nproposed_wiki_pages:\n  - wiki/summaries/topic-a.md\n```\n\n## Candidate Dispositions\n\n- destination_page: wiki/summaries/topic-a.md\n""",
            encoding="utf-8",
        )
        ledger = self.kb / "log/semantic-runs/run-001/topics/topic-a.json"
        ledger.parent.mkdir(parents=True, exist_ok=True)
        value = {
            "schema": "apex.kb.semantic-run-ledger.v1",
            "run_id": "run-001",
            "topic_slug": "topic-a",
            "target_queries": [{"query_id": "q1", "status": "answered"}],
            "sources": [],
            "page_decisions": [],
            "candidate_dispositions": [],
            "completion_blockers": [],
        }
        ledger.write_text(json.dumps(value), encoding="utf-8")

    def write_phase2_output(self):
        page = self.kb / "wiki/summaries/topic-a.md"
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text("# Topic A\n\n## Macro\nAnswer.\n\n## Meso\nDefinition.\n\n## Micro\nMechanism.\n", encoding="utf-8")

    def write_acceptance(self, verdict="semantic_pass"):
        path = self.kb / "audit/semantic-acceptance/run-001/topic-a.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        value = {
            "schema": "apex.kb.semantic-acceptance.v1",
            "run_id": "run-001",
            "topic_slug": "topic-a",
            "semantic_contract_version": "2",
            "evaluator_context": "fresh evaluator",
            "query_results": [{"query_id": "q1", "result": "answerable", "page_pointers": ["wiki/summaries/topic-a.md#Macro"]}],
            "claim_reviews": [{"claim_id": "c1", "result": "supported", "page_pointer": "wiki/summaries/topic-a.md#Macro", "source_pointer": "raw/notes/source.md#Topic"}],
            "repairs": [],
            "verdict": verdict,
        }
        path.write_text(json.dumps(value), encoding="utf-8")

    def test_init_is_idempotent_and_state_schema_validates(self):
        first = self.init()
        second = self.init()
        self.assertEqual(first["status"], "ok")
        self.assertEqual(second["next_stage"], "scaffold")
        state = control.load_state(self.kb)
        self.assertEqual(state["schema"], control.RUN_STATE_SCHEMA)
        self.assertEqual(state["revision"], 1)

    def test_direct_mutating_command_is_blocked_for_controlled_run(self):
        self.init()
        guarded = control.guard_direct_command(self.args(command="phase0"))
        self.assertIsNotNone(guarded)
        self.assertEqual(guarded["reason_code"], "direct_command_bypasses_control_plane")

    def test_operator_confirmation_gate_and_illegal_repeat(self):
        self.init()
        control.control_run(self.args(control_action="run"), self.core.mapping())
        waiting = control.control_run(self.args(control_action="run"), self.core.mapping())
        self.assertEqual(waiting["status"], "needs_operator")
        self.assertTrue((self.kb / "log/runs/run-001/operator-readback.md").exists())
        confirmed = control.control_confirm(self.args(control_action="confirm"))
        self.assertEqual(confirmed["next_stage"], "preflight")
        repeated = control.control_confirm(self.args(control_action="confirm"))
        self.assertEqual(repeated["reason_code"], "illegal_transition")

    def test_exact_next_stage_and_power_shell_quoting(self):
        self.init()
        result = control.control_next(self.args(control_action="next"))
        self.assertEqual(result["next_stage"], "scaffold")
        quoted = control.ps_quote(r"C:\GitDev\Apex KB\O'Brien")
        self.assertEqual(quoted, r"'C:\GitDev\Apex KB\O''Brien'")

    def test_phase1_packet_has_exact_output_and_short_trigger(self):
        self.run_until_phase1_packet()
        packet = json.loads((self.kb / "log/runs/run-001/packets/phase1-topic-a.json").read_text(encoding="utf-8"))
        self.assertEqual(packet["exact_output_path"], "ingest-analysis/topic-a.analysis.md")
        self.assertIn("raw/notes/source.md", packet["exact_input_files"])
        self.assertEqual(packet["allowed_writes"], ["ingest-analysis/topic-a.analysis.md", "log/semantic-runs/run-001/topics/topic-a.json"])
        next_result = control.control_next(self.args(control_action="next"))
        self.assertEqual(next_result["status"], "needs_semantic_executor")
        self.assertIn("phase1-topic-a.md", next_result["operator_action"])

    def test_resume_from_files_advances_without_chat_memory(self):
        self.run_until_phase1_packet()
        self.write_phase1_outputs()
        result = control.control_reconcile(self.args(control_action="reconcile"), self.core.mapping())
        self.assertEqual(result["next_stage"], "phase2:topic-a")
        reloaded = control.load_state(self.kb)
        self.assertIn("phase1:topic-a", reloaded["completed_stages"])

    def test_wrong_path_output_is_reason_coded(self):
        self.run_until_phase1_packet()
        wrong = self.kb / "ingest-analysis/wrong/topic-a.analysis.md"
        wrong.parent.mkdir(parents=True)
        wrong.write_text("not the exact path", encoding="utf-8")
        result = control.control_reconcile(self.args(control_action="reconcile"), self.core.mapping())
        self.assertEqual(result["reason_code"], "output_wrong_path")

    def test_independent_semantic_acceptance_is_mandatory(self):
        self.run_until_phase1_packet()
        self.write_phase1_outputs()
        control.control_reconcile(self.args(control_action="reconcile"), self.core.mapping())
        control.control_run(self.args(control_action="run"), self.core.mapping())
        self.write_phase2_output()
        control.control_reconcile(self.args(control_action="reconcile"), self.core.mapping())
        control.control_run(self.args(control_action="run"), self.core.mapping())
        state = control.load_state(self.kb)
        self.assertEqual(state["current_stage"], "semantic_acceptance:topic-a")
        self.write_acceptance(verdict="semantic_fail")
        failed = control.control_reconcile(self.args(control_action="reconcile"), self.core.mapping())
        self.assertEqual(failed["reason_code"], "semantic_acceptance_not_passed")

    def test_query_ready_flow_requires_postflight(self):
        self.run_until_phase1_packet()
        self.write_phase1_outputs()
        control.control_reconcile(self.args(control_action="reconcile"), self.core.mapping())
        control.control_run(self.args(control_action="run"), self.core.mapping())
        self.write_phase2_output()
        control.control_reconcile(self.args(control_action="reconcile"), self.core.mapping())
        control.control_run(self.args(control_action="run"), self.core.mapping())
        self.write_acceptance()
        accepted = control.control_reconcile(self.args(control_action="reconcile"), self.core.mapping())
        self.assertEqual(accepted["next_stage"], "postflight")
        completed = control.control_run(self.args(control_action="run"), self.core.mapping())
        self.assertEqual(completed["stage"], "postflight")
        final = control.control_next(self.args(control_action="next"))
        self.assertEqual(final["stage"], "complete")
        self.assertEqual(control.load_state(self.kb)["truthful_state"], "query_ready")

    def test_input_drift_blocks_then_invalidates_only_downstream(self):
        self.run_until_phase1_packet()
        registry_path = self.kb / "manifests/topic-registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["topics"][0]["supporting_terms"].append("changed")
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        blocked = control.control_status(self.args(control_action="status"))
        self.assertEqual(blocked["reason_code"], "canonical_input_changed")
        repaired = control.control_reconcile(self.args(control_action="reconcile", accept_input_change=True), self.core.mapping())
        self.assertEqual(repaired["next_stage"], "phase0")
        state = control.load_state(self.kb)
        self.assertIn("source_intake", state["completed_stages"])
        self.assertNotIn("phase0", state["completed_stages"])

    def test_same_run_id_with_changed_configuration_is_blocked(self):
        self.init()
        changed = control.control_init(self.args(operator_intent="Different intent"))
        self.assertEqual(changed["reason_code"], "run_init_mismatch")

    def test_scaffold_mode_stops_after_confirmation(self):
        first = control.control_init(
            self.args(
                mode="scaffold",
                output_tier="source_only",
                output_tier_rationale="Create only the controlled KB skeleton",
                topic_slug=[],
            )
        )
        self.assertEqual(first["next_stage"], "scaffold")
        control.control_run(self.args(control_action="run"), self.core.mapping())
        control.control_run(self.args(control_action="run"), self.core.mapping())
        confirmed = control.control_confirm(self.args(control_action="confirm"))
        self.assertIsNone(confirmed["next_stage"])
        self.assertEqual(control.load_state(self.kb)["truthful_state"], "source_only_complete")

    def test_packet_input_change_requires_fresh_packet(self):
        self.run_until_phase1_packet()
        contract = self.kb / "semantic-contract/semantic-execution-contract.md"
        contract.write_text("# Changed Contract\n", encoding="utf-8")
        self.write_phase1_outputs()
        result = control.control_reconcile(self.args(control_action="reconcile"), self.core.mapping())
        self.assertEqual(result["reason_code"], "packet_input_changed")

    def test_rankings_change_invalidates_all_semantic_topics(self):
        self.run_until_phase1_packet()
        self.write_phase1_outputs()
        control.control_reconcile(self.args(control_action="reconcile"), self.core.mapping())
        rankings = self.kb / "manifests/phase0/topic-source-rankings.json"
        value = json.loads(rankings.read_text(encoding="utf-8"))
        value["changed"] = True
        rankings.write_text(json.dumps(value), encoding="utf-8")
        blocked = control.control_reconcile(self.args(control_action="reconcile"), self.core.mapping())
        self.assertEqual(blocked["reason_code"], "canonical_input_changed")
        repaired = control.control_reconcile(
            self.args(control_action="reconcile", accept_input_change=True), self.core.mapping()
        )
        self.assertEqual(repaired["next_stage"], "phase1:topic-a")
        self.assertNotIn("phase1:topic-a", control.load_state(self.kb)["completed_stages"])

    def test_interrupted_source_intake_resumes_idempotently(self):
        pointer_spec = json.dumps(
            {
                "pointer": "repo/path/source.md",
                "storage_mode": "pointer_only",
                "source_type": "note",
                "source_id": "pointer-source",
            }
        )
        control.control_init(self.args(source_spec=[pointer_spec]))
        control.control_run(self.args(control_action="run"), self.core.mapping())
        control.control_run(self.args(control_action="run"), self.core.mapping())
        control.control_confirm(self.args(control_action="confirm"))
        control.control_run(self.args(control_action="run"), self.core.mapping())
        state = control.load_state(self.kb)
        spec = state["source_inputs"][0]
        fake_args = control._core_args(
            state,
            self.args(),
            pointer=spec["pointer"],
            storage_mode=spec["storage_mode"],
            source_type=spec["source_type"],
            source_id=spec["source_id"],
        )
        self.core.cmd_source_intake(fake_args)
        before = self.core.calls.count("source-intake")
        resumed = control.control_run(self.args(control_action="run"), self.core.mapping())
        after = self.core.calls.count("source-intake")
        self.assertEqual(resumed["stage"], "source_intake")
        self.assertEqual(before, after)

    def test_target_commit_mismatch_blocks_before_stage_execution(self):
        control.control_init(self.args(target_commit="deadbeef"))
        result = control.control_run(self.args(control_action="run"), self.core.mapping())
        self.assertEqual(result["reason_code"], "target_commit_mismatch")
        self.assertNotIn("scaffold", self.core.calls)

    def test_git_classifier_is_read_only_and_reports_clean_or_dirty(self):
        try:
            subprocess.run(["git", "init", str(self.repo)], capture_output=True, check=True)
        except (OSError, subprocess.CalledProcessError):
            self.skipTest("git not available")
        value = control.classify_git_state(self.kb)
        self.assertIn(value["classification"], {"dirty", "clean_no_upstream", "clean_synced"})
        self.assertIn("safe_for_kb_write", value)

    def test_nested_control_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--kb-root", required=True)
        sub = parser.add_subparsers(dest="command", required=True)
        control_parser = sub.add_parser("control")
        control.configure_parser(control_parser)
        parsed = parser.parse_args(["--kb-root", self.kb_rel, "control", "next"])
        self.assertEqual(parsed.control_action, "next")


if __name__ == "__main__":
    unittest.main()
