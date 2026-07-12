# Meta Ops Doctrine

The weekly orchestrator holds operator gates and routes its bounded stages. `apex-plan`, `apex-sync`, and `apex-session` remain independent project-engine capabilities: weekly reads confirmed Session and supplied Sync handoffs, then returns an approved status-merge proposal to Session.

## Rules

- Dispatch only the stage required by the current loop position; do not fan out speculative work.
- Preserve the distinction between evidence, candidate changes, operator approval, Session mutation, and confirmed planning context.
- Do not self-validate a consequential Session-mutation proposal; use the named review when the review contract applies.
- Do not create project/task state, Plan packets, Sync reports, or calendar/runtime actions from weekly routing.
