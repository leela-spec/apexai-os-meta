---
title: "Dry-Run First State Policy"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "dry-run-first-state-policy"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 86-98; defaults to dry run"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 54-68; high-risk gates"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
related_concepts: []
related_entities: []
review_flags: []
---

# Dry-Run First State Policy

## Definition

Dry-run first state policy is the rule that any component capable of mutating canonical project, KB, or execution state must default to producing a preview or report of the intended change rather than applying it, and must require an explicit, affirmative gate (an approval, flag, or confirmation phrase) before the write executes. This concept answers the compile plan's `project_execution_index` core question `what_defaults_to_dry_run`, and is reinforced by the apex-application-patterns claim that operator gates are a first-class Apex design rule (B04-C005).

## Operating Rules

```yaml
rules:
  - "Any action that could alter canonical project, KB, or execution state must default to dry-run/preview mode."
  - "Applying the write requires an explicit affirmative gate: operator approval, an explicit allow-write flag, or a required confirmation phrase."
  - "A dry-run preview must summarize the intended delta (what would change) without requiring a full destructive pass to be understood."
  - "Success must not be claimed from the dry-run preview alone; task-closure requires proof the approved write actually happened (fetch-back / validation status)."
reads:
  - "target path"
  - "planned delta"
  - "permission gate / confirmation phrase"
writes:
  - "dry-run report (always)"
  - "actual write (only after explicit approval)"
token_efficiency: "A dry-run preview summarizes change intent without dumping full file bodies or reprocessing the whole target."
drift_controls: "Dry-run blocks accidental promotion, wrong-target writes, and premature Phase 2 synthesis before an explicit operator gate is cleared."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Names what_defaults_to_dry_run as a core project_execution_index question, directly alongside which components may propose vs compute vs write confirmed mutation records."
    coverage: "Frames the semantic-planning / deterministic-read / gated-write-mutation separation this policy sits inside."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the operator-gate and file-output/task-closure claims that make dry-run-then-approve a first-class Apex rule rather than an incidental habit."
    coverage: "Claims B04-C005 (operator gates before downstream use), B04-C013 (HALT/CLARIFY as routing controls against unsafe continuation), B04-C014 (file-output and task-closure proof required before success is claimed)."
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Confirms which gates are hard-enforced (must always halt) versus soft-enforced (style/preference), which bounds how strictly dry-run-first should be read as a rule."
    coverage: "Q002 hard_enforce list includes phase2_without_approve_ingest, write_outside_kb_root, raw_source_delete_or_mutation, kb_schema_overwrite_without_explicit_flag, destructive_archive_delete."
```

## Macro / Meso / Micro

### Macro

The `project_execution_index` separates project work into semantic planning, deterministic read-side computation, and gated write-side mutation, and asks directly what should default to dry-run inside that separation, alongside which components may propose state changes, which may compute reports, and which may write confirmed mutation records. Dry-run-first state policy is the compiled answer to that specific question: anything that can mutate canonical state previews first and writes only after an explicit gate, so that "propose" and "commit" stay visibly separate steps.

### Meso

This is reinforced from the apex-application-patterns side by three converging claims. Operator gates are explicitly first-class: skills must pause for approval before downstream use when validation is required (B04-C005). HALT and CLARIFY are defined as routing controls that stop guessing, scope expansion, unsafe continuation, and silent failure (B04-C013) — i.e. the default posture under uncertainty is to stop and ask, not to proceed and hope. And file-output/task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed (B04-C014) — meaning even after a write is approved, the policy does not consider it "done" until proof of the actual write is captured. Together these describe a lifecycle where mutation is proposed, gated, and then verified, never assumed.

### Micro

- Compile plan `project_execution_index` core question `what_defaults_to_dry_run`, alongside `which_components_may_propose_state_changes` and `which_components_may_write_confirmed_mutation_records` (compile plan lines ~84-96).
- B04-C005: operator gates pause downstream use pending explicit approval.
- B04-C013: HALT/CLARIFY stop guessing, scope expansion, unsafe continuation, silent failure.
- B04-C014: file-output/task-closure contracts require fetch-back and explicit validation status.
- Operator decision Q002 hard_enforce list names the specific high-risk gates that must not be soft-pedaled (e.g. `phase2_without_approve_ingest`, `write_outside_kb_root`, `raw_source_delete_or_mutation`), giving the concrete floor under this general policy.

### Operational observation (not a Phase 1 ingested claim)

As a self-referential illustration only — this is an observation about the current repo's tooling, not material ingested during Phase 1 semantic ingest, and it should not be read as an accepted KB doctrine claim: this KB's own `apex_kb.py` script implements the same shape at the tooling layer. Its module docstring states "Default mode is dry-run; writes require --allow-write and are restricted to the supplied --kb-root," and its `effective_dry_run()` helper returns true unless `--allow-write` is set and `--dry-run` is not — i.e. every command defaults to preview-only unless a write is explicitly and affirmatively requested (`apex-meta/scripts/apex_kb.py` lines 13-15, 142-143). This is cited only as illustrative, present-day evidence that the pattern already exists in this repo's own tooling; it is not offered as a Phase 1 semantic claim.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "project_execution_index treats what_defaults_to_dry_run as a core question for how gated write-side mutation should behave, alongside which components may propose, compute, or write confirmed mutation records."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, project_execution_index core_questions"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Operator gates are first-class in Apex design: skills must pause for explicit approval before downstream use when validation is required."
    source_pointer: "phase1-batch04-apex-application-patterns.md, claim B04-C005"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "File-output and task-closure contracts require explicit validation status and fetch-back proof before success is claimed; a dry-run preview alone does not constitute task closure."
    source_pointer: "phase1-batch04-apex-application-patterns.md, claim B04-C014"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "As an operational observation about this repo's current tooling (not a Phase 1 ingested claim), apex_kb.py defaults every command to dry-run and requires an explicit --allow-write flag before any file write executes, matching the dry-run-first pattern at the script layer."
    source_pointer: "apex-meta/scripts/apex_kb.py lines 13-15, 142-143 (operational observation, not Phase 1 source material)"
    confidence: "medium"
    claim_label: "behavioral_inference"
```

## Routes Here

```yaml
routes:
  - question: "Which parts of project execution may propose vs commit state changes?"
    leads_to: "claude-code-orchestration-design/concepts/gated-write-side-mutation.md"
    rationale: "Gated-write-side-mutation is the sibling project_execution_index concept describing the commit side this policy gates."
  - question: "What does a read-only deterministic report look like before any mutation is proposed?"
    leads_to: "claude-code-orchestration-design/concepts/deterministic-read-side-report.md"
    rationale: "Deterministic-read-side-report is the read-only counterpart that a dry-run preview typically resembles."
  - related_page: "claude-code-orchestration-design/concepts/operator-confirmed-mutation.md"
    relation: "Operator-confirmed-mutation describes the approval step that turns a dry-run preview into an applied write."
```

## Evidence

```yaml
evidence:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "project_execution_index core_questions, what_defaults_to_dry_run"
    supports: "Definition and Macro section."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claims B04-C005, B04-C013, B04-C014"
    supports: "Meso and Micro sections: operator gate, HALT/CLARIFY, and file-output proof discipline."
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "Q002 hard_enforce list"
    supports: "Micro section: concrete floor of hard-enforced high-risk gates."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Exact script flags, CLI surface, and enforcement mechanics for dry-run-first behavior across all Apex mutation surfaces (not only this KB's own tooling) are a deterministic S7+ concern, not settled Phase 2 doctrine."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, project_execution_index"
    proposed_handling: "leave_as_gap"
  - id: U002
    description: "what_defaults_to_dry_run remains listed as an open core question in the compile plan; this page states the general pattern and cites this repo's own script as one operational example, but does not close the question for every future Apex execution surface."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, project_execution_index core_questions"
    proposed_handling: "revisit_source"
```
