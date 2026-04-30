# BEST_PRACTICES

## Purpose

Accepted validated practices for Special Ops Prompts Workflows.

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
  practice: Use full final bodies or live-edit instructions as the default artifact for Markdown rewrites; let Codex edit the live checkout and let Git generate the review diff.
  context_conditions:
    - new file creation
    - compact seed normalization
    - large Markdown rewrite
    - bounded Markdown patch where exact byte context is fragile
    - files with CRLF or uncertain line endings
  evidence_refs:
    - operator feedback, 2026-04-27, "unified-diff process diagnosis"
    - `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27
- id: `PW-BP-002`
  status: accepted
  practice: Treat pre-authored unified diffs as acceptable only when generated and checked in the actual repo checkout; otherwise emit a blocked patch or one-file live-edit instruction.
  context_conditions:
    - existing-file patch packs
    - browser or chat research handoffs
    - connector output that is not line-stable
    - any workflow using Markdown as a patch carrier
  evidence_refs:
    - operator feedback, 2026-04-27, "patch artifact hierarchy"
    - `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27
- id: `PW-BP-003`
  status: accepted
  practice: For implementation-ready deep-research prompts, include a preflight contract that specifies source-access priority, citation/evidence expectations, zero-budget exclusions, locked-assumption handling, missing-source behavior, and the Phase 1 fallback before the main research task begins.
  context_conditions:
    - deep research must synthesize from a local or repo-internal source basis
    - the prompt has many locked decisions or exclusions
    - the output must be operational rather than exploratory
    - connector behavior, citation mechanics, or tool capability could distract the agent
    - the task should convert uncertainty into validation tests instead of re-research loops
  evidence_refs:
    - `OpenClaw/02_research-kb/best-practices/operational-framework/UpdateProcessSSOTS/DRGPT55THinkingProcess.md`
    - `OpenClaw/04_final-system-setup/AfterOpenClawFIrstSetup/New_orchestration/DeepResearchPrompt_v2.md`
    - `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-28

- id: `PW-BP-004`
  status: accepted
  practice: Use production-first iteration for artifact-producing prompt and workflow runs: create the requested file, patch, prompt artifact, or KB update before broad validation, second research, or governance expansion.
  context_conditions:
    - file creation or file repair
    - patch or unified-diff generation
    - KB update or prompt artifact production
    - continuation-based workflow execution
    - subscription-browser or connector-mediated runs where control scaffolding can crowd out the artifact
  evidence_refs:
    - `Production_First_Iteration_Learning_Record.md`
    - `Production_First_Diff_Validation_Report.md`
    - `GitHub_Extended_Thinking_Production_First_Patch_Flow.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-30

- id: `PW-BP-005`
  status: accepted
  practice: Design production prompts so the target artifact is impossible to miss: name the artifact, place production before analysis, keep guardrails subordinate to output delivery, and require validation only after the first concrete artifact exists.
  context_conditions:
    - prompt design for file, diff, KB, or downloadable artifact creation
    - continuation-based production flows
    - browser or connector runs where preflight, source gates, or governance checks can crowd out delivery
    - tasks where the user needs to validate and continue rather than receive another plan
  evidence_refs:
    - `Production_First_Agent_Mode_KB_Update_Prompt_Flow.md`
    - `Production_First_Iteration_Learning_Record.md`
    - `Final_Production_First_Agent_Mode_Integration_Pack.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-30

- id: `PW-BP-006`
  status: accepted
  practice: Declare the intended execution mode and bottleneck in prompt flows before invoking Agent Mode.
  context_conditions:
    - prompt-flow design for KB, doctrine, markdown, unified diff, or repo work
    - workflows that could be misread as Agent Mode tasks because they are complex
    - tasks that mix reasoning, research, external action, and patch execution
    - operator-continuation flows where the next executor needs a clear mode boundary
  evidence_refs:
    - `docs/Agent_Mode_vs_Thinking_Mode_Routing_Baseline.md`
    - `docs/Agent_Mode_vs_Thinking_Mode_Routing_Baseline_Context.md`
    - `managed/agent_kb/special_ops__ai_handling_routing/BEST_PRACTICES.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 1
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-30

## Empty-state marker or initial entries

Add entries here only after validation and promotion from `LEARNING_QUEUE.md`.
