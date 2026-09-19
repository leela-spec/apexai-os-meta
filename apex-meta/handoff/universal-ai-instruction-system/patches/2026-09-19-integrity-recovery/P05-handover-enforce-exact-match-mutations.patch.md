---
type: ExactMatchPatch
title: P05 — Enforce deterministic bounded edits for existing files
status: APPLIED
target: apex-meta/handoff/universal-ai-instruction-system/09-MODULE-DEEPENING-HANDOVER.md
base_verified: 9a165f92f62f4ed18862995652f2cf3ee3d140fb
---

<old>
## Modification rules

During this run you may modify only:

- the selected module's research folder;
- the selected module block in `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` when evidence supports a change;
- the module status table in `README.md`.

Do not modify:
</old>

<new>
## Modification rules

During this run you may modify only:

- the selected module's research folder;
- the selected module block in `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` when evidence supports a change;
- the module status table in `README.md`.

### Existing-file mutation integrity

For every **existing** file, use a bounded exact-match edit. Do not regenerate an existing file from memory, reconstructed context, a summary, or a newly authored replacement.

Required procedure:

1. Re-read the target file from latest `main` immediately before editing.
2. Copy the exact intended edit region character-for-character into an `<old>` block.
3. Put only the localized replacement in `<new>`.
4. Require `<old>` to match **exactly once**. Zero or multiple matches = stop.
5. Keep one logical change per old/new block.
6. Never use whole-file replacement for a localized edit.
7. If a large restructure is genuinely required, preserve superseded material explicitly as history/archive or an additive appendix before removal.
8. Inspect the exact Git diff before commit. Unrelated churn, unexpected deletions, reordered untouched content, or large unplanned add/delete counts = reject and restore.
9. New-file creation is allowed only for genuinely new authorized artifacts, never as an indirect replacement for an existing file.
10. If the available tool cannot guarantee bounded exact-match mutation, do **not** edit the file. Produce an exact-match patch artifact for a deterministic CLI executor instead.

Do not modify:
</new>
