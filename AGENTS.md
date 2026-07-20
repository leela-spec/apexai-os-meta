# Codex Operating Note

## Git Dispatch
- Trigger: A request to push known files starts with the Git commands, not repository analysis.
- Sequence: Run `git add -- <requested paths>`, `git commit`, and `git push`.
- Retry: On non-fast-forward, run `git pull --rebase` and retry the push.
- Ignore: Unrelated dirty files are irrelevant and must not trigger inspection, stashing, worktrees, branches, or discussion.
- Escalate: Investigate only an actual command failure involving the requested files, validation, authentication, or merge conflicts.
- Stop: Report success immediately after the push completes.

## Directness
- Rule: For a simple push, commit, or file move, take the shortest correct path and finish it.
- Rule: Do not invent extra workflow, guardrails, retries, or analysis unless the task actually needs them.
- Rule: If the user says to push, stage the requested files, commit if needed, and push.
- Rule: Ignore unrelated dirty files unless they directly block the requested files.
- Rule: If the remote moved, integrate normally and continue without turning it into a bigger process.

## Core Intent Execution
- Execute: Produce the requested deliverable; process serves production and never substitutes for it.
- Target: Keep every action tied to the requested output and verify that output exists before reporting completion.
- Ignore: Leave unrelated dirty files, incidental warnings, and optional checks out of the critical path.
- Preserve: Keep intentional source bytes, formatting, and current contracts unchanged unless the target requires a change.
- Classify: Stop only for a genuine target, safety, authorization, or integrity blocker.
- Workaround: Resolve incidental failures with the narrowest safe, intent-preserving alternative and continue.
- Decide: Resolve low-stakes procedural choices with a reasonable default instead of gating delivery.
- Report: State the current result and exact unresolved blocker; do not narrate superseded content in working instructions.
- Current-truth: Keep working content limited to live guidance; place history in a dedicated log or memory.
- No-changelog: Do not retain old errors, rejected options, prior versions, incident narratives, or "what changed" explanations in current-truth content.

## Scope
- Rule: Keep actions tied to the user's stated target.
- Rule: Do not expand the task into adjacent cleanup, redesign, or general hardening.
- Rule: Prefer one clear action over a long plan when the outcome is already obvious.

## Apex KB Dispatch
- New KB: When the operator asks to create, build, initialize, or start a new Apex KB, read `.claude/skills/apex-kb/SKILL.md` and use its Start workflow. Do not begin with the generic executor-capability question and do not manually select `control init`, `source-intake`, or `phase0`.
- Public entrypoint: New-KB Setup uses `python apex-meta/scripts/apex_kb.py start --config <start-config.yaml> --repo-root <repository-root>` in preview mode first. Writes require explicit `--allow-write` after operator review.
- Existing controlled KB: When `<kb-root>/manifests/run-state.json` exists, continue through `control next`, `control run`, or `control reconcile` as directed by canonical state.
- Boundary: Start owns new-KB configuration, validation, preview, and initialization. It stops before deterministic corpus intelligence unless the operator explicitly requests later stages.