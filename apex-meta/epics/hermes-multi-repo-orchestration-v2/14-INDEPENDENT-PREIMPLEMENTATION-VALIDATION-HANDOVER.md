# Independent Pre-Implementation Validation Handover — Hermes Multi-Repo Orchestration v2

**Target:** Independently audit, challenge, simulate, and where safely possible non-destructively test the complete Hermes multi-repo v2 architecture **before implementation is authorized**. The result must determine whether the accepted design is actually safe, coherent, token-efficient, resilient, and aligned with current battle-tested agent/orchestration practice — or identify exact corrections before any migration/runtime reconfiguration.

**Repository under review:** `leela-spec/apexai-os-meta`  
**Branch:** `main`  
**Primary project folder:** `apex-meta/epics/hermes-multi-repo-orchestration-v2/`  
**Managed repos available for inspection:**
- `leela-spec/apexai-os-meta` (`main`)
- `leela-spec/MasterOfArts` (`main`)
- `leela-spec/acim-secular` (`master`)
- `leela-spec/Investment` (`main`)

## Role

You are the independent pre-implementation architecture, agent-orchestration, safety, reliability, and efficiency reviewer. Your job is **not to defend the current design**. Attempt to falsify it. Prefer proven upstream mechanisms over custom architecture. Recommend changes only when evidence or testing shows material benefit/risk reduction.

## Objective

Produce a decision-ready validation package answering:

> If this exact v2 architecture were implemented on the operator's Windows + WSL2 + Docker machine today, are its state ownership, repo boundaries, Kanban topology, reusable profiles, learning spillover, skill placement, QMD retrieval, Apex aggregation, filesystem model, Docker safety, scheduling, concurrency, failure recovery, and cross-client operation actually sound?

The primary result is a **verified go/revise/no-go judgment with exact evidence**, not another broad architecture proposal.

## Authority model

Use this precedence when claims conflict:

1. **Current live upstream behavior/contracts**: official docs, current source/release/changelog, current open/closed issues, runtime help/schema where accessible.
2. **Actual tested MasterOfArts implementation evidence**: what demonstrably worked on this machine.
3. **Accepted Apex v2 decisions/state**: intended target to audit, not assumptions to ratify.
4. **Current production agent/orchestration best practice** from established primary sources.
5. Secondary sources only when primary evidence is unavailable; label them.

A prior decision, report, or assistant statement is never sufficient evidence by itself.

## Required source set — read first

Read the following completely before settling conclusions:

### Apex v2 authority

- `README.md`
- `DECISIONS.md`
- `state.yaml`
- `01-VERIFIED-ARCHITECTURE.md`
- `11-IMPLEMENTATION-ROADMAP.md`
- `12-RISK-REGISTER.yaml`
- `13-SOURCE-VERIFICATION-MATRIX.md`
- `FUTURE-DEVELOPMENT.md`

### Decision appendices

- `decisions/D01-APEX-CONTROL-PLANE.md`
- `decisions/D02-KANBAN-TOPOLOGY.md`
- `decisions/D03-REUSABLE-ROLE-PROFILES.md`
- `decisions/D04-LEARNING-SPILLOVER.md`
- `decisions/D05-SHARED-SKILL-SOURCE.md`
- `decisions/D06-BMAD-AND-DOMAIN-SKILLS.md`
- `decisions/D07-WSL-CANONICAL-WORKSPACE.md`
- `decisions/D08-QMD-MULTI-REPO.md`
- `decisions/D09-EXTERNAL-MEMORY-DEFERRED.md`
- `decisions/D10-BACKGROUND-MULTI-BOARD-AUTONOMY.md`

### Detailed subject files

- `02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md`
- `03-MULTI-REPO-EFFICIENCY-RISKS-AND-SAFETY.md`
- `04-KANBAN-TOPOLOGY-AND-APEX-ROLLUP.md`
- `05-REUSABLE-PROFILES-LEARNING-AND-MEMORY.md`
- `06-SHARED-SKILL-PROMOTION-AND-CRON.md`
- `07-APEX-CROSS-PROJECT-EXCHANGE-CONTRACT.md`
- `08-QMD-MULTI-REPO-RETRIEVAL.md`
- `09-WSL-CANONICAL-WORKSPACE-MIGRATION-PLAN.md`
- `10-BMAD-AND-DOMAIN-SKILL-POLICY.md`

### Incidents

- `incidents/INC-001-HERMES-KANBAN-DOCKER-WORKSPACE-CONCURRENCY.md`

### MasterOfArts pilot evidence

Use `02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md` as the authoritative inventory. At minimum inspect the current versions of:

- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-002-full-functional-hermes-target.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/QA-VALIDATION-RUNBOOK-v2.md`
- research results R01–R07;
- stack-expansion audit/synthesis R08–R09;
- `Orchestration/Implementation/Antigravity Executor Runbook — Hermes Master of Arts Installation.md`
- `Orchestration/Implementation/Hermes Installation Baseline — Windows + WSL2 + Docker.md`
- `Orchestration/Implementation/OKF-EXECUTION-OBSERVATIONS.yaml`
- `Orchestration/Implementation/MASTER_HANDOVER_AND_AUDIT_REPORT.md`
- `Orchestration/Implementation/AUTONOMOUS_LEARNINGS_SUMMARY.md`
- `IMPLEMENTATION-ACCEPTANCE-REPORT.md`
- implementation evidence P03 and P07–P16;
- `AGENTS.md`, `Lika/AGENTS.md`, `IPOS/AGENTS.md` as examples of the tested project-context pattern.

Expand beyond this named set only when a source points to another authority, a material ambiguity remains, or a validation claim cannot otherwise be resolved.

## Current external research — mandatory

Re-check the **current** official state on the execution date. Do not trust URLs, versions, issue status, or behavior summaries in the v2 files without refreshing them.

At minimum verify:

- NousResearch Hermes Agent: profiles, memory, skills, profile distributions, projects, Kanban/boards/tenants, cron, Docker backend, MCP/config, security/permissions, CLI, current release/changelog and relevant current issues.
- QMD: current release, collection semantics, multi-directory/global registry behavior, MCP schema, update/embed/freshness behavior, AST/code support, exclusions/default scopes.
- BMAD: current installation model, Hermes/Agent Skills support, project/global behavior, current status of any global-link capability.
- MarketingSkills: current install/project-context behavior; confirm MasterOfArts-only remains sensible.
- Agent Skills specification/current interoperability where relevant.
- Microsoft WSL2 filesystem/interop guidance and Docker WSL guidance.
- Codex and Claude Code current Windows/WSL behavior only where it affects architecture portability.

For consequential runtime/tool claims, target **two independent primary confirmations when possible**, e.g. official docs + source/release/issue/runtime evidence. If only one authoritative source exists, say so rather than fabricating a second confirmation.

## Battle-proven orchestration lenses — mandatory

Compare the design against current established production guidance, including at least OpenAI, Anthropic, and Google primary sources. Test whether v2 follows these principles rather than merely naming them:

1. **Simplest sufficient architecture** — do not add agents/services/state stores when deterministic code or one agent suffices.
2. **Single-agent before multi-agent unless isolation, specialization, or real parallelism justify more.**
3. **Central control where synthesis/ownership must remain coherent; handoffs only where ownership genuinely transfers.**
4. **Deterministic code/workflows for deterministic state movement, routing, rollups, validation, scheduling and guardrails whenever feasible.**
5. **Explicit state ownership / one source of truth** for project facts, task state, agent memory, indexes, credentials and portfolio state.
6. **Context isolation + just-in-time retrieval** rather than loading all repos/skills/history into every run.
7. **Progressive disclosure / minimal tool and skill surface** to reduce token/tool-selection ambiguity.
8. **Least privilege + bounded tool access + reversible operations**; human gates for destructive/high-risk actions.
9. **Observability and receipts** — false success must be detectable; exit code alone is insufficient where state mutation matters.
10. **Idempotency, retry bounds, crash recovery, rollback and stale-state detection** for every scheduled/durable process.
11. **Concurrency ownership** — no two writers accidentally mutate one profile, task DB, canonical skill source, repo checkout or rollup artifact.
12. **Eval-driven expansion** — autonomy or complexity only after representative tests prove the simpler mode insufficient/safe.

Do not introduce a framework merely because a best-practice article describes one. Use these principles to challenge the current Hermes-native design.

## What must be audited

Validate **every D01–D10 decision independently**. For each give exactly one verdict:

- `PASS`
- `PASS_WITH_CONDITIONS`
- `REVISE`
- `REJECT`

For each decision record:

- exact claim being validated;
- strongest supporting evidence;
- strongest contradicting/risk evidence;
- hidden coupling/dependency;
- token/latency/operational cost;
- failure modes;
- whether the current mitigation is adequate;
- what evidence would invalidate the decision later;
- exact correction if not `PASS`.

Also audit the **interactions between decisions**, because local correctness is insufficient. At minimum test these cross-couplings:

- D01 Apex control plane × D02 separate boards × asynchronous rollup;
- D02 boards × D03 reused profiles × D10 concurrency gate;
- D03 profiles × D04 learning × D05 shared-skill promotion;
- D05 shared skills × repo-local skills × precedence/write permissions;
- D06 BMAD/domain skills × portable role profiles;
- D07 WSL workspace × Git × Docker mounts × Windows access × Codex/Claude portability;
- D08 QMD × profile-specific MCP config × repo switching × provider-context egress;
- deterministic cron/scheduler × stale/partial rollup × recovery;
- Apex cross-repo dependency references × source-board authority;
- MasterOfArts pilot assumptions × four-repo production topology.

## Simulation / testing standard

Do not stop at prose review.

For each critical flow, perform one of these and label which:

- **EXECUTED** — non-destructive test against an accessible runtime/repo;
- **STATIC-SIMULATED** — exact state-transition/tabletop simulation against current contracts;
- **SOURCE-VERIFIED** — direct contract verification where execution is unavailable or unnecessary.

Never claim a test was executed if it was only simulated.

At minimum validate these scenarios:

1. **Repo switch:** same role completes work in repo A, terminates cleanly, then works repo B without stale project facts or wrong cwd.
2. **Profile collision:** attempt/simulate two boards trying to run the same profile concurrently; prove the current gate detects/prevents it.
3. **Board isolation:** repo worker cannot accidentally inspect/mutate another board through ordinary Kanban tools.
4. **Apex rollup:** one source board succeeds, one fails/stales; rollup must fail closed or mark partial/stale rather than publish healthy state.
5. **Cross-repo dependency:** Apex reference object points to source task; source task remains authoritative; no recursive/bidirectional drift.
6. **Learning promotion:** project-specific lesson is rejected; generic procedure is sanitized, reviewed, versioned, deployed and discoverable without raw-memory sync.
7. **Skill collision:** project-local skill and shared skill have same/related trigger; verify precedence and no unintended canonical-source mutation.
8. **QMD repo-local use:** role working from each repo can retrieve only explicitly intended collections; unscoped query cannot silently search the whole estate.
9. **QMD stale index:** accepted repo change occurs but index is stale; detection/refresh path must be unambiguous.
10. **Docker workspace persistence:** disposable file and commit persist host-side; cwd/tool paths agree; unrelated host paths and secrets remain inaccessible.
11. **WSL migration:** Windows and WSL copies diverge before migration; process detects dirty/untracked/branch/HEAD differences before freezing old copy.
12. **Crash/restart:** board/task/rollup/QMD/profile state resumes without reconstructing truth from chat history.
13. **Scheduler duplicate/retry:** job runs twice or fails midway; outputs remain idempotent and health metadata reveals failure.
14. **Client portability:** Codex or Claude operates on the same canonical repo without requiring duplicated project truth or corrupting Hermes-owned state.
15. **Future D10 enablement:** define the exact acceptance evidence required before background multi-board autonomy could be safely enabled.

If the accessible environment permits safe read-only or disposable tests, use them. Do not mutate production project truth, install/change runtime components, migrate repositories, enable schedulers, or activate D10.

## Risk hunt — explicitly look for what we may have missed

Search for failure classes not already represented in `12-RISK-REGISTER.yaml`, including:

- hidden shared mutable state;
- file locks / SQLite WAL / multiple-process behavior;
- path normalization and Windows↔WSL path leakage;
- case sensitivity, permissions and ownership changes;
- Git safe-directory/credential/helper behavior;
- Docker user/UID/file ownership drift;
- environment-variable/credential leakage;
- stale config after profile/distribution updates;
- skill name/trigger collisions and supply-chain risk;
- repo trust boundaries and prompt-injection through project content;
- QMD collection overlap, stale embeddings, index corruption or retrieval bleed;
- cron timezone/startup/persistence/duplicate-run behavior;
- partial rollups and stale portfolio decisions;
- branch-name differences (`main` vs `master`);
- repo renames/moves and broken references;
- schema/version drift;
- upstream issue fixes that invalidate our workaround;
- upstream regressions that invalidate a previously passing pilot;
- token growth from AGENTS, memory, skill catalogs, tool schemas or portfolio summaries;
- observability gaps where an agent can report success without durable state change;
- recovery/rollback paths that exist only on paper.

## Anti-overengineering gate

Before recommending any new service, agent, database, synchronizer, wrapper, MCP server, memory layer, queue, framework or daemon, answer:

1. Which measured/verified failure requires it?
2. Can current Hermes/QMD/Git/Docker/OS primitives solve the same problem?
3. Can deterministic code solve it more simply?
4. Does it create another source of truth or mutable state owner?
5. Does it increase token/context/tool complexity?
6. Can it be deferred until a real failure occurs?

If there is no demonstrated need, **do not add it**.

## Required deliverables

Write validation outputs only under:

`apex-meta/epics/hermes-multi-repo-orchestration-v2/validation/independent-preimplementation-review/`

Create:

1. `00-VERDICT.md` — concise go/revise/no-go, top blockers, confidence.
2. `01-D01-D10-AUDIT.md` — decision-by-decision verdict matrix with evidence and corrections.
3. `02-CROSS-DECISION-ORCHESTRATION-SIMULATION.md` — critical flows, state transitions, failure injections, executed/static/source-verified labels.
4. `03-RISK-GAP-REGISTER.yaml` — only newly discovered or materially changed risks; map to existing risk IDs where applicable.
5. `04-CORRECTION-PLAN.md` — only if changes are needed; minimum coherent correction set, ordered by dependency and value.
6. `05-SOURCE-REFRESH-MATRIX.md` — current upstream version/date/status for every consequential contract/issue used.

Do not create implementation code or rewrite the current architecture during validation.

If corrections are required, do not directly edit existing v2 authority files. Produce exact proposed changes in `04-CORRECTION-PLAN.md`; implementation/patch generation is a later operator-authorized step.

## Evidence standard

For every consequential claim, distinguish:

- `REPO_EVIDENCE`
- `UPSTREAM_DOC`
- `UPSTREAM_SOURCE_OR_RELEASE`
- `UPSTREAM_ISSUE`
- `EXECUTED_TEST`
- `STATIC_SIMULATION`
- `INFERENCE`

Never turn an inference into a verified fact.

Open upstream issues are evidence of risk, not automatic proof that the installed version is affected; verify version/scope where possible.

A historical passing MasterOfArts test proves only the tested topology/version/conditions. Do not extrapolate it silently to multi-repo concurrency or a newer runtime.

## Research/process freedom

Choose your own internal research sequence, batching, source grouping, subagents and note-taking. Use subagents only when they materially improve **independence, specialization, context isolation, or parallel research**. Do not create agent swarms for work a single capable reviewer can do reliably.

A useful pattern is:

- one primary reviewer owns synthesis and verdict;
- independent verifier(s) may challenge high-risk claims or current upstream contracts;
- deterministic scripts/tools handle comparisons, schemas and reproducible checks;
- evaluator review is used only where clear acceptance criteria exist.

This is a heuristic, not a required implementation.

## Hard boundaries

- Work on current repository branches; do not create/switch branches or worktrees.
- Do not implement the v2 architecture.
- Do not migrate/delete/freeze repositories.
- Do not change Hermes/QMD/Docker/WSL configuration.
- Do not enable schedulers or D10 background dispatch.
- Do not write outside the specified validation output folder.
- Do not overwrite current decisions merely because a newer option looks interesting; require evidence that the accepted choice is materially wrong or suboptimal.
- Do not lower standards to preserve prior work. `REVISE` or `REJECT` is allowed.

## Final validation

Before finishing, perform a system-level consistency check:

- every D01–D10 audited;
- every critical cross-decision coupling tested/simulated;
- every current upstream dependency refreshed;
- every incident/status assumption rechecked;
- every new risk mapped to detection + mitigation + owner;
- no duplicated source-of-truth introduced;
- no recommended complexity without demonstrated value;
- token/context/tool efficiency explicitly assessed;
- safety, persistence, concurrency, rollback and false-success paths covered;
- conclusions distinguish evidence, simulation and inference;
- proposed corrections form the **minimum coherent change set**, not a redesign by default.

## Success condition

The run is successful when an operator can read `00-VERDICT.md` and know whether v2 is safe to implement, while another technical executor can use the remaining validation artifacts to reproduce the evidence, understand every residual risk, and apply only the minimum necessary corrections.

**Do not return `PASS` because the architecture is plausible. Return `PASS` only if the consequential contracts and interactions survive current-source verification plus the required tests/simulations.**
