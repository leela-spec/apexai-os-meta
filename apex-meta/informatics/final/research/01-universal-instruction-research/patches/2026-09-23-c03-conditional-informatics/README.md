---
okf: 0.2
type: patch_packet
id: c03-conditional-informatics
created: 2026-09-23
status: proposed_not_applied
base_commit: 244c2d15a91d60e06f9989ae402efd00871c0700
---

# C03 patch packet

This packet contains the only proposed changes to existing files for C03.

The GitHub/chat orchestrator must not apply these patches directly.

## Patch order

1. `P01-C03-pilot-informatics-router.patch.md`
   - target: `apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`
   - replaces only the C03 `<informatics>` block.

2. `P02-C03-readme-status.patch.md`
   - target: `apex-meta/handoff/universal-ai-instruction-system/README.md`
   - changes only C03 status from NEXT to DONE.

After P02, the module-deepening sequence is complete. Do not invent a new NEXT module.

## Executor contract

A deterministic local/CLI executor must:

1. sync latest `main`;
2. re-read each target;
3. require the exact `old` block to match exactly once;
4. stop on zero or multiple matches;
5. apply only that one localized replacement;
6. inspect `git diff --check` and the complete diff;
7. reject whitespace/line-ending churn or unrelated changes;
8. stage only the two target files;
9. commit and push `main` without force;
10. stop.

If live `main` has changed so either exact old block no longer matches once, do not improvise. Re-author patches against live current truth.
