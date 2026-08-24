# 11 — Hermes Multi-Repo v2 Implementation Roadmap

Status: **V1 TECHNICAL PHASE CATALOG / SUPERSEDED AS EXECUTION AUTHORITY BY `15-IMPLEMENTATION-ROADMAP-v2-ANTIGRAVITY.md` / IMPLEMENTATION NOT AUTHORIZED**  
Date: 2026-08-24

> Preservation rule: keep this file intact as detailed v1 technical planning evidence. The v2 plan imports useful phase detail from this file but governs execution order, Antigravity behavior, validation corrections, and patch-only mutation law.

## Target outcome

One machine-level Hermes environment serving four separate repositories with:

- hard repo-level Kanban board separation;
- one canonical WSL checkout per repo;
- reusable role profiles used sequentially across repos;
- one local QMD engine with explicit repo collection scopes;
- Docker execution isolation proven against each actual workspace mode;
- asynchronous deterministic Apex status rollup;
- delayed reviewed procedural-learning promotion;
- repo-local BMAD/domain skills where required;
- no raw-memory synchronization;
- no dependency on Antigravity.

## Implementation law

```text
PROVE ONE LANE
  -> PROVE SECOND REPO
  -> PROVE CROSS-REPO ROLE REUSE
  -> PROVE QMD SCOPING
  -> PROVE STATUS ROLLUP
  -> PROVE LEARNING PROMOTION
  -> ONBOARD REMAINING REPOS
  -> ONLY THEN CONSIDER BACKGROUND AUTONOMY
```

Do not configure everything at once.

## Two runtime modes

### MODE A — initial safe v2

```text
one active repo at a time
background Kanban dispatch OFF
operator/orchestrator selects explicit repo/board
reusable role runs sequentially
Docker CWD/mount verified
QMD collections explicit
```

Purpose: avoid current cross-board concurrency and Kanban/Docker workspace bugs while proving the architecture.

### MODE B — later autonomous v2

```text
multiple boards persisted
background dispatcher allowed
Kanban task-scoped Docker workspace proven host-backed
machine-wide profile concurrency control proven
```

MODE B is forbidden until its gates pass on the installed Hermes version.

---

# Phase 0 — Preserve MasterOfArts pilot evidence

**Owner:** executor  
**Mutations:** Apex docs only  
**Goal:** make sure architecture provenance survives migration.

Inputs:

- `02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md`
- MasterOfArts implementation acceptance/evidence.

Actions:

1. verify every manifest path exists at current MasterOfArts HEAD;
2. classify each artifact:
   - architecture authority;
   - research provenance;
   - implementation evidence;
   - historical/obsolete;
3. decide copy vs move vs pointer for Apex control-plane history;
4. preserve source commit SHAs;
5. do not delete originals yet.

Output:

```text
Apex migration receipt with source repo/path/SHA and destination/pointer
```

Gate:

```text
P0_PASS = no architecture/evidence file can be lost or silently rewritten
```

---

# Phase 1 — Runtime/version preflight

**Goal:** refresh all syntax against installed current versions before touching config.

Record:

```yaml
hermes_version:
qmd_version:
docker_version:
wsl_version:
ubuntu_version:
node_version:
git_version:
claude_version_if_installed:
codex_version_if_installed:
```

Check current upstream:

- Hermes release/changelog/docs;
- QMD release/changelog/docs;
- open issues relevant to Kanban, Docker, memory, cron, MCP;
- BMAD current installer only when a repo will use it.

Gate:

```text
P1_PASS = current installed behavior/syntax known
```

No architecture command may rely only on this planning document.

---

# Phase 2 — Disable unsafe background orchestration during migration

**Goal:** ensure no profile or repo receives background writes while paths/boards are changing.

Actions:

1. inspect current Hermes gateway/Kanban dispatcher configuration;
2. disable automatic all-board dispatch and auto-decomposition for migration window using current supported settings;
3. list current processes/jobs/cron;
4. pause any job that writes MasterOfArts or future managed repos;
5. keep read-only status collection allowed.

Candidate desired semantics:

```yaml
kanban:
  dispatch_in_gateway: false
  auto_decompose: false
```

Verify actual installed keys before edit.

Gate:

- no autonomous worker can start unexpectedly;
- no same profile can run in two projects during migration.

---

# Phase 3 — WSL workspace pilot on ACIM

**Goal:** validate canonical workspace migration on lowest-risk repo first.

Use `09-WSL-CANONICAL-WORKSPACE-MIGRATION-PLAN.md`.

Actions:

1. inventory Windows + any WSL ACIM copies;
2. compare remote/branch/HEAD/dirty/untracked/local files;
3. preserve ACIM default branch `master`;
4. reconcile differences;
5. create/verify canonical `~/workspaces/acim-secular`;
6. open from Windows Explorer via `\\wsl.localhost`;
7. run ACIM deterministic pipeline/test baseline;
8. freeze old Windows live copy, do not delete.

Gate:

```text
P3_PASS = one canonical ACIM checkout with no lost local state
```

---

# Phase 4 — Create isolated repo boards

Boards:

```text
apex
masterofarts
acim
investment
```

Actions:

1. create board if missing;
2. verify `boards list --json`;
3. inspect actual DB path per board;
4. create one disposable task in each;
5. query explicitly using `--board`;
6. prove task link across boards is rejected;
7. delete/archive disposable tasks according to supported behavior.

Do not use tenants as security/memory isolation.

Gate:

```text
P4_PASS = four hard-isolated board stores/query surfaces
```

---

# Phase 5 — Create native Hermes Projects cautiously

Create one project per repo where current Hermes Projects behavior is useful:

```text
apex          -> ~/workspaces/apexai-os-meta -> board apex
masterofarts  -> ~/workspaces/MasterOfArts   -> board masterofarts
acim          -> ~/workspaces/acim-secular   -> board acim
investment    -> ~/workspaces/Investment     -> board investment
```

Before `bind-board`:

```text
verify board exists
```

After binding:

```text
hermes project show <slug>
verify primary folder + board
```

Do not trust command exit 0 alone because current upstream issue #76285 documents dangling board bindings.

Gate:

```text
P5_PASS = every project references an existing folder + existing board
```

---

# Phase 6 — QMD machine-level registry pilot

**Goal:** prove QMD access from ACIM without Apex checkout.

Actions:

1. inspect current QMD global index config;
2. preserve existing MasterOfArts collections;
3. add minimal ACIM collections:
   - `acim-control`;
   - `acim-site-docs`;
   - `acim-site-code` only if needed;
4. give meaningful collection context;
5. mark large project collections excluded from default search;
6. update/embed/status;
7. benchmark current/stale/source questions.

Gate:

- `qmd query -c acim-control ...` works from ACIM cwd;
- same named collection works from another cwd;
- unscoped query does not search excluded corpora;
- current authority retrieval passes.

---

# Phase 7 — QMD availability per reusable profile

For each profile that genuinely needs retrieval:

```text
research-strategist
independent-reviewer
portfolio-orchestrator (new or existing)
```

Do not automatically add QMD to every profile.

Actions:

1. configure native QMD MCP in profile;
2. start fresh session;
3. verify MCP tool discovery automatically;
4. query ACIM explicit collection;
5. confirm no QMD skill load was needed for normal MCP use;
6. repeat for second selected profile.

Optional after manual success:

- test Apex-controlled profile distribution carrying the same MCP declaration while preserving local memory/session/auth.

Gate:

```text
P7_PASS = same local QMD engine accessible to intended profiles independent of cwd
```

---

# Phase 8 — Docker execution boundary on direct sequential repo work

**Goal:** prove reusable role can safely act in ACIM without Kanban task-scoped Docker dependency.

Use a disposable branch/workspace only if repo policy permits; otherwise use disposable untracked test artifact and remove it.

Actions:

1. launch Hermes explicitly from canonical ACIM repo with reusable test role;
2. inspect effective Docker mount and cwd;
3. create disposable file;
4. verify file exists host-side;
5. if allowed, make disposable Git commit and verify host-side;
6. verify terminal/file/execute_code use same workspace;
7. verify unrelated host paths are absent;
8. verify secrets not forwarded unnecessarily.

Do not use a profile-level fixed repo `terminal.cwd`.

Gate:

```text
P8_PASS = direct repo execution is host-persistent and bounded
```

---

# Phase 9 — Sequential reusable-role test across ACIM -> Investment

Before phase:

- migrate/verify Investment canonical WSL checkout using Phase 3 process.
- configure Investment minimal QMD collections.

Test:

```text
research-strategist
  task A in ACIM
  completes
  inspect memory/learned skill changes

then

research-strategist
  task B in Investment
  completes
```

Required observations:

- no concurrent profile process;
- repo AGENTS/context switches correctly;
- QMD scope switches explicitly;
- ACIM facts do not appear as Investment authority;
- generic procedure can remain available;
- project outputs stay in source repos.

Gate:

```text
P9_PASS = reusable role across two repos without factual contamination
```

This is the decisive D03/D04 proof.

---

# Phase 10 — Learning promotion pilot

Use `06-SHARED-SKILL-PROMOTION-AND-CRON.md`.

Create two controlled candidates:

```text
Candidate A = genuinely generic procedure
Candidate B = intentionally project-specific procedure/fact
```

Process:

1. deterministic candidate scanner hashes local learned skills;
2. unchanged second scan emits no duplicate;
3. reviewer classifies A/B;
4. A promoted to disposable Apex shared-skill candidate;
5. B remains local/rejected;
6. deploy A to test runtime skill directory;
7. another role/session discovers A;
8. no raw MEMORY copied.

Run manually first.

Gate:

```text
P10_PASS = useful spillover without project-fact or memory synchronization
```

---

# Phase 11 — Apex read-only portfolio rollup pilot

Use `04-KANBAN-TOPOLOGY-AND-APEX-ROLLUP.md` and `07-APEX-CROSS-PROJECT-EXCHANGE-CONTRACT.md`.

Input:

```text
four explicit `hermes kanban --board <slug> list --json` calls
```

Actions:

1. define normalized schema;
2. parse all four board outputs;
3. fail entire run if configured board query fails;
4. emit current snapshot with source timestamp;
5. rerun unchanged source and compare deterministic semantics;
6. verify source boards unchanged.

Then create one manual cross-repo Apex dependency/escalation object referencing two source task IDs.

Gate:

```text
P11_PASS = Apex daily portfolio view is rebuildable and read-only
```

---

# Phase 12 — Schedule rollup and candidate harvest

Only after manual deterministic runs pass.

Options to test:

```text
A. Hermes no-agent cron
B. WSL systemd timer / OS scheduler
```

Decision criteria:

- zero model calls;
- visible nonzero failure;
- persists restart;
- idempotent;
- health receipt;
- simple operator inspection;
- no broad repo write authority.

Do not pick Hermes Cron merely because it is inside Hermes. Pick the simpler mechanism that passes the actual reliability test.

Initial cadence:

```text
portfolio rollup: on-demand + daily
learning harvest: daily or end-of-batch
semantic promotion review: only when candidates exist
```

Gate:

```text
P12_PASS = scheduled jobs prove last-success/failure visibility across restart
```

---

# Phase 13 — Migrate MasterOfArts canonical workspace

This repo already has a WSL Hermes pilot and a Windows copy.

Special process:

1. compare both complete Git states;
2. identify files generated since pilot acceptance in either copy;
3. reconcile before declaring one canonical;
4. remove any old WSL path hard-coding from role/profile definitions;
5. repoint QMD collection paths if needed;
6. verify MasterOfArts board;
7. preserve MarketingSkills MasterOfArts-only;
8. preserve BMAD project-local installation;
9. rerun a small known-good MasterOfArts task.

Gate:

```text
P13_PASS = no more bidirectional Windows<->WSL synchronization requirement
```

---

# Phase 14 — Migrate Apex canonical workspace

Migrate last because Apex is both managed repo and control plane.

Actions:

1. full dirty/untracked/divergence audit;
2. verify existing Apex KB skill authority;
3. reconcile current Windows work;
4. establish canonical WSL checkout;
5. configure minimal `apex-control` QMD collection; do not index giant history wholesale;
6. create Apex board/project;
7. verify root AGENTS behavior;
8. separately solve Apex-KB cross-client skill path without duplicate drift.

Gate:

```text
P14_PASS = control plane operational from canonical checkout
```

---

# Phase 15 — BMAD/domain-skill normalization

Per `10-BMAD-AND-DOMAIN-SKILL-POLICY.md`:

- MasterOfArts MarketingSkills remains local;
- BMAD remains per project where needed;
- Apex KB remains Apex-specific;
- ACIM/Investment receive only skills justified by their real workflows;
- generic approved procedures use Apex shared-skill channel.

Produce desired-state registry, no mass install.

---

# Phase 16 — Full cross-repo recovery test

Scenario:

1. all four boards contain representative persisted tasks;
2. one role has worked ACIM then Investment sequentially;
3. QMD has scoped collections;
4. Apex rollup exists;
5. one shared procedure has been promoted;
6. stop Hermes/QMD/WSL cleanly or simulate the approved restart condition;
7. restart;
8. verify every source of state independently.

Verify:

```text
Git repos
boards
QMD index/status
profile local memory
shared-skill deployment
Apex rollup freshness
scheduled-job health
```

No chat replay should be required to reconstruct operational state.

---

# Phase 17 — Decide whether to enable Kanban background dispatch

This is an explicit **post-v2-safe-mode decision**, not automatic.

Research current Hermes version/issues again.

Required before enabling:

1. task-scoped Docker workspace is actually host-backed;
2. profile `terminal.cwd` cannot override task mount;
3. container cwd provenance mapping is correct;
4. global/per-profile worker cap semantics across boards are known;
5. same reusable role cannot be concurrently written from multiple boards;
6. worker swarm limits have live tests;
7. recovery/cleanup tested.

If any fail:

```text
KEEP SAFE MODE A
```

That is a valid production operating mode because the user does not require simultaneous cross-repo autonomous work.

---

# Phase 18 — Final acceptance report

Allowed verdicts:

```text
MULTI_REPO_V2_PASS_SAFE_SEQUENTIAL
MULTI_REPO_V2_PASS_WITH_AUTONOMOUS_DISPATCH
MULTI_REPO_V2_BLOCKER
```

Report:

- actual versions;
- canonical repo paths;
- board paths;
- QMD collections/profile connections;
- Docker mount/isolation evidence;
- reusable role test;
- learning-promotion test;
- Apex rollup test;
- cron/scheduler health;
- BMAD/domain-skill locations;
- known upstream issues still open;
- future-development items.

## Stop conditions

Stop and require human decision only when:

- reconciling divergent uncommitted data;
- deleting/freezing old canonical-looking checkout;
- provider/privacy class changes;
- moving authoritative Apex-KB skill source;
- background dispatch would weaken tested safety;
- upstream behavior contradicts an accepted invariant.

Routine commands/research/verification do not require operator micro-approval.

## Success metric

Not:

```text
"all tools installed"
```

Success is:

```text
one durable portfolio control plane
+ four independent project truths
+ reconstructible status
+ reusable but non-concurrent agents
+ local scoped retrieval
+ delayed reviewed learning spillover
+ one canonical filesystem per repo
+ proven Docker persistence/isolation
+ no custom synchronization framework beyond small deterministic rollups
```
