---
type: ExactMatchPatchPacket
title: C01 Intent-Surface Preservation Correction
status: PENDING_APPLICATION
created: 2026-09-22
repository: leela-spec/apexai-os-meta
branch: main
base_verified: 97484ccf665c07c420dbc46f7200591eb228c99c
---

# C01 Intent-Surface Preservation Correction

## Purpose

Correct one semantic defect in the completed C01 decision module without directly mutating existing files in this chat.

The operator rejected the phrase **"smallest needed choice"** because it can optimize for minimizing operator interaction at the expense of preserving the full intent-relevant decision. The replacement principle is:

> **Autonomy for delegated implementation decisions; fidelity for operator-owned decisions.**

The agent should remove irrelevant implementation noise, but it must not compress away material dimensions of a decision that belongs to the operator.

## Desired invariant

~~~text
delegated or evidence-determined trade-off
  -> agent resolves autonomously

material operator-owned choice
  -> preserve the full intent-relevant decision surface
  -> show viable alternatives
  -> show decisive criteria, evidence, consequences, uncertainty
  -> recommend when justified
  -> surface the remaining choice clearly

NEVER
  -> shrink the decision merely to minimize operator interaction
  -> hide material trade-offs
  -> manufacture numerical certainty
~~~

## Patch files

1. `P01-C01-result-preserve-full-decision-surface.patch.md`
   - patches the completed C01 module result;
   - removes the "smallest choice" optimization;
   - aligns the compact method and final invariant with full intent-surface preservation.

2. `P02-pilot-C01-preserve-full-decision-surface.patch.md`
   - patches only the C01 XML block in the non-active pilot.

## Constraints

- Do not patch these files through whole-file replacement.
- Apply literal exact-match replacements only.
- Do not change C01 status, C02 status, A13, C02, the Source-Governed Execution Contract, or the graded-rigor project as part of this correction.
- After applying both patches, inspect the exact diff before commit.
- Commit the correction atomically on `main`.
