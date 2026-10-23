---
type: Reference
id: V2-DOSSIER-06-CROSS-DEPENDENCY-REPORT
title: Step 6 — Cross-Dependency Checkup & Verification Report
description: Cross-file dependency audit across all developed v1.0 candidate files, canonical Plane 4 library files, and automated validator/pytest suites.
status: current
tags: [finalization-dossier, step-6, cross-dependency, verification, v1.0]
---

# Step 6: Cross-Dependency Checkup & Verification Report

> **Purpose:** Final cross-file consistency checkup across all developed candidate files (`v2-always-on-architecture/`), canonical library files (`apex-meta/informatics/`), and the automated conformance/adversarial test suite (`okf_validator.py` + `pytest`).
> **Scope Boundary:** Confirms that all developed candidate, blueprint, and library files are finalized to `v1.0` without modifying live root `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md` (which remain untouched until the operator triggers system integration).

---

## 1. Cross-Dependency Audit Matrix (What Changed & What Depending Files Required)

During the step-by-step audit and patching loop (Steps 0–5), every file mutation was checked against downstream and upstream dependents. The table below records the **7 cross-dependencies** detected and resolved during this pass:

| # | Originating Change | Dependent File(s) Affected | Cross-Dependency Resolution Applied | Status |
|---|---|---|---|---|
| **CD-01** | Upgraded `<apex_contract>` from `v0.4`/`v0.5` to `v1.0` (`13-candidate-3A-xml.md` & `14-candidate-3B-hybrid.md`) and dropped all 5 `deepen_when=` attributes (`DEC-23`). | [`03-BLUEPRINT-agents.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/03-BLUEPRINT-agents.md), [`09-contract-block-v0.5.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md) | Upgraded `03-BLUEPRINT-agents.md` from `v0.4` to `v1.0`, removed the 140-token Layer 2 `Git Dispatch` duplication with `<sync>`, removed the withdrawn `Option D` recommendation, and marked `09-contract-block-v0.5.md` superseded by `13` & `14`. | **RESOLVED** |
| **CD-02** | Renamed `v0.3` tags (`<always>`, `<writing>`, `<files>`, `<dispatch>`) to `v1.0` tags (`<target>`..`<sync>`, `<authoring>`, `<editing>`, etc.). | [`04-empirical-test-protocol.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/04-empirical-test-protocol.md) (§4 `T1`–`T12`, §5 `T5` trap note, §8b `Arms E–H`) | Updated §3 (`Arm B1` = `3A`, `Arm B2` = `3B`), §4 (`T1`–`T12` expected gate triggers), §5 (`<authoring>` instead of `<writing>`), and §8b (`v1.0` instead of `v0.4`) so no retired tag names remain in active test steps. | **RESOLVED** |
| **CD-03** | Added empirical wording upgrades (`DEC-24`) into `v1.0` `<target>` (`RP-05` SpecBench + `RP-07` FixedBench), `<communication>` (`RP-04` Cool Blue + warranted uncertainty), `<hold_position>` (anti-sycophancy), and `<new_machinery>` (`RP-07` pre-action blocker check). | [`writing-profile.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/writing-profile.md) (`WP-03`, `WP-05`), [`anti-drift-rules.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/anti-drift-rules.md) (`AD-01`, `AD-22`, `AD-25`), [`execution-modes.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/execution-modes.md) (`EM-12`) | Synchronized `WP-03`, `WP-05`, `AD-01`, `AD-22`, `AD-25`, and `EM-12` so every clause in `<apex_contract v="1.0">` is 100% backed by its Plane 4 canonical library owner (`WP-23`). | **RESOLVED** |
| **CD-04** | `test_olt_05_anti_overcorrection_and_asset_preservation` in [`test_tier5_adversarial.py`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/tests/test_tier5_adversarial.py#L321) asserts the exact title substring `"Surgical Edits & Anti-Overcorrection"` on `AD-22`. | [`anti-drift-rules.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/anti-drift-rules.md) (`AD-22`) | Titled `AD-22` `Surgical Edits & Anti-Overcorrection (Hold Position)` so both the `test_tier5_adversarial.py` contract test and the `<hold_position>` provenance mapping pass simultaneously. | **RESOLVED** |
| **CD-05** | `okf_validator.py` sentence-length scanner (`STE-SENTENCE-LENGTH`) concatenates a section heading with the first bullet item if no period-terminated introductory sentence separates them. | [`file-architecture.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/file-architecture.md) (§5), [`execution-modes.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/execution-modes.md) (§8) | Added an 8-word period-terminated lead-in sentence (`Guard actively against these recurring ... failure modes.`) beneath the new closing `Failure Modes & Not-To-Dos` headings, keeping `Advisories` at `12` (`0` new advisories). | **RESOLVED** |
| **CD-06** | `MMM/` sub-bundle existed on disk (`apex-meta/informatics/MMM/index.md`) with sub-bundle isolation (`FA-08`) but was unlinked from the root bundle index and missing from the topology tree. | [`apex-meta/informatics/index.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/index.md) (§4), [`file-architecture.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/file-architecture.md) (§4) | Linked `[MMM Methodology Sub-Bundle](MMM/index.md)` in `index.md` §4 and added `MMM/` to the directory topology tree in `file-architecture.md` §4. | **RESOLVED** |
| **CD-07** | `FA-01` and `FA-11` prohibit inline changelogs in live specifications and require recording modification milestones in `log.md`. | [`apex-meta/informatics/log.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/log.md) | Added the `2026-10-21` Wave 2 / `v1.0` Architecture & Library Finalization entry to `log.md`. | **RESOLVED** |

---

## 2. Bidirectional Provenance Verification (`<apex_contract v="1.0">` ↔ `apex-meta/informatics/*.md`)

Every tag in [`13-candidate-3A-xml.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/13-candidate-3A-xml.md) and [`14-candidate-3B-hybrid.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/14-candidate-3B-hybrid.md) has been verified against its canonical Plane 4 rule IDs:

| `<apex_contract v="1.0">` Clause | Relative `ref=` Target | Canonical Rule IDs Verified in Target File |
|---|---|---|
| `<target>` | *(always-on)* | `AD-01` (`anti-drift-rules.md`), `EM-04` (`execution-modes.md`), `WP-01` (`writing-profile.md`) |
| `<product_first>` | *(always-on)* | `AD-10`, `AD-09`, `AD-12` (`anti-drift-rules.md`) |
| `<scope>` | *(always-on)* | `AD-18`, `AD-05` (`anti-drift-rules.md`), `WP-09` (`writing-profile.md`) |
| `<communication>` | *(always-on)* | `WP-02`, `WP-03`, `WP-04`, `WP-05`, `WP-12` (`writing-profile.md`), `AD-17` (`anti-drift-rules.md`) |
| `<hold_position>` | *(always-on)* | `AD-22` (`anti-drift-rules.md`) |
| `<ground>` | *(always-on)* | `AD-19`, `AD-20`, `AD-06` (`anti-drift-rules.md`), `WP-04`, `WP-16` (`writing-profile.md`) |
| `<reuse>` | *(always-on)* | `AD-11`, `AD-14` (`anti-drift-rules.md`), `WP-23` (`writing-profile.md`) |
| `<context>` | *(always-on)* | `AD-04` (`anti-drift-rules.md`), `EM-03`, `EM-10` (`execution-modes.md`) |
| `<recovery>` | *(always-on)* | `AD-07`, `AD-16`, `AD-21` (`anti-drift-rules.md`) |
| `<stop_repairing>` | *(always-on)* | `AD-02`, `AD-07`, `AD-24` (`anti-drift-rules.md`), `EM-05` (`execution-modes.md`) |
| `<current_truth>` | *(always-on)* | `FA-01`, `FA-09`, `FA-11` (`file-architecture.md`), `WP-08` (`writing-profile.md`), `AD-15` (`anti-drift-rules.md`) |
| `<surgical>` | *(always-on)* | `EM-01` (`execution-modes.md`), `AD-03` (`anti-drift-rules.md`), `GS-02` (`governance-schemas.md`) |
| `<editing>` | `execution-modes.md` | `EM-01`, `EM-08` (`execution-modes.md`), `AD-23` (`anti-drift-rules.md`), `GS-09`..`GS-11` (`governance-schemas.md`) |
| `<new_machinery>` | *(conditional gate)* | `AD-25`, `AD-10`, `AD-13` (`anti-drift-rules.md`) |
| `<detour>` | *(conditional gate)* | `AD-05`, `AD-10`, `AD-12` (`anti-drift-rules.md`) |
| `<authoring>` | `index.md` | `FA-13`, `FA-06`, `FA-02`, `FA-10` (`file-architecture.md`), `WP-06`, `WP-07`, `WP-10`, `WP-19`, `WP-24`, `WP-25` (`writing-profile.md`), `GS-03`, `GS-04`, `GS-14`..`GS-17` (`governance-schemas.md`) |
| `<trade_off>` | `execution-modes.md` | `EM-06`, `EM-07` (`execution-modes.md`), `GS-12`, `GS-13` (`governance-schemas.md`) |
| `<handover>` | `execution-modes.md` | `EM-09`, `EM-02` (`execution-modes.md`), `AD-06` (`anti-drift-rules.md`) |
| `<iterative>` | `execution-modes.md` | `EM-10`, `EM-11` (`execution-modes.md`), `AD-04` (`anti-drift-rules.md`) |
| `<schemas>` | `governance-schemas.md` | `GS-01`, `GS-09`, `GS-10`, `GS-11` (`governance-schemas.md`) |
| `<sync>` | *(conditional gate)* | `EM-12` (`execution-modes.md`), `AD-23` (`anti-drift-rules.md`) |
| `<pointers>` | *(terminal guard)* | `general-informatics-router.md`, `WP-25`, `WP-18` (`writing-profile.md`), `AD-26` (`anti-drift-rules.md`) |

---

## 3. Deterministic Conformance & Test Verification Output

- **Command 1 (OKF & Apex Profile Validator):**
  `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics`
  - **Result:** `Summary: OKF Errors: 0 | Apex Profile Errors: 0 | Advisories: 12` (Exit code `0`).
- **Command 2 (Full Pytest Conformance, Canonical Ownership & Tier-5 Adversarial Test Suite):**
  `python -m pytest apex-meta/informatics/tests/ -q`
  - **Result:** `196 passed, 97 subtests passed in 0.34s` (Exit code `0`).
- **Command 3 (Live Root Carrier Non-Modification Check):**
  `git status --short AGENTS.md CLAUDE.md GEMINI.md`
  - **Result:** Clean (`0` modifications to live root carrier files, honoring the staging boundary).
