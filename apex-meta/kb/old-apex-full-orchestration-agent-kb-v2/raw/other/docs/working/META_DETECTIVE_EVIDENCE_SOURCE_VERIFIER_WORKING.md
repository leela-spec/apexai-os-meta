# META_DETECTIVE_EVIDENCE_SOURCE_VERIFIER_WORKING

Status: working  
Owner: meta_detective  
Primary validator: special_ops__hygiene_clean  
Not accepted canon by storage alone  
Not a separate agent  
Not a separate KB root  
Does not execute or mutate truth  
Metric convention: all EVD / IMP / RSK scores use the active 1-100 scale only.

## Purpose

The Evidence & Source Verifier mode checks whether the artifact under review is grounded in the correct authority layer and whether its claims are supported enough for the requested action.

## Activation triggers

- source hierarchy affects the verdict
- evidence is weak, missing, stale, or contested
- a summary may be replacing a primary source
- citation, path, or file authority matters
- source/candidate/canon state is unclear
- output will be reused, committed, routed, or promoted

## Owns

- source authority classification
- evidence sufficiency review
- source/candidate/canon status check
- citation and path validity pressure
- confidence tier assignment for evidence-dependent claims

## Does not own

- patch application
- primary execution
- final strategy choice
- KB placement decision
- taxonomy design
- runtime config authority

## Input shape

```yaml
review_input:
  artifact_under_review:
  claimed_sources: []
  required_decision:
  expected_authority_level:
  known_gaps: []
```

## Output shape

```yaml
evidence_source_verdict:
  source_map:
    - source:
      tag: PRIMARY | DERIVED | WORKING | SPECULATIVE | STALE
      authority_scope:
      status:
  strongest_source:
  missing_source:
  conflict:
  confidence: VERIFIED | PROBABLE | WEAK | UNSAFE
  verdict: pass | revise | hold | needs_input | escalate
  required_next_evidence:
```

## Handoff partners

- `special_ops__knowledge_bank` for source/candidate/canon placement questions
- `special_ops__hygiene_clean` for pointer, path, stale-state, or structural QA questions
- `meta_ops` when missing evidence blocks execution routing
- `meta_strategy` when evidence changes the recommendation logic

## Failure modes

- polished summary is treated as primary truth
- source scope is overextended
- stale source silently outranks current source
- missing source is hidden by confident wording
- two primary sources conflict but the conflict is averaged away
- 1-5 metric scale is used instead of 1-100

## Template snippet

```md
## Evidence & source check

| Source | Tag | Authority scope | Evidence strength | Issue |
|---|---|---|---|---|
|  | PRIMARY / DERIVED / WORKING / SPECULATIVE / STALE |  | VERIFIED / PROBABLE / WEAK / UNSAFE |  |

Verdict: pass / revise / hold / needs_input / escalate  
Required next evidence:  
Stop condition:  
```

## Candidate KB target

- `BEST_PRACTICES.md` for the source-authority-before-verification practice
- `TEMPLATES.md` for the source/evidence verification checklist
- `MISTAKES.md` for summary elevation and missing-source failure patterns
