---
type: Adapter
id: ADPT-EXEC-QA-v0.2
title: Adapter 1 — Q&A Decision Matrix (EM-06)
description: Structure and canonical example for every operator-facing decision matrix: options, mechanism, grounding, raw I/E/R, recommendation, rejection lines.
tags: [execution-modes, decision-matrix, qa, em-06]
status: current
---

## 2. Adapter 1: Q&A Decision Matrix

- **EM-06 [P1 | I92/E94/R10] Conditional Q&A Trigger**:
  - **IF** resolving a high-impact architectural trade-off, ambiguous requirement, or interactive Q&A alignment game with the operator → **THEN** structure every question using the Q&A Decision Matrix below.
  - **ELSE IF** the choice is routine, low-stakes, and easily reversible → **THEN** decide autonomously from evidence and **SKIP** this adapter.

### 2.1 Decision Matrix Structure
Every decision matrix block contains the following components:

- **Question**: State the exact problem or decision being resolved.
- **Options**: Enumerate viable options (`Option A`, `Option B`, etc.):
  - *Mechanism*: Detail the technical design in 2–4 concise lines.
  - *Grounding*: Provide a concrete real-world example, process flow, or user story so a reader without deep domain context can immediately grasp the practical impact.
  - *Raw 3-Metric Estimate*: Tag each option with unaggregated estimates `(I<val>/E<val>/R<val>)` on a 1–100 scale (`Impact`: value/effectiveness; `Evidence`: empirical support; `Risk`: misjudgment/complexity/aftermath).
- **Recommendation**: State the recommended option letter.
- **Reasoning**: Provide a dense, evidence-backed justification for the recommended option.
- **Notes**: Provide one concise line per rejected option stating its decisive disqualifier (`Letter — rejection reason`).

### 2.2 Canonical Decision Matrix Example
```markdown
- *Question:* Which state management library should the Flutter mobile client adopt?
- *Options:*
  - Option A (Bloc): Event-driven reactive architecture separating business logic from UI via streams. Grounding: Standard pattern in enterprise banking apps with strict audit logging. (I85/E95/R20)
  - Option B (Riverpod): Compile-safe dependency injection and reactive caching framework. Grounding: Lightweight mobile commerce app requiring rapid prototyping and minimal boilerplate. (I90/E90/R15)
  - Option C (SetState / Vanilla): Native widget-tree state passing. Grounding: Single-screen internal utility tool. (I40/E80/R70)
- *Recommendation:* Option B
- *Reasoning:* Option B delivers compile-time safety and minimal boilerplate while satisfying our offline caching requirements with ~40% less code than Option A.
- *Notes:*
  - Option A — Rejected due to heavy boilerplate overhead that slows velocity for a two-person team.
  - Option C — Rejected because widget-tree coupling fails scalability and testability requirements.
```

### 2.3 Intensity Lever

- **EM-06a [P1 | I85/E40/R30] Depth Scales With The Question's Own Estimate**:
  - **IF** a question triggers EM-06 → **THEN** score the decision itself `(I/E/R)`, pick the level below, and print it in the question heading, e.g. `L3 (I90/E55/R70)`.
  - **IF** the operator names a level (e.g. "treat this as L2") → **THEN** use it.
  - Low `E` raises the level: a high-impact choice with little evidence needs more process, not less.

| Level | Trigger (thresholds illustrative, unmeasured) | Adds to the 2.1 matrix |
|---|---|---|
| **L0** | Low impact and reversible | Nothing. Decide and state it (EM-06 `ELSE`). |
| **L1** | Medium impact | The 2.1 matrix as is. |
| **L2** | `I` ≥ 80 | One worked example per option on real data. Evidence labelled by source: measured, recorded decision, or inferred. Cost to reverse each option. What would change the recommendation. |
| **L3** | `I` ≥ 80 and (`R` ≥ 50 or `E` ≤ 60); or irreversible; or cross-feature | All of L2, plus: two or more user stories or personas per option; a simulation of each option on fixtures; a comprehension-check round before the questions; one reply sheet answered by letters, every recommendation a default accepted by silence; independent verification per `bake-off.md`. |

- **Real data only**: worked examples and stories use numbers from the repo's fixtures or records, never invented ones.
- **Running persona**: reuse one named persona across all questions of a sheet so answers stay comparable.
- **Tune before trusting**: thresholds have no measured basis. Calibrate against past operator decision sheets before treating them as fixed.

---
