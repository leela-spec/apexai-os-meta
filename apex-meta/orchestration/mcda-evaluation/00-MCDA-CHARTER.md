# 00 — MCDA Charter: Master of Arts Orchestration

## 1. Decision objective

Choose the best **existing orchestration + project-management + reusable-skill/process framework** for Master of Arts so that AI agents can continuously work across heterogeneous business and knowledge tasks while the human operator remains the CEO/decider.

Target work includes, at minimum:

- website and offer development;
- workshops and training formats;
- coaching methods and session structures;
- social/content production;
- research and knowledge synthesis;
- operational/admin workflows;
- product/offer development;
- future Leela translation;
- cross-project prioritization and recurring reviews.

The selected system should support a repository-native, machine-readable operating state that survives individual chats/models and can be used by local CLI AIs and, where repository access exists, web-subscription AIs.

## 2. Decision principle

**Reuse before invention is a hard constraint, not a preference.**

The system must come from established maintained software/frameworks. We may configure, install, combine documented extension points, define project workflows, and create Master-of-Arts-specific skills/templates. We may not build a new orchestration engine, task graph store, memory layer, agent communication protocol, workflow runtime, or project-management framework merely because an AI can describe one.

If no single framework covers the target, a small composition may win, but every major layer must be an existing product/framework and the composition must be demonstrably simpler and more interoperable than adopting a larger established system.

## 3. Hard gates — fail one = cannot be production winner

| Gate | Requirement | Rationale |
|---|---|---|
| G1 Existing system | Publicly available maintained implementation exists now; not a design paper or proposed architecture. | Prevent invention masquerading as integration. |
| G2 Proven use | Meaningful adoption/usage evidence, active maintenance, documentation, examples, and issue/release history. | Prefer battle-tested behavior over novelty. |
| G3 Repo-native durable state | Project/work state can be persisted in Git/repo files or a deterministic repo-adjacent store with exportable machine-readable state. | Agents must not depend on chat memory. |
| G4 Cross-agent portability | At least the core project state/workflows are usable from more than one agent/client. A vendor-specific runtime may participate, but cannot be the only readable source of truth. | Master of Arts will use multiple AI clients. |
| G5 Human decision gates | Supports explicit approval/checkpoint semantics for consequential decisions/actions. | Operator remains CEO/decider. |
| G6 Deterministic backbone | Can use ordinary code/scripts/hooks/CI for validation, state transitions, scheduling, schema checks, and repetitive mechanics instead of spending reasoning tokens on them. | Reliability + token efficiency. |
| G7 Resumability | Interrupted work has durable task/state identity and can be resumed without reconstructing the plan from prose chat history. | Long-running portfolio work must be robust. |
| G8 Review topology | Supports maker/reviewer or equivalent independent verification rather than a single agent self-certifying everything. | Required for reliable autonomous work. |
| G9 Non-software extensibility | Can model workshops, research, content, coaching/process design, operations, etc.; not intrinsically limited to code-change tasks. | Master of Arts is a business/knowledge portfolio. |
| G10 No mandatory metered AI API for orchestration core | Core orchestration/project state must not require pay-as-you-go model API calls. Subscription/local agents may execute semantic work around it. | Fit with intended operating model and cost control. |

## 4. Weighted MCDA criteria

Candidates that pass hard gates are scored **0–5** per criterion.

| ID | Criterion | Weight | What 5/5 means |
|---|---|---:|---|
| C1 Proven maturity & ecosystem | 12 | Strong adoption, active maintenance, good docs, real examples, healthy issue/release history. |
| C2 Cross-agent / cross-client interoperability | 15 | Same durable plan/task/skill state can be consumed by Claude Code, Codex/other CLIs and web agents with repo access, without parallel duplicated truth. |
| C3 Durable project/task orchestration | 12 | Dependencies, owners/claims, status, blocking, handoffs, history and resumability are first-class and machine-readable. |
| C4 Human governance & review | 10 | Explicit gates, reviewer roles, acceptance criteria, escalation and decision authority are natural rather than bolted on. |
| C5 Skill/workflow framework quality | 10 | Reusable workflows are discoverable, composable, testable, progressively disclosed and easy for multiple agents to invoke correctly. |
| C6 Knowledge/SSOT efficiency | 10 | Clear compact canonical state, provenance, contextual retrieval/progressive disclosure, low duplication and low context-loading burden. |
| C7 Deterministic automation leverage | 8 | Hooks/scripts/CI/schedulers/state machines can own mechanical work, validation and recurring actions. |
| C8 Non-software business fit | 8 | Naturally models content, workshops, research, operations, method development and portfolio work—not only coding tickets. |
| C9 Operational simplicity & maintainability | 7 | Install/update/backup/inspect/debug are understandable; little hidden infrastructure or fragile custom glue. |
| C10 Token/context efficiency | 5 | Agents load only relevant state; durable summaries/task packets prevent repeated repo/chat rereading. |
| C11 Security & permissions | 3 | Clear execution boundaries, approval controls, least-privilege patterns and auditable actions. |

**Total weight: 100.**

### 4.1 Scoring scale

- **5 — excellent:** native/direct fit; strong evidence.
- **4 — strong:** good fit with small documented configuration.
- **3 — adequate:** works, but meaningful limitations or integration effort.
- **2 — weak:** possible but awkward/custom-heavy.
- **1 — poor:** technically possible only by fighting the framework.
- **0 — absent / disqualifying.**

Every score must carry an evidence confidence:

- **A:** official docs/repo plus direct feature evidence and/or actual pilot.
- **B:** official claims/examples but not yet tested for Master of Arts.
- **C:** credible secondary evidence/inference.
- **D:** speculation; cannot support a final selection.

No production winner may rely on a load-bearing criterion scored from D-level evidence.

## 5. Mandatory sensitivity analysis

The ranking must be recalculated under at least these weight profiles:

1. **Balanced** — weights above.
2. **Interoperability-first** — increase C2 + C6, reduce ecosystem/simplicity weights proportionally.
3. **Autonomy/reliability-first** — increase C3 + C4 + C7.
4. **Simplicity-first** — increase C9 + C10.

A winner is robust only if it remains top-tier across profiles or if the tradeoff causing ranking changes is explicitly acceptable to the operator.

## 6. Pilot-first final selection

Desk MCDA only chooses finalists. Final selection requires **real Master of Arts outputs**.

The pilot must cover at least:

- one ambiguous creative/product workflow;
- one research/knowledge workflow;
- one recurring portfolio/project-management workflow;
- one cross-agent handoff/review workflow.

The winning framework/composition must demonstrate:

- useful output, not orchestration theater;
- persistent task/project state;
- independent review;
- explicit CEO decision point;
- cross-session resume;
- deterministic validation where applicable;
- context/token discipline;
- no loss of provenance/decision history.

## 7. Stop rules

Stop evaluating or integrating a candidate when:

- it fails a hard gate;
- its key capability requires custom infrastructure that another candidate provides natively;
- two bounded attempts fail to produce a usable representative output;
- its portability requires maintaining parallel project truths for different agents;
- its orchestration overhead is larger than the work it coordinates.

## 8. Decision outputs

The MCDA is complete only when it produces:

1. evidence-backed score matrix;
2. sensitivity analysis;
3. pilot results;
4. selected framework or minimal framework composition;
5. explicit rejected alternatives and reasons;
6. exact install/configuration approach using upstream-supported mechanisms;
7. migration/rollback path;
8. machine-readable operating contract for future agents.
