# Apex Codex Execution Standard

This file is persistent project memory for Apex Codex handovers.

## Core Rule

Codex is an execution orchestrator, not a reasoning agent.

All Codex prompts in this project must be stupid-simple, deterministic, and command-oriented.

## Required Codex Prompt Shape

Every Codex prompt should state only:

- repository
- branch: always `main`
- working directory
- exact files or scripts to modify
- exact commands to run
- exact expected output
- commit message
- push instruction
- final machine-readable report format

## Branch Rule

Codex must work only on `main`.

Never create feature branches, staging branches, or PR branches unless the operator explicitly overrides this in the same task.

Default ending for every Codex task:

```text
commit to main and push origin main
```

## No Interpretation Rule

Codex must not be asked to:

- redesign architecture
- reinterpret the process
- validate broad lifecycle state
- inspect unrelated files
- create alternative implementation strategies
- open unnecessary PRs
- reason about what should happen next
- run broad smoke-test loops unless explicitly requested

## Dirty / Stale State Rule

Codex should not get distracted by stale branches, unrelated local dirty files, or unrelated repo state.

If unrelated files are dirty, Codex should ignore them unless they block the exact requested task.

## Standard Codex Handover Sentence

Use this shape:

```text
Run this deterministic script/tool/patch in this repo, on main, against these exact files, then run these exact validation commands, commit to main, push origin main, and return the final machine-readable report.
```
