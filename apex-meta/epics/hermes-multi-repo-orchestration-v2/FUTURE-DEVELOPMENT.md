# Future Development — Hermes Multi-Repo Orchestration v2

Status: **DEFERRED / NOT REQUIRED FOR FIRST SAFE MULTI-REPO BASELINE**  
Date: 2026-08-24

Current v2 intentionally stops before adding layers that are not proven necessary.

## External shared memory service

Trigger for reevaluation:

- role-local Hermes memory + reviewed shared-skill promotion is measurably insufficient;
- multiple independent profiles must recall the same evolving non-project state automatically;
- reviewed skill promotion creates material operator burden;
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

## Bidirectional repo <-> Apex task synchronization

Current v2 includes a **read-only asynchronous source-board -> Apex portfolio rollup**.

Future-only capability:

```text
Apex decision/task mutation
  -> automatically changes one or more source repo boards
  -> conflict resolution / acknowledgement
```

Do not implement yet.

Why deferred:

- separate Hermes boards deliberately have no native cross-board dependency graph;
- source boards are the project task authority;
- bidirectional replication introduces conflict, ordering and source-of-truth problems;
- current user requirement does not need real-time synchronization.

Reopen only if explicit source-task updates from Apex become a measured repetitive burden.

## Fully automatic learned-skill promotion

Current v2 target:

```text
role learns reusable procedure
 -> deterministic changed-candidate harvest
 -> independent semantic/human-reviewable evaluation
 -> accepted sanitized skill committed to Apex
 -> controlled deployment
```

Future-only:

```text
candidate
 -> fully automatic acceptance
 -> autonomous write to canonical shared skill source
 -> autonomous deployment everywhere
```

Do not enable until the reviewed promotion loop has demonstrated low false-promotion and no project-fact/secret contamination across multiple repositories.

## Global/shared BMAD installation

BMAD current official installer is project-oriented. Open issue #1728 proposes a global installation with project links, which confirms this is not a capability v2 should assume today.

Current baseline:

```text
BMAD installed separately only in repos that actually need BMAD.
```

Reopen global deduplication only after upstream ships a supported mechanism and it is live-tested.

## External/shared skill package distribution optimization

Current v2 will first test the simplest safe delivery for reviewed Apex skills:

- deployed protected external skill directory; and/or
- Hermes Skills Tap; and/or
- profile distribution for role-owned skills/config.

Future improvement:

- one versioned package/release process across Hermes, Claude and Codex where their current skill mechanisms actually overlap;
- dependency pinning;
- rollback;
- compatibility matrix.

Do not create a bespoke package manager.

## Fully autonomous multi-board Hermes dispatch

Current v2 safe mode keeps all repo boards persisted but does not automatically dispatch all of them concurrently.

Reopen only after current upstream/runtime risks are proven resolved:

- tenant/memory isolation assumptions are not needed;
- machine-wide/per-profile concurrency across boards is safe;
- Kanban Docker task workspace is host-backed;
- task workspace cannot be overridden by profile cwd;
- host/container cwd provenance agrees across terminal/file/code execution;
- worker swarm/recovery behavior passes live stress test.

The safe sequential mode is an acceptable production endpoint if simultaneous repo execution has no demonstrated value.

## Broad multi-repo Hermes Project

Hermes Projects can group multiple folders/repos, but v2 starts with one project object per repo.

A future orchestrator-only `portfolio` project may span all managed repos if it materially improves navigation or portfolio analysis.

Do not give routine workers broad multi-repo project scope merely for convenience.

## Portfolio dashboard beyond existing Hermes/Apex surfaces

Potential later UI over:

- repo/board status;
- cross-project dependency objects;
- blockers;
- reviews;
- recent accepted outputs;
- QMD freshness;
- learning-promotion queue;
- model/cost telemetry.

First use:

```text
Hermes per-board dashboard
+ deterministic Apex portfolio snapshot
+ Apex daily/weekly review artifacts
```

Only build/add another UI if those are insufficient.

## QMD HTTP warm daemon

Hermes' official QMD integration documents an HTTP daemon option that keeps local models warm for frequent querying at the cost of persistent RAM (~2 GB class in current docs).

Current baseline can remain stdio unless measured QMD cold-start latency becomes an actual productivity problem.

Reopen daemon mode based on observed query frequency/latency and available memory.

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
