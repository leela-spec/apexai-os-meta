---
title: "SWE-agent"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "swe-agent"
entity_type: "external_repo"
source_refs:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "claims B03-C011 through B03-C012; entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "agent-computer-interface"
review_flags: []
---

# SWE-agent

## Identity

```yaml
entity:
  label: "princeton-nlp/SWE-agent"
  type: "external_repo"
  aliases:
    - "SWE-agent"
```

## Source-Grounded Summary

SWE-agent is read in this KB purely for its Agent-Computer Interface (ACI) background documentation (`docs/background/aci.md`). Batch 03 extracted the ACI definition itself (B03-C011: the tools and interaction format that let an agent operate in a computer environment, with good ACI design materially improving results) and a set of concrete ACI design details that function as deterministic guardrails: linting before edits are accepted, a bounded file viewer, succinct full-directory search results, and explicit success text for empty command output (B03-C012). SWE-agent is treated as comparative implementation-pattern material, not as an authority over Claude Code tool design.

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    rationale: "Sole ingested source for this entity; ranked first (and only) because all claims trace to this batch's reading of aci.md."
    coverage: "B03-C011 (ACI definition and importance), B03-C012 (concrete ACI guardrail details)."
```

## Macro / Meso / Micro

### Macro

SWE-agent contributes one reusable idea: deliberate tool/interaction design (an "agent-computer interface") is itself a design surface that materially affects agent performance, and that surface benefits from deterministic guardrails around tool output (linting, bounded viewers, succinct search results, explicit empty-output handling).

### Meso

The ACI concept (B03-C011) frames tool and interaction design as a first-class concern rather than an afterthought. The concrete details batch03 extracted (B03-C012) are notable because they resemble deterministic guardrails rather than model-judgment features: linting runs before an edit is accepted (a mechanical gate), the file viewer is bounded (a context-budget control), full-directory search results are kept succinct (output discipline), and empty command output gets explicit success text rather than silence (ambiguity reduction). This is why SWE-agent is grouped with Aider and BMAD under the same B03-C013 recommendation: Apex should copy the pattern (ACI/tool-output discipline), not the SWE-agent architecture itself.

### Micro

- B03-C011: "SWE-agent defines an Agent-Computer Interface as the tools and interaction format that allow an agent to operate in a computer environment, and states that good ACI design materially improves agent results." (`aci.md` lines 3-10)
- B03-C012: "SWE-agent's ACI includes design details that resemble deterministic guardrails: linting before edits are accepted, a bounded file viewer, succinct full-directory search results, and explicit success text for empty command output." (`aci.md` lines 11-17)

## Key Claims

```yaml
key_claims:
  - claim_id: B03-C011
    claim: "SWE-agent defines an Agent-Computer Interface as the tools and interaction format that allow an agent to operate in a computer environment, and states that good ACI design materially improves agent results."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; aci.md lines 3-10"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: B03-C012
    claim: "SWE-agent's ACI includes design details that resemble deterministic guardrails: linting before edits are accepted, a bounded file viewer, succinct full-directory search results, and explicit success text for empty command output."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; aci.md lines 11-17"
    confidence: "medium"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "What is a comparative example of deterministic tool-output discipline for agent-computer interaction?"
    leads_to: "claude-code-orchestration-design/entities/swe-agent.md"
    rationale: "SWE-agent's aci.md is the sole ingested source for ACI/tool-output-discipline patterns."
  - related_page: "claude-code-orchestration-design/entities/aider.md"
    relation: "Both are batch03 comparative external-repo entities feeding the same B03-C013 recommendation to copy patterns, not architectures."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_pointer: "aci.md lines 3-17"
    supports: "B03-C011 and B03-C012 claims and the agent-computer-interface concept"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "What is the minimum ACI/tool-output contract Apex should require for local agents or Codex-style repo executors remains an open question; only the SWE-agent example, not a finalized Apex contract, has been ingested."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; B03-Q004"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "SWE-agent's details are read only from its background/ACI doc; no source has been ingested on its broader agent-loop or evaluation architecture, so no claims beyond ACI should be attributed to this entity."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; source_files_read scope for swe-agent-aci"
    proposed_handling: "leave_as_gap"
```
