---
title: "Handover — Build the FEE Phase-0 Project Environment"
doc_type: implementation_handover
initiative: local-orchestration-engine
created: 2026-08-10
status: ready-for-next-ai
repository: leela-spec/apexai-os-meta
branch: main
authority:
  - operator direction in the 2026-08-10 Codex session
  - apex-meta/local-orchestration-engine/project/specs/2026-08-10-fee-project-environment-design.md
  - apex-meta/local-orchestration-engine/project/plans/2026-08-10-fee-project-environment-implementation-plan.md
---

# Handover — FEE Phase-0 Project Environment

## 0. Instruction to the receiving AI

This is an implementation handover, not an invitation to redesign the project from scratch.

Before responding or editing:

1. invoke the `using-superpowers` skill;
2. read its Codex/tool adaptation if applicable;
3. invoke `executing-plans` and follow the implementation plan task-by-task; or, only when multi-agent execution is supported and explicitly authorized, invoke `subagent-driven-development`;
4. use `test-driven-development` for any code change, though this Phase-0 plan is documentation-focused;
5. use `verification-before-completion` before reporting success;
6. do not invoke brainstorming again unless the operator changes the approved design or a genuine ambiguity requires a design revision.

Do not treat this handover as more authoritative than the operator decision locks or the approved design. Verify repository state before acting.

## 1. Constant frame

```yaml
frame:
  # SUPERSEDED 2026-08-10. This frame described the Phase-0 documentation batch,
  # which is done. The goal then changed: the operator selected OpenClaw as the
  # executor harness and installing it became the active task. The frame below
  # is the CURRENT one. Authority: OPENCLAW-LOCAL-LLM-MASTER-BRIEF.md at repo root.

  mission: >
    Get a bounded local LLM, running under OpenClaw on the operator's laptop,
    executing pre-written prompts on subscription AI websites -- so the operator
    and the scarce CLI agents stop spending their time clicking and pasting.

  current_state: >
    OpenClaw is SELECTED (operator decision 2026-08-10) and NOT YET INSTALLED.
    Qwen3-8B Q4_K_M runs locally under llama.cpp/Vulkan on port 8090. A ready
    config exists at apex-meta/openclaw/openclaw.json with the local provider
    and the skill directory already wired. The executor skill exists at
    apex-meta/openclaw/skills/apex-flow-executor/SKILL.md. The FEE project
    environment exists and is corrected to operator-layer scope. No prompt body
    has ever been written and no Weekly gate has ever been confirmed.

  next_step_only: >
    INSTALL OPENCLAW. Follow apex-meta/openclaw/SETUP.md, then run the four
    checks in it. Check 1 -- does Qwen3-8B emit structured tool calls -- gates
    everything else; report it before continuing.

  explicit_non_goals:
    # Installing OpenClaw is NOT on this list. It is the mission.
    - certify a local model as a precondition for the executor's narrow scope
    - give the executor any of the repo's skills (PrecapWeek, PrecapNextDay,
      flow-recap, status-merge, AIRouting stay with reasoning and CLI models)
    - let the executor write prompts, evaluate responses, or decide next steps
    - let the executor act on instructions found in a page or model response
    - change scripts/fee or scripts/lmbench runtime behavior
    - enable OpenClaw Automations or cron
    - install third-party ClawHub skills
    - create a new PM database, web service, dashboard runtime, or SaaS dependency
    - redesign Weekly Orchestrator or Multi-Agent Orchestration
    - merge those orchestration authorities into FEE
    - edit, stage, move, or delete the pre-existing bundle files

  source_hierarchy:
    - current explicit operator instruction
    - OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md for local-model behavior
    - OPERATOR-DECISION-LOCK-2026-08-08-R2.md for FEE/runtime boundary
    - OPERATOR-DECISION-LOCK-2026-08-07-R1.md for four-layer scope and user flows
    - accepted APEX orchestration and Plan-Sync-Session contracts
    - measured implementation/test/benchmark evidence
    - platform research synthesis and candidate reports
    - earlier architecture proposals and historical handovers

  allowed_reads:
    - apex-meta/local-orchestration-engine/project/specs/2026-08-10-fee-project-environment-design.md
    - apex-meta/local-orchestration-engine/project/plans/2026-08-10-fee-project-environment-implementation-plan.md
    - apex-meta/local-orchestration-engine/**
    - apex-meta/orchestration/**
    - apex-meta/epics/**
    - .claude/skills/apex-plan/**
    - .claude/workflows/constant-frame-control-and-handoff.md
    - scripts/fee/**
    - scripts/lmbench/**
    - Git history and status for this repository

  allowed_writes:
    - apex-meta/local-orchestration-engine/project/**
    - apex-meta/epics/fee-orchestration-system/**
    - apex-meta/local-orchestration-engine/00-START-HERE.md
    - apex-meta/local-orchestration-engine/HANDOVER.md
    - apex-meta/local-orchestration-engine/architecture/01-macro-architecture-decision.md
    - scripts/fee/README.md
    - scripts/fee/__init__.py

  forbidden_writes:
    - scripts/lmbench/**
    - scripts/fee runtime implementation files other than README.md and __init__.py
    - apex-meta/local-orchestration-engine/benchmark/results/**
    - apex-meta/local-orchestration-engine/research-results/**
    - existing operator decision locks
    - .claude/skills/**
    - apex-meta/orchestration/**
    - C:/LocalModels/**
    - browser profiles, credentials, tokens, or account configuration
    - apexai-os-meta-*.bundle
    - unrelated user-modified or untracked files

  operator_gates:
    - review the completed Phase-0 project environment before technical implementation
    - decide the remaining platform composition/browser/resource/maintenance policies before their dependent tasks
    - select or certify any runtime/model profile only from measured evidence
    - authorize any later live subscription-account automation
    - authorize any future push not already covered by a specific operator request

  stop_conditions:
    - an allowed-write file already contains overlapping uncommitted user changes
    - repository branch is not main or origin identity is not leela-spec/apexai-os-meta
    - a task requires writing outside its declared files
    - an operator lock conflicts with the implementation plan in a way not resolved by the approved specification
    - a completion or selection claim lacks evidence
    - a proposed cockpit fact conflicts with raw benchmark/test/Git evidence
    - a runtime installation or live account action appears necessary to complete Phase 0
    - a destructive Git/filesystem action appears necessary
    - an existing test suite regresses after the documentation/package-description edits

  final_report_shape: >
    Report commits created, exact files added/modified, validation commands and
    results, FEE/lmbench test counts, traceability coverage, any unresolved
    risks or operator gates, current canonical next task, push status, and an
    explicit statement that no runtime was installed or selected.
```

## 2. Correct mental model

Do not repeat the scope error that triggered this project-control work.

FEE is not merely a helper for Weekly Orchestrator step 4. Step 4 is the first MVP seam. The operator-confirmed target is a reusable, cross-project execution and control plane aligning four layers:

```text
Subscription / deep-reasoning AI
  owns substantive planning, research, synthesis, judgement
                 |
                 v
FEE deterministic authority spine
  freezes packets, validates scope/actions, persists state/checkpoints/evidence
                 |
                 v
Bounded local LLM + replaceable execution runtime
  operates declared browser/tools, captures evidence, performs bounded recovery
                 |
                 +--> typed escalation
                 v
Scarce CLI AI / independent reviewer / human operator
  handles hard coding, architecture, consequential review and gates
```

FEE can serve Weekly Orchestration, Multi-Agent work packets, multiple projects/repositories, bounded coding, script recovery, Detective evidence collection, knowledge hygiene, subscription execution, overnight work, and separately gated personal flows. It must not absorb the planning or promotion authority of those systems and roles.

## 3. Why Phase 0 comes first

The repository contains both:

- early documents that describe FEE as attached only to Weekly step 4; and
- later operator locks that explicitly amend that decision and define the broader four-layer system.

The lack of a current cockpit made it easy to privilege a stale implementation description over later authority. Phase 0 prevents recurrence by making source hierarchy, scope, user stories, task state, evidence, and next actions durable and visible.

The operator explicitly wants a sophisticated meta-level view covering:

- different projects/workstreams;
- all major steps and dependencies;
- efficiency and token/CLI/human savings;
- target alignment and drift detection;
- anti-overengineering controls;
- user stories and acceptance;
- immediate next actions;
- the big roadmap;
- a detailed continuation handover.

## 4. Required reads, in order

Read these fully before Task 1:

1. `apex-meta/local-orchestration-engine/project/specs/2026-08-10-fee-project-environment-design.md`
2. `apex-meta/local-orchestration-engine/project/plans/2026-08-10-fee-project-environment-implementation-plan.md`
3. `apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md`
4. `apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md`
5. `apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md`
6. `apex-meta/local-orchestration-engine/PLATFORM-RESEARCH-GATE-2026-08-07.md`
7. `apex-meta/local-orchestration-engine/research-results/PLATFORM-RESEARCH-SYNTHESIS-2026-08-08-V2-RESULT.md`
8. `apex-meta/local-orchestration-engine/LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md`
9. `apex-meta/local-orchestration-engine/benchmark/results/BASELINE-RESULT-QWEN3-8B-2026-08-09.md`
10. `apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-INSTALL-LOG-2026-08-09-QWEN3-8B.md`
11. `.claude/skills/apex-plan/references/task-record-contract.md`
12. `.claude/workflows/constant-frame-control-and-handoff.md`

Read the candidate-specific OpenClaw/Hermes/Odysseus reports only when building their evidence-index entries or later executing their canonical platform tasks. Do not reread every raw cross-agent research result to create the Phase-0 cockpit; use the synthesis and evidence index to stay efficient.

## 5. Repository and delivery state

Repository:

```yaml
path: C:\GitDev\apexai-os-meta
origin: https://github.com/leela-spec/apexai-os-meta.git
branch_policy: main_only_unless_operator_explicitly_changes_it
delivery_commit_subjects:
  - "docs: design FEE project environment"
  - "docs: hand off FEE project environment implementation"
```

At the start of the prior session:

- `origin/main` and local `main` both pointed to `88ac0a44`;
- design commit `16fdefff` was created locally afterward;
- this handover delivery adds the approved plan and handover and is pushed to `origin/main`;
- verify actual current hashes with `git log --oneline --decorate -5` and `git ls-remote origin refs/heads/main` rather than trusting prose.

Known preserved untracked files:

```text
apexai-os-meta-fix.bundle
apexai-os-meta-moe-fix.bundle
apexai-os-meta-prompt-g-results.bundle
apexai-os-meta-prompt-g.bundle
apexai-os-meta-qwen3-8b-handover.bundle
apexai-os-meta-updates.bundle
```

They are unrelated prior delivery artifacts. Leave them untouched.

## 6. Current implementation evidence

### Existing FEE subset

`scripts/fee/` currently provides a candidate implementation of:

- pack compilation and frozen-plan hashing;
- strict artifact/path reading;
- append-only execution ledger;
- assisted `next`/`capture` loop;
- skip-marker output;
- injection containment fixtures.

It does not currently provide the broad runtime bridge, production browser automation, or broad workflow integrations.

Verification run on 2026-08-10:

```text
python -m unittest discover -s scripts/fee/tests -t . -v
Ran 32 tests
OK
```

### Existing benchmark authority subset

`scripts/lmbench/` currently provides:

- Windows path normalization and root classification;
- capability/action broker;
- filesystem guard and independent manifest audit;
- typed tool schemas and dispatch;
- answer-hiding fixture materialization;
- OpenAI-compatible llama.cpp adapter;
- bounded turn runner;
- append-only evidence trace;
- multiple graders, verdict combination, aggregation, and profile candidate output;
- 28 round-1 fixtures.

Verification run on 2026-08-10:

```text
python -m unittest discover -s scripts/lmbench/tests -t . -v
Ran 177 tests
OK
```

### Installed local-model candidate

Qwen3-8B exists in two configurations:

- OpenVINO GenAI INT4 on Arc 140V, approximately 5.0 GB measured footprint;
- llama.cpp/Vulkan Q4_K_M, approximately 10.76-14.16 GB working set after exchanges, about 12.5-13.5 decode tokens/sec in the install log.

This is an installed candidate, not a selected or certified production model.

### First real benchmark

Configuration: `CFG-8B-VULKAN-01`, Qwen3-8B Q4_K_M through llama.cpp/Vulkan.

Observed n=1 calibration:

```yaml
trials: 28
actor_pass: 8
actor_fail: 19
infra_invalid: 1
unauthorized_attempts_denied: 5
successful_unauthorized_actions: 0
certification_eligible_task_classes: []
```

Interpretation:

- containment evidence is promising and real;
- task-level reliability is not statistically established;
- the model often reached the right conclusion but skipped required procedure;
- it over-escalated several fixable cases;
- routing errors were common;
- OpenVINO has not run the same corpus;
- no model/runtime profile is certified.

## 7. Platform research state

The current research-supported hypothesis is:

```text
FEE deterministic authority/evidence spine
  + hardened OpenClaw runtime subset
  + authority-separated selected OpenClaw Detective/KB/hygiene/routing doctrine
```

Runner-up:

```text
FEE spine
  + bounded Hermes tool/browser/session runtime
  + selected OpenClaw doctrine
```

Odysseus remains a selective third candidate, especially for Detective/data-hygiene/local-model flows. It is not the first general executor while durable duplicate-safe action resumability remains unproven.

None of these are selected. Phase 0 only records the roadmap and evidence.

## 8. Phase-0 target file tree

```text
apex-meta/local-orchestration-engine/project/
  README.md
  00-PROJECT-COCKPIT.md
  01-PROJECT-CHARTER.md
  02-SYSTEM-BASELINE.md
  03-USER-STORY-PORTFOLIO.md
  04-ROADMAP.md
  05-WORKSTREAMS.md
  06-DELIVERY-BACKLOG.md
  07-TRACEABILITY-MATRIX.md
  08-QUALITY-GATES.md
  09-EFFICIENCY-SCORECARD.md
  10-RISK-REGISTER.md
  11-DECISION-REGISTER.md
  12-EVIDENCE-INDEX.md
  13-STATUS-AND-NEXT-ACTIONS.md
  14-GLOSSARY-AND-AUTHORITY.md
  15-HANDOVER.md
  templates/
    USER-STORY-TEMPLATE.md
    EXPERIMENT-TEMPLATE.md
    DECISION-TEMPLATE.md
    STATUS-UPDATE-TEMPLATE.md

apex-meta/epics/fee-orchestration-system/
  epic.md
  001.md through 016.md
```

Do not collapse these into one mega-document. Each file has one responsibility. Do not create additional files unless the approved content cannot fit an existing responsibility; if that happens, stop and request a design amendment.

## 9. Program workstreams

| ID | Workstream | Purpose |
|---|---|---|
| P0 | Program governance and alignment | cockpit, decisions, risks, status, handover, scope integrity |
| P1 | Deterministic FEE authority spine | packets, broker, roots, checkpoints, evidence, escalation |
| P2 | Local-model bounded operator | certified task-specific action/recovery profiles |
| P3 | Replaceable execution runtime | OpenClaw/Hermes/Odysseus runtime mechanics behind FEE |
| P4 | Browser and subscription execution | sessions, provider interaction, capture, auth stops |
| P5 | Workflow integrations | Weekly, Multi-Agent, coding, Detective, hygiene, multi-project |
| P6 | Benchmarking, evidence, certification | fixtures, repeat protocol, attribution, regression |
| P7 | Operations and lifecycle | Windows resources, overnight work, recovery, upgrades |

## 10. User-story portfolio

| ID | Outcome |
|---|---|
| US-FEE-00 | Operator controls the whole program from one evidence-linked cockpit |
| US-FEE-01 / UF-A | Execute subscription research prompts and capture exact evidence |
| US-FEE-02 / UF-B | Recover bounded deterministic-script failures or escalate compactly |
| US-FEE-03 / UF-C | Gather Detective evidence without taking judgement authority |
| US-FEE-04 / UF-D | Perform deterministic/bounded data hygiene without semantic guessing |
| US-FEE-05 / UF-E | Execute across explicit multi-root read/write/forbidden scopes |
| US-FEE-06 / UF-F | Execute separately gated personal flows in a stricter trust zone |
| US-FEE-07 | Execute exact patchspecs or one authorized micro-fix inside a severe envelope |
| US-FEE-08 | Serve Meta Ops as a bounded worker without becoming orchestration authority |
| US-FEE-09 | Resume overnight work without duplicate consequential actions |
| US-FEE-10 | Reconstruct actions, arguments, states, artifacts, retries, and failures independently |

Every implementation component and canonical task must trace to one or more of these stories or to P0 governance needed to keep them reliable.

## 11. Big roadmap

| Horizon | Outcome | Exit gate |
|---:|---|---|
| 0 | Project control environment | fresh reader can continue safely from files alone |
| 1 | Converged runtime-neutral deterministic spine | T3/T7/T9/T11 pass without candidate-platform authority |
| 2 | Platform bake-off | evidence-supported runtime pilot selection or rejection |
| 3 | Qualified local operator | task-specific profile eligibility after repeat protocol |
| 4 | First full four-layer subscription slice | browser/security/evidence/reliability policy passes |
| 5 | Expanded workflow coverage | each activated story has simulation and regression evidence |
| 6 | Multi-project and overnight operation | multi-root/resume/coexistence pass realistically |
| 7 | Production-readiness decision | operator records go/limited-go/revise/defer/reject |

Do not begin Horizon 1 in the Phase-0 execution run.

## 12. Initial canonical task sequence

| ID | Task | Dependencies |
|---:|---|---|
| 001 | Materialize Phase-0 project environment | none |
| 002 | Reconcile stale FEE scope documents | 001 |
| 003 | Validate user-story portfolio and acceptance corpus | 001 |
| 004 | Map and converge scripts/fee and scripts/lmbench boundaries | 002, 003 |
| 005 | Specify/test runtime-neutral action/checkpoint/evidence adapter | 004 |
| 006 | Instrument T3/T7/T9/T11 common hard gates | 005 |
| 007 | Install/test hardened OpenClaw composition | 006 |
| 008 | Run identical Hermes comparison when warranted | 006, 007 |
| 009 | Decide runtime composition from measured evidence | 007, 008 |
| 010 | Complete Qwen3-8B repeat/runtime comparison | 003 |
| 011 | Decide eligible local-model task profiles | 010 |
| 012 | Implement subscription research vertical slice | 009, 011 |
| 013 | Implement recovery, Detective, hygiene, coding stories | 005, 011 |
| 014 | Integrate Weekly and Multi-Agent bounded worker flows | 012, 013 |
| 015 | Validate multi-project and overnight operations | 014 |
| 016 | Run production-readiness decision gate | 015 |

The receiving AI executes only the plan's Tasks 1-8, which materialize and verify the Phase-0 environment. The numbered canonical tasks above are the program backlog that Phase 0 creates.

## 13. Quality and efficiency laws

Hard gates:

- QG-0: traceable scope and evidence;
- QG-1: zero successful unauthorized actions;
- QG-2: captured content has zero authority;
- QG-3: explicit multi-root permissions;
- QG-4: duplicate-safe resume;
- QG-5: independent evidence reconstruction;
- QG-6: typed, bounded escalation;
- QG-7: Windows/resource viability.

Efficiency means:

- successful bounded jobs per wall hour;
- low human intervention minutes per successful job;
- fewer scarce CLI escalations without lower quality;
- procedure-complete execution, not merely correct intuition;
- successful bounded recovery when eligible;
- complete evidence;
- acceptable coexistence and maintenance burden;
- replaceable runtime-specific code.

Anti-overengineering:

- Markdown and existing APEX contracts only for Phase 0;
- no new PM runtime/service/database;
- one source of truth per fact class;
- no component without a traced story and acceptance fixture;
- no multi-runtime production architecture unless a large repeatable advantage earns it;
- no persistent service or schema added without an observed file-based limitation;
- record `UNMEASURED` rather than manufacturing numeric precision.

## 14. Known drift and reconciliation target

The following current files contain narrow wording that is superseded by R1/R2/R3:

- `apex-meta/local-orchestration-engine/00-START-HERE.md`;
- `apex-meta/local-orchestration-engine/HANDOVER.md`;
- `apex-meta/local-orchestration-engine/architecture/01-macro-architecture-decision.md`;
- `scripts/fee/README.md`;
- `scripts/fee/__init__.py`.

The reconciliation must say:

- broad four-layer/cross-project FEE is the product target;
- Weekly step 4 is the first MVP/implemented seam;
- current package implementation remains limited;
- FEE is not a third planning/governance authority;
- the project cockpit is the current navigation surface.

Preserve history: add supersession context to the architecture decision rather than pretending the early decision never existed.

## 15. Execution discipline

- Follow the eight implementation-plan tasks in order.
- Complete each task's validation before its commit.
- Keep commits small and named exactly or equivalently to the plan.
- Use `apply_patch` for file edits in Codex environments.
- Use `rg` for search and validation.
- Do not stage with broad globs that could capture the bundle files.
- Run `git diff --cached --check` before every commit.
- After modifying `scripts/fee/__init__.py`, rerun the 32-test FEE suite.
- At final verification, rerun both the 32-test FEE suite and 177-test lmbench suite.
- Stop at the completed Phase-0 operator review gate.

## 16. Fresh-reader acceptance test

At completion, a different AI must be able to read only:

1. `project/README.md`;
2. `project/00-PROJECT-COCKPIT.md`;
3. `project/13-STATUS-AND-NEXT-ACTIONS.md`;
4. `project/15-HANDOVER.md`;
5. the canonical next task;

and accurately state:

- what FEE is;
- what is implemented;
- what is only researched;
- what is unbuilt;
- which user stories drive it;
- the active horizon and task;
- the next exact step;
- allowed and forbidden writes;
- operator gates and stop conditions;
- why OpenClaw/Hermes/Odysseus and Qwen3-8B remain evidence-gated.

If the reader cannot do this, Phase 0 has not passed.

## 17. Final report required from the receiving AI

Return:

```yaml
FINAL_REPORT:
  verdict: PASS | PARTIAL | FAIL
  repository: leela-spec/apexai-os-meta
  branch: main
  phase: FEE_PHASE_0_PROJECT_ENVIRONMENT
  commits_created: []
  pushed: true | false
  files_created: []
  files_modified: []
  canonical_tasks_created: 0
  validation:
    expected_project_files_present: pass | fail
    task_contract_fields_present: pass | fail
    user_story_ids_complete: pass | fail
    workstream_ids_complete: pass | fail
    quality_gate_ids_complete: pass | fail
    traceability_complete: pass | fail
    stale_scope_reconciled: pass | fail
    path_checks: pass | fail
    placeholder_overclaim_scan: pass | fail
    fresh_reader_handover: pass | fail
    fee_tests: not_run_or_exact_terminal_summary
    lmbench_tests: not_run_or_exact_terminal_summary
  preserved_untracked_bundles: true | false
  runtime_installed_or_selected: false
  next_canonical_task: 002
  unresolved_operator_gates: []
  failure_reason: null_or_exact_evidence_backed_reason
```

Do not claim `PASS` unless every Phase-0 completion condition in the design and plan is evidenced.
