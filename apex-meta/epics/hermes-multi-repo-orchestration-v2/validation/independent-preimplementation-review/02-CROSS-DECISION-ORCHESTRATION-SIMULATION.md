# 02 — Cross-Decision Orchestration Simulations

- **Program:** Hermes Multi-Repo Orchestration v2
- **Mode:** static adversarial simulation against current source and upstream evidence
- **Evaluation date:** 2026-08-24
- **Rule:** no scenario below is treated as live runtime execution unless explicitly marked `EXECUTED`. This run performed no WSL/Hermes shell execution.

## Simulation contract

Each scenario records the intended path, injected fault, expected invariant, and verdict. These are `STATIC_SIMULATION` unless a supporting upstream or repository fact is explicitly marked `SOURCE_VERIFIED`.

---

## S01 — Healthy morning portfolio rollup

**Path:** four repository boards -> deterministic reads -> Apex derived snapshot.

- **STATIC_SIMULATION — setup:** all four configured boards exist and return valid structured state; source branches and Git HEADs resolve.
- **Expected:** snapshot contains every configured source, exact source identity, generation timestamp, and health=healthy.
- **Invariant:** no source task/project content is copied into Apex beyond the declared rollup schema.
- **Verdict:** **PASS** if C03 atomic publication is used.

## S02 — one board read fails mid-rollup

- **STATIC_SIMULATION — fault:** Apex reads MasterOfArts and Investment successfully; ACIM board read errors; Apex board is still readable.
- **Unsafe behavior:** publish a three-board “success” snapshot.
- **Expected:** abort replacement, preserve last-known-good snapshot, emit a degraded receipt naming ACIM read failure.
- **Verdict:** **FAIL without C03 / PASS with C03.**

## S03 — source repo advances during rollup

- **STATIC_SIMULATION — fault:** board status is read against source SHA A; before publication the source branch advances to B.
- **Expected:** snapshot declares SHA A rather than pretending it reflects B. A downstream high-stakes decision refreshes if current HEAD != snapshot source SHA.
- **Verdict:** **PASS_WITH_CONDITION** — source SHA is mandatory provenance.

## S04 — sequential reusable profile: Investment -> ACIM

- **SOURCE_VERIFIED — risk basis:** Hermes tenant/board isolation does not isolate shared profile memory (`#85497`).
- **STATIC_SIMULATION — sequence:** `research-strategist` completes an Investment task, then starts ACIM after process completion.
- **Expected:** role definition remains the same, but task workdir/context/QMD scope switch to ACIM; no Investment project fact or schedule is injected from persistent profile memory.
- **Failure detector:** preflight scans reusable profile memory/config for repo names, source paths, task schedules, `terminal.cwd`, and repo-specific mounts.
- **Verdict:** **FAIL until C05 profile reset is complete.**

## S05 — accidental same-profile concurrency on two boards

- **SOURCE_VERIFIED — risk basis:** `#78122` allows per-board limits to multiply workers; `#85497` documents shared profile-memory contamination.
- **STATIC_SIMULATION — fault:** both Investment and ACIM have ready tasks assigned to `research-strategist` at the same time.
- **Expected Safe Mode A:** only one can enter execution; the second stays queued/blocked.
- **Verdict:** **PASS only while D10 remains disabled and a single-profile/single-lane guard is effective.**

## S06 — legacy static MasterOfArts Docker volume survives

- **SOURCE_VERIFIED — pilot evidence:** P07 and `OKF-EXECUTION-OBSERVATIONS.yaml` record `/root/MasterOfArts` mounted to both `/root/MasterOfArts` and `/workspace`.
- **STATIC_SIMULATION — fault:** an Investment task starts with that configuration unchanged.
- **Expected:** preflight rejects execution before any command; container must not receive MasterOfArts as the active workspace.
- **Verdict:** **FAIL until C01.**

## S07 — profile `terminal.cwd` overrides task workspace

- **SOURCE_VERIFIED — risk basis:** Hermes issue `#73556` remains open.
- **STATIC_SIMULATION — fault:** task workspace is `~/workspaces/acim-secular`, profile cwd is a broader parent or another repo.
- **Expected:** task workspace is authoritative; if effective mount/cwd differs, worker fails closed before command execution.
- **Verdict:** **BLOCKER on any installed-version reproduction.** Do not compensate with a custom wrapper.

## S08 — Docker worker reports commit but host lacks artifact

- **SOURCE_VERIFIED — risk basis:** `#91568` documents task Docker workspaces that are not host-backed, allowing apparent commits to disappear after container exit.
- **STATIC_SIMULATION — test:** worker writes a canary file and creates a disposable commit in an authorized test checkout; container exits; host verifies exact file/commit.
- **Expected:** host sees both before task may report success.
- **Verdict:** **D10 acceptance must fail if host receipt is absent.**

## S09 — ambient credential leaks into Docker

- **SOURCE_VERIFIED — pilot evidence:** `OKF-EXECUTION-OBSERVATIONS.yaml` records environment inheritance as a risk in Hermes 0.20.5.
- **STATIC_SIMULATION — test:** host process exposes a harmless canary variable that is not on the explicit forward allowlist.
- **Expected:** canary absent inside container; required named variables only are present.
- **Verdict:** **FAIL until C07 negative test passes.**

## S10 — QMD scoped Investment retrieval

- **STATIC_SIMULATION — setup:** query is issued with explicit Investment collection(s); ACIM and MasterOfArts are excluded from the request/default heavy set.
- **Expected:** results contain only authorized Investment paths; exact files may then be fetched with `get`/`multi_get`.
- **Verdict:** **PASS by design; requires live collection-isolation acceptance.**

## S11 — QMD stale after source commit

- **STATIC_SIMULATION — fault:** Investment HEAD advances A -> B after previous QMD refresh; index remains healthy but reflects A.
- **Expected:** pre-query high-stakes gate compares current HEAD B with refresh receipt A and forces `qmd update` plus required embedding refresh before synthesis.
- **Verdict:** **FAIL without C04 / PASS with C04.**

## S12 — learned procedure promoted from project A to project B

- **STATIC_SIMULATION — flow:** a task creates a learned skill candidate in a profile; deterministic inventory detects changed candidate; independent review removes project facts and checks overlap; accepted procedure is committed to Apex shared-skill source; runtime deployment is hash/provenance verified; Project B activates it on demand.
- **Expected:** no source-project paths, facts, credentials, schedules, or hidden memory move with the procedure.
- **Verdict:** **PASS_WITH_CONDITIONS C05+C06.**

## S13 — stale global BMAD/MarketingSkills shadows repo policy

- **SOURCE_VERIFIED — pilot evidence:** P11/P12 record global Hermes copies in addition to MasterOfArts project copies; the autonomous summary lists BMAD/MarketingSkills under learned skills.
- **STATIC_SIMULATION — fault:** ACIM profile discovers a global MarketingSkills/BMAD copy despite D06 saying those capabilities are not globally owned.
- **Expected:** skill inventory gate rejects target activation until ambiguous/shadowing copies are disabled or removed; active capability set is explicit per repo.
- **Verdict:** **FAIL until C06.**

## S14 — cross-project dependency without cross-board native edge

- **STATIC_SIMULATION — flow:** Investment task blocks a MasterOfArts task. Source-side Investment task stays blocked; Apex XDEP record carries source refs and dependency state; periodic deterministic rollup sees Investment completion; operator/orchestrator creates or unblocks the explicit downstream task according to the declared process.
- **Expected:** no hidden bidirectional synchronization and no copied task becomes a second owner.
- **Verdict:** **PASS**; asynchronous coupling is intentional.

## S15 — board binding typo returns success

- **SOURCE_VERIFIED — risk basis:** Hermes `#76285` remains open.
- **STATIC_SIMULATION — fault:** configuration says `investmentt` instead of `investment` and upstream binding command exits 0.
- **Expected:** orchestration preflight independently enumerates real boards and rejects nonexistent configured slug.
- **Verdict:** **PASS only with explicit existence validation.**

## S16 — no-agent scheduler silently produces no evidence

- **SOURCE_VERIFIED — issue state:** `#77131` and `#80624` are closed; `#20353` remains open regarding silent no-agent output/failure visibility.
- **STATIC_SIMULATION — fault:** deterministic harvest script catches an exception or produces no output while exit semantics do not surface a useful failure.
- **Expected:** scheduled job has an explicit success receipt/heartbeat and last-run verification; absence is unhealthy, not success.
- **Verdict:** **scheduler remains non-authoritative and D10-disabled until acceptance covers this.**

## S17 — restart during single-repo task

- **SOURCE_VERIFIED — pilot:** P16 reports WSL cold-restart preservation for Kanban, QMD, profiles, memory, Docker recovery, and Git cleanliness in MasterOfArts.
- **STATIC_SIMULATION — multi-repo extension:** crash occurs with exactly one active Safe Mode A task. On restart, validate board/task state, repo path/branch/HEAD, task artifact existence, profile lock release, and QMD freshness before resuming.
- **Expected:** resume from durable state, not chat transcript; no duplicate side effect.
- **Verdict:** **PASS_WITH_CONDITIONS**; prior pilot supports mechanism but exact multi-repo run still requires acceptance.

## S18 — missing repository context entrypoint

- **SOURCE_VERIFIED — repository inspection:** root `AGENTS.md` was not found in `acim-secular` or `Investment`; Apex root `AGENTS.md` exists but primarily addresses Codex/Apex-KB behavior.
- **STATIC_SIMULATION — fault:** Hermes enters a repo expecting automatic root routing but no intentional Hermes-readable authority pointer exists.
- **Expected:** repository activation gate identifies current owner/authority entrypoint and adds/validates only the minimal upstream-consumed context required by D07/D08/D03; it must not create a new knowledge layer.
- **Verdict:** **FAIL until C08 per repo.**

## S19 — attempt to enable D10 early

- **STATIC_SIMULATION — fault:** operator/runtime tries to start unattended concurrent multi-board execution because single-repo P15/P16 passed.
- **Expected:** architecture gate rejects enablement; single-repo E2E/recovery is not evidence of multi-board concurrency, same-profile isolation, task-scoped mount safety, or scheduler correctness.
- **Verdict:** **HARD BLOCK.**

## S20 — token/context pressure

- **SOURCE_VERIFIED — external practice:** OpenAI favors simpler single-agent systems before multi-agent escalation; Anthropic emphasizes finite context and reports high token multiplication for multi-agent systems; Agent Skills/QMD use progressive disclosure.
- **STATIC_SIMULATION — flow:** portfolio task loads only Apex rollup + named repo authority + scoped QMD passages + activated skill, not all four repositories or all skill bodies.
- **Expected:** context expands only on a concrete unresolved question.
- **Verdict:** **PASS** and no new router/compressor is justified.

---

## Cross-simulation conclusion

**INFERENCE:** the dominant failure class is not missing architecture. It is **authority leakage through runtime state**: wrong mount, stale index, stale rollup, polluted reusable profile, or shadowing skill. The correction plan targets exactly these seams with deterministic checks and preserves the minimal upstream-native design.
