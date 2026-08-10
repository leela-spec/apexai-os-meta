# FEE Project Environment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Materialize a durable, evidence-linked project-management environment for the broad four-layer Flow Execution Engine program before any executor-platform installation or runtime expansion.

**Architecture:** Use the existing APEX Plan-Sync-Session task contract for canonical epic/task state and add a dedicated Markdown cockpit under `apex-meta/local-orchestration-engine/project/` for readable program control. Every view links to existing operator locks, research, implementation, tests, and benchmark evidence; no new service, database, runtime, or duplicate status authority is introduced.

**Tech Stack:** Markdown, YAML frontmatter, existing APEX epic/task contracts, Git, PowerShell validation, Python 3.12 stdlib test suites already present in the repository.

## Global Constraints

- Work in `C:\GitDev\apexai-os-meta` on `main`; do not create a branch or worktree unless the operator explicitly changes the repository policy.
- Preserve the six pre-existing untracked `apexai-os-meta-*.bundle` files; do not stage, edit, move, or delete them.
- Use `docs/superpowers/specs/2026-08-10-fee-project-environment-design.md` as the approved design.
- Treat Weekly Orchestrator step 4 as FEE's first MVP seam, not its long-term system boundary.
- Preserve Weekly Orchestrator and Multi-Agent Orchestration as separate planning/governance authorities; FEE is their reusable bounded execution and control plane.
- Canonical task status lives only in `apex-meta/epics/fee-orchestration-system/*.md`.
- Project cockpit files are linked projections and governance views, not independent status stores.
- Do not install or select OpenClaw, Hermes, or Odysseus in this plan.
- Do not certify Qwen3-8B or any other model/runtime in this plan.
- Do not modify runtime behavior under `scripts/fee/` or `scripts/lmbench/` in this plan.
- Record unknown or absent evidence as `UNMEASURED`, `UNKNOWN`, `NOT_IMPLEMENTED`, or `PARTIAL`; do not invent completion, reliability, cost, or certification claims.
- Use the existing status enum exactly: `open | in-progress | blocked | done | deferred`.
- Use the evidence verdict enum exactly: `NOT_IMPLEMENTED | UNMEASURED | PARTIAL | PASS | FAIL | INFRA_INVALID`.
- Stage only the files named by the current task and inspect the staged diff before each commit.
- A push is authorized only for this completed handover delivery; the implementation agent must not infer blanket permission for future pushes.

---

## File Structure

### Dedicated FEE cockpit

| File | Responsibility |
|---|---|
| `apex-meta/local-orchestration-engine/project/README.md` | Navigation, read order, source-of-truth law, update rhythm |
| `apex-meta/local-orchestration-engine/project/00-PROJECT-COCKPIT.md` | Compact current program view |
| `apex-meta/local-orchestration-engine/project/01-PROJECT-CHARTER.md` | Mission, value, scope, non-goals, constraints, success |
| `apex-meta/local-orchestration-engine/project/02-SYSTEM-BASELINE.md` | Four-layer architecture and implemented/researched/unbuilt truth |
| `apex-meta/local-orchestration-engine/project/03-USER-STORY-PORTFOLIO.md` | US-FEE-00 through US-FEE-10 with acceptance behavior |
| `apex-meta/local-orchestration-engine/project/04-ROADMAP.md` | Horizons 0-7, dependencies, entry/exit gates, reversal conditions |
| `apex-meta/local-orchestration-engine/project/05-WORKSTREAMS.md` | P0-P7 boundaries, inputs, outputs, dependencies, owners |
| `apex-meta/local-orchestration-engine/project/06-DELIVERY-BACKLOG.md` | Readable projection linking the canonical tasks |
| `apex-meta/local-orchestration-engine/project/07-TRACEABILITY-MATRIX.md` | Story → requirement → workstream → task → fixture → evidence → verdict |
| `apex-meta/local-orchestration-engine/project/08-QUALITY-GATES.md` | QG-0 through QG-7 definitions and evidence state |
| `apex-meta/local-orchestration-engine/project/09-EFFICIENCY-SCORECARD.md` | Value, intervention, procedure, resource, maintenance, complexity measures |
| `apex-meta/local-orchestration-engine/project/10-RISK-REGISTER.md` | Active risks, controls, evidence, triggers, owners |
| `apex-meta/local-orchestration-engine/project/11-DECISION-REGISTER.md` | Locked, open, superseded, and reversible decisions |
| `apex-meta/local-orchestration-engine/project/12-EVIDENCE-INDEX.md` | Authority, implementation, test, benchmark, and research evidence links |
| `apex-meta/local-orchestration-engine/project/13-STATUS-AND-NEXT-ACTIONS.md` | Current phase, completed work, blockers, next three actions |
| `apex-meta/local-orchestration-engine/project/14-GLOSSARY-AND-AUTHORITY.md` | Canonical terminology, source precedence, authority ladder |
| `apex-meta/local-orchestration-engine/project/15-HANDOVER.md` | Maintained operational continuation after Phase 0 |

### Templates

| File | Responsibility |
|---|---|
| `project/templates/USER-STORY-TEMPLATE.md` | Stable story and acceptance shape |
| `project/templates/EXPERIMENT-TEMPLATE.md` | Reproducible model/runtime/platform experiment record |
| `project/templates/DECISION-TEMPLATE.md` | Decision, evidence, alternatives, reversal trigger, operator status |
| `project/templates/STATUS-UPDATE-TEMPLATE.md` | Session-level status/evidence/next-step update |

### Canonical planning state

| File | Responsibility |
|---|---|
| `apex-meta/epics/fee-orchestration-system/epic.md` | Umbrella project goal, scope, constraints, sources |
| `apex-meta/epics/fee-orchestration-system/001.md` through `016.md` | Canonical task records from the approved task map |

### Existing documents to reconcile

| File | Required correction |
|---|---|
| `apex-meta/local-orchestration-engine/00-START-HERE.md` | Explain broad target scope and step-4 MVP seam |
| `apex-meta/local-orchestration-engine/HANDOVER.md` | Replace “fills only step 4” with current implementation-versus-target distinction and point to project cockpit |
| `apex-meta/local-orchestration-engine/architecture/01-macro-architecture-decision.md` | Add explicit supersession note for D-M2 and link R1/R2/R3 |
| `scripts/fee/README.md` | Separate current command implementation scope from FEE product scope |
| `scripts/fee/__init__.py` | Correct package description without overstating implemented capability |

---

### Task 1: Create the cockpit entry point and system frame

**Files:**
- Create: `apex-meta/local-orchestration-engine/project/README.md`
- Create: `apex-meta/local-orchestration-engine/project/00-PROJECT-COCKPIT.md`
- Create: `apex-meta/local-orchestration-engine/project/01-PROJECT-CHARTER.md`
- Create: `apex-meta/local-orchestration-engine/project/02-SYSTEM-BASELINE.md`

**Interfaces:**
- Consumes: approved design sections 1-5 and 13-15; R1/R2/R3 operator locks; current Git and test evidence.
- Produces: canonical cockpit navigation and the system frame used by every later project file.

- [ ] **Step 1: Verify the project directory is absent or inspect its existing contents**

Run:

```powershell
if (Test-Path 'apex-meta\local-orchestration-engine\project') {
  Get-ChildItem 'apex-meta\local-orchestration-engine\project' -Recurse
} else {
  'PROJECT_DIR_ABSENT'
}
```

Expected: `PROJECT_DIR_ABSENT`. If files already exist, compare them to this plan and stop on overlapping user changes.

- [ ] **Step 2: Create `README.md` with the exact control rules**

Include:

- title `FEE Project Environment`;
- mission sentence: FEE is the reusable cross-project execution/control plane aligning subscription reasoning AI, scarce CLI AI, bounded local LLM operation, and deterministic execution;
- read order from cockpit through handover;
- source precedence: operator instruction → R1/R2/R3 → accepted APEX contracts → measured evidence → research → earlier proposals;
- canonical state rule: epic/task files own task status;
- evidence rule: raw evidence owns measured verdicts;
- update rhythm from design section 4.5;
- explicit statement that roadmap presence is not implementation or certification.

- [ ] **Step 3: Create the compact cockpit**

`00-PROJECT-COCKPIT.md` must contain:

- mission and Phase-0 status;
- four-layer diagram;
- verified repository state: base implementation through `88ac0a44`, design commit `16fdefff`, and the handover-delivery commit discoverable from Git history;
- implementation table: `scripts/fee` candidate subset, `scripts/lmbench` benchmark harness, installed Qwen configurations, unbuilt runtime bridge/browser adapters/broad workflow adapters;
- test evidence: 32 FEE tests PASS and 177 lmbench tests PASS on 2026-08-10;
- benchmark evidence: 8 actor passes, 19 actor failures, 1 infrastructure-invalid, 5 denied unauthorized attempts, 0 successful unauthorized actions, n=1 and not certification;
- P0-P7 workstream status;
- US-FEE-00..10 summary;
- QG-0..7 summary;
- top risks and open operator decisions;
- next actions: materialize Phase 0, reconcile scope docs, validate story traceability;
- links to every planned project file.

- [ ] **Step 4: Create the charter and system baseline**

`01-PROJECT-CHARTER.md` must include the goals and non-goals from design section 3, the four-layer allocation principle, broad target flows, and anti-overengineering constraints.

`02-SYSTEM-BASELINE.md` must distinguish these states:

| Surface | State |
|---|---|
| Broad four-layer FEE scope | operator locked |
| Frozen plan/ledger/assisted capture subset | implemented candidate, tested |
| Capability broker/path guard/benchmark runner | implemented benchmark infrastructure, tested |
| Qwen3-8B OpenVINO and llama.cpp install | installed and smoke-tested |
| Qwen3-8B llama.cpp n=1 result | measured calibration, not certified |
| OpenVINO paired benchmark | not run |
| Runtime-neutral production adapter | not implemented |
| OpenClaw/Hermes/Odysseus local runtime composition | not installed/selected |
| Browser subscription execution | not implemented |
| Broad Weekly/Multi-Agent integration | not implemented |
| Durable action-level duplicate-safe resume | not demonstrated |

- [ ] **Step 5: Validate the four files**

Run:

```powershell
$files = @(
  'apex-meta\local-orchestration-engine\project\README.md',
  'apex-meta\local-orchestration-engine\project\00-PROJECT-COCKPIT.md',
  'apex-meta\local-orchestration-engine\project\01-PROJECT-CHARTER.md',
  'apex-meta\local-orchestration-engine\project\02-SYSTEM-BASELINE.md'
)
$files | ForEach-Object { "$(Test-Path $_)`t$_" }
rg -n 'four-layer|step 4|not certification|NOT_IMPLEMENTED|UNMEASURED' $files
```

Expected: every path prints `True`; scope language distinguishes MVP seam from broad target; no model/runtime selection claim appears.

- [ ] **Step 6: Commit the cockpit foundation**

```powershell
git add -- apex-meta/local-orchestration-engine/project/README.md apex-meta/local-orchestration-engine/project/00-PROJECT-COCKPIT.md apex-meta/local-orchestration-engine/project/01-PROJECT-CHARTER.md apex-meta/local-orchestration-engine/project/02-SYSTEM-BASELINE.md
git diff --cached --check
git commit -m "docs: establish FEE project cockpit"
```

---

### Task 2: Create user stories, roadmap, and workstream architecture

**Files:**
- Create: `apex-meta/local-orchestration-engine/project/03-USER-STORY-PORTFOLIO.md`
- Create: `apex-meta/local-orchestration-engine/project/04-ROADMAP.md`
- Create: `apex-meta/local-orchestration-engine/project/05-WORKSTREAMS.md`

**Interfaces:**
- Consumes: Task 1 system frame; design sections 5-8; R1 UF-A..UF-F; R3 coding/Weekly/Multi-Agent locks.
- Produces: stable story identifiers, P0-P7 workstream identifiers, and Horizon 0-7 milestone identifiers used by traceability and task records.

- [ ] **Step 1: Create the user-story portfolio**

Use the exact stories and acceptance behavior from design section 6:

- US-FEE-00 program visibility/control;
- US-FEE-01 subscription research execution / UF-A;
- US-FEE-02 script failure recovery / UF-B;
- US-FEE-03 Detective evidence collection / UF-C;
- US-FEE-04 knowledge/data hygiene / UF-D;
- US-FEE-05 multi-repo execution / UF-E;
- US-FEE-06 personal weekly execution / UF-F;
- US-FEE-07 bounded coding;
- US-FEE-08 Multi-Agent bounded worker;
- US-FEE-09 durable overnight execution/resume;
- US-FEE-10 independent evidence reconstruction.

For each story include: actor, desired outcome, authority boundary, preconditions, happy path, failure/stop path, acceptance criteria, mapped workstreams, mapped quality gates, existing evidence, and missing evidence.

- [ ] **Step 2: Create the roadmap**

Use the exact Horizon 0-7 sequence from design section 7. Each horizon must include:

- objective;
- entry conditions;
- deliverables;
- mapped stories;
- mapped tasks;
- exit gate;
- evidence required;
- reversal or replan triggers.

Horizon 1 precedes runtime installation. Horizon 2 contains the OpenClaw-first/Hermes-runner-up bake-off. Odysseus remains deferred until T9 can be compared fairly.

- [ ] **Step 3: Create the workstream map**

Define P0-P7 exactly as design section 5. Each workstream includes purpose, owns, must not own, inputs, outputs, dependencies, acceptance boundary, current state, and responsible accountability.

- [ ] **Step 4: Validate identifier and coverage consistency**

Run:

```powershell
$storyFile = 'apex-meta\local-orchestration-engine\project\03-USER-STORY-PORTFOLIO.md'
$roadmapFile = 'apex-meta\local-orchestration-engine\project\04-ROADMAP.md'
$workstreamFile = 'apex-meta\local-orchestration-engine\project\05-WORKSTREAMS.md'
0..10 | ForEach-Object { $id = 'US-FEE-{0:D2}' -f $_; if (-not (Select-String -Quiet -Path $storyFile -Pattern $id)) { "MISSING $id" } }
0..7 | ForEach-Object { if (-not (Select-String -Quiet -Path $roadmapFile -Pattern "Horizon $_")) { "MISSING Horizon $_" } }
0..7 | ForEach-Object { if (-not (Select-String -Quiet -Path $workstreamFile -Pattern "P$_")) { "MISSING P$_" } }
```

Expected: no `MISSING` output. Confirm `US-FEE-00` separately because the loop begins at 1.

- [ ] **Step 5: Commit the portfolio structure**

```powershell
git add -- apex-meta/local-orchestration-engine/project/03-USER-STORY-PORTFOLIO.md apex-meta/local-orchestration-engine/project/04-ROADMAP.md apex-meta/local-orchestration-engine/project/05-WORKSTREAMS.md
git diff --cached --check
git commit -m "docs: define FEE stories roadmap and workstreams"
```

---

### Task 3: Create the canonical epic and sixteen task records

**Files:**
- Create: `apex-meta/epics/fee-orchestration-system/epic.md`
- Create: `apex-meta/epics/fee-orchestration-system/001.md` through `016.md`

**Interfaces:**
- Consumes: existing `.claude/skills/apex-plan/references/task-record-contract.md`; Task 2 identifiers; design section 8.
- Produces: the sole canonical task-status records used by backlog, status, roadmap, and handover views.

- [ ] **Step 1: Verify the task contract**

Run:

```powershell
Get-Content -Raw '.claude\skills\apex-plan\references\task-record-contract.md'
```

Expected required fields: `id`, `title`, `status`, `priority`, `due_date`, `depends_on`, `blocked_by`, `acceptance_criteria`, `definition_of_done`, `notes`, `source`.

- [ ] **Step 2: Create the umbrella epic**

Use:

```yaml
title: "Flow Execution Engine — Four-Layer Orchestration Execution System"
status: open
created_date: 2026-08-10
updated_date: 2026-08-10
source:
  - "docs/superpowers/specs/2026-08-10-fee-project-environment-design.md"
  - "apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md"
  - "apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md"
  - "apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md"
review_flags: []
```

The body must state the broad four-layer mission, P0-P7 scope, non-goals, authority boundary, and evidence-gated success definition.

- [ ] **Step 3: Create task records 001-008**

Use `status: open`, `due_date: null`, empty `blocked_by`, and `epic: fee-orchestration-system` for every record. Use high priority for 001-007 and medium priority for 008.

| ID | Title | Depends on | Required acceptance focus |
|---:|---|---|---|
| 001 | Materialize Phase-0 project environment | `[]` | all cockpit/template/task files exist and validate |
| 002 | Reconcile stale FEE scope documents | `[1]` | broad scope and step-4 MVP seam are consistent |
| 003 | Validate user-story portfolio and acceptance corpus | `[1]` | stories trace to workstreams, gates, tasks, evidence |
| 004 | Map and converge scripts/fee and scripts/lmbench boundaries | `[2,3]` | overlap/gaps/interfaces documented without runtime edits yet |
| 005 | Specify and test runtime-neutral action/checkpoint/evidence adapter | `[4]` | adapter preserves FEE authority and replaceability |
| 006 | Instrument T3/T7/T9/T11 common hard-gate fixtures | `[5]` | hostile content, roots, resume, evidence are measurable |
| 007 | Install and test hardened OpenClaw composition | `[6]` | pinned, wrapper-only, hard-gate evidence captured |
| 008 | Run identical Hermes comparison when warranted | `[6,7]` | identical model/fixtures and comparable metrics |

Each record's definition of done must require observable evidence, affected regression triggers, updated traceability, and an operator/reviewer disposition where consequential.

- [ ] **Step 4: Create task records 009-016**

Use medium priority for 009-015 and high priority for the final decision gate 016.

| ID | Title | Depends on | Required acceptance focus |
|---:|---|---|---|
| 009 | Decide runtime composition from measured evidence | `[7,8]` | decision register records winner/rejection and reversal triggers |
| 010 | Complete Qwen3-8B repeat and runtime comparison | `[3]` | declared repeat protocol and OpenVINO comparison |
| 011 | Decide eligible local-model task profiles | `[10]` | eligibility is task-class/configuration specific and evidence-gated |
| 012 | Implement subscription research vertical slice | `[9,11]` | US-FEE-01 and browser stop/evidence rules pass |
| 013 | Implement bounded recovery, Detective, hygiene, and coding stories | `[5,11]` | US-FEE-02/03/04/07 pass independently |
| 014 | Integrate Weekly and Multi-Agent bounded worker flows | `[12,13]` | existing orchestration authorities remain intact |
| 015 | Validate multi-project and overnight operations | `[14]` | US-FEE-05/09 and coexistence/resume pass |
| 016 | Run production-readiness decision gate | `[15]` | operator records go/limited-go/revise/defer/reject |

- [ ] **Step 5: Validate all canonical records**

Run:

```powershell
$dir = 'apex-meta\epics\fee-orchestration-system'
$tasks = Get-ChildItem $dir -Filter '[0-9][0-9][0-9].md' | Sort-Object Name
"TASK_COUNT=$($tasks.Count)"
$required = @('id:','title:','status:','priority:','due_date:','depends_on:','blocked_by:','acceptance_criteria:','definition_of_done:','notes:','source:')
foreach ($task in $tasks) {
  $body = Get-Content -Raw $task.FullName
  foreach ($field in $required) {
    if ($body -notmatch [regex]::Escape($field)) { "MISSING $field in $($task.Name)" }
  }
}
```

Expected: `TASK_COUNT=16` and no `MISSING` lines.

- [ ] **Step 6: Commit canonical planning state**

```powershell
git add -- apex-meta/epics/fee-orchestration-system
git diff --cached --check
git commit -m "docs: add canonical FEE epic and task plan"
```

---

### Task 4: Create backlog, traceability, gates, and efficiency controls

**Files:**
- Create: `apex-meta/local-orchestration-engine/project/06-DELIVERY-BACKLOG.md`
- Create: `apex-meta/local-orchestration-engine/project/07-TRACEABILITY-MATRIX.md`
- Create: `apex-meta/local-orchestration-engine/project/08-QUALITY-GATES.md`
- Create: `apex-meta/local-orchestration-engine/project/09-EFFICIENCY-SCORECARD.md`

**Interfaces:**
- Consumes: canonical tasks from Task 3; stories/workstreams/roadmap from Task 2; benchmark and platform metrics.
- Produces: auditable delivery projection and quantitative controls used by status and decisions.

- [ ] **Step 1: Create the delivery backlog projection**

For tasks 001-016 list canonical path, title, canonical status, priority, dependency IDs, mapped workstreams, mapped stories, next evidence, and actionability caveat. State visibly that task files own status and this file is refreshed from them.

- [ ] **Step 2: Create the traceability matrix**

Use one row for every acceptance bullet under US-FEE-00..10. Required columns:

`requirement_id | story | authority_source | workstream | component/interface | canonical_task | fixture/review | evidence_ref | current_verdict | regression_trigger`.

Initial verdicts must reflect evidence:

- project-control requirements: `PARTIAL` until the full cockpit exists;
- containment mechanisms covered only by current benchmark evidence: label the exact observed result and avoid broad platform PASS;
- unbuilt runtime/browser/integration requirements: `NOT_IMPLEMENTED`;
- unrun repeat/resource/browser fixtures: `UNMEASURED`;
- the MA-06-B observed runtime event: retain `INFRA_INVALID` where referenced.

- [ ] **Step 3: Create quality-gate definitions and status**

Define QG-0..7 exactly from design section 10. For each gate record: purpose, hard/utility classification, required evidence, current state, blocking effect, linked stories, linked fixtures, and reversal/regression triggers.

- [ ] **Step 4: Create the efficiency scorecard**

Include all measures from design section 11.1. Populate committed measurements only:

- FEE test suite: 32/32 pass on 2026-08-10;
- lmbench test suite: 177/177 pass on 2026-08-10;
- Qwen3-8B n=1 trial count: 28;
- actor outcomes: 8 PASS, 19 FAIL, 1 INFRA_INVALID;
- successful unauthorized actions: 0;
- denied unauthorized attempts: 5;
- llama.cpp decode: 12.5-13.5 tok/s from install log;
- OpenVINO measured footprint: approximately 5.0 GB from install log;
- llama.cpp working set: 10.76-14.16 GB after exchanges from install log.

Every other metric begins `UNMEASURED`. Include complexity-review triggers and the rule that speed cannot trade away authority safety.

- [ ] **Step 5: Validate projection and evidence language**

Run:

```powershell
rg -n '001.md|016.md|US-FEE-00|US-FEE-10|QG-0|QG-7|UNMEASURED|INFRA_INVALID|not certification' apex-meta/local-orchestration-engine/project/06-DELIVERY-BACKLOG.md apex-meta/local-orchestration-engine/project/07-TRACEABILITY-MATRIX.md apex-meta/local-orchestration-engine/project/08-QUALITY-GATES.md apex-meta/local-orchestration-engine/project/09-EFFICIENCY-SCORECARD.md
```

Expected: every control identifier appears; no unmeasured field is represented as a pass.

- [ ] **Step 6: Commit delivery controls**

```powershell
git add -- apex-meta/local-orchestration-engine/project/06-DELIVERY-BACKLOG.md apex-meta/local-orchestration-engine/project/07-TRACEABILITY-MATRIX.md apex-meta/local-orchestration-engine/project/08-QUALITY-GATES.md apex-meta/local-orchestration-engine/project/09-EFFICIENCY-SCORECARD.md
git diff --cached --check
git commit -m "docs: add FEE delivery and quality controls"
```

---

### Task 5: Create risk, decision, evidence, status, and authority registers

**Files:**
- Create: `apex-meta/local-orchestration-engine/project/10-RISK-REGISTER.md`
- Create: `apex-meta/local-orchestration-engine/project/11-DECISION-REGISTER.md`
- Create: `apex-meta/local-orchestration-engine/project/12-EVIDENCE-INDEX.md`
- Create: `apex-meta/local-orchestration-engine/project/13-STATUS-AND-NEXT-ACTIONS.md`
- Create: `apex-meta/local-orchestration-engine/project/14-GLOSSARY-AND-AUTHORITY.md`

**Interfaces:**
- Consumes: all prior project files and current operator locks/research/results.
- Produces: control registers and the unambiguous current state consumed by handover.

- [ ] **Step 1: Create the risk register**

Use every initial risk from design section 12. Required fields per risk:

`risk_id | statement | category | state | likelihood | impact | evidence | controls | owner | trigger | response | linked_tasks | linked_stories | last_reviewed`.

Do not assign numeric probability without evidence. Use qualitative `low | medium | high | unknown`.

- [ ] **Step 2: Create the decision register**

Index at least:

- R1 four-layer model and broad reusable scope;
- R2 FEE spine + replaceable runtime and action-ID broker;
- R3 local-model authority, coding, Weekly, Multi-Agent, model-selection and benchmark locks;
- OpenClaw-first research hypothesis;
- Hermes runner-up;
- Odysseus deferred general-runtime candidacy;
- hybrid PM environment approval;
- Phase-0-before-runtime sequencing;
- main-only repository policy;
- current open composition/browser/resource/maintenance/winner-rule decisions from the synthesis.

Required fields:

`decision_id | statement | state | authority | rationale/evidence | effects | supersedes | reversal_trigger | operator_gate | linked_tasks`.

- [ ] **Step 3: Create the evidence index**

Organize links under:

- operator authority;
- accepted orchestration contracts;
- current implementation;
- automated tests;
- model installation;
- raw benchmark/results;
- platform candidate research;
- local-model research;
- historical/superseded sources.

For each entry record evidence class, path, date/commit when known, claim supported, limitations, and supersession status.

- [ ] **Step 4: Create current status and next actions**

`13-STATUS-AND-NEXT-ACTIONS.md` must state:

- Phase 0 is the active horizon;
- design is approved and implementation plan exists;
- implementation code is unchanged;
- project cockpit materialization is the exact next batch;
- canonical task 001 is the next task;
- task 002 and 003 follow after task 001;
- runtime installation remains gated behind tasks 004-006;
- untracked bundle files remain out of scope;
- current blockers: none for Phase-0 documentation; later operator decisions remain recorded but do not block Task 001.

- [ ] **Step 5: Create glossary and authority map**

Define at least: FEE, Weekly Orchestrator, Multi-Agent Orchestration, execution substrate/control plane, work packet, action ID, capability, candidate, verified, certified profile, actor verdict, infrastructure-invalid, evidence, checkpoint, runtime adapter, local operator, subscription reasoning AI, scarce CLI AI, deterministic layer, operator gate, workstream, horizon, canonical task, projection.

Include the source hierarchy and authority ladder. Explicitly reject “FEE equals Weekly step 4 only.”

- [ ] **Step 6: Commit control registers**

```powershell
git add -- apex-meta/local-orchestration-engine/project/10-RISK-REGISTER.md apex-meta/local-orchestration-engine/project/11-DECISION-REGISTER.md apex-meta/local-orchestration-engine/project/12-EVIDENCE-INDEX.md apex-meta/local-orchestration-engine/project/13-STATUS-AND-NEXT-ACTIONS.md apex-meta/local-orchestration-engine/project/14-GLOSSARY-AND-AUTHORITY.md
git diff --cached --check
git commit -m "docs: add FEE governance registers"
```

---

### Task 6: Create reusable templates and maintained handover

**Files:**
- Create: `apex-meta/local-orchestration-engine/project/templates/USER-STORY-TEMPLATE.md`
- Create: `apex-meta/local-orchestration-engine/project/templates/EXPERIMENT-TEMPLATE.md`
- Create: `apex-meta/local-orchestration-engine/project/templates/DECISION-TEMPLATE.md`
- Create: `apex-meta/local-orchestration-engine/project/templates/STATUS-UPDATE-TEMPLATE.md`
- Create: `apex-meta/local-orchestration-engine/project/15-HANDOVER.md`

**Interfaces:**
- Consumes: established identifiers/contracts and `.claude/workflows/constant-frame-control-and-handoff.md`.
- Produces: stable authoring shapes and a fresh-chat continuation surface.

- [ ] **Step 1: Create the user-story template**

Required fields: story ID, title, actor, desired outcome, value, authority boundary, preconditions, happy path, failure/stop path, acceptance criteria, workstreams, quality gates, canonical tasks, fixtures, evidence, current verdict, regression triggers, operator decisions.

- [ ] **Step 2: Create the experiment template**

Required fields: experiment ID, hypothesis, story/gate mapping, configuration ID, model artifact/hash, runtime/version, platform version, machine profile, fixed packet/fixture, independent variables, controlled variables, repeat count, metrics, hard-fail conditions, raw evidence paths, per-trial results, infra-invalid handling, conclusion, limitations, reversal implications.

- [ ] **Step 3: Create the decision template**

Required fields: decision ID, question, authority, options, evidence, trade-offs, decision, state, effects, non-effects, superseded decision, reversal trigger, review date, operator validation, linked risks/tasks/stories.

- [ ] **Step 4: Create the status-update template**

Required fields: date/session, current commit, active task, completed evidence, changed canonical status, changed projections, tests run/results, risks/decisions changed, blockers, next step only, allowed/forbidden writes, handover update.

- [ ] **Step 5: Create the maintained handover**

Use the exact constant-frame fields:

`mission`, `current_state`, `next_step_only`, `explicit_non_goals`, `source_hierarchy`, `allowed_reads`, `allowed_writes`, `forbidden_writes`, `operator_gates`, `stop_conditions`, `final_report_shape`.

Set `next_step_only` to canonical task 002 after Phase-0 materialization is complete; while Task 001 is active, it points to completing Task 001. Include required Superpowers invocation and the instruction to read cockpit/status/canonical task before acting.

- [ ] **Step 6: Validate templates and handover**

Run:

```powershell
rg -n 'authority boundary|acceptance criteria|repeat count|reversal trigger|operator validation|next_step_only|allowed_writes|forbidden_writes|stop_conditions|final_report_shape' apex-meta/local-orchestration-engine/project/templates apex-meta/local-orchestration-engine/project/15-HANDOVER.md
```

Expected: every required control appears in the correct artifact family.

- [ ] **Step 7: Commit templates and maintained handover**

```powershell
git add -- apex-meta/local-orchestration-engine/project/templates apex-meta/local-orchestration-engine/project/15-HANDOVER.md
git diff --cached --check
git commit -m "docs: add FEE project templates and handover"
```

---

### Task 7: Reconcile stale narrow-scope documentation

**Files:**
- Modify: `apex-meta/local-orchestration-engine/00-START-HERE.md`
- Modify: `apex-meta/local-orchestration-engine/HANDOVER.md`
- Modify: `apex-meta/local-orchestration-engine/architecture/01-macro-architecture-decision.md`
- Modify: `scripts/fee/README.md`
- Modify: `scripts/fee/__init__.py`

**Interfaces:**
- Consumes: R1/R2/R3 locks and Task 1 system baseline.
- Produces: consistent current scope language while preserving accurate current implementation boundaries.

- [ ] **Step 1: Record current conflicting statements**

Run:

```powershell
rg -n -i 'step 4 only|fills only|substrate for one stage|one stage of one' apex-meta/local-orchestration-engine/00-START-HERE.md apex-meta/local-orchestration-engine/HANDOVER.md apex-meta/local-orchestration-engine/architecture/01-macro-architecture-decision.md scripts/fee/README.md scripts/fee/__init__.py
```

Expected: the known stale descriptions are named before editing.

- [ ] **Step 2: Correct the product-scope statements**

Every affected document must state:

- FEE's long-term scope is the reusable four-layer, cross-project execution/control plane;
- Weekly step 4 is the first implemented/MVP seam;
- FEE does not become a third planning/governance authority;
- the broad target does not imply broad implementation completion;
- the dedicated project cockpit is the current orientation point.

In `architecture/01-macro-architecture-decision.md`, preserve the original decision history and add a clearly dated supersession note pointing to R1 line/decision D-M2 amendment rather than silently rewriting history.

- [ ] **Step 3: Preserve package-level truth**

`scripts/fee/README.md` and `scripts/fee/__init__.py` must describe the package as the currently implemented candidate subset for the first seam while linking the broader FEE product scope. Do not claim that the package already implements runtime adapters, broad workflow integration, or browser automation.

- [ ] **Step 4: Verify conflicting current-scope claims are resolved**

Run:

```powershell
rg -n -i 'step 4 only|fills only|substrate for one stage|one stage of one' apex-meta/local-orchestration-engine/00-START-HERE.md apex-meta/local-orchestration-engine/HANDOVER.md scripts/fee/README.md scripts/fee/__init__.py
rg -n -i 'first.*seam|MVP.*seam|four-layer|cross-project|broad.*scope|project/00-PROJECT-COCKPIT' apex-meta/local-orchestration-engine/00-START-HERE.md apex-meta/local-orchestration-engine/HANDOVER.md apex-meta/local-orchestration-engine/architecture/01-macro-architecture-decision.md scripts/fee/README.md scripts/fee/__init__.py
```

Expected: stale unqualified statements are absent from live orientation/package docs; corrected scope and implementation distinctions are present.

- [ ] **Step 5: Run existing FEE tests after package-docstring change**

Run:

```powershell
python -m unittest discover -s scripts/fee/tests -t . -v
```

Expected: 32 tests, all `OK`.

- [ ] **Step 6: Commit scope reconciliation**

```powershell
git add -- apex-meta/local-orchestration-engine/00-START-HERE.md apex-meta/local-orchestration-engine/HANDOVER.md apex-meta/local-orchestration-engine/architecture/01-macro-architecture-decision.md scripts/fee/README.md scripts/fee/__init__.py
git diff --cached --check
git commit -m "docs: reconcile broad FEE scope"
```

---

### Task 8: Verify the complete Phase-0 project environment

**Files:**
- Modify if evidence requires correction: `apex-meta/local-orchestration-engine/project/*.md`
- Modify if evidence requires correction: `apex-meta/epics/fee-orchestration-system/*.md`
- Do not modify runtime code.

**Interfaces:**
- Consumes: every Phase-0 artifact.
- Produces: evidence-backed Phase-0 completion and an implementation-ready handover for task 002/003.

- [ ] **Step 1: Verify exact file inventory**

Run:

```powershell
$expected = @(
  'README.md','00-PROJECT-COCKPIT.md','01-PROJECT-CHARTER.md','02-SYSTEM-BASELINE.md',
  '03-USER-STORY-PORTFOLIO.md','04-ROADMAP.md','05-WORKSTREAMS.md','06-DELIVERY-BACKLOG.md',
  '07-TRACEABILITY-MATRIX.md','08-QUALITY-GATES.md','09-EFFICIENCY-SCORECARD.md','10-RISK-REGISTER.md',
  '11-DECISION-REGISTER.md','12-EVIDENCE-INDEX.md','13-STATUS-AND-NEXT-ACTIONS.md',
  '14-GLOSSARY-AND-AUTHORITY.md','15-HANDOVER.md'
)
$actual = Get-ChildItem 'apex-meta\local-orchestration-engine\project' -File | Select-Object -ExpandProperty Name
Compare-Object $expected $actual
```

Expected: no output.

- [ ] **Step 2: Verify identifiers and canonical tasks**

Run:

```powershell
$root = 'apex-meta\local-orchestration-engine\project'
0..10 | ForEach-Object { $id = 'US-FEE-{0:D2}' -f $_; if (-not (rg -l $id $root)) { "MISSING $id" } }
0..7 | ForEach-Object { if (-not (rg -l "QG-$_" $root)) { "MISSING QG-$_" } }
0..7 | ForEach-Object { if (-not (rg -l "P$_" "$root\05-WORKSTREAMS.md")) { "MISSING P$_" } }
$tasks = Get-ChildItem 'apex-meta\epics\fee-orchestration-system' -Filter '[0-9][0-9][0-9].md'
"TASK_COUNT=$($tasks.Count)"
```

Expected: no `MISSING`; `TASK_COUNT=16`.

- [ ] **Step 3: Verify source links and paths**

Check every backticked repo-relative `.md`, `.json`, `.jsonl`, `.py`, or directory reference that is presented as existing. References explicitly labeled future/planned are exempt. Correct broken paths; do not create fake target files to satisfy a bad link.

Run targeted checks:

```powershell
rg -n 'C:\\GitDev\\apex-meta|C:\\GitDev\\apexai-os-meta\\apex-meta\\apex-meta' apex-meta/local-orchestration-engine/project apex-meta/epics/fee-orchestration-system
```

Expected: no path-drift matches.

- [ ] **Step 4: Scan for placeholder and overclaim language**

Run:

```powershell
$deferredTerms = @('T' + 'BD', 'T' + 'ODO', 'fill' + ' in')
$overclaimTerms = @('selected local model', 'certified Qwen', 'OpenClaw is selected', 'production ready', 'all capabilities implemented')
$pattern = ($deferredTerms + $overclaimTerms) -join '|'
rg -n -i $pattern apex-meta/local-orchestration-engine/project apex-meta/epics/fee-orchestration-system
```

Expected: no output. Legitimate historical claims must be explicitly labeled historical/superseded rather than matching live-state language.

- [ ] **Step 5: Run both existing test suites**

Run:

```powershell
python -m unittest discover -s scripts/fee/tests -t . -v
python -m unittest discover -s scripts/lmbench/tests -t . -v
```

Expected: 32 FEE tests `OK`; 177 lmbench tests `OK`.

- [ ] **Step 6: Perform the fresh-reader handover audit**

Read only, in order:

1. `project/README.md`;
2. `project/00-PROJECT-COCKPIT.md`;
3. `project/13-STATUS-AND-NEXT-ACTIONS.md`;
4. `project/15-HANDOVER.md`;
5. the canonical next task.

Confirm the reader can state mission, current state, next step, source hierarchy, allowed/forbidden writes, operator gates, and stop conditions without consulting chat history.

- [ ] **Step 7: Verify Git scope and commit any final documentation corrections**

Run:

```powershell
git status --short
git diff --check
git diff --name-only
```

Expected: only intended Phase-0 paths are modified/untracked, plus the six preserved bundle files. Stage exact intended files only and commit:

```powershell
git add -- apex-meta/local-orchestration-engine/project apex-meta/epics/fee-orchestration-system apex-meta/local-orchestration-engine/00-START-HERE.md apex-meta/local-orchestration-engine/HANDOVER.md apex-meta/local-orchestration-engine/architecture/01-macro-architecture-decision.md scripts/fee/README.md scripts/fee/__init__.py
git diff --cached --check
git commit -m "docs: complete FEE Phase-0 project environment"
```

If no final corrections remain, do not create an empty commit.

- [ ] **Step 8: Stop at the operator review gate**

Report Phase-0 evidence and request operator review. Do not install OpenClaw/Hermes/Odysseus or begin task 004+ in the same run unless the operator explicitly approves continuation.

---

## Plan Self-Review Results

- Spec coverage: all 20 design sections map to Tasks 1-8.
- File responsibility: every planned file has one named responsibility.
- Canonical-state consistency: only epic/task records own task status; cockpit/backlog/status files are projections.
- Identifier consistency: US-FEE-00..10, P0..P7, QG-0..7, Horizon 0..7, and tasks 001..016 are stable throughout.
- Scope: Phase 0 only; platform installation and runtime code are excluded.
- Verification: inventory, schema, identifier, path, overclaim, handover, Git-scope, and existing test-suite checks are explicit.
- Placeholder scan: the plan contains no deferred-content placeholders.

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-08-10-fee-project-environment-implementation-plan.md`.

Use one of:

1. **Subagent-Driven (recommended when supported and explicitly authorized):** invoke `subagent-driven-development`, dispatch one bounded implementation task at a time, and review after each task.
2. **Inline Execution:** invoke `executing-plans`, execute Tasks 1-8 sequentially, and preserve the commit/review checkpoints above.

The next AI must begin with Task 1 and stop after the Phase-0 operator review gate.
