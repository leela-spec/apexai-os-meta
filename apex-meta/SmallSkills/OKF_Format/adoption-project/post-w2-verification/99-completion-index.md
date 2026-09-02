---
type: Review
title: Post-W2 Verification — Completion Index
description: Completion record for the adversarial post-W2 agent wiring, standards, terminology, and cross-client instruction audit, including the five proposed patch packs and corrected findings.
tags: [verification, completion, patch-index, agents, informatics]
status: complete_review_patches_not_applied
---

# Post-W2 Verification — Completion Index

## Status

```yaml
repository: leela-spec/apexai-os-meta
branch: main
implementation_under_review: 64b68f1bbac57a481c3178f32614c7d6cf8a3c70
initial_verification_basis: c140f3679107722e66b812320b62de5dc247ed3b
review_mode: static_adversarial_verification_plus_request_simulation
live_target_patches_applied: false
saved_artifacts_only: true
completion_state: complete
```

After `c140f367`, later commits in this review series add only review/patch artifacts. The live target files inspected by the audit were not modified by this review.

# Artifact set

| Artifact | Purpose | Saved commit |
|---|---|---|
| `00-verification-report.md` | Full wiring audit, request simulations, reference audit, defects, and prioritization | `2e3c9cc539c5d34e68fff0b8df61a0cefd0b1545` |
| `PATCH-01-informatics-scope-and-standard.md` | Claude path scoping, OKF-vs-Apex separation, reference hierarchy, authoring-Skill corrections | `e1bb212947f560d30e63fbc40ff846bf2b52361c` |
| `PATCH-02-okf-validator-correctness.md` | Validator semantics, YAML parsing, nested indexes, reserved files, regression tests | `9d237ecccc36a3fd5ca77ff5968ba3a2caf65979` |
| `PATCH-03-weekly-runtime-and-topology.md` | Runtime `context: fork`, direct stage-Skill topology, Macro/Meso repair, Session mutation path | `db9e08b111b87ca3d2f77d9cbcacec07f074911a` |
| `PATCH-04-terminology-and-ambiguity.md` | One glossary owner, verified-vs-accepted split, Weekly Macro/Meso/Micro namespacing, project-principles routing | `8a7f27c2e3e26eaef43670dbe97387bd3b237dad` |
| `PATCH-05-cross-client-instruction-drift.md` | Cursor/Kiro conditional wiki context, safe Windsurf/generic-agent adapters, Hermes synchronization | `bfbad062db7f08bd2068252bdf74c7506ae714ec` |

All patch files are operator-reviewable proposals using exact-match `<file>`, `<old>`, and `<new>` blocks. None has been applied to its target file.

# Corrected findings

## Weekly Micro exists

The original verification report §4.2 said no canonical Weekly Micro file was found. That statement is superseded.

`apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md` explicitly defines:

```text
Weekly Macro -> architecture/01-macro-architecture-decision.md
Weekly Meso  -> architecture/02-meso-file-map.md
Weekly Micro -> architecture/03-execution-trace-verification.md
```

The Micro file itself explicitly says it is a **historical execution-trace record**, not the current runtime contract. PATCH-03 therefore preserves the evidence and changes the entrypoint label to `weekly_micro_evidence` instead of rewriting history as current truth.

## Glossary authority is split today

The repository-wide orchestration index names `apex-meta/orchestration/GLOSSARY.md` as the live terminology authority, while Weekly material still points to `apex-meta/GLOSSARY.md`. PATCH-04 makes the root glossary a compatibility route and keeps one canonical owner.

## `verified` is not `accepted`

The canonical orchestration glossary currently collapses `canon / accepted / verified`. This conflicts with the architecture's independent-review versus operator-confirmed-mutation separation. PATCH-04 splits those meanings explicitly.

# Highest-impact application order

```yaml
apply_first:
  - PATCH-03-weekly-runtime-and-topology.md
  - PATCH-05-cross-client-instruction-drift.md
  - PATCH-02-okf-validator-correctness.md
then:
  - PATCH-04-terminology-and-ambiguity.md
  - PATCH-01-informatics-scope-and-standard.md
conditional_after_runtime_evidence:
  - root_CLAUDE_deduplication
  - Windsurf_or_Devin_activation_schema_migration
  - hard_tool_allowlist_for_direct_fork_weekly_stages
later_not_now:
  - cross_client_skill_mirror_canonicalization
  - broad_historical_OKF_retrofit
  - RAG_or_vector_retrieval
```

Rationale:

1. **PATCH-03** fixes a runtime contract mismatch: isolation is documented but not declared in stage Skill frontmatter, and current Macro/Meso still point at retired wrapper agents.
2. **PATCH-05** removes false always-on repository identity in several clients.
3. **PATCH-02** prevents the conformance tool from producing false upstream failures or missing invalid nested concepts.
4. **PATCH-04** removes authority/permission ambiguity that can misroute maintenance agents.
5. **PATCH-01** completes standards/reference separation and scoped informatics loading.

# Representative routing acceptance suite

After application, test from cold-start contexts rather than relying only on static path resolution.

| Request | Expected route / behavior |
|---|---|
| `Run the Weekly Orchestrator.` | APEX router -> `weekly-orchestrator` -> current stage -> direct forked stage Skill |
| `Run Precap Week.` | `PrecapWeek` executes in a fork; parent receives bounded return, not full worker context |
| `Start Multi-Agent Orchestration for this architecture problem.` | `00-START-HERE.md` -> Alfred/Meta Ops -> bounded specialist/review as needed |
| `Create a project from these notes.` | `apex-plan`; no implicit orchestration activation |
| `What is my exact next task?` | `apex-sync`; no planning authorship |
| `Mark TASK-123 done.` | `apex-session` after its evidence/confirmation contract |
| `Create an OKF concept here.` | informatics route -> authoring Skill -> upstream OKF + separate Apex profile checks |
| `Fix this unrelated Python bug.` | no informatics Claude rule and no wiki-specific client rule loaded merely because the session exists |
| `Run the orchestration.` | one clarification: Weekly Orchestrator or Multi-Agent Orchestration? |
| `Check the Meso file.` | resolve directly only in explicit Weekly context; otherwise one clarification |
| `Apply the project principles.` | resolve named authority scope or ask one clarification; do not invent a principles file |
| `Update project status.` | clarify derived overview vs confirmed durable mutation when intent does not distinguish them |

# Final acceptance gates

```yaml
weekly:
  six_stage_skills_runtime_fork_verified: required
  retired_stage_wrapper_paths_in_live_meso: 0
  weekly_review_agents: [apex-review-validity, apex-review-alignment]
  durable_project_task_mutation_owner: apex-session
  implicit_project_kb_write_path: forbidden

terminology:
  canonical_orchestration_glossary_count: 1
  verified_distinct_from_accepted: required
  weekly_macro_meso_micro_namespaced: required

cross_client:
  false_obsidian_repository_identity_in_current_instruction_surfaces: 0
  generic_repository_questions_forced_to_wiki_query: forbidden

informatics:
  unrelated_claude_task_loads_informatics_rule: false
  upstream_okf_and_apex_profile_diagnostics_separate: required
  nested_indexed_directories_still_validated: required

residual_runtime_evidence:
  root_claude_memory_load_trace: required_before_deduplication
  windsurf_devin_rule_schema_trace: required_before_activation_key_migration
  direct_fork_stage_tool_surface_trace: required_before_permission_hardening
```

# Closure

The requested post-implementation verification is now persisted: full audit, simulated request routing, standards-reference review, Macro/Meso/Micro correction, terminology authority analysis, high-impact improvement ranking, and five exact-match patch packs.

**No proposed target patch is applied by this review.**
