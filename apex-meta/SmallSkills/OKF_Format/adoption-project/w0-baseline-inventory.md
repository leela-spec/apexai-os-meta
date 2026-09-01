---
type: Research
title: Apex Informatics Adoption — Wave 0 Baseline Inventory
description: Read-only empirical baseline of instruction surfaces, knowledge zones, OKF conformance footprints, pseudo-OKF drift, and skill distributions before W1 routing changes.
tags: [okf, informatics, w0, baseline, inventory, apex-meta]
generated: { by: gemini-3.7-flash, at: 2026-09-01T20:25:00Z }
status: stable
---

# Wave 0 Baseline Inventory

## 1. Repository Execution Context
- **Repository**: `leela-spec/apexai-os-meta`
- **Base Commit**: `c21915f0` (`feat/informatics-w0-w2` worktree branched from `main`)
- **Execution Date**: 2026-09-01

---

## 2. Always-On & Scoped Instruction Surfaces

| Path | Consumer | Load Scope | Authority Role | Canonicality | Duplicate Group / Hash | Current Action |
|---|---|---|---|---|---|---|
| `AGENTS.md` | Codex, Gemini, general agents | Always-on | Universal Invariants & Routing | Canonical | `hash:2b36dacc7011` (matches root `CLAUDE.md`) | Candidate Refactor (A1.2) |
| `CLAUDE.md` | Claude root / IDE fallback | Always-on | Duplicate mirror of `AGENTS.md` | Byte mirror | `hash:2b36dacc7011` (matches `AGENTS.md`) | Conditional resolution (A1.6) |
| `.claude/CLAUDE.md` | Claude Code project | Always-on (Claude) | Orchestration router | Canonical | `hash:5215b36c1699` (independent) | Candidate Refactor (A1.3) |
| `.github/copilot-instructions.md` | GitHub Copilot | Always-on (Copilot) | Stale wiki framework prompt | Stale legacy | `hash:c33f4743a18c` | Candidate Repair (A1.4) |
| `.claude/rules/**` | Claude Code scoped | Path-scoped | Scoped instructions | Non-existent | None | Create `.claude/rules/informatics.md` (A1.5) |
| `.github/instructions/**` | GitHub Copilot scoped | Path-scoped | Scoped instructions | Non-existent | None | Create `.github/instructions/informatics.instructions.md` (A1.5) |
| `.agents/skills/**` | Generic agents | Task-triggered | Reusable skills | Mirror (40 skills) | Mirrored across `.cursor`, `.kiro`, `.pi`, `.windsurf` | Preserve (exclude from W0-W2) |
| `.claude/skills/**` | Claude runtime | Task-triggered | Reusable skills | Primary (65 skills) | Contains orchestration skills | Preserve (extend/point only) |

---

## 3. Knowledge Zones Classification

| Zone | Authority | Loading | Artifact | Lifecycle | Notes |
|---|---|---|---|---|---|
| `apex-meta/SmallSkills/OKF_Format/**` | Normative (OKF ref) | Task / Reference | Knowledge (OKF v0.2) | Current | Primary grounded OKF reference bundle |
| `apex-meta/orchestration/**` | Normative (MAO) | Explicit Task | Architecture / Procedure | Current | Multi-Agent Orchestration; OUT OF SCOPE for W0-W2 |
| `apex-meta/kb/Weekly-Orchestrator/**` | Operational / Evidence | Explicit Task | Knowledge / State | Current | Weekly Orchestrator KB; OUT OF SCOPE for W0-W2 |
| `apex-meta/kb/claude-code-orchestration-design/**` | Evidence / Research | Reference | Synthesis / Practice Guide | Current | Houses `informatics-design-formats-practice-guide.md` |
| `apex-meta/handoff/**` | Operational | Task / Stage | Handoff packets | Generated / Active | Handoff artifacts; OUT OF SCOPE |
| `.claude/skills/**` | Operational | Task-triggered | Executable procedures | Current | Reusable agent capabilities |

---

## 4. OKF Footprint & Drift Analysis

### A. Declared OKF Bundles
- `apex-meta/SmallSkills/OKF_Format/`:
  - `index.md`: Declares `okf_version: "0.2"`.
  - Concept files (`attested-computation.md`, `bundle-structure.md`, `conformance-rules.md`, `cross-linking-and-citations.md`, `frontmatter-fields.md`, `provenance-and-trust.md`): Valid parseable YAML frontmatter with `type: Reference`, `sources`, etc.
  - `log.md`: Reserved changelog markdown.
  - `adoption-project/`: Research and implementation plans (`type: Research`, `type: Plan`).

### B. Pseudo-OKF Drift Inventory
- Total files using `.okf.md` suffix across repository: **62 files**.
- Analysis:
  - Files with YAML frontmatter: **4 files** (in `deterministic-markdown-patcher2/repair-packs/`).
  - Files lacking YAML frontmatter: **58 files** (e.g. `tier0-kb-validation-and-extension-packet.okf.md`, `apex-meta/handoff/*.okf.md`, `simulations/hermes-e2e-two-week-v1/00-PROGRAM.okf.md`).
- Policy confirmation: In accordance with `implementation-waves-w0-w2.md`, no mass retrofit or renaming will occur during W0–W2. Governed targets remain strictly bounded.

---

## 5. Skill Footprint & Mirror Map

- **Canonical Active Skills**:
  - `apex-kb`: `.claude/skills/apex-kb/SKILL.md` (owns Apex KB procedure & control).
  - `weekly-orchestrator`: `.claude/skills/weekly-orchestrator/SKILL.md` (owns Weekly loop).
  - `apex-plan`, `apex-sync`, `apex-session`: `.claude/skills/apex-*/SKILL.md` (Plan-Sync-Session backbone).
- **Client Mirror Footprint**:
  - `.agents/skills` (40), `.cursor/skills` (40), `.kiro/skills` (40), `.pi/skills` (40), `.windsurf/skills` (40).
  - Mirror consolidation is explicitly deferred to later waves.

---

## 6. Baseline Verification Sign-off
- Baseline inventory complete.
- No production files modified.
