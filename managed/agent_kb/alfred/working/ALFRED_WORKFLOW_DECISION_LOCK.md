# ALFRED_WORKFLOW_DECISION_LOCK

## 0. File role

```yaml
file_id: ALFRED_WORKFLOW_DECISION_LOCK
repo: leela-spec/apexai-os-meta
path: managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md
status: working_context_file
canonical_status: non_canonical
purpose: prevent drift during Alfred workflow design before KB hardening
owner: operator_and_alfred_workflow_design
update_rule: update after every newly validated workflow decision
read_rule: read before answering or patching Alfred workflow / personal-assistant design questions
promotion_rule: validated decisions may later be promoted into canonical Alfred KB files through the normal source/audit/promotion path
```

This is a working decision-lock file for the developing Alfred workflow. It is not accepted doctrine by itself. It exists to preserve current decisions, open questions, and Q&A defaults while the Alfred personal-assistant workflow is being designed.

Canonical KB files remain under `managed/agent_kb/alfred/`. This file may inform those files later, but it must not bypass source/audit controls.

---

## 1. Non-negotiable naming lock

### 1.1 Current-system naming

- **Decision:** The personal assistant in this Apex/OpenClaw environment is called **Alfred**.
- **Decision:** Alfred is the operator-facing personal assistant, organizer, planner, and workflow coordinator in this system.
- **Decision:** Do not introduce a second personal-agent actor for this workflow.
- **Decision:** Do not use the future Leela-app personal-agent name in ordinary Alfred workflow design.

### 1.2 Future app naming

- **Decision:** The future Leela app may use a different product name for the personal assistant.
- **Constraint:** That future app name must not be treated as a separate agent, separate owner, or parallel architecture inside this Apex/OpenClaw workflow.
- **Constraint:** The future Leela app is not the runtime environment for this process.

### 1.3 Drift prevention rule

If a future answer splits Alfred from a separate in-app assistant actor, that answer is wrong for this workflow unless the operator explicitly asks for future product naming or app-spec comparison.

---

## 2. Alfred identity lock

- **Decision:** Alfred is the operator-facing personal executive assistant in this system.
- **Decision:** Alfred is not merely a router.
- **Decision:** Alfred is not the Leela app.
- **Decision:** Alfred uses Leela-like mechanisms and life-operating logic to organize the operator's real work and days.
- **Decision:** Alfred's lived-use patterns may later inform the Leela app design.
- **Constraint:** Alfred must not drift into being a full product runtime, project executor, or separate app simulation.

### 2.1 Alfred owns

- daily personal operating synthesis
- morning planning before the operator starts work
- organization of the four craft-flow working day
- ranking of project outputs and next tasks from the operator's perspective
- personal-context-aware recommendations
- session outro prompting and completion support
- next-highest-impact task framing
- pattern-library evolution from repeated interactions
- light chunk / epic / workflow candidate capture from real usage
- Rhythm-style planning logic as a reference model
- handoff quality to MetaOps and Knowledge/KB operations

### 2.2 Alfred does not own

- detailed project execution workflows
- prompt-chain engineering inside every work sprint
- full AI-routing implementation for project tasks
- silent SSOT mutation
- silent calendar mutation
- final truth promotion
- pretending the future Leela app already exists as runtime
- acting as a separate product agent from himself

---

## 3. Adjacent owner lock

### 3.1 MetaOps

- **Decision:** MetaOps owns project-facing workflow decomposition.
- **Decision:** MetaOps creates sprint workflows, task chains, prompt chains, and AI-routing packages for craft-flow work sessions.
- **Decision:** Alfred and MetaOps jointly decide what should be tackled when project priority and personal/day context interact.
- **Boundary:** Alfred decides why this matters for the operator's day; MetaOps structures how to execute the work.

### 3.2 Knowledge / KB operations

- **Decision:** Alfred should cooperate with the Knowledge/KB sub-head to evolve pattern libraries, chunk candidates, epic/block candidates, reusable workflows, and future product-learning material.
- **Boundary:** Alfred may nominate and describe candidates; KB operations hardens, places, audits, or promotes them.

### 3.3 Algorithm / decision logic

- **Decision:** Alfred may need a logic layer to decide what to do next.
- **Current status:** use explicit heuristics first; do not claim a full product Algorithm exists.
- **Future path:** the heuristic layer may later inform the Leela app's Algorithm design.

---

## 4. Leela app boundary lock

- **Decision:** Leela is a future app/product, not the current agent infrastructure.
- **Decision:** The current workflow designs Alfred's real operator-assistant process first.
- **Decision:** The Leela app should later be built from the validated mechanisms, patterns, templates, tracking, and interaction learnings produced through Alfred.
- **Constraint:** Do not answer Alfred workflow questions as if Leela app screens, features, or agents already exist in this environment.
- **Constraint:** Use app language only when explicitly discussing future productization.

---

## 5. Default working-day lock

### 5.1 Four craft-flow working day

- **Decision:** A normal working day is organized around **four craft-flow sessions**.
- **Decision:** These four craft flows represent the working day.
- **Decision:** Recovery/regeneration comes after the four work craft flows, not as a normal replacement for one of them.
- **Exception:** Alfred may deviate only if calendar reality, sickness, travel, or explicit operator override makes four craft flows impossible.

### 5.2 Default allocation

```yaml
default_daily_craft_flow_allocation:
  flow_1: Leela_app_development_or_related_product_work
  flow_2: Leela_app_development_or_related_product_work
  flow_3: Master_of_Arts_business_or_system_work
  flow_4: wildcard_highest_current_priority
```

- **Decision:** Two flows are normally reserved for Leela-related app/product/build/spec work.
- **Decision:** One flow is normally reserved for Master of Arts business/system work.
- **Decision:** One flow remains wildcard and is assigned by current priority.

---

## 6. Craft-flow timing lock

### 6.1 Default Sprint Alex structure

```yaml
craft_flow_template: Sprint Alex
container_minutes: 120
sprints: 3
sprint_minutes: 35
final_break_minutes: 15

per_sprint:
  activity: 2
  mental: 3
  pre_cap: 1
  deep_work: 28
  re_cap: 1

totals:
  activity: 6
  mental: 9
  pre_cap: 3
  deep_work: 84
  re_cap: 3
  break: 15
  total: 120
```

### 6.2 Timing interpretation

- **Decision:** Pre-Cap and Re-Cap count into the work sprint.
- **Decision:** Pre-Cap is a cognitive intro step before deep work.
- **Decision:** Re-Cap is a cognitive outro step after deep work.
- **Decision:** Every sprint ends with a recap.
- **Decision:** The final sprint/session has a real output protocol saved for the Night shift.

### 6.3 Craft-flow essence

- **Decision:** A craft flow must combine multiple branches for holistic working experience.
- **Decision:** Physical/body activation and mental/cognitive process framing are essential to the craft-flow concept.
- **Decision:** Work-only craft flows are rejected for this workflow.
- **Decision:** Physical chunks are not project-linked by default.
- **Decision:** Emotional-tone coaching is not a default craft-flow component; use cognitive/process frames unless explicitly needed.

---

## 7. Morning planning lock

- **Decision:** Alfred should prepare the daily plan before the operator's morning starts.
- **Likely cadence:** daily morning job between 06:00 and 07:00.
- **Source:** the morning plan should be derived from Night outputs, Session Exports, project protocol outputs, priorities, calendar reality, and current default working-day policy.

### 7.1 Morning plan output

The morning output must include at least:

- project packets received from Night / OpenClaw processing
- ranked daily priorities
- proposed four craft-flow sessions
- proposed physical / mental / regen chunks where relevant
- MetaOps handoff requests for each work session
- visible assumptions and blocked items
- operator decisions needed

### 7.2 High-priority unresolved template

- **Open task:** define the exact Daily Command Board template.
- **Status:** high priority before KB hardening.

---

## 8. Session outro and Night loop lock

### 8.1 Session outro

- **Decision:** Every craft-flow session has an outro process.
- **Decision:** The outro defines next highest-impact tasks with the operator.
- **Decision:** The outro feeds Night processing.
- **Decision:** The outro should be based on a pre-filled scaffold generated from what Night expected to happen.
- **Decision:** The operator corrects the pre-filled scaffold with actual output, updated priorities, blockers, and next tasks.

### 8.2 Night processing

Night processing must compare and synthesize:

- what was planned last night
- what actually happened in the day/session
- which process worked
- which chat/workflow patterns were efficient
- what learnings emerged
- what KB/pattern candidates should be updated
- what improved flows should be proposed for the next day
- what project-specific tasks or protocols should be prepared for the morning

### 8.3 Repo protocol relationship

- **Decision:** Use the existing Session Export and Night Planning protocols as the operating-spine basis.
- **Action:** before patching those protocols, run a delta audit against the uploaded versions.

---

## 9. Pattern-library lock

- **Decision:** Alfred should create and evolve his own pattern library from the operator's interactions, behaviors, repeated workflows, repeated craft-flow structures, and recurring planning corrections.
- **Decision:** Pattern candidates should start lightweight and become durable only through repeated use, operator validation, and KB/promotion discipline.
- **Decision:** Pattern-library development should be designed as a process and KB logic, not as an ad-hoc memory dump.

### 9.1 Pattern candidates include

- repeated daily planning structures
- repeated craft-flow variants
- repeated project handoff structures
- repeated prompt/workflow chains
- repeated chunk combinations
- repeated failure/repair patterns
- repeated next-action ranking patterns

---

## 10. Tracking lock

### 10.1 Start infrastructure now

- **Decision:** Start building tracking infrastructure now so the system can learn from use.
- **Decision:** Tracking may become central for later epics, chunks, and future Algorithm development.

### 10.2 Track in v1

- planned craft flow
- actual craft flow
- planned output
- actual output
- sprint completion
- next highest-impact task
- blockers
- deviation reason
- process worked / did not work
- chat/workflow efficiency signal
- pattern candidate
- chunk candidate

### 10.3 Do not track in v1

- mood
- energy
- complex emotional state
- authoritative BP/XP
- biometric/body signals

---

## 11. Rhythm logic lock

- **Decision:** Rhythm is not a separate app feature in this workflow.
- **Decision:** Rhythm is not a separate agent in v1.
- **Decision:** Rhythm should be represented as a reference logic or KB entry for Alfred.
- **Definition:** Rhythm is Alfred's gamified life/time planning logic for days, weeks, and eventually months.
- **Purpose:** give excellent recommendations by balancing project priority, calendar reality, craft-flow placement, branch balance, and long-range planning.

### 11.1 Rhythm reference should support

- daily planning
- weekly planning
- month-ahead planning
- calendar-aware flow placement
- four-craft-flow working day protection
- afterwork regeneration placement
- project-priority conflict resolution
- physical / mental / regen branch balancing
- future Leela product logic extraction

---

## 12. Q&A flow requirement

- **Decision:** Before KB building, create a comprehensive Q&A flow.
- **Decision:** Every question must be prefilled with a proposed answer, recommendation, and options.
- **Purpose:** the operator validates, corrects, or improves the prefilled answers.
- **Constraint:** the Q&A must use Alfred as the current system actor and must not split off a second personal agent.

### 12.1 Required Q&A blocks

1. Alfred identity and naming
2. Alfred vs MetaOps
3. Alfred vs Knowledge/KB operations
4. Morning planning
5. Four craft-flow day
6. Craft-flow template and timing
7. Session outro
8. Night processing
9. Pattern library
10. Tracking v1
11. Rhythm reference logic
12. Next-action decision logic
13. Calendar and long-range planning
14. Future Leela productization boundary
15. KB integration path

---

## 13. Immediate next steps

1. Use this file as the context lock before further Alfred workflow design.
2. Create the prefilled Q&A flow for operator validation.
3. After Q&A validation, create appendix drafts.
4. Only then patch canonical Alfred KB files.

---

## 14. Current open questions

1. What exact fields belong in the Daily Command Board?
2. What exact fields belong in the pre-filled Session Export scaffold?
3. What exact heuristic ranking formula should Alfred use before a full Algorithm exists?
4. How far ahead should Alfred plan in v1: day only, week, or month?
5. Where should working-pattern candidates live before promotion into canonical KB?
6. Should Rhythm logic be a single appendix first or a separate working package with multiple templates?
7. What is the minimum acceptable tracking format for the first live use?

---

## 15. Update log

| Date | Change |
|---|---|
| 2026-05-01 | Initial working decision-lock file created from operator corrections after Alfred interaction-design Q&A. |
