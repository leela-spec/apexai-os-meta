# Plan: Multi-Agent Knowledge Audit & Cross-Repo Lineage Mapping

## Overview
Perform a rigorous, 100% ground-truth inventory, deep evaluation, quality-and-value ranking, and cross-repo lineage mapping of all agent definitions, doctrine files, orchestration workflows, and skills across `c:\GitDev\apexai-os-meta` and `C:\Quasi Desktop\AI_PreperationUntil_06-26`.

Deliverables target: `c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit`
- `README.md`
- `agent_knowledge_matrix.csv`
- `agent_knowledge_matrix.json`

## Milestone Decomposition

### Milestone 1: Comprehensive Multi-Source Inventory & Discovery
- **Scope**:
  - Track A: Active repo `c:\GitDev\apexai-os-meta` (`.claude/agents/*.md`, `apex-meta/orchestration/agents/`, `apex-meta/orchestration/`, `.claude/skills/`, `apex-meta/skills/`).
  - Track B: Legacy archives `C:\Quasi Desktop\AI_PreperationUntil_06-26` (`Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\`, `agent_kb_source_indexes\`, uncurated sources).
  - Track C: Doctrine Manifest & Lineage delta mapping (`apex-meta/orchestration/agents/DOCTRINE-MANIFEST.md` vs legacy OpenClaw doctrine).
- **Subagents**:
  - `explorer_repo_inv`: Inventory active repo files, gathering exact paths, byte size, line count, modified time, functional domain.
  - `explorer_legacy_inv`: Inventory legacy archive files, gathering exact paths, byte size, line count, modified time, functional domain.
  - `explorer_lineage_delta`: Analyze DOCTRINE-MANIFEST.md, tracking migration deltas, superseded rules, and omitted knowledge.
- **Verification**: Zero phantom files; 100% path grounding on disk.

### Milestone 2: Evaluation Matrix & Machine Dataset Generation
- **Scope**:
  - Author `artifacts/agent_knowledge_audit/agent_knowledge_matrix.csv` and `agent_knowledge_matrix.json`.
  - Score each file across 4 dimensions (1-10 integer scale): Content Quality, Content Quantity, Machine Readability, Current Operational Value.
  - Calculate weighted Composite Score.
  - Assign Lifecycle Status (`Canonical / Active`, `Distilled / Migrated`, `Empty Scaffold / Stub`, `Reference-Only / Historical`).
  - Provide concise 1-2 sentence evidence-backed Rationale and Lineage Notes.
- **Subagents**:
  - `worker_matrix_builder`: Author CSV and JSON datasets adhering strictly to schema and scoring rubrics.
- **Verification**: CSV parses cleanly, JSON is valid, all required columns present, all scores in range [1, 10].

### Milestone 3: Executive Summary & Comprehensive Audit Report
- **Scope**:
  - Author `artifacts/agent_knowledge_audit/README.md`.
  - Sections:
    1. Executive Summary & Audit Methodology
    2. Top-Tier Leaderboard (top performers across ecosystem)
    3. Agent-by-Agent & Domain Synthesis (Alfred, Meta Ops, Meta Strategy, Meta Detective, Knowledge Bank, Informatics Design, Prompts & Workflows, AI Routing / Special Ops)
    4. Cross-Repository Lineage & Omitted Knowledge Audit (detailed cross-check with DOCTRINE-MANIFEST.md)
    5. Migration Roadmap & Consolidation Strategy
- **Subagents**:
  - `worker_report_author`: Synthesize findings into comprehensive, executive-ready documentation.
- **Verification**: README matches all findings, cross-references matrix data accurately.

### Milestone 4: Multi-Agent Gate Verification (Review, Challenge, Forensic Audit)
- **Scope**:
  - Two independent Reviewers verify correctness, completeness, and adherence to requirements.
  - Two Challengers execute stress tests and schema validations (verifying every single path on disk, testing row counts, checking scoring consistency).
  - Forensic Auditor conducts integrity forensics ensuring no fabricated data or hallucinated files.
- **Gate Criteria**:
  - All tests and validation scripts pass.
  - Reviewers APPROVE.
  - Challengers APPROVE.
  - Auditor CLEAN.
- **Status**: **ALL MILESTONES COMPLETE & VERIFIED** (Milestones 1, 2, 3, and 4 PASS)
