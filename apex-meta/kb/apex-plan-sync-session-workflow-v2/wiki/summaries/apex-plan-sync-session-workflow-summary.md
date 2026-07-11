---
title: "Apex Plan Sync Session Workflow Summary"
page_type: "summary"
kb_slug: "apex-plan-sync-session-workflow-v2"
summary_slug: "apex-plan-sync-session-workflow-summary"
source_refs:
  - source_id: "apex-plan-skill"
    source_path: "raw/other/SKILL.md"
    source_hash: "a83172f1d3f075273ca05a7e91254ed65ef77294a7519f74e94267c1ff3629cf"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-sync-skill"
    source_path: "raw/notes/SKILL.md"
    source_hash: "698848fede4076f10bf3cca2e03d16ffbb9497e9fc9f8d03a851869a54af5b14"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-session-skill"
    source_path: "raw/refs/SKILL.md"
    source_hash: "c45445a3499990275483e0103b7cfc7c1e5b35e7ed0c3ab48d3556fb6902537c"
    source_pointer: "full file"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-11T10:10:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "../concepts/three-package-boundary.md"
  - "../concepts/proposal-computation-mutation-split.md"
  - "../concepts/operator-gated-phase-boundary.md"
  - "../concepts/isolation-with-overlap.md"
related_entities:
  - "../entities/apex-plan.md"
  - "../entities/apex-sync.md"
  - "../entities/apex-session.md"
review_flags: []
---

# Apex Plan Sync Session Workflow Summary

## Core Summary

Three Claude Code skill packages — `apex-plan`, `apex-sync`, and `apex-session` — jointly
implement a system where planning proposals, deterministic computation, and confirmed state
mutations are kept in three structurally separate states that are never allowed to collapse into
each other silently. `apex-plan` captures projects, decomposes work into epics/tasks, and proposes
qualitative dependency/priority/urgency/focus rationale, packaged as an `apex_plan_packet` for
operator review — it has zero script execution surface of its own. `apex-sync` computes eight
exact, deterministic reports (next action, blocker, registry, stall, drift, score, focus
candidate, dependency validation) via the standard-library-only `scripts/apex_sync.py`, defaulting
to dry-run everywhere except one narrow, explicitly-flagged registry-write exception. `apex-session`
converts task/session evidence into gated mutation records (confirmed only once
`operator_validation: confirmed` is present) and four persistent H6 handoff artifacts (`task_plan.md`,
`findings.md`, `progress.md`, `next-session.md`) that carry context forward across sessions.

## What This Adds

```yaml
adds:
  - "Durable, hashed, copy_into_kb source custody for all three skill packages' canonical files (31 sources total), replacing the prior pointer_only/Windows-path records that this KB's own audit found unverifiable."
  - "A corrected topic-registry.json schema (slug/name) enabling 5 separately and correctly computed Adaptive Ranked Source Sets, after discovering the wrong schema (topic_id/title) silently collapses all topics into one 'unnamed' bucket -- the concrete mechanism behind the operator's original 'wrong signal words' suspicion."
  - "A fifth topic and tracked source pair covering the previously-orphaned Master of Arts workflow research (ProcessRanking_GPT&MasterOA.md and the Hermes Workflow Example Database)."
clarifies:
  - "The three-way handoff triangle is verified consistent by direct cross-comparison of all three live SKILL.md files during this KB run, not merely asserted."
  - "Isolation (disjoint process_scope ownership) and overlap (shared status vocabulary, mirrored boundary assertions, shared gate discipline) are two distinct, both-necessary design properties -- see Isolation With Overlap."
limits:
  - "No runtime/session-transcript evidence was available to confirm the handoff triangle or routing behavior actually holds in a live multi-turn session -- all claims here are contract-level (from the SKILL.md text itself), not execution-observed."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "apex-plan-skill"
    rationale: "120 hits under apex-plan-contract -- the single highest-ranked source for its own package's topic."
    coverage: "apex-plan's full contract."
  - source_id: "apex-session-skill"
    rationale: "131 hits under apex-session-contract -- the highest single-file hit count of any SKILL.md across all three packages, reflecting apex-session's comparatively larger and more granular contract text."
    coverage: "apex-session's full contract."
  - source_id: "apex-sync-skill"
    rationale: "71 hits under apex-sync-contract -- the top-ranked source for its package's topic."
    coverage: "apex-sync's full contract."
  - source_id: "plan-sync-session-interconnection"
    rationale: "Cross-cutting topic covering all three packages' handoff and boundary language together."
    coverage: "The handoff triangle and shared gate/vocabulary overlap."
```

## Macro / Meso / Micro

### Macro

The system exists to let an operator delegate real planning and execution work to Claude Code
skills without either (a) losing the ability to review before anything consequential happens, or
(b) having planning judgment, computed fact, and confirmed history become indistinguishable in the
output. Three packages, three epistemic states, one operator-in-the-loop discipline repeated three
times in three different shapes.

### Meso

Each package's procedure ends in a structurally similar place: apex-plan's procedure ends in
"Gate and hand off" (present, don't mutate); apex-sync's procedure ends in a completion gate
requiring the sibling packages' boundaries to remain intact; apex-session's procedure ends in
validating the final output set against the package manifest and H1 status values before
returning. None of the three packages treats "I produced output" as equivalent to "the work is
done" — each has its own explicit completion gate as a separate, checked step.

### Micro

Concretely, this KB run source-intook 31 canonical files across the three packages (9 apex-plan,
12 apex-session, 8 apex-sync) plus 2 Master-of-Arts research files, replacing 3 stale pointer_only
manifest entries. Phase0 corpus intelligence, re-run against the corrected topic-registry schema,
produced 5 separately-ranked topics instead of the single collapsed "unnamed" bucket a naive
(topic_id/title-schema) registry would have produced — directly demonstrated by comparing this
KB's own before/after Phase0 runs during this session.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "apex-plan, apex-sync, and apex-session own disjoint process_scope sets (6, 8, and 7 items respectively) verified by direct cross-read of all three live SKILL.md files."
    source_pointer: "raw/other/SKILL.md lines 25-31; raw/notes/SKILL.md lines 45-54; raw/refs/SKILL.md lines 27-34"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: ["../concepts/three-package-boundary.md"]
  - claim_id: C002
    claim: "All 31 of this KB's tracked sources are now durable copy_into_kb copies with verified SHA-256 hashes matching their live repository originals, replacing the prior 3 pointer_only, unhashed, Windows-path source records."
    source_pointer: "manifests/source-manifest.json (this KB run)"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "The topic-registry.json schema bug (topic_id/title vs. required slug/name) that this KB run discovered and fixed is the same bug present in old-apex-full-orchestration-agent-kb-v2's topic-registry.json, and is the concrete, confirmed mechanism behind the operator's original suspicion about 'previously wrong signal words.'"
    source_pointer: "scripts/apex_kb.py line 1038; this KB's manifests/phase0/topic-source-rankings.json before/after this session's fix"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What exactly does each of the three packages do, in detail?"
    leads_to: "../entities/apex-plan.md"
    rationale: "This summary is the entry point; each package's full contract is on its own entity page."
  - question: "How does the isolation-with-overlap design actually produce resilience?"
    leads_to: "../concepts/isolation-with-overlap.md"
    rationale: "Directly answers the operator's original framing question about redundant overlap and resilience."
  - question: "What was actually wrong with the previous run of this KB, and how was it fixed?"
    leads_to: "../index.md"
    rationale: "The master index consolidates every finding and fix from this KB run, including the topic-registry schema bug and the source-intake destination-collision bug."
  - related_page: "apex-plan-sync-session-workflow-v2/summaries/master-of-arts-workflow-research-summary.md"
    relation: "A separate, adjacent research lineage tracked in this same KB at the operator's request; not part of the implemented skill package."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      All claims in this summary and its linked pages are contract-level (derived from the three
      packages' own SKILL.md and reference text) rather than confirmed against a live runtime
      trace of the three skills actually cooperating on a real multi-step operator request. This
      is flagged consistently across every page in this KB rather than re-litigated per page.
    source_pointer: "no runtime source available to this KB"
    proposed_handling: revisit_source
```
