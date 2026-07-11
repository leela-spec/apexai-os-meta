---
title: "Master of Arts Workflow Research"
page_type: "concept"
kb_slug: "apex-plan-sync-session-workflow-v2"
concept_slug: "master-of-arts-workflow-research"
source_refs:
  - source_id: "master-of-arts-process-ranking-gpt"
    source_path: "raw/papers/ProcessRanking_GPT&MasterOA.md"
    source_hash: "2f5c385c982d7765f2445206866c1dc60094d83402a981c99c2af44bf0e850fa"
    source_pointer: "lines 1-77 (full ranking, top-10 table, rejected-tier list)"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-hermes-workflow-example-database-master-of-arts-v0-1"
    source_path: "raw/papers/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md"
    source_hash: "35af64d7dd9dc2b713430d6bf9dc57b1deaaab60454febfadfaafd6054677f9c"
    source_pointer: "lines 1-100 (Scope/Status header, Source Scan Summary, Source Map S01-S10)"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-11T10:08:00Z"
updated_at: "2026-07-11T10:08:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "isolation-with-overlap.md"
related_entities: []
review_flags: []
---

# Master of Arts Workflow Research

## Definition

This is a distinct, separate research lineage from the apex-plan/apex-sync/apex-session skill
contracts: draft operator research toward automating a personal project called "Master of Arts"
using a Hermes/Alfred-style agent orchestration approach. Both tracked sources are explicitly
self-labeled as drafts, not finished specifications — the workflow database states plainly
"Status: Draft ... not a Hermes implementation" (Apex_Hermes_Workflow_Example_Database...
line 5). What this project specifically decides here is a *methodology* for selecting and ranking
candidate automation processes (coverage-over-raw-score) and a *methodology* for ranking which
upstream source material is worth extracting from next (an explicit source_map with
extraction_priority per source) — not a finished workflow implementation.

## Operating Rules

```yaml
rules:
  - draft_status_must_be_preserved: "Any citation of the Workflow Example Database must carry forward its own stated caveat: it does not create profiles, SOUL.md files, SKILL.md files, Kanban boards, or cron jobs (source lines 3-5)."
  - ranking_methodology: "Coverage and complementarity across distinct workflow needs, not raw score alone, determines the top-10 process portfolio (ProcessRanking lines 3-4, 42-46)."
  - source_extraction_priority: "The workflow database's own source_map ranks 10 upstream sources by extraction_priority (high/medium), reasoned per source, not by arbitrary order (lines 37-100)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "apex-hermes-workflow-example-database-master-of-arts-v0-1"
    rationale: "336 hits under the master-of-arts-workflow-research topic (script-computed) -- overwhelmingly the dominant source for this concept by keyword density."
    coverage: "Draft workflow database: scope/status, source scan summary, ranked source_map (S01-S10), and (beyond the portion read for this analysis) further extracted workflow examples."
  - source_id: "master-of-arts-process-ranking-gpt"
    rationale: "85 hits -- second-ranked, the companion process-ranking document."
    coverage: "Top-10 process portfolio ranking, 11-20 tier, explicitly-deprioritized tier, selection methodology."
```

## Macro / Meso / Micro

### Macro

This research thread asks a narrower question than the apex-plan/apex-sync/apex-session system
does: not "how should three cooperating skill packages divide responsibility," but "which general
process patterns (Double Diamond, Scrum, CRISP-DM, ReAct, and eight others) best cover a specific
person's real portfolio of creative, administrative, and content-production workflows, and which
raw source material should be mined first to build a concrete workflow database." It is upstream
of any implementation — a selection-and-prioritization exercise, not a built system.

### Meso

Both documents apply the same underlying discipline seen in the skill-package research: rank by
a stated, multi-criterion methodology instead of a single score, and make the ranking rationale
explicit per item rather than asserting a bare ordered list. The ProcessRanking document scores
by Coverage, Complementarity, Hermes fit, Evidence/maturity, and Risk control (lines 9-17), and
explicitly explains why raw top-scorers were demoted in favor of complementary-but-individually-
weaker processes (lines 42-46). The Workflow Example Database's source_map applies the same
discipline to source material: each of 10 source entries gets an `extraction_priority` and a
`reason` field (lines 37-100), not just a rank number.

### Micro

The #1-ranked process, `PRC-CORE-001` Goal-to-Verified-Artifact Loop ("intake -> goal contract ->
source map -> brainstorm -> skeleton -> fill -> verify -> revise -> learn," ProcessRanking line
27), is structurally close to a macro-to-micro-and-back-up loop: it moves from an abstract goal
contract down to concrete filled content, then back up through verify/revise/learn. This is the
closest concrete example this KB found anywhere in its tracked sources to the "iterative macro to
meso to micro and back up" workflow model the operator described wanting documented — but it
describes a single-agent content-creation loop, not a multi-agent orchestration loop, and it comes
from a self-labeled draft ranking document, not an implemented or tested system (see Uncertainty).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The ProcessRanking document's top-10 selection explicitly favors a complementary-coverage portfolio over the 6 processes that score highest on raw impact/evidence/risk criteria alone."
    source_pointer: "raw/papers/ProcessRanking_GPT&MasterOA.md lines 42-46"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "The Workflow Example Database explicitly states it is a draft and not a Hermes implementation, and does not create profiles, SOUL.md files, SKILL.md files, Kanban boards, or cron jobs."
    source_pointer: "raw/papers/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md lines 3-5"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "The #1-ranked process (PRC-CORE-001) describes a 9-step loop from intake through goal contract, source map, brainstorm, skeleton, and fill, to verify, revise, and learn -- the closest match in this KB's tracked corpus to a macro-to-micro-and-back iterative model, though scoped to single-agent content creation rather than multi-agent orchestration."
    source_pointer: "raw/papers/ProcessRanking_GPT&MasterOA.md line 27"
    confidence: medium
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "Is there a documented macro-meso-micro iterative workflow pattern anywhere in this KB's sources?"
    leads_to: "isolation-with-overlap.md"
    rationale: "That page's Uncertainty section (U002) records the same content gap this page's Micro section identifies -- PRC-CORE-001 is the closest match found, but it is not a multi-agent orchestration example."
  - question: "What is the 'Master of Arts' project and how does it relate to the apex-plan/apex-sync/apex-session skills?"
    leads_to: "../summaries/master-of-arts-workflow-research-summary.md"
    rationale: "The summary page states explicitly that this is a separate research lineage, not a description of the currently implemented skill package."
```

## Evidence

```yaml
evidence:
  - source_id: "master-of-arts-process-ranking-gpt"
    source_pointer: "lines 1-77"
    supports: "C001, C003"
  - source_id: "apex-hermes-workflow-example-database-master-of-arts-v0-1"
    source_pointer: "lines 1-100"
    supports: "C002"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      Both sources reference substantial upstream material (Master Of Arts Meta.docx, Workshop
      Structure Analysis.txt, various named chat histories) that is not part of this KB's tracked
      corpus -- only the two extraction/ranking documents themselves are tracked. Claims here are
      scoped strictly to what these two documents state, not to the underlying project content
      they describe.
    source_pointer: "raw/papers/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md lines 11-30 (source list, none tracked in this KB)"
    proposed_handling: leave_as_gap
  - id: U002
    description: >
      Confidence on this page is set to medium/mixed overall (rather than high, as on the skill-
      contract pages) because both sources are self-labeled drafts describing a different,
      earlier-stage research effort than the implemented apex-plan/apex-sync/apex-session skills
      -- claims here describe what the research documents propose, not settled or implemented
      system behavior.
    source_pointer: "n/a (confidence-level rationale)"
    proposed_handling: leave_as_gap
```
