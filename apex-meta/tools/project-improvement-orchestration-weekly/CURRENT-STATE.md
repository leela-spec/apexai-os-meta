# Current State

**Project phase:** Module 00 architecture integration (implementation, not research)

**Active module:** `00-orchestration-spine`

**Accepted topology (D012, O001 resolved):** one main-session `weekly-orchestrator`; six stage components (`PrecapWeek`, `PrecapNextDay`, `raw-flow-dump-normalize`, `flow-recap`, `status-merge`, `ProjectStatus`) executed as directly-dispatched Skills with isolated `context: fork`; two retained blind reviewer agents (`apex-review-validity`, `apex-review-alignment`); `apex-session` (durable mutation) and `apex-sync` (deterministic read-side) as direct backbone; `PromptEngineer`/`AIRouting`/`model-usage-log` loaded on demand only.

**Last accepted result:** O001 recorded as resolved in `DECISIONS.md` (D012). The realization plan is `00-orchestration-spine/05-TARGET-STRUCTURE-IMPLEMENTATION-PLAN.md` (filename corrected from a duplicated `.md.md` extension found on disk).

**Current architectural finding (still true, now the thing being fixed):** The repo has a real central Weekly Orchestrator, but validated operator-facing templates were previously promoted without changing owning entrypoints/contracts/runtime. Current PrecapWeek and PrecapNextDay entrypoints still encode schema-first packet behavior, and `weekly-orchestrator/SKILL.md` still hardcodes dispatch to the six wrapper agents. This is Module 00's implementation target, not an open question.

**Implementation phase order (from the target plan):**

1. Phase 1/2 — record decision (done) + fix cold-start discovery: rename `.claude/Claude.md` -> `.claude/CLAUDE.md`.
2. Phase 3 — rewrite `weekly-orchestrator/SKILL.md` routing to dispatch directly to owning Skills (`context: fork`), keeping only lifecycle/gate/persistence ownership centrally.
3. Phase 4 — convert the six owning Skills into self-contained fork workers, one at a time (PrecapWeek -> PrecapNextDay -> raw-flow-dump-normalize -> flow-recap -> status-merge -> ProjectStatus).
4. Phase 5 — switch production routing to the Skills; smoke-test before archiving anything.
5. Phase 6 — simplify `handoff-schema.md` via per-field consumer audit.
6. Phase 7 — normalize the authority/persistence map inside `weekly-orchestrator`.
7. Phase 8 — archive the six wrapper agents (only after Phase 5 smoke test passes).
8. Phase 9 — clean doctrine loading (meta-ops/meta-strategy/meta-detective/alfred doctrines).
9. Phase 10 — static topology verification (zero-reference + positive checks).
10. Phase 11 — fresh-context Module 00 integration test (Tests A-H, no design-chat rationale supplied).
11. Phase 12 — Module 00 closure; write Module 01 handover.

**Open decision:** none architectural. Remaining implementation judgment calls (e.g., exact handoff-schema field disposition) are resolved per-field using the retention test in the target plan, not re-litigated as architecture.

**Next action:** Phase B/2 — rename `.claude/Claude.md` to `.claude/CLAUDE.md` (two-step rename; NTFS is case-insensitive), verifying content stays a compact activation/routing surface only. Then proceed to Phase C/3 — rewrite `weekly-orchestrator/SKILL.md` stage routing.

**Regression fixture:** Existing W34 planning/run artifacts and recovered operator-output design.

**Original scaffold commit:** `9d2811bb7e34a45a49883d9a31774887d6d95606`
