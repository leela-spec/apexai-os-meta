---
type: Index
title: Macro–Meso–Micro Working Method
description: Compact orientation for a hierarchical top-down definition and bottom-up verification method for AI work.
status: candidate_for_testing
---

# Macro–Meso–Micro Working Method

## Purpose

This package defines a small general orientation for how an AI should structure nontrivial work with the operator.

The local shorthand is **Macro → Meso → Micro → Meso → Macro**.

The method is not intended as a new project-management system. Its established basis is **hierarchical systems engineering**, especially the **V-model/Vee**, **requirements decomposition/flowdown**, **integration**, **verification**, and **validation**.

## Meaning

- **Macro — strategic/system level — WHY:** define the whole target, purpose, value, boundaries, environment, major parts, system-wide constraints, dependencies, and success.
- **Meso — tactical/architecture level — HOW:** decompose the target into coherent modules/sub-targets; define responsibilities, interfaces, dependencies, sequencing, and how the parts jointly satisfy Macro intent.
- **Micro — operational/realization level — WHAT:** define and execute the exact implementation, content, code, design, actions, tests, and evidence needed for each Meso module.

Work downward to define and realize the target; work upward to check coherence:

```text
Macro
  ↓ decompose / derive / allocate
Meso
  ↓ specify / realize
Micro
  ↑ verify / integrate
Meso
  ↑ validate against purpose and system constraints
Macro
```

## Candidate always-on agent instruction

> **Work at the smallest sufficient level.** Execute simple tasks directly. For nontrivial work, use hierarchical decomposition and V-model reasoning: establish Macro intent (why/system), derive Meso structure (how/modules), realize Micro details (what/implementation), then verify bottom-up Micro → Meso → Macro. Load `apex-meta/informatics/MMM/working-method.md` only when that structure is needed.

This is intentionally short. The detailed behavior lives in [working-method.md](working-method.md).

## Read next only when needed

- [established-concepts.md](established-concepts.md) — what established concepts this shorthand maps to and what it does **not** claim.
- [working-method.md](working-method.md) — compact execution behavior for nontrivial work.

## Current status

Candidate for testing. Do not yet propagate this paragraph into global agent files until it has been tested on representative simple, medium, and complex tasks.
