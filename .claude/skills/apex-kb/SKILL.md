---
name: apex-kb
description: >
  Use this skill when the operator asks to scaffold, intake sources, hash sources,
  run deterministic corpus intelligence, perform two-phase ingest, compile wiki
  pages, query, retrieve, lint, audit, or maintain a durable Apex knowledge base
  under apex-meta/kb/<kb-slug>/. Produces source-preserving KB artifacts,
  Phase 1 ingest analysis, operator-gated Phase 2 wiki pages that implement an adaptive page value contract (Adaptive Ranked Source Set, Macro / Meso / Micro synthesis, Key Claims with source pointers, Routes Here, and Uncertainty / Raw Source Triggers), deterministic
  indexes, local retrieval outputs, query packets, lint reports, and audit flags.
  Does not plan projects, mutate task/session/sync state, rank next tasks,
  rebuild task registries, contact external services, or write outside the KB root.
---

# Apex KB

## Operating contract

```yaml
package_name: apex-kb
primary_role: durable_source_preserving_knowledge_base_compiler
data_root_template: apex-meta/kb/<kb-slug>/
one_kb_root_per_invocation: true
required_global_argument: --kb-root apex-meta/kb/<kb-slug>/

owned_lifecycle:
  - scaffold
  - source_intake
  - deterministic_corpus_intelligence
  - ingest_phase_1_analysis
  - operator_gate
  - ingest_phase_2_wiki_compile
  - deterministic_index_validation
  - local_retrieval
  - query_packet_generation
  - lint_audit_maintenance

canonical_paths:
  - raw/
  - kb-schema.md
  - manifests/source-manifest.json
  - manifests/source-payload-manifest.json
  - ingest-analysis/
  - wiki/
  - audit/
  - log/

derived_paths:
  - manifests/phase0/
  - derived/search/
  - outputs/queries/

semantic_compile_policy:
  default: continuous_phase1_to_phase2_when_output_tier_includes_wiki
  no_mandatory_gate_by_default: true
  safe_modes:
    - analysis_only
    - phase1_only
    - operator_explicit_stop_before_wiki
  legacy_explicit_gate_phrase: approve ingest

execution_surface_policy:
  default_semantic_execution_surface: current_assistant_chat_llm
  external_agent_or_codex_role: deterministic_executor_only_by_default
  use_external_agent_or_codex_for:
    - live_worktree_script_execution
    - git_native_patch_application
    - deterministic_postflight_validation
    - commit_and_push_when_connector_or_local_git_is_required
  do_not_use_external_agent_or_codex_for:
    - phase_1_semantic_analysis_by_default
    - phase_2_wiki_drafting_by_default
    - LLM_owned_synthesis_when_current_assistant_can_perform_it
  semantic_delegation_requires: explicit_operator_override
boundary:
  must_not_mutate:
    - apex-plan files
    - apex-sync files
    - apex-session files
    - PreCap artifacts
    - FlowRecap artifacts
    - APSU/status-merge artifacts
    - personal orchestration state
```

## Operator-facing v3 lifecycle and output tiers

```yaml
operator_flow:
  A_prepare: repo / KB preflight, scaffold, path validation, run profile selection
  B_ingest_and_compile: source intake, source payload manifest, Phase 0, semantic analysis, and wiki compile when selected output tier requires it
  C_postflight: capability-checked index rebuild, retrieval rebuild, strict lint/quality, bounded semantic acceptance, and evidence packet
  D_query_or_maintain: query packets, stale checks, source drift checks, repair backlog

output_tiers:
  source_only: custody and manifests only
  analysis_only: semantic analysis, no wiki pages
  compiled_minimal: small high-value wiki with index and patch backlog
  compiled_full: full summaries/concepts/entities
  query_ready: compiled wiki plus successful deterministic postflight and semantic acceptance
```

## File navigation

Read supporting files only when needed:

| Need | File |
|---|---|
| Data layout, canonical/derived rules, page and manifest constraints | `references/kb-contract.md` |
| Python command surface and write policy | `references/script-command-contract.md` |
| Ingest, query, lint, audit behavior | `references/ingest-query-lint-audit-rules.md` |
| Retrieval engine rules | `references/retrieval-contract.md` |
| State transitions and gates | `references/lifecycle-state-machine.md` |
| Acceptance checks | `references/acceptance-tests.md` |
| Phase 1 analysis shape | `templates/ingest-analysis-template.md` |
| Phase 2 wiki page shape | `templates/wiki-page-templates.md` |
| Query packet shape | `templates/query-output-template.md` |
| Starter KB schema | `templates/kb-schema-template.md` |
| Starter source manifest | `templates/source-manifest-template.json` |
| Local commands | `examples/powershell-commands.md` |
| Operator runbook | `examples/lifecycle-runbook.md` |


## Capability precheck and truthful state cap

Before procedure steps that require Python, retrieval rebuild, or Git, record whether the active executor can run terminal commands and capture their outputs.

```yaml
capability_precheck:
  terminal_execution: supported | unsupported
  python_execution: supported | unsupported
  retrieval_rebuild: supported | unsupported
  git_diff_and_commit: supported | unsupported

completion_state_cap:
  semantic_pages_written_without_postflight: compiled_unvalidated
  deterministic_postflight_failed: partial
  required_semantic_review_missing: partial
  query_ready_requires:
    - deterministic_postflight_pass
    - retrieval_fresh
    - semantic_acceptance_pass
```

Connector read-back proves file content only. It never proves Python execution, index freshness, lint, quality, or query readiness.

## Procedure

1. Resolve exactly one `--kb-root`. Never hardcode `claude-skill-design`; treat it only as a possible test KB slug.
2. Select a run profile and output tier before intake.
3. Keep LLM-owned semantic work in the current assistant/chat LLM by default. Use Agent Mode, Codex, or local executors only for deterministic script execution, Git-native patch/application work, validation, and commit/push operations unless the operator explicitly delegates semantic drafting.
4. Run deterministic checks through `apex-meta/scripts/apex_kb.py` for scaffold, hash, source-intake, generate-source-payload-manifest, preflight, phase0, index, lint, audit, status, and health.
5. Preserve source custody before semantic work: raw source, durable pointer, storage mode, source hash or no-hash reason, source manifest entry, and source payload manifest.
6. Run `generate-source-payload-manifest` after source intake and before Phase 0. It is an Apex-native BagIt-style ledger using stdlib hashing only; it does not replace `source-manifest.json`.
7. Run Phase 0 before LLM ingest when corpus navigation is needed. Phase 0 may create only deterministic artifacts under `manifests/phase0/`.
8. When the selected output tier includes wiki output, Phase 1 semantic analysis and Phase 2 wiki compile are one continuous semantic compile by default. Stop after Phase 1 only for `analysis_only`, `phase1_only`, or `operator_explicit_stop_before_wiki` safe modes.
9. In Phase 2, draft or update `wiki/summaries/`, `wiki/concepts/`, and `wiki/entities/` pages and any audit or semantic index sections. Compiled pages **must** implement the Phase 2 page value contract: include an Adaptive Ranked Source Set, Macro / Meso / Micro synthesis, Key Claims with source pointers and labels, Routes Here, and Uncertainty / Raw Source Reopen Triggers. Every claim still needs a source pointer, confidence, and claim label.
10. Rebuild deterministic index sections and retrieval indexes after wiki updates. Use `apex_kb_retrieval.py` for `build-index`, `stale`, `query`, `export`, and `clear-index`.
11. Answer queries index-first. Read `wiki/index.md`, retrieve the smallest sufficient page set, synthesize from compiled wiki pages, and save query packets when reuse is useful.
12. Keep lint/audit maintenance read-only unless the operator explicitly asks for a deterministic write inside the KB root.

## Deterministic versus LLM ownership

```yaml
python_owns:
  - scaffold_structure
  - file_hashing
  - source_manifest_shape
  - source_payload_manifest_generation
  - source_storage_mode_recording
  - corpus_profile
  - heading_link_frontmatter_maps
  - keyword_hit_maps
  - deterministic_index_sections
  - frontmatter_validation
  - link_orphan_stale_checks
  - retrieval_index_build_query_export
  - audit_file_listing

llm_owns:
  - relevance_judgment
  - source_summary
  - concept_extraction
  - entity_synthesis
  - contradiction_interpretation
  - phase_1_analysis
  - phase_2_wiki_drafting
  - query_answer_synthesis
  - knowledge_gap_framing
```

## Failure behavior

```yaml
source_access_precheck_failed:
  behavior: stop
  output_only: SOURCE_ACCESS_PRECHECK_FAILED

missing_kb_root:
  behavior: route_to_scaffold_or_request_existing_root

missing_source:
  behavior: stop
  rule: never infer source contents from filename, title, memory, or summary

phase2_stop_requested:
  behavior: stop_after_phase1
  applies_to: [analysis_only, phase1_only, operator_explicit_stop_before_wiki]
  optional_legacy_phrase: approve ingest
stale_retrieval_index:
  behavior: report_stale_and_rebuild_before_reliance

contradiction_detected:
  behavior: expose_as_uncertainty_trigger_or_audit_item

request_mutates_plan_sync_session:
  behavior: refuse_in_apex_kb_and_handoff_read_only_evidence_packet
```

## Completion gate

The skill is complete only when the requested mode has produced the correct artifact and every required gate has evidence. `compiled_unvalidated` and `partial` are valid truthful outcomes, not success aliases. `query_ready` requires a passing deterministic postflight, fresh retrieval, and bounded semantic acceptance. Repair loops must be candidate-driven: patch only pages named by reason-coded findings, then rerun the failed checks.
