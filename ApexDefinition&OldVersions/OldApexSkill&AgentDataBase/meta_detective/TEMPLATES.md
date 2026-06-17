# TEMPLATES

## Purpose

Accepted validated reusable templates for `meta_detective`.

Meta Detective templates are inspection instruments. They structure adversarial review, source-authority checks, evidence verification, contradiction surfacing, boundary protection, risk/failure-mode pressure, and escalation handoffs without turning Detective into the executor or patch author.

The durable doctrine for selecting and combining Meta Detective internal validation modes lives in:

`OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md`

## Template schema

```yaml
template_entry:
  id:
  status: accepted | deprecated
  use_when:
  template_body:
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

## Accepted templates

### DET-TPL-001 — Source / evidence verification checklist

```yaml
template_entry:
  id: DET-TPL-001
  status: accepted
  use_when: A claim, patch, recommendation, or handoff depends on file authority, source hierarchy, evidence sufficiency, citation/path validity, or source/candidate/canon status.
  evidence_refs:
    - AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md
    - AIHowTo/BasicFiles4Agents/Validation&Authority/Val&AuthResearchClaude.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_EVIDENCE_SOURCE_VERIFIER_WORKING.md
  scores:
    score_scale: 1-100
    EVD: 96
    IMP: 96
    RSK: 92
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

```md
## Source / evidence verification checklist

| Source | Tag | Authority scope | Evidence strength | Issue |
|---|---|---|---|---|
|  | PRIMARY / DERIVED / WORKING / SPECULATIVE / STALE |  | VERIFIED / PROBABLE / WEAK / UNSAFE |  |

Strongest usable source:  
Missing source:  
Conflicting source:  
Assumed claim requiring label:  

Verdict: pass / revise / hold / needs_input / escalate  
Required next evidence:  
Stop condition:  
```

### DET-TPL-002 — Meta Detective validation verdict packet

```yaml
template_entry:
  id: DET-TPL-002
  status: accepted
  use_when: Detective reviews whether an output is safe to trust, forward, commit, promote, or use as input to another agent.
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_VERDICT_ESCALATION_SYNTHESIZER_WORKING.md
    - AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md
  scores:
    score_scale: 1-100
    EVD: 93
    IMP: 96
    RSK: 90
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

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

### DET-TPL-003 — Contradiction audit table

```yaml
template_entry:
  id: DET-TPL-003
  status: accepted
  use_when: A claim, recommendation, KB candidate, or handoff may contain internal contradictions, inference jumps, unsupported conclusions, or claim/evidence mismatch.
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_CONTRADICTION_LOGIC_AUDITOR_WORKING.md
    - Logic Frameworks.md
  scores:
    score_scale: 1-100
    EVD: 86
    IMP: 92
    RSK: 84
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

```md
## Contradiction & logic audit

| Claim | Evidence | Logic issue | Severity | Required disposition |
|---|---|---|---|---|
|  |  | contradiction / inference jump / unsupported claim / assumption as fact / evidence mismatch | critical / major / minor |  |

Verdict: pass / revise / hold / needs_input / escalate  
Stop condition:  
Owner of correction:  
```

### DET-TPL-004 — Boundary / authority drift check

```yaml
template_entry:
  id: DET-TPL-004
  status: accepted
  use_when: A workflow, agent output, or KB update may collapse roles, mutate truth, skip validation, blur source/candidate/canon status, or violate config/promotion authority.
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/managed/agents/AGENT_INDEX.md
    - OpenClaw/07_finalopenclawsystem/managed/knowledge/OVERLAP_VALIDATION_MATRIX.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_BOUNDARY_AUTHORITY_GUARDIAN_WORKING.md
  scores:
    score_scale: 1-100
    EVD: 94
    IMP: 95
    RSK: 96
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

```md
## Boundary & authority check

| Surface / actor | Claimed role | Actual behavior | Boundary risk | Required route |
|---|---|---|---|---|
|  |  |  | clean / blurred / violated / blocked |  |

Required checks:

- Is the validator also acting as executor?
- Is candidate material treated as accepted truth?
- Is source/staging material being patched as final-system output?
- Is a learning queue entry self-promoted?
- Is Strategy executing, Ops validating itself, Hygiene mutating truth, or Detective patching?
- Is advisory routing being treated as runtime config authority?

Verdict: pass / revise / hold / needs_input / escalate  
Required owner:  
Required validator:  
Stop condition:  
```

### DET-TPL-005 — Risk / failure-mode red-team packet

```yaml
template_entry:
  id: DET-TPL-005
  status: accepted
  use_when: A recommendation, handoff, patch plan, or promotion candidate is high-impact, high-risk, irreversible, or dependent on uncertain assumptions.
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_RISK_FAILURE_RED_TEAMER_WORKING.md
    - Logic_Thinking_Iteration_Concepts.md
    - Creative Strategy.md
  scores:
    score_scale: 1-100
    EVD: 82
    IMP: 91
    RSK: 82
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

```md
## Risk & failure-mode red-team packet

| Failure scenario | Cause | Early warning signal | Kill / revise trigger | Owner |
|---|---|---|---|---|
|  |  |  |  |  |

Base-rate gap:  
Reversibility risk:  
Falsification test:  
Verdict: pass / revise / hold / needs_input / escalate  
```

### DET-TPL-006 — Detective to Hygiene handoff

```yaml
template_entry:
  id: DET-TPL-006
  status: accepted
  use_when: A finding includes structural QA, pointer integrity, stale-state, cleanup-risk, closure-safety, or mixed structural/adversarial issues.
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

```md
## Detective -> Hygiene handoff

Issue summary:  
Structural finding: yes / no  
Adversarial finding: yes / no  

| Finding | Class | Severity | Requested Hygiene check | Detective disposition |
|---|---|---|---|---|
|  | structural / adversarial / mixed | critical / major / minor |  |  |

Handoff target: special_ops__hygiene_clean  
Detective retains: authority / plausibility / contradiction / risk challenge  
Hygiene owns: structural QA / pointer integrity / stale state / cleanup risk / closure safety  
Stop condition:  
```

### DET-TPL-007 — Detective to Meta Ops escalation return

```yaml
template_entry:
  id: DET-TPL-007
  status: accepted
  use_when: A Detective finding blocks execution, creates owner ambiguity, or requires orchestration-level decision.
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/managed/agents/meta_ops.md
    - OpenClaw/07_finalopenclawsystem/managed/processes/AGENT_HANDOFF_CONTRACTS.md
  scores:
    score_scale: 1-100
    EVD: 84
    IMP: 88
    RSK: 80
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

```md
## Detective -> Meta Ops escalation return

Blocked action:  
Blocking finding:  
Required orchestration decision:  
Recommended next owner:  
Recommended validator:  

Execution may proceed? yes / no / only after input  
Stop condition:  
```

### DET-TPL-008 — Detective to Knowledge Bank promotion-risk check

```yaml
template_entry:
  id: DET-TPL-008
  status: accepted
  use_when: Source, candidate, learning queue, or accepted KB material may be crossing promotion boundaries.
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/managed/knowledge/AGENT_KB_LANES.md
    - OpenClaw/07_finalopenclawsystem/managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_BOUNDARY_AUTHORITY_GUARDIAN_WORKING.md
  scores:
    score_scale: 1-100
    EVD: 91
    IMP: 93
    RSK: 94
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

```md
## Detective -> Knowledge Bank promotion-risk check

Source material:  
Candidate target:  
Accepted-truth risk:  
Promotion packet present? yes / no  
Owner named? yes / no  
Validator named? yes / no  
Overlap check present? yes / no  

Verdict: pass / revise / hold / needs_input / escalate  
Knowledge Bank handoff needed: yes / no  
Stop condition:  
```

## Empty-state marker or initial entries

Initial accepted templates above are base-build instruments derived from primary source-authority, verification, audit, final-system governance, and Meta Detective internal-mode working files. Future templates must enter through `LEARNING_QUEUE.md` first unless separately promoted through the governed promotion path.
