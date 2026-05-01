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
resolved_detail_lock: managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
```

This is a working decision-lock file for the developing Alfred workflow. It is not accepted doctrine by itself. It exists to preserve current decisions, open questions, and Q&A defaults while the Alfred personal-assistant workflow is being designed.

Canonical KB files remain under `managed/agent_kb/alfred/`. This file may inform those files later, but it must not bypass source/audit controls.

---

## 0.1 Supersession rule

- **Decision:** Newer operator corrections beat older assistant assumptions.
- **Decision:** All prior Q&A content from this workflow is considered validated unless it was explicitly corrected, rejected, or superseded by a newer operator message.
- **Decision:** The current strongest correction is that Alfred is the only personal-agent actor in this Apex/OpenClaw workflow.
- **Decision:** `managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md` resolves the prior open decisions about process-handover priority, Daily Command Board fields, MetaOps craft-flow handoff, Session Export / OpState separation, tracking, pattern learning, and planning horizon.
- **Decision:** The corrected priority model is `EVD / IMP / RSK + URG`, 1-100, for Alfred/Apex process handovers where time pressure matters.
- **Constraint:** If this file conflicts with older chat content, this file wins for the next Alfred-workflow iteration.
- **Constraint:** If a future operator message conflicts with this file, update this file before continuing workflow design.

---

## 1. Non-negotiable naming lock

### 1.1 Current-system naming

- **Decision:** The personal assistant in this Apex/OpenClaw environment is called **Alfred**.
- **Decision:** Alfred is the operator-facing personal assistant, organizer, planner, and workflow coordinator in this system.
- **Decision:** Alfred is the current test/development version of the future personal assistant concept.
- **Decision:** Do not introduce a second personal-agent actor for this workflow.
- **Decision:** Do not use any future Leela-app assistant name in ordinary Alfred workflow design, Q&A, user stories, templates, or repo patches.

### 1.2 Future app naming

- **Decision:** The future Leela app may use a different product name for the personal assistant.
- **Constraint:** That future app name must not be treated as a separate agent, separate owner, or parallel architecture inside this Apex/OpenClaw workflow.
- **Constraint:** The future Leela app is not the runtime environment for this process.
- **Constraint:** Future app naming may be discussed only in an explicit productization boundary section, not as the actor for current-system use cases.

### 1.3 Drift prevention rule

If a future answer splits Alfred from a separate in-app assistant actor, that answer is wrong for this workflow unless the operator explicitly asks for future product naming or app-spec comparison.

All current-system user stories must use **Alfred** as the actor.

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
- process-handover priority framing with `EVD / IMP / RSK + URG` when time pressure matters
- personal-context-aware recommendations
- calendar-aware and long-range planning recommendations
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
- replacing first-wave `EVD / IMP / RSK` handoff contracts with another metric family

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
- **Decision:** Alfred's first explicit heuristic layer is the corrected process-handover priority model: `EVD / IMP / RSK + URG` plus readiness, lane, hard flags, and P0-P3 classification.
- **Decision:** `URG` is added only where time pressure, deadline pressure, delay penalty, or blocked-window pressure materially affects priority.
- **Decision:** `value / urgency / leverage / fit` must not be reintroduced as canonical metric fields.
- **Current status:** use explicit heuristics first; do not claim a full product Algorithm exists.
- **Future path:** the heuristic layer may later inform the Leela app's Algorithm design.
- **Resolved task:** the first heuristic ranking model is defined in `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`.

---

## 4. Leela app boundary lock

- **Decision:** Leela is a future app/product, not the current agent infrastructure.
- **Decision:** The current workflow designs Alfred's real operator-assistant process first.
- **Decision:** The Leela app should later be built from the validated mechanisms, patterns, templates, tracking, and interaction learnings produced through Alfred.
- **Constraint:** Do not answer Alfred workflow questions as if Leela app screens, features, or agents already exist in this environment.
- **Constraint:** Use app language only when explicitly discussing future productization.
- **Deferred:** product-agnostic or detailed app-facing naming decisions are skipped until a later productization iteration.

---

## 5. Default working-day lock

### 5.1 Four craft-flow working day

- **Decision:** A normal working day is organized around **four craft-flow sessions**.
- **Decision:** These four craft flows represent the working day.
- **Decision:** Recovery/regeneration comes after the four work craft flows, not as a normal replacement for one of them.
- **Exception:** Alfred may deviate only if calendar/availability reality or explicit operator override makes four craft flows impossible.

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
- **Decision:** Urgent overrides are possible, but Alfred must name the tradeoff and the displaced work.
- **Decision:** No more than four P1 craft-flow items may be assigned in one day.
- **Decision:** P0 items are surfaced before normal allocation and are not auto-assigned by default.

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
- **Decision:** A craft-flow session may produce one concrete output or multiple concrete outputs.

### 6.3 Craft-flow essence

- **Decision:** A craft flow must combine multiple branches for holistic working experience.
- **Decision:** Physical/body activation and mental/cognitive process framing are essential to the craft-flow concept.
- **Decision:** Work-only craft flows are rejected for this workflow.
- **Decision:** Physical chunks are not project-linked by default.
- **Decision:** Emotional-tone coaching is not a default craft-flow component; use cognitive/process frames unless explicitly needed.
- **Clarification:** The 15-minute final break is an internal transition/reset inside the 120-minute craft-flow container. Larger regeneration belongs after the four-flow working day.

---

## 7. Morning planning lock

- **Decision:** Alfred should prepare the daily plan before the operator's morning starts.
- **Likely cadence:** daily morning job between 06:00 and 07:00.
- **Source:** the morning plan should be derived from Night outputs, Session Exports, project protocol outputs, priorities, calendar reality, and current default working-day policy.

### 7.1 Morning plan output

The morning output must include at least:

- project packets received from Night / OpenClaw processing
- project-specific night-shift protocols and outputs
- proposed daily shift process and task plans
- `EVD / IMP / RSK + URG` priority signals where time pressure matters
- ranked daily priorities
- proposed four craft-flow sessions
- proposed physical / mental / regen chunks where relevant
- MetaOps handoff requests for each work session
- visible assumptions and blocked items
- operator decisions needed

### 7.2 Daily Command Board template

- **Resolved:** the exact Daily Command Board v1 fields are defined in `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`.
- **Resolved:** physical, mental, and regen chunk selections appear through a separate `rhythm_profile`, not by bloating every craft-flow card.
- **Status:** ready for appendix integration before canonical KB patching.

### 7.3 Non-work routine planning

- **Decision:** Alfred may lightly begin planning non-work routines.
- **Boundary:** non-work routine planning must not displace the four craft-flow working day unless explicitly approved or calendar reality makes the default day impossible.

---

## 8. Session outro and Night loop lock

### 8.1 Session outro

- **Decision:** Every craft-flow session has an outro process.
- **Decision:** The outro defines next highest-impact tasks with the operator.
- **Decision:** The outro feeds Night processing.
- **Decision:** The outro should be based on a pre-filled scaffold generated from what Night expected to happen.
- **Decision:** The operator corrects the pre-filled scaffold with actual output, updated priorities, blockers, and next tasks.
- **Decision:** Best-practice direction: the operator can drop session outputs into the scaffold and correct the anticipated next steps instead of writing the outro from scratch.
- **Decision:** Alfred and MetaOps both process the corrected session outro.
- **Resolved:** exact low-friction Session Export correction fields are defined in `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`.

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
- what project-specific daily shift plans should be proposed with `EVD / IMP / RSK + URG` priority signals where relevant

### 8.3 Repo protocol relationship

- **Decision:** Use the existing Session Export and Night Planning protocols as the operating-spine basis.
- **Known repo paths:**
  - `managed/rituals/NIGHT_PLANNING_PROTOCOL.md`
  - `managed/rituals/SESSION_EXPORT_PROTOCOL.md`
- **Action:** process files should be patched only if the corrected Alfred/Apex model exposes a real contradiction, gap, or pointer update need.

---

## 9. Pattern-library lock

- **Decision:** Alfred should create and evolve his own pattern library from the operator's interactions, behaviors, repeated workflows, repeated craft-flow structures, and recurring planning corrections.
- **Decision:** Pattern candidates should start lightweight and become durable only through repeated use, operator validation, and KB/promotion discipline.
- **Decision:** Pattern-library development should be designed as a process and KB logic, not as an ad-hoc memory dump.
- **Resolved:** pattern candidate creation and promotion thresholds are defined in `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`.

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
- **Decision:** Define complex user flows and interactions early enough to create a solid first learning system.

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

### 10.4 Tracking schema status

- **Resolved:** minimum acceptable tracking format is defined in `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`.

---

## 11. Skill-tree / chunk-system lock

- **Decision:** Alfred should eventually help build a personal chunk, epic, and skill-tree system from use.
- **Decision:** This is not the top-priority definition task right now.
- **Decision:** The personal system may be defined by the operator later and then evolve through usage.
- **Decision:** Branch/life-domain classification may later be defined by the Leela system/product logic.
- **Current posture:** build lightly through lived usage, tracking, and pattern candidates; do not over-design taxonomy now.

---

## 12. Rhythm logic lock

- **Decision:** Rhythm is not a separate app feature in this workflow.
- **Decision:** Rhythm is not a separate agent in v1.
- **Decision:** Rhythm should be represented as a reference logic or KB entry for Alfred.
- **Definition:** Rhythm is Alfred's gamified life/time planning logic for days, weeks, and eventually months.
- **Purpose:** give excellent recommendations by balancing project priority, calendar reality, craft-flow placement, branch balance, and long-range planning.

### 12.1 Rhythm reference should support

- daily planning
- weekly planning
- month-ahead planning
- calendar-aware flow placement
- four-craft-flow working day protection
- afterwork regeneration placement
- project-priority conflict resolution
- physical / mental / regen branch balancing
- future Leela product logic extraction

### 12.2 Calendar and long-range planning

- **Decision:** Alfred may use calendar knowledge to plan ahead.
- **Decision:** Alfred may plan days, weeks, and months as recommendations.
- **Decision:** v1 planning horizon is daily plus light weekly preview.
- **Decision:** full Weekly Rhythm Plan belongs to v1.1 after daily tracking evidence exists.
- **Decision:** monthly planning is later and directional only when used.
- **Constraint:** Alfred must not silently mutate calendar state or commit the operator to events without permission.
- **Resolved:** how far ahead Alfred should plan in v1 is defined in `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`.

---

## 13. Q&A flow requirement

- **Decision:** Before KB building, create a comprehensive Q&A flow.
- **Decision:** Every question must be prefilled with a proposed answer, recommendation, and options.
- **Purpose:** the operator validates, corrects, or improves the prefilled answers.
- **Constraint:** the Q&A must use Alfred as the current system actor and must not split off a second personal agent.

### 13.1 Required Q&A blocks

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
11. Personal chunk / epic / skill-tree evolution
12. Rhythm reference logic
13. Next-action decision logic
14. Calendar and long-range planning
15. Future Leela productization boundary
16. KB integration path

---

## 14. Immediate next steps

1. Use this file and `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md` as context locks before further Alfred workflow design.
2. Create appendices in this order:
   - `APPENDIX_PROCESS_HANDOVER_PRIORITY.md`
   - `APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md`
   - `APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md`
   - `APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md`
3. Run completeness, simplification, and process/handoff audits.
4. Only then patch canonical Alfred KB files.

---

## 15. Current open questions

1. Should Rhythm logic be a single appendix first or a separate working package with multiple templates?
2. Which later pattern-library storage path should hold rejected candidates before canonical promotion infrastructure exists?
3. What exact evidence threshold should later permit low-risk OpState auto-apply classes?
4. How should full Weekly Rhythm Plan v1.1 be represented after enough daily tracking exists?

---

## 16. Resolved open questions

| Prior open question | Resolution |
|---|---|
| Exact fields in Daily Command Board | Resolved in `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`. |
| Exact fields in pre-filled Session Export scaffold | Resolved through operator-required Session Export fields in `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`. |
| First heuristic ranking formula before full Algorithm | Resolved as `EVD / IMP / RSK + URG` process-handover priority model plus readiness, lane, hard flags, and P0-P3 classification. |
| How far ahead Alfred should plan in v1 | Resolved as daily + light weekly preview; full weekly v1.1; monthly later/directional. |
| Where working-pattern candidates live before promotion | Resolved as candidate-first pattern learning with promotion and rejected-candidate archive rules; exact long-term storage path remains future-improvement detail. |
| Minimum acceptable tracking format | Resolved as `tracking_record_v1`. |
| Exact MetaOps handoff schema | Resolved as `metaops_craft_flow_handoff_v1`, while preserving formal first-wave handoff requirements when applicable. |
| Which daily board fields are editable by the operator | Resolved through board lock/revision rule. |
| Night scaffold low-friction correction | Resolved through operator-required Session Export fields and correction event rule. |

---

## 17. Rejected older assumptions

These older assumptions are superseded and must not be reintroduced:

- A separate current-system personal agent distinct from Alfred.
- User stories for current-system workflow using the future app assistant name instead of Alfred.
- A separate timekeeper/nudge role split away from Alfred in this architecture.
- Treating Leela app as current runtime participant.
- Treating Rhythm as an app feature or separate agent in v1.
- Recovery replacing one of the four normal working craft flows.
- Work-only craft flows.
- Project-linked physical chunks by default.
- Mood/energy tracking in Alfred tracking v1.
- Emotional-tone coaching as default craft-flow logic.
- Branch/taxonomy over-design before usage creates enough evidence.
- A parallel `value / urgency / leverage / fit` metric system.
- 0-3 orientation scoring as the canonical process-handover model.

---

## 18. Update log

| Date | Change |
|---|---|
| 2026-05-01 | Initial working decision-lock file created from operator corrections after Alfred interaction-design Q&A. |
| 2026-05-01 | Controlled against `ChatsoFar.md`; added supersession rule, stronger Alfred-only naming lock, long-range planning, protocol paths, session-scaffold details, skill-tree posture, rejected-assumption register, and expanded open questions. |
| 2026-05-01 | Updated after corrected `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`; resolved prior open questions with `EVD / IMP / RSK + URG` process-handover priority model and rejected V/U/L/F as a parallel canonical metric system. |
