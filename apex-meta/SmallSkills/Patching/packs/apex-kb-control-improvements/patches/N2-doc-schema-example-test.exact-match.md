# N2 - Anti-drift doc/schema example exact-match replacements

Adds the `<!-- schema: <name> -->` marker convention and one concrete, schema-conformant
worked example, so `test_doc_schema_examples.py` (new file, this module) has something real to
validate. This is the direct fix for the confirmed incident where a prior run's semantic
acceptance JSON used `semantic_run_id`/`review_mode`/`verdict: "answerable"`/
`material_claim_verifications` -- a shape that looked plausible but did not match
`semantic-acceptance.schema.json` (which requires `run_id`/`evaluator_context`/`result`/
`claim_reviews`). M4 of the installed control-plane pack already removed the drifted embedded
example from `semantic-value-contract.md` in favor of prose-only schema references; this module
adds the marker convention so a *future* concrete example cannot silently drift again without a
test failing.

Every `<old>` block was copied from the live baseline at commit `878839459ff8430c8bbfd3e8c52a4753794f1c56` (see
`package-manifest.json`).

<file>C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\references\acceptance-tests.md</file>
<old>
Pass criteria:
- the thin page is named in `phase2_repair_candidates` with its actual reason codes on the first check;
- redrafting using those exact reason codes and rechecking clears the page within the 2-retry bound described in `SKILL.md`;
- a page deliberately left thin through both retries is not silently accepted -- it must be flagged as an audit item with residual reason codes and the batch capped at `partial`, never promoted to a passing state;
- `phase2_repair_candidates`/`shell_page_candidates` empty for a page is required for that page to count as done; heading presence alone (`missing_phase2_value_sections` empty) is confirmed insufficient by re-running this fixture with a page that has every heading but fails on `thin_macro_meso_micro` or `single_claim_summary` instead.
</old>
<new>
Pass criteria:
- the thin page is named in `phase2_repair_candidates` with its actual reason codes on the first check;
- redrafting using those exact reason codes and rechecking clears the page within the 2-retry bound described in `SKILL.md`;
- a page deliberately left thin through both retries is not silently accepted -- it must be flagged as an audit item with residual reason codes and the batch capped at `partial`, never promoted to a passing state;
- `phase2_repair_candidates`/`shell_page_candidates` empty for a page is required for that page to count as done; heading presence alone (`missing_phase2_value_sections` empty) is confirmed insufficient by re-running this fixture with a page that has every heading but fails on `thin_macro_meso_micro` or `single_claim_summary` instead.

## Semantic acceptance artifact worked example

A fenced block immediately preceded by an HTML comment `<!-- schema: <schema-file-name> -->`
is a concrete, schema-conformant instance, not a placeholder template. `test_doc_schema_examples.py`
validates every such block against the named schema on every test run, so this example cannot
drift from `semantic-acceptance.schema.json` the way a prior run's output once silently did.

<!-- schema: semantic-acceptance.schema.json -->
```json
{
  "schema": "apex.kb.semantic-acceptance.v1",
  "run_id": "run-2026-07-17-example",
  "topic_slug": "example-topic",
  "semantic_contract_version": "2",
  "evaluator_context": "clean-context evaluator; no drafting rationale or self-assessment supplied",
  "query_results": [
    {"query_id": "example-topic-q1", "result": "answerable", "page_pointers": ["wiki/summaries/example-topic.md#target-questions-answered"]}
  ],
  "claim_reviews": [
    {"claim_id": "C001", "result": "supported", "page_pointer": "wiki/summaries/example-topic.md#key-claims", "source_pointer": "raw/example-source.md#Section"}
  ],
  "repairs": [],
  "verdict": "semantic_pass"
}
```
</new>
