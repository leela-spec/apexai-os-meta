# 15 — Hermes Multi-Repo v2 Implementation Roadmap v2 — Antigravity Executor

Status: **PLAN COMPLETE / IMPLEMENTATION NOT AUTHORIZED / BECOMES EXECUTION AUTHORITY AFTER CONTROL-FILE PATCH APPLICATION**  
Date: 2026-08-24  
Repository: `leela-spec/apexai-os-meta`  
Branch: `main`  
Executor: **Google Antigravity**  
Architecture dependency on Antigravity: **NO**  
Implementation-run dependency on Antigravity: **YES**

## 0. Why v2 exists

`11-IMPLEMENTATION-ROADMAP.md` remains a valuable technical phase catalog, but it is no longer sufficient as the execution authority.

Drift found after independent pre-implementation validation:

1. **Executor drift:** v1 says the target has “no dependency on Antigravity.” That remains true for the final architecture, but the implementation run now intentionally uses Antigravity as the bounded executor and verifier.
2. **Correction sequencing drift:** validation corrections C05/C06 require profile-memory and skill-scope cleanup **before** reusable-role cross-repo tests; v1 normalizes some of this later.
3. **Docker security drift:** C01/C07 require task-scoped mount provenance, host persistence, and environment/credential canary tests before a reusable execution lane is accepted.
4. **QMD freshness drift:** C04 requires a refresh receipt bound to source Git HEAD; `qmd status` or timestamps alone are insufficient.
5. **Rollup integrity drift:** C03 requires atomic fail-closed publication with last-known-good preservation.
6. **Context-entry drift:** C08 requires every managed repository to expose a concise, verified authority-routing context entrypoint before board activation.
7. **Pilot-state drift:** MasterOfArts proved a strong single-repo runtime, but its `/root/MasterOfArts` mounts, globally visible BMAD/MarketingSkills copies, and project schedules recorded in profile memory must not become the multi-repo baseline.

This v2 does **not** redesign D01–D10. It imports the useful technical detail from v1, changes execution order where validation requires it, and adds Antigravity execution discipline.

## 1. Authority and read order

Antigravity must read only the material required for the active phase.

Always read first:

1. `README.md`
2. `DECISIONS.md`
3. `state.yaml`
4. this file
5. `validation/independent-preimplementation-review/00-VERDICT.md`
6. `validation/independent-preimplementation-review/04-CORRECTION-PLAN.md`

Read when relevant:

- `11-IMPLEMENTATION-ROADMAP.md` — v1 technical phase detail only; not current execution authority after the activation patch lands.
- `12-RISK-REGISTER.yaml`
- `13-SOURCE-VERIFICATION-MATRIX.md`
- decision appendix for the active decision only;
- `incidents/INC-001-HERMES-KANBAN-DOCKER-WORKSPACE-CONCURRENCY.md` for Docker/Kanban/D10 work;
- `02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md` for pilot evidence migration;
- the relevant deeper subject file (`03`–`10`) only when its phase needs it.

Do not reconstruct the architecture from chat memory. Do not load every research file into every context.

## 2. Antigravity executor law

Antigravity is the **implementation executor and verifier**, not the architect.

It may:

- inspect current runtime/repository state;
- refresh current official upstream contracts;
- execute the already-approved phased implementation;
- apply approved exact-match patches;
- create new implementation state/evidence files;
- run safe disposable tests;
- commit phase-related changes on `main` when the launch authorization allows it;
- produce explicit blockers when native/upstream behavior cannot satisfy a locked invariant.

It must not:

- redesign D01–D10;
- introduce another orchestrator, database, memory service, RAG service, message broker, sync service, wrapper, global BMAD linker, or custom policy runtime;
- create branches, PRs, or worktrees;
- switch away from the repository’s canonical branch;
- force-push or rewrite history;
- silently reconcile divergent local work;
- weaken a security condition to make a phase pass;
- treat prior pilot receipts as proof of current installed behavior without rechecking the active runtime;
- enable D10 merely because earlier single-repo tests passed.

If an upstream-native mechanism fails a required invariant, diagnose once, verify current docs/issues, attempt one evidence-backed correction, then record `PHASE_BLOCKER`. Do not invent substitute infrastructure.

## 3. Patch-only mutation law

For **existing** control, authority, plan, decision, state, risk, registry, or handover files:

1. read the live target content needed for the change;
2. create an exact-match patch block containing:
   - `<file>`
   - `<old>` copied byte-for-byte from the live file
   - `<new>` containing only the intended replacement;
3. require the `<old>` block to match **exactly once**;
4. apply with a deterministic exact-match operation;
5. re-read the changed range and verify only the intended bytes changed;
6. never use whole-file replacement, `cat >`, generated full rewrites, or connector-style replace-file operations for an existing file.

New files may be created directly.

Patch artifacts live under:

`apex-meta/epics/hermes-multi-repo-orchestration-v2/patches/`

Do not create a reusable patch framework merely to apply these changes. Use the existing project patch convention or a one-shot deterministic exact-match operation with explicit assertions.

## 4. Current-source law

Immediately before each installation/configuration/runtime mutation phase, Antigravity must refresh the relevant contract using this precedence:

1. installed runtime `--version`, `--help`, schema, or effective config output;
2. current official product documentation;
3. current official repository/release/changelog/issues;
4. durable project research and pilot receipts;
5. secondary sources only to identify a question.

Record:

```text
component
installed_version
current_upstream_version_or_commit
source_checked_at
syntax_or_schema_used
meaningful_drift
phase_consequence
```

Do not hard-code the MasterOfArts Antigravity baseline (`agy 1.1.19`) as current truth. Recheck Antigravity.

## 5. Context-management protocol

Keep one **primary Antigravity conversation as the thin program coordinator** across the implementation run while it remains healthy. Do not restart the primary conversation merely because a phase ended.

The coordinator owns only:

- the current roadmap position;
- `implementation-state.yaml`;
- active blockers and operator gates;
- delegation of the next bounded task;
- acceptance of returned evidence;
- the decision to advance, retry once with evidence, or block.

Do not make the coordinator ingest deep research, large logs, repository-wide dumps, or full subagent transcripts. Detailed work belongs in fresh bounded subagent contexts or targeted tool calls and returns as concise evidence plus file/path references.

At the first authorized implementation mutation, create:

```text
apex-meta/epics/hermes-multi-repo-orchestration-v2/implementation/
  implementation-state.yaml
  evidence/
```

Minimum state:

```yaml
schema_version: 1
program: hermes_multi_repo_orchestration_v2
executor: antigravity
branch: main
current_phase:
last_completed_phase:
phase_status:
last_verified_commit:
last_verified_repo:
last_verified_workdir:
installed_versions: {}
corrections: {}
blockers: []
next_phase:
next_exact_action:
```

For every phase create exactly one compact evidence file:

`implementation/evidence/PXX-<slug>.md`

It contains only:

- input state;
- official/current sources consulted;
- commands/config actually used;
- exact files/paths changed;
- relevant PASS/FAIL evidence;
- rollback/recovery information;
- unresolved blocker if any;
- final phase verdict.

Do not paste giant terminal logs into the coordinator context. Save large logs separately only when necessary and cite the exact relevant excerpt/path.

At phase end:

1. update implementation state;
2. write evidence;
3. verify Git diff is phase-scoped;
4. return a concise result to the coordinator;
5. let the coordinator advance to the next phase without reloading completed phase detail.

For each new phase, load only:

- this v2 plan;
- current implementation state;
- the authority/source files actually required by that phase.

Use Antigravity's `/context` view to notice context pressure. If the primary conversation becomes materially degraded, repetitive, or confused, persist state first and resume from the durable state in a fresh coordinator conversation. A context reset is recovery, not the normal phase boundary.

## 6. Main-agent / subagent policy

The primary Antigravity agent is the **coordinator**. It keeps the high-level plan and durable state, delegates bounded work, reviews returned evidence, and decides whether a phase passes.

Use fresh subagents when they reduce coordinator context or provide valuable independent verification. Do not spawn them by default for trivial deterministic steps.

A delegated task must be narrow enough to state in a short contract containing:

- goal;
- allowed workspace/files;
- required source(s);
- whether mutation is allowed;
- acceptance check;
- expected concise return.

Subagent rules:

- each starts from the minimum task-specific context, not the parent transcript;
- return conclusions, evidence paths, changed paths, tests, and blockers rather than a narrative transcript;
- read-only research/verification tasks may run in parallel when independent;
- writable tasks against the canonical checkout run one at a time and must not overlap on shared files or runtime state;
- a writable subagent may execute a bounded phase task, but the coordinator remains the authority for phase acceptance and state advancement;
- subagents do not redesign architecture or create independent authoritative state;
- do not create a permanent custom-agent hierarchy merely for this implementation run.

At P00, probe the installed Antigravity version's current subagent behavior before depending on it. If subagents are unavailable or unreliable, execute the same bounded task sequentially in the primary agent; do not stop the Hermes implementation to debug Antigravity orchestration internals.

## 7. Git law

- Work directly on each repository’s canonical branch: Apex/MasterOfArts/Investment=`main`, ACIM=`master`.
- Never create a branch or PR unless the operator explicitly changes this rule.
- Never use worktrees for this implementation program.
- Before mutation, record branch, HEAD, remote, dirty/untracked state.
- Never discard unrelated changes.
- Commit only phase-related files when commit authorization exists.
- Push only when the active launch instruction explicitly authorizes remote persistence.
- A command returning exit 0 is not acceptance evidence when the relevant upstream defect documents false-success behavior.

## 8. Human gates

Do not ask routine technical questions. Continue autonomously through ordinary ambiguity using current evidence.

Stop only for:

- **H1 ADMIN/REBOOT:** Windows/WSL/Docker change requires operator elevation or reboot.
- **H2 CREDENTIAL/PRIVACY:** a credential must be entered or a new data class would leave the machine.
- **H3 DIVERGENT USER DATA:** two candidate canonical copies contain unresolved local work.
- **H4 ARCHITECTURE CONTRADICTION:** current upstream behavior cannot satisfy a locked D01–D10 invariant without custom infrastructure.
- **H5 DESTRUCTIVE/FREEZE:** deletion, overwrite, migration cutover, or freezing a prior live checkout requires explicit operator choice.
- **H6 D10/AUTONOMY:** enabling background concurrent multi-board execution requires a separate explicit decision after its acceptance tests.
- **H7 FINAL:** final production transition / remote push where not already authorized by the launch command.

## 9. Evidence labels

Use exactly:

- `EXECUTED` — this Antigravity run executed the check against the current runtime;
- `SOURCE_VERIFIED` — current primary source or durable prior receipt inspected;
- `STATIC_SIMULATION` — explicit state/failure simulation;
- `INFERENCE` — reasoned conclusion not itself an observed fact.

Never relabel a prior receipt as `EXECUTED` in the current phase.

---

# Phase sequence

## P00 — Antigravity + repository preflight

**Goal:** prove the executor and Apex repository are safe to use.

Actions:

1. verify current Antigravity version/help/current official release;
2. verify targeted web/current-source research works;
3. verify repository `leela-spec/apexai-os-meta`, branch `main`, remote, HEAD, dirty state;
4. verify patch-only mutation method can assert exact-match count without changing a file;
5. verify no implementation mutation has occurred.

Gate:

`P00_PASS = executor current + repo identified + patch mechanism proven read-only`

## P01 — Authority, validation, and pilot-provenance freeze

**Goal:** start from the exact accepted architecture and preserve evidence before migration.

Read:

- D01–D10 ledger;
- v2 validation verdict/correction plan;
- MasterOfArts migration manifest;
- current managed-repo registry in `state.yaml`.

Actions:

1. verify every manifest source path still exists at current MasterOfArts HEAD;
2. record current four repo refs/branches;
3. classify existing MasterOfArts evidence as authority / research provenance / implementation evidence / historical;
4. record all C01–C08 as pending gates in implementation state;
5. do not migrate or copy content yet.

Gate:

`P01_PASS = no authority/evidence ambiguity and all correction gates represented`

## P02 — Freeze unsafe background mutation

Imports technical intent from v1 Phase 2.

Goal:

- background all-board dispatch OFF;
- auto-decomposition OFF unless explicitly needed for a later bounded test;
- no scheduled writer touching managed repos during migration;
- read-only inspection still allowed.

Recheck installed Hermes syntax before mutation.

Gate:

`P02_PASS = no unmanaged worker can start while paths/profiles/skills are changing`

## P03 — Reusable-profile and skill-scope reset (C05 + C06)

**This is intentionally earlier than v1 normalization.**

Actions:

1. inventory reusable profile homes/config/memory/skills;
2. classify `USER.md`/`MEMORY.md` entries;
3. preserve only stable non-project preferences appropriate to the reusable profile;
4. remove project schedules/task facts from reusable runtime memory without moving them into another memory store;
5. verify no fixed repo `terminal.cwd`, static project volumes, project credentials, or project-default QMD collections in reusable profiles;
6. inventory every active skill root and same-name precedence;
7. disable/remove stale global/learned copies that shadow approved sources;
8. enforce target scope: BMAD repo-local where used; MarketingSkills MasterOfArts-only; Apex KB Apex-only; reviewed generic skills through the Apex promotion channel.

Use patch-only edits for existing repo control files. Runtime-home configuration changes must be separately evidenced and reversible.

Gate:

`P03_PASS = clean reusable profiles + unambiguous skill provenance`

## P04 — ACIM normal-user WSL + context-entry pilot (C02 + C08)

Imports v1 Phase 3 and the relevant D07/C08 requirements.

Actions:

1. inventory ACIM Windows/WSL copies, branch `master`, HEAD, dirty/untracked/local-only data;
2. stop at H3 if divergent user data cannot be reconciled deterministically;
3. establish/verify `~/workspaces/acim-secular` under the normal WSL operator account;
4. prove ownership/UID/GID and normal Git operations without routine root ownership;
5. freeze old live-looking copy only at H5; never auto-delete;
6. add/adapt only a minimal root authority-routing context entry using an exact-match patch if an existing file must change;
7. cold-start from the intended workdir and prove the context route identifies current truth and exclusions without repo-wide exploration.

Gate:

`P04_PASS = one canonical ACIM workspace + correct authority routing + no lost state`

## P05 — Isolated boards and optional Hermes Projects

Imports v1 Phases 4–5.

Boards:

- `apex`
- `masterofarts`
- `acim`
- `investment`

Rules:

- validate each board exists from live enumeration;
- never trust `bind-board` exit 0 alone (`#76285`);
- one disposable task/query proof per board;
- no tenants as memory/security boundary;
- no cross-board native dependency assumption.

Gate:

`P05_PASS = four isolated board stores + project mappings only to existing board/path identities`

## P06 — QMD ACIM pilot + Git-HEAD refresh receipt (C04)

Imports v1 Phases 6–7 with stronger freshness semantics.

Actions:

1. preserve existing MasterOfArts QMD collections;
2. create the minimum approved ACIM named collections;
3. exclude large project corpora from default search;
4. run native update/embed/status;
5. write deterministic refresh receipt bound to ACIM branch+HEAD;
6. verify explicit collection query from ACIM and another cwd;
7. advance a disposable source change/commit where safe and prove the stale receipt blocks high-stakes retrieval until refreshed;
8. configure QMD MCP only for profiles that need retrieval; test at least two profiles.

Gate:

`P06_PASS = scoped retrieval + cwd independence + source-HEAD freshness gate`

## P07 — Docker workspace + credential boundary (C01 + C07)

Imports v1 Phase 8 and strengthens it.

Before commands execute:

1. resolve authorized host workspace;
2. inspect effective bind list;
3. prove no stale `/root/MasterOfArts` or sibling-repo mount;
4. prove container cwd maps to the actual bound destination;
5. reject profile cwd override;
6. create host-persistence canary and, where safe, disposable Git commit; verify after worker/container exit;
7. verify terminal/file/execute-code share the same workspace;
8. verify unrelated host paths and Docker socket absent;
9. set harmless host credential canaries and prove they do not enter the container unless explicitly allowlisted;
10. verify only required environment values are forwarded using current installed Hermes semantics.

If native Hermes cannot satisfy the task-scoped host-backed boundary, stop at H4. Do not add a mount router/wrapper.

Gate:

`P07_PASS = bounded host-backed workspace + negative credential canary`

## P08 — Investment canonical workspace + context/QMD onboarding

Repeat the proven P04/P06 pattern for Investment on `main`.

Do not generalize from ACIM without checking Investment’s real files/authority.

Gate:

`P08_PASS = Investment canonical workspace + context route + scoped/fresh QMD`

## P09 — Sequential reusable-role proof: ACIM -> Investment

Imports v1 Phase 9.

Use one clean reusable role, preferably `research-strategist`:

1. task A in ACIM;
2. complete and inspect resulting local memory/learned-skill changes;
3. confirm no active same-profile process remains;
4. task B in Investment;
5. prove context/QMD/workspace switch;
6. prove ACIM facts are not Investment authority;
7. distinguish generic procedure from project facts.

Gate:

`P09_PASS = same role reused sequentially with no factual contamination or concurrent writer`

## P10 — Reviewed learning-promotion pilot

Imports v1 Phase 10 and D04/D05.

Use two candidates:

- A = deliberately generic reusable procedure;
- B = deliberately project-specific fact/procedure.

Actions:

1. deterministic candidate hash inventory;
2. unchanged rescan produces no duplicate;
3. independent reviewer classifies A/B;
4. A enters disposable Apex reviewed shared-skill candidate path;
5. B stays project-local/rejected;
6. deploy A through the proposed runtime deployment mechanism;
7. verify another role discovers exactly the reviewed copy;
8. prove no raw memory copy and no same-name ambiguous skill source.

Gate:

`P10_PASS = reviewed procedural spillover without memory or skill-source drift`

## P11 — Atomic fail-closed Apex rollup (C03)

Imports v1 Phase 11.

Required algorithm:

1. resolve managed repo registry and expected branches;
2. read all four explicit board JSON surfaces;
3. resolve current repo HEADs;
4. reject missing/duplicate repo or board identities;
5. build candidate snapshot in memory/temp path;
6. validate completeness/schema;
7. atomically publish only after all four inputs pass;
8. include source HEADs and generation time;
9. on failure preserve last-known-good snapshot and emit degraded health receipt.

Failure injection:

- one board query fails;
- one wrong board slug;
- one branch mismatch.

Gate:

`P11_PASS = partial data can never overwrite the last-known-good portfolio snapshot`

## P12 — Scheduler selection and reliability

Imports v1 Phase 12.

Compare only the native candidates actually available on the installed machine:

- Hermes no-agent cron;
- WSL systemd timer / OS scheduler.

Require:

- zero model calls for deterministic rollup/harvest;
- visible nonzero failure;
- restart persistence;
- idempotence;
- last-success/last-failure/heartbeat evidence;
- no broad repo write authority;
- no silent-success inference from empty stdout (`#20353`).

Choose the simpler mechanism that passes. Do not prefer Hermes merely because it is already present.

Gate:

`P12_PASS = scheduled deterministic job survives restart and exposes health`

## P13 — MasterOfArts canonical migration + legacy pilot cleanup

Imports v1 Phase 13 plus C02/C05/C06/C01/C07 consequences.

Actions:

1. compare current Windows and WSL Git/local states completely enough to detect divergence;
2. reconcile before canonical declaration; stop at H3/H5 when necessary;
3. converge to normal-user `~/workspaces/MasterOfArts`;
4. eliminate target dependence on `/root/MasterOfArts`;
5. repoint QMD collections and refresh receipts;
6. verify MasterOfArts board/project;
7. preserve BMAD repo-local and MarketingSkills MasterOfArts-only;
8. ensure no global/learned duplicate shadows them;
9. run a small known-good task through the already-proven Docker/QMD/profile contracts.

Gate:

`P13_PASS = MasterOfArts uses the same clean multi-repo rules without losing pilot provenance`

## P14 — Apex canonical migration + control-plane context

Imports v1 Phase 14.

Actions:

1. full Apex dirty/untracked/divergence audit;
2. verify current Apex KB authority before moving anything;
3. establish `~/workspaces/apexai-os-meta` under normal WSL user;
4. verify/create minimal Apex Hermes authority-routing context without weakening existing Codex/Apex-KB rules;
5. configure minimal Apex QMD control collection with Git-HEAD receipt;
6. verify Apex board/project;
7. verify shared-skill canonical source/deployment does not become routine agent-writeable state.

Gate:

`P14_PASS = control plane operational from canonical WSL workspace without authority duplication`

## P15 — Cross-repo skill/capability registry normalization

Imports v1 Phase 15.

Produce the desired-state registry from actual installed/discovered capabilities, not planned assumptions.

For every repo/profile pair record:

- discovered skill source/path;
- version/commit/hash where relevant;
- intended scope;
- precedence winner if duplicate names exist;
- QMD MCP presence only where needed;
- prohibited capabilities absent.

No mass install.

Gate:

`P15_PASS = active capabilities match D06 and no hidden global shadow copies exist`

## P16 — Full cross-repo recovery test

Imports v1 Phase 16.

State before restart:

- four boards with representative persisted tasks;
- sequential role reuse already proven;
- scoped QMD collections + refresh receipts;
- Apex last-known-good rollup + health state;
- one reviewed shared procedure;
- scheduler health receipt.

Restart approved subsystems/WSL condition, then verify independently:

- Git repos/branches/HEADs;
- board state;
- QMD health + freshness receipts;
- clean reusable profile state;
- shared-skill deployment provenance;
- Apex rollup freshness;
- scheduler health.

No chat replay may be required.

Gate:

`P16_PASS = operational state reconstructs from durable owners only`

## P17 — D10 installed-version autonomy decision

Imports v1 Phase 17 and D10/INC-001.

Recheck current Hermes version/issues first.

Required before even considering enablement:

1. Kanban task workspace is host-backed;
2. profile cwd cannot override task mount;
3. host/container cwd provenance correct;
4. global/per-profile cross-board worker limits known and tested;
5. same reusable role cannot receive concurrent writers;
6. worker/swarm limits tested;
7. recovery/cleanup tested;
8. credential/mount isolation remains intact under dispatched workers.

If any condition fails or remains unproven:

`KEEP_SAFE_MODE_A`

This is a fully acceptable production result.

Enabling D10 requires H6 explicit operator approval.

## P18 — Final acceptance

Allowed verdicts:

```text
MULTI_REPO_V2_PASS_SAFE_SEQUENTIAL
MULTI_REPO_V2_PASS_WITH_AUTONOMOUS_DISPATCH
MULTI_REPO_V2_BLOCKER
```

Final report must include:

- actual Antigravity/Hermes/QMD/Docker/WSL versions;
- canonical repo paths and branch refs;
- board/project identities;
- profile baseline and single-writer evidence;
- active skill provenance/scopes;
- QMD collections/MCP/freshness receipts;
- Docker mount/cwd/persistence/credential negative tests;
- sequential cross-repo role proof;
- reviewed learning-promotion proof;
- atomic rollup proof;
- scheduler health/restart proof;
- full recovery result;
- open upstream issues still relevant;
- D10 decision;
- unresolved future-development items.

## 10. Success metric

Success is not “all tools installed” and not “Antigravity finished the checklist.”

Success is:

```text
one durable Apex control plane
+ four independent source-repo truths
+ one canonical WSL checkout per repo
+ isolated repo boards
+ reusable but single-writer role profiles
+ explicit scoped/fresh QMD retrieval
+ task-bounded host-persistent Docker execution
+ reviewed procedural spillover only
+ atomic reconstructible portfolio status
+ observable deterministic scheduling
+ no hidden pilot-state inheritance
+ no unnecessary subsystem
```

Antigravity is discarded as an implementation dependency after realization if desired; the resulting Hermes/Apex architecture must remain operable from its own durable repository/runtime contracts.

## 11. Operator launch instruction

When implementation is explicitly authorized, give Antigravity this command-oriented start instruction:

```text
Repository: leela-spec/apexai-os-meta
Branch: main

Execute:
apex-meta/epics/hermes-multi-repo-orchestration-v2/15-IMPLEMENTATION-ROADMAP-v2-ANTIGRAVITY.md

Read it completely first.
Treat D01-D10 as locked architecture.
Use 11-IMPLEMENTATION-ROADMAP.md only as referenced v1 technical detail.
Use validation/independent-preimplementation-review/04-CORRECTION-PLAN.md as mandatory acceptance input.

Work directly on main. No branches, PRs, or worktrees.
Existing control files: exact-match patches only; never whole-file rewrite.
New files may be created directly.
One major phase per context.
Persist implementation-state and one compact evidence file per phase.
Refresh current upstream/runtime syntax immediately before each mutation phase.
Do not add custom infrastructure when an upstream mechanism fails; record PHASE_BLOCKER.
Do not enable D10 without explicit operator approval after P17 passes.
Continue through routine technical decisions without asking for approval; stop only at the human gates defined in the v2 plan.
```
