---
type: Reference
title: Machine-executable handoff plans for AI agents — verified best practice
status: stable
generated: { by: "claude/opus-4.8", at: "2026-09-28" }
tags: [research, planning, ai-agents, handoff, spec-driven]
---

# Machine-executable handoff plans (research summary)

Condensed from a 2026-09-28 web-research pass; sources at the bottom. This is the pattern `PLAN.md` is built on.

## Best practices (highest leverage first)
1. **Split intent from execution into sequential, reviewable artifacts:** **Specify → Plan → Tasks → Implement**, each a Markdown artifact feeding the next, with a human checkpoint between phases (GitHub Spec Kit; AWS Kiro `requirements.md → design.md → tasks.md`). Don't collapse into one giant prompt.
2. **Testable, unambiguous acceptance criteria — EARS grammar:** `WHEN <condition> THE SYSTEM SHALL <behavior>`. Each criterion maps to a checkable test, not prose.
3. **Small, isolated, traceable, dependency-ordered tasks** (a DAG). Mark parallel-safe tasks (`[P]`); encode prerequisites explicitly; keep each task reviewable/testable.
4. **Validation gates between steps:** plan → execute (small change) → test → fix → verify; no next step until the current verifies. Constitutional/simplicity gates prevent scope drift.
5. **Exact commands + expected outputs, not descriptions** — this is what makes a plan executable by an agent vs a human: the literal command, the files it may touch, the expected result.
6. **`AGENTS.md` entry point, nearest-file-wins, progressive disclosure** — keep root short, link to detail.
7. **A small, continuously-updated continuation/state file:** goal, current state, exact next step, decisions taken, approaches ruled out, file paths. A valid continuation **executes from the reached state, preserves accepted choices + realized effects, and completes open obligations — never restarts.**
8. **Bounded rollback + human gate on destructive/high-risk actions;** keep an evidence bundle (task brief, plan, executed commands, test results, diff, criteria→test trace, reviewer decision, rollback path). Verify "done" with a fresh check on evidence, not the executor's assertion.

## Failure modes to design against
Ambiguity (→ EARS + exact commands + explicit open-question markers); missing/after-the-fact acceptance criteria (→ define before starting); stale/duplicated context (→ single source of truth, one state file updated in place, never dated forks); destructive step without a human (→ `gate: human-approval` + reviewed rollback queue); unbounded scope (→ non-goals, small tasks, budgets); false "done" (→ fresh-verifier on evidence); restart-instead-of-resume (→ continuation file with realized effects + open obligations).

## Per-task field set (load-bearing)
`id` · `goal` · `deps` (DAG edges; `[P]` = parallel-safe) · `steps` (exact commands/edits) · `acceptance` (EARS, checkable) · `gate` (none | human-approval | operator-decision) · `rollback` (bounded, exact) · `status` (machine-readable) · `evidence` (path to proof) · `owner`. Plan frontmatter carries `status`, `current_task`, `blocked_by`.

## Sources (accessed 2026-09-28)
GitHub Spec Kit `spec-driven.md` + GitHub Blog 2025-09-02; AWS Kiro Specs / feature-specs; agents.md + morphllm AGENTS.md guide; *AI Agent Workflow Orchestration* (Liles, Medium); arXiv preprints 2605.17998 (*Verify-Gated Completion*), 2609.13800 (*Do Not Restart*) — **preprints, corroboration not authority**. No single canonical per-task schema exists; the field set is synthesized from convergent conventions.
