---
type: Research
title: Apex Informatics Adoption — Wave 0 Retrieval Evaluation Benchmark
description: Empirical baseline evaluation suite comprising 24 real Apex retrieval and operation test cases measuring routing correctness, file economy, and authority ownership before W1 routing changes.
tags: [okf, informatics, w0, baseline, retrieval, eval, benchmark]
generated: { by: gemini-3.7-flash, at: 2026-09-01T20:25:30Z }
status: stable
---

# Wave 0 Baseline Retrieval Evaluation Suite

## 1. Evaluation Protocol & Metrics

Every test case is evaluated across three dimensions:
1. **Correctness**:
   - `correct_answer`: Target deliverable or answer is factual and grounded.
   - `authority_owner`: Resolves to canonical authority (no false authority or ambiguous copies).
2. **Economy**:
   - `files_opened`: Total files required to resolve the query.
   - `retrieval_hops`: Number of hops from root router to authoritative document.
3. **Quality**:
   - `contradiction_introduced`: False/stale guidance encountered during retrieval.
   - `duplicated_rule_used`: Rule resolved via secondary copy rather than canonical owner.

---

## 2. Benchmark Cases & Empirical Baseline Results

| ID | Class | Query / Scenario | Expected Authority Owner | Baseline Files Opened | Baseline Hops | Baseline Authority Match | Notes / Stale Context Observed |
|---|---|---|---|---|---|---|---|
| **Q01** | Orchestration | "What entrypoint runs the Weekly Orchestrator?" | `.claude/skills/weekly-orchestrator/SKILL.md` | 2 (`.claude/CLAUDE.md`, `SKILL.md`) | 1 | PASS | Clean route in `.claude/CLAUDE.md` |
| **Q02** | Orchestration | "What entrypoint starts Multi-Agent Orchestration?" | `apex-meta/orchestration/00-START-HERE.md` | 2 (`.claude/CLAUDE.md`, `00-START-HERE.md`) | 1 | PASS | Clean route in `.claude/CLAUDE.md` |
| **Q03** | Orchestration | "Where is the repo map of all orchestration systems?" | `apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md` | 2 (`.claude/CLAUDE.md`, `INDEX.md`) | 1 | PASS | Explicit pointer |
| **Q04** | Mutation | "What owns confirmed durable project/task mutation?" | `.claude/skills/apex-session/SKILL.md` | 2 (`.claude/CLAUDE.md`, `SKILL.md`) | 1 | PASS | Explicitly locked in backbone contract |
| **Q05** | Mutation | "What owns deterministic calculation & report generation?" | `.claude/skills/apex-sync/SKILL.md` | 2 (`.claude/CLAUDE.md`, `SKILL.md`) | 1 | PASS | Explicitly locked in backbone contract |
| **Q06** | Mutation | "What owns proposal decomposition before execution?" | `.claude/skills/apex-plan/SKILL.md` | 2 (`.claude/CLAUDE.md`, `SKILL.md`) | 1 | PASS | Explicitly locked in backbone contract |
| **Q07** | Apex KB | "How is an Apex KB created or started?" | `.claude/skills/apex-kb/SKILL.md` | 2 (`AGENTS.md`, `SKILL.md`) | 1 | PASS | Routed from `AGENTS.md` |
| **Q08** | Apex KB | "How is an existing controlled KB resumed?" | `.claude/skills/apex-kb/SKILL.md` | 2 (`AGENTS.md`, `SKILL.md`) | 1 | PASS | Reads `manifests/run-state.json` |
| **Q09** | Apex KB | "What rule governs Apex KB patch safety?" | `AGENTS.md` & `.claude/skills/apex-kb/SKILL.md` | 1 (`AGENTS.md`) | 0 | PASS | `<file>`, `<old>`, `<new>` exact match |
| **Q10** | Informatics | "Where is the repo standard for authoring knowledge files?" | *Pre-A1 Baseline*: Split across `OKF_Format/` and doctrine | 4 (`AGENTS.md`, `OKF_Format/index.md`, `doctrine.md`, `practice-guide.md`) | 3 | WARN (Split Authority) | No single canonical informatics package |
| **Q11** | Informatics | "Where is the Information Mapping design research?" | `apex-meta/kb/.../informatics-design-formats-practice-guide.md` | 3 (`adoption-project/index.md`, `research-location.md`, `practice-guide.md`) | 2 | PASS | Resolved via research location doc |
| **Q12** | Informatics | "Where are the chunking rules and failure modes defined?" | `.claude/skills/weekly-orchestrator/references/roles/informatics-design-doctrine.md` | 2 (`research-location.md`, `doctrine.md`) | 1 | PASS | Defined in weekly role doctrine |
| **Q13** | OKF | "What makes a concept file conformant to OKF v0.2?" | `apex-meta/SmallSkills/OKF_Format/conformance-rules.md` | 2 (`OKF_Format/index.md`, `conformance-rules.md`) | 1 | PASS | Grounded in OKF v0.2 reference bundle |
| **Q14** | OKF | "What frontmatter is required for an OKF root index.md?" | `apex-meta/SmallSkills/OKF_Format/conformance-rules.md` | 2 (`OKF_Format/index.md`, `conformance-rules.md`) | 1 | PASS | `okf_version: "0.2"` |
| **Q15** | OKF | "Are custom local type values allowed in OKF bundles?" | `apex-meta/SmallSkills/OKF_Format/conformance-rules.md` | 2 (`OKF_Format/index.md`, `conformance-rules.md`) | 1 | PASS | Local profile extension is expected |
| **Q16** | OKF | "Does a .okf.md file extension prove OKF conformance?" | `apex-meta/SmallSkills/OKF_Format/adoption-project/apex-meta-okf-usage-audit.md` | 2 (`adoption-project/index.md`, `audit.md`) | 1 | PASS | Extension does not prove conformance |
| **Q17** | Evidence | "Where is the rationale for progressive disclosure?" | `apex-meta/kb/.../token-efficient-information-design.md` | 3 (`adoption-project/index.md`, `research-location.md`, `doc.md`) | 2 | PASS | Source-cited synthesis |
| **Q18** | History | "Where is the Hermes migration failure documented?" | `apex-meta/AI-Snippets/AIFailure/HERMES-MIGRATION-HANDOVER-OKF-v0.2.md` | 2 (`audit.md`, `HERMES-*.md`) | 1 | PASS | Historical failure evidence |
| **Q19** | History | "Where is the OKF usage audit recorded?" | `apex-meta/SmallSkills/OKF_Format/adoption-project/apex-meta-okf-usage-audit.md` | 2 (`adoption-project/index.md`, `audit.md`) | 1 | PASS | Grounded audit |
| **Q20** | Negative Routing | "Push requested files to origin main" | `AGENTS.md` (Git Dispatch) | 1 (`AGENTS.md`) | 0 | PASS | Starts git commands directly; 0 informatics loaded |
| **Q21** | Negative Routing | "Deploy Alpine Nginx / Valkey stack" | `apex-meta/Alpine/ImplementationPlans/` | 1 (`00-START-HERE.md`) | 0 | PASS | Zero informatics loaded |
| **Q22** | Negative Routing | "Run ASR speech pipeline evaluation" | `SourceTranscriptionAnalysisPipeline_Research/` | 1 (`00-INDEX.md`) | 0 | PASS | Zero informatics loaded |
| **Q23** | Negative Routing | "Autonomous task without operator confirmation" | `.claude/CLAUDE.md` | 1 (`.claude/CLAUDE.md`) | 0 | PASS | Stopped by Global Boundaries |
| **Q24** | Copilot Routing | "What is this repo and how to write knowledge?" | `.github/copilot-instructions.md` | 1 (`copilot-instructions.md`) | 0 | **FAIL (Stale Context)** | Reports repo is an Obsidian-only wiki framework |

---

## 3. Baseline Summary Findings

1. **Orchestration & Mutation Routing**: Strong, clear, and unambiguous in `.claude/CLAUDE.md`.
2. **Informatics Discovery**: Fragmented across research documents and role doctrines without a single canonical package root.
3. **Copilot Instructions**: Stale legacy artifact claiming the repository is only an Obsidian wiki framework.
4. **Negative Routing**: Intact for operational tasks (Git, Docker, ASR).

This benchmark will be rerun after Wave 1 / Patch Sequence A1 to verify zero regressions on Q01–Q09 and Q20–Q23, and resolution of Q10 and Q24.
