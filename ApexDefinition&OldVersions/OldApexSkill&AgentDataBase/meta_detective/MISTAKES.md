# MISTAKES

## Purpose

Accepted validated Meta Detective failure patterns and countermeasures.

This file records recurring ways Detective work can fail: approving without evidence, trusting summaries as truth, collapsing into execution, over-challenging without a decision path, allowing source/candidate/canon drift, merging Hygiene and Detective responsibilities, or hiding severity and stop conditions.

The durable non-drift doctrine for Meta Detective's internal validation modes lives in:

`OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md`

## Entry schema

```yaml
mistake_entry:
  id:
  status: accepted | deprecated
  pattern:
  trigger_conditions:
  countermeasure:
  evidence_refs:
  scores:
    score_scale: 1-100
    EVD:
    IMP:
    RSK:
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due:
```

## Score convention

All `EVD`, `IMP`, and `RSK` scores use the active **1-100** scale. No 1-5 metric scale is used in this managed KB.

## Accepted mistake patterns

### DET-MIS-001 — Approval by fluency

```yaml
mistake_entry:
  id: DET-MIS-001
  status: accepted
  pattern: Detective passes an artifact because it is coherent, polished, or structurally convincing without concrete evidence.
  trigger_conditions:
    - no source, file, diff, test, schema, or acceptance criterion is cited
    - reviewer uses aesthetic language instead of check evidence
    - output will be reused downstream but has not been verified
  countermeasure: Require a verification verdict packet that names exactly what was checked and assigns a confidence tier.
  evidence_refs:
    - AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md
    - AIHowTo/BasicFiles4Agents/Validation&Authority/Val&AuthResearchClaude.md
  scores:
    score_scale: 1-100
    EVD: 96
    IMP: 98
    RSK: 94
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

### DET-MIS-002 — Summary elevation

```yaml
mistake_entry:
  id: DET-MIS-002
  status: accepted
  pattern: A derived summary, chat recap, or polished working note is treated as more authoritative than the original artifact.
  trigger_conditions:
    - raw source exists but was not checked
    - summary conflicts with a saved file or spec
    - the artifact under review depends on buried constraints from an original file
  countermeasure: Apply source tags and use primary-source lock before any verdict or patch recommendation.
  evidence_refs:
    - AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md
    - AIHowTo/BasicFiles4Agents/Validation&Authority/Val&AuthResearchClaude.md
  scores:
    score_scale: 1-100
    EVD: 95
    IMP: 95
    RSK: 92
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

### DET-MIS-003 — Silent primary-source conflict resolution

```yaml
mistake_entry:
  id: DET-MIS-003
  status: accepted
  pattern: Detective chooses between conflicting primary sources by preference, recency, or narrative fit without surfacing the conflict.
  trigger_conditions:
    - two primary sources disagree
    - one source is a lock/governance file and another is a current managed file
    - a recommendation relies on resolving the conflict
  countermeasure: Mark the review `hold` or `escalate` and name the conflicting sources, authority scopes, and required decision owner.
  evidence_refs:
    - AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md
    - OpenClaw/07_finalopenclawsystem/managed/knowledge/KB_STARTING_SOURCE_MAP.md
  scores:
    score_scale: 1-100
    EVD: 92
    IMP: 94
    RSK: 95
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

### DET-MIS-004 — Validator becomes executor

```yaml
mistake_entry:
  id: DET-MIS-004
  status: accepted
  pattern: Detective finds a defect and directly rewrites, patches, promotes, or implements the fix it is supposed to validate.
  trigger_conditions:
    - Detective produces a patch instead of a verdict or handoff
    - Detective promotes its own learning queue entry
    - Detective absorbs Hygiene, Ops, Strategy, or Knowledge Bank responsibilities
  countermeasure: Return a verdict, required owner, validator, stop condition, and handoff path; do not execute the fix.
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/managed/agents/AGENT_INDEX.md
    - OpenClaw/07_finalopenclawsystem/managed/knowledge/OVERLAP_VALIDATION_MATRIX.md
    - OpenClaw/07_finalopenclawsystem/managed/processes/AGENT_HANDOFF_CONTRACTS.md
  scores:
    score_scale: 1-100
    EVD: 94
    IMP: 95
    RSK: 96
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

### DET-MIS-005 — Challenge theater

```yaml
mistake_entry:
  id: DET-MIS-005
  status: accepted
  pattern: Detective challenges everything broadly but does not identify the load-bearing assumption, concrete failure mode, or decision consequence.
  trigger_conditions:
    - review produces generic skepticism
    - no counter-evidence or kill condition is named
    - Strategy receives critique but no revision path
  countermeasure: Use the adversarial review template and isolate assumption, evidence, counter-evidence, failure signal, and verdict.
  evidence_refs:
    - Logic_Thinking_Iteration_Concepts.md
    - Logic Frameworks.md
    - Creative Strategy.md
  scores:
    score_scale: 1-100
    EVD: 82
    IMP: 90
    RSK: 80
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

### DET-MIS-006 — Candidate-to-canon leakage

```yaml
mistake_entry:
  id: DET-MIS-006
  status: accepted
  pattern: Source, staging, or learning-queue material is treated as accepted doctrine without validation and promotion.
  trigger_conditions:
    - learning queue content drives runtime decisions
    - source/staging files are used as final-system targets
    - evidence-only material is copied into accepted KB without owner, validator, scores, and review_due
  countermeasure: Enforce source/candidate/canon separation and route proposed promotions through the promotion ledger path.
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/managed/knowledge/AGENT_KB_LANES.md
    - OpenClaw/07_finalopenclawsystem/managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md
    - OpenClaw/07_finalopenclawsystem/managed/agents/AGENT_INDEX.md
  scores:
    score_scale: 1-100
    EVD: 93
    IMP: 95
    RSK: 96
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

### DET-MIS-007 — Retry theater

```yaml
mistake_entry:
  id: DET-MIS-007
  status: accepted
  pattern: The same failure is reviewed or corrected repeatedly without meaningful delta, creating loops instead of resolution.
  trigger_conditions:
    - second attempt does not state what substantively changed
    - the same defect recurs after revision
    - reviewer requests another vague retry instead of stopping or escalating
  countermeasure: On attempt two or later, require meaningful delta. If the same failure recurs, stop and escalate.
  evidence_refs:
    - AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md
    - AIHowTo/BasicFiles4Agents/Validation&Authority/Val&AuthResearchClaude.md
  scores:
    score_scale: 1-100
    EVD: 91
    IMP: 86
    RSK: 84
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

### DET-MIS-008 — Hygiene and Detective become interchangeable

```yaml
mistake_entry:
  id: DET-MIS-008
  status: accepted
  pattern: Structural QA and adversarial plausibility review are merged into one ambiguous review lane.
  trigger_conditions:
    - pointer integrity, stale state, or cleanup-risk issue is treated as adversarial doctrine
    - authority or contradiction challenge is routed as generic cleanup
    - mixed issue has no separate structural and adversarial dispositions
  countermeasure: Classify both finding types and route structural QA to Hygiene Clean while retaining adversarial validation in Detective.
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/managed/knowledge/OVERLAP_VALIDATION_MATRIX.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_ORIENTATION_WORKING.md
  scores:
    score_scale: 1-100
    EVD: 92
    IMP: 90
    RSK: 88
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

### DET-MIS-009 — Verdict lacks evidence or stop condition

```yaml
mistake_entry:
  id: DET-MIS-009
  status: accepted
  pattern: Detective returns pass, revise, hold, or escalate without naming evidence checked, evidence gap, stop condition, and next owner.
  trigger_conditions:
    - verdict says “looks good” or “needs work” without evidence
    - finding severity is hidden or softened
    - next owner or validator is missing
    - stop condition is implied but not stated
  countermeasure: Use the validation verdict packet with evidence checked, finding class, severity, confidence, evidence gap, stop condition, next owner, and next validator.
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_VERDICT_ESCALATION_SYNTHESIZER_WORKING.md
    - AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md
  scores:
    score_scale: 1-100
    EVD: 91
    IMP: 94
    RSK: 86
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

### DET-MIS-010 — Contradiction is averaged away

```yaml
mistake_entry:
  id: DET-MIS-010
  status: accepted
  pattern: Conflicting claims, sources, or constraints are blended into a compromise verdict instead of being recorded as a contradiction.
  trigger_conditions:
    - two sections or sources cannot both be true
    - recommendation violates a stated constraint
    - the review resolves conflict by tone or convenience
  countermeasure: Record the contradiction explicitly, assign severity, name the affected source or claim, and hold or escalate if the contradiction blocks trust.
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_CONTRADICTION_LOGIC_AUDITOR_WORKING.md
    - AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md
  scores:
    score_scale: 1-100
    EVD: 88
    IMP: 91
    RSK: 89
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

## Empty-state marker or initial entries

Initial accepted mistake patterns above are base-build patterns derived from primary source-authority, verification, audit, final-system governance, and Meta Detective internal-mode working files. Future mistake patterns must be promoted from `LEARNING_QUEUE.md` through the governed promotion path.
