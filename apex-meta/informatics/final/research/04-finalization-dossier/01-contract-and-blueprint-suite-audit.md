---
type: Reference
id: V2-DOSSIER-01-CONTRACT-BLUEPRINT-AUDIT
title: Step 1 — File-by-File Audit & Patches: Contract Block (09, 13, 14), Blueprint (03), and Surface Architecture (11)
description: Detailed analysis, research verification, and exact patches for the Always-On Contract candidates, the AGENTS.md Blueprint, and the Instruction Surface Architecture document.
status: current
tags: [dossier, step-1, contract-block, blueprint, surface-architecture, patches]
---

# Step 1 — File-by-File Audit & Patches: Contract Block, Blueprint & Surface Architecture

> **Context Loaded for Step 1 (`AD-04` Bounded Context):**
> - [09-contract-block-v0.5.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)
> - [13-candidate-3A-xml.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/13-candidate-3A-xml.md) & [14-candidate-3B-hybrid.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/14-candidate-3B-hybrid.md)
> - [03-BLUEPRINT-agents.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/03-BLUEPRINT-agents.md)
> - [11-instruction-surface-architecture.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/11-instruction-surface-architecture.md)
> - Research Packets: [RESULTS-04](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-04-register-terminology.md), [RESULTS-05](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md), [RESULTS-06](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-06-condition-syntax.md), [RESULTS-07](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md), [RESULTS-08](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-08-deepen-when-mechanics.md), [RESULTS-09](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md), [RESULTS-10](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-10-surface-layering.md).

---

## 1. File Audit: [09-contract-block-v0.5.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md) $\rightarrow$ Finalized Candidates [13-candidate-3A-xml.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/13-candidate-3A-xml.md) & [14-candidate-3B-hybrid.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/14-candidate-3B-hybrid.md)

### A. Current State-of-the-Art Assessment
- **What is already good:** `v0.5` restored the three missing execution gates (`<handover>`, `<iterative>`, `<sync>`), introduced `<hold_position>` (anti-sycophancy), separated overcorrection out of `<editing>`, and added external source verification (`roughly three`) to `<ground>`.
- **What `ResearchOfFile10` proved needs improvement:**
  1. **`<target>` (`RP-05` & `RP-07` — `[P0 | I96/E94/R08]`):** `v0.5` relies on a negative ban (`"Never substitute acceptance criteria you authored yourself"`). [SpecBench (2026)](https://arxiv.org/abs/2605.21384) and [Ma et al. (2026)](https://arxiv.org/abs/2606.28430) show agents still treat passing self-written tests as completion unless given a **positive final requirement-by-requirement verification duty** while permitting diagnostic tests as supporting evidence. Furthermore, [FixedBench (2026)](https://arxiv.org/abs/2605.07769) shows a 35%–65% false-edit rate on already-resolved tasks unless the rule explicitly permits concluding **"no change is needed"**.
  2. **`<communication>` (`RP-04` — `[P1 | I90/E92/R06]`):** `v0.5` had a placeholder register and stated `"No hedging"`. `RESULTS-04` confirmed the **Insights Discovery "Cool Blue"** register and identified that `"No hedging"` contradicts `<ground>` when evidence is incomplete—forcing models to state unverified guesses with false certainty. Replaced with: *"State uncertainty plainly when evidence is incomplete; avoid empty hedges."*
  3. **`<new_machinery>` (`RP-07` — `[P1 | I91/E90/R08]`):** Upgraded to require naming the **exact requirement, blocker, or material risk** before creating any script, test, gate, schema, wrapper, or abstraction.
  4. **`deepen_when=` Removal & Count Correction (`RP-08` — `[P1 | I90/E90/R08]`):** `RESULTS-08` proved `deepen_when=` is not parsed by any runtime and caught that `v0.5` had **5** instances (not 6 as written in `09` §4 line 148). Dropping `deepen_when=` and sharpening `<pointers>` to *"Open one only when its condition matches and the inline summary is insufficient"* saves ~99 tokens.
  5. **`base_ref` Layer 1 Portability (`RP-09` & `RP-10` — `[P1 | I92/E88/R10]`):** Adding `base_ref="apex-meta/informatics/"` once on `<apex_contract v="1.0">` eliminates 6 repeated path prefixes (saving ~25 tokens) and makes the entire `<apex_contract>` body 100% portable across repositories.

### B. Patches Applied
- Preserved [09-contract-block-v0.5.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md) as the historical `v0.5` record with a top banner pointing to the finalized `v1.0` candidates (`13` and `14`) and a factual note correcting the 5-vs-6 `deepen_when` count and floor status.
- Finalized [13-candidate-3A-xml.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/13-candidate-3A-xml.md) (**1,556 repo tokens** / **1,305 BPE tokens**, 65 lines) and [14-candidate-3B-hybrid.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/14-candidate-3B-hybrid.md) (**1,510 repo tokens** / **1,260 BPE tokens**, 41 lines) with full per-rule provenance and measurement breakdowns.

---

## 2. File Audit: [03-BLUEPRINT-agents.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/03-BLUEPRINT-agents.md)

### A. Current State-of-the-Art Assessment — **4 Cross-File Drift Defects Found**
Inspecting [03-BLUEPRINT-agents.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/03-BLUEPRINT-agents.md) against `09-contract-block-v0.5.md` and `ResearchOfFile10` exposed **four serious staleness defects**:
1. **Stuck on `v0.4`:** Line 25 and line 80 still embed `CONTRACT BLOCK v0.4 (1,357 tokens)`, omitting `<hold_position>`, `<handover>`, `<iterative>`, and `<sync>`.
2. **Unapplied `Git Dispatch` Deduplication (`140 tokens` wasted):** In `09-contract-block-v0.5.md` §1 line 28, the author claimed: *"Git behaviour stated once — `<sync>` carries it; the blueprint's `Git Dispatch` section keeps only the repo-specific ext4/`/mnt/c` fact."* Yet `03-BLUEPRINT-agents.md` lines 92–99 still retained **all 7 `Git Dispatch` bullets** (185 tokens), duplicating `<sync>`!
3. **Withdrawn Option D Still Recommended:** In `03-BLUEPRINT-agents.md` §4 line 152, the file still recommended *"Option D — Move the infrastructure banner out of `AGENTS.md` (-215 tokens)"*, even though `09-contract-block-v0.5.md` §4 line 164 recorded that the operator **explicitly rejected and withdrew Option D** because agents must always see the current stack topology!
4. **Missing 2-Layer Separation (`RP-10`):** Did not reflect the explicit separation between **Layer 1 (Universal Contract)** and **Layer 2 (Repository-Specific Operating Context)**.

### B. Exact Patch Applied to [03-BLUEPRINT-agents.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/03-BLUEPRINT-agents.md) `[P0 | I95/E96/R05]`
- Upgraded the blueprint to `v1.0` referencing [13-candidate-3A-xml.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/13-candidate-3A-xml.md) (1,556 tokens) and [14-candidate-3B-hybrid.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/14-candidate-3B-hybrid.md) (1,510 tokens).
- Slimmed `## Git & Workspace Environment (Repo-Specific)` to the **45-token WSL2 ext4 / `/mnt/c` rule**, eliminating the 140-token duplication with `<sync>`.
- Removed the withdrawn Option D recommendation and updated the net token budget table:
  - Kept Repo-Specific Layer 2 (Infrastructure Banner `215` + WSL2 Filesystem Rule `45` + Completion Reporting `35`) = **295 tokens** (down from 435!).
  - Combined Blueprint Total: **1,851 tokens (`3A-XML`)** or **1,805 tokens (`3B-Hybrid`)** — down from `2,057` in `v0.5`!

---

## 3. File Audit: [11-instruction-surface-architecture.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/11-instruction-surface-architecture.md)

### A. Current State-of-the-Art Assessment
- **What is already good:** Accurately mapped the 5 instruction files in the repository, identified the live `D10` defect (`GEMINI.md` missing informatics routing), and framed the two-layer (Universal vs. Repo-Specific) problem.
- **What was unfinished:** Marked `status: open_architecture`; §3 listed loader behaviors as `"Assumed"`; §4 had 5 unanswered questions (`Q1`–`Q5`) waiting on `RP-10`; §5 held a loose provisional position.

### B. Exact Patch Applied to [11-instruction-surface-architecture.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/11-instruction-surface-architecture.md) `[P0 | I94/E95/R06]`
- Promoted status to `current` (`v1.0`).
- Replaced §3's `"Assumed"` table with the verified 2026 vendor loader matrix from [RESULTS-10-surface-layering.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-10-surface-layering.md) (citing [Anthropic Claude Code Memory Docs](https://code.claude.com/docs/en/memory), [Gemini CLI Context Docs](https://geminicli.com/docs/cli/gemini-md/), and [GitHub Copilot Custom Instructions Matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support)).
- Resolved `Q1`–`Q5` with explicit engineering decisions:
  - **Layering (`Option 2A` + `Option 5A`):** Layer 1 (`<apex_contract v="1.0" base_ref="apex-meta/informatics/">`) is 100% portable across repos; Layer 2 (`Infrastructure Banner`, `WSL2 Filesystem Rule`, `Completion Reporting`) sits outside `<apex_contract>` in the same file.
  - **Multi-Surface Synchronization (`Option 1A` vs. `@import` Shims):** Documented why physical byte-identical `<apex_contract>` blocks across `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` (verified by `pytest` and DITA single-source projection) beat `@AGENTS.md` import shims—because IDE rule injectors (Antigravity `<RULE>`, VS Code extensions, Windsurf) read raw files without executing CLI `@` preprocessors.
