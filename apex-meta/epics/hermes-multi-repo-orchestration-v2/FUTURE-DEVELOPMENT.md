# Future Development — Hermes Multi-Repo Orchestration v2

Status: **DEFERRED / NOT REQUIRED FOR FIRST MULTI-REPO BASELINE**  
Date: 2026-08-24

## External shared memory service

Trigger for reevaluation:

- role-local Hermes memory + reviewed shared skill promotion is measurably insufficient;
- multiple independent profiles must recall the same evolving non-project state automatically;
- manual/shared-skill promotion creates material operator burden;
- cross-profile memory inconsistency becomes a demonstrated failure mode.

Current Hermes supports external memory-provider plugins and recommends an external provider when profiles genuinely need shared memory. Candidate providers documented by Hermes include Honcho, OpenViking, Mem0, Hindsight, Holographic, RetainDB, ByteRover and Supermemory.

Do not add one yet.

A future research run must compare:

- privacy/data egress;
- local vs hosted operation;
- retrieval quality;
- cross-agent identity model;
- memory write conflict behavior;
- token/API cost;
- failure/recovery;
- portability across Hermes/Codex/Claude;
- whether the provider becomes an unnecessary second source of project truth.

Project facts must remain in project repositories even if external shared memory is later adopted.

## Automatic repo -> Apex portfolio synchronization

Desired capability:

```text
managed repo events
 -> concise current state
 -> Apex portfolio view
```

Do not implement until the single-board/tenant Kanban experiment proves whether Hermes already provides enough portfolio visibility.

If a gap remains, prefer an existing native/export/reporting mechanism before any custom synchronizer.

## Automatic learned-skill promotion

Desired capability:

```text
profile learns reusable procedure
 -> evaluator verifies multi-repo generality
 -> sanitized version committed to Apex shared skill source
 -> distributed to applicable agents
```

Do not automate promotion initially. First prove a manual reviewed promotion loop across at least two repositories.

## Global/shared BMAD installation

BMAD supports Hermes as an installation platform, but current upstream installation remains project-oriented. A proposal exists for a global installation linked into projects; treat that as future/unproven until shipped and verified.

Initial multi-repo implementation should not depend on a custom global BMAD linker.

## External/shared skill package distribution

Potential later improvement:

- make approved Apex shared skills an installable/versioned skill package;
- use one documented upstream install mechanism across Hermes, Codex and Claude where compatibility is proven;
- pin versions and provide rollback.

Do not create a bespoke package manager.

## Portfolio dashboard

Potential human-facing dashboard over:

- repo/tenant status;
- cross-project dependencies;
- blockers;
- reviews;
- recent accepted outputs;
- operational model/cost telemetry.

First determine whether Hermes Kanban dashboard plus Apex repository summaries already meet the requirement.

## Sensitive customer-data routing

When a real customer/confidential workflow exists, decide explicitly:

- provider allowed for that data class;
- retention/training requirements;
- local-model fallback;
- redaction rules;
- whether remote model egress is forbidden.

This is independent of QMD: QMD retrieval is local; the privacy event occurs when selected context is sent to a remote model.

## Optional stack candidates retained from prior research

- OpenClaw
- Agency Agents
- AnythingLLM
- Semantic Router
- CrewAI
- Superpowers

Reopen only against a measured failure of the implemented Hermes multi-repo baseline.
