# D09 Appendix — External Shared Memory Deferred

**Decision status:** DEFERRED / ACCEPTED  
**Decision ledger:** `../DECISIONS.md`  
**Primary subject file:** `../FUTURE-DEVELOPMENT.md`

## Decision

Do not add an external shared-memory provider in the initial multi-repo baseline. Reconsider only after the combination of role-local Hermes memory, project truth in Git, QMD retrieval and reviewed shared-skill promotion demonstrates a measured insufficiency.

## Forces

- cross-profile shared memory is desirable only if real workflows require it;
- Hermes already provides local profile memory and supports external memory providers when genuine shared-state needs exist;
- adding another memory system introduces another data store, service, privacy boundary and failure mode;
- project facts must not migrate into an opaque shared memory system and compete with Git truth.

## Current sufficiency model

```text
project facts -> source repo
project retrieval -> QMD
role preferences/experience -> profile memory
reusable procedures -> reviewed shared skills
portfolio decisions -> Apex
```

Use this before adding another layer.

## Risks if added too early

- duplicate/conflicting project truth;
- unexpected cloud egress/retention depending on provider;
- cross-agent contamination;
- write conflicts and unclear provenance;
- vendor lock-in and operational dependency;
- additional model/API cost.

## Shortcomings of deferral

- one role's raw memory is not automatically visible to another role;
- some useful non-procedural context may require explicit repo/Apex artifacts instead of instant shared recall;
- manual reviewed promotion remains necessary for cross-role procedural spillover.

## Rejected alternatives

1. **Immediate external memory deployment** — rejected: no measured gap.
2. **Share the same Hermes profile home between agents** — rejected: profile state is intentionally isolated and concurrent sharing is unsafe.
3. **Use Apex Git as a raw memory dump** — rejected: Apex stores durable reviewed portfolio truth/procedures, not private runtime memory streams.

## Reopen triggers

Reopen research only if one or more occur:

- multiple independent roles repeatedly need the same evolving non-project state;
- useful context is repeatedly lost despite QMD/Apex/shared skills;
- reviewed promotion creates material operator burden;
- cross-profile inconsistency becomes a demonstrated failure mode.

## Required future comparison

Any future provider must be evaluated for privacy/egress, local-vs-hosted operation, write-conflict semantics, auditability, token/API cost, portability, recovery and whether it creates a second source of project truth.

## Evidence links

- Hermes memory providers: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers/
- Hermes profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Future backlog: `../FUTURE-DEVELOPMENT.md`
