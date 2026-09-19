---
type: RepositoryIntegrityRecoveryPacket
title: Universal AI Instruction System — Whole-File Rewrite Integrity Audit
status: PATCHES_NOT_APPLIED
created: 2026-09-19
repository: leela-spec/apexai-os-meta
branch: main
base_verified: 9a165f92f62f4ed18862995652f2cf3ee3d140fb
---

# Whole-file rewrite integrity audit and recovery packet

## Purpose

Prior AI edits sometimes replaced large portions of existing files when the intended operation was a localized patch. This packet does **not** apply repairs. It provides deterministic exact-match patches for a CLI agent that can enforce literal-match editing.

## Audit scope

Reviewed every commit touching `apex-meta/handoff/universal-ai-instruction-system/` from the initial program commit `98f75197...` through `9a165f92...`, plus the graded-rigor epic.

## Findings

| Commit | Existing file | Churn | Classification | Recovery |
|---|---|---:|---|---|
| `d361bb0055d6678f8a771d891fd80e0cc33eace7` | program `README.md` | +148 / -22 | intentional current-truth rewrite, but original research index/discoverability was lost | P01 |
| `a6485b38ece182444c13ba01e96de3b9d3b43159` | `09-MODULE-DEEPENING-HANDOVER.md` | +68 / -38 | research-order refactor; semantic coverage expanded | no restore; P05 prevents recurrence |
| `54d7a12d14324b82a7649c78a02f62a101513b55` | program `README.md` | +30 / -16 | research-order refinement; semantic coverage expanded | no restore |
| `aebd3f27f6e3ee3c6ce4fb655fb40a77a8fc5259` | A01 result | +159 / -162 | **high-risk replacement; useful pre-merge research disappeared** | P02 |
| `ce9582f0cd439ea66a770523e0e485d7ba14f4b9` | A03 result | +53 / -35 | controlled strengthening; prior candidate explicitly retained as superseded | no restore |
| `bdc9a657e1237cc02519cc4cfbf0beaa15053f3a` | A13 result | +263 / -514 | **confirmed information loss** | P03 |
| `9a165f92f62f4ed18862995652f2cf3ee3d140fb` | A13 result | +235 / -301 | **confirmed information loss** | P03 |
| `9a165f92f62f4ed18862995652f2cf3ee3d140fb` | graded-rigor epic | +94 / -188 | **confirmed information loss** | P04 |

All other program commits were either new-file additions or small bounded edits, normally 1–3 changed lines in the live README/pilot, and did not show the destructive-replacement signature.

## Recovery principle

Do **not** replace current files with historical versions.

Instead:
- preserve current decisions;
- add exact, explicit pointers to superseded research;
- recover lost material from Git history with `git show <commit>:<path>`;
- optionally materialize those historical snapshots into archival companion files only if the operator wants physical copies;
- never silently reintroduce superseded wording as current authority.

## Deterministic execution contract

For every patch file in this folder:

1. update local `main`;
2. read the target file from disk;
3. copy the literal text between `<old>` and `</old>`;
4. verify it occurs **exactly once**;
5. replace only that substring with the literal `<new>` content;
6. do not normalize whitespace, headings, punctuation, or surrounding lines;
7. show the diff;
8. abort if any unrelated line changes;
9. after all patches, run `git diff --check`;
10. commit only after the operator/agent verifies the exact target diff.

## Patch order

1. P01 — restore background research discoverability
2. P02 — preserve A01 pre-merge research
3. P03 — preserve A13 superseded research
4. P04 — preserve graded-rigor superseded research
5. P05 — prevent future whole-file regeneration

## Acceptance

- current A01/A13/graded-rigor decisions remain unchanged;
- current module status remains unchanged;
- historical evidence is discoverable and explicitly marked superseded;
- no patch uses whole-file replacement;
- future module instructions prohibit whole-file regeneration of existing files.
