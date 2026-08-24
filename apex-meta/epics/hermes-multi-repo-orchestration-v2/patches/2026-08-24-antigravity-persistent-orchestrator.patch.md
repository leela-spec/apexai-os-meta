# Exact-Match Patch — Antigravity Persistent Orchestrator

Status: **READY FOR DETERMINISTIC APPLICATION**  
Date: 2026-08-24

Purpose: keep one thin Antigravity coordinator conversation across the implementation run while delegating bounded, context-heavy work to fresh subagents. This changes execution mechanics only; D01-D10, phase goals, gates, and implementation scope are unchanged.

Evidence basis:

- Google Antigravity CLI Best Practices: explore -> plan -> execute; verification loops; fan out large sweeps with parallel subagents.
- Google Antigravity Subagents docs: subagents start with clean context, preserve the parent context, and support asynchronous delegation.
- Anthropic context-engineering guidance: keep the lead agent on the high-level plan, move detailed exploration into fresh subagents, and persist structured notes outside the context window.

Application law:

1. Re-read the live target before applying.
2. Baseline blob SHA below must still match, or rebuild this patch from the new live bytes.
3. `<old>` must match exactly once.
4. Apply only the exact replacement.
5. Re-read and diff the changed range.
6. Do not fall back to whole-file replacement.

Baseline blob SHA: `7330fa95e51279f5629ade8a198840e93dd129f9`

<file>
apex-meta/epics/hermes-multi-repo-orchestration-v2/15-IMPLEMENTATION-ROADMAP-v2-ANTIGRAVITY.md
</file>

<old>
## 5. Context-management protocol

One major phase = one Antigravity execution context.

At the first authorized implementation mutation, create:

```text
apex-meta/epics/hermes-multi-repo-orchestration-v2/implementation/
  implementation-state.yaml
  evidence/
```

Minimum state:

```yaml
schema_version: 1
program: hermes_multi_repo_orchestration_v2
executor: antigravity
branch: main
current_phase:
last_completed_phase:
phase_status:
last_verified_commit:
last_verified_repo:
last_verified_workdir:
installed_versions: {}
corrections: {}
blockers: []
next_phase:
next_exact_action:
```

For every phase create exactly one compact evidence file:

`implementation/evidence/PXX-<slug>.md`

It contains only:

- input state;
- official/current sources consulted;
- commands/config actually used;
- exact files/paths changed;
- relevant PASS/FAIL evidence;
- rollback/recovery information;
- unresolved blocker if any;
- final phase verdict.

Do not paste giant terminal logs into context. Save large logs separately only when necessary and cite the exact relevant excerpt/path.

At phase end:

1. update implementation state;
2. write evidence;
3. verify Git diff is phase-scoped;
4. summarize in <=15 lines;
5. end the context.

Next context loads only:

- this v2 plan;
- implementation state;
- previous phase summary/evidence;
- authority files required by the next phase.

## 6. Main-agent / subagent policy

Main Antigravity agent:

- owns phase state;
- performs mutations;
- performs final phase verification;
- writes the checkpoint/evidence.

Optional subagents:

- maximum two per phase;
- read-only research or independent verification only;
- never concurrently edit/install/configure;
- never make architecture decisions;
- never hold independent authoritative state.

Preferred when useful:

1. one current-source researcher;
2. one independent verifier.

If subagents are unreliable, continue sequentially in the main agent. Do not debug the subagent framework inside this program.
</old>

<new>
## 5. Context-management protocol

Keep one **primary Antigravity conversation as the thin program coordinator** across the implementation run while it remains healthy. Do not restart the primary conversation merely because a phase ended.

The coordinator owns only:

- the current roadmap position;
- `implementation-state.yaml`;
- active blockers and operator gates;
- delegation of the next bounded task;
- acceptance of returned evidence;
- the decision to advance, retry once with evidence, or block.

Do not make the coordinator ingest deep research, large logs, repository-wide dumps, or full subagent transcripts. Detailed work belongs in fresh bounded subagent contexts or targeted tool calls and returns as concise evidence plus file/path references.

At the first authorized implementation mutation, create:

```text
apex-meta/epics/hermes-multi-repo-orchestration-v2/implementation/
  implementation-state.yaml
  evidence/
```

Minimum state:

```yaml
schema_version: 1
program: hermes_multi_repo_orchestration_v2
executor: antigravity
branch: main
current_phase:
last_completed_phase:
phase_status:
last_verified_commit:
last_verified_repo:
last_verified_workdir:
installed_versions: {}
corrections: {}
blockers: []
next_phase:
next_exact_action:
```

For every phase create exactly one compact evidence file:

`implementation/evidence/PXX-<slug>.md`

It contains only:

- input state;
- official/current sources consulted;
- commands/config actually used;
- exact files/paths changed;
- relevant PASS/FAIL evidence;
- rollback/recovery information;
- unresolved blocker if any;
- final phase verdict.

Do not paste giant terminal logs into the coordinator context. Save large logs separately only when necessary and cite the exact relevant excerpt/path.

At phase end:

1. update implementation state;
2. write evidence;
3. verify Git diff is phase-scoped;
4. return a concise result to the coordinator;
5. let the coordinator advance to the next phase without reloading completed phase detail.

For each new phase, load only:

- this v2 plan;
- current implementation state;
- the authority/source files actually required by that phase.

Use Antigravity's `/context` view to notice context pressure. If the primary conversation becomes materially degraded, repetitive, or confused, persist state first and resume from the durable state in a fresh coordinator conversation. A context reset is recovery, not the normal phase boundary.

## 6. Main-agent / subagent policy

The primary Antigravity agent is the **coordinator**. It keeps the high-level plan and durable state, delegates bounded work, reviews returned evidence, and decides whether a phase passes.

Use fresh subagents when they reduce coordinator context or provide valuable independent verification. Do not spawn them by default for trivial deterministic steps.

A delegated task must be narrow enough to state in a short contract containing:

- goal;
- allowed workspace/files;
- required source(s);
- whether mutation is allowed;
- acceptance check;
- expected concise return.

Subagent rules:

- each starts from the minimum task-specific context, not the parent transcript;
- return conclusions, evidence paths, changed paths, tests, and blockers rather than a narrative transcript;
- read-only research/verification tasks may run in parallel when independent;
- writable tasks against the canonical checkout run one at a time and must not overlap on shared files or runtime state;
- a writable subagent may execute a bounded phase task, but the coordinator remains the authority for phase acceptance and state advancement;
- subagents do not redesign architecture or create independent authoritative state;
- do not create a permanent custom-agent hierarchy merely for this implementation run.

At P00, probe the installed Antigravity version's current subagent behavior before depending on it. If subagents are unavailable or unreliable, execute the same bounded task sequentially in the primary agent; do not stop the Hermes implementation to debug Antigravity orchestration internals.
</new>
