---
name: apex-kb
description: >
  Use this skill when the operator asks to scaffold, intake sources, hash sources,
  run deterministic corpus intelligence, perform two-phase ingest, compile wiki
  pages, query, retrieve, lint, audit, or maintain a durable Apex knowledge base
  under apex-meta/kb/[kb-slug]/. Produces source-preserving KB artifacts,
  one topic-scoped Phase 1 ingest analysis per registry topic, operator-gated Phase 2 wiki pages that implement an adaptive page value contract (Adaptive Ranked Source Set, Macro / Meso / Micro synthesis defined as Why / What-it-is / How, Key Claims with source pointers and a present/proposed/open state, Routes Here, and Uncertainty / Raw Source Triggers), deterministic
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

This router's answer, together with the `capability_precheck` below, fills the `execution_route` slot of the Step 0 intake record (`manifests/run-intent.md`); it is not a separate question asked again later.

### Connector-only semantic authoring route


Allowed work is limited to complete semantic files or complete rewrites of explicitly owned semantic files. Partial edits, appends, machine-maintained sections, `wiki/index.md`, manifests, hashes, derived indexes, deterministic commands, and certification are prohibited.

Read the repository-local `semantic-contract/` before Phase 1. An account-level Skill is optional; missing Skill availability is never a stop condition. Use `references/browser-git-connector-semantic-runbook.md` when preparing repository-local instructions.

Work one topic per context. Before selecting sources, lock stable target questions, priorities, answer requirements, and expected page routes in the topic registry. Treat Phase 0 rankings as candidate navigation only. Maintain `log/semantic-runs/<run-id>/topics/<topic-slug>.json` after every source and before context ends.

Continue reading while a known readable canonical source can answer an unresolved critical or routine question. Unopened sources are not evidence and must not appear in Adaptive Ranked Source Sets. Connector cost, source length, context pressure, or write friction may force `partial`; they never lower completion criteria.

For each source, read the complete source or every relevant section, write and reread Phase 1, and dispose every concept/entity candidate. Choose page topology by recurring retrieval value and duplication reduction. Write and reread complete answer-bearing Phase 2 pages. Boundary notices and readable-source reopen triggers cannot satisfy target questions.

Run page-only query and claim-entailment acceptance in a fresh context that did not receive drafting rationale or self-assessment. Record the result under `audit/semantic-acceptance/<run-id>/<topic-slug>.json`. Only `semantic_pass` for every in-scope topic permits `compiled_unvalidated`; otherwise report `partial` or `analysis_complete_unvalidated`.

The route never runs Python, shell, scaffold, intake, hashing, manifest updates, Phase 0, index/retrieval rebuild, lint, quality, or postflight, and never claims `query_ready`.
### Terminal-backed route

For a **new KB, fresh Setup, or `/apex-kb start` request**, use `apex_kb.py start` as the only operator entrypoint and follow `references/start-workflow.md`. Start translates the compact operator configuration into the canonical control-plane inputs; never manually recreate its derived fields through `control init`.

For an **existing controlled KB**, use `apex_kb.py control` as the lifecycle surface. `control run` executes exactly one legal deterministic stage or renders one semantic packet, `control next` derives the exact next command or short packet trigger, and `control reconcile` resumes from repository files and reason-codes drift. Direct low-level mutation commands remain available only for legacy KBs without `manifests/run-state.json`; a controlled run blocks them so state cannot drift. `postflight` remains the bounded deterministic completion aggregate and independent semantic acceptance remains mandatory for every compiled tier.

## Operating contract

```yaml
package_name: apex-kb
primary_role: durable_source_preserving_knowledge_base_compiler
data_root_template: apex-meta/kb/<kb-slug>/
one_kb_root_per_invocation: true
required_global_argument: --kb-root apex-meta/kb/<kb-slug>/

owned_lifecycle:
  - intake_and_intent_lock
  - canonical_run_state_and_legal_transitions
  - exact_next_command_derivation
  - scaffold
  - source_intake
  - deterministic_corpus_intelligence
  - semantic_handoff_packet_rendering
  - ingest_phase_1_analysis
  - ingest_phase_2_wiki_compile
  - independent_semantic_acceptance
  - deterministic_index_validation
  - local_retrieval
  - query_packet_generation
  - lint_audit_maintenance
  - read_only_git_state_classification
  - file_based_recovery_and_input_drift_invalidation

canonical_paths:
  - raw/
  - kb-schema.md
  - manifests/run-intent.md
  - manifests/run-state.json
  - manifests/topic-registry.json
  - manifests/source-manifest.json
  - manifests/source-payload-manifest.json
  - ingest-analysis/
  - wiki/
  - audit/
  - log/
  - log/runs/<run-id>/packets/
  - log/runs/<run-id>/stage-results/

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


The lifecycle and state labels are defined by `references/semantic-value-contract.md`.

```yaml
operator_flow:
  A_prepare: repo / KB preflight, target-query lock, scaffold, path validation, run profile selection
  B_ingest_and_compile: source intake, source payload manifest, Phase 0, evidence-led semantic analysis, and answer-bearing wiki compile
  C_semantic_acceptance: clean-context page-only query and claim-entailment evaluation
  D_postflight: capability-checked index rebuild, retrieval rebuild, strict lint/quality, acceptance-artifact validation, and evidence packet
  E_query_or_maintain: query packets, stale checks, source drift checks, repair backlog

output_tiers:
  source_only: custody and manifests only
  analysis_only: semantic analysis, no wiki pages
  compiled_minimal: minimum useful page topology with complete priority-query value
  compiled_full: complete priority-query value plus independently useful summaries/concepts/entities
  query_ready: accepted compiled wiki plus successful deterministic postflight and fresh retrieval

truthful_states:
  analysis_complete_unvalidated: Phase 1 complete without accepted Phase 2
  partial: material query, evidence, architecture, disposition, or acceptance gaps remain
  compiled_unvalidated: critical/routine queries and sampled claims pass semantic acceptance; deterministic postflight pending
  query_ready: semantic acceptance and deterministic postflight pass; retrieval fresh
```
## File navigation


Select the execution route above before opening terminal-oriented references.

Read supporting files only when needed:

| Need | File |
|---|---|
| Completion target, registry v2, ledger, traceability, semantic acceptance | `references/semantic-value-contract.md` |
| Browser/Git-connector workflow and evaluator prompts | `references/browser-git-connector-semantic-runbook.md` |
| Data layout, canonical/derived rules, page and manifest constraints | `references/kb-contract.md` |
| New-KB Setup routing and Start preview/write sequence | `references/start-workflow.md` |
| Python command surface, control plane, stage results, Git classification, and write policy | `references/script-command-contract.md` |
| Canonical run intent/state, semantic packet, and Git-state schemas | `references/run-intent.schema.json`, `references/run-state.schema.json`, `references/stage-result.schema.json`, `references/semantic-handoff-packet.schema.json`, `references/git-state.schema.json` |
| Ingest, query, lint, audit behavior | `references/ingest-query-lint-audit-rules.md` |
| Retrieval engine rules | `references/retrieval-contract.md` |
| Acceptance checks and fixtures | `references/acceptance-tests.md` |
| KB doctrine distilled from the old-apex knowledge-bank role | `references/old-apex-knowledge-bank-doctrine.md` |
| Phase 1 analysis shape | `templates/ingest-analysis-template.md` |
| Run-specific semantic packet projection | `templates/semantic-handoff-packet-template.md` |
| Phase 2 wiki page shape | `templates/wiki-page-templates.md` |
| Query packet shape | `templates/query-output-template.md` |
| Topic work pack shape (bounded semantic input) | `templates/topic-work-pack-template.md` |
| Starter KB schema | `templates/kb-schema-template.md` |
| Starter source manifest | `templates/source-manifest-template.json` |
| Local commands | `examples/powershell-commands.md` |
| Operator runbook | `examples/lifecycle-runbook.md` |

## Capability precheck and truthful state cap


Before procedure steps that require Python, retrieval rebuild, Git, or semantic evaluation, record whether the active executor can perform them and capture evidence.

```yaml
capability_precheck:
  terminal_execution: supported | unsupported
  python_execution: supported | unsupported
  retrieval_rebuild: supported | unsupported
  git_read_only_classification: supported | unsupported
  target_commit_verification: supported | unsupported
  git_diff_and_commit: supported | unsupported
  independent_semantic_evaluator: supported | unsupported

completion_state_cap:
  phase1_complete_without_phase2_acceptance: analysis_complete_unvalidated
  material_gap_or_missing_acceptance: partial
  semantic_acceptance_pass_without_postflight: compiled_unvalidated
  deterministic_postflight_failed: partial
  query_ready_requires:
    - semantic_acceptance_pass
    - deterministic_postflight_pass
    - retrieval_fresh
```

Connector readback proves stored content only. It never proves semantic usefulness, source entailment, Python execution, index freshness, lint, quality, or query readiness.
## Procedure

Follow only the selected route. The connector route uses the bounded whole-file semantic-authoring sequence above. The terminal-backed route follows the referenced command, retrieval, acceptance-test, and runbook contracts. Neither route may weaken the existing lifecycle, output tiers, ownership model, semantic acceptance requirement, or completion labels.

### Step 0 — Intake and intent lock (before scaffold, source intake, or Phase 0)

On the terminal-backed route, a new KB enters through `apex_kb.py start` and `references/start-workflow.md`. Start validates the compact operator YAML, writes the topic registry and Start records when authorized, and delegates canonical initialization to the control plane. Do not author `manifests/topic-registry.json` or invoke `control init` freehand for a new KB. After Start returns, obey only its `operator_action` and then `control next`, `control run`, and `control reconcile`. Existing controlled KBs resume directly through control. On a connector-only semantic handoff, the rendered packet file is authoritative and the stable chat trigger is one line pointing to that packet.

Nothing that registers sources, runs Phase 0, writes wiki pages, or commits may run until this
step ends in a recorded operator confirmation (creating the empty KB skeleton is permitted as
pre-gate setup — see 0d). This is the single point where the executor's whole understanding of
the run is read back and approved — it exists because a run that silently locks a misread
subject can otherwise burn a full corpus intake and Phase 0 before anyone notices. This step
runs on every run, new KB or extending an existing one. It never re-runs for read-only work
(`query`, `retrieve`, `lint`, `audit`, `status`, `health`) or for repeated commands within a
run already confirmed for this `run_id`.

**0a — Intake Q&A.** In one conversational pass (not a form — fill every slot you can from the
operator's first message, and ask follow-ups only for slots left genuinely unresolved),
establish and record each intent-record slot below from the operator's own answers. Never
substitute an assumption or an inference from a filename, path, or prior summary for an answer;
if a slot is ambiguous, ask. The slots (see `references/semantic-value-contract.md` for the
`manifests/run-intent.md` schema):

- `operator_intent` — the job to be done, in the operator's words.
- `kb_identity` — one line: "this KB is about `<kb_identity>`."
- `source_locus` — where the real source material actually lives, and what is explicitly out of scope.
- `success_definition` — what the chosen output tier means for this specific KB.
- `output_tier`, `execution_route`, `corpus_breadth` — proposed by the executor in 0d, confirmed by the operator.
- `topic_slugs` — the registry topics this run will build (from 0b).

**0b — Topic interview.** For each topic, lock stable query IDs, question text, priority, answer requirements, and expected page route in `manifests/topic-registry.json`. Also record vocabulary where it sharpens routing: `phrases`/`aliases` (strong signals), `supporting_terms` (weaker; legacy `keywords` are read this way), `negative_terms` (suppress body-only false matches), `ambiguous_terms` (require co-occurrence). Vocabulary supports deterministic ranking but never defines semantic completion. An absent registry remains valid for scaffold, intake, `source_only`, and early `analysis_only`. Any compiled tier requires target queries for every in-scope topic. Broad topics must cover material definitions, structure, workflow, ownership, rules, relationships, current versus proposed state, examples, and edge cases where applicable.

**0c — Topic-scope validation input.** For each locked topic run `topic-sanity-check` (terminal-backed route) or its manual equivalent (connector route: check the topic's `phrases`/`aliases` against the KB root's own path, sibling registry topics, and a light sample of nearby filenames — never against a freshly-written `kb-schema.md`/`README.md` or the KB's own generated output, which are self-authored by the same run and so are circular, not independent evidence; a single generic `supporting_term` never counts alone). This is a **validation input to the 0d read-back, not a standalone stop.** Record each topic's verdict in `manifests/run-intent.md`. A `scope_evidence_absent` verdict must be surfaced prominently in the read-back, but the enforcement point is the operator's confirmation in 0d, not the verdict itself.

**0d — Read-back and operator intent gate (mandatory).** Emit ONE compact read-back (roughly eight lines) that states: `kb_identity`; mode (new_kb / extend_kb); `source_locus` and out-of-scope; the executor's **recommended** `output_tier`, `execution_route`, and `corpus_breadth`, each with a one-line reason drawn from `operator_intent` (recommend from intent, never silently choose — the operator accepts or overrides); the `topic_slugs`; and the per-topic 0c verdict. End with an explicit ask: "Reply to confirm before I intake sources / run Phase 0." On the operator's affirmative, write `manifests/run-intent.md` with `operator_confirmed: true` and the operator's verbatim affirmative in `operator_confirmation_quote`. **No `source-intake`, `phase0`, wiki writing, or commit/push runs until that record shows `operator_confirmed: true` for this `run_id`.** Creating the empty KB skeleton with `scaffold` (and writing `run-intent.md`/`topic-registry.json` themselves) is permitted as pre-gate setup — it registers no sources and runs no corpus analysis — but the expensive, hard-to-reverse steps stay behind the gate. On the connector route the read-back is authored in chat and `run-intent.md` is written as a complete whole file (this operator-authored markdown is an allowed connector-route write, like `log/semantic-runs/.../*.json`); the gate is the operator's chat confirmation. This intake gate is distinct from and earlier than the Phase 2 `approve ingest` gate; use a plain recorded affirmative here, no approval-phrase machinery.

**Source-intake breadth defaults to narrow.** Registering the entire repository as pointer-only sources for a single topic request is not the default — it requires either an explicit operator instruction to index broadly, or a `broad_breadth_reason` recorded in `manifests/run-intent.md` and confirmed in 0d. Prefer the smallest root that plausibly contains the named subject's material; never auto-widen to full-corpus "to see."

After Phase 0, review `term-frequency.json` and propose additional topics from real corpus evidence. A newly proposed topic re-enters at 0b–0d before it is built. Phase 0 emits the exhaustive, tiered rankings in `topic-source-rankings.json` and a concentrated per-topic work pack in `manifests/phase0/work-packs/<topic-slug>.md`. Start semantic reading from the work pack, not the full ranking map. Before semantic work, create the per-topic ledger required by `references/semantic-value-contract.md`.
### Phase 2 compile: per-page draft, check, retry, escalate


Compile one topic at a time after its critical evidence coverage is resolved.

1. Confirm every target query has an answer requirement and expected page route.
2. Use Phase 0 rankings only to locate candidates. Record candidate rank, authority, availability, read status, reviewed passages, supported query IDs, analysis reference, claim use, and next action in the topic ledger.
3. Continue source reading while a known readable canonical source could answer an unresolved critical/routine query. Never put an unopened source in frontmatter or Adaptive Ranked Source Set.
4. Complete Phase 1 query linkage and give every concept/entity candidate a promotion disposition.
5. Choose the minimum useful page topology. A summary must answer broad target questions directly. Promote concept/entity pages when they answer recurring independent questions or remove repeated project-specific definitions.
6. Draft and reread complete v2 pages. Run deterministic `quality --strict --json` only on the terminal route; repair reason-coded wiring failures without treating a pass as semantic proof.
7. Run page-only query and claim-entailment acceptance in a clean context. Record reason-coded acceptance artifacts. Repair only failed queries/claims and reevaluate in a fresh context.
8. If any critical/routine query is partial, not answerable, blocked by readable evidence, or missing acceptance, record `partial`. If Phase 1 is complete but Phase 2 is not accepted, record `analysis_complete_unvalidated`.

A page is semantically complete only when its declared questions are directly answerable and sampled material claims are supported. Headings, counts, length, rankings, and drafter self-review are never sufficient.
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

topic_vocabulary_mismatches_kb_scope_evidence:
  behavior: surface_in_step_0d_readback_and_require_operator_confirmation
  rule: a Step 0c `scope_evidence_absent` verdict (topic phrases/aliases have zero correspondence to the KB's own scope evidence - path components, sibling registry topics, a light filename sample) is surfaced prominently in the Step 0d read-back; the enforcement point is the operator's confirmation, not the verdict
  detection: topic-sanity-check (terminal-backed) or its manual equivalent (connector route), run as a Step 0c validation input
  never_treat_as: source_access_blocker
  rationale: a topic name derived from a misread of the operator's request is a topic-lock error, not evidence the subject lacks local material; conflating the two, or proceeding without the Step 0d confirmation, burns a full corpus intake and Phase 0 run on the wrong subject before anyone notices

phase2_stop_requested:
  behavior: stop_after_phase1
  applies_to: [analysis_only, operator_explicit_stop_before_wiki]
  legacy_direct_command_phrase: approve ingest

control_input_changed:
  behavior: block_and_report_earliest_affected_stage
  next_action: run_control_reconcile_with_operator_review_then_explicit_accept_input_change
  rule: never silently overwrite recorded fingerprints or preserve downstream completion after an upstream change

control_packet_input_changed:
  behavior: reject_semantic_output_and_render_a_fresh_packet_after_reconciliation
  rule: chat continuity or executor self-report cannot override a changed packet input

git_conflict_or_operation_in_progress:
  behavior: block_with_read_only_classification
  rule: never fetch, pull, reset, stash, merge, rebase, cherry-pick, revert, commit, or push

target_commit_mismatch:
  behavior: block_before_stage_execution
  rule: the configured target commit is a reproducibility guard, not permission to move HEAD

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


The requested mode is complete only when its artifact and every applicable gate have evidence. Completion reports lead with target-query coverage, reviewed/materially-used source coverage, semantic verdicts, and unresolved blockers; artifact counts are secondary.

`analysis_complete_unvalidated`, `partial`, and `compiled_unvalidated` are truthful states, not success aliases. `compiled_unvalidated` requires clean-context `semantic_pass` for every in-scope topic. `query_ready` additionally requires passing deterministic postflight and fresh retrieval.

Never declare completion while a known readable canonical source is named only as a reopen trigger for an unresolved critical/routine query, an unopened source is represented as evidence, a Phase 1 concept/entity candidate lacks disposition, or an acceptance artifact is missing/incomplete. Repair loops remain reason-coded and candidate-driven.
