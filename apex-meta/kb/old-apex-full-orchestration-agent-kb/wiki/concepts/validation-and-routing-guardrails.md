---
title: "Validation and Routing Guardrails"
page_type: concept
kb_slug: "old-apex-full-orchestration-agent-kb"
concept_slug: "validation-and-routing-guardrails"
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
related_entities:
  - meta-detective
  - special-ops-ai-handling-routing
  - special-ops-hygiene-clean
review_flags: []
---

# Validation and Routing Guardrails

## Definition

A guardrail set for high-risk handoffs and repo-affecting work. It requires source authority classification before verification or approval, verdict packets for substantial validation, validator/executor separation, explicit route contracts, and repo execution preflight before file mutation.

## Operating Rules

```yaml
rules:
  - "Classify source authority before trusting, forwarding, patching, or approving an output."
  - "Reject approval by fluency; require concrete evidence or acceptance criteria."
  - "Validators produce findings, verdicts, evidence gaps, stop conditions, and owner routes; they do not implement the fix under review."
  - "For repo-affecting work, freeze exact paths, operation class, allowed/forbidden actions, checks, stop conditions, and commit strategy before writing."
  - "Escalate or stop if a task touches runtime config, provider policy, model registry, permissions, or authority surfaces."
```

## Relationships

```yaml
related_concepts:
  - source-authority-before-verification
  - verification-verdict-packet
  - validator-executor-separation
  - repo-execution-router
related_entities:
  - meta-detective
  - special-ops-ai-handling-routing
  - special-ops-hygiene-clean
```

## Evidence

```yaml
evidence:
  - source_id: batch03-handoffs-validation-and-risk
    source_pointer: "C001"
    supports: "Source authority classification before verification or approval."
  - source_id: batch03-handoffs-validation-and-risk
    source_pointer: "C002"
    supports: "Approval by fluency as explicit failure pattern."
  - source_id: batch03-handoffs-validation-and-risk
    source_pointer: "C003"
    supports: "Validator/executor separation."
  - source_id: batch03-handoffs-validation-and-risk
    source_pointer: "C010"
    supports: "Repo execution router requirements."
```

## Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - "Should repo execution router checks become deterministic lint, a skill checklist, or both?"
```
