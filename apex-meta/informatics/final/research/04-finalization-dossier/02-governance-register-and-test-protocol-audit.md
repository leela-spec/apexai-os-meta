---
type: Reference
id: V2-DOSSIER-02-GOVERNANCE-TEST-AUDIT
title: Step 2 — File-by-File Audit & Patches: Decision Register (01), Test Protocol (04), Status Index (12), and Bundle Index
description: Detailed analysis and surgical patches for the Decision Register, Empirical Read-Trace Test Protocol, Status Index, and v2 bundle index after ResearchOfFile10 completion.
status: current
tags: [dossier, step-2, decision-register, test-protocol, status-index, patches]
---

# Step 2 — File-by-File Audit & Patches: Decision Register, Test Protocol & Status Index

> **Context Loaded for Step 2 (`AD-04` Bounded Context):**
> - [01-decision-register.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/01-decision-register.md)
> - [04-empirical-test-protocol.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/04-empirical-test-protocol.md)
> - [12-status-index.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/12-status-index.md)
> - [v2-always-on-architecture/index.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/index.md)
> - Research Synthesis: [RESULTS-11-synthesis.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/RESULTS-11-synthesis.md)

---

## 1. File Audit: [04-empirical-test-protocol.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/04-empirical-test-protocol.md)

### A. Current State-of-the-Art Assessment — **Stale `v0.3` Tag Names Found**
- **What is already good:** The four-arm experimental design (Baseline vs. Gated vs. Ungated Control vs. Split Files), the 12-task matrix (`T1`–`T12` + adversarial `T13`–`T14`), the blind rubric, and the pre-registered decision thresholds (`<20%` bloat rate + `>15pp` over Arm C) are methodologically sound and endorsed by [RESULTS-01](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-01-gating-efficacy.md).
- **What is broken / stale:**
  1. **Task Matrix (§3, lines 70–81) Still Uses Retired `v0.3` Tag Names:** References `<always>`, `<writing>`, `<files>`, `<dispatch>`, and `deepen_when=ranking_tags` / `deepen_when=bundle_layout`—none of which exist in `v0.5` or `v1.0`! In `v1.0`, those tags are `<stop_repairing>`, `<authoring>`, `<editing>`, `<trade_off>`, `<handover>`, `<iterative>`, `<schemas>`, `<new_machinery>`, and `<detour>`.
  2. **Missing Head-to-Head Serialization Comparison (`RP-06`):** `RESULTS-06` and operator decision `Option 6C` require comparing `v1.0-3A` (Pure XML) against `v1.0-3B` (Hybrid XML + Conditional Table) in the protocol (`Arm B1` vs. `Arm B2`).

### B. Exact Patch Applied to [04-empirical-test-protocol.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/04-empirical-test-protocol.md) `[P0 | I94/E95/R05]`
- Updated §2 (Experimental Arms) to include `Arm B1` ([13-candidate-3A-xml.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/13-candidate-3A-xml.md)) and `Arm B2` ([14-candidate-3B-hybrid.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/14-candidate-3B-hybrid.md)).
- Updated every row of §3 (Task Matrix `T1`–`T12`), §5 (Scoring Rubric), and §8b (`Arms E–H`) from retired `v0.3`/`v0.4` tag names to the exact `v1.0` tags.

---

## 2. File Audit: [01-decision-register.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/01-decision-register.md)

### A. Current State-of-the-Art Assessment
- **What is already good:** Parts A, B, D, F, and G provide a transparent, honest audit trail of settled vs. superseded decisions and pre-registered falsification conditions.
- **What needs updating after `ResearchOfFile10`:**
  1. **Part F2 (`DEC-21`):** Needs the verified 2026 loader matrix findings from `RP-10` and the IDE `<RULE>` preprocessor rationale explaining why byte-identical `<apex_contract>` blocks beat `@AGENTS.md` import shims.
  2. **New Finalized `v1.0` Decisions (`DEC-22`..`DEC-24`):**
     - `DEC-22`: Two-Layer Separation & `base_ref="apex-meta/informatics/"` Portability (`RP-09` & `RP-10`).
     - `DEC-23`: Removal of `deepen_when=` Attributes (-99 tokens across 5 tags, `RP-08`) and Rejection of Hard 1,000-Token Wall under Prompt Caching (`RP-03` & `RP-09`).
     - `DEC-24`: Empirical Wording Upgrades for `<target>` (`RP-05` SpecBench + `RP-07` FixedBench no-op legitimacy), `<communication>` (`RP-04` Cool Blue + warranted uncertainty vs. empty hedges), and `<new_machinery>` (`RP-07` pre-action blocker requirement).

### B. Exact Patch Applied to [01-decision-register.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/01-decision-register.md) `[P0 | I93/E95/R05]`
- Added Part H (`DEC-22` through `DEC-24` — Post-`ResearchOfFile10` Finalized `v1.0` Decisions) and updated Part E (`DEC-O1`..`DEC-O6`) and Part F (`RP-02` vector retrieval falsifier closed).

---

## 3. File Audit: [12-status-index.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/12-status-index.md) & [v2-always-on-architecture/index.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/index.md)

### A. Current State-of-the-Art Assessment
- Both files were written *before* `ResearchOfFile10` returned (`12-status-index.md` line 189 still states *"No research has been executed. Ten packets are written and dispatched, zero returned"*), and neither indexes `ResearchOfFile10/`, `13-candidate-3A-xml.md`, `14-candidate-3B-hybrid.md`, or `FinalizationDossier/`.

### B. Exact Patch Applied `[P1 | I90/E96/R04]`
- Updated [12-status-index.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/12-status-index.md) §3, §4, §5, and §8 to record all 10 completed research packets (`RESULTS-01`..`11`), the new `DEC-22`..`DEC-24` decisions, and the finalized `v1.0` artifacts.
- Updated [v2-always-on-architecture/index.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/index.md) with complete clickable links to every file in `v2-always-on-architecture/`, `ResearchOfFile10/`, and `FinalizationDossier/`.
