---
title: "User Stories — Real Workflow Records"
purpose: "What the finished orchestration system must actually let someone do. Anticipated draft, written ahead of the dedicated authoring session per prompts/phase1-user-stories-prompt.md, to unblock milestone 1 now."
created: 2026-07-11
status: anticipated_draft — real content, subject to revision once the dedicated authoring pass runs
---

# User Stories

## US1 — Reconcile the old Apex system with apex-plan/sync/session into one target architecture

- **Trigger**: milestones 1–3 in `target-log.md` are complete and operator-verified.
- **Inputs**: `apex-meta/handoff/agent-skill-system-research/design-lock-qa.md` (the 8 open questions), the milestone findings, `claude-code-orchestration-design` KB pages.
- **Mechanism**: Fable drafts an answer to each question citing real evidence from the systems named in `README.md`'s core problem. Where reasoning is heavy or ambiguous, Fable authors a prompt for ChatGPT/Gemini per `fable-execution-best-practices.md` §3, integrates the result, and verifies it against real repo files before using it.
- **Output**: `design-lock-qa.md`'s 8 questions answered with cited evidence, written into `decisions.md` as new locked decisions.
- **Handoff/validation**: operator reviews and confirms each answer before it's locked.

## US2 — Decide subagent-vs-inline-work for a specific task

- **Trigger**: Fable (or a future orchestrator agent) needs to decide whether a given task should be a subagent or inline work.
- **Inputs**: the task description, `wiki/summaries/agent-vs-subagent-vs-skill.md` in `claude-code-orchestration-design`.
- **Mechanism**: Fable reads the KB page directly and applies its documented decision criteria — no external model needed, this KB page already answers it (see `build-plan.md`'s worked example).
- **Output**: a one-line decision with a real citation.
- **Handoff/validation**: none beyond the citation — already proven low-stakes.

## US3 — Check a drafted architecture piece's resilience before building it

- **Trigger**: milestone 5 drafts a piece of the target architecture; it needs a resilience check before milestone 6 builds it.
- **Inputs**: the drafted piece, `claude-code-orchestration-design`'s skill-package-design pages, the old Apex KB's failure-mode lessons (`ingest-analysis/phase1-failure-evidence.md`).
- **Mechanism**: Fable checks the draft against both sources. Where a gap exists, Fable authors a prompt for an external model asking it to check the specific design against known multi-agent resilience failure patterns.
- **Output**: a pass/fail/gap verdict on the drafted piece, with a proposed fix for any gap found.
- **Handoff/validation**: operator reviews before the piece is built.

## US4 — Reconcile a flagged multi-KB overlap into one decision document

- **Trigger**: operator points Fable at a flagged overlap (e.g., `ORCHESTRATION-SYSTEMS-INDEX.md` §5's `old-apex-full-orchestration-agent-kb` vs. `-v2`, or `llm-wiki-project-repos` vs. `claude-orchestration-agents`).
- **Inputs**: `ORCHESTRATION-SYSTEMS-INDEX.md` §5, the actual KB folders in question.
- **Mechanism**: Fable reads/greps the real KB content directly; for anything requiring deep repo-file research, routes to Perplexity (GitHub connector) per `fable-execution-best-practices.md` §2.
- **Output**: one decision document per flagged overlap, citing real evidence, not invented justification.
- **Handoff/validation**: operator confirms.
