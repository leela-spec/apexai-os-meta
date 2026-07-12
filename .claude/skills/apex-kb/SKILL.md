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

## Execution-surface router

Ask exactly one question before procedure or file navigation:

> Can the executor run repository Python commands in a live worktree and capture the command, exit status, stdout, and stderr?

```yaml
execution_route:
  terminal_backed:
    when: yes
    authority: deterministic execution and validation
    preferred_completion_interface: postflight
  connector_only:
    when: no, but complete repository-file reads and whole-file writes are available
    authority: bounded semantic authoring only
    completion_cap: compiled_unvalidated
  unsupported:
    when: neither terminal execution nor reliable whole-file read/write is available
    behavior: stop without claiming compile or validation
```

### Connector-only semantic authoring route

Allowed work is limited to complete new semantic files or complete rewrites of explicitly owned semantic files. Partial edits, appends, machine-maintained sections, `wiki/index.md`, manifests, hashes, derived indexes, deterministic commands, and certification are prohibited.

Use one semantic page per context window. For each page: read a bounded source set, author the complete page, reread the complete candidate, run the preventive checklist below, write the whole file, read back stored content, and add one entry to `log/connector-compile-<run-id>.json`. That log is a complete new handoff file, not a deterministic certificate.

```yaml
connector_precheck_reason_concepts:
  - missing_source_refs
  - missing_phase2_value_sections
  - placeholder_text
  - no_key_claims
  - claim_pointer_coverage_below_100_percent
  - single_claim_summary
  - single_claim_concept_thin
  - concept_micro_not_evidenced
  - thin_macro_meso_micro
  - summary_source_breadth_below_profile
  - no_query_routes
```

The checklist is preventive only. Terminal `quality --strict` remains authoritative. Connector readback proves stored content only. The route stops at `compiled_unvalidated`.

### Terminal-backed route

Use the existing command contract, retrieval contract, acceptance tests, and lifecycle runbook rather than duplicating command sequences here. After the runtime change is applied, use `postflight` as the preferred bounded deterministic completion interface. Preserve bounded semantic acceptance as a separate required gate for `query_ready`.

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

Select the execution route above before opening terminal-oriented references.

Read supporting files only when needed:

| Need | File |
|---|---|
| Data layout, canonical/derived rules, page and manifest constraints | `references/kb-contract.md` |
| Python command surface and write policy | `references/script-command-contract.md` |
| Ingest, query, lint, audit behavior | `references/ingest-query-lint-audit-rules.md` |
| Retrieval engine rules | `references/retrieval-contract.md` |
| State transitions and gates | `references/lifecycle-state-machine.md` |
| Acceptance checks | `references/acceptance-tests.md` |
| KB doctrine distilled from the old-apex knowledge-bank role | `references/old-apex-knowledge-bank-doctrine.md` |
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

Follow only the selected route. The connector route uses the bounded whole-file semantic-authoring sequence above. The terminal-backed route follows the referenced command, retrieval, acceptance-test, and runbook contracts. Neither route may weaken the existing lifecycle, output tiers, ownership model, semantic acceptance requirement, or completion labels.

### Step 0 — Topic interview (before scaffold or source intake)

Before creating or adding sources to a KB, ask the operator to name target topics and open questions this KB should be able to answer. This is purely declarative -- no corpus exists yet. Write each named topic to `manifests/topic-registry.json` with `source: operator`, `status: not_started`, and a starter `keywords` list. An empty or absent registry is a valid state; it never blocks scaffold or intake.

After Phase 0 produces `manifests/phase0/term-frequency.json` (deterministic, domain-agnostic word counts -- no hardcoded topic strings), review it and propose additional topics evidenced by real counts from this corpus. Append proposals to the same registry with `source: llm_proposed`. Never blend proposed topic names into the deterministic ranking outputs themselves: the registry only ever holds topic names and keyword lists; `manifests/phase0/topic-source-rankings.json` (Phase 0's output, computed from those keywords) is the only place ranked results live, and it is always machine-written, never edited by hand.

### Phase 2 compile: per-page draft, check, retry, escalate

Compile one page or a small batch (2-3 pages) at a time, never the whole file list in one pass.

1. Draft the page against the page value contract. For a `summary` page tied to a registry topic, populate its Adaptive Ranked Source Set directly from that topic's entry in `topic-source-rankings.json` -- real ranked files and real hit counts, not invented ones.
2. Immediately validate. Terminal route: run `quality --strict --json` on the KB. Connector route: run the precheck against `connector_precheck_reason_concepts` above.
3. If the page is named in `phase2_repair_candidates` / `shell_page_candidates` (or fails the connector precheck), redraft using the exact reason codes returned. Up to 2 redraft attempts total.
4. If it still fails after 2 redrafts, do not silently accept it and do not silently drop it: record it as an audit item under `audit/` with its path and residual reason codes, and cap that batch's completion state at `partial`.
5. Advance to the next page or batch only once the current one has zero repair reasons or has been explicitly escalated per step 4.

"Done" for a Phase 2 batch means `phase2_repair_candidates` and `shell_page_candidates` are empty for every page in it. Heading presence alone (`missing_phase2_value_sections` empty) is not sufficient -- the engine measures section depth, claim count, and pointer specificity, and a batch is not done until those pass too.

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
  - generic_term_frequency
  - registry_driven_topic_source_ranking
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

phase2_page_fails_quality_after_retries:
  behavior: flag_as_audit_repair_candidate
  state_cap: partial
  rule: never_promote_to_query_ready_and_never_silently_drop
```

## Completion gate

The skill is complete only when the requested mode has produced the correct artifact and every required gate has evidence. `compiled_unvalidated` and `partial` are valid truthful outcomes, not success aliases. `query_ready` requires a passing deterministic postflight, fresh retrieval, and bounded semantic acceptance. Repair loops must be candidate-driven: patch only pages named by reason-coded findings, then rerun the failed checks. A page that still fails after two redraft attempts is escalated to an audit item, never silently accepted or silently dropped.
