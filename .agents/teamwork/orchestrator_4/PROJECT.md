# Project: Layered Rule KB (Rules 02–22), Plane 4 Audits & 16-candidate-3A-ultra

## Architecture
- **Layer 0 (Essence Contract):** `apex-meta/informatics/final/candidates/13-candidate-3A-xml.md` (1,350 BPE baseline) and `candidates/16-candidate-3A-ultra.md` (~935 BPE target). Pure XML tags for embedding into AI instruction carriers.
- **Layer 1 (Layered Rule Knowledge Base):** `apex-meta/informatics/final/research/06-layered-rule-kb/` containing deep-dives `rule-01-target.md` through `rule-22-pointers.md` and module audits `audit-module-01` through `audit-module-05`, indexed via `06-layered-rule-kb/index.md`.
- **Layer 2 (Canonical Plane 4 Library Modules):** `apex-meta/informatics/` containing `writing-profile.md` (WP), `file-architecture.md` (FA), `execution-modes.md` (EM), `anti-drift-rules.md` (AD), `governance-schemas.md` (GS), `general-informatics-router.md`, and `index.md`.
- **Upstream Research Corpora (Layer 3 Grounding):** `final/research/` containing `01-universal-instruction-research/` (A01–A13, C01–C03), `03-research-of-file-10/` (RESULTS-01..11, RP-01..10), `04-finalization-dossier/`, `05-analysis-after-research/`.
- **Validation & Test Harness:** `apex-meta/scripts/okf_validator.py` and `apex-meta/informatics/tests/` (196 tests).

## Feature Inventory
| # | Feature | Description | Milestone | Source | Status |
|---|---------|-------------|:---:|:---:|:---:|
| F01 | `rule-02-product-first.md` | Deep-dive for `<product_first>` with 3 semantic blocks, options A/B/C, AD-09/10/12 links | M1 | Survey 1 | **DONE** |
| F02 | `rule-03-scope.md` | Deep-dive for `<scope>` with 3 semantic blocks, options A/B/C, AD-05/18, WP-09 links | M1 | Survey 1 | **DONE** |
| F03 | `rule-04-communication.md` | Deep-dive for `<communication>` with 4 semantic blocks, Cool Blue register, options A/B/C | M1 | Survey 1 | **DONE** |
| F04 | `rule-05-hold-position.md` | Deep-dive for `<hold_position>` with 3 semantic blocks, pushback resilience, options A/B/C | M1 | Survey 1 | **DONE** |
| F05 | `rule-06-ground.md` | Deep-dive for `<ground>` with 4 semantic blocks, path:line/command grounding, options A/B/C | M1 | Survey 1 | **DONE** |
| F06 | `rule-07-reuse.md` | Deep-dive for `<reuse>` with 4 semantic blocks, modular part composition, options A/B/C | M1 | Survey 1 | **DONE** |
| F07 | `rule-08-context.md` | Deep-dive for `<context>` with 2 semantic blocks, JIT loading & ranking, options A/B/C | M1 | Survey 1 | **DONE** |
| F08 | `rule-09-recovery.md` | Deep-dive for `<recovery>` with 2 semantic blocks, narrowest safe alternative, options A/B/C | M2 | Survey 1 | **DONE** |
| F09 | `rule-10-stop-repairing.md` | Deep-dive for `<stop_repairing>` with 2 semantic blocks, 2-strike pivot rule, options A/B/C | M2 | Survey 1 | **DONE** |
| F10 | `rule-11-current-truth.md` | Deep-dive for `<current_truth>` with 3 semantic blocks, active truth, options A/B/C | M2 | Survey 1 | **DONE** |
| F11 | `rule-12-surgical.md` | Deep-dive for `<surgical>` with 1 semantic block, full file overwrite ban, options A/B/C | M2 | Survey 1 | **DONE** |
| F12 | `rule-13-editing.md` | Deep-dive for `<editing>` with 4 semantic blocks, character-for-character patch, options A/B/C | M2 | Survey 1 | **DONE** |
| F13 | `rule-14-new-machinery.md` | Deep-dive for `<new_machinery>` with 3 semantic blocks, blocker requirement gate, options A/B/C | M2 | Survey 1 | **DONE** |
| F14 | `rule-15-detour.md` | Deep-dive for `<detour>` with 2 semantic blocks, refactor deferral gate, options A/B/C | M2 | Survey 1 | **DONE** |
| F15 | `rule-16-authoring.md` | Deep-dive for `<authoring>` with 6 semantic blocks, flat YAML, P-tiers, options A/B/C | M3 | Survey 1 | **DONE** |
| F16 | `rule-17-trade-off.md` | Deep-dive for `<trade_off>` with 3 semantic blocks, reversible choices & options, options A/B/C | M3 | Survey 1 | **DONE** |
| F17 | `rule-18-handover.md` | Deep-dive for `<handover>` with 3 semantic blocks, 5-element report structure, options A/B/C | M3 | Survey 1 | **DONE** |
| F18 | `rule-19-iterative.md` | Deep-dive for `<iterative>` with 4 semantic blocks, MMM preflight & route ladder, options A/B/C | M3 | Survey 1 | **DONE** |
| F19 | `rule-20-schemas.md` | Deep-dive for `<schemas>` with 4 semantic blocks, patch intent & schema match, options A/B/C | M3 | Survey 1 | **DONE** |
| F20 | `rule-21-sync.md` | Deep-dive for `<sync>` with 3 semantic blocks, git push discipline, options A/B/C | M3 | Survey 1 | **DONE** |
| F21 | `rule-22-pointers.md` | Deep-dive for `<pointers>` with 2 semantic blocks, base_ref terminal guard, options A/B/C | M3 | Survey 1 | **DONE** |
| F22 | `audit-module-01-writing-profile.md` | Audit of `writing-profile.md` (WP-01..WP-25), single-ownership (WP-23), cross-traceability | M4 | Survey 2 | PLANNED |
| F23 | `audit-module-02-file-architecture.md` | Audit of `file-architecture.md` (FA-01..FA-13), single-ownership, cross-traceability | M4 | Survey 2 | PLANNED |
| F24 | `audit-module-03-execution-modes.md` | Audit of `execution-modes.md` (EM-01..EM-12), single-ownership, cross-traceability | M4 | Survey 2 | PLANNED |
| F25 | `audit-module-04-anti-drift-rules.md` | Audit of `anti-drift-rules.md` (AD-01..AD-28), single-ownership, cross-traceability | M4 | Survey 2 | PLANNED |
| F26 | `audit-module-05-governance-schemas.md` | Audit of `governance-schemas.md` (GS-01..GS-22), single-ownership, cross-traceability | M4 | Survey 2 | PLANNED |
| F27 | `16-candidate-3A-ultra.md` | Compile 3A-Ultra block concatenating Option B compressions (~900-980 BPE, target ~950 BPE) | M5 | Survey 3 | PLANNED |
| F28 | Delta Table Documentation | Rule-by-rule delta table against `13-candidate-3A-xml.md` with measured BPE before/after/% savings | M5 | Survey 3 | PLANNED |
| F29 | `06-layered-rule-kb/index.md` | Sub-bundle index listing and linking all 22 rule deep-dives and 5 module audits | M5 | Survey 3 | PLANNED |
| F30 | Update `final/index.md` | Add references to `06-layered-rule-kb/` and `16-candidate-3A-ultra.md` | M5 | Survey 3 | PLANNED |
| F31 | Deterministic Conformance Gate | Verify `okf_validator.py` exits 0 with 0 OKF and 0 Profile errors | M5 | Survey 3 | PLANNED |
| F32 | Pytest Test Suite Gate | Verify `pytest apex-meta/informatics/tests/ -q` passes 100% (196/196) | M5 | Survey 3 | PLANNED |
| F33 | Carrier & Research Invariant Gate | Verify zero modifications to AGENTS.md, CLAUDE.md, GEMINI.md, and upstream research bytes | M5 | Survey 3 | PLANNED |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|:---:|
| **M1** | Layered Rule KB Phase 1 (Rules 02–08) | Author `rule-02` through `rule-08` in `final/research/06-layered-rule-kb/` matching `rule-01-target.md` | Survey complete | **DONE** |
| **M2** | Layered Rule KB Phase 2 (Rules 09–15) | Author `rule-09` through `rule-15` in `final/research/06-layered-rule-kb/` matching `rule-01-target.md` | M1 | **DONE** |
| **M3** | Layered Rule KB Phase 3 (Rules 16–22) | Author `rule-16` through `rule-22` in `final/research/06-layered-rule-kb/` matching `rule-01-target.md` | M2 | **DONE** |
| **M4** | Plane 4 Infrastructure Module Audits | Author `audit-module-01` through `audit-module-05` in `final/research/06-layered-rule-kb/` | M3, Survey 2 | **PLANNED** |
| **M5** | 3A-Ultra Compilation, Indexes & Gates | Compile `16-candidate-3A-ultra.md`, author `06-layered-rule-kb/index.md`, update `final/index.md`, verify gates | M1–M4, Survey 3 | **PLANNED** |

## Interface Contracts
### Layer 0 (3A / 3A-Ultra) ↔ Layer 1 (Layered Rule KB)
- Every rule in `16-candidate-3A-ultra.md` corresponds 1:1 with Option B recommended surgical compression in `rule-XX-...md`.
- Every `rule-XX-...md` provides exact BPE token counts (`cl100k_base`), repo tokens (`chars // 4`), characters, and words for Baseline 3A, Option B, and Option C.
- Every `rule-XX-...md` has OKF v0.2 frontmatter: `type: Reference`, unique durable ID `V2-LAYERED-KB-RULE-XX-...`, title, description, `status: current_truth`, tags.

### Layer 1 (Layered Rule KB) ↔ Layer 2 (Plane 4 Modules)
- Single-Ownership rule (`WP-23`): Contract rules state the operative imperative; canonical definitions remain in Plane 4 modules.
- Every rule file and module audit file links to canonical rule IDs (`WP-xx`, `FA-xx`, `EM-xx`, `AD-xx`, `GS-xx`).
- 100% of relative links resolve to actual files on disk.

### Sub-Bundle Isolation Contract
- `06-layered-rule-kb/index.md` creates an isolated sub-bundle in `okf_validator.py`. All relative links within `06-layered-rule-kb/` must resolve accurately.

## Code Layout
- Layered Rule KB deep-dives: `apex-meta/informatics/final/research/06-layered-rule-kb/rule-01-target.md` through `rule-22-pointers.md`
- Module audits: `apex-meta/informatics/final/research/06-layered-rule-kb/audit-module-01-writing-profile.md` through `audit-module-05-governance-schemas.md`
- KB Index: `apex-meta/informatics/final/research/06-layered-rule-kb/index.md`
- Candidate 3A-Ultra: `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md`
- Final Directory Index: `apex-meta/informatics/final/index.md`
- Agent Metadata (State only): `.agents/teamwork/orchestrator_4/` and per-agent subdirectories under `.agents/teamwork/`
