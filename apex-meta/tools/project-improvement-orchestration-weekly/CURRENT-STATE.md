# Current State

**Project phase:** Module 00 architecture integration (implementation, not research)

**Active module:** `00-orchestration-spine`

**Accepted topology (D012, O001 resolved):** one main-session `weekly-orchestrator`; six stage components (`PrecapWeek`, `PrecapNextDay`, `raw-flow-dump-normalize`, `flow-recap`, `status-merge`, `ProjectStatus`) executed as directly-dispatched Skills with isolated `context: fork`; two retained blind reviewer agents (`apex-review-validity`, `apex-review-alignment`); `apex-session` (durable mutation) and `apex-sync` (deterministic read-side) as direct backbone; `PromptEngineer`/`AIRouting`/`model-usage-log` loaded on demand only.

**Last accepted result:** O001 recorded as resolved in `DECISIONS.md` (D012). The realization plan is `00-orchestration-spine/05-TARGET-STRUCTURE-IMPLEMENTATION-PLAN.md` (filename corrected from a duplicated `.md.md` extension found on disk).

**Current architectural finding (still true, now the thing being fixed):** The repo has a real central Weekly Orchestrator, but validated operator-facing templates were previously promoted without changing owning entrypoints/contracts/runtime. Current PrecapWeek and PrecapNextDay entrypoints still encode schema-first packet behavior, and `weekly-orchestrator/SKILL.md` still hardcodes dispatch to the six wrapper agents. This is Module 00's implementation target, not an open question.

**Implementation phase order (from the target plan):**

1. Phase 1/2 — record decision (done) + fix cold-start discovery: rename `.claude/Claude.md` -> `.claude/CLAUDE.md`. **DONE** (commits `ad95d50d`, `e24d3039`).
2. Phase 3 — rewrite `weekly-orchestrator/SKILL.md` routing to dispatch directly to owning Skills (`context: fork`), keeping only lifecycle/gate/persistence ownership centrally. **DONE** (commit `91efd902`). `stage_routing` now maps to `PrecapWeek`/`PrecapNextDay`/`raw-flow-dump-normalize`/`flow-recap`/`status-merge`/`ProjectStatus` owners with `execution: context_fork*`; no wrapper-agent name remains in the file. Reviewer agents and role-doctrine reference list left untouched (doctrine cleanup is Phase 9/H).
3. Phase 4 — convert the six owning Skills into self-contained fork workers, one at a time (PrecapWeek -> PrecapNextDay -> raw-flow-dump-normalize -> flow-recap -> status-merge -> ProjectStatus). **IN PROGRESS.**
   - **PrecapWeek: DONE** (commit `fda9645f`). Added `execution: {context: fork, parent_context_assumed: false}`; frontmatter `name:` corrected to `PrecapWeek` (was `precap-week`, mismatched vs. directory/stage_routing/Skill-tool listing). `primary_operator_output` is now `Weekly_Command_Brief` (the already-promoted template, now actually wired in); dropped the fixed five-project roster and mandatory 1-100 numeric ratings as hard schema/approval gates in both `SKILL.md` and `references/validation-checklist.md` — active project set now derives from confirmed project context, ratings are an optional aid. Downstream seed for PrecapNextDay is the Brief's own compact-handoff block, not a duplicate machine artifact. Archived the superseded `weekly-plan-output-contract.md` to `apex-meta/archive/weekly-orchestration/topology-pre-forked-skills-2026-08/PrecapWeek/` with archive_metadata (D007/D012). Fixed two stale cross-references in the blueprint reference files that pointed at the now-archived contract. Left `weekly-blueprint-standard.md`/`weekly-blueprint-meeting-example.md` substantively untouched (real domain planning logic, not schema bloat) except those reference-path fixes; a few cosmetic `non_goals` mentions of the old artifact name remain there deliberately (Module 01 wording territory, not a live consumer dependency).
   - **Next: PrecapNextDay.** Known coupling to check: `PrecapNextDay/references/input-intake-and-resilience-contract.md` and `daily-plan-output-contract.md` still list `precap_week_output` in their accepted-inputs (found during PrecapWeek's consumer search) — reconcile naming when migrating PrecapNextDay itself, not before.
   - Then: raw-flow-dump-normalize -> flow-recap -> status-merge -> ProjectStatus. Same per-skill protocol each time: read SKILL.md + its wrapper agent, classify wrapper rules, add fork execution semantics, consumer-search before removing fields, one commit per skill. Also verify/fix the same frontmatter `name:` vs. directory-name mismatch for PrecapNextDay and ProjectStatus when reached (raw-flow-dump-normalize, flow-recap, status-merge already match).
4. Phase 5 — switch production routing to the Skills; smoke-test before archiving anything.
5. Phase 6 — simplify `handoff-schema.md` via per-field consumer audit.
6. Phase 7 — normalize the authority/persistence map inside `weekly-orchestrator`.
7. Phase 8 — archive the six wrapper agents (only after Phase 5 smoke test passes).
8. Phase 9 — clean doctrine loading (meta-ops/meta-strategy/meta-detective/alfred doctrines).
9. Phase 10 — static topology verification (zero-reference + positive checks).
10. Phase 11 — fresh-context Module 00 integration test (Tests A-H, no design-chat rationale supplied).
11. Phase 12 — Module 00 closure; write Module 01 handover.

**Open decision:** none architectural. Remaining implementation judgment calls (e.g., exact handoff-schema field disposition, the skill-name-vs-directory-name mismatch above) are resolved per-field/per-skill using the retention test in the target plan, not re-litigated as architecture.

**Next action:** Phase D/4 — migrate `PrecapNextDay` next, same protocol as PrecapWeek (read SKILL.md + `.claude/agents/apex-precap-next-day.md`, classify wrapper rules, add fork execution semantics, consumer-search before removing fields, one commit). Then raw-flow-dump-normalize, flow-recap, status-merge, ProjectStatus in that order.

**Regression fixture:** Existing W34 planning/run artifacts and recovered operator-output design.

**Original scaffold commit:** `9d2811bb7e34a45a49883d9a31774887d6d95606`
