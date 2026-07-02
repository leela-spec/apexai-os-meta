---
class: reference
role: EXAMPLE_LIBRARY
surface: agent_kb_appendix
quality: reliable
scope: agent
purpose: provide prompt and workflow examples that function as regression tests for bounded execution behavior
dependencies: ESSENCE.md | BEST_PRACTICES.md | MISTAKES.md | TEMPLATES.md | APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
status: candidate_patch
owner: special_ops__prompts_workflows
validator: meta_ops
---

# APPENDIX_KB_EXAMPLES

## Purpose

This appendix stores concrete examples for Special Ops Prompts Workflows.

Examples in this lane are not decorative. They are behavioral regression cases for prompt, workflow, promptflow, handoff, and bounded execution discipline.

## Use rule

- Use these examples when turning vague operator intent into bounded prompt/workflow execution.
- Keep examples subordinate to the F5 scaffold and source appendices.
- Do not treat an example as governance, approval, or permission to mutate unrelated targets.

## Example 1: vague prompt to bounded execution contract

### Bad input

```text
Improve the KB and make it better.
```

### Failure risk

- The target file set is undefined.
- The source authority is undefined.
- The allowed write type is undefined.
- The stop condition is undefined.
- The assistant may do broad governance rereads or silently edit unrelated scaffold files.

### Better prompt

```yaml
execution_mode: bounded_artifact_manufacturing
current_phase: MANUFACTURE
exact_input_files:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
exact_output_artifact: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_003_TEMPLATES.diff
allowed_actions:
  - create exactly one unified diff artifact for TEMPLATES.md
forbidden_actions:
  - edit TEMPLATES.md directly
  - create extra files
  - broaden into governance or config work
  - apply inferred improvements
validation_checks:
  - artifact exists
  - exactly one diff target
  - target path is under the Prompts Workflows KB root
  - content implements the named candidate only
stop_condition: stop_after_named_diff_artifact_validation
```

### Regression check

The assistant should create only the named diff artifact and stop after validation.

## Example 2: user intent versus named artifact mismatch

### Bad behavior

The operator names a promptflow file, but the actual task is to execute the flow and produce gap analysis, F5 promotion options, and future KB-system research. The assistant fetches the promptflow, sees the file already exists, and reports a no-op.

### Correct behavior

```yaml
intent_contract_check:
  user_intent: execute the promptflow and produce the decision/options/recommendation layer
  named_promptflow_or_artifact: PROMPTFLOW_PROMPTS_WORKFLOWS_BOUNDED_EXECUTION_GUARDRAILS.md
  intended_execution_scope: gap analysis, appendix inventory, F5 promotion candidates, future KB improvements
  exact_output_expected: durable appendix or unified diff artifact named by the active step
  repo_write_expected: true
  scaffold_mutation_allowed: false unless explicitly approved
  appendix_only_allowed: true
  open_questions: []
  stop_if_mismatch: true
```

### Regression check

If user intent and artifact text diverge, the assistant should surface the gap and create the missing bounded control artifact rather than claiming completion from file equality alone.

## Example 3: fragile diff to live-edit contract

### Bad input

```text
Patch this long Markdown file however you need.
```

### Failure risk

- Long Markdown anchors may drift.
- A malformed patch may invite hand editing.
- The executor may rewrite unrelated content.

### Better mode chooser

```yaml
edit_mode_chooser:
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
  change_size: medium
  anchor_stability: fragile
  markdown_transport_risk: high
  exact_byte_patch_safe: false
  recommended_mode: live_edit_instruction
  forbidden_modes:
    - broad rewrite
    - unrelated cleanup
  reason: choose live edit or full final body when Markdown diff transport is less reliable than controlled replacement
```

### Regression check

The assistant should not hand-edit after a failed patch unless the operator explicitly authorizes live edit or full-body replacement.

## Example 4: clean handoff

### Bad handoff

```text
Continue the KB thing from earlier. You know what to do.
```

### Better handoff

```markdown
# Clean Handoff

## What is being continued

Prompts Workflows KB aggressive P1 improvement wave.

## Settled decisions

- Create one unified diff artifact per target file.
- Do not apply diffs directly in this pass.
- Validate each diff after creation.

## Authority stack

1. `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`
2. current F5 scaffold files
3. source appendices and conflict report

## Do not redo

- Do not reopen broad KB architecture.
- Do not edit config or governance surfaces.

## Exact next job

Create the next pending diff artifact and fetch it back.

## Success condition

The artifact exists, contains exactly one `diff --git` header, targets the approved path, and implements the intended candidate.
```

### Regression check

The receiving agent can continue without reconstructing hidden reasoning from chat.

## Example 5: out-of-mode improvement capture

### Situation

While creating a `TEMPLATES.md` diff artifact, the assistant notices that YAML sidecars could improve automation.

### Bad behavior

The assistant creates sidecar files in the same pass.

### Correct capture

```markdown
## Improvement Opportunities Not Applied

- Create `APPENDIX_KB_TEMPLATE_CATALOG.yaml` after template catalog fields are approved.
- Reason not applied: current phase is one-file diff artifact manufacturing.
- Suggested target: `LEARNING_QUEUE.md` candidate or future sidecar patchset.
```

### Regression check

High-confidence adjacent improvements are captured, not applied.

## Example 6: promptflow stage-gate skeleton

```markdown
## Stage 1: Source lock

- Read only the declared source list.
- Stop if a required source is missing.

## Stage 2: Gap and candidate analysis

- Identify what is missing.
- Classify scaffold promotion candidates separately from appendix-only material.

## Stage 3: Diff manufacturing

- Create one unified diff artifact per target file.
- Fetch back after every artifact.
- Stop on validation failure.

## Stage 4: Apply

- Apply only approved diffs.
- Do not hand-edit failed diffs without operator approval.
```

## Regression checklist

- The prompt names exact target path(s).
- The source authority is explicit.
- The output artifact is explicit.
- The write mode is explicit.
- The assistant creates no extra targets.
- The assistant does not apply inferred improvements.
- The assistant validates against file state before reporting completion.
