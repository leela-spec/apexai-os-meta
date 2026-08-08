---
title: "Platform Research Prompt — OpenClaw"
doc_type: research_prompt
initiative: local-orchestration-engine
created: 2026-08-08
candidate: OpenClaw
depends_on:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md
  - apex-meta/local-orchestration-engine/PLATFORM-RESEARCH-GATE-2026-08-07.md
---

# Deep Research Prompt — OpenClaw

## Mission

Evaluate **OpenClaw** as a candidate component of the APEX bounded local execution architecture. Do not assume OpenClaw must be the primary runtime. Determine what is executable runtime versus doctrine/configuration/process, which components are reusable, and what role OpenClaw should occupy in a hybrid composition if it is not the low-level executor.

The target architecture is already constrained:

```text
Layer 4 — subscription/deep-reasoning AI: strategy, planning, research, synthesis, judgement
Layer 3 — scarce CLI AI: Claude Code/Codex for difficult coding/architecture/debugging/verification
Layer 2 — local LLM execution operator: bounded operations, small recovery, evidence capture, escalation
Layer 1 — deterministic execution: Python/PowerShell/Git/validators/ledgers/exact transforms
```

Core rule: **the local LLM is the operator, not the brain.**

APEX/FEE is the candidate deterministic spine for work packets, permissions, state/checkpoints, evidence and escalation. OpenClaw must be evaluated on whether it can operate behind or alongside that spine without becoming a competing orchestration/project-management authority.

## Evidence requirements

Use current primary sources wherever possible:

1. current OpenClaw source repositories and versioned code;
2. current official documentation;
3. the operator's existing OpenClaw material in `leela-spec/MasterOfArts/OpenClaw/07_finalopenclawsystem/`;
4. executed tests/benchmarks only when available;
5. secondary sources only as supporting context, never as sole evidence for a consequential claim.

For every important claim, distinguish:

- verified source-code behavior;
- official documentation claim;
- operator-repo doctrine/process;
- inference/hypothesis;
- unknown/unverified.

Do not convert marketing language into a fact.

## Locked architecture decisions to respect

OpenClaw must be tested against these decisions, not evaluated as a generic autonomous agent:

- FEE/custom deterministic state/evidence/permission spine remains the default architecture hypothesis;
- OpenClaw may be decomposed: runtime components and higher-level doctrine/Detective/KB/hygiene/routing processes are separate evaluation targets;
- work packet declares fresh vs persistent browser conversation;
- browser control should support layered/provider-specific adapters behind a common bounded contract;
- local browser recovery is bounded; auth loss, CAPTCHA/challenge, account/payment/security ambiguity stops/escalates;
- local model may perform bounded operational/mechanical edits, not general unbounded code repair;
- tools should be exposed as authorized action IDs with independently validated arguments rather than arbitrary model-generated shell;
- jobs may declare multiple explicit roots/repositories with separate read/write permissions;
- Git authority is capability based, destructive history operations prohibited/escalated;
- personal automation needs a separate trust profile;
- overnight blocked jobs checkpoint while independent safe work may continue;
- structured event ledger is mandatory, screenshots selective;
- captured browser/model/source content has zero executable authority.

## Mandatory user-flow corpus

Evaluate OpenClaw against **all six flows using the same definitions**.

### UF-A — Subscription research executor

A higher-reasoning model creates prompts for subscription surfaces such as Claude, ChatGPT and Gemini Deep Research. The executor opens the declared authenticated surface/session, submits the exact prompt, waits, captures exact results/artifacts/provenance, checkpoints state and returns raw evidence for higher-quality synthesis. The executor is not the research judge.

Evaluate:

- authenticated browser/session control;
- fresh vs persistent conversations;
- file upload/download if supported;
- deep-research/long-running completion handling;
- reliable output capture;
- login expiration/challenge handling;
- resumability;
- prompt-injection containment;
- evidence integration with FEE.

### UF-B — Script failure recovery

A deterministic Python/PowerShell process fails. Deterministic retry/known recipes run first. The local execution model receives a bounded error packet, selects one authorized recovery action if applicable, retries once, then creates an evidence/escalation packet if unresolved.

Evaluate:

- shell/process tooling;
- action allowlisting and argument validation;
- log/exit-status inspection;
- closed-set recovery selection;
- arbitrary-shell prevention;
- escalation behavior.

### UF-C — Detective evidence collection

Collect objective evidence for Meta Detective/stronger reviewers: diffs, test results, hashes, file presence, timestamps, logs, contradiction candidates and source provenance without issuing the final validity/authority verdict.

Evaluate:

- Git/filesystem inspection;
- evidence packet generation;
- source-reference precision;
- separation of observation from judgement;
- reuse of existing OpenClaw Detective concepts without collapsing authority layers.

### UF-D — Database / knowledge hygiene

A reasoning model supplies explicit transformation rules. Deterministic scripts handle exact cases; bounded local model handles format anomalies; semantic ambiguity queues/escalates.

Evaluate:

- constrained file/database operations;
- schema adherence;
- dry-run/transaction patterns;
- exception queues;
- preservation of unknown data;
- support for OpenClaw Knowledge Bank/Hygiene processes where relevant.

### UF-E — Multi-repo / multi-folder execution

A Weekly Orchestrator job may explicitly read/write one or more project roots and output folders, while other roots remain forbidden. `C:\GitDev` is a common root, not a permanent exclusive boundary.

Evaluate:

- per-job root registry/capabilities;
- read/write distinction per root;
- multiple repositories per job;
- cross-repo artifact/provenance handling;
- Git capability controls;
- Windows path behavior;
- ability to place OpenClaw execution behind an external permission broker if native controls are insufficient.

### UF-F — Personal weekly execution

Higher-reasoning models create bounded personal/work instructions. The execution layer may perform explicitly permitted low-risk operations but sensitive/consequential actions stop for approval. Project and personal trust profiles should be separable.

Evaluate:

- browser profile/session separation;
- credential/data separation;
- root/capability separation;
- approval gates;
- auditability;
- whether OpenClaw architecture naturally encourages or undermines this split.

## Hard gates

Mark each `PASS`, `PASS_WITH_EXTERNAL_BROKER`, `FAIL`, or `UNKNOWN`.

### G-P1 Authority containment
Captured browser/model/source content must not automatically become new commands, paths, provider choices or workflow changes.

### G-P2 Job-scoped permissions
Explicit allowed roots/repositories/capabilities per job, natively or behind a thin deterministic broker.

### G-P3 Resumability
Crash/logout/browser failure/model restart must resume from durable state rather than memory reconstruction.

### G-P4 Evidence capture
Inputs, actions, outputs, provider/model/runtime use, retries, artifacts and failures must integrate with the FEE/APEX evidence chain.

### G-P5 Safe escalation
Unresolved problems must stop and package evidence for Claude Code/Codex/reasoning/human review rather than continuing goal-seeking autonomously.

### G-P6 Practical Windows viability
Realistic Windows 11 deployment and maintenance on an Intel Core Ultra 7 258V / ~32 GB RAM / Intel Arc 140V laptop while browsers and local inference coexist.

## OpenClaw-specific questions

1. What is the current executable OpenClaw runtime architecture?
2. Which parts of the operator's `07_finalopenclawsystem` are executable runtime, which are prompts/configuration/doctrine, and which require another engine?
3. Can OpenClaw expose bounded browser/tool capabilities without controlling project strategy?
4. What permission/allowlist model exists for tools/filesystem/shell/Git?
5. Can an external deterministic broker validate every action/argument before execution?
6. How is session/task state persisted and resumed?
7. What browser stack exists today, especially for authenticated subscription sites?
8. What current Windows deployment path exists?
9. How are local models configured/swapped? Which runtimes/backends are supported?
10. What event/action logs are available and how easily can they map to FEE evidence?
11. How does OpenClaw handle prompt injection or instructions discovered inside source/browser content?
12. Does adopting OpenClaw introduce a competing Meta Ops/Weekly/Strategy authority?
13. Which OpenClaw concepts are best retained purely as higher-level doctrine: Meta Ops, Detective, KB, Hygiene, routing, prompt/workflow handling, handoff contracts?
14. What maintenance/update risk exists if browser/runtime internals change?
15. What licenses/deployment/data-handling constraints matter?

## Scoring

Score 0–100 with confidence 0–100. Numbers must be evidence-based estimates, not false precision.

Use platform-gate weights:

| Dimension | Weight |
|---|---:|
| FIT to UF-A..UF-F | 18 |
| BOUND containment | 15 |
| BROWSER | 14 |
| TOOLS | 12 |
| RECOVERY | 10 |
| AUDIT | 9 |
| MULTIROOT | 8 |
| LOCALMODEL | 5 |
| WINDOWS | 4 |
| RESOURCE | 3 |
| MAINT | 2 |

Also score each UF-A..UF-F individually.

Hard-gate failure overrides weighted score.

## Required comparison of OpenClaw roles

Assess at least these role hypotheses independently:

1. **Primary low-level executor behind FEE**
2. **Browser/tool capability provider behind FEE**
3. **Higher-level Detective/KB/Hygiene/agent doctrine only**
4. **Hybrid: runtime subset + higher-level doctrine**
5. **Not recommended in the execution stack**

For each role, provide:

- strengths;
- required external wrappers/brokers;
- duplicated-orchestration risk;
- implementation burden;
- reversal trigger.

## Required output

Produce:

1. Executive finding — no more than one page.
2. Runtime reality map: executable vs doctrine/config/process.
3. UF-A..UF-F evidence table.
4. Hard-gate table.
5. Weighted scoring matrix + confidence.
6. Windows/local-model/browser viability findings.
7. Integration diagram showing how OpenClaw could sit behind/above FEE.
8. Strongest role for OpenClaw.
9. Rejected OpenClaw roles and why.
10. Unknowns that require a local bake-off.
11. Concrete test fixtures for unresolved claims.
12. Source/evidence appendix with dates/versions/commit SHAs where possible.

End with exactly this YAML shape:

```yaml
platform_research_result:
  candidate: OpenClaw
  evidence_date: null
  versions_or_commits_reviewed: []
  runtime_reality: {}
  per_user_flow_scores: {}
  weighted_scores: {}
  score_confidence: {}
  hard_gate_results: {}
  windows_fit: {}
  browser_fit: {}
  local_model_fit: {}
  permission_model: {}
  state_and_resumability: {}
  audit_and_evidence: {}
  duplicated_orchestration_risk: {}
  strongest_role: null
  required_external_brokers: []
  unresolved_unknowns: []
  benchmark_tests_required: []
  rejected_roles: []
  reversal_triggers: []
  overall_confidence_0_to_100: null
```
