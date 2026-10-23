---
okf_version: "0.2"
title: V2 Always-On Architecture — Finalized v1.0 Candidates, Blueprint, Research & Dossier
description: Separate version branch holding the finalized v1.0 always-on contract architecture, decision register, non-active AGENTS.md two-layer blueprint, empirical test protocol, completed 10-packet research results, and step-by-step finalization dossier.
tags: [v2, always-on, architecture, decisions, blueprint, research-results, finalization-dossier, v1.0]
---

# V2 Always-On Architecture (`v1.0` Finalized Specification Suite)

> **Status: Specification & Candidates Finalized (`v1.0`) — Ready for Future System Integration.**
> Every artifact in this folder is a finalized candidate, blueprint, research result, or engineering audit dossier. Nothing here modifies the live root `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md` until you trigger the system-integration step.

---

## 1. Finalization Dossier (Step-by-Step File Audits & Patch Rationale)

Start at **[FinalizationDossier/index.md](FinalizationDossier/index.md)** to click through the file-by-file analysis:

| Step | Dossier File | What It Covers |
|---:|---|---|
| **0** | [FinalizationDossier/00-research-critique-and-architecture-design.md](FinalizationDossier/00-research-critique-and-architecture-design.md) | Critical audit of `ResearchOfFile10` (`RESULTS-01`..`11`) — what is verified, where we push back (`<hold_position>`), and the `v1.0` 2-Layer architecture diagram. |
| **1** | [FinalizationDossier/01-contract-and-blueprint-suite-audit.md](FinalizationDossier/01-contract-and-blueprint-suite-audit.md) | Audit & patches for Contract Candidates `3A` ([13](13-candidate-3A-xml.md)) & `3B` ([14](14-candidate-3B-hybrid.md)), Blueprint ([03](03-BLUEPRINT-agents.md)), and Surface Architecture ([11](11-instruction-surface-architecture.md)). |
| **2** | [FinalizationDossier/02-governance-register-and-test-protocol-audit.md](FinalizationDossier/02-governance-register-and-test-protocol-audit.md) | Audit & patches for Decision Register ([01](01-decision-register.md)), Empirical Test Protocol ([04](04-empirical-test-protocol.md)), and Status Index ([12](12-status-index.md)). |
| **3** | [FinalizationDossier/03-root-index-and-router-audit.md](FinalizationDossier/03-root-index-and-router-audit.md) | Audit & patches for [apex-meta/informatics/index.md](../../../index.md) and [general-informatics-router.md](../../../general-informatics-router.md). |
| **4** | [FinalizationDossier/04-writing-and-file-architecture-audit.md](FinalizationDossier/04-writing-and-file-architecture-audit.md) | Audit & patches for [writing-profile.md](../../../writing-profile.md) and [file-architecture.md](../../../file-architecture.md). |
| **5** | [FinalizationDossier/05-execution-antidrift-governance-audit.md](FinalizationDossier/05-execution-antidrift-governance-audit.md) | Audit & patches for [execution-modes.md](../../../execution-modes.md), [anti-drift-rules.md](../../../anti-drift-rules.md), and [governance-schemas.md](../../../governance-schemas.md). |
| **6** | [FinalizationDossier/06-cross-dependency-and-verification-report.md](FinalizationDossier/06-cross-dependency-and-verification-report.md) | Complete cross-dependency matrix, second-iteration reconciliation, and `okf_validator.py` + `pytest` verification report. |

---

## 2. Core Architecture & Candidate Files (`v2-always-on-architecture/`)

| File | Role | Status |
|---|---|---|
| [12-status-index.md](12-status-index.md) | **Master Coverage Index.** Every defect, decision, research packet, and backlog item. | **Current (`v1.0`)** |
| [13-candidate-3A-xml.md](13-candidate-3A-xml.md) | **Finalized `v1.0-3A` Contract Block (Pure Named XML).** `1,556` repo tokens (`1,305` BPE), `base_ref`, no `deepen_when`, `RP-04`/`05`/`07` wording applied. | **Finalized Candidate `3A`** |
| [14-candidate-3B-hybrid.md](14-candidate-3B-hybrid.md) | **Finalized `v1.0-3B` Contract Block (Hybrid XML + Dispatch Table).** `1,510` repo tokens (`1,260` BPE), `41` lines. | **Finalized Candidate `3B`** |
| [03-BLUEPRINT-agents.md](03-BLUEPRINT-agents.md) | **Two-Layer `AGENTS.md` Blueprint (`v1.0`).** Shows Layer 1 (`<apex_contract>`) + Layer 2 (`295` tokens repo-specific context) = `1,805–1,851` tokens total. | **Finalized Blueprint** |
| [11-instruction-surface-architecture.md](11-instruction-surface-architecture.md) | **Five-Surface & Two-Layer Architecture (`v1.0`).** Verified 2026 loader matrix (`RP-10`) and `DEC-21`/`DEC-22` resolution. | **Current (`v1.0`)** |
| [01-decision-register.md](01-decision-register.md) | **Decision Register (`DEC-01`..`DEC-24`).** Settled, superseded, mechanical facts, falsification conditions, and post-research `v1.0` decisions. | **Current (`v1.0`)** |
| [04-empirical-test-protocol.md](04-empirical-test-protocol.md) | **Empirical Read-Trace Test Protocol (`v1.0`).** Updated to `v1.0` tag names and `Arm B1` (`3A`) vs. `Arm B2` (`3B`) comparison. | **Ready to Run** |
| [09-contract-block-v0.5.md](09-contract-block-v0.5.md) | Pre-research `v0.5` candidate (1,622 tokens). | *Superseded by `13` & `14`* |
| [08-discussion-and-open-threads.md](08-discussion-and-open-threads.md) | Operator feedback on `v0.4` that produced `v0.5` and `RP-04`..`RP-08`. | *Historical Record* |
| [07-contract-block-v0.4.md](07-contract-block-v0.4.md) | Earlier `v0.4` candidate (1,357 tokens). | *Superseded by `09`* |
| [06-contract-block-revision-proposal.md](06-contract-block-revision-proposal.md) | Revision proposal from `v0.3` to `v0.4`. | *Historical Record* |
| [05-research-prompt-packets.md](05-research-prompt-packets.md) | The ten research prompt packets (`RP-01`..`RP-10`). | *Executed in `ResearchOfFile10/`* |
| [10-RESEARCH-EXECUTION-HANDOVER.md](10-RESEARCH-EXECUTION-HANDOVER.md) | Handover that dispatched the ten research packets. | *Executed in `ResearchOfFile10/`* |
| [02-informatics-contract-block.md](02-informatics-contract-block.md) | Earliest `v0.3` candidate (721 tokens). | *Superseded by `07`* |

---

## 3. Executed Research Packets (`ResearchOfFile10/`)

- [ResearchOfFile10/RESULTS-00-progress.md](ResearchOfFile10/RESULTS-00-progress.md) — Progress ledger (10/10 complete)
- [ResearchOfFile10/RESULTS-11-synthesis.md](ResearchOfFile10/RESULTS-11-synthesis.md) — Ten-packet synthesis
- Individual Packet Reports (`RESULTS-01` through `RESULTS-10`): located in `ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/`.
