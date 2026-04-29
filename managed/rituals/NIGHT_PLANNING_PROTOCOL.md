# NIGHT_PLANNING_PROTOCOL

## 1. Purpose

- **Decision:** This file defines the principal synthesis cycle for cross-session continuity inside the OpenClaw operating spine.
- **Decision:** Night planning converts bounded session trace, project control state, promotion candidates, hygiene findings, and open holds into next-cycle plans.
- **Decision:** Night planning is explicit ritual authority, not hidden behavior inside `HEARTBEAT.md` or companion docs.
- **Constraint:** Night planning may recommend truth change or state updates, but it may not directly mutate accepted truth.

## 2. Inputs

- Night planning must read, at minimum:
  - latest active Session Export artifacts
  - current project interface surfaces: `ProjCard`, `OpState`, `SSOT_INDEX`, and `SigMat`
  - `role: ORCHESTRATION`
  - `surface: night_plan`
  - `quality: reliable`
  - `scope: session` or `project` for per-project variants, `system` for global meta synthesis
- **Decision:** the global nightly synthesis artifact is normally `scope: system`.
- **Decision:** per-project night outputs may exist when a project needs its own bounded nightly synthesis.
- **Keep as compatibility bridge:** legacy planning files may be mapped temporarily if the mapping is explicit and the lane split remains legible.
- **Rule:** Read through the project interface contract first.
- **Constraint:** Deep project traversal is justified only when an interface is invalid, an escalation requires source inspection, or a bounded planning question cannot be answered from exposed surfaces.
- **Constraint:** `HEARTBEAT.md` may surface continuity signals, but it does not become silent planning authority.

## 3. Output structure

Night planning must produce a bounded Night Plan with:

### 3.1 Cycle header

- `cycle_id`
- `generated_at`
- `scope`
- `source_window`

### 3.2 Input summary

- bounded list of the surfaces synthesized

### 3.3 Project progress lane

- next session targets
- major blockers
- bounded execution recommendations
- priority shifts
- candidate review needs

### 3.4 Infrastructure and hygiene lane

- missing interface surfaces
- stale state
- broken pointers or dependencies
- unresolved authority leakage
- structural-risk backlog
- hygiene holds

### 3.5 Operator plan summary

- recommended interactive session targets
- recommended order
- operator-facing constraints or prerequisites
- what needs human judgment

### 3.6 Cloud plan summary

- low-risk background work
- verification or hygiene tasks
- aggregation or packet-drafting preparation that does not require direct human judgment

### 3.7 Promotion review queue

- packets needing verification, approval, or application

### 3.8 Escalations and holds

- unresolved blocking conditions

## 4. Two-lane split

### 4.1 Progress and hygiene

- **Decision:** Progress and hygiene are co-equal lanes.
- **Constraint:** Progress recommendations must not hide hygiene failures that materially threaten execution quality.
- **Constraint:** Severe hygiene findings may block progress work.

### 4.2 Operator and cloud

- **Decision:** Operator plans are for interactive, ambiguity-heavy, or approval-heavy work.
- **Decision:** Cloud plans are for low-risk background execution, verification, hygiene, aggregation, and packet-preparation work.
- **Constraint:** Operator and cloud plans may derive from the same synthesis, but they must remain explicitly separated.
- **Constraint:** This protocol defines the split, not the implementation machinery.

## 5. Validation and handoff boundaries

- **Rule:** A Night Plan is valid only when cycle header, input summary, progress lane, hygiene lane, operator plan, and cloud plan are present.
- **Rule:** Promotion review queue must be present when open packets exist. Escalations and holds must be present when blocking conditions exist.
- **Constraint:** The source window must remain bounded and legible.
- **Constraint:** Night may recommend `OpState` changes, but those remain recommendations until another governing rule applies them.
- **Constraint:** Missing critical session trace requires an explicit hygiene finding and either degraded mode or a hold for the affected planning output.
- **Constraint:** Night may not bury structural problems inside general planning prose or silently resolve authority questions.
- **Decision:** If a cycle is skipped, the system should record degraded mode rather than pretend continuity exists.

## 6. Compatibility notes

- **Decision:** Legacy end-of-day plans or orchestration summaries may be mapped to Night Plan during transition when lane separation, bounded input summary, and truth/state separation remain explicit.
- **Constraint:** A legacy planning artifact that mixes truth mutation, execution state, and unresolved research without boundary clarity is not a valid Night Plan.
- **Decision:** The protocol can exist before every project has concrete Night artifacts.
- **Decision:** `HEARTBEAT.md` stays lightweight and routes planning needs here rather than absorbing them.
