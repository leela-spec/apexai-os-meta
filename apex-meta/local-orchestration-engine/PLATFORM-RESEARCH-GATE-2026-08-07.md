---
title: "Local Execution Layer — Platform Research Gate"
doc_type: research_gate
initiative: local-orchestration-engine
created: 2026-08-07
authority: operator-session-2026-08-07
status: "research required before platform lock"
depends_on:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md
candidate_platforms:
  - custom_FEE_components
  - OpenClaw
  - Hermes
  - Odysseus
  - hybrid
---

# Platform Research Gate — OpenClaw / Hermes / Odysseus / FEE

## 1. Decision that is intentionally NOT made yet

The executor platform is **not selected**.

The operator confirmed a hybrid research posture in Round 1: retain the useful deterministic/FEE work, but research and test OpenClaw, Hermes, and Odysseus against the actual execution-user stories before assigning permanent roles.

No future implementation session may treat any of the following as already proven:

- Odysseus is the executor;
- Hermes is only a notifier;
- OpenClaw is the executor;
- FEE must implement all browser/tool functionality itself;
- one platform must own every function;
- a platform's generic benchmark or marketing feature list is enough to select it.

The target architecture may be **hybrid** if different systems are strongest at different parts of the execution stack.

---

## 2. Product role to evaluate

The required role is a **bounded local execution operator**, not the project-management brain.

It must help conserve scarce Claude Code/Codex usage by performing repeatable operational work under plans created by stronger reasoning systems.

Required behavioral distinction:

```text
Reasoning layer:
  "What should we do and why?"

Execution layer:
  "Perform the authorized steps, capture results, recover from small known failures,
   and escalate when the problem exceeds your authority."
```

A platform that is excellent at autonomous goal-seeking but weak at bounded, auditable execution may be a worse fit than a less autonomous platform.

---

## 3. Mandatory evaluation user flows

Every candidate must be evaluated against the same corpus.

### UF-A — Subscription research executor

**Story:** A subscription reasoning model produces a plan and several prompts. The execution layer opens the declared subscription surfaces, submits prompts, waits for completion, captures exact outputs/artifacts, and returns them for higher-quality synthesis.

**Required abilities:**
- browser/session control;
- deterministic prompt selection from the plan;
- output capture;
- resumability;
- account/session error reporting;
- no reinterpretation of captured text into unauthorized local commands.

### UF-B — Script failure recovery

**Story:** A deterministic Python/PowerShell process fails for a small operational reason. The executor reads a bounded error packet, chooses a permitted recovery route, retries once when allowed, then escalates with evidence if unresolved.

**Required abilities:**
- run declared commands;
- read exit status/log slices;
- use allowlisted recovery operations;
- distinguish safe recoverable failure from escalation;
- never rewrite arbitrary runtime/code just because a small model suggested it.

### UF-C — Detective evidence collection

**Story:** The executor gathers objective evidence for a stronger Detective/reviewer: diffs, tests, file presence, hashes, timestamps, contradiction candidates, logs, status and provenance.

**Required abilities:**
- filesystem/repository inspection;
- structured evidence packet creation;
- exact source references;
- separation of observation from judgement.

### UF-D — Database / knowledge hygiene

**Story:** A reasoning model specifies transformation/cleanup rules. Exact cases are deterministic. The local execution model handles bounded format anomalies; semantic ambiguity escalates.

**Required abilities:**
- constrained file/database operations;
- schema adherence;
- transaction/dry-run support where appropriate;
- exception queues;
- no silent semantic invention.

### UF-E — Multi-repo / multi-folder execution

**Story:** The Apex Weekly Orchestrator receives project states from multiple project repos, creates sprint guidance, and issues jobs that may read/write one or more explicitly declared repos/folders.

**Required abilities:**
- job-scoped root/repository permissions;
- support for multiple repositories;
- no permanent assumption that all work lives in one repo;
- support for `C:\GitDev\...` as a common root without making it the only possible root;
- safe future support for other configured folders;
- clean provenance of which project/repo each artifact came from.

### UF-F — Personal weekly execution

**Story:** A higher-reasoning model creates bounded personal/work execution instructions from permitted sources. The execution layer performs low-risk operations and stops at sensitive/consequential gates.

**Required abilities:**
- explicit data/source permissions;
- sensitive-action gating;
- auditability;
- separation of project and personal trust zones;
- resumable unattended execution.

---

## 4. Evaluation dimensions and 1–100 scoring

Scores are evidence-based estimates during research and measured values during testing. They are not to be fabricated to create false precision.

| Dimension | Meaning | Weight |
|---|---|---:|
| `FIT` | How well the platform naturally supports UF-A..UF-F | 18 |
| `BOUND` | Ability to constrain actions/permissions and stop autonomy drift | 15 |
| `BROWSER` | Reliability of browser/subscription interaction | 14 |
| `TOOLS` | Safe local tools, scripts, filesystem, Git/process support | 12 |
| `RECOVERY` | Bounded error handling, resumability, failure evidence | 10 |
| `AUDIT` | Logs, provenance, replayability, deterministic envelopes | 9 |
| `MULTIROOT` | Multi-repo/multi-folder permission model | 8 |
| `LOCALMODEL` | Quality of local-model backend integration and model swapping | 5 |
| `WINDOWS` | Windows operating fit and installation/maintenance burden | 4 |
| `RESOURCE` | RAM/CPU/GPU overhead while browsers and local model coexist | 3 |
| `MAINT` | Expected maintenance burden; score 100 = low burden | 2 |

Weighted score is useful for comparison, but **hard failures override the total**.

---

## 5. Hard gates

A candidate cannot become the primary execution runtime if any of these remain unmitigated:

### G-P1 — Authority containment

Captured browser/model content must not automatically become local commands, filesystem paths, provider choices, or workflow changes.

### G-P2 — Job-scoped permissions

The system must support explicit allowed roots/repositories/capabilities per execution job, either natively or through a thin external broker.

### G-P3 — Resumability

A crash, logout, browser failure, or model restart must not force the entire flow to restart from memory.

### G-P4 — Evidence capture

Inputs, actions, outputs, failures, retries, model/provider usage and produced artifacts must be recoverable enough to build the existing FEE/APEX evidence chain.

### G-P5 — Escalation

The executor must be able to stop and package an unresolved problem for Claude Code/Codex/human review rather than continuing autonomously until it invents a solution.

### G-P6 — Windows viability

The chosen composition must run realistically on the operator's Windows laptop and coexist with browser sessions and the local model. A theoretically elegant Linux-only architecture is insufficient unless the Windows-hosted deployment path is practical.

---

## 6. Platform hypotheses to research — NOT decisions

These are starting hypotheses only.

### H1 — Custom FEE components

Possible strength:
- deterministic state, frozen work packets, evidence contracts, APEX-native semantics, small attack surface.

Possible weakness:
- browser control, tool brokerage, session management and local-model agent runtime may require substantial custom engineering.

Research question:
- should FEE remain the deterministic state/evidence spine while another platform supplies execution capabilities?

### H2 — Hermes

Possible strength:
- agent/tool ecosystem, sessions, memory/messaging and local-model integration may reduce custom runtime work.

Possible weakness:
- generic autonomous-agent behavior may need significant restriction to meet the bounded-operator role.

Research question:
- can Hermes be constrained into a reliable execution worker/tool host rather than becoming a competing orchestration brain?

### H3 — Odysseus

Possible strength:
- self-hosted agent workspace, local-model backends and tool/web integrations may provide much of the required runtime stack.

Possible weakness:
- its built-in agent/orchestration concepts may overlap with or bypass APEX/FEE authority boundaries.

Research question:
- can Odysseus expose reusable execution capabilities behind APEX/FEE contracts without importing an unwanted autonomous control plane?

### H4 — OpenClaw

Known repo-level strength:
- the operator already has substantial agent, handoff, routing, Detective, informatics-design, hygiene and orchestration doctrine in `leela-spec/MasterOfArts/OpenClaw/07_finalopenclawsystem/`.

Unknown:
- how much of the current final-system baseline is executable runtime versus governance/configuration/doctrine;
- whether its runtime/tool/browser surfaces are the best substrate for UF-A..UF-F;
- whether using OpenClaw directly would duplicate the Weekly/Multi-Agent orchestration responsibilities.

Research question:
- which OpenClaw components should be reused as execution capabilities, and which should remain higher-level agent doctrine/process rather than the low-level executor?

### H5 — Hybrid

Possible composition examples to investigate, not endorse:

```text
APEX Weekly / Multi-Agent orchestration
        |
        v
FEE deterministic work-packet + evidence spine
        |
        +--> Hermes execution/tool capability
        +--> Odysseus capability where superior
        +--> provider-specific browser mechanisms
        +--> OpenClaw agent/Detective/KB processes where they genuinely fit
        |
        v
local model as bounded operator
```

A hybrid is justified only if the interfaces remain simpler than rebuilding one monolith.

---

## 7. Research questions that must be answered

1. **Runtime reality:** What does each candidate actually execute today, versus what exists only as design/documentation?
2. **Browser control:** How does each candidate control authenticated browser sessions, and how stable/supported is that mechanism per provider?
3. **Local tool model:** Can tools be individually allowlisted and arguments validated outside the local model?
4. **Command safety:** Can captured untrusted content be prevented from dynamically generating arbitrary shell commands?
5. **State:** Where is task state persisted? Can a run resume after process/browser/model restart?
6. **Multi-root:** Can one job receive explicit allowed folders/repositories without globally opening the machine?
7. **Windows:** What is the real Windows deployment path and maintenance cost?
8. **Local inference:** Which inference backends/model formats are supported, and can the operator swap models without redesigning the runtime?
9. **Observability:** What action/event log exists? Can it feed FEE/APEX evidence artifacts deterministically?
10. **Failure classes:** How are timeouts, provider logout, captcha/challenge, malformed tool output, script failure and partial completion represented?
11. **Escalation:** Can failures be packaged for Claude Code/Codex/human review with minimal context/token waste?
12. **Resource use:** What CPU/RAM/GPU footprint remains while browsers and the local model are simultaneously active?
13. **Update risk:** How frequently does the platform change and how likely are integrations/configurations to break?
14. **Governance overlap:** Does adopting the platform accidentally create a third project-management/orchestration authority?
15. **License/operational constraints:** Are there licensing, deployment, update, security or data-handling constraints that materially affect long-term use?

---

## 8. Required test protocol after desk research

Desk research narrows candidates; it does not choose the winner.

For each surviving platform/composition:

1. install/configure in an isolated test setup;
2. use the **same local-model candidate** where technically possible so platform quality is not confused with model quality;
3. execute standardized fixtures for UF-A through UF-F;
4. run each critical fixture repeatedly rather than accepting one successful demo;
5. record success/failure, human interventions, elapsed time, local-model turns, CLI escalations, browser/session failures, and peak memory;
6. inject expected failures deliberately;
7. verify resumability after interruption;
8. verify job-root containment and unauthorized-action rejection;
9. verify captured hostile text remains inert data;
10. calculate the evidence-based scoring matrix and document qualitative failure modes.

---

## 9. Core metrics

Metrics should be measured per user flow and overall.

### Reliability

- task completion rate;
- correct-action rate;
- false-success rate;
- recovery success rate;
- resume success rate;
- unauthorized-action attempt rate.

### Resource conservation

- Claude Code/Codex escalations per 100 execution jobs;
- CLI tokens/turns avoided versus manual/CLI-first baseline;
- human interventions per 100 jobs;
- subscription reasoning turns used for operational rather than substantive work.

### Operational cost

- elapsed time per job;
- local-model inference time;
- peak RAM/GPU usage;
- simultaneous browser viability;
- setup/update/repair effort.

### Target direction — not yet a proven threshold

The architecture should aim to move routine operational work away from scarce CLI agents while preserving safe escalation. A later benchmark round may establish explicit thresholds such as maximum CLI escalations per 100 jobs; **no numeric acceptance threshold is locked before baseline measurement exists**.

---

## 10. Research deliverable

The research pass must return one comparison table plus a recommendation packet containing:

```yaml
platform_research_result:
  candidates_tested_or_researched: []
  evidence_date: null
  per_user_flow_scores: {}
  weighted_scores: {}
  hard_gate_results: {}
  strongest_role_per_candidate: {}
  duplicated_orchestration_risk: {}
  windows_fit: {}
  resource_profile: {}
  implementation_effort: {}
  unresolved_unknowns: []
  recommended_composition: null
  rejected_compositions: []
  reversal_triggers: []
  confidence_0_to_100: null
```

Every consequential claim must point to either:

- current primary documentation/source code;
- direct inspection of the operator's repos; or
- an executed local benchmark/test.

Marketing descriptions alone are insufficient for final selection.

---

## 11. Operator Q&A gate after research

Research does **not** automatically authorize implementation.

After the comparison packet exists, run another operator Q&A round covering at minimum:

- platform/composition choice;
- exact browser-provider strategy;
- local-model benchmark candidates;
- path/root capability model;
- sandbox/isolation level;
- personal-life trust zone;
- CLI escalation policy;
- overnight/scheduling behavior;
- observability/notifications;
- resource/token budgets;
- revised build order.

Only after that round is locked should the implementation plan be rewritten.
