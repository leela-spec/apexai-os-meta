---
title: "Rerun Batch 03 — Handoffs, Validation, and Risk"
page_type: ingest_analysis
kb_slug: old-apex-full-orchestration-agent-kb
phase: ingest_phase_1_rerun
status: operator_gate_already_approved_for_rerun
created_at: "2026-07-06T22:45:00+02:00"
updated_at: "2026-07-06T22:45:00+02:00"
confidence: high
claim_label: source_grounded_analysis
phase_2_allowed: true
phase_2_approval_phrase: "approve ingest"
---

# Rerun Batch 03 — Handoffs, Validation, and Risk

## source_scope

This replacement Phase 1 batch analyzes handoff integrity, validation posture, routing safety, risk handling, and repeated-failure controls in the old managed agent KB. It connects those patterns to the finalized deterministic lint concepts that now exist in the target KB: repo-execution routing safety and historical-path authority safety.

## files_read

```yaml
files_read:
  validation_sources:
    - path: sources/primary/managed-agent-kb/meta_detective/ESSENCE.md
      pointer: "adversarial validation owns/does-not-own, confidence, verdict states"
    - path: sources/primary/managed-agent-kb/meta_detective/APPENDIX_INTERNAL_MODES.md
      pointer: "mode selection rule, standard validation flow, verdict definitions"
    - path: sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md
      pointer: "mode lock, exact-span before rewrite, one-file-before-many, closure by evidence"
    - path: sources/primary/managed-agent-kb/special_ops__ai_handling_routing/ESSENCE.md
      pointer: "routing minimum, route states, repo execution vs chat routing checks"
  deterministic_closure_sources:
    - path: outputs/synthesis/apex-kb-semantic-continuation-after-lint-closure.md
      pointer: "semantic meaning of lint-repo-execution-router and lint-historical-path-authority"
    - path: wiki/index.md
      pointer: "current retrieval notes and page set"
```

## source_grounded_claims

```yaml
claims:
  - id: A03-C001
    claim: "The old validation model requires source authority classification before trust, forwarding, approval, or semantic promotion."
    source_pointer: "meta_detective/ESSENCE.md / Core constraints; special_ops__ai_handling_routing/ESSENCE.md / Core doctrine"
    confidence: high
    claim_label: source_backed_summary

  - id: A03-C002
    claim: "Meta Detective verdicts use pass, revise, hold, needs_input, and escalate, giving validation outputs explicit routing outcomes instead of vague critique."
    source_pointer: "meta_detective/ESSENCE.md / Default verdicts; meta_detective/APPENDIX_INTERNAL_MODES.md / Verdict definitions"
    confidence: high
    claim_label: raw_source

  - id: A03-C003
    claim: "Meta Detective confidence tiers are VERIFIED, PROBABLE, WEAK, and UNSAFE, and are used for evidence-dependent claims."
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md / Confidence definitions"
    confidence: high
    claim_label: raw_source

  - id: A03-C004
    claim: "A substantial validation output should state evidence checked, evidence gap, stop condition, next owner, and next validator."
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md / Standard validation flow"
    confidence: high
    claim_label: raw_source

  - id: A03-C005
    claim: "Special Ops AI Handling Routing freezes task, non-task, target output, source authority, overload class, recommended surface, stop conditions, fallback path, validator, and confidence before routing."
    source_pointer: "special_ops__ai_handling_routing/ESSENCE.md / Minimal routing card"
    confidence: high
    claim_label: raw_source

  - id: A03-C006
    claim: "Repo-affecting work must use exact repo-relative paths and operation modes; this old doctrine now maps to the finalized repo-execution-router lint primitive in Apex KB."
    source_pointer: "special_ops__ai_handling_routing/ESSENCE.md / Core doctrine; semantic-continuation-after-lint-closure.md / semantic meaning of lint-repo-execution-router"
    confidence: high
    claim_label: source_backed_summary

  - id: A03-C007
    claim: "Historical old-agent paths may be preserved as source evidence but must not be treated as current runtime authority; this is now reinforced by the historical-path-authority lint primitive."
    source_pointer: "semantic-continuation-after-lint-closure.md / semantic meaning of lint-historical-path-authority"
    confidence: high
    claim_label: source_backed_summary

  - id: A03-C008
    claim: "Hygiene Clean requires mode lock before execution and closure by evidence only, which complements the Apex KB requirement to separate semantic synthesis from deterministic repo execution."
    source_pointer: "special_ops__hygiene_clean/ESSENCE.md / Operating doctrine"
    confidence: high
    claim_label: source_backed_summary

  - id: A03-C009
    claim: "Validation and routing safety are not just wiki themes; they are process controls that prevent semantic work from drifting into repo mutation and prevent old-source references from becoming active authority."
    source_pointer: "Apex KB SKILL.md / deterministic versus LLM ownership; semantic-continuation-after-lint-closure.md / current lifecycle position"
    confidence: high
    claim_label: source_backed_summary
```

## concepts_extracted

```yaml
concepts_extracted:
  - slug: source-authority-before-verification
    label: "Source authority before verification"
    definition: "Classify whether evidence is primary, derived, working, speculative, stale, or current-authoritative before relying on it."
    source_pointer: "meta_detective/ESSENCE.md; special_ops__ai_handling_routing/ESSENCE.md"
    phase2_value: high

  - slug: verification-verdict-packet
    label: "Verification verdict packet"
    definition: "A validation output with artifact, evidence checked, findings, verdict, evidence gap, stop condition, owner, validator, and handoff target."
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md / Standard validation flow"
    phase2_value: high

  - slug: repo-execution-routing-safety
    label: "Repo execution routing safety"
    definition: "A boundary rule and lintable contract that separates semantic KB work from repo-affecting execution."
    source_pointer: "semantic-continuation-after-lint-closure.md / lint-repo-execution-router"
    phase2_value: high

  - slug: historical-path-authority-safety
    label: "Historical path authority safety"
    definition: "A boundary rule that old paths remain source evidence unless current runtime authority is separately established."
    source_pointer: "semantic-continuation-after-lint-closure.md / lint-historical-path-authority"
    phase2_value: high

  - slug: closure-by-evidence-only
    label: "Closure by evidence only"
    definition: "No finding closes by silence, omission, or later prose cleanup; closure needs a source, diff, test, file state, or report."
    source_pointer: "special_ops__hygiene_clean/ESSENCE.md / Operating doctrine"
    phase2_value: high
```

## entities_extracted

```yaml
entities_extracted:
  - id: meta_detective
    role_in_validation: adversarial_validator
    key_outputs: [source_evidence_check, contradiction_audit, boundary_verdict, risk_packet, validation_verdict_packet]
    source_pointer: "meta_detective/ESSENCE.md; meta_detective/APPENDIX_INTERNAL_MODES.md"

  - id: special_ops__ai_handling_routing
    role_in_validation: advisory_execution_surface_router
    key_outputs: [routing_minimum, source_authority_card, repo_execution_router, fallback_path]
    source_pointer: "special_ops__ai_handling_routing/ESSENCE.md"

  - id: special_ops__hygiene_clean
    role_in_validation: structural_QA_and_closure_validator
    key_outputs: [pointer_integrity_check, stale_state_check, closure_evidence_check]
    source_pointer: "special_ops__hygiene_clean/ESSENCE.md"

  - id: deterministic_lint_primitives
    type: finalized_process_infrastructure
    members: [lint-repo-execution-router, lint-historical-path-authority]
    source_pointer: "semantic-continuation-after-lint-closure.md / deterministic_closure_summary"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: A03-T001
    tension: "The old system has execution-control roles, but this Apex KB semantic rerun must not become an execution-control mutation."
    disposition: "Write only semantic KB artifacts and postflight prompt/report surfaces; do not edit scripts or adjacent Apex systems."
    confidence: high

  - id: A03-T002
    tension: "Historical paths are useful source pointers but unsafe as current authority."
    disposition: "Use source_path/source_pointer language; add raw-source reopen triggers before any runtime use."
    confidence: high
```

## open_questions

```yaml
open_questions:
  - id: A03-Q001
    question: "Which recorded real-surface findings from finalized lint reports require semantic rewrite versus later deterministic cleanup?"
    blocker: false
  - id: A03-Q002
    question: "Should repo-execution routing safety remain one concept page or become a reusable Apex-wide lint/audit doctrine page?"
    blocker: false
```

## proposed_phase_2_wiki_targets

```yaml
summaries:
  - handoff-validation-and-risk-doctrine
  - deterministic-execution-safety-after-lint-closure
concepts:
  - validation-and-routing-guardrails
  - repo-execution-routing-safety
  - migration-safety-patterns
entities:
  - meta-detective-internal-modes
```

## phase_gate_statement

```yaml
phase_2_gate:
  required_phrase: approve ingest
  status_for_this_rerun: approved
```
