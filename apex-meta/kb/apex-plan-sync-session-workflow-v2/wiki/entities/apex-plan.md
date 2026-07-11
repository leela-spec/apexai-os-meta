---
title: "apex-plan"
page_type: "entity"
kb_slug: "apex-plan-sync-session-workflow-v2"
entity_slug: "apex-plan"
entity_type: "tool"
source_refs:
  - source_id: "apex-plan-skill"
    source_path: "raw/other/SKILL.md"
    source_hash: "a83172f1d3f075273ca05a7e91254ed65ef77294a7519f74e94267c1ff3629cf"
    source_pointer: "lines 1-265 (full frontmatter, Skill Contract, Procedure, Failure Modes, Output Requirements, Completion Gate)"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-plan-package-manifest"
    source_path: "raw/other/package-manifest.md"
    source_hash: "b67bbfb44d21e9ba216f5290bc5bb3ddfeb5346aeabf74fac3a76755a343f08e"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-plan-extraction-report"
    source_path: "raw/other/extraction-report.md"
    source_hash: "0d51cf31efeb325b787a564a6aae8596fa728c98a278d8b62d054a3055da2343"
    source_pointer: "lines 1-11 (Sources: dr/pro provenance, extracted_blocks counts)"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-plan-decomposition-and-dependency-rules"
    source_path: "raw/other/decomposition-and-dependency-rules.md"
    source_hash: "d5794042467c1db18f0d4620c68ff105d22c5e1a1f605c5ca4830d63d27aac6c"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-plan-priority-urgency-focus-policy"
    source_path: "raw/other/priority-urgency-focus-policy.md"
    source_hash: "e0562ae86ae8db20136304043b2d8c6da1776f8f2a09ef2271a6a23d38de911d"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-11T09:55:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "../concepts/three-package-boundary.md"
  - "../concepts/isolation-with-overlap.md"
  - "../concepts/proposal-computation-mutation-split.md"
review_flags: []
---

# apex-plan

## Identity

```yaml
entity:
  label: "apex-plan"
  type: "tool"
  aliases: ["C_PLAN", "apex_plan_packet producer"]
  package_path: ".claude/skills/apex-plan/"
  cluster: "no explicit cluster code in SKILL.md; contrasts with apex-sync's B_SYNC and apex-session's C_SESSION"
```

## Source-Grounded Summary

`apex-plan` is a no-script, operator-gated project-planning skill. Its entire output is a single
artifact, the `apex_plan_packet` (SKILL.md line 13), assembled from nine required sections:
`plan_packet_metadata`, `project_capture_record`, `epic_record`, `proposed_task_records`,
`dependency_plan`, `priority_urgency_focus_rationale`, `review_flags`, `handoff_requests`, and
`operator_gate` (SKILL.md lines 199-208). It owns exactly six process-scope items — project
capture, project decomposition, dependency-proposal assignment, priority policy, urgency policy,
and focus-recommendation rationale (SKILL.md lines 25-31) — and explicitly hands off everything
else. `script_policy` sets `scripts_allowed`, `bash_allowed`, and `python_allowed` all to `false`
(SKILL.md lines 73-76): apex-plan is the only one of the three packages with zero execution
surface of its own. What this project specifically decides about "planning" is narrower than the
word usually implies: apex-plan never computes an exact next task, never traverses a dependency
graph, never rebuilds a registry, and never writes a file to disk on the operator's behalf — it
only proposes, and every proposal is qualitative, not exact.

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "apex-plan-skill"
    rationale: "Top-ranked by Phase0 keyword hit-count (120 hits against plan/epic/task/decomposition/dependency/priority/urgency/cluster/focus) — the single authoritative contract file."
    coverage: "Full skill contract: process_scope, boundaries, procedure, failure modes, output requirements, completion gate."
  - source_id: "apex-plan-extraction-report"
    rationale: "Second-ranked (105 hits) — reveals the provenance of the canonical file set itself (dr/pro source extraction, block counts) rather than describing plan behavior directly."
    coverage: "Extraction provenance metadata for the apex-plan package's own construction history."
  - source_id: "apex-plan-priority-urgency-focus-policy"
    rationale: "71 hits — the canonical source for the priority/urgency/focus rationale process_scope item."
    coverage: "Qualitative priority assignment, due_date urgency explanation, provisional focus recommendation rules."
  - source_id: "apex-plan-plan-cluster-contract"
    rationale: "63 hits — package-scope and boundary detail supporting SKILL.md's process_scope claims."
    coverage: "Cluster-level contract cross-referenced by SKILL.md's supporting_files list."
  - source_id: "apex-plan-decomposition-and-dependency-rules"
    rationale: "58 hits — canonical source for the decomposition and dependency-proposal process_scope items."
    coverage: "Work-decomposition rules, depends_on proposal rules, circular-dependency flagging."
```

## Macro / Meso / Micro

### Macro

apex-plan is the proposal layer of a three-package system that deliberately separates
"what should probably happen" from "what is exactly true" from "what has been confirmed to have
happened." It exists so that planning reasoning — which is inherently qualitative, judgment-laden,
and sometimes wrong — never gets to silently become deterministic fact (apex-sync's job) or a
confirmed state change (apex-session's job) without passing through an operator.

### Meso

Three structural patterns repeat throughout apex-plan's contract. First, every field that looks
exact is paired with an explicit "who computes the exact version" note: the priority policy
weights (`high: 3, medium: 2, low: 1`, SKILL.md lines 61-64) are the same weights apex-sync uses,
but SKILL.md line 65 assigns apex-plan only the qualitative rationale role while line 66 assigns
apex-sync the exact-ranking role over those same weights. Second, apex-plan's nine failure modes
(SKILL.md lines 158-190) are almost all "malformed input → return a degraded-but-safe default"
patterns (invalid status → `open`, invalid priority → `medium`) except for two which are pure
boundary-enforcement failure modes: `deterministic_ranking_requested` and
`state_mutation_requested` (SKILL.md lines 183-189), both of which correct by handing off to
another package rather than by producing a degraded answer. Third, the `boundaries.must_not_create`
list (SKILL.md lines 78-90) is not an independent policy — it is defined as exactly the union of
`hands_off_to_apex_sync` and `hands_off_to_apex_session` (SKILL.md lines 32-44). apex-plan is
forbidden from doing precisely what it already hands off, no more and no less; there is no gap
between "things apex-plan delegates" and "things apex-plan is disallowed from doing itself."

### Micro

At the level of individual fields: `depends_on` is an `integer_array` (SKILL.md lines 55-58) and
the rule that "all task IDs listed in `depends_on` must have status `done` before the task is
actionable" is defined here in apex-plan's contract even though apex-plan itself never evaluates
that rule — it only records the proposal and defers evaluation to apex-sync (SKILL.md lines 149,
232-234). The seven-step procedure (SKILL.md lines 141-153) ends, not with a write, but with "Gate
and hand off" (step 7): "Present the planning packet, review flags, and handoff requests to the
operator; do not mutate state" (SKILL.md line 153) — the terminal action of the entire skill is a
presentation, never a write.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "apex-plan's sole primary output is the apex_plan_packet, assembled from exactly nine required sections."
    source_pointer: "raw/other/SKILL.md lines 13, 199-208"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "apex-plan hands off exactly 6 operations to apex-sync and exactly 5 to apex-session, and its own must_not_create boundary list is defined as precisely that same 11-item union."
    source_pointer: "raw/other/SKILL.md lines 32-44 vs 78-90"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "apex-plan is the only one of the three packages with scripts_allowed, bash_allowed, and python_allowed all set to false — it has zero execution surface of its own."
    source_pointer: "raw/other/SKILL.md lines 73-76"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C004
    claim: "The priority_policy weights (high=3, medium=2, low=1) are shared verbatim with apex-sync, but ownership of the qualitative-rationale role vs. the exact-ranking role over the same weights is split explicitly between the two packages."
    source_pointer: "raw/other/SKILL.md lines 60-66"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C005
    claim: "Four of apex-plan's nine failure modes degrade to a safe default value (invalid_status_value -> open, invalid_priority_value -> medium) while two (deterministic_ranking_requested, state_mutation_requested) correct by handing off to another package rather than degrading."
    source_pointer: "raw/other/SKILL.md lines 158-190"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What happens if I ask apex-plan to just compute the next task itself?"
    leads_to: "../concepts/isolation-with-overlap.md"
    rationale: "Answered by the deterministic_ranking_requested failure mode (C005) and the isolation-with-overlap concept's handoff-triangle description."
  - question: "Why does apex-plan record depends_on if it never checks it?"
    leads_to: "../entities/apex-sync.md"
    rationale: "apex-sync is the package that evaluates depends_on against the H1 status enum for actionability."
  - related_page: "apex-plan-sync-session-workflow-v2/concepts/three-package-boundary.md"
    relation: "apex-plan is one of the three packages whose disjoint ownership this concept defines."
  - related_page: "apex-plan-sync-session-workflow-v2/concepts/proposal-computation-mutation-split.md"
    relation: "apex-plan is the 'proposal' side of the proposal/computation/mutation split."
```

## Evidence

```yaml
evidence:
  - source_id: "apex-plan-skill"
    source_pointer: "lines 11-91"
    supports: "C001, C002, C003, C004"
  - source_id: "apex-plan-skill"
    source_pointer: "lines 155-190"
    supports: "C005"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      apex-plan's package directory contains five reference topics (dependency-and-priority-rules,
      operator-gate, planning-contract, source-basis, task-decomposition-rules) that exist only as
      .dr.md/.pro.md variant pairs with no canonical non-suffixed file, and are not named in
      SKILL.md's supporting_files list at all. These are historical draft artifacts, deliberately
      excluded from this KB's tracked corpus as non-canonical.
    source_pointer: ".claude/skills/apex-plan/references/ (directory listing, not KB-tracked)"
    proposed_handling: leave_as_gap
  - id: U002
    description: >
      All four .pro.md files in the apex-plan package are 0 bytes despite extraction-report.md
      documenting 7 extracted_blocks for at least one Prothinking-sourced extraction. This is a
      genuine data-integrity gap in the live repository, not a KB artifact — flagged as an audit
      item rather than silently corrected, since apex-kb must not mutate skill package files.
    source_pointer: ".claude/skills/apex-plan/*.pro.md (0 bytes); raw/other/extraction-report.md lines 9-11"
    proposed_handling: audit_item
```
