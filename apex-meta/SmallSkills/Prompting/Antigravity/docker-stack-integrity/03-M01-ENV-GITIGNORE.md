# M01 — Protect Real `ki-basis/.env` from Git

## Goal

Ensure the real runtime `.env` file cannot be accidentally committed.

## Required active context

Read only:

- correction START HERE + orchestrator + context protocol;
- this module;
- root `.gitignore`;
- `ki-basis/.env.example`;
- Git status/index state for `ki-basis/.env`.

Do not load unrelated service plans or runtime documentation.

## Current defect

The repo contains `.env.example`, but the root `.gitignore` does not explicitly protect `ki-basis/.env`, and no local `ki-basis/.gitignore` is canonical in Git.

## Scope

Allowed existing-file patch:

- `.gitignore`

Optional new evidence/state files only as required by the program protocol.

Do not modify `ki-basis/.env.example` in this module.

## Implementation

Add the narrowest explicit ignore rule that protects the real stack env file, preferably:

```gitignore
/ki-basis/.env
```

If a broader existing repo convention is already authoritative, use it only if it provides equal or stronger protection without hiding committed examples/templates.

## Verification

Positive:

1. create or use a non-secret disposable `ki-basis/.env` locally;
2. `git check-ignore -v ki-basis/.env` must identify the new rule;
3. `git status --short --untracked-files=all` must not offer the real `.env` for commit;
4. `ki-basis/.env.example` must remain tracked.

Negative/adversarial:

- verify `.env.example` is **not** ignored;
- verify no wildcard accidentally ignores other required tracked configuration.

## Secret hygiene

Do not print or commit the contents of the real `.env`.

## Acceptance

PASS only when Git deterministically ignores `ki-basis/.env` while continuing to track `.env.example`.

Write `apex-meta/Alpine/IntegrityResults/M01-RESULT.md`, update program state, commit only M01-scoped files, then context-reset and continue to M02.