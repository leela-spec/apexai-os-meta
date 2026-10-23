---
type: Reference
id: TEST-KB-02-SINGLE-OWNERSHIP
title: Test Rationale 02: Single-Ownership & Durable Rule ID Uniqueness
description: Empirical rationale and failure-mode analysis for Single-Ownership tests in test_canonical_ownership.py.
status: current_truth
tags: [informatics, verification, test-kb, single-ownership]
---

# Test Rationale 02: Single-Ownership & Durable Rule ID Uniqueness

## 1. Defect Class Addressed
- **Failure Mode:** Duplicate rule IDs and drift across multiple specification files. For instance, defect `D1` occurred when `FA-04` was assigned to two unrelated rules across different modules, and `D9` occurred when an inline schema drifted from the authoritative JSON schema.
- **Enforcing Tests:** `test_canonical_ownership.py` (`test_no_duplicate_rule_id_within_a_file`, `test_no_duplicate_rule_id_across_the_suite`).

## 2. Operative Guarantee
- Every durable rule ID (`WP-XX`, `FA-XX`, `EM-XX`, `AD-XX`, `GS-XX`) is defined in exactly ONE authoritative file.
- All cross-references use `Canonical: 'XX-NN'` pointers rather than re-defining rules.

## 3. Grounding in Research
- Provenance: [`final/research/06-layered-rule-kb/`](../../research/06-layered-rule-kb/) (Chapters 2.1 and 2.2 across all 5 audit modules).
- Operational Codification: [`<current_truth>`](../../research/06-layered-rule-kb/rule-11-current-truth.md) and [`<schemas>`](../../research/06-layered-rule-kb/rule-20-schemas.md).
