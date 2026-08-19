# V3 OpenClaw ↔ Antigravity Orchestration Contract

**Status:** AUTHORITATIVE RELAY CONTRACT  
**Date:** 2026-08-19

## 1. Purpose

Remove the operator from copy/paste transport between ChatGPT and Antigravity without turning OpenClaw into another reasoning layer.

OpenClaw is a **mechanical relay and process supervisor**.

## 2. Shared-state model

Git/main is the durable state bus.

ChatGPT writes/updates the active work package in:

`SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/CURRENT-WORK.md`

OpenClaw reads that file and launches the exact active module.

Antigravity works in the repository and commits useful results to `main`.

ChatGPT later reads GitHub directly at review gates. The operator should not paste CLI transcripts or commit summaries unless GitHub itself is unavailable.

## 3. Relay agent boundary

Do not repurpose the existing protected `apex-executor` design whose authority contract forbids planner/router/scheduler behavior.

Prefer either:

- a separate minimal OpenClaw `ttk-relay` agent/profile; or
- one bounded OpenClaw invocation with only `exec` and `process` available.

No browser tool is required for initial V3 orchestration.

## 4. OpenClaw tool surface

Required only:

- `exec`;
- `process`.

Use `exec(..., pty=true)` when Antigravity needs a TTY.

Use background/process operations to:

- poll status;
- read logs;
- detect likely input wait;
- send literal input or keypresses only when explicitly authorized;
- terminate a stuck process.

Do not add a custom queue/database merely because process state is in-memory. Git commits and module result files are the durable recovery points.

## 5. Antigravity launch strategy

Never assume a transport mode from documentation alone.

At M00:

1. run `agy --version`;
2. verify auth works;
3. run a small headless text-only smoke;
4. verify captured output and exit code;
5. run a bounded workspace-capability smoke under safe permissions;
6. if all required headless behavior passes, headless is permitted for modules that fit it;
7. otherwise use interactive `agy` inside OpenClaw PTY.

Current external docs/changelog (verified 2026-08-19) show that Antigravity 1.1.x fixed several earlier headless problems, but current open issues still report permission-scope limitations. Therefore capability detection is mandatory.

Do not use `--dangerously-skip-permissions` as the normal solution.

## 6. Permissions

Antigravity's current official permissions model is `deny > ask > allow` with action resources such as `read_file(...)`, `write_file(...)`, `read_url(...)`, `command(...)`, etc.

Use the narrowest practical workspace/project policy.

Allowed examples may include only commands actually needed for the module, such as:

- git status/diff/log/show;
- language/package manager commands required by the selected candidate;
- test commands;
- exact acquisition/transcription commands when the module owns them.

Keep dangerous/destructive commands denied.

OpenClaw must not automatically answer a permission or semantic question whose correct response requires judgment. In that case return `OPERATOR_DECISION`.

## 7. Module lifecycle

```text
1. OpenClaw reads CURRENT-WORK.md
2. verifies requested module file exists
3. verifies repo is main and working context is acceptable
4. launches fresh Antigravity context
5. Antigravity reads only:
   - CURRENT-WORK.md
   - active Mxx module
   - files explicitly named by that module
6. Antigravity performs normal research/run/test/repair loop
7. Antigravity saves Mxx-RESULT.md and commits useful work to main
8. process exits
9. OpenClaw records only mechanical result:
   - exit status
   - observed commit SHA if any
   - result-file existence
10. next action follows module plan
```

## 8. Automatic progression

OpenClaw may start the next module without ChatGPT review only when:

- the implementation plan explicitly makes the next module unconditional;
- current result status is PASS;
- no `REVIEW_GATE`, `OPERATOR_DECISION`, `APPROACH_SUSPECT`, or `BLOCKED` appears;
- the next module has a separate context file.

Required ChatGPT review gates are M01, M05 and M07.

At a review gate OpenClaw stops. The operator only needs to tell ChatGPT something equivalent to `review M01`; ChatGPT reads GitHub itself.

## 9. Anti-drift supervision

OpenClaw does not assess product quality, but it can enforce mechanical stop markers.

If Antigravity emits:

- `OPERATOR_DECISION` -> stop;
- `APPROACH_SUSPECT` -> stop;
- `BLOCKED` -> stop;
- `REVIEW_GATE` -> stop;
- repeated process crash -> apply relay repair budget.

## 10. Repair budgets

### Relay

One repair cycle.

If the relay breaks a second time before completing a real product-advancing task:

`RELAY_FALLBACK_DIRECT_AGY`

Then run future module files directly in Antigravity; do not spend more project time on OpenClaw.

### Executor/module approach

Two corrective iterations on the same subsystem without product advancement.

After strike two, Antigravity must not perform correction #3. It writes `APPROACH_SUSPECT` and stops.

## 11. What is deliberately deferred

Not part of V3 initial implementation:

- OpenClaw browser control of this ChatGPT conversation;
- a custom Antigravity ACP adapter;
- TaskFlow/Lobster workflow authoring unless the simple relay proves insufficient after the pipeline works;
- custom job database;
- automatic semantic approval by local Qwen;
- full autonomous cross-chat loop.

These can be reconsidered only after the transcript product succeeds.
