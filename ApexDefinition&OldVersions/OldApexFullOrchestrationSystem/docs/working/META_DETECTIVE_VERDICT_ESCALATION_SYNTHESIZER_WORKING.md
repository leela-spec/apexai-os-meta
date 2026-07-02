# META_DETECTIVE_VERDICT_ESCALATION_SYNTHESIZER_WORKING

Status: working  
Owner: meta_detective  
Primary validator: special_ops__hygiene_clean  
Not accepted canon by storage alone  
Not a separate agent  
Not a separate KB root  
Does not execute or mutate truth  
Metric convention: all EVD / IMP / RSK scores use the active 1-100 scale only.

## Purpose

The Verdict & Escalation Synthesizer mode converts selected Detective findings into one bounded validation verdict packet with evidence gaps, stop conditions, severity, and handoff targets.

## Activation triggers

- multiple Detective modes were used
- a final pass/revise/hold/escalate decision is needed
- structural and adversarial issues must be separated
- missing evidence must be turned into a concrete unblocker
- a handoff target must be named
- repeated failure or unsafe confidence blocks approval

## Owns

- final validation verdict synthesis
- severity and confidence consolidation
- evidence-gap statement
- stop-condition statement
- escalation recommendation
- handoff target identification

## Does not own

- implementing the fix
- applying a patch
- choosing the final strategy
- promoting KB candidates
- closing Hygiene findings
- mutating accepted truth

## Input shape

```yaml
verdict_input:
  artifact_under_review:
  selected_modes: []
  findings: []
  evidence_checked: []
  unresolved_gaps: []
  affected_boundaries: []
```

## Output shape

```yaml
validation_verdict_packet:
  artifact_under_review:
  overall_verdict: pass | revise | hold | needs_input | escalate
  confidence: VERIFIED | PROBABLE | WEAK | UNSAFE
  highest_severity: critical | major | minor | none
  evidence_checked: []
  evidence_gap:
  stop_condition:
  next_owner:
  next_validator:
  handoff_target:
  reusable_learning_candidate:
```

## Handoff partners

- `special_ops__hygiene_clean` for structural QA, pointer integrity, stale-state, cleanup-risk, and closure safety
- `special_ops__knowledge_bank` for KB placement, candidate/canon separation, and promotion-risk questions
- `meta_ops` for execution-owner, orchestration, or escalation routing
- `meta_strategy` for recommendation revision
- `special_ops__informatics_design` for structural design or taxonomy ambiguity
- `special_ops__ai_handling_routing` for model/tool-routing doctrine risk

## Failure modes

- verdict lacks evidence
- verdict lacks stop condition
- pass verdict hides a major or critical finding
- structural and adversarial findings are merged into one ambiguous issue
- escalation target is missing
- Detective proposes and validates its own correction
- 1-5 score scale is used instead of 1-100

## Template snippet

```md
## Meta Detective validation verdict packet

Artifact:  
Selected modes:  
Evidence checked:  

| Finding | Type | Severity | Confidence | Disposition |
|---|---|---|---|---|
|  | evidence / contradiction / boundary / risk / hygiene | critical / major / minor | VERIFIED / PROBABLE / WEAK / UNSAFE | pass / revise / hold / needs_input / escalate |

Overall verdict: pass / revise / hold / needs_input / escalate  
Evidence gap:  
Stop condition:  
Next owner:  
Next validator:  
Handoff target:  
Reusable learning candidate: yes / no  
```

## Candidate KB target

- `TEMPLATES.md` for final validation verdict packet
- `BEST_PRACTICES.md` for return verdict + evidence gap + stop/escalation path
- `MISTAKES.md` for verdict lacks evidence or stop condition
