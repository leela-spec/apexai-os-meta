---
title: "Reusable task prompt — benchmark orchestration systems vs KB best practice"
purpose: >
  Standalone prompt to re-run the same comparison cold, in a fresh session with no prior context.
  Already executed once on 2026-07-12; result at
  apex-meta/fable-orchestrator/orchestration-design-benchmark-20260712.md. Re-run only if the KB,
  System A, or System B changed materially since.
---

# Task: benchmark two orchestration systems against KB best practice

Repo root: `C:\GitDev\apexai-os-meta`, branch `main`. Read-only research — do not write or edit
files except the one output file named at the end.

There is a knowledge base of orchestration best practice at
`apex-meta/kb/claude-code-orchestration-design/`. Read its wiki/summaries and index to find its
concrete, checkable practices (context isolation, doctrine/instruction-loading efficiency,
state-vs-context separation, review/validation gating, terminology consistency, packet-size and
token-management patterns, resume/continuity design).

Two separately-built orchestration systems live on `main` and both need to be checked against it:

**System A — "Fable" multiagent orchestration** (general-purpose macro/meso/micro project
orchestrator): `apex-meta/orchestration/` (ARCHITECTURE.md, 00-START-HERE.md, GLOSSARY.md,
workflows/, schemas/, agents/DOCTRINE-MANIFEST.md + per-role CORE.md files) plus the runtime agent
defs under `.claude/agents/` for alfred, meta-strategy, meta-ops, meta-detective,
informatics-design, knowledge-bank, prompts-workflows, apex-review-validity, apex-review-alignment,
apex-plan-ops. Behavioral evidence: `apex-meta/orchestration/simulations/US-IDEA-01-20260711.md` and
`US-SEQ-01-20260712.md`.

**System B — "Weekly Orchestrator"** (recurring weekly/daily planning loop): `.claude/CLAUDE.md`
(core_loop/skills/agents tables), `.claude/skills/weekly-orchestrator/` (SKILL.md + references/),
runtime agent defs `.claude/agents/apex-precap-week.md`, `apex-precap-next-day.md`,
`apex-evidence-normalize.md`, `apex-flow-recap.md`, `apex-status-merge.md`,
`apex-project-status.md`. Design rationale: `apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md`.

Do not spawn either system's own agents to test them — this is an inspection-only comparison, not a
live run.

Produce a structured report with: (1) the KB's practices as a numbered checkable list with sources,
(2) System A vs each practice, (3) System B vs each practice, with file/line evidence and a
compliant/partial/non-compliant verdict per cell, (4) efficiency-specific findings with real numbers
where found (line counts, token counts, packet-size caps), (5) cross-system terminology/schema
convergence or divergence, flagging which divergences are recorded as deliberate product decisions
vs which look like uncoordinated duplication, (6) any KB practice neither system implements.

Save the final report to
`apex-meta/fable-orchestrator/orchestration-design-benchmark-<YYYYMMDD>.md`. No git commit or push.
