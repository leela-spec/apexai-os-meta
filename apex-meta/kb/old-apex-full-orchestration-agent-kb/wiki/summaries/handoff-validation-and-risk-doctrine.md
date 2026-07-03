---
title: "Handoff, Validation, and Risk Doctrine"
page_type: summary
kb_slug: "old-apex-full-orchestration-agent-kb"
summary_slug: "handoff-validation-and-risk-doctrine"
source_refs:
  - source_id: "batch03-handoffs-validation-and-risk"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch03-handoffs-validation-and-risk.analysis.md"
    source_hash: "NA"
    source_pointer: "source_grounded_claims C001-C014; concepts_extracted"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T00:00:00Z"
updated_at: "2026-07-03T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - source-authority-before-verification
  - verification-verdict-packet
  - validator-executor-separation
  - routing-decision-card
  - repo-execution-router
  - approval-by-fluency
  - path-drift
  - constant-frame-control
related_entities:
  - meta-detective
  - special-ops-ai-handling-routing
  - special-ops-hygiene-clean
review_flags: []
---

# Handoff, Validation, and Risk Doctrine

## Core Summary

The old system treats validation as a structured control layer. Source authority classification comes before verification, handoff, patching, or approval. Substantial validation should end with a verdict, evidence gap, stop condition, and next owner or validator route.

The system explicitly rejects approval by fluency: an artifact should not pass because it looks coherent or polished without concrete evidence, read-back, diff, source check, test, schema, or acceptance criterion. Validators identify defects, evidence gaps, stop conditions, and required routes; they do not implement or self-approve the fix under review.

Repo-affecting work requires a pre-write route contract: exact repo-relative paths, operation class, target files, allowed and forbidden actions, pre-write checks, post-write checks, stop conditions, and commit strategy. Advisory routing must not silently become repo execution.

## What This Adds

```yaml
adds:
  - "A source-authority-first validation model."
  - "A verdict packet structure for high-risk outputs."
  - "A repo execution router pattern before connector-backed or local writes."
  - "Reusable anti-patterns for approval by fluency, summary elevation, path drift, retry theater, and advisory routing collapse."
clarifies:
  - "Meta Detective validates and routes; it does not patch or self-promote."
  - "AI Handling Routing advises route posture; it does not mutate config or become final approval authority."
limits:
  - "Current model/provider/cost/performance claims still require current verification in the run where they matter."
```

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Source authority classification is a pre-step gate before verification, handoff, or approval."
    source_pointer: "batch03-handoffs-validation-and-risk.analysis.md / C001"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [concepts/validation-and-routing-guardrails.md]
  - claim_id: C002
    claim: "Approval by fluency is an explicit failure pattern."
    source_pointer: "batch03-handoffs-validation-and-risk.analysis.md / C002"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [concepts/validation-and-routing-guardrails.md]
  - claim_id: C003
    claim: "Meta Detective returns verdicts and escalation recommendations without implementing the fix."
    source_pointer: "batch03-handoffs-validation-and-risk.analysis.md / C003"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [entities/old-agent-roles.md]
  - claim_id: C010
    claim: "Repo-affecting work requires exact path, operation, check, and commit contracts."
    source_pointer: "batch03-handoffs-validation-and-risk.analysis.md / C010"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [concepts/migration-safety-patterns.md]
```

## Contradictions

```yaml
contradictions:
  - "Validator roles can produce strong recommendations, but their authority stops before execution and self-approval."
```

## Open Questions

```yaml
open_questions:
  - "Should verdict packet generation become a skill, a workflow checklist, or a reusable KB template?"
```
