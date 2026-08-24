# 00 — Independent Pre-Implementation Validation Verdict

- **Program:** Hermes Multi-Repo Orchestration v2
- **Repository / branch:** `leela-spec/apexai-os-meta` / `main`
- **Validation date:** 2026-08-24
- **Governing launcher:** `14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md`
- **Prior independent review incorporated:** `49b716a21ee82b94fcd26a6adac7bb2809ad2303`
- **Review mode:** adversarial validation; no implementation, migration, scheduler enablement, or D10 enablement
- **Status:** **VALIDATION COMPLETE — OPERATOR DECISION READY**

## 1. Verdict

# **`REVISE`**

The accepted D01–D10 architecture is directionally sound and should **not** be replaced with another orchestrator, state store, memory service, retrieval service, framework, or synchronization layer. The revision is narrower: the implementation gates must explicitly prevent legacy single-repository pilot state from becoming the multi-repository baseline and must close four deterministic integrity seams that the first independent review correctly identified.

**SOURCE_VERIFIED — architecture direction:** the current authority pack preserves one owner per concern: source repositories own project truth, Hermes Kanban owns runtime task/review state, Apex owns portfolio governance and derived rollups, QMD owns a rebuildable retrieval index, profile memory stays local, and reviewed skills carry only reusable procedure.

**SOURCE_VERIFIED — upstream risk remains live:** on 2026-08-24 the relevant Hermes defects remain open: tenant memory isolation `#85497`, per-board rather than gateway-wide concurrency `#78122`, profile `terminal.cwd` overriding task workspace `#73556`, Docker workspace provenance `#83856`, host-backed Kanban workspace persistence `#91568`, and dangling board binding returning success `#76285`. The no-agent cron false-positive and job-clobber regressions `#77131` and `#80624` are closed, while silent no-agent failure visibility `#20353` remains open.

**SOURCE_VERIFIED — pilot scope:** the MasterOfArts receipts prove a strong **single-repository** baseline: Docker host persistence, WSL isolation from `/mnt/c`, QMD MCP operation, Kanban durability, role reuse inside MasterOfArts, end-to-end review, and cold-restart recovery. They do **not** prove concurrent multi-board safety, cross-repository profile cleanliness, task-specific Docker mounts, or cross-repository skill scoping.

**STATIC_SIMULATION — decision consequence:** Safe Mode A (sequential execution, one active repository/workspace per profile, D10 disabled) neutralizes the known Hermes multi-board concurrency defects during initial rollout. It does not neutralize a stale static Docker mount, stale QMD index, stale derived Apex snapshot, polluted profile memory, or globally shadowing skills. Those must be corrected before the first cross-repository activation.

## 2. Snapshot validated

| Source | Ref observed | Evidence |
|---|---|---|
| `leela-spec/apexai-os-meta` | `49b716a21ee82b94fcd26a6adac7bb2809ad2303` before this revision | `SOURCE_VERIFIED` |
| `leela-spec/MasterOfArts` | `b50b758b30f8f07a1c003fb582f32811a35376df` | `SOURCE_VERIFIED` |
| `leela-spec/acim-secular` | `master` at `2cb94a0d899e02e2989934b98e428f8f005d4c96` | `SOURCE_VERIFIED` |
| `leela-spec/Investment` | `main` at `63ad92ddf35507b351f9c069e790b7736cfcfd56` | `SOURCE_VERIFIED` |
| Hermes Agent upstream | `main` reports v`0.20.5` / release date `2026.8.19` | `SOURCE_VERIFIED` |
| QMD upstream | current 2.8.x contract: named collections, `includeByDefault`, `update`, `embed`, `status`, MCP `query/get/multi_get/status` | `SOURCE_VERIFIED` |
| BMAD Method | current package v`6.11.0`; Hermes target is project `.agents/skills`; global linking remains non-baseline | `SOURCE_VERIFIED` |
| Agent Skills | `SKILL.md` + metadata-first progressive disclosure + resources on demand | `SOURCE_VERIFIED` |

## 3. D01–D10 disposition

| Decision | Verdict | Why |
|---|---|---|
| D01 — Apex control plane | **PASS_WITH_CONDITIONS** | Keep Apex derived-only; make rollup publication atomic and source-SHA-bearing. |
| D02 — separate repo boards + async rollup | **PASS_WITH_CONDITIONS** | Board separation is the correct boundary; rollup must preserve last-known-good on partial read failure. |
| D03 — reusable role profiles | **PASS_WITH_CONDITIONS** | Sequential role reuse is valid, but reusable profiles must start free of project schedules/facts and fixed cwd/mount state. |
| D04 — learning spillover | **PASS_WITH_CONDITIONS** | Reviewed skills are the right spillover mechanism; legacy pilot `USER.md` schedules and learned upstream-package copies must not be carried forward. |
| D05 — Apex shared-skill source | **PASS_WITH_CONDITIONS** | Canonical Git source is sound; runtime deployment must be provenance-verifiable and must not be shadowed by stale local copies. |
| D06 — BMAD/domain skill placement | **PASS_WITH_CONDITIONS** | Policy is correct, but the MasterOfArts pilot receipts show global BMAD/MarketingSkills copies that conflict with the target scope if retained. |
| D07 — canonical WSL workspace | **PASS_WITH_CONDITIONS** | Linux-native WSL storage is correct; converge on a normal WSL user/home and remove `/root/MasterOfArts` assumptions. |
| D08 — QMD multi-repo retrieval | **PASS_WITH_CONDITIONS** | Explicit collections prevent bleed; high-stakes retrieval needs a deterministic source-HEAD freshness receipt. |
| D09 — external memory deferred | **PASS** | No measured gap justifies another memory service. Sequential profiles plus reviewed skill promotion are sufficient. |
| D10 — background multi-board autonomy gated | **PASS** | The decision to keep autonomy disabled is correct. This is a PASS for the gate, **not** authorization to enable D10. |

## 4. Mandatory correction set

Implementation remains unauthorized until the applicable corrections in `04-CORRECTION-PLAN.md` are satisfied.

1. **C01 — task-scoped Docker mount contract.** Remove the single-repo static `/root/MasterOfArts` volume assumption. A worker must mount only the resolved active task workspace; host-side persistence and mount provenance must be verified before commands execute.
2. **C02 — WSL user/home normalization.** Operate from the normal WSL user under `~/workspaces`; verify ownership/UID/GID and absence of hard-coded `/root` paths. Do not impose an arbitrary `umask` unless a real permission test requires it.
3. **C03 — atomic fail-closed Apex rollup.** Read every configured source, validate board/repo/branch/source SHA, render to a temporary artifact, and atomically replace only after all reads succeed. Preserve the last-known-good snapshot on failure.
4. **C04 — QMD source-HEAD freshness receipt.** Because QMD index health does not itself prove which Git HEAD was indexed, record a deterministic per-collection refresh receipt after successful `qmd update` + required `qmd embed`; compare that receipt with current source HEAD before high-stakes retrieval.
5. **C05 — reusable-profile state reset.** Do not promote the pilot profiles wholesale. Rebuild/review role profiles from thin role definitions and stable operator preferences only; remove project schedules, project facts, fixed cwd, and project-specific runtime assumptions from `USER.md`/`MEMORY.md`.
6. **C06 — skill-scope/provenance reset.** Remove or disable legacy global/learned copies that would shadow target policy. BMAD is repo-local; MarketingSkills is MasterOfArts-only until another repo has an approved need; Apex-reviewed shared skills have one canonical source and a verifiable runtime deployment.
7. **C07 — Docker credential/environment negative test.** Use current Hermes `docker_forward_env` allowlisting and verify with canary secrets that unrelated host credentials do not enter the container. Filesystem isolation alone is not credential-isolation proof.
8. **C08 — repository context-entry preflight.** Before board activation, verify each repository has an intentional root context entrypoint usable by Hermes and that it points to current authority. `acim-secular` and `Investment` currently have no root `AGENTS.md`; Apex has one, but it is primarily a Codex/Apex-KB operating note rather than a Hermes portfolio context.

**SOURCE_VERIFIED — prior C05 disposition:** the first review proposed “parameterize default branches” as a correction. That requirement is already locked in `state.yaml`, D07, and the migration plan (`acim-secular=master`; others `main`). It remains an acceptance check, not a new architecture correction.

## 5. Reconciliation with the other independent review (`49b716a2`)

| Prior finding | This review | Disposition |
|---|---|---|
| Overall `GO_WITH_CONDITIONS` | **`REVISE`** | Same architecture direction; stricter authorization threshold because pilot runtime-state conflicts were found and this run did not inherit unverifiable live-host claims as `EXECUTED`. |
| C01 static Docker mount | Confirmed | Retained as C01. |
| C02 WSL user/home | Confirmed, narrowed | Retained without hard-coding `umask 022`; require normal user + ownership/path evidence. |
| C03 atomic rollup | Confirmed | Retained as C03. |
| C04 QMD freshness | Confirmed, made Git-HEAD-based | Retained as C04; timestamps alone are insufficient. |
| C05 default branches | Already in authority | Reclassified to acceptance test. |
| D01/D02/D04/D06/D08 unconditional PASS | Too optimistic | Downgraded to conditional where implementation integrity or legacy-state cleanup is still required. |
| Claimed direct live WSL inspection | Not independently reproducible here | Durable pilot receipts are accepted as `SOURCE_VERIFIED` evidence of prior execution, not relabeled as this reviewer’s `EXECUTED`. |

## 6. External-practice comparison

**SOURCE_VERIFIED — OpenAI:** current agent guidance recommends maximizing a single agent with clear tools/instructions before introducing multi-agent orchestration, using layered guardrails and human intervention for high-risk actions. The v2 design follows this by keeping one Hermes runtime and deferring extra frameworks.

**SOURCE_VERIFIED — Anthropic:** current engineering guidance treats context as finite, favors selective high-signal context, and reports that multi-agent research can consume about 15× chat tokens and performs poorly where agents require tightly shared context/dependencies. The v2 Safe Mode and scoped QMD design match this constraint.

**SOURCE_VERIFIED — Google:** Vertex Agent Engine models durable session/event state explicitly by user/session identity rather than relying on hidden conversational memory. This supports the v2 separation of durable task state from profile memory and project truth.

**SOURCE_VERIFIED — Microsoft/Docker:** Microsoft recommends Linux-tool projects live in the WSL Linux filesystem under `/home/<user>/...`, and Docker documents that writable bind mounts directly mutate host files and should be verified explicitly. These support C01/C02.

## 7. What is not required

No evidence demonstrates a need for:

- another orchestration runtime;
- a cross-runtime memory synchronizer;
- a custom RAG/KB service;
- a message broker;
- a global BMAD linker;
- a bidirectional task synchronizer;
- a second QMD engine;
- tenant-based memory isolation;
- D10 concurrent autonomy now.

## 8. Authorization boundary

**INFERENCE — final decision:** `REVISE` means “retain D01–D10, tighten implementation gates, then re-evaluate authorization.” It does **not** mean redesign the architecture.

D10 remains disabled. Repository migrations, runtime reconfiguration, scheduler enablement, and cross-repo background dispatch remain outside this review.
