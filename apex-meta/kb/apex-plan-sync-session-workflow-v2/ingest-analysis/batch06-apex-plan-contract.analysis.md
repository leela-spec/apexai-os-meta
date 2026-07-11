---
analysis_id: "apex-plan-sync-session-workflow-v2-apex-plan-contract-analysis"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_slug: "apex-plan-contract"
run_profile:
  output_tier: "compiled_full"
  safe_mode: "none"
source_payload_manifest_ref:
  path: "manifests/source-payload-manifest.json"
  status_at_analysis_time: "fresh"
created_at: "2026-07-11T09:40:00Z"
created_by: "apex-kb"
phase: ingest_phase_1
status: operator_review_needed
semantic_compile_policy:
  phase_2_continues_when_output_tier_includes_wiki: true
  optional_resume_phrase: "approve ingest"
supersedes: "ingest-analysis/batch02-apex-plan.analysis.md (pointer_only, unverifiable; content cross-checked and largely confirmed below)"
---

# Phase 1 Ingest Analysis — apex-plan contract

## 1. Source Identity

```yaml
source_identity:
  title: "apex-plan skill package"
  author_or_origin: "repo .claude/skills/apex-plan/, this repo, current HEAD"
  publication_or_creation_date: "unknown (repo history predates this KB run)"
  source_authority_level: "primary"
  source_authority_rationale: "Live skill definition read directly from the repository working tree; this is the canonical, currently-effective contract, not a report about it."
  source_scope: "Defines apex-plan's role, ownership, boundaries, procedure, failure modes, and completion gate."
  source_limitations:
    - "Directory also contains .dr.md/.pro.md/.v1.md variant files that were deliberately excluded from this batch; see Uncertainty U001-U002."
```

## 2. Source Summary

```yaml
source_summary:
  one_sentence_core: "apex-plan is a no-script, operator-gated project-planning skill that produces an apex_plan_packet and hands off all deterministic computation to apex-sync and all mutation to apex-session."
  compact_summary: >
    apex-plan owns project capture, epic/task decomposition, dependency proposal (qualitative),
    priority/urgency/focus rationale (qualitative), and packages these into an apex_plan_packet for
    operator review. It explicitly must not run scripts, compute exact next-task rankings, traverse
    dependency graphs, scan blockers, rebuild the registry, or mutate any state. Every consequential
    action is expressed as a handoff request rather than a direct effect.
  relevant_to_kb_because:
    - "One of the three skills this KB exists to document."
    - "Defines the exact handoff contract to apex-sync and apex-session that the interconnection topic depends on."
  likely_not_relevant_for:
    - "Master-of-Arts workflow content (separate topic, separate sources)."
```

## 3. Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "raw/other/SKILL.md lines 11-91 (Skill Contract yaml block)"
      reason: "Single authoritative statement of process_scope.owns, hands_off_to_apex_sync, hands_off_to_apex_session, and boundaries.must_not_create."
      extraction_priority: high
    - section_ref: "raw/other/SKILL.md lines 139-153 (Procedure)"
      reason: "Operational sequence: load context -> capture -> epic -> decompose -> propose dependencies -> priority/urgency/focus -> gate and hand off."
      extraction_priority: high
    - section_ref: "raw/other/SKILL.md lines 155-190 (Failure Modes)"
      reason: "Nine named failure modes with trigger/correction pairs, including deterministic_ranking_requested and state_mutation_requested, which are the exact failure modes that misuse would trip."
      extraction_priority: high
    - section_ref: "raw/other/SKILL.md lines 251-265 (Completion Gate)"
      reason: "Ten boolean completion checks; apex_sync_handoff_present_when_needed and apex_session_handoff_present_when_needed are the two checks that prove the boundary held."
      extraction_priority: high
  reusable_definitions:
    - "status_enum: open | in-progress | blocked | done | deferred (raw/other/SKILL.md lines 46-53) — identical to apex-sync's H1 and apex-session's allowed_status_values; this is the shared vocabulary across all three skills."
    - "priority_policy: high=3, medium=2, low=1, with apex-plan assigning qualitative rationale and apex-sync computing exact ranking from the same weights (raw/other/SKILL.md lines 60-66)."
  reusable_processes:
    - "7-step procedure (raw/other/SKILL.md lines 139-153)."
```

## 4. Concept Candidates

```yaml
concept_candidates:
  - concept_slug: "qualitative-vs-exact-split"
    concept_label: "Qualitative proposal vs. exact deterministic computation"
    source_pointer: "raw/other/SKILL.md lines 60-71 (priority_policy, urgency_policy)"
    summary: "apex-plan assigns qualitative priority/urgency values and rationale; apex-sync uses the same policy weights/fields to compute exact ranking. Same field, two ownership tiers."
    confidence: high
  - concept_slug: "no-script-boundary"
    concept_label: "apex-plan runs no scripts"
    source_pointer: "raw/other/SKILL.md lines 73-76 (script_policy: scripts_allowed/bash_allowed/python_allowed all false)"
    summary: "apex-plan is explicitly forbidden from script/bash/python execution — all determinism is delegated to apex-sync's scripts/apex_sync.py."
    confidence: high
```

## 5. Entity Candidates

```yaml
entity_candidates:
  - entity_slug: "apex-plan-packet"
    entity_label: "apex_plan_packet"
    entity_type: artifact
    source_pointer: "raw/other/SKILL.md lines 194-249 (Output Requirements)"
    summary: "The sole primary output: plan_packet_metadata, project_capture_record, epic_record, proposed_task_records, dependency_plan, priority_urgency_focus_rationale, review_flags, handoff_requests, operator_gate."
    confidence: high
```

## 6. Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "apex-plan's package_path is .claude/skills/apex-plan/ and its durable paths are apex-meta/, apex-meta/harmonization/, apex-meta/epics/, apex-meta/registry/index.md, apex-meta/handoff/."
    source_pointer: "raw/other/SKILL.md lines 15-22"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "apex-plan hands off exactly 6 operations to apex-sync (exact_next_task_computation, dependency_graph_traversal, blocker_scan, registry_rebuild, drift_detection, exact_priority_urgency_unlock_sorting) and exactly 5 to apex-session (status_mutation, entity_update, session_progress_log, next_session_context, operator_confirmed_write)."
    source_pointer: "raw/other/SKILL.md lines 32-44"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "Every item in boundaries.must_not_create (lines 78-90) is exactly the union of the two hands_off_to lists — apex-plan's forbidden set is defined as identical to what it delegates, with no extra restrictions and no gaps."
    source_pointer: "raw/other/SKILL.md lines 32-44 vs 78-90"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C004
    claim: "The prior (untrusted) batch02-apex-plan.analysis.md's claims C001-C003 about apex-plan's purpose and packet shape are confirmed accurate against the live SKILL.md, despite having been recorded against a pointer_only, unhashed source."
    source_pointer: "ingest-analysis/batch02-apex-plan.analysis.md claims C001-C003, cross-checked against raw/other/SKILL.md lines 4, 13-17, 194-210"
    confidence: high
    claim_label: source_backed_summary
```

## 7. Uncertainty / Raw Source Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      The apex-plan package directory contains .dr.md/.pro.md/.v1.md variant files for several
      reference topics (dependency-and-priority-rules, operator-gate, planning-contract,
      source-basis, task-decomposition-rules) that have NO canonical non-suffixed counterpart at
      all — these five reference topics exist only as historical draft/production-thinking
      artifacts and are not part of the live SKILL.md's supporting_files list (raw/other/SKILL.md
      lines 93-137 names only 4 references: plan-cluster-contract, task-record-contract,
      decomposition-and-dependency-rules, priority-urgency-focus-policy). They were deliberately
      excluded from this KB's tracked corpus as non-canonical.
    source_pointer: ".claude/skills/apex-plan/references/ directory listing"
    proposed_handling: leave_as_gap
  - id: U002
    description: >
      All four *.pro.md files in .claude/skills/apex-plan/ (SKILL.pro.md, package-manifest.pro.md,
      references/*.pro.md, four total observed) are exactly 0 bytes, despite
      extraction-report.md documenting non-zero extracted_blocks (7 blocks) for at least one
      Prothinking-sourced extraction. This is a genuine data-integrity gap: extraction was recorded
      as producing content that is not present on disk. The prior audit
      (apex-plan-sync-session-workflow-v2/audit/FailureReport_HighImpact_CC_Testrun.md, finding P3)
      characterized the *.v1.md files as "byte-identical duplicates — cosmetic duplication," which
      is confirmed correct for .v1.md, but that finding did not separately flag the .pro.md files as
      empty — this is a new finding, not previously documented.
    source_pointer: ".claude/skills/apex-plan/*.pro.md (0 bytes); .claude/skills/apex-plan/extraction-report.md lines 9-11"
    proposed_handling: audit_item
  - id: U003
    description: >
      .v1.md files (SKILL.v1.md, package-manifest.v1.md, and four references/*.v1.md,
      templates/*.v1.md) are confirmed byte-identical (diff exit 0) to their non-suffixed
      canonical twins. This matches the prior audit's P3 finding exactly. Given extraction-report.md
      shows the naming convention is provenance-driven (.dr = DeepResearch source, .pro =
      Prothinking source), .v1.md most plausibly represents an intentional frozen version snapshot,
      not an accidental duplicate — a nuance the prior audit did not consider.
    source_pointer: ".claude/skills/apex-plan/SKILL.md vs SKILL.v1.md (identical, 264 lines each)"
    proposed_handling: leave_as_gap
```

## 8. Proposed Phase 2 Changes

```yaml
proposed_wiki_pages:
  summaries: []
  concepts:
    - "qualitative-vs-exact-split (new or fold into existing proposal-computation-mutation-split.md)"
  entities:
    - "entities/apex-plan.md (update source_refs to real copy_into_kb hashes; add U001/U002/U003 as Uncertainty section)"
audit_items:
  - "U002: apex-plan .pro.md files are empty despite extraction-report.md claiming non-zero extracted content."
manifest_updates: []
```

## 9. Compile Decision

Output tier is `compiled_full`. Continue into Phase 2 wiki compile once the operator issues `approve ingest`.
