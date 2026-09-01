# M06 — Canonicalize the Implementation-Plan Family

## Goal

Remove ambiguity caused by two overlapping implementation-plan families in `apex-meta/Alpine/ImplementationPlans/`.

## Depends on

M05 PASS.

## Required active context

Read only:

- correction control files;
- this module;
- directory tree of `apex-meta/Alpine/ImplementationPlans/`;
- `00-START-HERE.md`;
- `README.md`;
- filenames and headers of both generic and Antigravity plan sets.

Do not load full contents of every plan unless needed to determine whether two files are semantically distinct.

## Current defect

The directory contains the original generic implementation plans and the later Antigravity-hardened plans. `README.md` indexes the generic family while `00-START-HERE.md` points to the Antigravity family. This creates competing authority for future agents.

## Canonicalization policy

The Antigravity-hardened family is the execution authority for Antigravity. The original generic plans may remain only as reference/history if they preserve useful source detail.

Choose the smallest durable structure that makes this unambiguous. Preferred options, in order:

1. move generic originals under a clearly named `reference/` or `archive/` subfolder and keep the Antigravity execution set at the active root; or
2. if moving would break material external references, retain files in place but add one canonical manifest/README that marks every generic file `REFERENCE_ONLY` and every Antigravity file `EXECUTION_AUTHORITY`.

Do not maintain two unlabeled active sequences.

## Scope

Allowed:

- `apex-meta/Alpine/ImplementationPlans/README.md`
- plan-location moves/renames necessary to create one authority line
- minimal link patches caused by those moves

Do not rewrite plan bodies merely to harmonize wording.

## Verification

Positive:

- one START-HERE path leads to exactly one executable sequence;
- README explicitly identifies canonical execution files;
- all internal links resolve after any move;
- Git history preserves generic originals if archived.

Negative/adversarial:

- ask: could a fresh Antigravity instance reasonably choose the generic plan sequence as equally authoritative? If yes, fail the module;
- search for stale links to moved generic files.

## Acceptance

PASS when there is one unmistakable current execution authority and any retained alternatives are clearly non-authoritative reference material.

Persist M06 result with before/after file map, update state, commit only authority/organization changes, context-reset, continue M07.