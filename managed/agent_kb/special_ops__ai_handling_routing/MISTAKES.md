# MISTAKES

## Purpose

Accepted validated AI Handling Routing failure patterns and countermeasures.

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
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  review_due:
```

## Score convention

All `EVD` / `IMP` / `RSK` scores use the active 1-100 scale. No 1-5 metric scale is used in this KB.

- `EVD`: evidence strength
- `IMP`: positive impact when prevented
- `RSK`: adoption risk of the countermeasure inside the stated context conditions

## Accepted mistake patterns

```yaml
mistake_entry:
  id: AIHR-MK-001
  status: accepted
  pattern: Mode-mismatch substitution routes a task to a mode whose strengths do not match the bottleneck, causing the system to produce the wrong kind of output.
  trigger_conditions:
    - Agent Mode is used for KB architecture, prompt design, doctrine synthesis, exact markdown, or unified diff drafting without a real external UI/action bottleneck
    - Deep Research is used where the user needs repo mutation, patch application, or tests
    - normal chat is used for patch/test execution without repo-aware validation
    - extended thinking is used where the user actually needs browser, app, form, spreadsheet, or multi-tool action
  countermeasure: Route by bottleneck before execution; require a concrete success condition; use Agent Mode for external action, extended thinking for reasoning/artifact drafting, Deep Research for broad synthesis, and Codex/repo tooling for patch application and tests.
  evidence_refs:
    - docs/Agent_Mode_vs_Thinking_Mode_Routing_Baseline.md
    - docs/Agent_Mode_vs_Thinking_Mode_Routing_Baseline_Context.md
  scores:
    score_scale: 1-100
    EVD: 90
    IMP: 90
    RSK: 20
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  review_due: 2026-07-25
```

## Empty-state marker or initial entries

Initial accepted mode-mismatch entry is present. Add further entries only after validation and promotion from `LEARNING_QUEUE.md`.
