---
title: "Subscription AI Handoff — ProjectStatus and PreCap Week G1"
document_role: subscription_ai_execution_handoff
created: 2026-08-16
updated: 2026-08-16
status: ready
run_date: 20260816
week_id: 2026-W34
actor: subscription_ai_main_chat
stop_gate: G1
---

# Objective

Use repository truth to create the first full-portfolio ProjectStatus overview, collect only the missing W34-specific inputs from the operator, run PreCap Week G1 through the existing weekly orchestration contracts, commit and push the resulting artifacts, and stop for operator approval. Do not run G2.

# Required reading order

1. `apex-meta/handoff/portfolio-project-capture-cursor-20260816.md`
2. `apex-meta/handoff/planning-feed-20260816-w34.md`
3. `apex-meta/handoff/sync-reports/20260816-w34/next.json`
4. `apex-meta/handoff/sync-reports/20260816-w34/blockers.json`
5. `apex-meta/handoff/sync-reports/20260816-w34/score.json`
6. `.claude/skills/ProjectStatus/SKILL.md`
7. `.claude/skills/PrecapWeek/SKILL.md`
8. `.claude/skills/PrecapWeek/weekly-plan-output-contract.md`
9. `.claude/skills/weekly-orchestrator/SKILL.md`
10. `.claude/agents/apex-precap-week.md`
11. `.claude/skills/weekly-orchestrator/references/handoff-schema.md`

# Execution process

## 1. Establish repository truth

- Pull `origin/main` before reading sources.
- Treat canonical task files under `apex-meta/epics/`, the confirmed planning feed, and the committed Sync reports as authority.
- Do not reconstruct accepted state from this chat or from proposal packets.
- Preserve explicit blockers, missing inputs, unknown deadlines, and equal operator priority across the three Investment workstreams.
- Do not run `registry --dry-run false` and do not mutate canonical project/task files.

## 2. Generate ProjectStatus

Create:

`artifacts/weekly-plans/project-status-overview-20260816.md`

Requirements:

- cover the full active portfolio using the fixed roster `Leela`, `MasterOfArts`, `Apex`, `Investment`, `Residual`;
- use the ProjectStatus project → task → subtask boundary;
- derive feasibility and next-action signals from committed Sync evidence;
- use `[priority/urgency/date]` ratings only when evidence supports them;
- use `NA` for unknown dates and visibly flag uncertain ratings for operator review;
- preserve Dating as a W34 capacity input under Residual, not as a project or task;
- do not create weekly direction inside the ProjectStatus artifact.

## 3. Collect W34-only operator inputs

After ProjectStatus exists, ask the operator one compact message containing only the missing values below. Do not answer these questions on the operator's behalf.

1. What is the single most important outcome for W34, and what is the minimum result that would make the week successful?
2. Which categories should be primary, secondary, maintenance, deferred, or recovery this week? State any explicit priority override.
3. What fixed appointments, unavailable periods, deadlines, or reduced-capacity days affect Monday 2026-08-17 through Friday 2026-08-21?
4. How much total focused-work capacity is realistically available, and is there a specific Dating time allocation?
5. Are there any tasks or categories that must be excluded from this week?

Use the exact operator answers as stage inputs. If the operator explicitly says a value is unknown or unavailable, record that as missing input and use the PreCap Week degraded behavior; do not invent it.

## 4. Run PreCap Week G1

Dispatch the existing PreCap Week stage with:

```yaml
run_date: 20260816
week_id: 2026-W34
input_paths:
  - apex-meta/handoff/planning-feed-20260816-w34.md
  - apex-meta/handoff/sync-reports/20260816-w34/next.json
  - apex-meta/handoff/sync-reports/20260816-w34/blockers.json
  - apex-meta/handoff/sync-reports/20260816-w34/score.json
  - artifacts/weekly-plans/project-status-overview-20260816.md
operator_stage_inputs:
  - exact W34 answers collected in step 3
```

Create:

`artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md`

The packet must follow the PreCap Week output contract and weekly-orchestrator envelope contract. It must remain a proposal with `gate: G1`, `authority.state: candidate`, and `operator_validation: not_requested`.

## 5. Verify, commit, push, and stop

- Verify both target artifacts exist and contain the required fixed roster.
- Verify the G1 packet includes `first_precap_next_day_seed` and visible operator-review flags.
- Verify no canonical task, registry, calendar, G2, prompt-packet, or execution artifact was changed.
- Commit only the two target artifacts and push `main`.
- Present the G1 summary and exact approval question to the operator.
- Stop. Do not run G2, OpenClaw, project execution, status merge, or Session mutation.

# Exact first message for the subscription AI

```text
Continue the W34 weekly orchestration from repository truth. Pull origin/main, read and execute apex-meta/handoff/plan-packets/subscription-ai-projectstatus-precap-g1-handoff-20260816-w34.okf.md exactly. Generate ProjectStatus first, then ask me the compact W34-only input questions specified there. After I answer, run PreCap Week G1, commit and push only the two named artifacts, present the G1 approval question, and stop. Do not run G2.
```
