# D04 Appendix — Learning Spillover Without Raw-Memory Synchronization

**Decision status:** ACCEPTED WITH CONSTRAINTS  
**Decision ledger:** `../DECISIONS.md`  
**Primary subject files:** `../05-REUSABLE-PROFILES-LEARNING-AND-MEMORY.md`, `../06-SHARED-SKILL-PROMOTION-AND-CRON.md`

## Decision

Raw Hermes profile memory stays profile-local. Project facts stay in the source repository. Learning spills across repositories/roles only after a useful behavior is generalized, reviewed and promoted as a reusable skill/procedure.

## Forces

- operator wants compounding learning across projects;
- project-specific facts must not contaminate unrelated work;
- profile memory is runtime state rather than durable project truth;
- asynchronous transfer is acceptable and preferred over live synchronization;
- most useful spillover is procedural, not factual.

## Learning classes

| Learning | Owner | Spillover |
|---|---|---|
| project fact | source repo/QMD | no automatic spillover |
| user/role preference | role memory | same profile only |
| role procedure | role-local learned skill initially | candidate for review |
| proven project-neutral procedure | reviewed shared skill | selected roles/repos |

## Chosen flow

```text
task experience
  -> local role learning
  -> deterministic candidate detection later
  -> semantic/reviewer gate only if candidate changed
  -> strip project facts/secrets
  -> deduplicate/merge
  -> promote accepted generic skill
```

## Risks

- automatic memory copying can transfer stale facts, confidential data and context-specific assumptions;
- indiscriminate skill promotion can create a large noisy catalog and token/selection overhead;
- reviewer may over-generalize a procedure that only worked in one domain;
- a promoted skill may become stale as upstream tools change.

## Shortcomings

- spillover is delayed, not instantaneous;
- semantic review of candidates costs model tokens when a candidate exists;
- some useful tacit knowledge may remain role-local if it cannot be safely generalized.

## Rejected alternatives

1. **Sync MEMORY.md between profiles/repos** — rejected: wrong ownership boundary and contamination risk.
2. **Automatically promote every learned skill** — rejected: noise, duplication, unsafe context leakage.
3. **One shared external memory now** — rejected/deferred under D09; adds another service/source before a measured need.

## Implementation consequence

Build a candidate-harvest process around changed learned-skill artifacts, not around copying raw memory. Promotion requires explicit evidence of reuse/generalizability and a review record.

## Watch / revisit conditions

Revisit if promotion overhead becomes material, useful knowledge is repeatedly lost between roles, or a proven external-memory provider offers needed shared-state semantics without becoming a second project-truth store.

## Evidence links

- Hermes memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
- Hermes profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Hermes skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Agent Skills specification: https://agentskills.io/specification
- Current promotion flow: `../06-SHARED-SKILL-PROMOTION-AND-CRON.md`
