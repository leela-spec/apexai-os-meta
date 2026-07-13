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
        "allow_write": False,
        "dry_run": False,
        "strict": False,
        "json": True,
        "output_json": None,
        "init": False,
        "title": "Semantic Fixture",
        "topic_title": None,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class SemanticValueContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.kb = Path(self.temp.name) / "semantic-fixture"
        (self.kb / "manifests").mkdir(parents=True)
        (self.kb / "wiki" / "summaries").mkdir(parents=True)
        (self.kb / "ingest-analysis").mkdir(parents=True)
        (self.kb / "audit" / "semantic-acceptance" / "run-1").mkdir(parents=True)
        (self.kb / "outputs" / "queries" / "evals").mkdir(parents=True)
        (self.kb / "manifests" / "source-manifest.json").write_text(
            json.dumps({"schema_version": "1.0", "kb_slug": self.kb.name, "sources": [{"source_id": "source-1"}]}),
            encoding="utf-8",
        )
        self.registry = {
            "schema": "apex.kb.topic-registry.v2",
            "topics": [
                {
                    "name": "Topic One",
                    "slug": "topic-one",
                    "status": "draft",
                    "target_page": "wiki/summaries/topic-one.md",
                    "target_queries": [
                        {
                            "query_id": "topic-one-q1",
                            "question": "What is the exact contract?",
                            "priority": "critical",
                            "answer_requirements": ["fields", "rules"],
                            "expected_page": "wiki/summaries/topic-one.md",
                        }
                    ],
                }
            ],
        }
        (self.kb / "manifests" / "topic-registry.json").write_text(json.dumps(self.registry), encoding="utf-8")
        (self.kb / "ingest-analysis" / "source-1.analysis.md").write_text(
            "# Analysis\n\nsource-1\n\nconcept_candidates: []\nentity_candidates: []\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp.cleanup()

    def write_page(self, *, query_ids=True, unopened=False, contract="2"):
        trigger = (
            '- id: U001\n  availability_class: "readable_unopened"\n  completion_effect: "blocks_priority_query"'
            if unopened
            else "uncertainty_triggers: []"
        )
        target_ids = '["topic-one-q1"]' if query_ids else "[]"
        text = f'''---
title: "Topic One"
page_type: summary
kb_slug: "{self.kb.name}"
semantic_contract_version: "{contract}"
semantic_run_id: "run-1"
target_query_ids: {target_ids}
source_refs:
  - source_id: "source-1"
created_at: "2026-07-13T00:00:00Z"
updated_at: "2026-07-13T00:00:00Z"
confidence: high
claim_label: source_backed_summary
status: active
---
# Topic One

## Target Questions Answered

topic-one-q1: The contract has fields and rules.

## Adaptive Ranked Source Set

- source_id: source-1
  analysis_ref: ingest-analysis/source-1.analysis.md
  reviewed_status: complete
  supported_query_ids: [topic-one-q1]
  claim_ids: [C001, C002]

## Macro / Meso / Micro

### Macro
The contract governs the domain with source-grounded constraints and durable routes for future retrieval.
### Meso
Fields and rules are linked into one workflow and retain their authority boundary across related operations.
### Micro
The exact fixture field and rule are supported by source-1 section Contract and its resolved evidence passage.

## Key Claims

- claim_id: C001
  claim: The contract has fields.
  source_pointer: source-1#Contract
- claim_id: C002
  claim: The contract has rules.
  source_pointer: source-1#Rules

## Routes Here

- question: What is the exact contract?
  leads_to: wiki/summaries/topic-one.md#target-questions-answered

## Uncertainty / Raw Source Reopen Triggers

{trigger}
'''
        path = self.kb / "wiki" / "summaries" / "topic-one.md"
        path.write_text(text, encoding="utf-8")
        return path

    def write_acceptance(self, verdict="semantic_pass", query_result="answerable", claim_result="supported"):
        artifact = {
            "schema": "apex.kb.semantic-acceptance.v1",
            "run_id": "run-1",
            "topic_slug": "topic-one",
            "semantic_contract_version": "2",
            "evaluator_context": "clean-context fixture",
            "query_results": [
                {
                    "query_id": "topic-one-q1",
                    "result": query_result,
                    "page_pointers": ["wiki/summaries/topic-one.md#target-questions-answered"],
                }
            ],
            "claim_reviews": [
                {
                    "claim_id": "C001",
                    "result": claim_result,
                    "page_pointer": "wiki/summaries/topic-one.md#key-claims",
                    "source_pointer": "raw/source.md#Contract",
                }
            ],
            "repairs": [],
            "verdict": verdict,
        }
        (self.kb / "audit" / "semantic-acceptance" / "run-1" / "topic-one.json").write_text(json.dumps(artifact), encoding="utf-8")

    def test_query_eval_v2_initializes_from_registry(self):
        result = apex_kb.cmd_query_eval(args(self.kb, allow_write=True, init=True))
        self.assertEqual(result["schema"], "apex.query_eval_pack.v2")
        self.assertEqual(result["query_count"], 1)
        pack = json.loads((self.kb / "outputs" / "queries" / "evals" / "query-eval-pack.json").read_text(encoding="utf-8"))
        self.assertEqual(pack["queries"][0]["query_id"], "topic-one-q1")

    def test_missing_queries_and_readable_unopened_are_reason_coded(self):
        page = self.write_page(query_ids=False, unopened=True)
        metrics = apex_kb._quality_page_metrics(self.kb, page)
        self.assertIn("missing_target_queries", metrics["repair_reasons"])
        self.assertIn("readable_unopened_source_blocks_completion", metrics["repair_reasons"])

    def test_legacy_page_is_readable_but_not_promoted(self):
        page = self.write_page(contract="1")
        metrics = apex_kb._quality_page_metrics(self.kb, page)
        self.assertIn("legacy_semantic_contract", metrics["repair_reasons"])

    def test_human_readable_v2_evidence_wiring_is_recognized(self):
        page = self.write_page(contract="2.0")
        text = page.read_text(encoding="utf-8")
        text = text.replace(
            "- source_id: source-1\n"
            "  analysis_ref: ingest-analysis/source-1.analysis.md\n"
            "  reviewed_status: complete\n"
            "  supported_query_ids: [topic-one-q1]\n"
            "  claim_ids: [C001, C002]",
            "- **source-1** — fully reviewed; analysis ingest-analysis/source-1.analysis.md; "
            "supports topic-one-q1 and claims TOP-C001–C002.",
        )
        text = text.replace(
            "- claim_id: C001\n"
            "  claim: The contract has fields.\n"
            "  source_pointer: source-1#Contract\n"
            "- claim_id: C002\n"
            "  claim: The contract has rules.\n"
            "  source_pointer: source-1#Rules",
            "- **TOP-C001:** The contract has fields. (SRC-source-1, Contract)\n"
            "- **TOP-C002:** The contract has rules. (SRC-source-1, Rules)",
        )
        text = text.replace(
            "- question: What is the exact contract?\n"
            "  leads_to: wiki/summaries/topic-one.md#target-questions-answered",
            "See [Topic One](topic-one.md#target-questions-answered).",
        )
        page.write_text(text, encoding="utf-8")
        metrics = apex_kb._quality_page_metrics(self.kb, page)
        self.assertEqual(metrics["target_query_ids"], ["topic-one-q1"])
        self.assertEqual(metrics["key_claim_count"], 2)
        self.assertEqual(metrics["ranked_source_count"], 1)
        self.assertEqual(metrics["route_count"], 1)
        self.assertNotIn("legacy_semantic_contract", metrics["repair_reasons"])
        self.assertNotIn("no_key_claims", metrics["repair_reasons"])
        self.assertNotIn("no_query_routes", metrics["repair_reasons"])

    def test_semantic_acceptance_requires_answerable_queries_and_supported_claims(self):
        self.write_page()
        self.assertEqual(apex_kb.semantic_acceptance_status(self.kb)["status"], "missing")
        self.write_acceptance()
        self.assertEqual(apex_kb.semantic_acceptance_status(self.kb)["status"], "pass")
        self.write_acceptance(verdict="semantic_partial", query_result="partial")
        self.assertEqual(apex_kb.semantic_acceptance_status(self.kb)["status"], "partial")

    def test_missing_candidate_disposition_is_detected(self):
        (self.kb / "ingest-analysis" / "candidate.analysis.md").write_text(
            "# Analysis\n\nconcept_candidates:\n  - concept_slug: missing-disposition\n",
            encoding="utf-8",
        )
        findings = apex_kb.candidate_disposition_findings(self.kb)
        self.assertTrue(any(item["reason"] == "candidate_promotion_disposition_missing" for item in findings))

    def test_scaffold_copies_repository_local_contract(self):
        other = Path(self.temp.name) / "new-kb"
        result = apex_kb.cmd_scaffold(args(other, allow_write=True))
        self.assertTrue((other / "semantic-contract" / "semantic-execution-contract.md").exists())
        self.assertTrue((other / "semantic-contract" / "phase1-analysis-template.md").exists())
        self.assertTrue(any(item.get("written") for item in result["semantic_contract"]))

    def test_source_only_scaffold_does_not_require_semantic_acceptance(self):
        other = Path(self.temp.name) / "source-only-kb"
        apex_kb.cmd_scaffold(args(other, allow_write=True))
        report = apex_kb.quality_report(other)
        self.assertFalse(any(item.get("reason") == "semantic_acceptance_missing" for item in report["global_findings"]))


if __name__ == "__main__":
    unittest.main()
