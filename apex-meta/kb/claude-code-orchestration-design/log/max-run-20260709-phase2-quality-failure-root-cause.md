# Max Run 20260709 Phase 2 Quality Failure Root Cause

```yaml
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
report_type: phase2_quality_failure_root_cause
status: completed_with_root_cause
created_at: 2026-07-10T00:00:00Z
repository: leela-spec/apexai-os-meta
branch: main
```

## Executive Finding

The Phase 2 quality fix partially landed in the repository as contracts, scripts, and deterministic quality/coverage surfaces, but it did not operationally govern the max-run LLM compile. The max-run Phase 2 pages satisfy the visible section-heading contract, but they do not satisfy the intended operator value: dense, source-grounded, query-useful pages.

The root cause is not a single hallucination. It is a chain failure:

```yaml
root_cause_chain:
  - contract_patch_landed_as_structure_and_report_surfaces
  - max_run_generation_optimized_for_file_creation_under_connector_limits
  - deterministic_quality_command_was_not_run_after_generation
  - quality_command_itself_is_structural_not_semantic
  - shell_page_heuristic_is_too_weak_for_pages_with_headings_and_source_refs
  - github_connector_write_limits_encouraged compressed pages and one-file commits
  - final_validation_checked existence/headings/readback, not depth/evidence density
```

## What the Patch Plan Actually Required

The closure patch plan explicitly identified the same failure mode before this run: Apex could pass structural lint while still producing low-value wiki pages.

```yaml
patch_plan_quality_problem:
  issue: "Quality / coverage command"
  consequence: "Apex can pass structural lint while still producing low-value wiki pages."
  required_fix:
    - deterministic source-to-page coverage
    - page-to-source map
    - shell-page density
    - claim-pointer density
    - repair candidate list
```

The patch plan also said existing-page repair must depend on quality output and must produce targeted later LLM repair candidates, not blind rewrites.

```yaml
intended_repair_flow:
  quality_command: first
  existing_page_repair_flow: second
  repair_should_be: candidate_driven
  output_expected:
    - phase2_repair_candidates
    - low_value_page_backlog
```

## What Landed in Code

The script includes a `quality_report` / `cmd_quality` implementation. It computes:

```yaml
implemented_quality_fields:
  - source_to_page_map
  - page_to_source_map
  - unmanifested_source_refs
  - manifest_sources_without_pages
  - pages_without_source_refs
  - pages_missing_phase2_value_sections
  - phase2_repair_candidates
  - shell_page_candidates
  - deterministic_only
```

The code also exposes `cmd_quality`, and strict mode fails only if `phase2_repair_candidates` or `shell_page_candidates` are present.

## Why the Max-Run Thin Pages Escaped

### RC1 — The quality command was not executed after the LLM wrote pages

The previous execution did not run the live terminal command:

```bash
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design quality --json --strict
```

It also did not run index, retrieval rebuild, stale, status, or lint in a live worktree. Connector read-back confirmed files and headings, but did not execute the deterministic quality gate.

```yaml
impact:
  quality_gate_effect: not_applied
  repair_candidates_generated: no
  page_density_detected_by_script: no
  operator_received: readback_validation_instead_of_quality_validation
```

### RC2 — The implemented quality heuristic is structural and too permissive

The script defines low density thresholds:

```yaml
shell_page_thresholds:
  SHELL_PAGE_MIN_WORDS: 40
  SHELL_PAGE_MIN_CHARS: 200
```

But a page is marked as a shell candidate only when it is low density and also lacks at least one structural anchor:

```yaml
shell_candidate_condition:
  low_density: true
  and_one_of:
    - no_source_refs
    - missing_Key_Claims
    - missing_Macro_Meso_Micro
```

The max-run pages generally include `source_refs`, `Key Claims`, and `Macro / Meso / Micro`. Therefore, a very small page with all headings and one source pointer can avoid `shell_page_candidates` even when it is not a useful compiled page.

```yaml
failure_pattern:
  page_has_required_headings: true
  page_has_source_refs: true
  page_has_key_claims_heading: true
  page_has_macro_meso_micro_heading: true
  semantic_density: thin
  quality_command_likely_result: not_flagged_as_shell_page
```

### RC3 — The Phase 2 value contract was interpreted as a heading contract during execution

The KB contract says the Phase 2 sections must contain adaptive source ranking, layered synthesis, specific source-backed claims, routes, and uncertainty/reopen triggers. However, deterministic lint checks currently verify mainly whether the headings are present. This allows a page to pass the visible contract while failing the intended value contract.

```yaml
contract_intent:
  Adaptive Ranked Source Set: ranked sources with rationale and coverage
  Macro_Meso_Micro: layered synthesis with specific details anchored by source pointers
  Key Claims: specific claims with pointers, confidence, labels
  Routes Here: usable query routing examples and related links
  Uncertainty: contradictions/open questions with source pointers and handling

execution_result:
  headings_present: yes
  section_depth: shallow
  claim_count: often_one
  raw_pointer_specificity: mostly_file_level
  line_level_or_span_level_evidence: absent
```

### RC4 — GitHub connector execution biased toward compressed one-shot page creation

The GitHub connector can create/update files, but it does not run local commands. In this run, it also forced practical compression because large writes and repeated long content became fragile. One attempted larger file-write/update path was blocked, and the workaround was smaller pages and many independent commits.

```yaml
connector_effect:
  can_write_files: true
  can_fetch_readback: true
  cannot_run_python_postflight: true
  cannot_execute_quality_command: true
  large_content_fragility: high
  operational_bias: shorter_pages_and_many_single_file_commits
```

This is an operations failure: the connector was used for semantic page creation and file writes, but the quality system depended on a terminal postflight that the connector could not perform.

### RC5 — The max-run task treated artifact count as the main completion pressure

The max-run created many Phase 1 and Phase 2 files. The operational pressure became: write the requested file set, avoid old-output overwrite, keep all pages under the KB root, and read back representative pages. That caused the quality target to collapse into structural compliance.

```yaml
observed_completion_proxy:
  - file exists
  - commit succeeded
  - frontmatter exists
  - required headings exist
  - representative pages read back

missing_completion_proxy:
  - source_to_page coverage report run
  - shell_page_candidates reviewed
  - phase2_repair_candidates reviewed
  - claim pointer density checked
  - source diversity checked per page
  - query route usefulness tested
```

### RC6 — The existing-page repair flow did not run

The patch plan specifically says existing-page repair should be candidate-driven and should depend on the quality command. That did not happen. No repair-plan file was generated from quality output before or after Phase 2 page creation.

```yaml
missing_repair_loop:
  expected:
    - run quality
    - inspect phase2_repair_candidates
    - create repair plan
    - rerun only selected pages
    - rerun quality
  actual:
    - write pages
    - read back representative files
    - search headings
    - mark postflight required
```

## Concrete Example: Thin Page That Looks Structurally Valid

The `claude-code-mechanism-decision-model.md` page includes required headings, ranked sources, Macro/Meso/Micro, one key claim, route, and uncertainty trigger. Structurally it looks valid. But the actual synthesis is very short: the macro layer is one sentence, the meso layer is one sentence, and the micro layer is one sentence. The key claims section contains one claim.

```yaml
example_page: wiki/summaries/max-run-20260709/claude-code-mechanism-decision-model.md
structural_status:
  source_refs: present
  required_headings: present
  key_claims: present
quality_problem:
  macro_depth: one_sentence
  meso_depth: one_sentence
  micro_depth: one_sentence
  claim_count: one
  line_level_source_evidence: absent
  query_usefulness: limited
```

The `phase2-value-contract.md` page explicitly says: "This max-run intentionally writes smaller pages, but every Phase 2 page includes the mandatory headings." That is the smoking gun: the run optimized for mandatory headings, not the full quality outcome.

## Responsibility Split

```yaml
operations_failure:
  - used GitHub connector for a workflow that required terminal quality/postflight execution
  - allowed one-file-per-commit direct writes to main
  - did not stop after recognizing page compression risk
  - did not downgrade status early enough from completed to partial-quality compile

process_failure:
  - quality command was report-only by default
  - strict quality gate was not made mandatory before promotion
  - existing-page repair flow was specified but not operationally invoked
  - acceptance tests validate a known shell page but do not force realistic density for structurally complete pages

script_failure:
  - shell_page_candidate heuristic misses pages that have headings/source_refs but little substance
  - phase2_repair_candidates only catches missing headings or missing source refs
  - no deterministic minimum claim count per page type
  - no deterministic source pointer density metric
  - no line/span pointer requirement
  - no section word-count/claim-count report for value sections

connector_limitation:
  - GitHub connector cannot run scripts
  - GitHub connector readback is not validation
  - content-size / tool safety limits incentivized page compression
  - create/update contents API creates many commits unless tree/blob commit flow is used

llm_execution_failure:
  - interpreted the contract too literally as headings-plus-short-content
  - did not preserve the operator's deeper intent: actual useful Phase 2 pages
  - over-prioritized completing the file list under constraints
```

## Why This Happened Again Despite the Day of Work

The day of work improved the repository process artifacts, but the max-run did not execute the full lifecycle those artifacts describe. The repair work created a better gate, but the gate was not placed in the critical path of this GitHub-connector run.

```yaml
why_it_repeated:
  old_failure: "pages can structurally exist while being low value"
  intended_fix: "quality/coverage + repair candidate flow"
  actual_run_gap: "quality/coverage was not run and not enforced"
  deeper_gap: "quality/coverage cannot yet detect thin-but-structurally-complete pages"
```

## Required Fixes Before Repeating Phase 2

### Fix 1 — Make quality mandatory before any success claim

```yaml
policy_change:
  before_claiming_phase2_success_must_run:
    - quality --json --strict
    - lint --json --strict
    - status --json
    - retrieval stale check
  connector_only_allowed_status: partial_unvalidated_compile
```

### Fix 2 — Strengthen deterministic quality metrics

Add report fields:

```yaml
required_new_quality_fields:
  - section_word_counts_by_page
  - key_claim_count_by_page
  - source_pointer_count_by_page
  - raw_source_pointer_specificity
  - ranked_source_count_by_page
  - route_count_by_page
  - uncertainty_count_by_page
  - pages_with_only_file_level_pointers
  - pages_with_single_claim
  - pages_with_micro_layer_under_threshold
```

Add repair-candidate criteria:

```yaml
new_repair_candidate_rules:
  - page_has_required_headings_but_total_body_under_threshold
  - page_has_required_headings_but_key_claim_count_below_minimum
  - page_has_required_headings_but_no_line_or_section_pointers
  - page_has_required_headings_but_macro_meso_micro_each_under_threshold
  - page_has_ranked_sources_but_only_one_real_source_for_broad_topic
```

### Fix 3 — Separate connector write mode from terminal validation mode

```yaml
execution_rule:
  github_connector_mode:
    allowed:
      - create draft semantic artifacts
      - write audit reports
      - read back exact files
    forbidden_success_claims:
      - query_ready
      - quality_validated
      - lint_clean
      - postflight_complete
  terminal_mode_required_for:
    - quality
    - lint
    - index rebuild
    - retrieval rebuild
    - stale check
    - source-payload-manifest regeneration
```

### Fix 4 — Rerun only high-value pages after deterministic quality repair

```yaml
recommended_repair_order:
  - fix source-payload-manifest
  - run quality and capture output
  - patch quality command to catch thin-but-structurally-complete pages
  - rerun quality
  - generate phase2 repair candidate list
  - rewrite selected pages with deeper source grounding
  - rerun quality/lint/status/retrieval
```

## Final Diagnosis

```yaml
verdict: process_landed_but_was_not_enforced
primary_cause: operational_execution_bypassed_quality_gate
secondary_cause: quality_gate_too_structural_to_catch_heading_complete_thin_pages
tertiary_cause: github_connector_cannot_execute_required_deterministic_postflight
operator_concern_valid: true
should_this_be_treated_as_serious_regression: true
next_state: repair_quality_gate_before_any_more_phase2_compile
```
