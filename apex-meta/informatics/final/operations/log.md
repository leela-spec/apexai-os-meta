# Apex Informatics Standard — Change Log

## 2026-11-07 (orchestrator batch 1)

**T6 and T7 measured** — `HANDOVER-11` ledger rows T6 and T7 now hold numbers: 20 failing verification tests (4 stale against candidate 16, 4 path-dependent on sibling repos missing from the short-path clone, 12 stale from the monolith split or archiving) and OKF validator counts at `5a316e6b` and `main` (profile errors 13 and 17). No tests or validator output were changed. Details under `## Orchestrator report`, Batch 1.

## 2026-11-07

**Carrier gaps closed; MausBot record; shared Layer 2 text** — `<trade_off>` in `specs/apex_contract_v1.0_ultra.xml` now names the intensity lever (`EM-06a`, `qa-decision-matrix.md`). `specs/execution-modes.md` section 2 points at the split matrix file, as sections 3-7 already did. `tools/apex_carrier_sync.py` now compares the three global files' shared Layer 2 sections against the new `specs/carrier-layer2-shared.md` (found drift: Gemini lacked the Windows defaults, worded the other sections differently, and carried a corrupted dash), and Claude's `base_ref` is absolute.
- **MausBot:** `operations/19-MAUSBOT-INSTALLATION-RECORD.md` records the 2026-11-04 installation, including the change MausBot applied to the global Codex file, and why its apex skills exist only in its workspace. `HANDOVER-09` asks MausBot to list its deviations from the master (notably `<align>`). `HANDOVER-10` holds the probes for the Claude account folders and the two Gemini files.
- **Moved in:** the two ultra-style-audit files from Leela (`research/07-ultra-style-audit/`), because they are Apex material. Three carrier templates now name the master instead of candidate 16.
- **Documented:** `operations/20-CHANGE-RECORD-2026-11-06-07.md` records every change (before, problem, solution, after) and the mistakes found. `research/06-layered-rule-kb/` got update blocks in `rule-17-trade-off.md`, `audit-module-03-execution-modes.md` and `index.md`, and a new `rule-23-align.md` (the KB covers 22 rules; the master has 23). `operations/handovers/HANDOVER-11-ORCHESTRATOR-CONTINUATION.md` holds the open-task ledger for a new orchestrating chat.

## 2026-11-06

**Carrier sync, intensity lever, and retirement of candidate 16** — Added `EM-06a` (Intensity Lever, `L0`–`L3`, thresholds unmeasured) to `specs/execution-modes/qa-decision-matrix.md`. Changed the `<align>` trigger (and `EM-13` in `task-specification.md`) so an already-defined step does not need a new restatement. Added `tools/apex_carrier_sync.py` and `operations/18-APEX-CARRIER-MAP.md`: the script compares the always-on block in every carrier with `specs/apex_contract_v1.0_ultra.xml` on `main`, and `--sync` rewrites drifted inline copies (block only, with a backup).
- **Codex restored.** `~/.codex/AGENTS.md` lost its inline block on 2026-11-04 when the MausBot installation replaced it with a pointer. The block is inline again; Codex is a synced carrier like Claude and Gemini.
- **Candidate 16 archived.** `candidates/16-candidate-3A-ultra.md` (22 rules, no `<align>`) moved to `candidates/_archive/` with a README. The master XML is the only live always-on source. Markdown links to it were rewritten; bare mentions in dated historical records were left.
- **Why:** the vendored copy in Leela named candidate 16 as its source, so an agent following that header would audit or copy a stale block, and nothing compared the vendored block with the master.

## 2026-10-23

**Multi-CLI & Multi-Repo Two-Layer Carrier Formulation (`RUNBOOK-TWO-LAYER-CARRIER-DRAFTS-v1.0`)** — Synthesized and staged concrete Two-Layer Carrier drafts across all 3 primary `C:\GitDev\` repositories (`apexai-os-meta`, `MasterOfArts`, `Leela-Cloud-2026`) preserving 100% of local domain invariants and safety sandboxes while coupling them to the byte-identical `<apex_contract v="1.0-ultra">` kernel:
- **`apexai-os-meta`:** Windows 11 host environment isolation, QMD speed protocol (`DEC-QMD-01`/`04`), and canonical OpenProject skill routing.
- **`MasterOfArts`:** Hermes operating doctrine (ADR-002), project family isolation, Docker sandboxed terminal execution (`terminal.backend = docker`), untracked source materials manifest (`UNTRACKED-SOURCE-MATERIALS.md`), and QMD scopes.
- **`Leela-Cloud-2026`:** 3-tier product authority hierarchy (decisions + authored materialization > code > SSOT specs), materialization contracts (`target_status`), OpenProject commitment routing (SSOT-D-054), blast radius guard, operator-selected framework restriction (BMAD/Superpowers), 6-step decision batch transactions, and gates runner.
- **Deterministic Validation:** 348 passing tests in 0.9s (including 10 tests in `test_m6_two_layer_carrier_drafts.py`) verifying zero link, schema, or carrier immutability regressions and 100% byte-exact Layer 2 preservation.

## 2026-10-21

**Wave 2 / `v1.0` Architecture & Library Finalization (`DEC-21`..`DEC-24`)** — Integrated verified findings from the 10-packet deep research campaign (`ResearchOfFile10/`) across the modular specification suite (`index.md`, `writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md`) and finalized the `v1.0` Always-On Architecture candidates (`13-candidate-3A-xml.md` and `14-candidate-3B-hybrid.md`) and carrier blueprint (`03-BLUEPRINT-agents.md`):
- **Multi-Surface Sync & Two-Layer Carrier Architecture (`DEC-21`, `DEC-22`, `FA-12`):** Standardized on physical byte-identical `<apex_contract v="1.0" base_ref="apex-meta/informatics/">` blocks across `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` (Layer 1) followed by a deduplicated repo-specific layer (Layer 2).
- **Contract Serialization & Attribute Pruning (`DEC-23`):** Finalized Candidate `3A` (Pure Named XML, `1,632` repo tokens / `1,350` BPE) and Candidate `3B` (Hybrid XML + Conditional Table, `1,586` repo tokens / `1,314` BPE), removing all 5 redundant `deepen_when=` attributes (`RP-08`) while preserving 100% of their second-threshold escalation triggers (`AST patches`, `tier definitions/bundle layout`, `bake-offs`, `delegation contracts`, `MMM/route ladder`, `JSON/YAML schemas`) via concise inline `Open ref for ...` cues in both `3A` and `3B`.
- **Empirical Behavioral Wording Upgrades & Conformance Alignment (`DEC-24`, `WP-04`, `WP-12`, `FA-03`, `AD-01`, `AD-17`, `AD-25`, `standard.md`, `migration.md`, `.claude/rules/informatics.md`):** Synchronized `RP-05` SpecBench positive requirement-by-requirement final validation, `RP-07` FixedBench no-op legitimacy and pre-action blocker requirement, `RP-04` Insights Discovery Cool Blue analytical register + warranted uncertainty distinction, added `id:` frontmatter and `WP-25` terminal guard to `standard.md` and `migration.md`, and added `paths:` YAML frontmatter to `.claude/rules/informatics.md` (`RP-02`/`RP-03`).

## 2026-09-01

**Wave 1 Ratification** — Established the canonical Apex Informatics package (`apex-meta/informatics/`), establishing the 14-section conformance profile (`standard.md`), the forward-default migration policy (`migration.md`), and the minimal bundle routing index (`index.md`).
