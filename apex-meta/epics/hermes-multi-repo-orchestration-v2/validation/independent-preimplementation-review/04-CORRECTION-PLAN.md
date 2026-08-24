# 04 — Minimum Correction Plan Before Implementation Authorization

- **Program:** Hermes Multi-Repo Orchestration v2
- **Verdict input:** `REVISE`
- **Scope:** corrections to implementation acceptance only; no D01–D10 redesign
- **Execution in this review:** none. All changes below are requirements for the authorized implementation phase.

## Governing principle

**INFERENCE:** the architecture does not need another subsystem. The minimum correction set makes the existing upstream-native design fail closed at the exact places where legacy pilot state or current Hermes defects could produce false success.

---

## C01 — Task-scoped Docker workspace and persistence contract

**Priority:** P0 / implementation blocker  
**Evidence:** `SOURCE_VERIFIED`

### Problem

The MasterOfArts pilot used static `/root/MasterOfArts` binds. Current open Hermes issues `#73556`, `#83856`, and `#91568` show that task workspace precedence, container cwd mapping, and host-backed persistence remain active risk areas.

### Required correction

Before any repository executes through Hermes Docker:

1. resolve the task's authorized host workspace from the active repository/task;
2. verify the effective Docker bind list contains that workspace and no sibling repository or stale MasterOfArts mount;
3. verify the container cwd maps to the corresponding mounted path;
4. reject profile `terminal.cwd` or other configuration that changes the task workspace boundary;
5. perform a disposable host-persistence test: write a canary and, where safe, a disposable Git commit inside the worker; verify both from the host after worker/container exit;
6. record the resolved mount/cwd/persistence receipt with the task acceptance evidence.

### Fail-closed rule

If the installed Hermes release cannot express a safe task-scoped host-backed workspace with documented/native configuration, stop the phase. Do not add a custom mount router or wrapper to make the architecture appear to pass.

### Acceptance

- exact authorized workspace only;
- no static `/root/MasterOfArts` mount when another repo is active;
- no sibling-repo mount;
- host receives worker artifact/commit after exit;
- terminal, file tools and execute-code observe the same workspace.

---

## C02 — Normal-user WSL workspace and ownership normalization

**Priority:** P0 before repository migration  
**Evidence:** `SOURCE_VERIFIED`

### Problem

The pilot proved a working `/root/MasterOfArts` stack, while D07 intentionally targets normal-user `~/workspaces`. Reusing root-owned paths creates unnecessary privilege and permission coupling.

### Required correction

1. choose the normal WSL operator account used for Hermes/QMD/Git;
2. use `~/workspaces/<repo>` as the canonical root pattern;
3. verify repository files, QMD cache/config, Hermes runtime state and Docker bind source paths are readable/writable by the intended user without routine `sudo`;
4. record UID/GID and ownership of each canonical checkout and relevant runtime directory;
5. remove hard-coded `/root/MasterOfArts` assumptions from target configuration before cross-repo activation;
6. retain the existing D07 divergence audit before any Windows checkout is frozen or declared non-authoritative.

### Deliberate narrowing of prior review

Do **not** establish `umask 022` as an architecture requirement merely because the first review suggested it. Use the filesystem/user/group policy needed by the installed environment and prove the actual operations.

### Acceptance

Normal Git, QMD, Hermes task operations and Docker host persistence succeed as the normal user with no unexpected root ownership.

---

## C03 — Atomic, fail-closed Apex rollup publication

**Priority:** P0 before first portfolio rollup  
**Evidence:** `STATIC_SIMULATION`

### Problem

A derived portfolio view can become false authority if one board/repo read fails and the script publishes a partial snapshot.

### Required correction

The deterministic rollup must:

1. load the managed repository registry from current authority;
2. for every configured repo validate `repo`, expected branch, current source HEAD, configured board slug, and structured board query success;
3. reject duplicate/missing repo or board identities;
4. build a complete candidate snapshot in memory or a temporary file;
5. validate snapshot schema/completeness;
6. atomically replace the published snapshot only after all inputs pass;
7. on any failure preserve the prior good snapshot and emit a separate degraded health receipt naming the failing source;
8. include source HEADs and generation time in the published artifact.

### Acceptance

Inject one failed source query and prove the last-known-good snapshot remains unchanged. Inject a wrong board slug and prove publication fails even if an upstream bind command returned exit 0.

---

## C04 — QMD refresh receipt bound to source Git HEAD

**Priority:** P0 before high-stakes QMD-backed decisions  
**Evidence:** `STATIC_SIMULATION`

### Problem

`qmd status` proves index health, not that a collection represents the current Git commit. Timestamp comparison alone is insufficient because clocks, partial updates, or unrelated file changes can mislead.

### Required correction

After successful refresh of a managed collection, record a small deterministic receipt containing at least:

```text
collection
source_repo
source_branch
source_head_sha
qmd_version
refresh_completed_at
qmd_update: pass
embedding_state: current | not_required
collection_status: healthy
```

For a high-stakes retrieval task:

1. resolve current source HEAD;
2. compare it with the collection's last successful refresh receipt;
3. if mismatched/absent, run native `qmd update`, required `qmd embed`, validate `qmd status`, then replace the receipt;
4. issue the query only with the explicitly authorized `collections: [...]` list.

The receipt is operational derived state, not project truth and not a new KB.

### Acceptance

Advance a disposable source commit after a successful refresh and prove the pre-query gate detects the mismatch before synthesis.

---

## C05 — Reusable-profile state reset and classification

**Priority:** P0 before reusing any pilot role across repositories  
**Evidence:** `SOURCE_VERIFIED`

### Problem

The pilot proved useful profile reuse, but `AUTONOMOUS_LEARNINGS_SUMMARY.md` records project-work schedules (05:00/06:00/08:00) in Hermes `USER.md`. Current Hermes tenant/board behavior does not supply memory isolation.

### Required correction

Do not copy the pilot role homes wholesale into the multi-repo baseline. For each reusable profile:

1. reconstruct/review the thin role definition from the accepted role contract;
2. classify every persistent `USER.md`/`MEMORY.md` entry as stable operator preference, stable role procedure, project fact, project schedule/task state, or unknown;
3. keep only stable non-project preferences appropriate to that profile;
4. move no project fact into another memory store; project facts remain in source repos;
5. remove task schedules/milestones from reusable profile memory; scheduler/work state belongs to explicit orchestration/task state;
6. verify no profile config contains repo-specific `terminal.cwd`, static volumes, repository credentials, or project-specific QMD defaults;
7. start the multi-repo role with a clean baseline and observe learning under D04 rules.

### Acceptance

A deterministic/independent scan of profile files finds no managed repo name/path, project schedule, task identifier, or project fact except an explicitly approved generic operator preference.

---

## C06 — Skill scope, precedence, and provenance reset

**Priority:** P0 before role discovery across multiple repositories  
**Evidence:** `SOURCE_VERIFIED`

### Problem

MasterOfArts P11/P12 recorded global Hermes copies of BMAD and MarketingSkills as well as project copies, and the autonomous summary lists BMAD/MarketingSkills among learned skills. D06 now intentionally scopes these capabilities.

### Required correction

1. inventory all active skill roots visible to each reusable profile: bundled/hub, profile-local, external/global, and current project root;
2. label every non-bundled skill by canonical source, version/commit/hash, intended scope, and owner;
3. disable/remove stale or learned same-name copies that can shadow the approved source;
4. enforce D06 target:
   - BMAD: repo-local only where explicitly used;
   - MarketingSkills: MasterOfArts-only until another repo has an approved need;
   - Apex KB: Apex-only;
   - Apex reviewed shared skills: one canonical Apex source plus a verified runtime deployment path;
5. never “adopt” an upstream project package as a learned skill merely to make it globally available;
6. validate actual skill discovery from at least two distinct reusable roles and two repositories.

### Acceptance

For each repo/profile pair, produce the active skill inventory and prove it matches the capability registry with no same-name ambiguous source.

---

## C07 — Docker environment/credential negative test

**Priority:** P0 security blocker  
**Evidence:** `SOURCE_VERIFIED`

### Problem

Filesystem mount isolation is not proof that environment secrets are isolated. The pilot observation explicitly identified parent-process environment inheritance risk.

### Required correction

1. use current installed Hermes documentation/schema for Docker environment forwarding;
2. default to an empty or minimal explicit `docker_forward_env` allowlist;
3. create harmless canary host variables representing unrelated credentials;
4. execute a disposable worker and enumerate only names/values required for the test;
5. prove canaries absent unless explicitly allowlisted;
6. prove required task-specific variables can be forwarded intentionally;
7. ensure QMD and source-repo credentials are not forwarded to action containers unless a task explicitly requires them.

### Acceptance

Negative canary test passes on every reusable execution profile before repository activation.

---

## C08 — Repository context-entry and authority-routing preflight

**Priority:** P1 before each repository board becomes active  
**Evidence:** `SOURCE_VERIFIED`

### Problem

The architecture expects root-to-workdir project context. Current inspection found no root `AGENTS.md` in `acim-secular` or Investment; Apex has a root `AGENTS.md` focused mainly on Codex dispatch/Apex KB rather than the Hermes portfolio runtime.

### Required correction

For each managed repository:

1. identify the current authoritative human/project entrypoint(s);
2. identify which upstream context filename/path Hermes will actually consume at repo root;
3. add or adapt only the minimal routing/invariant context required to point to those owners;
4. keep project fact bodies in existing authoritative files; do not duplicate them into context;
5. verify from the intended workdir that the expected root/family chain is discovered and that unrelated repo context is absent;
6. record size/token budget and keep automatic context concise.

### Acceptance

Cold-start role in each repo can answer “what owns current truth and what must I not treat as truth?” using the automatic/explicit routing chain without repository-wide exploration.

---

# Acceptance checks already required by existing architecture

These are important but do not justify additional correction IDs because current D01–D10/state already specify them.

## A01 — Default branch registry

**SOURCE_VERIFIED:** `acim-secular=master`; Apex/MasterOfArts/Investment=`main`. Every script/receipt resolves branch from the managed-repo registry and fails on mismatch.

## A02 — Board existence and identity

**SOURCE_VERIFIED:** due to Hermes `#76285`, validate configured board slug against live board enumeration; do not trust a successful bind command alone.

## A03 — Same-profile single-process rule

**SOURCE_VERIFIED:** D03/D10 remain controlling. Before D10, one writable role profile has at most one active worker across all boards.

## A04 — No-agent scheduler observability

**SOURCE_VERIFIED:** if deterministic unattended jobs are later used, `#20353` requires explicit success/heartbeat/last-run evidence. Absence of output is not accepted as success.

## A05 — D10 remains disabled

**SOURCE_VERIFIED:** single-repo MasterOfArts P15/P16 does not satisfy multi-board D10 acceptance. D10 requires exact installed-version multi-board tests before any enablement decision.

## A06 — Evidence-label discipline

Prior durable runtime receipts may be cited as `SOURCE_VERIFIED` evidence of prior execution. A reviewer may use `EXECUTED` only for a check it actually performed against the current runtime in that run.

---

# Sequencing

1. Apply/verify **C05+C06** before reusing pilot roles or skill roots.
2. Establish **C02+C08** while onboarding each canonical repository workspace.
3. Prove **C01+C07** before the first Docker-backed task in each repo/profile lane.
4. Implement/verify **C03** before publishing the first multi-repo Apex rollup.
5. Implement/verify **C04** before high-stakes multi-repo QMD retrieval.
6. Run existing D01–D09 roadmap acceptance in Safe Mode A.
7. Keep D10 disabled until its independent acceptance program passes.

# Stop conditions

Stop and return to the operator if:

- current upstream behavior contradicts a locked architecture requirement;
- native Hermes cannot provide a safe task workspace without custom middleware;
- source reconciliation finds unresolved divergent canonical work;
- profile cleanup would destroy information that cannot be confidently classified;
- skill provenance is ambiguous and the active runtime cannot show which copy wins;
- any D10 acceptance test fails when D10 is eventually reconsidered.

**INFERENCE — minimum-change conclusion:** these corrections harden the accepted architecture without creating another architecture layer. That is the intended outcome of `REVISE`.
