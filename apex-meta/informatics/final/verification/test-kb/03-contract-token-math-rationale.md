---
type: Reference
id: TEST-KB-03-CONTRACT-TOKEN-MATH
title: Test Rationale 03: Empirical BPE Token Math & Option B Verification
description: Empirical rationale and failure-mode analysis for BPE token tests in test_m3_challenger_tokens.py and test_m5_challenger_verification.py.
status: current_truth
tags: [informatics, verification, test-kb, token-math, option-b]
---

# Test Rationale 03: Empirical BPE Token Math & Option B Verification

## 1. Defect Class Addressed
- **Failure Mode:** Hallucinated token savings and synthetic math formulas. AI agents routinely claim "saves 40% tokens" while actually increasing token count or using arbitrary synthetic weights.
- **Enforcing Tests:** `test_m3_challenger_tokens.py` and `test_m5_challenger_verification.py`.

## 2. Operative Guarantee
- Every BPE token count is computed empirically using OpenAI's `cl100k_base` tokenizer (`tiktoken`).
- All rollup table math (deltas, percentages) must match 100% exact arithmetic.
- Prohibits all synthetic calculated score formulas (`Score = I * E / R`).

## 3. Grounding in Research
- Provenance: [`final/research/06-layered-rule-kb/`](../../research/06-layered-rule-kb/) (Chapters 1.1, 1.2, and 3 Rollups across all 22 rules).
- Operational Codification: [`16-candidate-3A-ultra.md`](../../candidates/16-candidate-3A-ultra.md) (`1,225` empirical BPE tokens).
