---
title: "apex-sync"
page_type: "entity"
kb_slug: "apex-plan-sync-session-workflow-v2"
entity_slug: "apex-sync"
entity_type: "tool"
source_refs:
  - source_id: "apex-sync-skill"
    source_path: "raw/notes/SKILL.md"
    source_hash: "698848fede4076f10bf3cca2e03d16ffbb9497e9fc9f8d03a851869a54af5b14"
    source_pointer: "lines 1-208 (full frontmatter, Objective, Required Outputs, Canonical Command Policy, Procedure, Validation Rules, Failure Modes, Completion Gate)"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-sync-sync-cluster-contract"
    source_path: "raw/notes/sync-cluster-contract.md"
    source_hash: "82bee71a2177026b3ff1f43443ebdbff88f24018fb4a0e87f70ff3ba7ce734a1"
    source_pointer: "lines 1-40 (package_role, B_SYNC_process_scope, only_write_exception)"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-sync-script-command-contract"
    source_path: "raw/notes/script-command-contract.md"
    source_hash: "ca11d205b22817dbe9dd34353a2ec3e944ee0c5c35e312b291daa11a962e2d6f"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-sync-registry-and-drift-rules"
    source_path: "raw/notes/registry-and-drift-rules.md"
    source_hash: "9916e0324e446b63156e1f07f21332d47d9d2ca8c9fd2a55c317496a274995b4"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-sync-scoring-and-focus-rules"
    source_path: "raw/notes/scoring-and-focus-rules.md"
    source_hash: "6df707394b0443282d10f1b699dbca3a28bc812dea5639dc76a1abc989b02425"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-11T09:56:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "../concepts/three-package-boundary.md"
  - "../concepts/isolation-with-overlap.md"
  - "../concepts/proposal-computation-mutation-split.md"
review_flags: []
---

# apex-sync

## Identity

```yaml
entity:
  label: "apex-sync"
  type: "tool"
  aliases: ["B_SYNC", "scripts/apex_sync.py wrapper"]
  package_path: ".claude/skills/apex-sync/"
  cluster: "B_SYNC"
  canonical_script_path: "scripts/apex_sync.py"
```

## Source-Grounded Summary

`apex-sync` is the deterministic read-side computation layer of the three-package system. Where
apex-plan proposes and apex-session confirms, apex-sync computes: it reads task frontmatter and
body content under `apex-meta/epics/` and delegates all exact arithmetic to
`scripts/apex_sync.py`, a standard-library-only Python script with no shell-out and no external
dependencies (sync-cluster-contract.md lines 12-19). What this project specifically decides about
"sync" is unusually strict: apex-sync produces exactly eight named reports and no others
(SKILL.md lines 45-54), defaults to dry-run on every command, and has exactly one narrow,
explicitly-flagged write exception — `apex-meta/registry/index.md`, writable only via
`registry --root . --json --dry-run false` (SKILL.md lines 95-106). Every other file category —
task files, handoff files, skill files, session artifacts — is declared unwritable by this
package (SKILL.md lines 174-175). apex-sync's own completion gate requires, as its final
condition, that "apex-plan and apex-session boundaries remain intact" (SKILL.md line 208) — the
isolation of the other two packages is written into apex-sync's own definition of "done."

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "apex-sync-skill"
    rationale: "Top-ranked by Phase0 keyword hit-count (71 hits against sync/registry/drift/blocker/score/stale/unlock/urgency) — the authoritative contract."
    coverage: "Full skill contract: required outputs, command policy, procedure, validation rules, failure modes, completion gate."
  - source_id: "apex-sync-script-command-contract"
    rationale: "Second-ranked (67 hits) — the canonical command-shape reference SKILL.md itself defers to before presenting any command."
    coverage: "scripts/apex_sync.py subcommand shapes, flags, JSON output, dry-run/exit-code policy."
  - source_id: "apex-sync-package-manifest"
    rationale: "64 hits — package inventory and invariants."
    coverage: "File set validation, source basis, forbidden claims, backup notes."
  - source_id: "apex-sync-sync-cluster-contract"
    rationale: "59 hits — the B_SYNC cluster-level boundary declaration, cross-verified against SKILL.md's own boundary claims in this analysis."
    coverage: "package_role, B_SYNC_process_scope, the single write exception."
  - source_id: "apex-sync-scoring-and-focus-rules"
    rationale: "51 hits — canonical source for the score/urgency/unlock-depth/focus-candidate computation the score subcommand performs."
    coverage: "Priority, urgency, dependency-satisfied actionability, unlock depth, stale detection, focus candidates."
  - source_id: "apex-sync-registry-and-drift-rules"
    rationale: "48 hits — canonical source for the registry and drift subcommands, the package's only write path."
    coverage: "Registry rebuild preview rules, drift detection, malformed task file handling."
```

## Macro / Meso / Micro

### Macro

apex-sync exists to give the system exactly one place where "what is true right now" gets computed
the same way every time, from the same script, with no room for an LLM's judgment to silently
substitute for arithmetic. Everything upstream of apex-sync (apex-plan's proposals) is explicitly
non-authoritative; everything downstream (apex-session's mutations) depends on apex-sync's reports
being trustworthy inputs, not on apex-sync trusting apex-session's or apex-plan's claims about
state.

### Meso

The read-only-with-one-exception design repeats a pattern seen across the whole system: default to
the safest possible mode, and require an explicit, hard-to-trigger-by-accident flag to leave it.
`--dry-run` defaults to `true` everywhere (SKILL.md line 95); the only command that may set it to
`false` is `registry`, and even then only that one command, only that one output file. This mirrors
apex-plan's `operator_gate` and apex-session's `operator_validation: confirmed` requirement
(see Isolation With Overlap) — three independent implementations of "nothing consequential by
default." apex-sync's failure-mode table (SKILL.md lines 179-191) is unusually exhaustive for a
read-only tool: it names 11 distinct review flags, several of which (`missing_task_id`,
`duplicate_task_id`, `missing_dependency_target`, `circular_dependency_risk`) exist specifically to
catch malformed *input* from the upstream package (apex-plan) without silently repairing it —
apex-sync reports the defect and continues, it does not fix apex-plan's proposal on its behalf.

### Micro

The H1 status enum (`open`, `in-progress`, `blocked`, `done`, `deferred`, SKILL.md lines 155-160)
is character-for-character identical to apex-plan's `status_enum` and apex-session's
`allowed_status_values` — verified directly across all three SKILL.md files during this KB run.
Actionability is defined precisely: a task is actionable only when status is `open` or
`in-progress`, every `depends_on` target exists and has status `done`, and `blocked_by` is empty or
references completed numeric blockers (SKILL.md lines 163-167) — this is the exact rule apex-plan
records `depends_on` for but never itself evaluates (see apex-plan entity page).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "apex-sync produces exactly 8 canonical reports: next_action, blocker, registry, stall, drift, score, focus_candidate, dependency_validation — and no others."
    source_pointer: "raw/notes/SKILL.md lines 45-54"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "The only non-dry-run command apex-sync allows is `registry --dry-run false`, and it may write only apex-meta/registry/index.md."
    source_pointer: "raw/notes/SKILL.md lines 95-106"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "apex-sync's completion gate explicitly requires that apex-plan and apex-session boundaries remain intact as its final condition."
    source_pointer: "raw/notes/SKILL.md line 208"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C004
    claim: "apex-sync has no fallback computation path if scripts/apex_sync.py fails — the required behavior on script_failed is to return the failure report and stop inference, making apex_sync.py a documented single point of failure for this package."
    source_pointer: "raw/notes/SKILL.md lines 145-147, 191"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C005
    claim: "apex-sync's H1 status enum is character-for-character identical to apex-plan's status_enum and apex-session's allowed_status_values."
    source_pointer: "raw/notes/SKILL.md lines 155-160 vs raw/other/SKILL.md lines 46-53 vs raw/refs/SKILL.md lines 45-50"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What happens if scripts/apex_sync.py crashes or is missing?"
    leads_to: "../concepts/isolation-with-overlap.md"
    rationale: "C004's single-point-of-failure finding is the most operationally important open risk documented for this package."
  - question: "Which package can actually write files, and under what condition?"
    leads_to: "../concepts/proposal-computation-mutation-split.md"
    rationale: "apex-sync's one narrow write exception contrasts with apex-session's broader (but still gated) mutation authority."
  - related_page: "apex-plan-sync-session-workflow-v2/entities/apex-plan.md"
    relation: "apex-plan hands off dependency validation, blocker scans, registry rebuild, drift detection, and exact ranking to apex-sync."
  - related_page: "apex-plan-sync-session-workflow-v2/concepts/three-package-boundary.md"
    relation: "apex-sync is the deterministic-computation package in the three-way disjoint ownership split."
```

## Evidence

```yaml
evidence:
  - source_id: "apex-sync-skill"
    source_pointer: "lines 43-64"
    supports: "C001"
  - source_id: "apex-sync-skill"
    source_pointer: "lines 78-109"
    supports: "C002"
  - source_id: "apex-sync-skill"
    source_pointer: "lines 145-147, 191, 208"
    supports: "C003, C004"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      C004 (single point of failure) is a documented architectural risk, independently confirmed
      by this KB run and matching the prior audit's finding P2. This KB records the risk
      accurately but does not and must not modify apex-sync's actual skill files to add a
      fallback — that is a design decision for whoever owns the apex-sync package, not a KB
      remediation.
    source_pointer: "raw/notes/SKILL.md lines 145-147"
    proposed_handling: planning_task_candidate
```
