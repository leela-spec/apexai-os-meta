# Module 07 — Status Merge / State Change Decision

## Purpose

Make project/task updates reliable without turning routine bookkeeping into repeated operator gates.

## Expected function

Classify recap-derived candidate changes into:

- routine/low-risk changes that may be applied through the authorized deterministic/session path without extra interruption;
- consequential, ambiguous, destructive, scope/priority-changing or explicitly operator-flagged changes that require review;
- rejected/deferred/unresolved candidates.

## Boundary

Session/canonical state remains the durable authority. This module decides/routes changes; it does not create a second truth store.

## Module work

Revalidate current StatusMerge, G5 and review behavior against Module 00's gate model and the operator's desire for task-dependent gating.

## Completion

Production integration -> Master authority/gate verification -> fresh routine-change and consequential-change tests -> operator acceptance.
