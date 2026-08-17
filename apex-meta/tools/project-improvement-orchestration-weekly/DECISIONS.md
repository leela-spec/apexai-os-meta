# Durable Decisions

## D001 — Production Weekly Orchestrator remains the canonical runtime control plane

**Status:** locked

**Decision:** Do not create a second permanent runtime orchestrator. The improvement project's Master Orchestrator repairs and verifies the existing production Weekly Orchestrator.

**Rationale:** A second control plane would duplicate lifecycle/authority knowledge and increase drift risk.

**Scope:** whole project

**Source:** operator, 2026-08-17

---

## D002 — Create a durable project-improvement coordination home

**Status:** locked

**Decision:** Maintain this folder as the token/context-resilient home for the redesign project so the Master can recover orientation across long/fresh chats.

**Rationale:** Conversational context alone is too fragile for a multi-module architecture repair.

**Scope:** improvement process only

**Source:** operator, 2026-08-17

---

## D003 — Repair global orchestration before detailed output modules

**Status:** locked

**Decision:** Module 00 audits and repairs the whole Weekly Orchestration lifecycle first. Detailed output modules follow bounded handovers.

**Rationale:** Current evidence indicates the central loop itself contains stale or over-specified assumptions; module-only fixes would inherit them.

**Scope:** module sequence

**Source:** operator + repository review, 2026-08-17

---

## D004 — Master verifies every module against the whole infrastructure

**Status:** locked

**Decision:** Completed module work returns to the Master. The Master independently inspects actual production changes and verifies cross-system compatibility before testing.

**Scope:** every module

**Source:** operator, 2026-08-17

---

## D005 — Integrate first, then test fresh

**Status:** locked

**Decision:** Module design is integrated into actual production skill/agent/template files before testing. Testing then occurs in a fresh context against existing W34/example data.

**Rationale:** Isolated mock examples do not prove the production path is encoded correctly; same-chat testing can benefit from hidden design context.

**Scope:** every module

**Source:** operator, 2026-08-17

---

## D006 — Repeatability means bounded AI judgment, not identical prose

**Status:** locked

**Decision:** Process, ownership, inputs, transactions, persistence and gates should be contract-bound/repeatable. AI judgment remains valid for planning, synthesis, prioritization, prompt generation and interpretation where the task is inherently semantic.

**Scope:** architecture

**Source:** operator, 2026-08-17

---

## D007 — Preserve superseded architecture in history/archive

**Status:** locked

**Decision:** When active architecture is replaced, move obsolete material to an explicit archive/history location instead of deleting it outright or leaving it active beside the replacement.

**Rationale:** Prior designs can later prove useful, but active ambiguity must be removed.

**Scope:** repository maintenance

**Source:** operator, 2026-08-17

---

## D008 — Human-facing output design already recovered is starting design authority

**Status:** locked unless operator changes it during module design

**Decision:** Human-first, result-card-first, progressive disclosure, minimum machine payload, no duplicate surfaces, readable flow cards and real prompt files are established starting intent. The project should wire/refine them, not rediscover them from zero.

**Scope:** output modules

**Source:** recovered operator-verified design + operator confirmation, 2026-08-17

---

## D009 — No presumption that Sync, ProjectStatus, gates or universal envelopes are necessary

**Status:** locked as evaluation rule

**Decision:** These components may remain only when Module 00 demonstrates concrete current value and a named consumer. Existing presence is not sufficient justification.

**Scope:** orchestration spine

**Source:** operator review, 2026-08-17

---

## D010 — Research skill/agent composition before changing topology

**Status:** locked process rule

**Decision:** Module 00 must run `00-orchestration-spine/01-ARCHITECTURE-RESEARCH-PROMPT.md` before reorganizing or retaining the current skill/agent topology by assumption.

**Rationale:** Claude Code natively supports both Skills and Subagents, but native support does not prove that each current wrapper agent creates enough value to justify its context/instruction layer. The architecture must be selected from actual APEX requirements and current official Claude behavior.

**Scope:** orchestration spine architecture

**Source:** operator feedback + architecture review, 2026-08-17

---

## D011 — Runtime activation requires entrypoint/contract behavior, not template presence

**Status:** locked evaluation rule

**Decision:** A promoted template is not considered integrated until the active production entrypoint and runtime path require/use the intended behavior and a fresh invocation can produce it without design-chat memory.

**Rationale:** Previous activation validation reported promoted templates and passing fixtures while changing zero contracts, zero entrypoints and zero runtime behavior; current stage skills still encode the stale schema-first path.

**Scope:** all output modules

**Source:** repository evidence + operator direction, 2026-08-17

---

## Open architecture question O001 — Skill/agent physical organization

**Status:** unresolved; Module 00 architecture research

Current official Claude Code architecture treats Skills and Subagents as distinct composable primitives: Skills provide reusable instructions/workflows; Subagents provide isolated workers with separate context and may preload Skills. The unresolved APEX question is **not** whether this composition is supported, but whether each current custom weekly stage agent delivers enough isolation, permissions, model specialization, parallelism or reusable worker value to justify the extra layer.

Resolve O001 using `00-orchestration-spine/01-ARCHITECTURE-RESEARCH-PROMPT.md`, then record the accepted topology here before production restructuring.
