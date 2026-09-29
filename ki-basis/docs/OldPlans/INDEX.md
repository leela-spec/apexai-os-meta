---
type: Index
title: Old / failed / superseded implementation plans — index
description: >
  A single index of the project's OWN historical implementation, execution, finalization, correction and
  migration plans that are OLD (pre-2026-09-26 consolidation baseline) or FAILED / SUPERSEDED / CORRECTED /
  DEFERRED. Kept for provenance — NOTHING here is current. Vendored/third-party and raw-KB material is
  excluded. Current infrastructure truth: ki-basis/docs/INFRASTRUCTURE.md.
created: 2026-09-29
baseline: "Current = the 2026-09-26 WSL2 consolidation (ADR-002) + later. Anything predating it that conflicts, or any plan that failed/was abandoned/superseded/deferred/corrected, is listed here."
current_truth: ki-basis/docs/INFRASTRUCTURE.md
scope: "apexai-os-meta only. EXCLUDED: source-knowledge/, apex-meta/kb/, ApexDefinition&OldVersions/, any /raw/ path, vendored skills (antigravity-awesome-skills, bmad), node_modules, researcher-attachments-*, and simulation fixtures."
---

# Old / failed / superseded implementation plans — index

**What this is.** A map of the project's historical plans so nobody mistakes them for current guidance and so
their provenance stays findable. These plans are **kept, not deleted**. For what is true *now*, read
[`ki-basis/docs/INFRASTRUCTURE.md`](../INFRASTRUCTURE.md) (+ `DUAL_INSTANCE_ARCHITECTURE.md` §6 / ADR-002).

**Companion:** [`REBUILD-AND-FAILURE-HISTORY.md`](REBUILD-AND-FAILURE-HISTORY.md) — the ranked, truthful failure/rebuild history (why we rebuilt for ~2 months) and the install-script requirements it implies.

**How to read it.** All paths are **relative to the repo root** (`C:\GitDev\apexai-os-meta\`). Status legend:

| Status | Meaning |
|---|---|
| **OLD** | Pre-2026-09-26; superseded by the WSL2 consolidation, not individually "failed" |
| **SUPERSEDED** | Replaced by a newer version / decision |
| **CORRECTED** | A correction/redo plan implying a prior attempt was wrong |
| **FAILED** | Explicitly failed / abandoned (or lives in a "failure" folder) |
| **DEFERRED** | Written but explicitly not authorized / not executed |

> ⚠️ Only a handful of these carry an in-file banner; most are classified here by folder, self-status line, or
> date. Treat **every** entry as non-current. Counts are approximate where a bundle spans many files.

---

## 1. Alpine ImplementationPlans — Docker Desktop / Antigravity era (pre-consolidation)
| Path | Date | Status | What it was | Bannered? |
|---|---|---|---|---|
| `apex-meta/Alpine/ImplementationPlans/00-START-HERE.md` | undated | OLD | Antigravity Docker-stack reading guide | no |
| `apex-meta/Alpine/ImplementationPlans/01-META-IMPLEMENTATION-PLAN-ANTIGRAVITY.md` | undated | OLD | Meta plan: one Docker Compose stack | no |
| `apex-meta/Alpine/ImplementationPlans/02..09-*-ANTIGRAVITY.md` (8: nginx, postgres-pgvector, valkey, firefly, paperless-ngx, openproject, hermes, integration-acceptance) | undated | OLD | Per-service Docker install/acceptance plans | no |
| `apex-meta/SmallSkills/Prompting/Antigravity/docker-stack-integrity/08-M06-CANONICALIZE-PLAN-FAMILIES.md` | undated | OLD | Module to canonicalize the two Alpine plan families | no |

## 2. ki-basis finalization 2026-09-03 (Docker Desktop era)
| Path | Date | Status | What it was | Bannered? |
|---|---|---|---|---|
| `apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/00-START-HERE.md` | 2026-09-03 | OLD | Finalization program entry (Docker Desktop → Hyper-V) | **yes** |
| `.../2026-09-03-ki-basis-finalization/06-DOCUMENTATION-TRUTH-CORRECTION.md` | 2026-09-03 | CORRECTED | Doc-truth correction (token redaction, stale push claims) | no |
| `.../2026-09-03-ki-basis-finalization/08-PERFORMANCE-TUNING-DEFERRED.md` | 2026-09-03 | DEFERRED | Perf tuning deferred (hypotheses, not measurements) | no |
| `.../2026-09-03-ki-basis-finalization/{01,02,03,04,04A,05,05A,07,09}-*.md` (9 modules: security rotation, backup, restore-oracle, strict-auth, docker-bg-runtime, hermes-control, cli-routing, cold-reboot, final-closure) | 2026-09-03 | OLD | Finalization modules on the Docker Desktop stack | no |
| `apex-meta/Alpine/Iteration2/Correction_Implementation Plan_ ki-basis Environment Recovery.md` | undated | CORRECTED | Recovery after Docker-host silently promoted; marks a prior 13-module patch ZIP "SUPERSEDED — do not run" | no |

## 3. Transcription pipeline — v1 / v2.1 failed → v3; v4 "after V3 but fail"
| Path | Date | Status | What it was | Bannered? |
|---|---|---|---|---|
| `SourceTranscriptionAnalysisPipeline_Research/archive/transcript-pipeline-v1-2026-08-18/V1_IMPLEMENTATION_PLAN_CLI_SEMANTIC_WORKER_2026-08-18.md` | 2026-08-18 | SUPERSEDED | V1 CLI semantic-worker plan (in `archive/`) | folder=archive |
| `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/08-V2.1-CORRECTIVE-EXECUTION-PLAN.md` | ~2026-08 | CORRECTED | Corrective rerun of the FAILED V2.1 Trial-1 | self-labels failed |
| `.../v2-reuse-bakeoff/11-V2.1-STAGE-BY-STAGE-IMPLEMENTATION-PLAN.md` | 2026-08-19 | SUPERSEDED | Pointer stub → superseded by V3 | **yes** |
| `.../v2-reuse-bakeoff/09-V2.1-TARGET-FIRST-EXECUTION-BRIEF.md` | ~2026-08 | SUPERSEDED | V2.1 target-first exec brief | no |
| `.../v2-reuse-bakeoff/archive-pre-v3-authority/11-...original.md`, `.../execution-modules-README.original.md` | 2026-08-19 | SUPERSEDED | Byte-preserved pre-V3 originals | folder=archive |
| `.../v3-proven-infrastructure/02-V3-IMPLEMENTATION-PLAN.md` | 2026-08-19 | SUPERSEDED | V3 impl plan; INDEX later demoted V3 PASS from product authority | no |
| `.../OperatorFolder/DR4_v4_after V3 but fail/06-PRIME-RECOMMENDATION-IMPLEMENTATION-PLAN.md` | 2026-08-19 | FAILED | v4 "prime recommendation" in a folder named "after V3 but fail" | no |
| `.../transcript-to-knowledge-complete-bundle/history/v1-research/RESEARCH-AND-IMPLEMENTATION-v1-original.md` | 2026-08-18 | SUPERSEDED | v1 research+impl (in `history/`) | folder=history |
| `apex-meta/validation/transcript-to-knowledge-20260818/RESEARCH-AND-IMPLEMENTATION.md` + `v2/20-MICRO-IMPLEMENTATION.md` | 2026-08-18 | OLD | Dated validation snapshots | no |

## 4. Hermes multi-repo orchestration v2 epic (2026-08-24, Antigravity; impl never authorized)
| Path | Date | Status | What it was | Bannered? |
|---|---|---|---|---|
| `apex-meta/epics/hermes-multi-repo-orchestration-v2/11-IMPLEMENTATION-ROADMAP.md` | 2026-08-24 | SUPERSEDED | v1 phase catalog, superseded by file 15 | **yes** |
| `.../hermes-multi-repo-orchestration-v2/15-IMPLEMENTATION-ROADMAP-v2-ANTIGRAVITY.md` | 2026-08-24 | OLD | v2 Antigravity execution roadmap (impl not authorized) | self-status |
| `.../09-WSL-CANONICAL-WORKSPACE-MIGRATION-PLAN.md` | 2026-08-24 | DEFERRED | Converge to one Linux-native checkout; "MIGRATION NOT AUTHORIZED" | self-status |
| `.../02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md` | 2026-08-24 | OLD | Source inventory; "NO MOVE OR DELETE AUTHORIZED" | self-status |
| `.../decisions/D09-EXTERNAL-MEMORY-DEFERRED.md` | 2026-08-24 | DEFERRED | External shared-memory provider deferred | self-status |
| `.../validation/independent-preimplementation-review/04-CORRECTION-PLAN.md` | 2026-08-24 | CORRECTED | Minimum correction set (verdict REVISE) | no |
| `.../patches/2026-08-24-implementation-roadmap-v2-antigravity.patch.md` | 2026-08-24 | OLD | Patch to roadmap v2 | no |

## 5. Fable orchestrator (2026-07; superseded by later orchestration/weekly systems)
| Path | Date | Status | What it was | Bannered? |
|---|---|---|---|---|
| `apex-meta/fable-orchestrator/implementation-plan.md` | 2026-07-11 | OLD | "Meta impl plan…being executed this session" (stale July) | no |
| `apex-meta/fable-orchestrator/build-plan.md` | 2026-07-11 | OLD | Execution-completion recovery plan | no |
| `apex-meta/fable-orchestrator/Newplan.md` | 2026-07 | OLD | Lean completion plan | no |
| `apex-meta/fable-orchestrator/orchestration-betterment-plan-v2.md` | 2026-07-12 | SUPERSEDED | Token-efficiency betterment (folded into MasterPlan v3) | no |
| `apex-meta/fable-orchestrator/orchestration-patch-plan-20260712.md` | 2026-07-12 | OLD | Patch plan for orchestration design gaps | no |
| `apex-meta/fable-orchestrator/patch-process-20260713/Tier 0 Micro-Implementation Validation Packet.md` | 2026-07-13 | OLD | Tier-0 micro-impl validation packet | no |
| `apex-meta/handoff/plan-packets/OrchestrationBetterment_MasterPlan_v3.md` | ~2026-07 | OLD | Master plan (preserves v2 + v3 corrections) | no |

## 6. Local orchestration engine / FEE environment (2026-07–08)
| Path | Date | Status | What it was | Bannered? |
|---|---|---|---|---|
| `apex-meta/local-orchestration-engine/00-START-HERE.md` | 2026-07-28 | OLD | Design-lock workspace, status "pre-design" | no |
| `apex-meta/local-orchestration-engine/LOCAL-MODEL-CROSS-AGENT-EXECUTION-PLAN-2026-08-08.md` | 2026-08-08 | OLD | Cross-agent local-model calibration exec plan | no |
| `apex-meta/local-orchestration-engine/architecture/03-micro-implementation-map.md` | 2026-07-28 | OLD | FEE micro-impl map, "NOTHING…EXECUTED" | no |
| `apex-meta/local-orchestration-engine/project/plans/2026-08-10-fee-project-environment-implementation-plan.md` | 2026-08-10 | OLD | FEE PM-environment plan | no |
| `FEE/2026-08-10-fee-project-environment-implementation-plan.md` | 2026-08-10 | OLD | Same FEE plan (root copy) | no |
| `docs/superpowers/plans/2026-08-10-fee-project-environment-implementation-plan.md` | 2026-08-10 | OLD | Third copy of same FEE plan | no |

## 7. FEE OpenClaw local executor (2026-08; corrected non-viable, GPU failure)
| Path | Date | Status | What it was | Bannered? |
|---|---|---|---|---|
| `FEE/OpenClaw Local Executor — Installation and Implementation Plan.md` | 2026-08-10 | SUPERSEDED | Install/impl plan; contradicted by the viability correction | no |
| `FEE/CORRECTION-2026-08-11-LOCAL-EXECUTOR-VIABILITY.md` | 2026-08-11 | CORRECTED | Local 8B model not a viable executor (capability + GPU) | no |
| `FEE/GPU_Failure/ANALYSIS-AND-PLAN-2026-08-11.md` | 2026-08-11 | FAILED | Vulkan device-lost crash on Intel Arc 140V; fix plan | folder=GPU_Failure |
| `FEE/OpenClaw_Setup/OpenClaw_SetupPlanCodexSuperpowers.md` | 2026-08 | OLD | Revised OpenClaw execution plan | no |
| `FEE/OpenClaw_Setup/OpenClaw_SetupPlan_Continuation_Claude.md` | 2026-08 | OLD | Continuation plan | no |
| `FEE/Patch_FinalGPTImplementationFiles.md` | 2026-08 | OLD | Exact-match patch to OpenClaw impl files | no |
| `FEE/PossiblyOld&Wrong/OPENCLAW-LOCAL-LLM-MASTER-BRIEF.md` | undated | OLD | Master brief (folder "PossiblyOld&Wrong") | no |

## 8. Hermes single-container (Arch-3) Docker migration (FAILED; retired by WSL2 consolidation)
| Path | Date | Status | What it was | Bannered? |
|---|---|---|---|---|
| `apex-meta/orchestration/architecture-improvements/02-hermes-single-container-runtime/G0.2-MIGRATION-RUNBOOK.md` | ~2026-08 | SUPERSEDED | Move Hermes into one persistent Docker container (Arch-3) | no |
| `apex-meta/AI-Snippets/Inbetween_Delete/HERMES-OPTION2-DOCKER-DOWNGRADE-PLAN.md` | 2026-08-26 | FAILED | Downgrade containerd to stabilize Arch-3; "proposed, not executed" | folder=Inbetween_Delete |
| `apex-meta/AI-Snippets/Inbetween_Delete/HERMES-MIGRATION-HANDOVER-OKF-v0.2.md` | 2026-08-26 | FAILED | Migration handover documenting repeated ❌ failed workarounds | folder=Inbetween_Delete |

## 9. Hermes WSL/DrvFs git-performance package (2026-08-25; corrected)
| Path | Date | Status | What it was | Bannered? |
|---|---|---|---|---|
| `apex-meta/orchestration/architecture-improvements/01-hermes-wsl-drvfs-git-performance/05-ACTIONABLE-REMEDIATION-ROADMAP-AND-RUNBOOKS.md` | 2026-08-25 | CORRECTED | Remediation roadmap; superseded by the corrected plan (06) | no |
| `.../01-hermes-wsl-drvfs-git-performance/06-VERIFICATION-AND-CORRECTED-SOLUTION-PLAN.md` | 2026-08-25 | CORRECTED | Detective review found modules 00–05 had wrong file-count data | no |
| `.../01-hermes-wsl-drvfs-git-performance/00-INDEX-AND-EXECUTIVE-SUMMARY.md` | 2026-08-25 | OLD | Package index, "PROPOSED & FULLY SPECIFIED FOR VERIFICATION" | no |

## 10. Apex KB lifecycle repair / finalization (handoff bundle; superseded by shipped apex-kb CLI)
| Path | Date | Status | What it was | Bannered? |
|---|---|---|---|---|
| `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/Old/Apex-KB_UpdatePlan.md` | ~2026-06 | OLD | KB change-planner report (folder "Old") | no |
| `.../Old/Apex KB Phase 2 Minimal Value Contract — MacroMeso Change Plan.md` | ~2026-06 | OLD | Phase-2 macro/meso change plan | no |
| `.../Old/apex-kb-v2-planning-handover.md` | ~2026-06 | OLD | KB v2 planning handover | no |
| `.../Old/codex-old-agent-kb-execution-process-audit.md` | ~2026-06 | OLD | Old-agent KB execution audit | no |
| `.../NextFinalization/Apex KB v3 P0–P2 Closure Patch Plan.md` | ~2026-07 | SUPERSEDED | v3 P0–P2 closure patch plan | no |
| `.../NextFinalization/apex-kb-v3-repair-patch-plan/09-final-execution-order.md` (+ `targets/012-package-manifest-plan-ledger.md`) | ~2026-07 | SUPERSEDED | v3 repair patch-plan execution order | no |
| `.../NextFinalization/post-codex-p0-p2-closure-audit/PatchPlan_v2.md`, `.../connector-detective-audit-and-repair-plan.md` | ~2026-07 | CORRECTED | Post-codex closure audit + repair plans | no |
| `.../NewUpgrade10-7/connector-rhythm-orchestration/{03-implementation-plan,04-research-commission-r09-final-minimal-change-plan,patch-plan-handover}.md`, `.../patch-builder{,-v2}/validation-plan.md` | ~2026 | CORRECTED/FAILED | Connector-rhythm upgrade cycle (siblings `NewFailure.md`/`NewFailureAnalysis.md`) | no |

## 11. WeeklyFlow prompt-failure corrections (2026-07-07)
| Path | Date | Status | What it was | Bannered? |
|---|---|---|---|---|
| `apex-meta/handoff/WeklyFlow/correction/plan.md` | 2026-07 | CORRECTED | Redo of Plan/Sync/Session ↔ Weekly Orchestrator bridge | no |
| `apex-meta/handoff/WeklyFlow/agent-mode-prompt-failure-pattern-analysis-correction-2026-07-07.md` | 2026-07-07 | CORRECTED | Correction of agent-mode prompt-failure pattern | no |
| `apex-meta/handoff/WeklyFlow/{patch-plan-reproduction-handoff,project-patch-plan-context-handoff}-2026-07-07.md`, `.../step1_prompt_blocker_cleanup_full_plan.okf.md` | 2026-07-07 | OLD/CORRECTED | Patch-plan handoffs + blocker cleanup | no |
| `apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md` | 2026-07-07 | OLD | Prompt-blocker cleanup plan | no |

## 12. Misc
| Path | Date | Status | What it was | Bannered? |
|---|---|---|---|---|
| `ki-basis/docs/openproject/openproject-cli-antigravity-pilot/DRAFT-IMPLEMENTATION-PLAN.md` | ~2026-09 | SUPERSEDED | OpenProject CLI pilot plan; superseded by DECISION-2026-09-28 | **yes** |
| `apex-meta/SmallSkills/OKF_Format/adoption-project/leela-ssot-migration-assessment.md` | 2026-09-01 | DEFERRED | OKF 0.1→0.2 SSOT migration "not executed yet" | no |
| `apex-meta/AI-Snippets/AIFailure/ClaudeCodeFailedPlan.md`, `.../ClaudePlanContextFuckup.md` | undated | FAILED | Captured examples of a failed AI plan / context failure (lessons) | no |

---

## Counts (approximate)
- **OLD** ~40 · **SUPERSEDED** ~15 · **CORRECTED** ~9 · **FAILED** ~6 · **DEFERRED** ~4 → **~70–75 plan files** total.

## Deliberately NOT listed (still active — do not archive)
- `apex-meta/orchestration/architecture-improvements/03-wsl2-native-stack-consolidation/03-execution-plan.md` — the current 2026-09-26 consolidation baseline.
- `apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md` and `PLAN-infra-docs-remediation-2026-09-28.md` — current close-out plans.
- `apex-meta/handoff/universal-ai-instruction-system/**` — active (patched through 2026-09-23).
- `apex-meta/apex-kb-cli/docs/**`, `apex-meta/informatics/migration.md` — current shipped CLI / policy.

## Borderline — worth an operator check before treating as old
- `apex-meta/SmallSkills/OKF_Format/adoption-project/implementation-waves-w0-w2.md` (approved 2026-09-01; separate informatics workstream).
- `apex-meta/tools/project-improvement-orchestration-weekly/00-orchestration-spine/05-TARGET-STRUCTURE-IMPLEMENTATION-PLAN.md` (may be the live weekly-orchestrator's design home).
- `apex-meta/apex-kb-cli/docs/apex-kb-improvement-plan.md`.

_Excluded from this index: vendored/third-party material (`source-knowledge/`, `apex-meta/kb/`, `ApexDefinition&OldVersions/`, any `/raw/` path, `antigravity-awesome-skills`, `bmad`), `researcher-attachments-*` evidence duplicates, and ~130 simulation fixtures (`flow-execution-card.md`, `weekly_plan.md`) — those are outputs, not plans._
