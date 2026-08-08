---
title: "Platform Research Prompt — Hermes"
doc_type: research_prompt
initiative: local-orchestration-engine
created: 2026-08-08
candidate: Hermes
depends_on:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md
  - apex-meta/local-orchestration-engine/PLATFORM-RESEARCH-GATE-2026-08-07.md
---

# Deep Research Prompt — Hermes

## Mission

Evaluate **Hermes Agent** as a candidate execution/tool runtime behind the APEX/FEE deterministic authority spine. Do not judge Hermes by generic autonomy alone. Determine whether its useful capabilities can be constrained into a bounded local execution operator that follows externally created plans, uses explicit capabilities, captures evidence, resumes safely and escalates instead of becoming a competing orchestration brain.

Locked architecture:

```text
subscription/deep-reasoning AI -> strategy/planning/research/synthesis
Claude Code/Codex -> scarce hard coding/architecture/debugging/verification
local LLM execution operator -> bounded operations/recovery/evidence/escalation
deterministic layer -> Python/PowerShell/Git/validators/ledgers/exact transforms
```

APEX/FEE is the candidate spine for work packets, permissions, state/checkpoints, evidence and escalation.

## Evidence requirements

Use current primary evidence:

1. official Hermes repository/source code;
2. official current documentation;
3. current release/version history;
4. relevant issues/discussions only to verify real deployment limitations or unresolved defects;
5. executed tests if available.

For consequential claims label evidence as source-code verified, officially documented, measured, inferred, or unknown.

## Locked architecture decisions to respect

- FEE/custom deterministic spine remains the default authority/state/evidence hypothesis;
- fresh vs persistent browser conversation is declared by the work packet;
- browser adapters may be provider-specific behind a common bounded contract;
- low-risk UI recovery may be local; auth/CAPTCHA/account/payment/security ambiguity stops;
- local edits are bounded/mechanical by default, not general code authorship;
- tools should appear as authorized action IDs with independently validated arguments rather than arbitrary shell;
- multiple explicit roots/repositories with distinct read/write permissions are required;
- Git authority is capability-based;
- project/personal trust profiles must be separable;
- local-model research must remain model-swappable;
- blocked overnight jobs checkpoint while independent work can continue safely;
- structured action/event evidence is mandatory;
- captured web/model/source instructions have zero execution authority.

## Mandatory user flows

### UF-A — Subscription research executor
Evaluate authenticated browser/session operation, fresh/persistent sessions, prompt submission, file transfer, long-running/deep-research waiting, exact response capture, provenance, logout/challenge detection, resumability and hostile-content containment.

### UF-B — Script failure recovery
Evaluate declared command execution, bounded log/exit inspection, allowlisted recovery actions, argument validation, one-safe-retry behavior, arbitrary-shell prevention and escalation packet creation.

### UF-C — Detective evidence collection
Evaluate Git/filesystem inspection, hashes, tests, source references, timestamps, structured evidence packets and clean separation of observation from consequential judgement.

### UF-D — Database / KB hygiene
Evaluate constrained file/data operations, schema fidelity, dry-run/transaction possibilities, bounded anomaly handling, preservation of unknown fields and semantic-ambiguity queues.

### UF-E — Multi-repo / multi-folder execution
Evaluate explicit per-job roots, different read/write permissions, multiple repositories, Windows path handling, cross-repo provenance, Git capabilities and whether an external FEE broker can enforce missing controls.

### UF-F — Personal weekly execution
Evaluate separate browser/session credentials, filesystem/capability profiles, approval gates, auditability, resumable unattended work and practical separation from project automation.

## Hard gates

Return `PASS`, `PASS_WITH_EXTERNAL_BROKER`, `FAIL`, or `UNKNOWN` for:

1. **Authority containment** — captured data cannot create executable authority.
2. **Job-scoped permissions** — explicit roots/repos/capabilities per job.
3. **Resumability** — durable continuation after crash/logout/browser/model restart.
4. **Evidence capture** — actions/inputs/outputs/retries/artifacts/failures can map into FEE evidence.
5. **Safe escalation** — unresolved problems stop and package evidence.
6. **Practical Windows viability** — realistic Windows 11 operation on Core Ultra 7 258V, ~32 GB RAM, Arc 140V alongside browser/local model/development tools.

Hard-gate failure overrides aggregate score.

## Hermes-specific questions

1. What is Hermes's current runtime architecture and supported deployment modes?
2. Does it run natively/practically on Windows, WSL, containers or another path, and what are the real maintenance implications?
3. Which browser/web-control mechanisms exist today? Are authenticated existing browser sessions supported reliably?
4. How are sessions/tasks persisted? What exactly survives restart?
5. What local-model backends/providers are supported? Can models be swapped without redesigning the orchestration layer?
6. How are tools defined, permissioned and invoked?
7. Can tools be individually allowlisted and arguments validated outside model reasoning?
8. Can arbitrary shell/filesystem actions be removed or wrapped behind an external broker?
9. How naturally can Hermes consume a frozen external plan rather than pursuing its own autonomous goals?
10. Can continuation/recovery be restricted to a closed set of externally authorized routes?
11. Can actions/events/results be exported deterministically to an APEX/FEE ledger?
12. How does Hermes represent timeouts, malformed tool output, browser failure, provider logout and partial completion?
13. Can it stop and produce compact escalation evidence rather than repeatedly self-repairing?
14. What messaging/notification mechanisms exist and are they useful without granting orchestration authority?
15. What MCP/tool ecosystem exists, and what attack/maintenance surface does that introduce?
16. What protections exist for prompt injection/tool-use attacks from retrieved/browser content?
17. Does memory/autonomous planning create authority drift risk? Can those features be disabled or subordinated?
18. What CPU/RAM/GPU overhead does the runtime add before the local model/browser load?
19. What release cadence/update churn could break integrations?
20. What licensing/security/data-handling constraints matter?

## Role hypotheses to test

Evaluate independently:

1. Hermes as **primary bounded executor behind FEE**.
2. Hermes as **tool/browser runtime behind FEE**, with planning/memory features minimized.
3. Hermes as **session/resume/notification infrastructure only**.
4. Hermes as a **specialized runtime for selected UF-A..UF-F flows**, not all jobs.
5. Hermes excluded because containment/Windows/maintenance burden is too high.

## Scoring

0–100 scores with confidence 0–100:

| Dimension | Weight |
|---|---:|
| FIT | 18 |
| BOUND | 15 |
| BROWSER | 14 |
| TOOLS | 12 |
| RECOVERY | 10 |
| AUDIT | 9 |
| MULTIROOT | 8 |
| LOCALMODEL | 5 |
| WINDOWS | 4 |
| RESOURCE | 3 |
| MAINT | 2 |

Score UF-A..UF-F individually too.

## Required output

1. Executive finding.
2. Current-runtime capability map with versions/commits.
3. UF-A..UF-F table.
4. Hard-gate table.
5. Weighted score + confidence.
6. Detailed Windows path and maintenance burden.
7. Browser/session mechanism assessment.
8. Tool/permission containment assessment.
9. Local-model/backend swapability assessment.
10. State/resume/evidence assessment.
11. Strongest Hermes role in a hybrid architecture.
12. Required external FEE wrappers/brokers.
13. Unknowns requiring local tests.
14. Concrete bake-off fixtures.
15. Rejected roles and reversal triggers.
16. Evidence appendix.

End with:

```yaml
platform_research_result:
  candidate: Hermes
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
