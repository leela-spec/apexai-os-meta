---
type: Reference
id: V2-DOSSIER-03-INDEX-ROUTER-AUDIT
title: Step 3 — File-by-File Audit & Patches: Root Index (index.md) & Portable Router (general-informatics-router.md)
description: Detailed analysis, research verification, and surgical patch assessment for apex-meta/informatics/index.md and general-informatics-router.md.
status: current
tags: [dossier, step-3, index, router, dec-07, dec-14, dec-15]
---

# Step 3 — File-by-File Audit & Patches: `index.md` & `general-informatics-router.md`

> **Context Loaded for Step 3 (`AD-04` Bounded Context):**
> - [apex-meta/informatics/index.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/index.md)
> - [apex-meta/informatics/general-informatics-router.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/general-informatics-router.md)
> - Research Packets: [RESULTS-01](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-01-gating-efficacy.md), [RESULTS-02](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-02-vector-retrieval.md), [RESULTS-08](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-08-deepen-when-mechanics.md), [RESULTS-10](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-10-surface-layering.md).

---

## 1. File Audit: [apex-meta/informatics/index.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/index.md)

### A. Current State-of-the-Art Assessment
- **Measured Size:** 65 lines | 2,847 chars (~711 tokens — well within the `<1,000`-token `test_rcb_02_root_index_ceilings` gate).
- **What is already good:**
  1. Valid OKF v0.2 bundle index (`okf_version: "0.2"`, `title`, `description`, inline `tags`).
  2. Serves two active roles simultaneously:
     - **Today (pre-integration):** The target of `AGENTS.md` and `CLAUDE.md`'s `Informatics & Knowledge Routing` section.
     - **Under `v1.0` (`<authoring ref="index.md">`):** The exact hub opened when an agent authors or validates a governed specification file and needs to jump to [writing-profile.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/writing-profile.md) or [file-architecture.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/file-architecture.md).
- **What `ResearchOfFile10` & Cross-Reference Inspection Found:**
  1. **Missing Sub-Bundle Link in §4 (`[P2 | I82/E95/R05]`):** `file-architecture.md` lists both `Agent_Setup/` and `MMM/` as sub-bundles in the bundle topology tree, but `index.md` §4 only linked `[Agent Setup Sub-Bundle](Agent_Setup/index.md)` and omitted `[MMM Methodology Sub-Bundle](MMM/index.md)`.
  2. **Rule ID Range Verification (`§3`, lines 47–51):** Currently lists `AD-01..28` (we will verify exact ID ranges after auditing `anti-drift-rules.md` in Step 5).
  3. **Role Under `DEC-14`:** Until the `v1.0` contract block is installed into the live root `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` at system-integration time, `index.md` **must retain** §1 (Core Operational Invariants) and §2 (Conditional JIT Dispatch Gates) so live agents routing through `index.md` today continue to receive full dispatch instructions and all 196 existing tests pass.

### B. Exact Patch Applied to [apex-meta/informatics/index.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/index.md)
- Added `- [MMM Methodology Sub-Bundle](MMM/index.md) — Sub-bundle boundary index for Macro/Meso/Micro execution methodology.` to §4 so all sub-bundles in `apex-meta/informatics/` are explicitly linked from the root bundle index (`WP-24`).

---

## 2. File Audit: [apex-meta/informatics/general-informatics-router.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/general-informatics-router.md)

### A. Current State-of-the-Art Assessment
- **Measured Size:** 43 lines | 1,988 chars (`497` estimated tokens — right at the `<= 2,000` char / `<= 500` token boundary enforced by `test_rcb_01_general_router_ceilings` and `test_live_07_general_router_compactness`).
- **What is already good:**
  - Respects `DEC-07` (*"`general-informatics-router.md` stays byte-identical to baseline; its 500-token ceiling is not relaxed"*).
  - Acts as the **ultra-lean (`<500`-token) portable router tier**, complementing the **full (`~1,510–1,556`-token) portable always-on contract tier** in [13-candidate-3A-xml.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/13-candidate-3A-xml.md) and [14-candidate-3B-hybrid.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/14-candidate-3B-hybrid.md).
- **Verdict (`[P0 | I95/E98/R02]`):** **Keep byte-identical (`0` edits).** Modifying `general-informatics-router.md` would violate `DEC-07` and break the `<= 2,000`-character test gate.
