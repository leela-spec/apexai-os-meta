---
okf: 0.2
type: patch_packet
id: c02-conditional-research-discipline
created: 2026-09-22
status: proposed_not_applied
base_commit: d38192dcaae5ef2ec804f82778a716e296b2ffe6
---

# C02 patch packet

This packet contains the **only authorized form** of C02 changes to pre-existing files.

The orchestrator must not apply these patches directly.

## patches

1. `P01-C02-pilot-research-block.patch.md`
   - target: `apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`
   - replaces only the C02 `<research>` block.

2. `P02-C02-readme-status.patch.md`
   - target: `apex-meta/handoff/universal-ai-instruction-system/README.md`
   - advances C02 from NEXT to DONE and C03 from QUEUED to NEXT.

## application contract

A deterministic executor must:

1. read latest `main`;
2. require each `old` block to match **exactly once**;
3. stop on zero or multiple matches;
4. apply only the localized replacement;
5. inspect the exact diff;
6. reject unrelated changes;
7. commit only after verification.

If `main` has moved and the old block does not match exactly once, do not adapt from memory. Re-author a new patch against live current truth.
