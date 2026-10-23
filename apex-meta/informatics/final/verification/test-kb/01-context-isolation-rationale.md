---
type: Reference
id: TEST-KB-01-CONTEXT-ISOLATION
title: Test Rationale 01: Context Isolation & JIT Router Dispatch
description: Empirical rationale and failure-mode analysis for Context Isolation tests in test_tier5_adversarial.py.
status: current_truth
tags: [informatics, verification, test-kb, context-isolation]
---

# Test Rationale 01: Context Isolation & JIT Router Dispatch

## 1. Defect Class Addressed
- **Failure Mode:** Eager monolithic context loading. Agents routinely ingest entire specification libraries (~15,000–30,000 tokens) on every turn, causing severe attention distraction, instruction dilution, and high token costs.
- **Enforcing Tests:** `test_tier5_adversarial.py` (`test_cis_01` through `test_cis_08`).

## 2. Operative Guarantee
- The agent router must match ONLY the specific task intent (e.g. `writing_or_documentation` loads ONLY `writing-profile.md`).
- Achieves **>= 70% token savings** compared to monolithic full-stack loading.
- Root router must adhere strictly to `< 4,000 characters` (< 1,000 tokens) and `< 100 lines`.

## 3. Grounding in Research
- Provenance: [`final/research/01-universal-instruction-research/module-deepening/A06-context-engineering-progressive-disclosure/`](../../research/01-universal-instruction-research/module-deepening/A06-context-engineering-progressive-disclosure/)
- Operational Codification: [`<context>`](../../research/06-layered-rule-kb/rule-08-context.md) and [`<pointers>`](../../research/06-layered-rule-kb/rule-22-pointers.md).
