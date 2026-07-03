---
title: "Old Agent Role System"
page_type: summary
kb_slug: "old-apex-full-orchestration-agent-kb"
summary_slug: "old-agent-role-system"
source_refs:
  - source_id: "batch02-agent-roles-and-doctrine"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch02-agent-roles-and-doctrine.analysis.md"
    source_hash: "NA"
    source_pointer: "source_grounded_claims C001-C013; entities_or_roles_extracted"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T00:00:00Z"
updated_at: "2026-07-03T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - persistent-agent-role
  - internal-mode-not-agent
  - negative-ownership-boundary
  - validator-like-role
  - specialist-lane
related_entities:
  - alfred
  - meta-ops
  - meta-strategy
  - meta-detective
  - special-ops-knowledge-bank
  - special-ops-informatics-design
  - special-ops-hygiene-clean
  - special-ops-prompts-workflows
  - special-ops-ai-handling-routing
review_flags:
  - "Historical role roster is evidence, not automatic current runtime architecture."
---

# Old Agent Role System

## Core Summary

The old role system is built around persistent role boundaries, specialist lanes, validator lanes, and internal modes. The indexed first-wave roles include Alfred, Meta Ops, Meta Strategy, Meta Detective, Knowledge Bank, Informatics Design, Prompts Workflows, AI Handling Routing, and Hygiene Clean.

Each role carries both positive ownership and negative ownership. The negative boundaries are a central anti-drift mechanism: roles are defined as much by what they must not own as by what they can do. Meta Detective and Hygiene Clean are validator-like lanes; Meta Ops is executor/orchestration-like; Meta Strategy is strategy/recommendation-like; the Special Ops roles are specialist lanes.

Meta Detective internal modes are not separate agents. They are validation lenses inside one adversarial validator role and should not automatically become permanent agents or separate KB roots.

## What This Adds

```yaml
adds:
  - "A role taxonomy for historical Apex orchestration behavior."
  - "A persistent-role versus internal-mode distinction."
  - "A durable negative-ownership boundary pattern."
clarifies:
  - "Validator-like roles check, route, and escalate without implementing their own fixes."
  - "Specialist lanes are bounded capability surfaces, not global authority surfaces."
limits:
  - "This page preserves the old role system as source-backed doctrine evidence; it does not authorize current runtime agent creation."
```

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The first-wave role set is explicitly indexed."
    source_pointer: "batch02-agent-roles-and-doctrine.analysis.md / C001"
    confidence: high
    claim_label: raw_source
    used_in_pages: [entities/old-agent-roles.md]
  - claim_id: C006
    claim: "Meta Detective internal modes are selection lenses inside one validator agent, not separate agents."
    source_pointer: "batch02-agent-roles-and-doctrine.analysis.md / C006"
    confidence: high
    claim_label: raw_source
    used_in_pages: [entities/meta-detective-internal-modes.md]
  - claim_id: C012
    claim: "Negative ownership boundaries are as important as positive capabilities."
    source_pointer: "batch02-agent-roles-and-doctrine.analysis.md / C012"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [concepts/migration-safety-patterns.md]
```

## Contradictions

```yaml
contradictions:
  - "The old role taxonomy is useful evidence but should not automatically become the current Apex/Claude-native permanent agent set."
```

## Open Questions

```yaml
open_questions:
  - "Which old roles should remain wiki doctrine only, and which should become current skills, workflows, or subagents?"
```
