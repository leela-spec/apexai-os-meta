# BEST_PRACTICES

## Purpose

Accepted compact practices for Special Ops Prompts Workflows.

This scaffold is intentionally short. Detailed source ranking and evidence live in `appendices/`.

## Entry schema

```yaml
practice_entry:
  id:
  status: accepted | deprecated
  practice:
  context_conditions:
  evidence_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due:
```

## Accepted practices

- id: `PW-BP-001`
  status: accepted
  practice: Use full final bodies or live-edit instructions when Markdown diff transport is fragile; use patch mode for small bounded defects when anchors are stable.
  context_conditions:
    - large Markdown rewrite
    - new file creation
    - connector or chat output that is not line-stable
    - CRLF or hidden-character risk
    - malformed unified diff with visible bounded intent
    - small bounded defect with reliable anchors
  evidence_refs:
    - `appendices/SOURCE_CONFLICT_REPORT.md#pw-conflict-001`
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-001`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-003`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-BP-002`
  status: accepted
  practice: Freeze objective, target, source authority, non-goals, output contract, and stop condition before serious prompt/workflow execution.
  context_conditions:
    - file-producing prompt
    - research-producing prompt
    - patch-producing prompt
    - handoff-producing prompt
    - multi-source or long-context task
  evidence_refs:
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-001`
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-002`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-a--scope-lock`
  scores:
    EVD: 5
    IMP: 5
    RSK: 2
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-BP-003`
  status: accepted
  practice: Use bounded, stage-gated, artifact-centered execution instead of broad autonomy or giant multi-phase prompts.
  context_conditions:
    - normal subscription-chat execution
    - low-context agent handoff
    - serious documentation or architecture work
    - workflow could blend research, writing, QA, packaging, and finalization
  evidence_refs:
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-003`
    - `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md#pw-cand-003`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-006`
  scores:
    EVD: 5
    IMP: 5
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-BP-004`
  status: accepted
  practice: Make source authority a pre-step gate and verification a post-step gate; do not trust output because it looks fluent.
  context_conditions:
    - source hierarchy matters
    - outputs will be reused or committed
    - multiple summaries and original files exist
    - two primary sources may conflict
  evidence_refs:
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-006`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-b--source-authority-preflight`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-d--verification-gate`
  scores:
    EVD: 5
    IMP: 5
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-BP-005`
  status: accepted
  practice: Detect out-of-mode improvements, but capture them explicitly instead of applying them silently.
  context_conditions:
    - execution prompt has a closed mode
    - Codex or another agent notices adjacent improvements
    - improvement is high-confidence but outside current scope
  evidence_refs:
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-008`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-e--out-of-mode-capture`
  scores:
    EVD: 5
    IMP: 4
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-BP-006`
  status: accepted
  practice: Use clean handoffs when moving work across chats, agents, or execution lanes: settled state, source priority, non-redo list, exact next job, risks, and success condition.
  context_conditions:
    - new chat continuation
    - Codex handoff
    - multi-stage research-to-patch workflow
    - prior thread is saturated or overloaded
  evidence_refs:
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-010`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-f--handoff-reset`
  scores:
    EVD: 4
    IMP: 5
    RSK: 2
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-BP-007`
  status: accepted
  practice: Record durable QA, gap, and next-research results in a repo appendix when a KB build or improvement pass changes what future agents should rely on.
  context_conditions:
    - KB build or improvement pass
    - future scaffold promotion candidates are identified
    - verification, gap analysis, or next-research work would otherwise remain only in chat
    - multiple appendices or scaffold files may be affected later
  evidence_refs:
    - `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#purpose`
    - `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#current-qa-status`
    - `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#next-patch-candidates`
  scores:
    EVD: 5
    IMP: 5
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-BP-008`
  status: accepted
  practice: Treat prompt and workflow examples as behavioral regression tests for this lane; use them to check whether prompts preserve target, source, mode, validation, and stop discipline.
  context_conditions:
    - prompt or promptflow behavior is being taught, reused, or validated
    - a previous failure involved scope drift, no-op completion, fragile diff transport, or out-of-mode improvement application
    - a template needs concrete before/after evidence
  evidence_refs:
    - `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#f5-scaffold-promotion-matrix`
    - `appendices/APPENDIX_KB_EXAMPLES.md#purpose`
    - `appendices/APPENDIX_KB_EXAMPLES.md#regression-checklist`
  scores:
    EVD: 5
    IMP: 5
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-BP-009`
  status: accepted
  practice: Carry execution state as an explicit frame or state block; never rely on chat-history reconstruction for current task state.
  context_conditions:
    - high-risk promptflow execution
    - multi-chat or operator-mediated task sequence
    - repo-writing or scaffold-update workflow
    - stale, missing, or contradictory prior context is possible
  evidence_refs:
    - `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-01--implicit-chat-history-state-reconstruction`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-02--stale-or-missing-state_block`
  scores:
    EVD: 5
    IMP: 5
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-BP-010`
  status: accepted
  practice: Execute high-risk tasks through an atomic task packet: one task, one target, explicit input refs, repeated scope, and a gate check before write or synthesis.
  context_conditions:
    - appendix creation
    - scaffold update
    - patch or file-write task
    - handoff to another chat, executor, or operator
    - source authority or target root must be constrained
  evidence_refs:
    - `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
    - `appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-03--compound-task_payload-using-andthen`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-05--directory-scan-without-explicit-input_refs`
  scores:
    EVD: 5
    IMP: 5
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-BP-011`
  status: accepted
  practice: Treat HALT, CLARIFY, patch-check failure, split-required conditions, and unverified external claims as routing controls, not prose warnings.
  context_conditions:
    - ambiguity remains after gate check
    - patch dry-run or preimage validation fails
    - output must be split to avoid summary substitution
    - external model, API, browser, runtime, or platform claim would affect doctrine
    - closure lacks fetch-back or claim-status proof
  evidence_refs:
    - `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
    - `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`
    - `appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-07--unsafe-continuation-after-halt-condition`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-11--split-required-output-that-substitutes-summary`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-13--external-modelplatform-claim-promoted-as-accepted-doctrine`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

## Appendix pointers

- Source manifest: `appendices/APPENDIX_KB_SOURCE_MANIFEST.md`
- Ranking ledger: `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`
- Candidate ledger: `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`
- Anti-drift evidence: `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`
- Source conflicts: `appendices/SOURCE_CONFLICT_REPORT.md`
- Examples: `appendices/APPENDIX_KB_EXAMPLES.md`
- Source notes: `appendices/APPENDIX_KB_SOURCE_NOTES.md`
- QA and next research plan: `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`
- Constant failure integration process: `appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md`
- Execution control contracts: `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
- Constant failure source notes: `appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md`
- Patch transport protocols: `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`
- Regression examples: `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`
- Runtime template catalog: `appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`
- External claim verification: `appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md`

## Promotion boundary

Add or revise accepted practices only after validation through `LEARNING_QUEUE.md` and `meta_ops` review.
