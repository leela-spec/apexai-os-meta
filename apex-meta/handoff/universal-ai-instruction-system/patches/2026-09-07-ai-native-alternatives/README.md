---
type: PatchPack
title: AI-native alternatives — additive exact-match patch set
description: Optional deterministic patches that add AI-native alternatives beside the existing A01–A05/module-research baselines without replacing the baseline wording.
status: NOT_APPLIED
created: 2026-09-07
source_audit: ../../10-AI-NATIVE-RETROACTIVE-AUDIT-A01-A05.md
---

# AI-native alternatives — additive patch set

## Purpose

This pack intentionally does **not** choose a winner. It converts the 2026-09-07 AI-native audit proposals into additive exact-match patches so the existing discipline-grounded versions and the newer AI-native versions can coexist and be evaluated side by side.

The patches themselves are repository artifacts only. None of the target files is modified by this commit.

## Deterministic patch contract

Each patch uses one literal `<old>` / `<new>` pair:

1. Match the `<old>` body character-for-character against the live target file.
2. Replace it with the `<new>` body.
3. The `<new>` body repeats the entire matched baseline anchor and **adds** the alternative; it does not delete or rewrite the baseline candidate.
4. Apply at most once. If `<old>` does not match exactly, stop and re-read the live file rather than reconstructing the text.
5. Do not combine unrelated edits across patch files.

## Patch inventory

| Patch | Target | Effect |
|---|---|---|
| `P01-A01-target-add-ai-native-alternative.patch.md` | `module-deepening/A01-target-outcome-alignment/README.md` | Adds AI-native A01 as Alternative B; baseline remains intact. |
| `P02-A02-scope-add-ai-native-alternative.patch.md` | `module-deepening/A02-scope-non-goals/README.md` | Adds positive-autonomy A02 as Alternative B; baseline remains intact. |
| `P03-A03-reuse-add-ai-native-alternative.patch.md` | `module-deepening/A03-reuse-before-invention/README.md` | Adds conditionally triggered external-reuse alternative; baseline remains intact. |
| `P04-A05-intent-add-ai-native-alternative.patch.md` | `module-deepening/A05-intent-alignment-clarification-threshold/README.md` | Adds intent-inference/default-to-action alternative; baseline remains intact. |
| `P05-pilot-add-ai-native-alternative-set.patch.md` | `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` | Adds a non-active alternative A01–A05 candidate set below the existing full pilot. |
| `P06-program-readme-add-research-profile-alternatives.patch.md` | `README.md` | Adds an explicit research-profile comparison: AI-native-first vs legacy discipline-first comparator. |
| `P07-handover-add-research-profile-alternatives.patch.md` | `09-MODULE-DEEPENING-HANDOVER.md` | Adds the same research-profile choice to the reusable execution handover. |

## Intentionally no semantic patch

- **A04 `<workflow>`:** the retroactive audit verdict is `KEEP`; no alternative wording is manufactured merely for symmetry.
- **A06+ modules:** not yet researched under the corrected method; no speculative alternatives are created.
- **Audit file:** `10-AI-NATIVE-RETROACTIVE-AUDIT-A01-A05.md` already records baseline vs proposed alternatives and therefore needs no additive alternative patch.

## Suggested evaluation labels

Use these labels consistently after applying any patch:

- **Baseline / A:** current completed module wording.
- **AI-native / B:** audit-derived alternative wording.
- **Unselected:** neither version becomes canonical merely because it is present.
- **Selected after eval:** only after representative cross-agent tests justify promotion.

## Selection principle

Presence is not precedence. The purpose of these patches is to preserve competing hypotheses until the later synthesis/evaluation phase can compare behavioral quality, over-triggering, autonomy, context cost, and cross-agent portability.