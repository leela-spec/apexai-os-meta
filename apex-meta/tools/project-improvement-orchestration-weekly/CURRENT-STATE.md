# Current State

**Project phase:** Module 00 architecture integration (implementation, not research)

**Active module:** `00-orchestration-spine`

**Accepted topology (D012, O001 resolved):** one main-session `weekly-orchestrator`; six stage components (`PrecapWeek`, `PrecapNextDay`, `raw-flow-dump-normalize`, `flow-recap`, `status-merge`, `ProjectStatus`) executed as directly-dispatched Skills with isolated `context: fork`; two retained blind reviewer agents (`apex-review-validity`, `apex-review-alignment`); `apex-session` (durable mutation) and `apex-sync` (deterministic read-side) as direct backbone; `PromptEngineer`/`AIRouting`/`model-usage-log` loaded on demand only.

**Implementation phase order (from the target plan) and status:**

1. Phase 1/2 — record decision + fix `.claude/Claude.md` -> `.claude/CLAUDE.md` cold-start discovery. **DONE** (commits `ad95d50d`, `e24d3039`).
2. Phase 3 — rewrite `weekly-orchestrator/SKILL.md` routing to dispatch directly to owning Skills. **DONE** (commit `91efd902`). No wrapper-agent name remains in the file. Role-doctrine reference list left untouched (that's Phase 9/H).
3. Phase 4 — convert all six owning Skills into self-contained fork workers. **DONE.**
   - `PrecapWeek` (`fda9645f`): primary output is now `Weekly_Command_Brief`; dropped the fixed five-project roster + mandatory 1-100 ratings as hard gates (project set now derives from confirmed context); archived the superseded `weekly-plan-output-contract.md`.
   - `PrecapNextDay` (`7478f4b5`): primary output is now the PreCap Next Day Brief + one Flow Execution Card per flow + real prompt files (J3/J4/J5), replacing the `next_day_plan`/`flow_packet`/`flow_prompt_pack` triad as the completion gate. The underlying ~700-1300 line schema files were kept as optional `internal_detail_schemas` (Module 02-04 depth), not rewritten; only the three fully-superseded *blank templates* were archived.
   - `raw-flow-dump-normalize` (`7c3b1324`): added conditional/bypass invocation as a self-declared Skill property (was previously only known to the orchestrator's routing table).
   - `flow-recap` (`c6c2db56`): `model_usage_delta_candidate` changed from unconditionally required to conditional-on-actual-usage-evidence, in the Skill, its packet contract, and its template.
   - `status-merge` (`46f4561b`) and `ProjectStatus` (`8c6c50ea`): both were already lean/boundary-correct; only needed explicit `execution: context_fork_*` declarations plus the target plan's literal owns/must_not/sources fields.
   - Frontmatter `name:` vs. PascalCase-directory mismatches fixed for all three affected skills: `PrecapWeek`, `PrecapNextDay`, `ProjectStatus`.
   - **Working rule for Module 02-08 handoff:** when a stage's entrypoint treats a deep internal schema file as optional rather than a hard gate, do NOT rewrite that file's internals in the same pass unless the plan's phase text explicitly names it as replaced. Only archive a file when it is *itself* fully superseded (its whole purpose was authoring the now-optional schema).
4. Phase 5 — switch production routing to the Skills; smoke-test before archiving anything. **DONE.** Static verification passed: `stage_routing` names only Skill owners, zero wrapper-agent references remained in `weekly-orchestrator/SKILL.md`. Found and fixed one leftover "same agent" wording inconsistency during the read-through (commit `47a01154`). Also found that `apex-review-alignment.md`, `write-rules.md`, and `PrecapNextDay/references/kb-integration-contract.md` matched the wrapper-agent-name grep pattern but were false positives (they reference the legacy state file `state/apex-project-status.md`, a naming collision with the `apex-project-status` agent, not an actual dependency).
5. Phase 6 — simplify `handoff-schema.md` via per-field consumer audit. **DONE** (commit `3aee01c3`). Removed `next_state`/`prerequisites` (no producer or consumer found anywhere). Kept `sources`/`uncertainties` (read by `apex-review-validity`), `unresolved_risk` (the literal review-trigger signal), `target_surface` (always `none` for weekly packets, kept as a boundary-check constant). Renamed `stage_agent_return` -> `stage_worker_return` in the packet_type enum.
6. Phase 7 — normalize the authority/persistence map inside `weekly-orchestrator`. **DONE** (commit `d8d0d25e`), lifted verbatim from the target plan.
7. Phase 8 — archive the six wrapper agents. **DONE** (commit `34bfbcb0`), each with `archive_metadata` under `apex-meta/archive/weekly-orchestration/topology-pre-forked-skills-2026-08/wrapper-agents/`. `.claude/agents/` now retains only the two reviewer agents plus agents belonging to other systems (Multi-Agent Orchestration, apex-kb).
8. Phase 9 — clean doctrine loading. **DONE** (commit `4dc3d7a8`). `meta-ops-doctrine.md`, `alfred-doctrine.md`, `meta-detective-doctrine.md`, `hygiene-clean-doctrine.md`, `informatics-design-doctrine.md` were already clean (no stale references; the two QA/improvement doctrines are already `read_when`-gated, never preloaded). `meta-strategy-doctrine.md` named the archived `apex-precap-week` agent as Consumer/authority and — worse — had zero live readers once that agent was archived (only the wrapper agent's own startup-reads list ever pointed at it; `weekly-orchestrator/SKILL.md` never did). Fixed the stale text and added it to `PrecapWeek/SKILL.md`'s Supporting Files so it has a real consumer again.
9. Phase 10 — static topology verification. **DONE**, all checks pass:
   - Zero-reference: no active-path mention of any of the six wrapper-agent names remains in `.claude/`. (Three grep matches are a confirmed pre-existing, unrelated naming collision with the legacy state-file path `state/apex-project-status.md`, not the agent — found during Phase 5, reconfirmed here.)
   - Positive: `weekly-orchestrator` is sole lifecycle owner; all six stage Skills self-declare `context: fork*` (grep-verified in their own `SKILL.md`); `.claude/agents/` contains exactly `apex-review-validity` + `apex-review-alignment` among weekly-loop-relevant agents; `apex-session`/`apex-sync` own durable-mutation/deterministic-read-side per the authority map; `PromptEngineer`/`AIRouting`/`model-usage-log` are all declared on-demand (`PrecapNextDay`'s `dependencies`, `flow-recap`'s `model_usage_delta.invocation`).
10. Phase 11 — fresh-context Module 00 integration test (Tests A-H, no design-chat rationale supplied). **NEXT.**
11. Phase 12 — Module 00 closure; write Module 01 handover.

**Open decision:** none architectural.

**Next action:** Phase 11/J — the fresh-context test. This must run in a session that receives no architecture explanation from this migration's history: just the repo, production `.claude/CLAUDE.md`, a normal `weekly-orchestrator` invocation, and W34 fixture/input refs. Verify Tests A-H from the target plan (cold start finds one entrypoint and no wrapper agent; PrecapWeek/PrecapNextDay dispatch directly; conditional evidence-normalize bypass/invoke correctly; two independent flow-recaps run as separate forked workers; model-usage-log/AIRouting stay unloaded absent a trigger; reviewer agents run blind only when consequential; a durable-mutation attempt from status-merge is rejected and routed to apex-session). On pass, close Module 00 per Phase 12 and write the Module 01 (Weekly Command Brief) handover.

**Regression fixture:** Existing W34 planning/run artifacts and recovered operator-output design.

**Original scaffold commit:** `9d2811bb7e34a45a49883d9a31774887d6d95606`
