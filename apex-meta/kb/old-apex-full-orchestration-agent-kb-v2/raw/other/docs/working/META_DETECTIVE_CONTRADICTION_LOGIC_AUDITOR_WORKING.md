# META_DETECTIVE_CONTRADICTION_LOGIC_AUDITOR_WORKING

Status: working  
Owner: meta_detective  
Primary validator: special_ops__hygiene_clean  
Not accepted canon by storage alone  
Not a separate agent  
Not a separate KB root  
Does not execute or mutate truth  
Metric convention: all EVD / IMP / RSK scores use the active 1-100 scale only.

## Purpose

The Contradiction & Logic Auditor mode checks whether a claim, recommendation, handoff, or KB candidate contains contradictions, unsupported conclusions, inference jumps, false equivalences, or claim/evidence mismatches.

## Activation triggers

- artifact makes a strong conclusion from weak evidence
- reasoning chain is unclear
- recommendations conflict with stated constraints
- multiple sections say incompatible things
- evidence does not support the verdict
- assumptions are presented as facts

## Owns

- contradiction detection
- inference-jump review
- claim/evidence mismatch review
- unsupported-conclusion surfacing
- weak-link analysis
- logic-gap classification

## Does not own

- writing the corrected argument
- deciding final strategy
- applying patches
- replacing Informatics Design's structure role
- replacing Hygiene Clean's structural QA role

## Input shape

```yaml
logic_review_input:
  artifact_under_review:
  central_claim:
  supporting_evidence: []
  stated_constraints: []
  known_counterclaims: []
```

## Output shape

```yaml
contradiction_logic_verdict:
  central_claim:
  findings:
    - finding:
      type: contradiction | inference_jump | unsupported_claim | assumption_as_fact | evidence_mismatch
      severity: critical | major | minor
      evidence:
      required_fix_owner:
  verdict: pass | revise | hold | needs_input | escalate
  stop_condition:
```

## Handoff partners

- `meta_strategy` when the recommendation logic needs revision
- `meta_ops` when contradiction blocks execution routing
- `special_ops__hygiene_clean` when structural ambiguity creates the logic defect
- `special_ops__informatics_design` when file shape or taxonomy creates repeated interpretive ambiguity

## Failure modes

- contradiction is averaged away instead of surfaced
- critique stays generic and does not name the exact inference gap
- logic review rewrites the artifact instead of returning a verdict
- structural issue is mislabeled as adversarial logic issue only
- evidence weakness is hidden under clean formatting

## Template snippet

```md
## Contradiction & logic audit

| Claim | Evidence | Logic issue | Severity | Required disposition |
|---|---|---|---|---|
|  |  | contradiction / inference jump / unsupported claim / assumption as fact / evidence mismatch | critical / major / minor |  |

Verdict: pass / revise / hold / needs_input / escalate  
Stop condition:  
Owner of correction:  
```

## Candidate KB target

- `TEMPLATES.md` for contradiction audit table
- `BEST_PRACTICES.md` for finding-type classification before verdict
- `MISTAKES.md` for contradiction averaged away and verdict without evidence
