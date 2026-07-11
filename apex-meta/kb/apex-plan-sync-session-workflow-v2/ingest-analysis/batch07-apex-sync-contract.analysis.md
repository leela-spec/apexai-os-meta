---
analysis_id: "apex-plan-sync-session-workflow-v2-apex-sync-contract-analysis"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_slug: "apex-sync-contract"
run_profile:
  output_tier: "compiled_full"
  safe_mode: "none"
source_payload_manifest_ref:
  path: "manifests/source-payload-manifest.json"
  status_at_analysis_time: "fresh"
created_at: "2026-07-11T09:42:00Z"
created_by: "apex-kb"
phase: ingest_phase_1
status: operator_review_needed
supersedes: "ingest-analysis/batch03-apex-sync.analysis.md (pointer_only, unverifiable; content cross-checked and confirmed below)"
---

# Phase 1 Ingest Analysis — apex-sync contract

## 1. Source Identity

```yaml
source_identity:
  title: "apex-sync skill package"
  author_or_origin: "repo .claude/skills/apex-sync/, this repo, current HEAD"
  source_authority_level: "primary"
  source_authority_rationale: "Live skill definition; canonical script path scripts/apex_sync.py is independently confirmed to exist and run in this repo (verified during this KB run)."
  source_scope: "Defines apex-sync's deterministic read-side computation role, the only script it may run, the single write exception, and its completion gate."
  source_limitations:
    - "No .dr/.pro/.v1 variant sprawl in this package — unlike apex-plan, apex-sync's file set is clean (8 files, all canonical)."
```

## 2. Source Summary

```yaml
source_summary:
  one_sentence_core: "apex-sync computes deterministic read-side synchronization reports over apex-meta/epics/ task files via scripts/apex_sync.py and may write only apex-meta/registry/index.md, only via the registry subcommand with --dry-run false."
  compact_summary: >
    apex-sync owns 8 canonical reports (next_action, blocker, registry, stall, drift, score,
    focus_candidate, dependency_validation) computed by scripts/apex_sync.py. Default mode is
    dry-run; the single non-dry-run command allowed is `registry --dry-run false`, which may write
    only apex-meta/registry/index.md. It must not capture projects, decompose work, mutate task
    status, author handoff files, validate operator decisions, or write session narrative — those
    are explicitly apex-plan's and apex-session's territory.
  relevant_to_kb_because:
    - "The deterministic computation layer of the three-package system; this KB's own apex_kb.py mirrors the same operator-gated, script-owned, write-restricted design pattern apex-sync uses."
  likely_not_relevant_for:
    - "Master-of-Arts workflow content."
```

## 3. Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "raw/notes/SKILL.md lines 43-64 (Required Outputs: 8 canonical report names)"
      reason: "Defines the exact and only outputs apex-sync may produce; anything else is scope creep."
      extraction_priority: high
    - section_ref: "raw/notes/SKILL.md lines 78-109 (Canonical Command Policy)"
      reason: "The exact command shape, the dry-run default, and the single writable exception command."
      extraction_priority: high
    - section_ref: "raw/notes/SKILL.md lines 153-176 (Validation Rules)"
      reason: "H1 status enum and depends_on/actionability rules — shared vocabulary with apex-plan and apex-session."
      extraction_priority: high
    - section_ref: "raw/notes/SKILL.md lines 193-208 (Completion Gate)"
      reason: "Explicitly requires 'apex-plan and apex-session boundaries remain intact' as a gate condition, proving the isolation is a first-class completion criterion, not an afterthought."
      extraction_priority: high
  reusable_definitions:
    - "H1 status values: open, in-progress, blocked, done, deferred (raw/notes/SKILL.md lines 155-160) — identical enum to apex-plan's status_enum and apex-session's allowed_status_values."
  reusable_processes:
    - "9-step procedure: classify request -> check package boundary -> load command contract -> select subcommand -> preserve dry-run -> run computation -> return without scope expansion -> surface failures exactly -> completion gate (raw/notes/SKILL.md lines 111-151)."
```

## 4. Concept Candidates

```yaml
concept_candidates:
  - concept_slug: "single-write-exception"
    concept_label: "The one narrow write exception in an otherwise read-only package"
    source_pointer: "raw/notes/SKILL.md lines 95-106; raw/notes/sync-cluster-contract.md lines 27-33 (only_write_exception: apex-meta/registry/index.md)"
    summary: "apex-sync is read-side by design, with exactly one narrow, explicit write path (registry rebuild), gated behind an explicit --dry-run false flag rather than a default behavior."
    confidence: high
```

## 5. Entity Candidates

```yaml
entity_candidates:
  - entity_slug: "apex-sync-py"
    entity_label: "scripts/apex_sync.py"
    entity_type: tool
    source_pointer: "raw/notes/SKILL.md line 19, lines 78-109"
    summary: "The canonical Python script apex-sync delegates all exact computation to; standard-library only, no shell-out, no external dependencies."
    confidence: high
```

## 6. Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "apex-sync produces exactly 8 canonical reports and no others: next_action_report, blocker_report, registry_report, stall_report, drift_report, score_report, focus_candidate_report, dependency_validation_report."
    source_pointer: "raw/notes/SKILL.md lines 45-54"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "The only non-dry-run command the package allows is `python scripts/apex_sync.py registry --root . --json --dry-run false`, and it may write only apex-meta/registry/index.md."
    source_pointer: "raw/notes/SKILL.md lines 98-106"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "apex-sync's completion gate explicitly requires 'apex-plan and apex-session boundaries remain intact' as its final condition — the cross-package isolation is verified as part of apex-sync's own definition of done, not left implicit."
    source_pointer: "raw/notes/SKILL.md line 208"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C004
    claim: "The prior audit's P2 finding (apex-sync is a single point of failure with no fallback if scripts/apex_sync.py is missing or broken) is independently confirmed by this analysis: SKILL.md line 145-147 confirms the required behavior on script failure is to 'return the script failure report and stop inference' — there is no fallback computation path defined anywhere in the skill contract, so the audit's SPOF concern is a genuine, still-open architectural gap, not a resolved one."
    source_pointer: "raw/notes/SKILL.md lines 145-147, 191; apex-plan-sync-session-workflow-v2/audit/FailureReport_HighImpact_CC_Testrun.md finding P2"
    confidence: high
    claim_label: source_backed_summary
```

## 7. Uncertainty / Raw Source Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      The apex-sync SPOF risk (C004) remains unaddressed by this KB run — this KB documents the
      gap accurately but does not (and per apex-kb's own boundary rules, must not) modify
      apex-sync's actual skill files to add a fallback. This is recorded as an open architectural
      risk for whoever owns apex-sync's design, not a KB defect.
    source_pointer: "raw/notes/SKILL.md lines 145-147"
    proposed_handling: planning_task_candidate
```

## 8. Proposed Phase 2 Changes

```yaml
proposed_wiki_pages:
  entities:
    - "entities/apex-sync.md (update source_refs to real hashes; add C004/U001 SPOF finding explicitly to Uncertainty section)"
audit_items: []
manifest_updates: []
```

## 9. Compile Decision

Output tier is `compiled_full`. Continue into Phase 2 wiki compile once the operator issues `approve ingest`.
