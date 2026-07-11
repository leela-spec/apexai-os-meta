---
analysis_id: "apex-plan-sync-session-workflow-v2-master-of-arts-workflow-research-analysis"
kb_slug: "apex-plan-sync-session-workflow-v2"
source_slug: "master-of-arts-workflow-research"
run_profile:
  output_tier: "compiled_full"
  safe_mode: "none"
source_payload_manifest_ref:
  path: "manifests/source-payload-manifest.json"
  status_at_analysis_time: "fresh"
created_at: "2026-07-11T09:48:00Z"
created_by: "apex-kb"
phase: ingest_phase_1
status: operator_review_needed
supersedes: "none (these two sources were previously untracked/orphaned in old-apex-full-orchestration-agent-kb-v2 -- see U001)"
---

# Phase 1 Ingest Analysis — Master of Arts workflow research

## 1. Source Identity

```yaml
source_identity:
  title: "Two operator-supplied research documents on the Master of Arts project workflow lineage"
  author_or_origin: "GPT (ProcessRanking) and an unspecified LLM/operator draft (Workflow Example Database); both explicitly draft-status, sourced from apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/"
  publication_or_creation_date: "unknown; committed to this repo 2026-07-11 (git commit 6c93bdb7, 'Add operator research folders')"
  source_authority_level: "tertiary"
  source_authority_rationale: "Both are explicitly self-labeled drafts ('Status: Draft ... not a Hermes implementation'; a ranking document proposing, not confirming, a process portfolio). Neither is a finished specification."
  source_scope: "ProcessRanking_GPT&MasterOA.md (222 lines): ranks 20 candidate 'process' patterns (Double Diamond, Scrum, CRISP-DM, ReAct, etc.) for automating Master-of-Arts-project workflows. Apex_Hermes_Workflow_Example_Database...v0_1 (1).md (1243 lines): a draft workflow database extracted from Master-of-Arts project source material, with a source_map (S01-S10+) ranking which source chats/docs are richest for workflow extraction."
  source_limitations:
    - "Both files reference external source material (Master Of Arts Meta.docx, Workshop Structure Analysis.txt, various chat histories) that is NOT part of this KB's tracked corpus -- only the two extraction/ranking documents themselves are tracked, not their upstream sources."
```

## 2. Source Summary

```yaml
source_summary:
  one_sentence_core: "These two documents are draft research artifacts, not finished specs: one ranks candidate process patterns for automating Master-of-Arts workflows, the other is a first-pass extraction of concrete workflow examples and their best source material, both explicitly pending further work."
  compact_summary: >
    ProcessRanking_GPT&MasterOA.md proposes a top-10 "process portfolio" (Goal-to-Verified-
    Artifact Loop, Durable Multi-Agent Task Graph/Kanban, Orchestrator-Worker Fan-Out, Handoff
    With Guardrails, Govern-Map-Measure-Manage, CRISP-DM, Diverge-Converge, Systems Engineering
    Flow, Sprint Artifact Loop, Chain-of-Verification Gate) selected for coverage and
    complementarity rather than raw score, plus a ranked 11-20 tier and an explicit
    do-not-prioritize-now tier. The Workflow Example Database is a draft source_map (S01-S10)
    ranking Master-of-Arts-related source material by extraction priority, with the top three
    being Prompt4WorkflowDBExtraction.md (governing schema), Master Of Arts Meta.docx (central
    project map), and Workshop Structure Analysis.txt.
  relevant_to_kb_because:
    - "The two files the operator specifically asked to have tracked and indexed in this KB run."
    - "Demonstrates a distinct research lineage (Hermes/Alfred/Master-of-Arts) adjacent to, but separate from, the apex-plan/sync/session skill contracts -- useful as a cross-reference for a future reader trying to understand how this repo's several KB/orchestration research threads relate to each other."
  likely_not_relevant_for:
    - "Direct claims about apex-plan/apex-sync/apex-session's current implemented behavior -- these two documents predate and are independent of that skill package."
```

## 3. Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "raw/papers/ProcessRanking_GPT&MasterOA.md lines 23-38 (Top 10 process portfolio table)"
      reason: "The core deliverable of the ranking document -- a ranked table with rationale and Hermes-target mapping per process."
      extraction_priority: high
    - section_ref: "raw/papers/ProcessRanking_GPT&MasterOA.md lines 42-46 ('Why these ten beat the raw top-scored list')"
      reason: "Explicit methodology note: raw score alone was rejected in favor of a coverage/complementarity criterion -- relevant to how ranking decisions should be justified in this KB's own topic-source-rankings, i.e. hit-count alone should not be read as a value judgment either."
      extraction_priority: medium
    - section_ref: "raw/papers/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md lines 1-5 (Scope/Status header)"
      reason: "Explicit draft-status declaration; must not be cited as a finished Hermes implementation."
      extraction_priority: high
    - section_ref: "raw/papers/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md lines 34-100+ (Source Map, S01-S10)"
      reason: "A ranked, reasoned list of upstream source material -- the extraction_priority/reason fields per source_id are directly reusable as an example of how to justify source ranking to an operator."
      extraction_priority: high
  reusable_definitions: []
  reusable_processes:
    - "Selection criteria for process ranking: Coverage, Complementarity, Hermes fit, Evidence/maturity, Risk control (ProcessRanking_GPT&MasterOA.md lines 9-17)."
```

## 4. Concept Candidates

```yaml
concept_candidates:
  - concept_slug: "coverage-over-raw-score-ranking"
    concept_label: "Rank by coverage/complementarity, not by raw score alone"
    source_pointer: "raw/papers/ProcessRanking_GPT&MasterOA.md lines 3-4, 42-46"
    summary: "The document explicitly rejects a pure highest-raw-score top-10 in favor of a coverage set that spans distinct workflow needs, demoting some individually-strong-but-narrow processes and promoting complementary ones."
    confidence: high
  - concept_slug: "draft-status-provenance-guard"
    concept_label: "Explicit draft/non-implementation status declared at the top of a source"
    source_pointer: "raw/papers/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md lines 3-5"
    summary: "The source itself states 'Status: Draft ... not a Hermes implementation. It does not create profiles, SOUL.md files, SKILL.md files, Kanban boards, or cron jobs' -- any wiki page citing this source must carry that caveat forward rather than presenting its contents as settled."
    confidence: high
```

## 5. Entity Candidates

```yaml
entity_candidates:
  - entity_slug: "prc-core-001"
    entity_label: "PRC-CORE-001 Goal-to-Verified-Artifact Loop"
    entity_type: other
    source_pointer: "raw/papers/ProcessRanking_GPT&MasterOA.md line 27"
    summary: "Ranked #1: 'intake -> goal contract -> source map -> brainstorm -> skeleton -> fill -> verify -> revise -> learn'; described as applicable to almost everything in the Master-of-Arts workflow set."
    confidence: high
  - entity_slug: "hermes-workflow-example-database-v0-1"
    entity_label: "Apex/Hermes Workflow Example Database v0.1"
    entity_type: artifact
    source_pointer: "raw/papers/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md lines 1-9"
    summary: "A draft, first-pass workflow database extracted from Master-of-Arts project context per the Prompt4WorkflowDBExtraction.md schema; explicitly not yet a Hermes implementation."
    confidence: high
```

## 6. Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The ProcessRanking document's top-10 selection explicitly favors portfolio coverage (10 complementary capabilities) over the 6 processes that score highest on raw impact/evidence/risk alone (PRC-CORE-001, PRC-VERIFY-001, PRC-MULTI-001, PRC-HANDOFF-001, PRC-RISK-001, PRC-SYS-001)."
    source_pointer: "raw/papers/ProcessRanking_GPT&MasterOA.md lines 42-46"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "The Workflow Example Database ranks its own upstream sources by extraction_priority in a structured YAML source_map (S01-S10+), with S01-S03 and S05-S07 marked extraction_priority: high and S04/S08/S09 marked medium."
    source_pointer: "raw/papers/Apex_Hermes_Workflow_Example_Database_Master_of_Arts_v0_1 (1).md lines 37-100"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "Before this KB run, neither of these two files was tracked in any KB manifest, wiki page, or index anywhere in this repository -- the only prior reference to either filename anywhere in the repo was inside a third raw document (OperatorResearch/Apex Hermes Claude Build Pack.md), listing them as candidate/expected filenames tagged 'if present,' which is narrative speculation, not an ingestion record."
    source_pointer: "grep across apex-meta/kb/ for both filenames prior to this KB run; git commit 6c93bdb7 diff"
    confidence: high
    claim_label: source_backed_summary
```

## 7. Uncertainty / Raw Source Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      Prior to this KB run these two files sat in old-apex-full-orchestration-agent-kb-v2/
      OperatorResearch/, which that KB's own source-manifest.json never scans (it only scans
      sources/ and raw/) -- so they were orphaned there too, not merely absent from this KB.
      This run resolves that specifically for apex-plan-sync-session-workflow-v2 by copying
      both files in as tracked, hashed, copy_into_kb sources; it does not modify
      old-apex-full-orchestration-agent-kb-v2 itself, which remains out of scope for this task.
    source_pointer: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/manifests/source-manifest.json (scans sources/, raw/ only)"
    proposed_handling: leave_as_gap
  - id: U002
    description: >
      A separate, more severe finding surfaced while setting up Phase 0 topic ranking for this
      batch: old-apex-full-orchestration-agent-kb-v2's manifests/topic-registry.json uses field
      names topic_id/title, but apex_kb.py's rank_topic_sources() (scripts/apex_kb.py line 1038)
      reads only slug/name, falling back to the literal string "unnamed" when name is absent.
      Because every one of that KB's 3 registered topics fell back to the same "unnamed" slug,
      Phase 0 silently overwrote all 3 topic rankings with only the LAST topic's
      (failure-evidence-and-recovery) keyword hits -- confirmed directly by inspecting
      manifests/phase0/topic-source-rankings.json there, which contains exactly one key,
      "unnamed". This means that KB's agent-architecture and resilient-iterative-workflows wiki
      summary pages were never backed by their own correctly-computed Adaptive Ranked Source
      Set. This is the concrete mechanism behind the operator's original suspicion that the
      prior run "ran on previously wrong signal words" -- the deterministic script itself is
      correct (confirmed by this KB's own successful 5-topic run once the slug/name schema was
      used), but the registry input file for that other KB used the wrong field names.
    source_pointer: "apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/manifests/topic-registry.json (topic_id/title schema); apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/manifests/phase0/topic-source-rankings.json (single 'unnamed' key); scripts/apex_kb.py line 1038"
    proposed_handling: audit_item
```

## 8. Proposed Phase 2 Changes

```yaml
proposed_wiki_pages:
  concepts:
    - "concepts/master-of-arts-workflow-research.md (new page)"
  summaries:
    - "summaries/master-of-arts-workflow-research-summary.md (new page)"
audit_items:
  - "U002: old-apex-full-orchestration-agent-kb-v2's topic-registry.json uses the wrong field schema (topic_id/title instead of slug/name), causing all 3 of its topics to collapse into one 'unnamed' Phase0 ranking bucket keyed by only the last topic's keywords. This is out of scope to fix in that KB under the current task, but is recorded here as the concrete answer to the operator's original suspicion."
manifest_updates: []
```

## 9. Compile Decision

Output tier is `compiled_full`. Continue into Phase 2 wiki compile once the operator issues `approve ingest`.
