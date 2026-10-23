---
type: Reference
id: V2-DOSSIER-04-WRITING-FILE-ARCH-AUDIT
title: Step 4 — File-by-File Audit & Patches: Writing Profile (writing-profile.md) & File Architecture (file-architecture.md)
description: Detailed analysis, research verification, and surgical patches for writing-profile.md and file-architecture.md integrating RP-03, RP-04, RP-09, and RP-10.
status: current
tags: [dossier, step-4, writing-profile, file-architecture, rp-04, rp-09, rp-10]
---

# Step 4 — File-by-File Audit & Patches: `writing-profile.md` & `file-architecture.md`

> **Context Loaded for Step 4 (`AD-04` Bounded Context):**
> - [apex-meta/informatics/writing-profile.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/writing-profile.md)
> - [apex-meta/informatics/file-architecture.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/file-architecture.md)
> - Research Packets: [RESULTS-03](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-03-currency-check.md), [RESULTS-04](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-04-register-terminology.md), [RESULTS-06](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-06-condition-syntax.md), [RESULTS-09](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md), [RESULTS-10](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-10-surface-layering.md).

---

## 1. File Audit: [apex-meta/informatics/writing-profile.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/writing-profile.md)

### A. Current State-of-the-Art Assessment
- **What is already good:**
  1. Clean functional chapters ordered descending by significance (`P0` $\rightarrow$ `P3`), immutable tier-agnostic IDs (`WP-01`..`WP-25`), and canonical ownership of the `[P<tier> | I/E/R]` ranking table (`WP-07`).
  2. Includes `WP-23` (Single-Owner Instruction Reuse), `WP-24` (Clickable File References), and `WP-25` (Terminal-Position Operative Content), closing on `## 5. Writing Failure Modes & Not-To-Dos`.
- **What `ResearchOfFile10` (`RP-04`) Revealed Was Missing:**
  1. **Missing Canonical Grounding for `<communication>`'s Warranted Uncertainty vs. Empty Modal Hedging (`[P0 | I95/E96/R05]`):**
     - In `WP-03`, the rule stated: *"Avoid modal hedging (`should`, `may`, `might`, `could`) in normative specifications."*
     - [RESULTS-04](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-04-register-terminology.md) proved that a blanket ban on hedging causes models to project false certainty when empirical evidence is incomplete, conflicting with `WP-04` (`<ground>`). `WP-03` must explicitly distinguish **empty modal hedging** in directives from **warranted uncertainty** in factual reporting.
  2. **Missing Canonical Grounding for the Insights Discovery "Cool Blue" Analytical Register (`[P0 | I94/E95/R07]`):**
     - We added the `Cool Blue` analytical register to `<communication>` in the `v1.0` contract (`13` and `14`), whose canonical owner is `WP-05`. Updating `WP-05` to codify the **evidence-led, analytical technical register (Insights Discovery Cool Blue orientation: precise, objective, high density, no filler, no flattery, no unearned agreement)** ensures the contract and its canonical library module are 100% synchronized.

### B. Exact Patch Applied to [writing-profile.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/writing-profile.md)
- **Patched `WP-03`:** Added *"State factual uncertainty plainly when primary evidence is incomplete; never use empty modal hedges."*
- **Patched `WP-05`:** Added *"Maintain an evidence-led, analytical technical register (Insights Discovery Cool Blue orientation): precise, objective, high density, no filler, no flattery, and no unearned agreement."*

---

## 2. File Audit: [apex-meta/informatics/file-architecture.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/file-architecture.md)

### A. Current State-of-the-Art Assessment
- **What is already good:**
  1. Owns the Five-Plane Information Architecture (§2) and the canonical OKF v0.2 Frontmatter Schemas (`FA-05`, `FA-06`, `FA-13`).
  2. Duplicate `FA-04` was cleanly resolved (`FA-13`).
- **What `ResearchOfFile10` (`RP-09`, `RP-10`) & Structural Audit Revealed:**
  1. **Control Plane Surface List & Two-Layer Separation (`§2 Plane 1` & `FA-12`, `[P1 | I90/E92/R08]`):**
     - §2 Plane 1 listed `AGENTS.md, .claude/CLAUDE.md, root router`. Under `RP-10` ([11-instruction-surface-architecture.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/11-instruction-surface-architecture.md)), the primary root carriers are `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` (with `.claude/CLAUDE.md` and `.github/copilot-instructions.md` as secondary surfaces), structured into **Layer 1 (Portable Universal Contract with `base_ref`)** and **Layer 2 (Repo-Specific Context)**.
     - In `FA-12`, adding the `RP-09` prompt-caching principle explains *why* Plane 1 stays stable (~2,000 tokens, cached across turns at 78.5%–90% discount) while Plane 4/5 modules are loaded JIT only when inline summaries are insufficient.
  2. **Incomplete Bundle Topology Tree (`§4`, line 135 — `[P2 | I82/E95/R05]`):**
     - The tree listed `Agent_Setup/` as an isolated sub-bundle, but omitted `MMM/` (which also has its own `MMM/index.md` sub-bundle boundary).
  3. **Missing Terminal Failure-Mode Guard (`WP-25` & `<authoring>` Compliance — `[P1 | I88/E90/R06]`):**
     - Both `WP-25` and the contract's `<authoring>` rule state: *"Front-load critical rules; close on the failure-mode guard."* Yet `file-architecture.md` ended on `FA-12` without a closing `## 5. File Architecture Failure Modes & Not-To-Dos` section!

### B. Exact Patch Applied to [file-architecture.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/file-architecture.md)
- Updated §2 Plane 1 artifacts to `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, root router.
- Updated §4 topology tree to include `MMM/` alongside `Agent_Setup/`.
- Enriched `FA-12` with two-layer portability (`Layer 1` universal + `Layer 2` repo-specific) and stable-prefix prompt caching (`RP-09`/`RP-10`).
- Added a concise closing `## 5. Architecture Failure Modes & Not-To-Dos` section at the bottom of `file-architecture.md` to satisfy `WP-25` and `<authoring>`.
