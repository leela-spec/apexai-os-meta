# META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN

Status: working execution plan  
Owner: meta_detective  
Primary validator: special_ops__hygiene_clean  
Secondary validators: meta_ops, special_ops__knowledge_bank, special_ops__prompts_workflows  
Not accepted canon by storage alone  
Not a separate agent  
Not a separate KB root  
Does not execute or mutate truth by itself  
Metric convention: all EVD / IMP / RSK scores use the active 1-100 scale only.

## 1. Executive decision

Meta Detective should become the cross-agent watchdog for truth, process compliance, contradiction, drift, and escalation.

The prior five-mode model remains useful, but it is missing one first-class mode:

> Execution & Promptflow Compliance Auditor

This mode is required because the observed failure pattern is not only a source-authority problem, not only a contradiction problem, and not only a boundary problem. It is a process-compliance false positive: an agent can claim it followed the required execution method while the actual artifact/tool/write behavior shows otherwise.

## 2. Main architecture stance

| Question | Decision | Rationale |
|---|---|---|
| Should QA/Hygiene be core to Meta Detective? | Yes, as watchdog/audit capability | Detective must verify that agents actually followed required process, scope, and method. |
| Should Hygiene Clean be moved under Meta Detective? | Not now | Moving the whole lane risks ownership collapse between structural QA and adversarial validation. |
| Should Hygiene Clean remain separate? | Yes | Hygiene owns structural QA, pointer integrity, stale-state, cleanup-risk, and closure safety. |
| Should Detective audit Hygiene/Ops/Strategy outputs? | Yes | Detective must be able to block false compliance and self-validation. |
| Should a new permanent sub-agent be created now? | No | Start with internal mode and trigger rules; promote only after repeated evidence. |

## 3. Decision scoring

| Decision | EVD | IMP | RSK | Verdict |
|---|---:|---:|---:|---|
| Add Execution & Promptflow Compliance Auditor as a core internal Detective mode | 96 | 98 | 24 | Execute next |
| Make QA/Hygiene watchdogging explicit in Meta Detective doctrine | 90 | 95 | 36 | Execute next |
| Keep Hygiene Clean separate but auditable by Detective | 94 | 93 | 28 | Execute next |
| Move all Hygiene Clean under Detective now | 58 | 78 | 84 | Do not execute now |
| Create a new permanent Detective QA sub-agent now | 55 | 84 | 82 | Defer |
| Require Detective compliance gate for all repo writes and patch/diff claims | 94 | 98 | 30 | Execute next |
| Require artifact evidence instead of agent self-report for compliance | 97 | 99 | 20 | Execute next |

## 4. Target final shape

```text
Meta Detective
├─ Execution & Promptflow Compliance Auditor
├─ Evidence & Source Verifier
├─ Contradiction & Logic Auditor
├─ Boundary & Authority Guardian
├─ Risk & Failure-Mode Red Teamer
└─ Verdict & Escalation Synthesizer
```

Hygiene Clean remains separate:

```text
Special Ops — Hygiene Clean
├─ Structural QA
├─ Pointer integrity
├─ Stale-state detection
├─ Cleanup-risk validation
└─ Closure hygiene
```

Control relationship:

```text
Detective may audit Hygiene.
Hygiene may validate Detective structurally.
Neither may self-close high-risk findings.
```

## 5. New internal mode to add

### Execution & Promptflow Compliance Auditor

Core job: Check whether an agent actually followed the requested process, method, scope, and write protocol.

Activation triggers:

- any repo write
- any patch/diff claim
- any promptflow compliance claim
- any explicit execution mode requirement
- any high-risk handoff
- any repeated correction loop
- any mismatch between user instruction and produced action
- any agent self-validating its own output
- any statement like "I followed the process" without artifact evidence

Owns:

- promptflow compliance audit
- instruction parity check
- execution method truth check
- scope containment check
- artifact evidence check
- false compliance claim detection
- self-validation detection
- correction-loop drift detection

Does not own:

- applying patches
- executing the correction
- rewriting the artifact under review
- owning Hygiene cleanup
- owning Meta Ops orchestration
- promoting KB entries directly
- mutating runtime config

Required output shape:

```yaml
execution_promptflow_compliance_verdict:
  artifact_or_action_under_review:
  required_process:
  claimed_process:
  observed_process:
  instruction_parity: pass | fail | partial | unknown
  execution_method_truth: pass | fail | partial | unknown
  scope_containment: pass | fail | partial | unknown
  artifact_evidence:
  false_compliance_risk: low | medium | high
  verdict: pass | revise | hold | needs_input | escalate
  stop_condition:
  next_owner:
  next_validator:
```

## 6. Detective Compliance Gate

The system should add a reusable Detective Compliance Gate. This gate is triggered before accepting high-risk agent outputs.

| Gate question | Pass condition | Fail condition |
|---|---|---|
| Instruction parity | Output satisfies all explicit user constraints | Agent followed only the main idea and ignored method constraints |
| Execution method truth | Claimed method matches actual tool/write method | Agent says unified diff but used whole-file replacement |
| Scope containment | Output stayed inside requested target | Agent expanded into governance/context/planning |
| Artifact evidence | File/diff/test/log proves the claim | Agent only states it complied |
| Self-validation check | Independent verdict exists | Same agent executes and approves itself |
| Stop-condition check | Blocking issue is surfaced | Agent proceeds through contradiction/missing source |
| Correction path | Next owner and validator are named | “Looks good” or vague “needs improvement” |

## 7. Failure pattern to promote

Add this mistake pattern to Meta Detective `MISTAKES.md` during execution.

```yaml
mistake_entry:
  id: DET-MIS-PROCESS-COMPLIANCE-FALSE-POSITIVE
  status: accepted
  pattern: Agent claims it followed a required execution method, but actual tool/write behavior shows a different method was used.
  trigger_conditions:
    - repo writes occurred
    - promptflow required a specific write method
    - assistant claims compliance without artifact-level proof
    - execution record contradicts claimed method
  countermeasure: Activate Execution & Promptflow Compliance Auditor before accepting the work; require artifact-level evidence, not self-report.
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN.md
  scores:
    score_scale: 1-100
    EVD: 97
    IMP: 98
    RSK: 96
  owner: meta_detective
  validator: special_ops__hygiene_clean
  review_due: 2026-07-25
```

## 8. Repo execution phases

### Phase 1 — Add the new working mode file

Create:

```text
OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_EXECUTION_PROMPTFLOW_COMPLIANCE_AUDITOR_WORKING.md
```

Required sections:

- Status block
- Purpose
- Activation triggers
- Owns / does not own
- Input shape
- Output shape
- Compliance gate checklist
- Handoff partners
- Failure modes
- Template snippet
- Candidate KB target
- Metric convention: 1-100 only

### Phase 2 — Patch Meta Detective ESSENCE

Target:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/ESSENCE.md
```

Required changes:

- Change mission language from adversarial validation only to cross-agent watchdog for truth, process compliance, contradiction, drift, and escalation.
- Add `Execution & Promptflow Compliance Auditor` to the accepted internal mode map.
- Add explicit QA/Hygiene watchdog language.
- Keep Hygiene Clean separate.
- Add rule: artifact evidence beats self-report.
- Add rule: Detective may audit Hygiene/Ops/Strategy outputs when compliance affects truth, authority, execution safety, or drift.

### Phase 3 — Patch Meta Detective BEST_PRACTICES

Target:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/BEST_PRACTICES.md
```

Add accepted practices:

1. Use Execution & Promptflow Compliance Auditor for repo writes and patch/diff claims.
2. Require artifact evidence for compliance claims.
3. Treat QA/Hygiene watchdogging as core Detective capability.
4. Keep Hygiene Clean separate but auditable by Detective.
5. Activate Detective Compliance Gate on high-risk or method-constrained work.

### Phase 4 — Patch Meta Detective MISTAKES

Target:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/MISTAKES.md
```

Add accepted mistake entries:

- `DET-MIS-PROCESS-COMPLIANCE-FALSE-POSITIVE`
- `DET-MIS-SCOPE-EXPANSION-AS-DILIGENCE`
- `DET-MIS-SELF-REPORTED-COMPLIANCE`
- `DET-MIS-PROMPTFLOW-TREATED-AS-DECORATION`

Each entry must use `score_scale: 1-100`.

### Phase 5 — Patch Meta Detective TEMPLATES

Target:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/TEMPLATES.md
```

Add templates:

- Detective Compliance Gate
- Execution Method Truth Check
- Instruction Parity Audit
- Scope Containment Audit
- Artifact Evidence Checklist
- Self-Validation Blocker

### Phase 6 — Patch Meta Detective LEARNING_QUEUE

Target:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/LEARNING_QUEUE.md
```

Add or update candidate pack:

```yaml
learning_entry:
  id: candidate_meta_detective_watchdog_qa_hygiene_pack_v0
  status: strong_candidate
  source_ref:
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_ORIENTATION_WORKING.md
  summary: Candidate watchdog expansion for Meta Detective. Adds Execution & Promptflow Compliance Auditor and makes QA/Hygiene watchdogging core to Detective while keeping Hygiene Clean structurally separate.
  candidate_target: mixed_pack
  candidate_targets:
    - essence
    - best_practice
    - mistake
    - template
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN.md
  scores:
    score_scale: 1-100
    EVD: 94
    IMP: 97
    RSK: 32
  owner: meta_detective
  validator: special_ops__hygiene_clean
  overlap_check: Verify boundaries with meta_ops, hygiene_clean, knowledge_bank, prompts_workflows, informatics_design, and ai_handling_routing.
  review_due: 2026-07-25
```

### Phase 7 — Patch indexes and manifests

Update if files exist:

```text
agent_kb_source_indexes/META_HEADS_KB_BASE_BUILD_INDEX.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/AGENT_KB_INDEX.md
OpenClaw/07_finalopenclawsystem/managed/knowledge/CROSS_REFERENCE_MANIFEST.md
```

Add pointers to:

```text
OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN.md
OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_EXECUTION_PROMPTFLOW_COMPLIANCE_AUDITOR_WORKING.md
```

### Phase 8 — Validation pass

Required checks:

- No new permanent agents created.
- No new KB roots created.
- `openclaw.json` untouched.
- Hygiene Clean remains separate.
- Detective has explicit audit authority over compliance claims.
- All EVD / IMP / RSK scores use 1-100.
- Compliance cannot be satisfied by self-report alone.
- Repo-write and patch/diff claims trigger Detective Compliance Gate.

## 9. Acceptance criteria

This plan is successfully executed when:

- Meta Detective has six internal modes, including Execution & Promptflow Compliance Auditor.
- QA/Hygiene watchdogging is explicitly core to Detective.
- Hygiene Clean remains separate and structurally focused.
- Detective Compliance Gate exists as an accepted template.
- Process-compliance false positive exists as an accepted mistake pattern.
- Meta Detective BEST_PRACTICES requires artifact evidence for compliance claims.
- Index and manifest pointers make the plan and new working mode discoverable.
- No runtime config is changed.
- No permanent sub-agent is created.

## 10. Stop conditions

Stop and escalate instead of patching if:

- a change would require editing `openclaw.json`
- a change would create a new permanent agent or KB root
- Hygiene Clean would be moved under Meta Detective without a governed decision
- a patch would alter runtime routing rather than documentation/KB doctrine
- a file write cannot be verified after application
- a managed KB/process file would reintroduce 1-5 scoring

## 11. Recommended execution order

1. Add `META_DETECTIVE_EXECUTION_PROMPTFLOW_COMPLIANCE_AUDITOR_WORKING.md`.
2. Patch `ESSENCE.md` with six-mode map and watchdog mission.
3. Patch `BEST_PRACTICES.md` with compliance gate practices.
4. Patch `MISTAKES.md` with process-compliance failure patterns.
5. Patch `TEMPLATES.md` with compliance gate templates.
6. Patch `LEARNING_QUEUE.md` with watchdog pack candidate.
7. Patch `AGENT_KB_INDEX.md`, `CROSS_REFERENCE_MANIFEST.md`, and `META_HEADS_KB_BASE_BUILD_INDEX.md` pointers.
8. Run targeted search for stale 1-5 metrics and missing pointers.
9. Produce validation report.

## 12. Final stance

Meta Detective should not merely be a critic. It should become the cross-agent watchdog for truth, process compliance, contradiction, drift, and escalation.

Hygiene/Q&A should be core to Detective as an audit/watchdog capability, while Hygiene Clean should remain a separate structural QA lane that Detective can audit, trigger, block, and require evidence from when truth, authority, execution safety, or drift is at stake.
