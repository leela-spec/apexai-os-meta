# Project Local AGENTS Override

This file is the project-local override template.

Base governance lives in the adopted managed kernel, especially:

- `managed/rules/AGENTS.base.md`
- `managed/rules/OPERATING_SPINE_CANON.md`
- `managed/rules/ESCALATION_EXCEPTION_BLOCK.md`
- `managed/rules/AGENT_SWARM_INTERACTION_CANON.md`
- `managed/rules/PROJECT_INTERFACE_CONTRACT.md`
- `managed/rules/PROMOTION_PROTOCOL.md`
- `managed/rules/QA_HYGIENE_PROTOCOL.md`

## Authority boundary

Local rules may tighten or specialize behavior for this project.

Local rules must not:

- weaken managed governance
- bypass escalation
- bypass promotion
- override the managed authority order
- convert OpState into truth
- create project-to-project authority bridges
- introduce private or operator memory into the project template

## Project-local rules

Add project-local rules here only after project initialization.

```text
TBD
```

## External actions

External actions require explicit approval under the project's governance and review rules.

Examples include:

- email or messages
- public posts
- purchases
- production deployments
- destructive commands
- credential or runtime config changes

## Drift prevention

- Prefer one foreground flow at a time.
- Start project work from `.openclaw/ProjCard.md`, `.openclaw/OpState.md`, `.openclaw/SSOT_INDEX.md`, and `.openclaw/SigMat.md`.
- Route truth changes through promotion.
- Route structural risk through QA/Hygiene or escalation.
- Keep project learnings sanitized before any upward meta submission.
