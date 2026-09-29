---
okf_version: "0.2"
type: handover
title: OpenProject CLI and Agent Skill — Antigravity pilot handover
description: Research handover for another AI to produce and independently validate a bounded, upstream-first Antigravity implementation plan.
tags: [openproject, antigravity, cli, agent-skill, windows, handover]
status: research_handover_ready
verified: "2026-09-25"
stale_after: "2026-10-02"
parent_handover: ../openproject-windows-agent-integration-v2/HANDOVER.md
required_deliverable: IMPLEMENTATION-PLAN.md
working_draft: DRAFT-IMPLEMENTATION-PLAN.md
---

> **✅ EXECUTED DIRECTLY — this handover's mission was superseded (2026-09-28).** The operator executed
> `DRAFT-IMPLEMENTATION-PLAN.md` directly and **waived** the required `IMPLEMENTATION-PLAN.md`; the
> **upstream OpenProject CLI route was rejected** in favour of a portable custom API-v3 skill
> (`.agents/skills/openproject/`); and a **fresh 17.8 install** replaced the in-place upgrade. The pilot is
> proven (read+write, census WP #38). **→ See `../DECISION-2026-09-28-pilot-execution-reconciliation.md`**
> for the accepted path and the DRAFT Phase A–H disposition. Read this file as history, not instructions.

# Mission for the receiving AI

Research and write an implementation-ready plan for the smallest safe path from Antigravity to the private Leela OpenProject instance using the upstream OpenProject CLI and upstream Work Package Agent Skill.

Your deliverable is `IMPLEMENTATION-PLAN.md` beside this handover. Do not install the package, change the OpenProject runtime, create accounts, perform live API calls, mutate Work Packages, or alter the retained handler package while producing the plan. Planning must precede implementation.

`DRAFT-IMPLEMENTATION-PLAN.md` preserves useful earlier work. Treat it as a hypothesis set and structural starting point—not accepted instructions. Verify, correct, reorder, or reject its content using the research contract below, then produce the reviewed `IMPLEMENTATION-PLAN.md` as the deliberate output.

This is a planning handover, not a second architecture owner. The parent handover owns the program target; this handover defines the research and planning assignment.

# Accepted decisions

- Pilot agent: Antigravity.
- Preferred integration: pinned, compatible upstream OpenProject CLI plus upstream `openproject-workpackage-crud` skill.
- OpenProject MCP is not part of this Community-edition pilot.
- The existing 58-handler package is preserved unchanged as a fallback. Open it only for an operation the pilot actually requires and upstream cannot perform.
- Write autonomy remains undecided. After plan acceptance and separate implementation authorization, reads may proceed following target verification; no general write permission is inferred.
- After plan acceptance and separate implementation authorization, live mutations require an explicit test project, a dedicated Leela agent identity, verified target identity, and confirmation under the temporary policy.
- Optional development frameworks are never invoked automatically. An operator must select one for the current task.
- Do not modify OpenProject runtime, Compose, database, handler files, repository-wide agent rules, or PM state while researching and writing the plan.

# Why the first trial is deliberately small

The upstream components are promising but not yet a stable matched release pair:

- the latest released CLI is currently v0.5.5 and uses the older verb-first command surface;
- the current upstream Agent Skill requires the newer noun-first `op work-package ...` surface;
- the CLI main branch warns that v0.6 is rapidly developed, unsupported, and not yet secure or stable enough for general use;
- the skill warns that it performs real writes and the CLI has no dry-run.

Therefore installation success would not prove compatibility, and compatibility would not prove that writes are safe. Research the exact version relationship and make the future plan pin both upstream revisions, probe their contract before credentials are introduced, and stop on a mismatch.

# Environment evidence already available

- Repository: `C:\GitDev\Leela-Cloud-2026`.
- Windows host has `agy` 1.1.15 available.
- Node, npm, and npx are available.
- `op`, `openproject-cli`, and Go were not found during the 2026-09-25 read-only check.
- Antigravity configuration directories exist under the user's `.gemini` directory.
- The private OpenProject stack is external to this repository and uses Compose with an external PostgreSQL service; it is not an all-in-one container.
- A duplicate/community-instance risk exists, so endpoint identity must be explicit before any authenticated call.

Refresh only a fact needed by the next step. Do not repeat broad machine or Docker inventories without a concrete blocker.

# Upstream scope and limitations

The upstream Agent Skill covers Work Package inspection, direct-child listing, creation, selected field updates, attachments, and named workflow actions. It does not currently provide a complete PM integration:

- no parent assignment on create;
- no custom-field or field-schema reads/writes;
- no general status-by-name mutation;
- workflow action names are not discoverable in JSON;
- no dry-run;
- no project, notification, time, budget, broad search, or MCP workflows.

These are recorded capability gaps, not reasons to rewrite the local package before the pilot. A gap becomes implementation work only when an accepted pilot outcome requires it.

# Authority and safety boundaries

1. The private Leela OpenProject instance is the intended target.
2. Never infer the target from whichever endpoint happens to answer first.
3. Before authentication, record the expected scheme, host, port, and instance fingerprint using non-secret data.
4. Environment variables can override a CLI profile; inspect relevant variable names without printing values.
5. Never place a token in a command, document, shell history example, repository file, log, or captured evidence.
6. No mutation may run during this planning task. In later separately authorized implementation, it may run only after the accepted plan's write-phase entry gate passes.
7. During later separately authorized implementation, reread the Work Package after every permitted mutation and compare intended versus observed state.
8. A rejected workflow action, ambiguous identity, partial update, unexpected redirect, or command-contract mismatch is a stop condition.

# Required reading order

1. `../openproject-windows-agent-integration-v2/HANDOVER.md`
2. this file
3. `../openproject-cli-agent-handover/index.md`
4. `../openproject-cli-agent-handover/openproject-cli-agent-handover.md`
5. `DRAFT-IMPLEMENTATION-PLAN.md`
6. only the evidence files needed to answer the current planning question

Do not preload all 184 retained package files or all 58 handlers.

# Current external evidence

- OpenProject CLI README and warning: https://github.com/opf/openproject-cli/blob/main/README.md
- CLI releases: https://github.com/opf/openproject-cli/releases
- upstream Agent Skills README: https://github.com/opf/openproject-agent-skills
- upstream Work Package skill: https://github.com/opf/openproject-agent-skills/blob/main/openproject-workpackage-crud/SKILL.md
- Antigravity skill locations and discovery: https://antigravity.google/docs/skills
- OpenProject upgrade rules: https://www.openproject.org/docs/installation-and-operations/operation/upgrading/
- OpenProject API v3: https://www.openproject.org/docs/api/
- OpenProject MCP boundary: https://www.openproject.org/docs/system-admin-guide/integrations/mcp-server/

Re-check changing version facts at execution time. Prefer official documentation and upstream repositories; record the URL, observed revision/version, and date.

# Research assignment

## 1. Ground the local inputs

Read the parent handover and prior evidence handover first. Then inspect only the local facts needed to plan:

- exact Antigravity surface, version, supported skill locations, and fresh-session discovery behavior;
- availability and versions of Node, npm/npx, Go, `op`, and `openproject-cli`;
- private OpenProject topology, exact current version, target endpoint, duplicate-instance risk, database topology, and Compose/image pinning;
- existing skill-name collisions or repository policy that would affect project-scoped installation;
- only the smallest relevant portion of the 58-handler package needed to understand its role as fallback.

This inspection is read-only. Reuse still-valid evidence unless a changed input would materially alter the plan. Do not start stopped services or print credential values.

## 2. Research official primary sources

Use current official documentation and upstream repositories, not summaries, for every external assertion. At minimum verify:

1. the latest released OpenProject CLI version, current development version, Windows distribution/build options, authentication/profile behavior, environment-variable precedence, command syntax, JSON output, and security/support warnings;
2. the exact revision and limitations of `opf/openproject-agent-skills`, its required CLI command surface, installation behavior, write safeguards, and unsupported operations;
3. Antigravity's current project/global skill locations, invocation/discovery behavior, and differences between Antigravity 2.0, CLI, and IDE;
4. the `npx skills` installer's current agent identifiers, destination behavior, pinning support, copy/symlink behavior, and non-interactive options;
5. OpenProject API v3 behavior required for the pilot, checked against the exact target instance version rather than only the newest online API docs;
6. official OpenProject upgrade rules from the exact current version to the selected stable Community target, including supported major hops, PostgreSQL and worker requirements, Compose changes, backups, restore testing, per-hop validation, and rollback limits;
7. the current licensing and capability boundary of OpenProject's native MCP so the plan does not accidentally rely on an Enterprise feature;
8. Windows-versus-macOS/Unix differences only on the selected execution path.

For every web conclusion, record:

```yaml
web_evidence:
  claim:
  source_url:
  source_owner:
  observed_version_or_revision:
  checked_on:
  planning_consequence:
```

If official sources conflict, preserve the conflict and design a probe or operator decision. Do not silently select the more convenient claim.

## 3. Challenge the proposed route before planning it

The preferred route is upstream-first, but it is not pre-proven. Answer these questions with evidence:

- Is there a reproducible pinned CLI/skill pair whose command contracts match?
- If the skill requires unreleased CLI behavior, is a pinned development build reasonable on this Windows host, or should the plan wait/use another bounded route?
- Can the package be installed project-locally for the actual Antigravity surface and discovered in a fresh session?
- Can installation and command probing be completed without credentials or live OpenProject requests?
- Can the current OpenProject version support the first read proof, allowing upgrade work to remain a separate later change?
- Which required outcomes are supported upstream, which are gaps, and which are not required for the pilot?
- Does any demonstrated required gap justify opening one or more retained handlers? Do not invent work merely because 58 handlers exist.

The research may reject or revise the preferred route, but only with concrete evidence and the smallest viable alternative.

Compare every conclusion in `DRAFT-IMPLEMENTATION-PLAN.md` with the grounded local inputs and current primary sources. Preserve useful detail, but do not inherit an assertion merely because it appears in the draft.

## 4. Design every phase as an interface contract

For every future execution phase, validate the whole chain rather than listing commands:

```yaml
phase:
  objective:
  authority_to_act:
  inputs:
    artifact_or_state:
    producer:
    exact_format_or_version:
    freshness_requirement:
    validation_before_use:
  actions:
    command_or_operation:
    actor_and_environment:
    preconditions:
    expected_transformation:
    side_effects:
    safety_boundary:
  outputs:
    artifact_or_state:
    exact_format:
    acceptance_checks:
    evidence_to_retain:
  handoff:
    consumer:
    entry_condition_for_next_phase:
    proof_the_output_is_usable:
  failure_handling:
    stop_conditions:
    diagnosis_boundary:
    rollback:
    operator_decision_required:
```

Check especially that:

- the named input actually exists and can be passed to the action;
- the action accepts that exact input format/version;
- the transformation can produce the claimed output;
- the output is machine- or human-verifiable;
- the next phase can consume it without hidden chat context;
- failure cannot silently redirect work to the wrong OpenProject instance;
- rollback restores data, configuration, and matching runtime state rather than only an image;
- no secret becomes part of the evidence artifact.

## 5. Required plan phases

The implementation plan should use the fewest phases that preserve these gates. It must cover:

1. minimum local/target baseline;
2. offline acquisition and pinning of a compatible CLI/skill pair;
3. fresh-session Antigravity discovery and one authenticated read from the verified private instance;
4. OpenProject upgrade as an independent, recoverable change—not a prerequisite to the initial install/read proof unless research proves otherwise;
5. bounded administrator setup of a dedicated test project and least-privilege Leela agent identity;
6. individually authorized writes with reread verification;
7. a required-capability matrix for CRUD, hierarchy, relations, workflow/status, evidence/comments, Kanban, and Gantt;
8. gap-driven use of the retained handler package only where an accepted outcome is unsupported upstream;
9. one real Leela task plus fresh-session resume from OpenProject and qualified repository references;
10. an operator decision point for write autonomy and any cross-agent generalization.

Use explicit dependencies rather than pretending every phase is strictly linear. A conditional gap phase may be `not_needed`. Unresolved write autonomy blocks unattended production writes, not safe research or approved test-scope work.

## 6. Required plan precision

For commands or file changes, provide exact but non-secret examples. For each proposed patch include:

```yaml
patch:
  objective:
  exact_files:
  prerequisites:
  minimal_diff:
  command:
  expected_result:
  verification:
  failure_diagnosis:
  rollback:
  operator_gate:
```

Do not pre-author speculative patches for the handler package. Specify the decision rule and evidence that would justify one.

## 7. Independent plan validation

Before presenting the plan, assign an independent reviewer AI to inspect the actual draft against this handover and the cited primary sources. The reviewer must check:

- every input/action/transformation/output/handoff chain;
- version and command-contract compatibility;
- whether a step is necessary at its proposed point;
- hidden prerequisites, circular dependencies, and outputs without consumers;
- over-engineering, especially full handler catalogs or broad platform audits;
- unintended runtime changes during the planning task;
- preservation of open write-autonomy decisions and operator-explicit-only framework use.

Resolve each concrete issue or record an explicit disagreement with evidence. Include the reviewer verdict in the plan.

# Required deliverable

Create `IMPLEMENTATION-PLAN.md` beside this file. It must contain:

- verified local baseline relevant to planning;
- a dated source table using primary sources;
- assumptions and unresolved conflicts;
- necessity ranking for every major phase (`required now`, `required later`, `conditional`, or `unnecessary`);
- selected architecture and rejected alternatives with evidence;
- phase dependency map;
- complete interface contract for every phase;
- required-capability matrix;
- exact stop conditions, rollback boundaries, operator gates, and evidence artifacts;
- expected repository/runtime blast radius by phase;
- independent-review findings and disposition;
- a draft-disposition table showing what was retained, corrected, removed, or still unresolved;
- a concise first executor action that cannot be mistaken for permission to continue into later phases.

# Completion boundary

This handover is complete when another AI has produced and independently validated the research-backed `IMPLEMENTATION-PLAN.md`. No installation or OpenProject implementation is part of this handover's execution.

# Immediate next action

Give this file and its parent handover to the receiving AI. Instruct it to perform the read-only local grounding and primary-source web research, then author and independently validate `IMPLEMENTATION-PLAN.md`. Stop for operator review after the plan; do not begin implementation.
