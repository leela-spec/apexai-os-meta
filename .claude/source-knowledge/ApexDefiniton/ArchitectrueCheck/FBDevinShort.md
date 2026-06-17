## 1. Correct and Hermes-compatible

**The loop structure itself is sound.** A weekly cron → daily cron → human execution → recap → status merge → next daily cron is a valid Hermes pattern. Cron jobs support `schedule`, `profile`, `skills`, and `workdir` fields that can carry this. jobs.py:39-45

**Skills as procedural knowledge units is correct.** `FlowRecapSkill`, `PreCapNextDay`, and `AllProjectStatusPacketUpdate` can each become a `SKILL.md` — a directory with YAML frontmatter and step-by-step instructions the agent reads on demand. This is exactly what skills are for. skills_tool.py:9-13

**Kanban for dependency-gated task graphs is correct.** The F1→F2→F3→F4 ordering and the FlowRecap→APSU dependency map directly to Kanban `parents=[...]` links. The dispatcher auto-promotes child tasks only after all parents reach `done`. SKILL.md:71-72

**Profile distributions as the packaging unit is correct.** A `distribution.yaml` can bundle `SOUL.md`, `skills/`, and `cron/` together — this is the right way to ship a self-contained orchestration persona. profile_distribution.py:87-94

**Operator gate → `kanban_block()` is correct.** The plan's `operator_validated_next_step` requirement maps cleanly to a worker calling `kanban_block()` to pause for human review, then the operator unblocking with feedback. SKILL.md:161

---

## 2. Mistaken or based on wrong Hermes assumptions

**"FlowRecapSkill" is not a Hermes skill in the runtime sense.** In Hermes, a skill is a `SKILL.md` file containing procedural instructions — it is not an executable process, callable function, or agent. Naming it `FlowRecapSkill` implies it is invoked like a function. It should be renamed to something like `flow-recap` (a skill directory) and the _execution_ of it should be a Kanban task or cron job that loads the skill. prompt_builder.py:170-176

**`MEMORY.md` cannot store artifacts.** The plan's artifacts (flow packets, APSU outputs, FlowRecap packets) are large structured documents. `MEMORY.md` has a hard 2200-character limit and `USER.md` has 1375 characters. These files are for short agent notes, not structured artifact storage. All artifacts must be stored as regular files in the filesystem (e.g., `~/.hermes/home/` or `~/.hermes/workspace/`). memory_tool.py:5-14

**Cron is time-based only — not event-driven.** The plan implies APSU completion triggers the next `PreCapNextDay`. Cron jobs fire on schedules (`every Xh`, cron expressions, ISO timestamps), not on artifact completion or process output. The event-driven trigger for `APSU → PreCapNextDay` must be implemented via Kanban dependency links, not cron. jobs.py:209-247

**Cron jobs cannot create more cron jobs.** The plan's loop implies one cron job spawning the next cycle. Hermes explicitly disables the `cronjob` toolset inside cron executions to prevent recursive scheduling loops. The loop must be implemented as a recurring cron schedule (e.g., `every 24h`) or via Kanban, not by having one job create the next. scheduler.py:60-73

**"Profiles" is used ambiguously.** In Hermes, a profile is a full agent identity with its own `SOUL.md`, `config.yaml`, `memories/`, `skills/`, and `cron/`. The plan uses "profile" loosely to mean toolset configuration or process role. You need to decide: is this one profile doing everything, or multiple profiles (e.g., a `planner` profile and a `recap` profile)? This decision determines cron job ownership and Kanban `assignee` names. Unknown assignee names cause tasks to sit in `ready` forever with no error. SKILL.md:18-21

---

## 3. Underdefined, ambiguous, or missing

**How does the operator's raw dump enter Hermes?** `OperatorExecutesPlannedFlow` is correctly marked as a human action, but the plan does not define the input gate. Does the operator paste into a Hermes chat session? Write a file to a known path? Upload via the web UI? This is the most critical undefined handoff in the entire loop. Without it, `FlowRecapSkill` has no reliable input.

**Which profile(s) own which processes?** The plan lists processes but never assigns them to a Hermes profile. A cron job must have a `profile` field. A Kanban task must have an `assignee`. These must be real profile names that exist on the machine. scheduler.py:174-180

**`PromptAndAIRoutingPlanning` is referenced but never defined.** It appears as a producer of `A4_prompt_packet` and a consumer of `routing_recommendation_packet`, but has no process definition in the document. It is either a skill, a manual operator step, or a section of `PreCapNextDay`. Decide which.

**Logical location slots have no Hermes mapping.** `WEEKLY_PLAN_SLOT`, `FLOW_RECAP_SLOT`, etc. are defined abstractly but never mapped to Hermes filesystem conventions. The relevant user-owned paths in Hermes are `~/.hermes/home/`, `~/.hermes/workspace/`, and `~/.hermes/plans/`. Pick one convention now — the agent needs to know where to write and read files. profile_distribution.py:100-119

**`ModelSubscriptionUsageTracking` schema contradictions are unresolved.** The plan itself flags `confidence_medium_high`, `reserve_for`, and `source_update_id` as broken. These must be resolved before any runtime file is written. This process is also the most speculative — it assumes Hermes can track per-model token usage across sessions, which it does not do natively.

---

## 4. What to define before creating runtime files

In priority order:

1. **Single profile or multi-profile?** Name the profile(s) that will own each cron job and Kanban task. This is a blocking decision for everything else.
2. **Operator raw dump input gate.** Define exactly how the operator's output enters the system (file path convention, chat paste, or upload). This unblocks `FlowRecapSkill`.
3. **Filesystem layout for artifacts.** Map each logical slot to an actual path under `~/.hermes/home/` or `~/.hermes/workspace/`. Example: `FLOW_RECAP_SLOT` → `~/.hermes/home/recaps/{execution_day_id}/{flow_id}.md`.
4. **Trigger mechanism for APSU → PreCapNextDay.** Choose: Kanban dependency (preferred) or fixed daily cron schedule. Not both.
5. **Resolve `ModelSubscriptionUsageTracking` scope.** Either simplify it to a plain append-log file + a skill that reads it, or defer it entirely. Do not let it block the core loop.

---

## 5. Simplify, rename, merge, or split

|Current name|Recommendation|
|---|---|
|`FlowRecapSkill`|Rename to `flow-recap` (skill directory). The "Skill" suffix is redundant and misleading.|
|`AllProjectStatusPacketUpdate`|Rename to `status-merge` or `apsu`. The full name is unwieldy in Kanban task titles and cron prompts.|
|`OperatorExecutesPlannedFlow`|This is not a process — remove it from the process list. Replace with a documented operator SOP (standard operating procedure) section.|
|`A5_context_instruction_packet`|Merge into `A3_flow_packet`. The plan already notes it is embedded. Remove as a separate artifact.|
|`A8_project_status_delta` + `A9_model_usage_delta`|Keep as named sections within `A7_flow_recap_packet`, not as separate files. One file per flow recap, with sections.|
|`ModelSubscriptionUsageTracking`|Simplify to a skill (`model-usage-log`) + one append-only log file. Defer routing recommendation logic to a later cycle.|
|`PromptAndAIRoutingPlanning`|Either merge into `PreCapNextDay` as a section, or define it as a skill. Do not leave it as an unnamed producer.|

---

## 6. Hermes runtime mapping recommendations

```
PreCapWeek  
  → cron job, weekly schedule (e.g. "0 8 * * MON")  
  → profile: <your-planner-profile>  
  → skills: [precap-week]  
  → writes: ~/.hermes/home/plans/week-{week_id}.md  
  
PreCapNextDay  
  → cron job, daily schedule (e.g. "0 9 * * *")  
    OR Kanban child task (parents=[apsu_task_id])  
  → profile: <your-planner-profile>  
  → skills: [precap-next-day, flow-recap, model-usage-log]  
  → reads: week plan, APSU output, previous recaps  
  → writes: ~/.hermes/home/plans/day-{execution_day_id}.md  
  
FlowRecapSkill (renamed: flow-recap)  
  → SKILL.md with procedural instructions  
  → invoked via: Kanban task per flow (F1, F2, F3, F4)  
  → assignee: <your-planner-profile>  
  → reads: flow packet from day plan file + operator raw dump file  
  → writes: ~/.hermes/home/recaps/{execution_day_id}/{flow_id}.md  
  
AllProjectStatusPacketUpdate (renamed: status-merge)  
  → Kanban task  
  → parents: [F1_recap_task, F2_recap_task, F3_recap_task, F4_recap_task]  
  → assignee: <your-planner-profile>  
  → skills: [status-merge]  
  → reads: all four recap files  
  → writes: ~/.hermes/home/status/apsu-{execution_day_id}.md  
  
OperatorExecutesPlannedFlow  
  → NOT a Hermes process  
  → operator SOP: read day plan, execute, write raw dump to  
    ~/.hermes/home/dumps/{execution_day_id}/{flow_id}-dump.md  
  → operator then runs: hermes kanban unblock <recap_task_id>  
    (or the recap task polls for the dump file's existence)  
  
ModelSubscriptionUsageTracking  
  → SKILL.md (model-usage-log) with append instructions  
  → log file: ~/.hermes/home/usage/usage-log.md  
  → summary: written by status-merge task as a section of APSU output  
```

---

## 7. Next best steps

1. **Decide profile architecture** (one profile vs. two). Write the profile name(s) down. Everything else depends on this.
2. **Define the operator raw dump convention**: exact file path template, minimal required fields, and how the operator signals "dump is ready" (e.g., creates the file → Kanban task polls or operator manually unblocks).
3. **Write one complete `SKILL.md` for `flow-recap`** as the proof-of-concept skill. This forces you to resolve the input/output contract concretely. Use F1 (Leela) as the example.
4. **Write one complete Kanban task graph for one execution day** (four recap tasks + one status-merge task with parents). This proves the dependency wiring before any cron is written.
5. **Map all logical slots to actual paths** under `~/.hermes/home/`. Write this as a one-page reference before touching any spec.

---

## 8. Do not do yet

- Do not write `SKILL.md` files for all processes simultaneously. Prove one (flow-recap) first.
- Do not implement `ModelSubscriptionUsageTracking` beyond a plain log file until the core loop runs end-to-end.
- Do not create cron jobs until the Kanban task graph for one day has been manually validated.
- Do not define `PromptAndAIRoutingPlanning` as a separate process until `PreCapNextDay` is stable — it is likely just a section of that skill.
- Do not invent profile names for Kanban `assignee` fields until you have run `hermes profile list` and confirmed what actually exists on the machine. SKILL.md:22-28