# Apex Informatics Standard — Change Log

## 2026-10-21

**Wave 2 / `v1.0` Architecture & Library Finalization (`DEC-21`..`DEC-24`)** — Integrated verified findings from the 10-packet deep research campaign (`ResearchOfFile10/`) across the modular specification suite (`index.md`, `writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md`) and finalized the `v1.0` Always-On Architecture candidates (`13-candidate-3A-xml.md` and `14-candidate-3B-hybrid.md`) and carrier blueprint (`03-BLUEPRINT-agents.md`):
- **Multi-Surface Sync & Two-Layer Carrier Architecture (`DEC-21`, `DEC-22`, `FA-12`):** Standardized on physical byte-identical `<apex_contract v="1.0" base_ref="apex-meta/informatics/">` blocks across `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` (Layer 1) followed by a deduplicated repo-specific layer (Layer 2).
- **Contract Serialization & Attribute Pruning (`DEC-23`):** Finalized Candidate `3A` (Pure Named XML, `1,632` repo tokens / `1,350` BPE) and Candidate `3B` (Hybrid XML + Conditional Table, `1,586` repo tokens / `1,314` BPE), removing all 5 redundant `deepen_when=` attributes (`RP-08`) while preserving 100% of their second-threshold escalation triggers (`AST patches`, `tier definitions/bundle layout`, `bake-offs`, `delegation contracts`, `MMM/route ladder`, `JSON/YAML schemas`) via concise inline `Open ref for ...` cues in both `3A` and `3B`.
- **Empirical Behavioral Wording Upgrades & Conformance Alignment (`DEC-24`, `WP-04`, `WP-12`, `FA-03`, `AD-01`, `AD-17`, `AD-25`, `standard.md`, `migration.md`, `.claude/rules/informatics.md`):** Synchronized `RP-05` SpecBench positive requirement-by-requirement final validation, `RP-07` FixedBench no-op legitimacy and pre-action blocker requirement, `RP-04` Insights Discovery Cool Blue analytical register + warranted uncertainty distinction, added `id:` frontmatter and `WP-25` terminal guard to `standard.md` and `migration.md`, and added `paths:` YAML frontmatter to `.claude/rules/informatics.md` (`RP-02`/`RP-03`).

## 2026-09-01

**Wave 1 Ratification** — Established the canonical Apex Informatics package (`apex-meta/informatics/`), establishing the 14-section conformance profile (`standard.md`), the forward-default migration policy (`migration.md`), and the minimal bundle routing index (`index.md`).
