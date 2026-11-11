---
type: Adapter
id: ADPT-EXEC-BAKEOFF-v0.2
title: Adapter 2 — Comparison & Bake-Off Rubric (EM-07)
description: The 4-phase analytical workflow and canonical comparison matrix for evaluating competing libraries, frameworks, tools, or architectures.
tags: [execution-modes, bake-off, comparison, em-07]
status: current
---

## 3. Adapter 2: Comparison & Bake-Off Rubric

- **EM-07 [P1 | I88/E90/R12] Conditional Bake-Off Trigger**:
  - **IF** conducting a landscape scan or comparing multiple competing libraries, frameworks, tools, or architectures → **THEN** execute the 4-Phase Analytical Workflow below.
  - **ELSE IF** an existing repository tool already satisfies the requirement (`Reuse Before Build`) → **THEN** reuse the existing tool and **SKIP** this adapter.

### 3.1 4-Phase Analytical Workflow

1. **Phase 1: Candidate Discovery & Hard Gating**:
   - Identify ~3–5 viable candidates.
   - Screen each candidate against non-negotiable hard filters; disqualify failing candidates before scoring.
2. **Phase 2: Multi-Metric Evaluation Matrix**:
   - Score surviving candidates on a 1–100 scale across weighted criteria.
   - Record trade-offs in a structured Markdown comparison table including a `Primary Failure Mode` column.
3. **Phase 3: Ranked Verdicts**:
   - Rank candidates from highest to lowest and state a one-sentence placement verdict per candidate.
4. **Phase 4: Functional Prototypes & Decision Triggers**:
   - Provide syntactically complete implementation boilerplate for the winning candidates.
   - Define explicit conditional decision boundaries:
     - `"Select this if..."` `[Exact condition]`
     - `"Avoid this if..."` `[Exact disqualifying edge case]`

### 3.2 Canonical Comparison Matrix Format
| Candidate | Velocity (40%) | Scalability (35%) | Ecosystem (25%) | Weighted Total | Primary Failure Mode |
|---|---|---|---|---|---|
| Candidate A | 82 | 94 | 96 | 89.70 | Steep onboarding learning curve |
| Candidate B | 92 | 64 | 80 | 79.20 | Memory degradation under heavy throughput |
| Candidate C | 44 | 78 | 62 | 60.40 | Lack of community plugins and active maintenance |

---
