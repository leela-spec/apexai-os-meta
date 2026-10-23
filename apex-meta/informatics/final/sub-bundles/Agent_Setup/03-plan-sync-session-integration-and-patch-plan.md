---
type: integration-patch-plan
status: decision_ready_not_applied
created: 2026-09-03
---

# Plan-Sync-Session Integration and Patch Plan

## 1. Integration principle

The shared working method defines **how work is understood, decomposed, realized, verified and validated**.

Plan-Sync-Session continues to define **who owns planning proposals, deterministic computation, and confirmed mutation/closure**.

These are complementary layers, not competing orchestration systems.

## 2. Ownership map

| Method responsibility | Existing Apex owner | Required change |
|---|---|---|
| task classification / route selection | compact agent router + shared method | add thin shared method route, no new state |
| project/epic/task decomposition proposal | `apex-plan` | enrich semantics with established specification/architecture/work-package vocabulary |
| qualitative dependencies / acceptance | `apex-plan` | preserve existing owner |
| exact dependency computation / ranking / blocker checks | `apex-sync` | no ownership change |
| implementation execution | selected runtime/agent/workflow | method governs bounded realization, not Plan-Sync-Session |
| verification evidence | selected implementation/test process | reference from handoff/session artifacts |
| final validation against intended outcome | shared method + operator/project acceptance | record result through existing artifacts, no new status machine |
| consequential mutation | `apex-session` | no ownership change |
| registry write | explicit `apex-sync` write path | no ownership change |
| session/handoff/closure | `apex-session` | reuse existing handoff output |
| orchestration-system activation | `.claude/CLAUDE.md` | unchanged: explicit operator intent only |

## 3. Mapping the lifecycle onto Apex

```text
USER / OPERATOR REQUEST
        │
        ▼
route task complexity
        │
        ├─ Direct ───────────────────────────► execute + verify result
        │
        └─ Structured
              │
              ▼
       execution preflight
              │
              ▼
     specification / architecture /
       work-package decomposition
              │
              ├────────► apex-plan when durable project/task planning is requested
              │
              ▼
       cross-artifact consistency
              │
              ├────────► apex-sync for deterministic graph/ranking/drift computation
              │
              ▼
        bounded implementation
              │
              ▼
        unit verification
              │
              ▼
      integration verification
              │
              ▼
      outcome validation
              │
              ├─ gaps ► update appropriate spec/plan/task and converge
              │
              ▼
       confirmed mutation / closure
              │
              └────────► apex-session
```

## 4. Important non-changes

Do **not** create:

- `apex-method-state.yaml`;
- a second registry;
- a separate task status enum;
- a new permission/authorization system;
- a new always-on orchestration system;
- a universal mandatory `TASK-BRIEF.md`;
- Macro/Meso/Micro fields on every task record;
- an automatic subagent hierarchy;
- a numeric complexity score persisted in project state.

## 5. Proposed implementation targets after operator approval

### Patch group P1 — shared method entrypoint

Create one shared working-method package or Informatics method entrypoint.

Candidate location:

```text
.claude/skills/apex-working-method/
  SKILL.md
  references/
  evals/
```

Alternative if a Skill is judged too auto-trigger-prone under current Apex rules:

```text
apex-meta/informatics/Agent_Setup/working-method/
  method.md
  references/
  evals/
```

Decision criterion: use a Skill only if activation can remain explicit/on-demand and compatible with current `.claude/CLAUDE.md` rule that no skill auto-triggers without operator intent. Otherwise keep it as a referenced method file consumed by active entrypoints.

### Patch group P2 — tiny global routing sentence

Target: `AGENTS.md` and/or `.claude/CLAUDE.md`.

Goal: add only the minimal Route 0 vs structured-work invariant. Do not duplicate method details.

Recommended candidate text is Candidate A from `02-preflight-and-progressive-disclosure-design.md`.

### Patch group P3 — apex-plan semantic alignment

Target: `.claude/skills/apex-plan/SKILL.md` and relevant existing references.

Do not replace its ownership boundaries.

Potential changes:

- project capture explicitly includes intended outcome/success/system boundary where applicable;
- decomposition terminology references specification/architecture/work package/task and traceability;
- acceptance criteria and definition of done are connected to later verification;
- parent-child decomposition follows a completeness rule analogous to WBS 100% accounting;
- unresolved derived requirements/constraints are reconciled before deeper decomposition;
- route to shared method reference rather than copy lifecycle prose.

### Patch group P4 — apex-session validation/closure alignment

Target: `.claude/skills/apex-session/SKILL.md` and handoff reference files.

Potential changes:

- distinguish `verification evidence` from `outcome validation` in handoff/findings fields where useful;
- closure should not infer system validation merely because task status becomes `done`;
- preserve current confirmation gate and mutation ownership exactly;
- reference shared method instead of duplicating hierarchy/V&V semantics.

### Patch group P5 — agent references

Audit `.claude/agents/*.md` for duplicated planning/execution lifecycle prose.

Patch only where duplication exists:

- add reference to shared method;
- retain domain-specific role/tool/evidence constraints;
- do not convert specialist agents into permanent project managers.

### Patch group P6 — terminology collision cleanup

Revisit:

`apex-meta/SmallSkills/OKF_Format/adoption-project/post-w2-verification/PATCH-04-terminology-and-ambiguity.md`

The general method decision means:

- historical Weekly Macro/Meso labels should not become authority for general realization semantics;
- operator-facing Macro/Meso/Micro may remain documented as aliases;
- machine-facing current-truth instructions should prefer system intent / architecture / work package / verification / validation;
- do not mechanically rename historical evidence merely to make terminology uniform.

## 6. Patch ordering

```text
D1-D5 operator decision
   ↓
P1 shared method surface
   ↓
P2 minimal router
   ↓
P3 apex-plan reference/alignment
   ↓
P4 apex-session verification/validation alignment
   ↓
P5 specialist-agent deduplication
   ↓
P6 terminology collision cleanup
   ↓
run simulation/evaluation suite
   ↓
small real-world pilot
   ↓
only then broaden adoption
```

Do not patch all live files in one uncontrolled change. Each group should have its own target-specific evaluation.

## 7. Acceptance criteria for implementation

The implementation is acceptable only if all are true:

1. A simple bounded Git/file task still takes the direct path and does not emit a planning artifact.
2. A nontrivial request exposes a compact applied preflight rather than generic methodology prose.
3. A complex project produces traceable parent/child decomposition and explicit acceptance conditions.
4. A very large target can be split into bounded slices without loading the full project into every worker context.
5. Verification and validation are distinguishable in generated handoff/closure reasoning.
6. No new operator confirmation is introduced merely because a preflight occurred.
7. Existing Plan-Sync-Session mutation boundaries still hold.
8. Weekly Orchestrator and Multi-Agent Orchestration remain opt-in and independent.
9. Specialist agents do not duplicate the general lifecycle.
10. The always-loaded instruction delta remains very small.

## 8. Risks and controls

| Risk | Control |
|---|---|
| Spec Kit cosplay: copying commands/files without their runtime | reuse concepts/vocabulary only unless actual installation is separately justified |
| process ceremony on trivial tasks | Route 0 directness test is mandatory |
| new method silently becomes new state system | prohibit IDs/statuses/registry ownership in shared method |
| preflight becomes another approval gate | explicit `PREVIEW_NOT_APPROVAL` decision |
| V&V becomes generic self-review prose | require concrete acceptance/spec evidence for verification and explicit intended-outcome question for validation |
| recursive decomposition used too early | only Route 3 after bounded Route 2 cannot fit/manage context |
| specialist agents drift | reference shared method; domain additions only |
| token bloat | progressive disclosure + eval on always-loaded word count |

## 9. Recommended first pilot after implementation

Use three deliberately different tasks:

1. **Direct:** push/move a known file with no ambiguity.
2. **Compact:** modify 3–5 related repository files to implement one explicit bounded feature.
3. **Full/recursive candidate:** design and realize a cross-module capability with multiple dependencies and an explicit operator outcome.

The method should select different routes without operator prompting and should demonstrate that added structure tracks actual task characteristics rather than superficial length.
