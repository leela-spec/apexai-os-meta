# D05 Appendix — Apex as Reviewed Shared-Skill Source

**Decision status:** ACCEPTED DIRECTION / PILOT REQUIRED  
**Decision ledger:** `../DECISIONS.md`  
**Primary subject file:** `../06-SHARED-SKILL-PROMOTION-AND-CRON.md`

## Decision

After a controlled promotion/deployment pilot, Apex becomes the canonical Git source for reviewed project-neutral shared skills. Runtime learned-skill scratch state remains separate from that canonical source.

## Forces

- useful procedures should be reusable across roles and repos;
- canonical shared procedures need version history, review and rollback;
- Hermes supports external skill directories and project-local skills;
- external skill directories can be writable if filesystem permissions allow, so canonical source must not be routine self-improvement scratch space;
- domain-specific skill libraries should remain siloed when not needed elsewhere.

## Intended hierarchy

```text
project-local skills
  > profile-local/learned skills
  > deployed shared skills

Apex Git canonical shared source
  -> reviewed deployment
  -> runtime shared-skill directory
```

## Promotion gate

A candidate is eligible only when it is:

- project-neutral;
- secret-free;
- repeated/proven enough to justify reuse;
- not already covered by a stronger upstream skill;
- narrow enough to trigger reliably;
- explicit about verification/failure behavior.

## Risks

- canonical source can be corrupted if autonomous skill-management writes directly into it;
- overly aggressive promotion creates a noisy skill catalog;
- copied upstream skills can drift from their upstream source;
- a cross-client skill may not behave identically in Hermes, Claude Code and Codex.

## Shortcomings

- requires a promotion/deployment step rather than instant global availability;
- shared skill compatibility across AI clients must be proven per client;
- the exact canonical/deployment directory layout is not locked until the pilot.

## Rejected alternatives

1. **All agents write directly to Apex shared skills** — rejected: weak review boundary and accidental global behavior change.
2. **Copy every skill into every repo** — rejected: duplication/drift.
3. **Globalize all domain libraries** — rejected: irrelevant capability/context surface.

## Implementation consequence

Pilot one small project-neutral skill from role-local learning through independent review, Apex commit, deployment, discovery by two intended profiles, rollback, and version verification. Lock the production path only after that test.

## Watch / revisit conditions

Revisit package/distribution mechanics if Hermes profile distributions or a common Agent Skills installer proves more reliable than an external-dir deployment while preserving local memory/auth/session boundaries.

## Evidence links

- Hermes skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Hermes profile distributions: https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions
- Agent Skills specification: https://agentskills.io/specification
- Current promotion process: `../06-SHARED-SKILL-PROMOTION-AND-CRON.md`
