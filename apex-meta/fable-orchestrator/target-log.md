---
title: "Target Log"
purpose: "The overarching mission and its milestone breakdown. Update at the start of each work session, not mid-session."
created: 2026-07-11
---

# Target Log

## Overarching target

Create the final orchestration system, merging the old Apex agent-swarm system and the new `apex-plan`/`apex-sync`/`apex-session` system into one coherent whole — where Fable itself evaluates the soundness, impact, resilience, and intent of each system's workflows and agents, supported by external research where the reasoning is heavy, verified by the operator at each milestone.

## Milestones

1. **Understand intent across every version** — read across `operator-research-orchestration-20260711`, `old-apex-full-orchestration-agent-kb`(+`-v2`), `apex-plan-sync-session-workflow-v2`: what each was trying to build, the biggest decisions each made, where they overlap, what patterns repeat. Gate: operator verifies.
2. **Understand resilience best-practice** — go into `claude-code-orchestration-design`'s skill-package pages for what makes a multi-agent system resilient; produce prompts for external models where the KB itself is thin. Gate: operator verifies.
3. **Evaluate soundness/impact/resilience of what already exists** — assess the old Apex 9-agent/BUILD-VERIFY-LOCK model and the `apex-plan`/`sync`/`session` boundary against milestone 2's best practice. Gate: operator verifies.
4. **Resolve the open architecture questions** (`apex-meta/handoff/agent-skill-system-research/design-lock-qa.md`) — using milestones 1–3 as evidence, not assumption.
5. **Draft the target architecture** — only after 1–4 are verified.
6. **Build it** — the actual construction, Codex for execution, per `build-plan.md`.

## Current target

Milestone 1 is underway: `prompts/phase1-user-stories-prompt.md` produces real workflow records feeding milestone 1, and `user-stories.md` has an anticipated first draft.

## Log

- 2026-07-11: Phase 0 lock attempted as a real test run. Found `design-lock-qa.md` had zero operator-confirmed answers (only recommended defaults); the `decisions.md` format precedent (`harmonization/decisions.md`) cited an out-of-scope external corpus (`source-knowledge/`) that shouldn't be borrowed here; no schema existed yet for `user-stories.md`/`simulations/` records.
- 2026-07-11: A claim that the branch `claude/code-orchestration-design-kb-qdipjj` didn't exist was wrong — `git branch -a` was checked without `git fetch origin` first. After fetching, the branch was confirmed real, with real commits (frontmatter fix on the 25 `max-run-20260709` pages, 7 new high-value wiki pages, a bytecode-cache sync). That branch was the operator's correct working branch for the KB task.
- 2026-07-11: That branch was fast-forward merged into `main` and pushed.
- 2026-07-11: The overarching target and 6-milestone breakdown above were agreed with the operator, replacing the earlier, narrower framing that only covered this folder's own file cleanup.
