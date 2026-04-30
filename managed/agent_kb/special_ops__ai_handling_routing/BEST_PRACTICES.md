# BEST_PRACTICES

## Purpose

Accepted validated practices for Special Ops AI Handling Routing.

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
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  review_due:
```

## Score convention

Scores use a 1-5 scale:

- `EVD`: evidence strength
- `IMP`: positive impact when followed
- `RSK`: adoption risk when applied inside the stated context conditions

## Accepted practices

```yaml
practice_entry:
  id: AIHR-BP-001
  status: accepted
  practice: Route AI work by bottleneck rather than by perceived complexity.
  context_conditions:
    - choosing between Agent Mode, extended thinking, Deep Research, and Codex/repo tooling
    - selecting a mode for OpenClaw KB, prompt, doctrine, markdown, diff, research, or repo work
  evidence_refs:
    - docs/Agent_Mode_vs_Thinking_Mode_Routing_Baseline.md
  scores:
    EVD: 5
    IMP: 5
    RSK: 1
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  review_due: 2026-07-25
```

```yaml
practice_entry:
  id: AIHR-BP-002
  status: accepted
  practice: Use Agent Mode when the bottleneck is external browser, app, UI, tool, form, spreadsheet, or supervised online action.
  context_conditions:
    - the task requires navigating websites or visual UI
    - the task requires form submission, settings changes, uploads, downloads, or authenticated external action
    - the task requires multi-app operational execution rather than mainly reasoning or wording
  evidence_refs:
    - docs/Agent_Mode_vs_Thinking_Mode_Routing_Baseline.md
  scores:
    EVD: 5
    IMP: 5
    RSK: 2
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  review_due: 2026-07-25
```

```yaml
practice_entry:
  id: AIHR-BP-003
  status: accepted
  practice: Use extended thinking for KB architecture, prompt design, doctrine synthesis, exact markdown, review, and unified diff drafting.
  context_conditions:
    - the requested output is a precise text artifact
    - the task requires controlled reasoning, source comparison, or exact wording
    - the work is OpenClaw KB, prompt-flow, doctrine, or patch-design work
  evidence_refs:
    - docs/Agent_Mode_vs_Thinking_Mode_Routing_Baseline.md
  scores:
    EVD: 5
    IMP: 5
    RSK: 1
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  review_due: 2026-07-25
```

```yaml
practice_entry:
  id: AIHR-BP-004
  status: accepted
  practice: Use Deep Research for broad multi-source synthesis and cited reports, not for repo mutation or exact patch application.
  context_conditions:
    - source breadth and citation-heavy synthesis are the bottleneck
    - the deliverable is a report or research basis rather than a direct repo change
  evidence_refs:
    - docs/Agent_Mode_vs_Thinking_Mode_Routing_Baseline.md
  scores:
    EVD: 5
    IMP: 4
    RSK: 2
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  review_due: 2026-07-25
```

```yaml
practice_entry:
  id: AIHR-BP-005
  status: accepted
  practice: Use Codex or repo-aware execution for patch application, tests, git-apply checks, and mechanical repo validation.
  context_conditions:
    - the requested work mutates repository files
    - the task requires running tests or validating whether a patch applies
    - the success condition depends on mechanical repo state, not only reasoning quality
  evidence_refs:
    - docs/Agent_Mode_vs_Thinking_Mode_Routing_Baseline.md
  scores:
    EVD: 5
    IMP: 5
    RSK: 2
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  review_due: 2026-07-25
```

## Empty-state marker or initial entries

Initial accepted mode-routing entries are present. Add further entries only after validation and promotion from `LEARNING_QUEUE.md`.
