# 05 — Refreshed Source and Claim Matrix

- **Program:** Hermes Multi-Repo Orchestration v2
- **Refresh date:** 2026-08-24
- **Purpose:** record current primary evidence used by this independent review and distinguish current source verification from prior runtime execution receipts
- **Evidence labels:** `EXECUTED`, `STATIC_SIMULATION`, `SOURCE_VERIFIED`, `INFERENCE`

## 1. Repository and authority sources

| Claim / concern | Current primary source | Ref / state observed | Label | Validation consequence |
|---|---|---|---|---|
| Project index and authority order | `apex-meta/epics/hermes-multi-repo-orchestration-v2/README.md` | `main` | `SOURCE_VERIFIED` | Used as authoritative project index. |
| Independent validation scope and output boundary | `14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md` | `main` | `SOURCE_VERIFIED` | Adversarial review only; no implementation or D10 enablement. |
| Machine-readable architecture state | `state.yaml` | `main` | `SOURCE_VERIFIED` | Confirms statuses, managed repos and branch registry. |
| D01–D10 current decisions | `decisions/D01...D10` | `main` | `SOURCE_VERIFIED` | Decisions retained; review changes no authority file. |
| Architecture synthesis | `01-VERIFIED-ARCHITECTURE.md` | `main` | `SOURCE_VERIFIED` | Confirms one-owner boundaries and Safe Mode. |
| Implementation sequence | `11-IMPLEMENTATION-ROADMAP.md` | `main` | `SOURCE_VERIFIED` | Corrections gate implementation; no roadmap execution here. |
| Existing architecture risks | `12-RISK-REGISTER.yaml` | `main` | `SOURCE_VERIFIED` | Independent register supplements rather than replaces it. |
| Existing source matrix | `13-SOURCE-VERIFICATION-MATRIX.md` | `main` | `SOURCE_VERIFIED` | Refreshed against current upstream issue/repo state. |
| MasterOfArts migration manifest | `02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md` | `main` | `SOURCE_VERIFIED` | Migration remains controlled and unauthorised by this run. |
| Prior independent review | commit `49b716a21ee82b94fcd26a6adac7bb2809ad2303` | 2026-08-24 | `SOURCE_VERIFIED` | Incorporated as comparison evidence, not authority. |

## 2. Managed repository snapshots

| Repository | Branch | Current observed commit | Label | Note |
|---|---|---|---|---|
| `leela-spec/apexai-os-meta` | `main` | `49b716a21ee82b94fcd26a6adac7bb2809ad2303` before this review commit | `SOURCE_VERIFIED` | Validation target/control plane. |
| `leela-spec/MasterOfArts` | `main` | `b50b758b30f8f07a1c003fb582f32811a35376df` | `SOURCE_VERIFIED` | Pilot evidence source. |
| `leela-spec/acim-secular` | `master` | `2cb94a0d899e02e2989934b98e428f8f005d4c96` | `SOURCE_VERIFIED` | Confirms non-`main` default branch. |
| `leela-spec/Investment` | `main` | `63ad92ddf35507b351f9c069e790b7736cfcfd56` | `SOURCE_VERIFIED` | Separate source repo. |

## 3. MasterOfArts pilot evidence refresh

| Pilot claim | Durable primary receipt | Label in this review | Scope / correction |
|---|---|---|---|
| Windows + WSL2 + Docker baseline passed | `IMPLEMENTATION-ACCEPTANCE-REPORT.md` | `SOURCE_VERIFIED` | Evidence of prior execution, not current live-host re-execution. |
| Docker reachable from WSL and disposable mount write works | `implementation-evidence/P03-docker-baseline.md` | `SOURCE_VERIFIED` | Supports baseline only. |
| Hermes action tools executed in Docker; `/mnt/c` absent; host repo writes landed | `implementation-evidence/P07-hermes-docker-backend.md` | `SOURCE_VERIFIED` | Strong single-repo evidence; static `/root/MasterOfArts` binds create C01. |
| QMD MCP uses `query/get/multi_get/status` | `implementation-evidence/P08-qmd-hermes-integration.md` | `SOURCE_VERIFIED` | Confirms native stdio path. |
| Lika QMD retrieval worked | `implementation-evidence/P09-lika-knowledge-package.md` | `SOURCE_VERIFIED` | Does not prove cross-repo collection isolation. |
| Kanban deps/context/persistence worked | `implementation-evidence/P10-kanban-baseline.md` | `SOURCE_VERIFIED` | One default board, not multi-board concurrency. |
| BMAD discovery worked | `implementation-evidence/P11-bmad-integration.md` | `SOURCE_VERIFIED` | Receipt shows both global and project copies; target D06 requires scope cleanup. |
| MarketingSkills worked across two MoA families | `implementation-evidence/P12-marketing-skills.md` | `SOURCE_VERIFIED` | Same repo; receipt shows global + project copies. |
| Shared profiles adapted across Lika/Dance Fusion | `implementation-evidence/P13-shared-specialists.md` | `SOURCE_VERIFIED` | Proves family reuse, not independent-repo reuse. |
| Memory/learning persisted | `implementation-evidence/P14-autonomous-learning.md` | `SOURCE_VERIFIED` | Useful mechanism; target governance is stricter than pilot. |
| E2E maker/reviewer loop passed | `implementation-evidence/P15-e2e-integration.md` | `SOURCE_VERIFIED` | Single-repo flow only. |
| Cold-restart recovery passed | `implementation-evidence/P16-recovery-test.md` | `SOURCE_VERIFIED` | Does not prove duplicate scheduler/multi-board behavior. |
| Static Docker mounts and environment inheritance observation | `Orchestration/Implementation/OKF-EXECUTION-OBSERVATIONS.yaml` | `SOURCE_VERIFIED` | Drives C01/C07. |
| Project schedules stored in Hermes USER memory; BMAD/MarketingSkills listed in learned library | `Orchestration/Implementation/AUTONOMOUS_LEARNINGS_SUMMARY.md` | `SOURCE_VERIFIED` | Drives C05/C06. |
| MasterOfArts has root Hermes context | `AGENTS.md` | `SOURCE_VERIFIED` | Useful model for C08. |

## 4. Current Hermes upstream refresh

| Claim / defect | Primary source | Current state observed 2026-08-24 | Label | Impact |
|---|---|---|---|---|
| Current Hermes source version | `NousResearch/hermes-agent` `hermes_cli/__init__.py` | `0.20.5`, release date `2026.8.19` | `SOURCE_VERIFIED` | Match pilot version family; upstream main continues moving. |
| Tenant does not isolate profile memory | issue `#85497` | **OPEN** | `SOURCE_VERIFIED` | Supports separate boards + no raw-memory isolation assumption. |
| `max_in_progress` is per board, not gateway-wide | issue `#78122` | **OPEN** | `SOURCE_VERIFIED` | D10 must remain disabled; per-profile sequential guard required. |
| Profile cwd can override task workspace and broaden mount | issue `#73556` | **OPEN** | `SOURCE_VERIFIED` | C01 and D10 exact-workspace acceptance. |
| Host mount provenance and container cwd can diverge | issue `#83856` | **OPEN** | `SOURCE_VERIFIED` | C01; test terminal/file/execute-code consistency. |
| Docker Kanban workspace may not be host-backed; apparent commit can disappear | issue `#91568` | **OPEN** | `SOURCE_VERIFIED` | C01 host persistence test mandatory. |
| Project board binding can accept nonexistent slug / exit 0 | issue `#76285` | **OPEN** | `SOURCE_VERIFIED` | Explicit board-existence acceptance required. |
| No-agent job may silently fail/no heartbeat | issue `#20353` | **OPEN** | `SOURCE_VERIFIED` | D10 scheduler observability requirement. |
| Python no-agent cron lifecycle false positive | issue `#77131` | **CLOSED / completed** | `SOURCE_VERIFIED` | Do not preserve obsolete blocker. |
| No-agent jobs clobbered/disappearing | issue `#80624` | **CLOSED / completed** | `SOURCE_VERIFIED` | Do not preserve obsolete blocker; still live-test installed version. |
| Latest upstream changes after release include MCP timeout work | Hermes `main` recent commits, including `057dcdf...` | current main newer than release commit | `SOURCE_VERIFIED` | Installed-release acceptance remains more important than memory of upstream behavior. |

## 5. Hermes architecture/practice sources retained

| Topic | Primary source | Label | What it supports |
|---|---|---|---|
| Profiles | Hermes official profile docs / upstream source | `SOURCE_VERIFIED` | Persistent role identity is distinct from project facts; concurrency requires care. |
| Context files | Hermes official context-file docs | `SOURCE_VERIFIED` | Git-root-to-workdir progressive context; use concise routing not copied KBs. |
| Kanban | Hermes official Kanban docs | `SOURCE_VERIFIED` | Durable task/dependency/review/workspace state; cross-board limitations remain. |
| Skills | Hermes official skills docs | `SOURCE_VERIFIED` | Project/profile/global precedence and progressive loading; provenance matters. |
| Memory/Curator | Hermes official memory/Curator docs | `SOURCE_VERIFIED` | Runtime learning is not project truth and needs governance. |
| Cron | Hermes official cron docs + current issues | `SOURCE_VERIFIED` | Native scheduling exists but unattended multi-board use remains gated. |
| Security / Docker backend | Hermes official security/configuration docs | `SOURCE_VERIFIED` | Use native isolation/allowlists; do not invent policy middleware. |

## 6. QMD refresh

| Claim | Current primary source | State | Label | Impact |
|---|---|---|---|---|
| QMD supports one engine with multiple named collections | `tobi/qmd` current repository/docs | current | `SOURCE_VERIFIED` | D08 remains valid. |
| QMD MCP exposes typed retrieval and exact fetch | current QMD MCP contract; pilot P08 | `query`, `get`, `multi_get`, `status` | `SOURCE_VERIFIED` | No custom MCP/RAG wrapper needed. |
| Explicit collection scope is required for project-heavy work | QMD collection/query contract + D08 | current | `SOURCE_VERIFIED` | Negative isolation test required. |
| Refresh uses native `qmd update` and embedding refresh as needed | QMD docs | current | `SOURCE_VERIFIED` | C04 adds only source-HEAD receipt, not another index. |
| QMD index is derived, not canonical | D08 + QMD behavior | current | `SOURCE_VERIFIED` | Git files remain truth. |

## 7. BMAD / Agent Skills refresh

| Claim | Primary source | State | Label | Impact |
|---|---|---|---|---|
| BMAD current package version | `bmad-code-org/BMAD-METHOD/package.json` | `6.11.0` | `SOURCE_VERIFIED` | Refreshes old version assumptions. |
| BMAD global install/link proposal | BMAD issue `#1728` | **OPEN** | `SOURCE_VERIFIED` | Do not build a global BMAD linker; D06 repo-local placement remains sound. |
| Agent Skills package model | `agentskills.io/specification` | current | `SOURCE_VERIFIED` | `SKILL.md`, metadata-first discovery, on-demand resources support D04/D05. |
| Apex KB is Apex-specific | Apex `.claude/skills/apex-kb/SKILL.md` | current | `SOURCE_VERIFIED` | Do not copy as generic domain skill. |

## 8. Repository context-entry refresh

| Repo | Root context result | Label | Impact |
|---|---|---|---|
| MasterOfArts | root `AGENTS.md` present, Hermes-oriented | `SOURCE_VERIFIED` | Existing example of macro routing. |
| apexai-os-meta | root `AGENTS.md` present, primarily Codex/Apex-KB execution note | `SOURCE_VERIFIED` | C08 must decide/adapt Hermes-relevant portfolio routing without duplicating truth. |
| acim-secular | root `AGENTS.md` not found on `master` | `SOURCE_VERIFIED` | C08 preflight required before Hermes board activation. |
| Investment | root `AGENTS.md` not found on `main` | `SOURCE_VERIFIED` | C08 preflight required before Hermes board activation. |

## 9. External battle-proven practice comparison

| Practice | Current primary source | Label | Relevance to v2 |
|---|---|---|---|
| Prefer simpler single-agent/tool systems before adding agents; add guardrails/human intervention for risk | OpenAI current practical agent-building guidance | `SOURCE_VERIFIED` | Supports one Hermes runtime, D10 gating, no extra orchestrator. |
| Context is finite; retrieve high-signal context selectively | Anthropic current context-engineering guidance | `SOURCE_VERIFIED` | Supports scoped QMD + concise context files. |
| Multi-agent systems impose major token overhead and work best when tasks are parallelizable rather than tightly interdependent | Anthropic multi-agent engineering/research guidance | `SOURCE_VERIFIED` | Supports Safe Mode/sequential roles and asynchronous cross-project coupling. |
| Durable agent/session state should have explicit session/user identity rather than hidden conversation state | Google Vertex Agent Engine session/event documentation | `SOURCE_VERIFIED` | Supports Kanban/repo truth separation from profile memory. |
| Keep Linux-tool projects in WSL Linux filesystem for performance | Microsoft WSL filesystem guidance | `SOURCE_VERIFIED` | Supports D07 and C02. |
| Writable Docker bind mounts can modify host files and must be deliberately scoped | Docker bind-mount documentation | `SOURCE_VERIFIED` | Supports C01 exact mount/persistence acceptance. |

## 10. Evidence limitations

- **SOURCE_VERIFIED:** this run inspected current repositories, commit history, primary-source issue state, and web documentation.
- **SOURCE_VERIFIED:** MasterOfArts receipts are durable evidence that prior live tests reported PASS on the recorded environment.
- **INFERENCE:** they do not prove the current machine/runtime is unchanged after those receipts.
- **INFERENCE:** no current host-runtime statement should be labeled `EXECUTED` by this reviewer because no WSL/Hermes shell execution was available in this run.
- **STATIC_SIMULATION:** cross-repo and failure-injection results in `02-CROSS-DECISION-ORCHESTRATION-SIMULATION.md` are explicit tabletop tests to be converted into installed-version acceptance tests later.

## 11. Refresh conclusion

**INFERENCE:** refreshed primary evidence strengthens rather than overturns the selected architecture. It specifically justifies keeping D10 disabled, preserving explicit state ownership, limiting skill/memory scope, using WSL-native checkouts, and adding deterministic fail-closed receipts around mounts, rollups, QMD freshness, board identity, and scheduler health.
