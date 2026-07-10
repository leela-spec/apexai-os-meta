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

## Scope
- Rule: Keep actions tied to the user’s stated target.
- Rule: Do not expand the task into adjacent cleanup, redesign, or general hardening.
- Rule: Prefer one clear action over a long plan when the outcome is already obvious.
