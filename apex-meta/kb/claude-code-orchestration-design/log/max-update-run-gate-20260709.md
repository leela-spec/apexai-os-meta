# Apex KB Max Update Run Gate — Claude Code Orchestration Design

```yaml
kb_slug: claude-code-orchestration-design
kb_root: apex-meta/kb/claude-code-orchestration-design
run_id: max-update-run-20260709
created_at: 2026-07-09
operator_answers_captured: true
run_status: deterministic_prerequisite_block_before_llm_rebuild
llm_phase_started: false
reason: >
  Existing Phase 0 and Phase 1 artifacts are present, but the improved Apex KB
  lifecycle requires source-payload custody and newer deterministic postflight
  artifacts before treating the corpus baseline as authoritative for a full
  query_ready semantic rebuild.
```

## Operator answers captured

```yaml
output_tier: query_ready_maximum
rebuild_scope: full_rebuild_new_parallel_outputs
preserve_old_outputs: true
versioning_policy:
  do_not_overwrite_existing_llm_outputs: true
  write_new_ingest_outputs_under: ingest-analysis/max-run-20260709/
  write_new_wiki_outputs_under:
    - wiki/summaries/max-run-20260709/
    - wiki/concepts/max-run-20260709/
    - wiki/entities/max-run-20260709/
  later_cleanup: operator_compares_old_vs_new_then_deletes_old_placeholders
source_authority_policy:
  primary: current KB folder contents and manifests
  read_deeply: true
  old_ingest_and_wiki_outputs: historical_comparison_only_until_revalidated
phase_mode:
  deterministic_before_llm: required
  if_deterministic_outputs_current: continuous_phase1_to_phase2
  if_deterministic_outputs_missing_or_stale: rerun_deterministic_phase_first
phase2_depth: maximum_detail
compile_granularity: one_page_per_entity_concept_summary_cluster
execution_surface_policy:
  semantic_llm_work: current_assistant_chat_llm_by_default
  agent_or_codex: deterministic_execution_only_by_default
validation_level: full
commit_policy: commit_and_push_main_after_successful_validation
```

## Connector preflight findings

```yaml
observed_existing_artifacts:
  kb_root_found: true
  source_manifest_found: true
  phase0_navigation_report_found: true
  phase0_navigation_report_generated_at: 2026-07-02T12:19:44Z
  phase0_files_scanned: 1732
  phase1_completion_report_found: true
  phase1_status: phase_1_complete_operator_review_needed
  phase1_batches_completed:
    - phase1-batch01-skill-package-contracts
    - phase1-batch02-claude-code-orchestration-surface
    - phase1-batch03-external-orchestration-patterns
    - phase1-batch04-apex-application-patterns
missing_or_not_found_with_connector_search:
  source_payload_manifest: manifests/source-payload-manifest.json
  query_eval_pack: outputs/queries/evals/query-eval-pack.json
  process_flow_graph: manifests/phase0/process-flow-graph.json
  quality_coverage_report: no committed quality/coverage artifact found
```

## Gate decision

```yaml
decision: rerun_deterministic_baseline_before_new_llm_outputs
rationale:
  - The old Phase 0 scan is useful historical evidence and scanned a large corpus.
  - The current source manifest points to the raw source tree as pointer_only custody.
  - The source-payload manifest required by the improved lifecycle is missing.
  - Query-eval, graph/process-flow, and quality/coverage artifacts are absent.
  - Starting a maximum-detail LLM rebuild from incomplete deterministic custody would reintroduce the sham/placeholder failure mode.
```

## Required deterministic rerun before LLM rebuild

Run from repository root in a live worktree on `main`:

```bash
git checkout main
git pull --ff-only origin main

python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design generate-source-payload-manifest --allow-write --json
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design phase0 --allow-write --json
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design graph --allow-write --json
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design query-eval --init --allow-write --json
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design quality --json
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design coverage --json
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design status --json
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design lint --json
```

If those commands pass, the LLM rebuild can proceed continuously into Phase 1 and Phase 2 using new parallel versioned output paths.

## LLM rebuild contract after deterministic pass

```yaml
new_phase1_outputs:
  root: ingest-analysis/max-run-20260709/
  required_shape:
    - source identity
    - source coverage ledger
    - source-grounded claims
    - extracted concepts
    - extracted entities
    - contradictions and uncertainty triggers
    - proposed wiki pages
new_phase2_outputs:
  roots:
    - wiki/summaries/max-run-20260709/
    - wiki/concepts/max-run-20260709/
    - wiki/entities/max-run-20260709/
  every_page_requires:
    - frontmatter with source_refs
    - Adaptive Ranked Source Set
    - Macro / Meso / Micro
    - Key Claims
    - Routes Here
    - Uncertainty / Raw Source Reopen Triggers
old_outputs_policy:
  preserve: true
  use_as_authority: false
  use_for_comparison: true
```
