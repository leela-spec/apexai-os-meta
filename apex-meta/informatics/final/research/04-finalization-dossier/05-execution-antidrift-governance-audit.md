---
type: Reference
id: V2-DOSSIER-05-EXEC-ANTIDRIFT-GOV
title: Step 5 — Execution Modes, Anti-Drift Rules, Governance Schemas & RBL-07 Audit
description: Step 5 audit and patch specification for execution-modes.md, anti-drift-rules.md, governance-schemas.md, and RBL-07 token redaction against ResearchOfFile10.
status: current
tags: [finalization-dossier, step-5, execution-modes, anti-drift-rules, governance-schemas, v1.0]
---

# Step 5 Audit & Patch Specification: `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md` & `RBL-07`

> **Target Files Audited:**
> - [`apex-meta/informatics/execution-modes.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/execution-modes.md) (`ADPT-EXEC-MODES-v0.2`)
> - [`apex-meta/informatics/anti-drift-rules.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/anti-drift-rules.md) (`GOV-ANTI-DRIFT-v0.2`)
> - [`apex-meta/informatics/governance-schemas.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/governance-schemas.md) (`GOV-SCHEMAS-v0.2`)
> - [`apex-meta/AI-Snippets/Orga/2Dos.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Orga/2Dos.md) & [`apex-meta/AI-Snippets/Orga/2Dos Ai Instructions.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (`RBL-07`)
>
> **Research Inputs Evaluated:** [`RESULTS-05-self-authored-criteria.md`](../ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md), [`RESULTS-07-over-building.md`](../ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md), [`RESULTS-11-synthesis.md`](../ResearchOfFile10/RESULTS-11-synthesis.md) (`RBL-07`).

---

## 1. File-by-File State-of-the-Art & Research Alignment Matrix

| File | Current SotA Status | Research Findings (`RP-05`, `RP-07`, `RBL-07`) | Verdict & Required Action |
|---|---|---|---|
| **[`execution-modes.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/execution-modes.md)** | Strong (`EM-01`..`EM-12`, explicit `<execution_dispatch>` `IF..THEN..ELSE` block, 6 task adapters, worked `patch_intent.v1` example). | Missing the scoped-push branch of `<sync>` in `EM-12` (`git push <paths>` vs. full `sync`/`synch`) and lacks a closing `## 8. Execution Failure Modes & Not-To-Dos` section (`WP-25`). | **SURGICAL PATCH** (`EM-12` + `## 8` closing failure-mode block) |
| **[`anti-drift-rules.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/anti-drift-rules.md)** | Strong (`AD-01`..`AD-28` across 4 sections, closing failure-modes block). | Needs canonical synchronization with the `v1.0` contract's empirical upgrades (`DEC-24`): `RP-05` SpecBench positive requirement check (`AD-01`), `RP-07` FixedBench no-op permission (`AD-01`) & pre-action blocker requirement (`AD-25`), and unified `<hold_position>` anti-sycophancy + narrow-correction discipline (`AD-22`). | **SURGICAL PATCH** (`AD-01`, `AD-22`, `AD-25`) |
| **[`governance-schemas.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/governance-schemas.md)** | Already 100% compliant (`GS-01`..`GS-22`, single-owner links to `FA-05`, `FA-06`, `patch-intent-schema.json`, `execution-modes.md`, and `writing-profile.md`). | Zero conflicts with `ResearchOfFile10`; preserves durable ID immutability (`WP-15`) by documenting retired IDs `GS-16`, `GS-18`, `GS-19`. | **KEEP AS-IS (`0` edits needed)** |
| **[`2Dos.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Orga/2Dos.md) & [`2Dos Ai Instructions.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Orga/2Dos%20Ai%20Instructions.md)** | Contains plaintext OpenProject password and API token at lines 122–125 (`2Dos.md`) and lines 66–69 (`2Dos Ai Instructions.md`). | `RBL-07` flagged plaintext OpenProject credentials in `apex-meta/AI-Snippets/Orga/`. | **REDACT CREDENTIALS (`RBL-07`)** |

---

## 2. Detailed Audit of `execution-modes.md` (`ADPT-EXEC-MODES-v0.2`)

### 2.1 What Is Already Good
1. **Explicit `IF..THEN..ELSE` Dispatch Block (`<execution_dispatch>`):** Routes across all 6 adapters (`#2-adapter-1-qa-decision-matrix` through `#7-adapter-6-git-sync--file-preservation`) with zero ambiguity.
2. **Raw 3-Metric Decision Matrix (`EM-06`):** Enforces mechanism, concrete grounding (example/process/user story), and raw unaggregated `(I<val>/E<val>/R<val>)` tags without synthetic math formulas.
3. **File-Producing Iterative & MMM Loop (`EM-10`):** Explicitly prevents upfront context bloat (`6.1`) and mandates that each iteration materializes dedicated files (`00-master-matrix.md`, `01-implementation-map.md`, `step-XX-<module>.md`).

### 2.2 Surgical Improvements (`EM-12` & Closing Failure-Mode Section)
1. **Complete `<sync>` Alignment in `EM-12` (`[P2 | I84/E92/R08]`):**
   - In `v1.0`, `<sync>` defines two distinct git behaviors:
     - **Scoped Push (`git push <paths>`):** Stage only the named paths, commit, and push (`git pull --rebase` on non-fast-forward), ignoring unrelated dirty files.
     - **Full Sync (`sync` / `synch`):** Pull (`--rebase`) and push after a status check so no untracked or modified work is lost; preserve unrequested dirty files in a separate commit rather than dropping them, deleting only files explicitly marked for removal.
   - Adding the scoped-push branch alongside the `sync`/`synch` branch in `EM-12` makes `EM-12` the complete single canonical owner of `<sync>`.
2. **Terminal-Position Failure Modes Section (`WP-25` — `[P2 | I82/E88/R06]`):**
   - Adds `## 8. Execution Failure Modes & Not-To-Dos` at the end of `execution-modes.md` so the file closes with operative anti-failure guards.

---

## 3. Detailed Audit of `anti-drift-rules.md` (`GOV-ANTI-DRIFT-v0.2`)

### 3.1 Synchronizing `v1.0` Contract Upgrades (`RP-05`, `RP-07`, `<hold_position>`)
To ensure 100% bidirectional traceability between the Plane 1 `<apex_contract v="1.0">` and its Plane 4 canonical library owner (`anti-drift-rules.md`), three rules receive targeted refinements:

1. **`AD-01` (`TARGET Dominance Invariant` — `RP-05` SpecBench & `RP-07` FixedBench `[P0 | I100/E96/R05]`):**
   - *Research Basis:* `RP-05` (SpecBench, `arXiv:2603.16849`) proved that positive requirement-by-requirement final checks outperform open-ended verification loops, and `RP-07` (FixedBench, `arXiv:2603.22663`) proved that explicitly legitimizing `"no change is needed"` (with proof) cuts unnecessary code mutations on already-correct artifacts by ~20 percentage points.
   - *Exact Addition to `AD-01`:* Append: `"Before concluding, positively verify each stated requirement against the output. When evidence shows no change is needed, report that finding with its proof as the complete deliverable."`
2. **`AD-22` (`Surgical Edits & Anti-Overcorrection (Hold Position)` — `[P2 | I88/E91/R08]`):**
   - *Research Basis:* `<hold_position>` in `v1.0` combines anti-sycophancy (`"Update a conclusion only when new evidence, a missed constraint, or a concrete flaw is shown—never from pushback alone"`) with narrow correction discipline (`"Make targeted, localized edits in response to operator feedback; never wipe out surrounding valid content or swing to an extreme opposite design"`). Preserving the exact substring `Surgical Edits & Anti-Overcorrection` in the rule title also satisfies `test_olt_05_anti_overcorrection_and_asset_preservation` in `test_tier5_adversarial.py`.
   - *Exact Update to `AD-22`:* Include the anti-sycophancy sentence at the start of `AD-22` so `AD-22` owns both halves of `<hold_position>`.
3. **`AD-25` (`Pre-Addition Gate & Machinery Rule` — `RP-07` `[P2 | I88/E92/R08]`):**
   - *Research Basis:* `RP-07` (FixedBench) showed that requiring an agent to name the exact requirement, blocker, or material risk *before* introducing new abstractions, wrappers, configs, refactors, or verification gates acts as a high-leverage pre-action pause.
   - *Exact Update to `AD-25`:* Prefix `AD-25` with: `"Before adding any abstraction, wrapper, config, refactor, or verification gate, name the exact requirement, blocker, or material risk it resolves."`

---

## 4. Detailed Audit of `governance-schemas.md` (`GOV-SCHEMAS-v0.2`)

### 4.1 Why `governance-schemas.md` Requires Zero Edits
- **Single-Owner Compliance (`WP-23`):** `GS-06` and `GS-07` delegate frontmatter schemas to `FA-05`/`FA-06`; `GS-09` delegates the JSON Schema to `patch-intent-schema.json` and the worked example to `execution-modes.md` §4.2; `GS-12` and `GS-13` delegate decision matrix and bake-off formats to `execution-modes.md` §2.1 and §3.1; `GS-14` and `GS-17` delegate directive ceilings and tier definitions to `WP-18` and `WP-07`.
- **Immutable Durable IDs (`WP-15`):** Explains retired IDs `GS-16`, `GS-18`, `GS-19` cleanly without renumbering `GS-20`..`GS-22`.
- **Terminal-Position Content (`WP-25`):** Places `## 4. Traceability & Reference Grounding` *before* `## 5. Conformance Diagnostics & Validation Mapping`, closing the file with operative validation gates (`GS-20`..`GS-22`) and the `STE-SENTENCE-LENGTH` floor rule.

---

## 5. Credential Redaction (`RBL-07`)

- **Locations Found:**
  1. [`apex-meta/AI-Snippets/Orga/2Dos.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Orga/2Dos.md#L122-L125) (lines 122–125)
  2. [`apex-meta/AI-Snippets/Orga/2Dos Ai Instructions.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Orga/2Dos%20Ai%20Instructions.md#L66-L69) (lines 66–69)
- **Action:** Replace both plaintext password/API-token blocks with `[REDACTED — stored in ~/.config/openproject/op.env per OpenProject safety policy]`.
