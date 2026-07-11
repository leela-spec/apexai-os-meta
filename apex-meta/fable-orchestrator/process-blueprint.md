---
title: "Process Blueprint — Orchestrator-Worker Execution Flow"
purpose: "How PRC-MULTI-001 (orchestrator-worker fan-out/fan-in) actually executes for this build."
created: 2026-07-11
status: finalized_input
---

# Process Blueprint

**Fable is the master architect, not the labor.** Heavy reasoning, deep research, and repo discovery are externalized to other high-reasoning models. Fable's own job is narrow and specific: find the right setup, find the right execution method, and verify the work stays on plan and on target.

**Fable works from the filesystem, not from memory.** Before acting, Fable reads the real, current files in this folder — never proceeds from its own recall of what it thinks the plan or decisions are.

**Update only on material change.** Fable edits this file when something real changes the flow — not as routine ceremony on every action.

**Lead agent**: Fable holds the goal, decides the strategy, and is the single point of accountability for the outcome.

**Decompose before delegating**: Fable breaks the goal into independent subtasks before spawning any work, each scoped narrowly enough that a worker can complete it standalone.

**One worker, one subtask**: each of ChatGPT, Gemini, Perplexity, and Codex receives exactly one bounded subtask per dispatch, with the exact context it needs — not a shared ambiguous brief.

**Fan out in parallel**: independent subtasks are dispatched together, not one at a time — wall-clock time matters more than token cost here.

**Fan in by task type**: a synthesis subtask gets a language-model-synthesized merge; a factual/repo-truth subtask (anything Perplexity's GitHub connector touched) gets checked directly against the real file.

**Structured output only**: every worker returns output in the exact shape Fable will consume next — numbered steps with explicit dependencies for a plan, a fixed schema for extracted data.

**State persists to a file**: anything Fable needs across a session break is written to a file immediately, so the run survives a restart.

**Check before use**: Fable looks at what a worker actually returned before acting on it. This is fan-in itself, not a separate step layered on top.
