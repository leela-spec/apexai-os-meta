---
type: Reference
id: CANDIDATES-ARCHIVE-README
title: Candidates Archive — Retired Always-On Contract Candidates
description: Which candidate contract files were retired from candidates/, why, where their content lives now, and what was deliberately not carried over.
status: current
tags: [archive, candidates, apex-contract]
---

# Candidates Archive

## 16-candidate-3A-ultra.md

- **Retired:** 2026-11-06.
- **Why:** it holds 22 rules and no `<align>` rule. The live always-on contract is the 23-rule `specs/apex_contract_v1.0_ultra.xml`. The Leela vendored copy named this file as its source, so an agent following that header edited or audited a stale block.
- **Where its content lives now:** `specs/apex_contract_v1.0_ultra.xml` (the block) and `research/06-layered-rule-kb/` (the per-rule reasoning behind each tag).
- **Not carried over:** the `1,225` BPE metric and the "Milestone 5" status text describe the 22-rule block and no longer match the live one. `verification/suites/test_m5_challenger_verification.py` and `test_m6_two_layer_carrier_drafts.py` still read this file to test that historical lineage; their path constants point here.
- **Links:** Markdown links to this file were rewritten to `candidates/_archive/`. Bare mentions inside dated historical records (`operations/06`, `07`, `12-RESTRUCTURING`, research audits) were left as written.
