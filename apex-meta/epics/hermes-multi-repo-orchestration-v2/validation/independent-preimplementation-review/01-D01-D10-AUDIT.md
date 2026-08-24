# 01 — D01–D10 Independent Adversarial Audit

- **Program:** Hermes Multi-Repo Orchestration v2
- **Repository / branch:** `leela-spec/apexai-os-meta` / `main`
- **Evaluation date:** 2026-08-24
- **Prior review incorporated:** `49b716a21ee82b94fcd26a6adac7bb2809ad2303`
- **Evidence labels:** `EXECUTED`, `STATIC_SIMULATION`, `SOURCE_VERIFIED`, `INFERENCE`

## Evidence discipline

`EXECUTED` is reserved for a check performed in this independent run. This reviewer had repository/API/web access but no shell path into the installed WSL/Hermes runtime, so prior host runs are not relabeled as this reviewer's `EXECUTED`. Durable MasterOfArts phase receipts are `SOURCE_VERIFIED` evidence that those prior tests occurred and reported the recorded result.

---

## D01 — Apex as portfolio control plane

**Architecture claim:** Apex owns portfolio governance, shared orchestration contracts, cross-project dependency records, derived rollups, and reviewed shared skills; each source repository owns its project truth and Git history.

**Verdict:** **PASS_WITH_CONDITIONS**

- **SOURCE_VERIFIED — support:** D01, `01-VERIFIED-ARCHITECTURE.md`, and `state.yaml` consistently prohibit project-content mirroring into Apex and distinguish source truth from derived control-plane state.
- **SOURCE_VERIFIED — repository reality:** the four managed repositories have independent histories and branches; `acim-secular` uses `master`, while Apex, MasterOfArts, and Investment use `main`.
- **STATIC_SIMULATION — failure:** if a derived Apex portfolio snapshot is published after one source read failed, “missing” can be mistaken for “zero work” and become false control-plane truth.
- **INFERENCE — hidden coupling:** every rollup or cross-project decision that claims current source state needs immutable source identity (`repo`, `branch`, `head_sha`, board/task identifiers) and generation time.
- **Token/cost:** deterministic source reads and rollup generation require no model call; semantic review belongs only where a human-level synthesis is actually required.
- **Required mitigation:** C03 atomic fail-closed rollup plus source-SHA receipts.
- **Revisit trigger:** only if a proven upstream primitive provides transactional cross-repository state without copying project truth.

---

## D02 — separate repository boards + asynchronous Apex rollup

**Architecture claim:** use one Hermes board per managed repository; reject tenant namespacing as the memory/security boundary; aggregate board state read-only into Apex.

**Verdict:** **PASS_WITH_CONDITIONS**

- **SOURCE_VERIFIED — support:** Hermes issue `#85497` remains open and documents that `HERMES_TENANT` does not isolate profile memory. Separate boards isolate task databases and are therefore the safer task-state topology.
- **SOURCE_VERIFIED — limitation:** Hermes issue `#78122` remains open and shows `max_in_progress` is counted per board rather than gateway-wide. Board separation does not create a global concurrency safety boundary.
- **SOURCE_VERIFIED — false-success seam:** issue `#76285` remains open; project-to-board binding can accept a nonexistent board slug and exit success.
- **STATIC_SIMULATION — consequence:** four healthy board databases can still dispatch four same-profile workers concurrently unless the external operating mode prevents it. Therefore D02 depends on D03 sequential execution and D10 remaining disabled.
- **Token/cost:** a JSON rollup is deterministic and should remain zero-model-call.
- **Required mitigations:** C03; validate configured board existence before accepting a binding; preserve last-known-good rollup on partial failure.
- **Revisit trigger:** upstream resolves tenant memory isolation and provides a verified gateway-wide cross-board concurrency contract plus cross-board dependency semantics.

---

## D03 — reusable role profiles, sequentially reused

**Architecture claim:** profiles represent reusable roles rather than repositories; one writable profile must not serve concurrent workers.

**Verdict:** **PASS_WITH_CONDITIONS**

- **SOURCE_VERIFIED — support:** MasterOfArts P13 demonstrates that the same thin `marketing-executive` profile produced family-specific outputs in Lika and Dance Fusion without embedding those family facts in the profile definition.
- **SOURCE_VERIFIED — concurrency risk:** `#78122` and `#85497` jointly show why board/tenant state cannot protect one shared writable profile from simultaneous use.
- **SOURCE_VERIFIED — workspace risk:** `#73556` remains open and documents that profile `terminal.cwd` can override the Kanban task workspace and broaden a Docker mount.
- **SOURCE_VERIFIED — pilot-state contamination:** `AUTONOMOUS_LEARNINGS_SUMMARY.md` states that 05:00/06:00/08:00 project-work milestones were stored in Hermes `USER.md`. Those are not stable role identity/preferences and must not be inherited by a reusable cross-repository role.
- **STATIC_SIMULATION — failure:** `research-strategist` finishes Investment, writes Investment-specific memory, then starts ACIM. Even sequential use can contaminate ACIM if persistent memory contains project facts. Sequential execution solves write races, not semantic contamination.
- **Required mitigations:** C05 profile reset; no fixed `terminal.cwd`; no repo-specific Docker mounts; stable operator preference only in reusable profile memory.
- **Token/cost:** thin profile memory is small and recurring; project facts in profile memory create recurring token waste as well as correctness risk.
- **Revisit trigger:** only after upstream supplies verified scoped memory namespaces and same-profile concurrent safety on the deployed release.

---

## D04 — learning spillover through reviewed procedures, not raw memory

**Architecture claim:** project facts stay in repositories, raw memory stays profile-local, and only generalized reviewed procedures may spill across projects via skills.

**Verdict:** **PASS_WITH_CONDITIONS**

- **SOURCE_VERIFIED — support:** Agent Skills uses metadata-first progressive disclosure; full instructions/resources load only when selected. This is a suitable portable unit for reviewed procedure reuse.
- **SOURCE_VERIFIED — pilot tension:** P14 shows a learned procedural skill can persist, but the autonomous summary also lists `bmad-method` and `marketingskills` among the learned library. Upstream packages must not be silently reclassified as agent-learned procedures or allowed to shadow approved package copies.
- **STATIC_SIMULATION — promotion test:** a Lika-specific lesson containing file paths, organization names, customer facts, or task schedules is not reusable merely because it is phrased procedurally. Independent review must remove facts and prove generality before Apex promotion.
- **INFERENCE — batching:** delayed spillover is a benefit: it provides an explicit review boundary and prevents every task observation becoming permanent startup context.
- **Required mitigations:** C05 and C06. Hash-based candidate discovery may remain deterministic; semantic generalization happens only for changed candidates.
- **Revisit trigger:** measured evidence that reviewed-skill promotion is too slow or loses necessary reusable procedure despite correct use.

---

## D05 — Apex as canonical reviewed shared-skill source

**Architecture claim:** approved project-neutral shared skills have one canonical Git owner in Apex; runtime scratch/learned state remains separate.

**Verdict:** **PASS_WITH_CONDITIONS**

- **SOURCE_VERIFIED — support:** Git gives reviewable provenance, exact version identity, diff, and rollback. D05 correctly forbids direct runtime self-modification of the canonical Apex source.
- **SOURCE_VERIFIED — conflict risk:** project skills have high discovery precedence in Hermes. Stale same-name copies in profile/global/project paths can shadow or conflict with a deployed Apex-reviewed skill.
- **STATIC_SIMULATION — drift:** Git skill `S@abc` is reviewed, but runtime profile still loads prior local `S@def`; operator believes Git is truth while execution uses different instructions.
- **Required mitigation:** C06: deterministic runtime inventory, exact source/provenance/hash, reject duplicate same-name active copies, pilot discovery from at least two role profiles.
- **No new subsystem:** a copy/symlink/export mechanism is acceptable only if it is a simple deterministic deployment of existing files and the runtime cannot write the canonical source. If the installed runtime cannot satisfy that safely, stop the pilot rather than inventing a skill service.
- **Revisit trigger:** upstream provides a first-class signed/read-only shared-skill distribution mechanism that is simpler than the selected deterministic deployment.

---

## D06 — BMAD and domain-skill placement

**Architecture claim:** BMAD is installed only in repositories that use it; MarketingSkills remains MasterOfArts-only until another repository has a demonstrated need; Apex KB remains Apex-specific.

**Verdict:** **PASS_WITH_CONDITIONS**

- **SOURCE_VERIFIED — current BMAD:** upstream `package.json` reports BMAD Method `6.11.0`. The open upstream proposal `#1728` still asks for a global install/link mechanism, so a global BMAD linker is not the baseline.
- **SOURCE_VERIFIED — pilot conflict:** MasterOfArts P11 records both a project BMAD copy and `/root/.hermes/skills/agile/bmad-method/`; P12 similarly records project MarketingSkills and a global `/root/.hermes/skills/marketing/` copy. These were valid single-repo pilot choices but conflict with D06 if carried unchanged into a multi-repo profile environment.
- **SOURCE_VERIFIED — Apex specificity:** Apex's `apex-kb` skill explicitly wraps the Apex KB Python CLI and is not a generic project method.
- **STATIC_SIMULATION — ambiguity:** a cross-repo profile sees global BMAD/MarketingSkills plus repo-local skills. Duplicate names or irrelevant catalog metadata can alter routing and increase context even when the active repository never opted in.
- **Required mitigation:** C06: inventory and disable/remove shadowing global or learned copies; verify exact skill set per repository and profile.
- **Token/cost:** repo-scoped catalogs reduce recurring discovery metadata and activation ambiguity.
- **Revisit trigger:** another repository demonstrates a real MarketingSkills use case or upstream BMAD ships a stable supported global-link model that preserves per-project configuration cleanly.

---

## D07 — canonical WSL2 workspace per repository

**Architecture claim:** converge to one Linux-native WSL checkout per managed repo under a common normal-user workspace root; Windows copies become non-authoritative after reconciliation.

**Verdict:** **PASS_WITH_CONDITIONS**

- **SOURCE_VERIFIED — support:** Microsoft recommends storing Linux-tool development projects in the WSL Linux filesystem rather than `/mnt/c`; the MasterOfArts pilot independently observed `/mnt/c` performance/credential friction.
- **SOURCE_VERIFIED — pilot mismatch:** the pilot operational checkout is `/root/MasterOfArts`. The v2 migration plan instead targets a normal WSL user under `~/workspaces`, which is the safer reusable baseline.
- **STATIC_SIMULATION — dual-authority failure:** Windows checkout receives an unpushed local edit after WSL becomes “canonical”; deleting/freezing it without divergence audit loses work.
- **Required mitigation:** C02 plus the existing per-repo divergence/reconciliation gate. Verify normal user, ownership/UID/GID, branch, upstream, working tree, ignored/untracked files, and Windows-vs-WSL differences before authority switch.
- **Important narrowing:** do not hard-code a specific `umask` as architecture. Pick permissions from the installed user/group model and prove required reads/writes.
- **Revisit trigger:** none expected unless the platform/storage model changes materially.

---

## D08 — one local QMD engine, explicit repository collections

**Architecture claim:** one QMD installation indexes named, non-overlapping repository collections; project-heavy collections are excluded from unscoped default queries; repository files remain truth.

**Verdict:** **PASS_WITH_CONDITIONS**

- **SOURCE_VERIFIED — pilot:** P08 proves QMD 2.8.3 stdio MCP with `query`, `get`, `multi_get`, `status`; P09 proves a real named `moa-lika` collection and scoped retrieval in MasterOfArts.
- **SOURCE_VERIFIED — current contract:** current QMD/Hermes research identifies explicit `collections: [...]` as the MCP scoping input and warns against unscoped whole-estate retrieval.
- **STATIC_SIMULATION — retrieval bleed:** an Investment task omits collection scope; an included-by-default ACIM collection returns semantically similar material. Even a high-scoring result is wrong-context evidence.
- **STATIC_SIMULATION — stale index:** source repo advances from SHA A to B, but QMD still reflects A. `qmd status` can be healthy while semantic answer is stale.
- **Required mitigation:** C04 source-HEAD freshness receipt plus explicit collection requirement on project tasks. Re-run `qmd update`, required embeddings, then bind the refresh receipt to current source HEAD.
- **Token/cost:** QMD local retrieval reduces provider context by returning bounded passages. Do not build another RAG router.
- **Revisit trigger:** measured retrieval quality/freshness failure after correct collection scoping and refresh discipline.

---

## D09 — external memory service deferred

**Architecture claim:** do not add Mem0/Letta/Zep/another memory plane without a measured capability gap.

**Verdict:** **PASS**

- **SOURCE_VERIFIED — present owners:** Git repositories already own facts/decisions, Kanban owns execution state, QMD owns derived retrieval, profiles own small preferences/process memory, and skills own reviewed reusable procedure.
- **STATIC_SIMULATION — added-service cost:** another memory service introduces a new write path, stale/conflicting state, privacy surface, lifecycle policy, and retrieval/routing burden without fixing the currently identified defects.
- **INFERENCE — correct trigger:** reconsider only if the sequential profile + reviewed skill + repo/QMD design measurably fails a required user story after correct implementation.

---

## D10 — background multi-board autonomy remains gated

**Architecture claim:** unattended concurrent multi-board autonomy is not enabled until installed-version acceptance tests prove host persistence, workspace isolation, concurrency control, recovery, and false-success resistance.

**Verdict:** **PASS** — **for the gate itself; NOT authorization to enable D10.**

- **SOURCE_VERIFIED — concurrency:** `#78122` remains open; per-board concurrency can multiply gateway-wide workers.
- **SOURCE_VERIFIED — memory:** `#85497` remains open; tenants/boards do not isolate shared profile memory.
- **SOURCE_VERIFIED — workspace precedence:** `#73556` remains open; profile cwd can override task workspace.
- **SOURCE_VERIFIED — Docker provenance:** `#83856` remains open; host mount and container cwd may diverge.
- **SOURCE_VERIFIED — persistence:** `#91568` remains open; Docker Kanban workers can report successful commits that disappear because the task workspace was not host-backed.
- **SOURCE_VERIFIED — false success:** `#76285` remains open; nonexistent board binding can return exit 0.
- **SOURCE_VERIFIED — scheduler:** no-agent cron regressions `#77131` and `#80624` are closed, but `#20353` remains open and documents silent no-agent failure/no heartbeat visibility.
- **STATIC_SIMULATION — conclusion:** Safe Mode A, with one active repository execution lane and no unattended cross-board scheduler, is the correct initial operating mode. It converts these defects into acceptance-test items instead of production incidents.
- **Required acceptance additions:** exact task mount, host artifact/commit persistence, environment-canary isolation, board existence validation, last-run/heartbeat evidence for any no-agent scheduler job, same-profile cross-board dispatch refusal, crash/restart no duplicate side effects.
- **Revisit trigger:** only after all D10 tests pass on the exact installed Hermes release and configuration, with repeatable receipts.

---

## Cross-decision consistency verdict

**INFERENCE:** the architecture is coherent because the decisions constrain each other in the right direction:

- D01 + D02 prevent task-state/project-truth conflation.
- D02 + D03 + D10 compensate for current Hermes board/profile concurrency defects.
- D03 + D04 + D05 define a controlled learning path without raw-memory synchronization.
- D05 + D06 prevent a global skill dump from becoming hidden policy.
- D07 + D08 give one path model and one derived retrieval engine without duplicating project truth.
- D09 prevents an unnecessary memory layer while those owners are sufficient.

The remaining defects are implementation-gate defects and pilot-state cleanup, not evidence for a replacement architecture.
