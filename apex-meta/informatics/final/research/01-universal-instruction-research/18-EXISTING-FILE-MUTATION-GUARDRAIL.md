---
okf: 0.2
type: repository_mutation_guardrail
id: no-direct-existing-file-mutation
created: 2026-09-22
status: active
scope: leela-spec/apexai-os-meta
---

# Existing-file mutation guardrail

## invariant

For ChatGPT / connector-driven work in this repository:

> **Never modify, rewrite, replace, delete, or directly patch an existing repository file.**

Existing files are read-only to this orchestrator.

## allowed repository writes

Only create **new additive files**, including:

- research results;
- handovers;
- patch artifacts;
- candidate Skills kept outside runtime discovery paths;
- correction/audit records.

## required method when an existing file should change

1. Re-read the current target file.
2. Create a new patch artifact.
3. Store exact `old` and `new` blocks, or an equivalent unified diff.
4. Require the old block to match exactly once.
5. Include target path, expected base SHA/blob SHA where available, validation steps, and stop conditions.
6. Do **not** apply the patch with GitHub connector write APIs.
7. A deterministic local/CLI executor or the operator applies the patch.
8. Re-read and verify after application in a later run.

## forbidden connector actions on existing files

Do not use any workflow that writes a complete replacement body for an existing file, including:

- `update_file`;
- tree/blob commits that replace an existing path;
- direct ref updates to commits containing orchestrator-authored replacements;
- delete-and-recreate;
- whole-file reconstruction from model context.

## emergency correction exception

If this orchestrator previously violated this invariant, it may make **one corrective restoration commit** that restores affected existing files byte-for-byte from their verified pre-violation commit. That restoration may not contain any new intended semantic change to an existing file.

After restoration, all intended changes return to patch-only form.

## rationale

This prevents information loss, context reconstruction errors, accidental deletion of concurrent material, and drift caused by whole-file model rewrites. It also keeps edits small, reviewable, replayable, and token-efficient.
