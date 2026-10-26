# Adversarial Challenge Report — Milestone 1 (Rules 02–08)

**Target Workspace**: `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\`
**Target Files**: `rule-02-product-first.md` through `rule-08-context.md`
**Author / Worker**: Worker M1
**Auditor**: Challenger 2 (Milestone 1) — Empirical Challenger
**Audit Date**: 2026-10-22

---

## Challenge Summary

**Overall risk assessment**: **HIGH**

While the authored rule deep-dives exhibit extraordinary semantic rigor, 100% exact byte-for-byte fidelity with the `<apex_contract v="1.0">` candidate, zero live carrier mutation, 100% research preservation, 100% pass on the pytest suite, and mathematically exact BPE token counts, **link resolution fails critically**:
- **30 relative Markdown links across all 7 files resolve to non-existent disk paths.**
- 21 links point to a deleted/relocated directory (`../../Agent_Setup/NextIteration/v2-always-on-architecture/` instead of `../../candidates/`).
- 9 links point to non-existent `.md` filenames under `module-deepening/` instead of directory `README.md` paths.

Because bidirectional traceability is an explicit requirement of R1 (§4) and link inspection was explicitly tasked in dispatch, this report issues a structured verdict of **REQUEST_CHANGES** pending surgical link repairs.

---

## Challenges

### [High] Challenge 1: 30 Broken Relative Markdown Links in Section 4.1 Provenance

- **Assumption challenged**: The author assumed that relative paths copied from prototype templates pointing to `../../Agent_Setup/NextIteration/v2-always-on-architecture/` and flat `.md` files under `module-deepening/` were valid.
- **Attack scenario**: When an autonomous agent, static site generator, IDE link validator, or human engineer navigates the Layered Rule Knowledge Base to trace the evolution of `<product_first>` through `<context>` back to earlier contract blocks (`v0.3`, `v0.4`, `v0.5`) or upstream research deepening packets (`A01`..`A13`), the link target fails to resolve (`FileNotFoundError`).
- **Blast radius**: All 7 files authored in Milestone 1 contain broken links (4 to 5 broken links per file, 30 total).
- **Root Cause Analysis**:
  1. **Lineage Consolidation Drift**: Contract versions `02-informatics-contract-block.md`, `07-contract-block-v0.4.md`, and `09-contract-block-v0.5.md` were relocated from `apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/` to `apex-meta/informatics/final/candidates/`. While the author updated `[13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md)` correctly, the three antecedent versions were left with stale pre-consolidation paths.
  2. **Folder vs File Mismatch in `module-deepening/`**: In `apex-meta/informatics/final/research/01-universal-instruction-research/module-deepening/`, each module is organized as a subdirectory containing a `README.md` (e.g., `A01-target-outcome-alignment/README.md`), not a single flat `.md` file (e.g., `A01-substance-over-ceremony.md`).
- **Mitigation**: Perform an exact-match surgical replacement across all 7 files replacing the 12 broken URL patterns with their verified target paths (detailed in Section 3 below).

---

## Stress Test Results

| # | Test Scenario | Expected Behavior | Actual Behavior | Verdict |
|---|---|---|---|---|
| **ST-01** | **Relative Markdown Link Resolution** (`rule-02` through `rule-08`) | 100% of relative markdown links resolve to live disk files | 30 broken links detected across 7 files (21 lineage, 9 research deepening) | **FAIL** |
| **ST-02** | **Zero Live Carrier Mutation** (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`) | Zero new modifications introduced by M1 | `git diff` shows no new changes (diffs date from 2026-10-08 / 2026-09-29) | **PASS** |
| **ST-03** | **Research Corpus 01 Preservation** (`01-universal-instruction-research/`) | Zero file modifications in research corpus | 70 files verified; latest mtime 2026-09-29 | **PASS** |
| **ST-04** | **Research Corpus 03 Preservation** (`03-research-of-file-10/`) | Zero file modifications in research corpus | 14 files verified; latest mtime 2026-10-21 14:36 | **PASS** |
| **ST-05** | **Pytest Test Suite Execution** (`apex-meta/informatics/tests/`) | 100% passing tests | 196 passed, 98 subtests passed in 0.52s | **PASS** |
| **ST-06** | **Exact Byte Match of `<apex_contract v="1.0">`** | Section 1.1 matches `13-candidate-3A-xml.md` character-for-character | All 7 rule tags match byte-for-byte | **PASS** |
| **ST-07** | **Section 1.1 Token & Char Metrics Accuracy** | Claimed BPE, repo tokens, chars, and words match live computation | All claimed counts verified mathematically | **PASS** |
| **ST-08** | **Section 1.2 Atomic Semantic Blocks Accuracy** | Semantic blocks partition inner text without token or character leakage | Claimed BPE and char lengths match `tiktoken` `cl100k_base` exactly | **PASS** |
| **ST-09** | **Section 2 Formulation Options (A, B, C)** | Every block provides Baseline, Option B (surgical), Option C (aggressive) | 100% presence across all 23 semantic blocks in 7 files | **PASS** |
| **ST-10** | **Section 3 Rollup BPE Measurements & Deltas** | Recomposed BPE counts and savings match live `cl100k_base` measurements | 21 / 21 rows in Section 3 rollup tables match exact token counts | **PASS** |
| **ST-11** | **Section 4 Provenance — Research Packet Resolution** | `RESULTS-03`, `04`, `05`, `07`, `09` resolve to disk | 100% of `RESULTS-xx` links resolve to existing files | **PASS** |
| **ST-12** | **Section 4 Provenance — Plane 4 Infrastructure Modules** | Links to `anti-drift-rules.md`, `writing-profile.md`, etc. resolve | 100% of Plane 4 module links resolve to live files | **PASS** |
| **ST-13** | **Section 4 Provenance — Operational Lore** | Links to `2Dos Ai Instructions.md` and `Snippets.md` resolve | 100% resolve after URL-decoding `%20` | **PASS** |
| **ST-14** | **Section 5 Failure Modes & Not-To-Dos** | Each rule includes >= 3 concrete negative boundary invariants | Exactly 3 high-leverage invariants per file | **PASS** |
| **ST-15** | **OKF v0.2 Frontmatter Validation** | `type: Reference`, unique durable `id`, `status: current_truth` | Frontmatter valid in all 7 files (`Apex Profile Errors: 0`) | **PASS** |
| **ST-16** | **Single-Owner Discipline (`WP-23`)** | Each file cites its canonical Plane 4 owner without re-defining rules | Clear Layer 2 citations to `AD-xx`, `WP-xx`, `EM-xx` | **PASS** |

---

## Detailed Empirical Evidence: The 30 Broken Links

### File-by-File Inventory

#### 1. `rule-02-product-first.md` (5 broken links)
- Line 12: `[A01-substance-over-ceremony.md](../../research/01-universal-instruction-research/module-deepening/A01-substance-over-ceremony.md)`
- Line 12: `[A07-hierarchical-realization.md](../../research/01-universal-instruction-research/module-deepening/A07-hierarchical-realization.md)`
- Line 14: `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)`
- Line 14: `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)`
- Line 14: `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)`

#### 2. `rule-03-scope.md` (4 broken links)
- Line 12: `[A02-scope-and-non-goals.md](../../research/01-universal-instruction-research/module-deepening/A02-scope-and-non-goals.md)`
- Line 14: `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)`
- Line 14: `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)`
- Line 14: `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)`

#### 3. `rule-04-communication.md` (4 broken links)
- Line 12: `[A12-communication-economy.md](../../research/01-universal-instruction-research/module-deepening/A12-communication-economy.md)`
- Line 14: `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)`
- Line 14: `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)`
- Line 14: `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)`

#### 4. `rule-05-hold-position.md` (4 broken links)
- Line 12: `[A05-intent-alignment.md](../../research/01-universal-instruction-research/module-deepening/A05-intent-alignment.md)`
- Line 14: `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)`
- Line 14: `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)`
- Line 14: `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)`

#### 5. `rule-06-ground.md` (5 broken links)
- Line 12: `[A08-evidence-integrity.md](../../research/01-universal-instruction-research/module-deepening/A08-evidence-integrity.md)`
- Line 12: `[A13-external-grounding.md](../../research/01-universal-instruction-research/module-deepening/A13-external-grounding.md)`
- Line 14: `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)`
- Line 14: `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)`
- Line 14: `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)`

#### 6. `rule-07-reuse.md` (4 broken links)
- Line 12: `[A03-reuse-before-invention.md](../../research/01-universal-instruction-research/module-deepening/A03-reuse-before-invention.md)`
- Line 14: `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)`
- Line 14: `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)`
- Line 14: `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)`

#### 7. `rule-08-context.md` (4 broken links)
- Line 12: `[A06-context-engineering.md](../../research/01-universal-instruction-research/module-deepening/A06-context-engineering.md)`
- Line 14: `[02-informatics-contract-block.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md)`
- Line 14: `[07-contract-block-v0.4.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md)`
- Line 14: `[09-contract-block-v0.5.md](../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md)`

---

## Actionable Remediation Table (100% Empirically Verified)

The Worker can execute a surgical find-and-replace using the following exact mapping. All target paths have been verified on disk:

| Broken URL in Rules 02–08 | Verified Disk Target Relative Path | Disk Existence Verified |
|---|---|:---:|
| `../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md` | `../../candidates/02-informatics-contract-block.md` | **TRUE** |
| `../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md` | `../../candidates/07-contract-block-v0.4.md` | **TRUE** |
| `../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md` | `../../candidates/09-contract-block-v0.5.md` | **TRUE** |
| `../../research/01-universal-instruction-research/module-deepening/A01-substance-over-ceremony.md` | `../../research/01-universal-instruction-research/module-deepening/A01-target-outcome-alignment/README.md` | **TRUE** |
| `../../research/01-universal-instruction-research/module-deepening/A07-hierarchical-realization.md` | `../../research/01-universal-instruction-research/module-deepening/A07-hierarchical-realization-verification-validation/README.md` | **TRUE** |
| `../../research/01-universal-instruction-research/module-deepening/A02-scope-and-non-goals.md` | `../../research/01-universal-instruction-research/module-deepening/A02-scope-non-goals/README.md` | **TRUE** |
| `../../research/01-universal-instruction-research/module-deepening/A12-communication-economy.md` | `../../research/01-universal-instruction-research/module-deepening/A12-communication-economy-actionable-visibility/README.md` | **TRUE** |
| `../../research/01-universal-instruction-research/module-deepening/A05-intent-alignment.md` | `../../research/01-universal-instruction-research/module-deepening/A05-intent-alignment-clarification-threshold/README.md` | **TRUE** |
| `../../research/01-universal-instruction-research/module-deepening/A08-evidence-integrity.md` | `../../research/01-universal-instruction-research/module-deepening/A08-evidence-integrity-uncertainty-calibration/README.md` | **TRUE** |
| `../../research/01-universal-instruction-research/module-deepening/A13-external-grounding.md` | `../../research/01-universal-instruction-research/module-deepening/A13-external-grounding-real-world-verification/README.md` | **TRUE** |
| `../../research/01-universal-instruction-research/module-deepening/A03-reuse-before-invention.md` | `../../research/01-universal-instruction-research/module-deepening/A03-reuse-before-invention/README.md` | **TRUE** |
| `../../research/01-universal-instruction-research/module-deepening/A06-context-engineering.md` | `../../research/01-universal-instruction-research/module-deepening/A06-context-engineering-progressive-disclosure/README.md` | **TRUE** |

---

## Unchallenged Areas

- **Rules 09 through 22**: Out of scope for Milestone 1; will be evaluated during Milestones 2 and 3.
- **Plane 4 Infrastructure Module Audits (`audit-module-01`..`05`)**: Out of scope for Milestone 1; assigned to Milestone 4.
- **Candidate `16-candidate-3A-ultra.md` Compilation**: Scheduled for Milestone 4.
- **Prototype `rule-01-target.md` Link Issues**: While `rule-01-target.md` was observed to contain 21 broken links due to similar pre-consolidation paths, `rule-01` is marked `status: prototype_for_review` and was not authored in M1. It should be swept for link repairs in the final index milestone.
