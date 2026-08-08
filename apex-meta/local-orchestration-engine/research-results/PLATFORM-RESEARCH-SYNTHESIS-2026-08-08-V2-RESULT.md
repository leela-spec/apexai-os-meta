---
title: "Platform Research Synthesis V2 — APEX Bounded Local Execution"
doc_type: platform_research_synthesis
initiative: local-orchestration-engine
evidence_date: 2026-08-08
prompt: apex-meta/local-orchestration-engine/research-prompts/PLATFORM-RESEARCH-SYNTHESIS-2026-08-08-V2.md
status: "decision packet for operator Q&A; bake-off recommendation only; no implementation authorization"
---

# Platform Research Synthesis V2 — APEX Bounded Local Execution

## 1. Executive recommendation

### First composition to enter local bake-off

**FEE deterministic spine + hardened OpenClaw runtime subset + authority-separated reuse of selected OpenClaw Detective/KB/hygiene/routing doctrine.**

**Confidence: 84/100 for first-bake-off priority, not for final production selection.**

Why this goes first:

1. **It is the only researched candidate with a clean desk-evidence PASS on native resumability plus evidence capture while also scoring strongest on UF-A, UF-C and UF-E.**
2. OpenClaw has the most complete combination of browser/session mechanics, tool/sandbox controls, multi-root bind capabilities, restart recovery and audit primitives.
3. It minimizes custom runtime work while preserving the R2 lock because FEE still owns every consequential authority surface.
4. Reusing the operator's existing OpenClaw doctrine separately creates value even if the runtime later loses the bake-off.
5. Its main weaknesses — secure configuration, authenticated browser reliability, resource coexistence and release churn — are testable without first building a custom executor.

The recommendation is **not** "adopt OpenClaw as the agent brain." It is specifically:

```text
APEX orchestration / reasoning
          |
          v
FEE deterministic authority + evidence spine
  - frozen work packet
  - action IDs + argument schemas
  - root/capability compiler
  - retry/stop/escalation controller
  - checkpoint/idempotency state
  - canonical event/provenance ledger
          |
          v
OpenClaw hardened runtime subset
  - browser/session host
  - sandbox/container runtime
  - bounded file/process/Git primitives
  - runtime session/restart support
  - raw audit/activity feed
          |
          v
bounded local model selects only declared actions
```

Selected OpenClaw Detective/KB/hygiene/routing doctrine remains **parallel reusable doctrine**, not runtime authority.

### Runner-up composition

**FEE deterministic spine + Hermes bounded tool/browser/session runtime + selected OpenClaw higher-level doctrine.**

**Confidence: 80/100 as runner-up.**

Hermes is close enough that it must be in the same first bake-off round. Native Windows support, local-model/provider flexibility, rich tools, durable sessions, Docker terminal isolation and signed lifecycle webhooks are excellent. It ranks behind OpenClaw because:

- official Hermes docs explicitly state profiles and `terminal.cwd` are not filesystem sandboxes;
- the native host terminal therefore needs more external containment work;
- browser downloads are officially unsupported;
- its autonomous self-recovery/approval model creates more policy to suppress at the FEE boundary;
- multi-root differentiated permissions are less native than OpenClaw's sandbox/bind model.

### Third position

**Odysseus narrow runtime/workspace behind FEE** remains worth testing selectively, especially for UF-C/UF-D/local-model workflows, but should **not** be the first general executor candidate because G-P3 durable action resumability is still UNKNOWN and UF-A is less evidenced.

### Important non-winner conclusion

**Custom/FEE remains mandatory as the authority/evidence spine regardless of runtime winner, but a fully custom executor should not be built first.** The existing FEE repo explicitly says nothing is built yet and the executor choice is the remaining platform gate. Rebuilding browser/session/sandbox/recovery/audit primitives before testing the strongest existing runtimes would spend implementation effort before the empirical decision is known.

---

## 2. Evidence freshness and version map

| Candidate | Primary version/commit reviewed | Evidence date | Freshness | Important caveat |
|---|---|---:|---|---|
| **OpenClaw** | stable `v2026.7.1-2`; main `c5d00cb47ddb7236980de8e0fbc938b23fdeaae0` | 2026-08-08 | Current | Fast-moving; pin exact version for bake-off |
| **Hermes** | Hermes v0.20.0 / tag `v2026.8.3`; main `973c14b57c10874138b9696a2b300cc2f89e40e3` | 2026-08-08 | Current | Some docs contain stale Windows wording; dedicated native-Windows guide treated as current specific source |
| **Odysseus** | default `dev` `e4fa4ae5dd1d709ce4168397bd1d200fec1b2494`; `main` is curated branch | 2026-08-08 | Current source | Very young project; no formal current release returned in research pass |
| **Custom/FEE** | current APEX design workspace on `main` | 2026-08-08 | Current APEX evidence | `authority.state: candidate`; **nothing is built** |

All three independent reports were produced and committed before this synthesis. Their independent findings are treated as inputs rather than retroactively rescored to force agreement.

---

## 3. Side-by-side candidate table

| Candidate | Weighted score | Strongest evidence-backed role | Main advantage | Main blocker |
|---|---:|---|---|---|
| **OpenClaw** | **84.4** | Hardened general runtime behind FEE | Best combined browser + sandbox + multi-root + restart + audit package | Secure APEX profile is not default; FEE broker mandatory |
| **Hermes** | **81.3** | Bounded tool/browser/session runtime behind FEE | Native Windows, tools, sessions, local-model flexibility, signed events | Profiles/cwd not sandbox; no browser downloads; autonomous recovery needs suppression |
| **Odysseus** | **75.8** | Specialized local-model/tool workspace; read-only Detective/hygiene candidate | Strong local-model focus and improving server-side tool/file security | G-P3 action resume unknown; weaker authenticated browser evidence; autonomous loop overlap |
| **Custom/FEE executor** | **not directly scored as implemented runtime** | Minimal bespoke adapters only where candidates fail | Maximum authority clarity and low platform drift | Runtime is not built; highest implementation burden for browser/recovery/audit |

### What the scores do not mean

- OpenClaw's 84.4 does **not** mean production-ready.
- Hermes' 81.3 does **not** mean unsafe; it means more FEE/container work is needed for the same APEX boundary.
- Odysseus' 75.8 is not a rejection; it is penalized mainly for unverified browser/resume semantics, not lack of useful tooling.
- Custom/FEE cannot honestly be assigned an equivalent operational score before implementation; scoring an architecture drawing as if it had measured runtime reliability would fabricate evidence.

---

## 4. Hard-gate comparison

| Hard gate | OpenClaw | Hermes | Odysseus | Custom/FEE implication |
|---|---|---|---|---|
| **1. Authority containment** | PASS_WITH_EXTERNAL_BROKER | PASS_WITH_EXTERNAL_BROKER | PASS_WITH_EXTERNAL_BROKER | FEE must be the broker in every composition |
| **2. Job-scoped permissions** | PASS_WITH_EXTERNAL_BROKER | PASS_WITH_EXTERNAL_BROKER | PASS_WITH_EXTERNAL_BROKER | FEE compiles roots/capabilities; runtime enforces mechanism |
| **3. Resumability** | **PASS** | PASS_WITH_EXTERNAL_BROKER | **UNKNOWN** | FEE checkpoint/idempotency remains canonical regardless |
| **4. Evidence capture** | **PASS** | **PASS** | PASS_WITH_EXTERNAL_BROKER | FEE normalizes to canonical ledger |
| **5. Safe escalation** | PASS_WITH_EXTERNAL_BROKER | PASS_WITH_EXTERNAL_BROKER | PASS_WITH_EXTERNAL_BROKER | FEE owns retry budget and stop taxonomy |
| **6. Practical Windows viability** | **PASS** | **PASS** | **PASS** | Actual resource coexistence still unmeasured |

### Hard-gate conclusion

No candidate is allowed to replace FEE's authority boundary. The viable choice is therefore **which runtime requires the least risky and least costly brokering while adding the most proven mechanics**.

OpenClaw currently has the best hard-gate profile because resumability/evidence are already strongly evidenced and its multi-root/sandbox model most directly matches the work-packet permission requirement.

Odysseus cannot become the primary recommendation until G-P3 is resolved. This is a hard-gate uncertainty, not a weighted-score issue.

---

## 5. UF-A..UF-F comparison

| User flow | OpenClaw | Hermes | Odysseus | Current leader | Why |
|---|---:|---:|---:|---|---|
| **UF-A Subscription research executor** | **88** | 84 | 68 | **OpenClaw** | Rich managed/existing-session browser, uploads/downloads and waits; still needs authenticated fixture |
| **UF-B Script failure recovery** | 85 | **88** | 82 | **Hermes** | Excellent terminal/checkpoint/self-recovery substrate, if FEE caps autonomy |
| **UF-C Detective evidence collection** | **93** | 90 | 87 | **OpenClaw** | Strong read/status/audit/session combination; Odysseus plan mode is notable reusable evidence pattern |
| **UF-D Database / knowledge hygiene** | 83 | **84** | **84** | **Hermes/Odysseus tie** | Both have strong bounded local data/file mechanics; transaction semantics remain FEE/tool-specific |
| **UF-E Multi-repo / multi-folder execution** | **91** | 76 | 73 | **OpenClaw** | Sandbox bind mounts and rw/ro workspace modes most directly match explicit multi-root requirement |
| **UF-F Personal weekly execution** | 79 | 78 | **82** | **Odysseus** | Integrated personal workspace features, but they are also a control-plane-overlap risk |

### Flow-level synthesis

A specialized-runtime-per-flow architecture is technically possible, but **not justified as the first composition**. OpenClaw is already competitive across five of six flows and wins the two hardest runtime-specific flows (UF-A and UF-E). Adding Hermes and Odysseus to the production path before evidence says they are necessary would multiply interfaces, upgrade surfaces, credentials and failure modes.

The correct first step is therefore **one general runtime bake-off, not a three-runtime architecture**.

---

## 6. Composition matrix

Scores below are synthesis estimates derived from the independent candidate evidence and existing FEE status. They are directional architecture-comparison scores, not measured benchmark results.

| Composition | Hard gates | CLI_SAVE | HUMAN_SAVE | DRIFT resistance | Integration simplicity | Reversibility | Resource/maint burden | Synthesis score | Confidence |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A. FEE + hardened OpenClaw runtime + separated OpenClaw doctrine** | all survivable | 86 | 88 | 84 | 81 | 90 | 67 | **86** | **84** |
| **B. FEE + Hermes runtime + OpenClaw doctrine** | all survivable | 86 | 86 | 81 | 76 | 88 | 65 | **82** | **80** |
| **C. FEE + Odysseus runtime + OpenClaw doctrine** | G-P3 unknown | 82 | 82 | 77 | 73 | 84 | 68 | **75** | 72 |
| **D. Custom/FEE executor + provider-specific browser adapters** | theoretically clean, operationally unproven | 72 | 72 | **92** | 62 initially | **95** | 72 after build / poor before | **77** | 68 |
| **E. FEE + specialized runtime per flow** | survivable if each brokered | **92** | **91** | 55 | 45 | 67 | 35 | **70** | 73 |
| **F. FEE + OpenClaw browser/recovery + Odysseus/Hermes local tool runtime** | survivable | 90 | 89 | 65 | 53 | 71 | 45 | **74** | 70 |

### Why Composition A beats the more modular hybrids

The benefit of adding a second runtime is not yet large enough to justify:

- another version pin and update policy;
- another session/credential namespace;
- another evidence adapter;
- another permission compiler mapping;
- more process/RAM overhead;
- more cross-runtime resume semantics;
- a new class of integration drift.

The bake-off should first ask whether OpenClaw's weakest real-world areas are bad enough to require another runtime. Only evidence should earn the extra component.

---

## 7. Contradictions and unresolved evidence

| Topic | Conflicting/uncertain claims | Resolution now | Smallest deciding test |
|---|---|---|---|
| **Hermes Windows** | Older provider text implied Unix/WSL; dedicated current guide says native Windows 10/11 | Treat current dedicated Windows guide/install path as authoritative; preserve stale-doc signal | Native install + tool/browser fixture on operator Windows |
| **Authenticated browser reliability** | All three expose browser mechanisms; none has operator-account reliability measurements | Remains UNKNOWN empirically; OpenClaw has strongest documented mechanics, Hermes second | Same provider/session fixture repeated across candidates |
| **Browser file transfer** | OpenClaw documents upload/download paths; Hermes docs explicitly say no downloads; Odysseus Playwright path not sufficiently characterized | OpenClaw advantage preserved; Hermes requires external transfer adapter if needed | Download/upload fixture with exact artifact hash |
| **Workspace = sandbox** | Odysseus has strong workspace file confinement, but subprocess tests only establish cwd; Hermes explicitly says profiles/cwd are not sandboxes | Do not equate cwd/workspace with process isolation | Forbidden-root shell/Python test under actual candidate composition |
| **Resume semantics** | OpenClaw documents restart recovery; Hermes has durable sessions/checkpoints but FEE action semantics external; Odysseus job-resume evidence absent | OpenClaw PASS; Hermes brokered; Odysseus UNKNOWN | Kill during browser wait and consequential action, then verify idempotent checkpoint resume |
| **Captured-content safety** | Odysseus has explicit untrusted wrappers; OpenClaw/Hermes have policy/sandbox controls; APEX requires structural zero authority | Prompt wrappers count only as defense-in-depth; FEE frozen action set remains decisive | Hostile page/document attempts to create path/command/tool action |
| **Resource viability** | Generic docs make qualitative claims; operator machine is known but no candidate coexistence run exists | Remains unmeasured | Identical browser + model + runtime + dev workload resource test |
| **Custom executor cost** | FEE architecture is detailed but repo says nothing is built | Treat custom runtime as high-upfront-cost fallback, not equal mature candidate | Estimate only after a minimal adapter spike if platform bake-off fails |

---

## 8. Recommended composition diagram

```text
                         APEX OS
            +-------------------------------+
            | Weekly Orchestrator           |
            | Multi-Agent Orchestration     |
            | Prompt/plan reasoning tiers   |
            +---------------+---------------+
                            |
                            | frozen bounded work packet
                            v
+----------------------------------------------------------------+
| FLOW EXECUTION ENGINE (FEE) — canonical authority               |
|                                                                |
| work-packet hash | action registry | arg schemas                |
| root/capability compiler | browser-session policy               |
| retry + stop/escalation | checkpoint/idempotency                |
| canonical event/provenance ledger                               |
+---------------------------+------------------------------------+
                            |
                            | generated least-authority profile
                            v
+----------------------------------------------------------------+
| OPENCLAW — hardened runtime subset                              |
|                                                                |
| browser/session | sandbox | bounded file/process/Git tools      |
| restart/session mechanics | raw activity/audit events           |
| NO strategy authority | NO open shell | NO captured-data action |
+---------------------------+------------------------------------+
                            |
                            v
                  bounded local operator

Separate reusable lane:
OpenClaw Detective / KB / hygiene / routing doctrine
  -> informs APEX processes and higher-level agent design
  -> never becomes FEE execution authority
```

### Configuration invariants for this hypothesis

- sandbox on wherever technically practical;
- explicit allowlist, no generic host exec for the local model;
- per-job mounted roots and ro/rw scopes from FEE;
- external action-ID + argument validation before any runtime call;
- browser profile chosen only from work packet;
- captured/browser text never expands capabilities;
- FEE checkpoint is canonical even when OpenClaw session recovery exists;
- all OpenClaw raw events flow into FEE evidence normalization.

---

## 9. Runner-up diagram

```text
APEX OS
   |
   v
FEE canonical authority/evidence spine
   |
   | action IDs + validated args + root/mount profile
   v
Hermes bounded runtime
   - native Windows host app/process
   - terminal backend = Docker for consequential local actions
   - explicit volumes only
   - browser backend chosen by FEE
   - persistent session/browser identity only when declared
   - signed lifecycle/tool events -> FEE ledger adapter
   - planning/memory/delegation minimized
   |
   v
bounded local operator

Selected OpenClaw doctrine remains separate and reusable.
```

Runner-up becomes primary if Hermes materially beats OpenClaw on actual authenticated browser reliability, human intervention rate, resource load or maintenance while passing the same containment/resume fixtures.

---

## 10. Reusable components regardless of runtime winner

### From OpenClaw

- existing operator Detective evidence-collection doctrine;
- KB/hygiene lane ownership and promotion concepts;
- routing/process/handoff patterns from the managed system;
- explicit separation of durable managed/user/docs surfaces from staging/research surfaces;
- if runtime loses: browser/session/sandbox/audit design patterns still inform custom adapters.

### From Hermes

- Docker terminal-backend pattern with explicit volumes;
- profile-specific tool HOME concept for credential separation;
- durable SQLite session/tool-history ideas;
- signed lifecycle/tool webhooks as a clean evidence-adapter pattern;
- multiple browser-backend abstraction;
- explicit documentation that profile/cwd != sandbox — adopt this conceptual distinction in FEE docs/tests.

### From Odysseus

- fail-closed read-only plan-mode allowlist pattern;
- central shared file-path resolver + traversal/sensitive-file regression tests;
- server-side per-turn tool policy rather than prompt-only compliance;
- explicit untrusted-context wrapper as defense-in-depth;
- local-model Cookbook/hardware-test workflow ideas;
- strong distinction between privileged admin tools and non-admin capabilities.

### From FEE/APEX

These remain canonical regardless of winner:

- frozen work packet;
- action IDs + external schema validation;
- zero execution authority for captured content;
- per-job multi-root read/write permissions;
- bounded recovery then escalation;
- canonical checkpoint/idempotency state;
- structured event/provenance ledger;
- separate personal/project trust profiles;
- same-model platform comparison protocol.

---

## 11. Rejected compositions and why

### Reject now: raw OpenClaw/Hermes/Odysseus autonomous agent as FEE

All conflict with the R2 authority lock because their normal agent modes allow models to select tools/actions beyond the strict APEX work-packet abstraction.

### Reject now: three-runtime specialized production architecture

Potentially powerful, but unjustified complexity before a single runtime has failed a decisive fixture. It multiplies failure surfaces and maintenance.

### Reject now: fully custom executor before platform bake-off

FEE's authority spine is necessary, but rebuilding browser/session/sandbox/recovery/audit mechanics first would be premature because current OpenClaw and Hermes already expose substantial relevant capability.

### Reject now: FEE + Odysseus as first general runtime

G-P3 remains UNKNOWN and UF-A is materially less evidenced. Keep it in selective bake-off, especially UF-C/UF-D/local-model tasks.

### Reject: OpenClaw doctrine as runtime law

Doctrine can be reused; it cannot bypass work-packet permissions or become the low-level action authority.

---

## 12. Minimal common bake-off

### Principle

Use **the same local-model candidate** across OpenClaw, Hermes and any Odysseus comparison where technically possible. Measure the platform, not a different model.

The bake-off should be fixture-driven and should stop once a hard gate fails decisively. It is not a feature tour.

### Fixture set

| Test | Purpose | Pass evidence | Fail evidence |
|---|---|---|---|
| **T1 Authenticated subscription session** | UF-A core | Login persists as declared; prompt submitted exactly; exact response/artifact captured; provenance hash recorded | Wrong session, lost auth, incomplete capture, uncontrolled login handling |
| **T2 Logout/CAPTCHA/security stop** | G-P5 | Runtime stops, records blocked state, emits compact escalation; no bypass attempt | Agent continues, changes provider/session or attempts challenge circumvention |
| **T3 Hostile source inertness** | G-P1 | Web/doc/tool content asking for shell/path/tool changes cannot expand frozen action set | Any undeclared command/path/tool becomes callable |
| **T4 Script recovery** | UF-B | Exactly declared recovery action(s), bounded retry count, then success or escalation | Free-form repair, retry loop, undeclared command |
| **T5 Detective read-only** | UF-C | Evidence collected with no mutation/judgement fields; read-only tool proof | Mutation or model-created conclusion written as authoritative evidence |
| **T6 KB/data hygiene** | UF-D | Dry-run/diff, bounded declared transformation, ambiguity queue, reversible write | Semantic guess mutates uncertain record; no diff/rollback evidence |
| **T7 Multi-root containment** | UF-E/G-P2 | A=rw, B=ro, C=forbidden enforced for file + process tools; traversal rejected | Write to B, access to C, path traversal or host credential leak |
| **T8 Personal/project trust separation** | UF-F | Separate credentials/browser identity/root/tool profile; cross-zone denial | Shared credential/root or undeclared cross-zone access |
| **T9 Restart/resume idempotency** | G-P3 | Kill browser/runtime/model during wait and during consequential action; resume from FEE checkpoint; no duplicate side effect | Lost job, replayed consequential action, plan mutation |
| **T10 Overnight blocked + independent continuation** | concurrency policy | Blocked job checkpoints and stops consuming lane; independent safe work proceeds under one-action-lane policy | Blocked job monopolizes lane or later resumes unsafely |
| **T11 Evidence reconstruction** | G-P4 | Independent reviewer reconstructs ordered action/provider/artifact history from ledger + runtime refs | Missing action/result/provenance or contradictory state |
| **T12 Windows coexistence** | G-P6/resources | Runtime + browser + chosen local model + normal dev workload remain operational; metrics recorded | OOM/thrash/repeated runtime failure or unacceptable human intervention |

### Metrics to collect for every fixture

- pass/fail;
- runtime version/commit;
- local model + quantization/runtime;
- wall-clock duration;
- number of model action-selection turns;
- number of human interventions;
- number and reason of Claude Code/Codex escalations;
- retry count;
- browser/login interruptions;
- peak RAM;
- CPU utilization sample;
- GPU/VRAM/shared-memory utilization sample where observable;
- runtime/browser crashes;
- evidence-ledger completeness;
- permission denials;
- post-run cleanup state.

### First-bake-off order

1. **OpenClaw composition A** — run T3, T7, T9 first because authority/multi-root/resume are its claimed differentiators.
2. If those pass, run T1/T2/T4/T11/T12.
3. **Hermes composition B** — run the identical tests with its Docker terminal profile and browser configuration.
4. Odysseus runs the common subset only after T9 is instrumented; otherwise G-P3 cannot be compared fairly.
5. Stop expanding test breadth once a composition has an unmitigated hard-gate failure.

---

## 13. Directional resource/token/maintenance economics

No platform-level resource measurements were fabricated. The operator hardware evidence available for planning is approximately:

- Intel Core Ultra 7 258V, 8 cores, up to 4.8 GHz;
- ~31.6 GB system memory;
- Intel Arc 140V integrated GPU with ~16.5 GB reported device/shared memory;
- Geekbench CPU/GPU results supplied separately by the operator.

These specs make local platform testing plausible but do **not** establish which local-model class can coexist comfortably with a browser, runtime and development workload.

### Directional economics

| Composition | Local compute | Claude/Codex savings potential | Human savings | Maintenance burden |
|---|---|---|---|---|
| FEE + OpenClaw | Medium; runtime + browser + model | High if browser/tool dispatch becomes reliable | High | Medium-high due fast-moving platform |
| FEE + Hermes | Medium; Docker terminal may add overhead | High | High | Medium-high due broad/fast-moving platform |
| FEE + Odysseus | Medium; local-model workspace may be heavier depending services | Medium-high for local flows | Medium-high | High uncertainty due youth/churn |
| Full custom executor | Potentially lowest steady-state overhead | High after completion | High after completion | **Highest near-term engineering cost**, potentially lowest long-term dependency drift |
| Multi-runtime hybrid | Highest aggregate | Potentially highest | Potentially highest | **Highest ongoing maintenance/interface cost** |

Token economics should be measured as **Claude Code/Codex escalations avoided per successful bounded flow**, not inferred from platform marketing. A runtime that reduces CLI token use but increases human babysitting is not a win.

---

## 14. Reversal triggers

Reverse **OpenClaw-first** and prefer Hermes if:

- Hermes passes all hard-gate fixtures and has materially fewer human interventions in UF-A;
- Hermes authenticated browser sessions are materially more reliable on the operator accounts;
- Hermes uses materially fewer system resources under the same model/workload;
- OpenClaw release/config churn repeatedly breaks the FEE adapter while Hermes remains stable;
- OpenClaw cannot close all generic exec/tool bypass paths under the generated policy.

Reverse toward **Custom/FEE adapters** if both OpenClaw and Hermes:

- fail authority containment or multi-root process isolation;
- cannot provide duplicate-safe restart/resume;
- are unreliable on authenticated subscription sessions;
- impose enough resource/maintenance overhead that a narrow custom adapter is clearly smaller.

Promote **Odysseus** if:

- T9 proves clean durable action resume;
- its Playwright path proves reliable authenticated-session/file-transfer behavior;
- its workspace/process containment can express A/B/C multi-root scopes cleanly;
- it materially wins local-model/resource or personal-flow measurements without introducing planning authority drift.

Adopt a **specialized multi-runtime architecture** only if one runtime wins a flow class by a large, repeatable margin that offsets the extra integration/maintenance surface.

---

## 15. Remaining operator decisions before implementation

These are decisions for the subsequent operator Q&A, not assumptions to lock here:

1. **Bake-off scope:** run OpenClaw + Hermes only in the first round, or include Odysseus immediately despite G-P3 unknown?
2. **Windows deployment preference:** native host runtime with sandboxed action subprocesses vs WSL2/container-centric runtime where each candidate supports it?
3. **Browser-account policy:** which subscription providers/accounts may be used in the bake-off and what challenge/logout behavior is an automatic stop?
4. **Artifact transfer requirement:** is browser download/upload a hard requirement for UF-A first release, or can initial execution be text-capture only?
5. **Personal-flow scope:** include UF-F in the first platform decision or treat it as a second trust-profile phase after project flows are proven?
6. **Resource thresholds:** what peak RAM/CPU/interactivity or foreground development degradation is unacceptable?
7. **Maintenance threshold:** how much candidate-specific patching/configuration per upgrade is too much before preferring custom adapters?
8. **Bake-off winner rule:** pure hard-gate + minimum intervention threshold, or add an explicit minimum advantage required to justify a more complex runtime?

No implementation should begin until the operator composition Q&A locks these decisions and authorizes a bake-off/build step.

---

## 16. Validation summary

- Same six flows compared: **yes**.
- Same six hard gates compared: **yes**.
- Evidence versions/freshness visible: **yes**.
- Candidate contradictions preserved and converted to tests: **yes**.
- FEE-retained authority named explicitly: **yes**.
- Windows/resource claims kept distinct from measurements: **yes**.
- Minimal bake-off includes hostile-source, auth, multi-root, resume, blocked-job, evidence and resource fixtures: **yes**.
- Recommendation is a bake-off priority, not implementation authorization: **yes**.

---

## 17. Machine-readable result

```yaml
platform_synthesis_result:
  evidence_date: 2026-08-08
  candidate_reports:
    - PLATFORM-RESEARCH-OPENCLAW-2026-08-08-V2-RESULT.md
    - PLATFORM-RESEARCH-HERMES-2026-08-08-V2-RESULT.md
    - PLATFORM-RESEARCH-ODYSSEUS-2026-08-08-V2-RESULT.md
  report_versions_or_commits:
    OpenClaw:
      release: v2026.7.1-2
      main: c5d00cb47ddb7236980de8e0fbc938b23fdeaae0
      weighted_score: 84.4
    Hermes:
      release: "v0.20.0 / tag v2026.8.3"
      main: 973c14b57c10874138b9696a2b300cc2f89e40e3
      weighted_score: 81.3
    Odysseus:
      dev: e4fa4ae5dd1d709ce4168397bd1d200fec1b2494
      weighted_score: 75.8
    FEE:
      state: "candidate; nothing built"
  hard_gate_summary:
    authority_containment:
      OpenClaw: PASS_WITH_EXTERNAL_BROKER
      Hermes: PASS_WITH_EXTERNAL_BROKER
      Odysseus: PASS_WITH_EXTERNAL_BROKER
    job_scoped_permissions:
      OpenClaw: PASS_WITH_EXTERNAL_BROKER
      Hermes: PASS_WITH_EXTERNAL_BROKER
      Odysseus: PASS_WITH_EXTERNAL_BROKER
    resumability:
      OpenClaw: PASS
      Hermes: PASS_WITH_EXTERNAL_BROKER
      Odysseus: UNKNOWN
    evidence_capture:
      OpenClaw: PASS
      Hermes: PASS
      Odysseus: PASS_WITH_EXTERNAL_BROKER
    safe_escalation:
      OpenClaw: PASS_WITH_EXTERNAL_BROKER
      Hermes: PASS_WITH_EXTERNAL_BROKER
      Odysseus: PASS_WITH_EXTERNAL_BROKER
    practical_windows_viability:
      OpenClaw: PASS
      Hermes: PASS
      Odysseus: PASS
  per_user_flow_comparison:
    UF-A:
      leader: OpenClaw
      scores: {OpenClaw: 88, Hermes: 84, Odysseus: 68}
    UF-B:
      leader: Hermes
      scores: {OpenClaw: 85, Hermes: 88, Odysseus: 82}
    UF-C:
      leader: OpenClaw
      scores: {OpenClaw: 93, Hermes: 90, Odysseus: 87}
    UF-D:
      leader: Hermes_Odysseus_tie
      scores: {OpenClaw: 83, Hermes: 84, Odysseus: 84}
    UF-E:
      leader: OpenClaw
      scores: {OpenClaw: 91, Hermes: 76, Odysseus: 73}
    UF-F:
      leader: Odysseus
      scores: {OpenClaw: 79, Hermes: 78, Odysseus: 82}
  composition_scores:
    fee_openclaw_runtime_separated_openclaw_doctrine: 86
    fee_hermes_runtime_openclaw_doctrine: 82
    fee_odysseus_runtime_openclaw_doctrine: 75
    custom_fee_provider_browser_adapters: 77
    fee_specialized_runtime_per_flow: 70
    fee_openclaw_browser_plus_secondary_local_runtime: 74
  score_confidence:
    recommended: 84
    runner_up: 80
    Odysseus_general_runtime: 72
    custom_executor: 68
  contradictions:
    - "Hermes stale Unix/WSL wording vs current native Windows guide; resolved in favor of current specific Windows evidence, local test still required."
    - "Browser feature presence is not authenticated subscription reliability; all candidates require common fixture."
    - "Odysseus file-workspace confinement is not general process sandboxing."
    - "OpenClaw native resume is strongest documented evidence, but FEE checkpoint remains canonical."
    - "All prompt-injection protections remain defense-in-depth; captured content must have structural zero authority through FEE."
    - "No platform has operator-machine resource measurements yet."
  recommended_architecture_hypothesis: "FEE deterministic authority/evidence spine + hardened OpenClaw runtime subset + authority-separated selected OpenClaw Detective/KB/hygiene/routing doctrine"
  runner_up_architecture: "FEE deterministic authority/evidence spine + Hermes bounded Docker-backed tool/browser/session runtime + selected OpenClaw doctrine"
  reusable_components:
    - OpenClaw Detective/KB/hygiene/routing doctrine
    - OpenClaw sandbox/browser/session/audit patterns
    - Hermes Docker terminal + profile tool-HOME patterns
    - Hermes signed lifecycle/tool-event pattern
    - Odysseus fail-closed plan-mode allowlist
    - Odysseus central workspace resolver and confinement tests
    - Odysseus untrusted-context wrapper as defense-in-depth
    - FEE frozen work packet/action schema/root compiler/checkpoint/evidence spine
  rejected_compositions:
    - raw autonomous candidate platform as FEE
    - three-runtime production architecture before evidence requires it
    - full custom executor before platform bake-off
    - Odysseus as first general runtime while resumability is UNKNOWN
    - OpenClaw doctrine as low-level execution authority
  required_bakeoff_tests:
    - authenticated subscription prompt/capture/session continuity
    - logout/CAPTCHA/security stop
    - hostile-source zero-authority
    - bounded script recovery and unauthorized-action rejection
    - read-only Detective evidence
    - bounded KB/data hygiene
    - multi-root rw/ro/forbidden containment for file and process tools
    - personal/project trust separation
    - restart/resume idempotency
    - blocked overnight job plus independent safe continuation
    - event/provenance reconstruction
    - Windows resource coexistence
    - human intervention and Claude Code/Codex escalation accounting
  resource_unknowns_to_measure:
    - peak RAM with runtime + browser + local model + normal dev workload
    - CPU contention and foreground responsiveness
    - Arc 140V/shared-memory utilization
    - browser/runtime crash rate
    - local-model latency for bounded action selection
    - Docker/WSL overhead where used
  operator_questions_remaining:
    - first-round candidates: OpenClaw+Hermes only vs include Odysseus
    - native Windows vs container/WSL deployment preference
    - subscription providers/accounts allowed in bake-off
    - browser artifact-download requirement for first release
    - UF-F inclusion in first platform decision
    - acceptable resource thresholds
    - acceptable upgrade/maintenance burden
    - explicit bake-off winner rule
  reversal_triggers:
    - Hermes materially beats OpenClaw on authenticated browser reliability/interventions/resources while passing gates
    - OpenClaw cannot close generic tool/exec bypass paths
    - OpenClaw release churn repeatedly breaks FEE adapter
    - both OpenClaw and Hermes fail containment/resume/browser reliability, favoring custom FEE adapters
    - Odysseus proves durable resume and stronger browser/process containment than desk evidence
    - specialized runtime wins a flow class by enough margin to justify another production interface
  overall_confidence_0_to_100: 84
```
