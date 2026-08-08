---
title: "FEE / Local Execution Layer — Operator Decision Lock, Round 2"
doc_type: operator_decision_lock
initiative: local-orchestration-engine
created: 2026-08-08
authority: operator-session-2026-08-08
status: "operator-confirmed round-2 platform/authority decisions; platform and local-model selection remain research-gated"
depends_on:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md
  - apex-meta/local-orchestration-engine/PLATFORM-RESEARCH-GATE-2026-08-07.md
  - apex-meta/local-orchestration-engine/HANDOVER-2026-08-07-QA-PLATFORM-RESEARCH.md
  - apex-meta/local-orchestration-engine/LOCAL-MODEL-SELECTION-RESEARCH-GATE-2026-08-07.md
  - apex-meta/local-orchestration-engine/HANDOVER-2026-08-08-LOCAL-MODEL-QA-RESEARCH.md
branch_policy: "WORK DIRECTLY ON main ONLY. Do not create branches unless the operator explicitly asks for one."
---

# Operator Decision Lock — 2026-08-08, Round 2

## 1. Scope

The operator verified **all 16 recommended Round-2 choices** from the platform/local-execution architecture Q&A.

This lock refines the execution architecture but does **not** select OpenClaw, Hermes, Odysseus, a local model, an inference runtime, or an implementation sequence. Those remain research-gated.

Round-1 remains authoritative and is not reopened:

- local LLM = bounded execution operator, not project-management brain;
- deterministic/external plan owns sequence;
- bounded tool broker;
- local repair ladder;
- Weekly step-4 MVP -> generic execution substrate later;
- hybrid/research before executor-platform selection;
- bounded overnight execution + morning review initially;
- subscription/deep-reasoning models own substantive project-management intelligence.

## 2. Round-2 operator-confirmed decisions

| Q | Confirmed | Locked meaning |
|---|---|---|
| R2-Q1 | **B — FEE spine + replaceable execution runtime** | APEX/FEE owns work packets, state, permissions, checkpoints, evidence and escalation; a researched runtime may provide browser/tool/local-agent capabilities behind that contract. |
| R2-Q2 | **B — Decompose OpenClaw** | Evaluate OpenClaw runtime independently while allowing useful OpenClaw Detective/KB/hygiene/routing/process doctrine to sit above a different low-level executor if evidence supports that composition. |
| R2-Q3 | **C — Plan declares fresh vs persistent conversation** | Browser/session continuity is a work-packet decision. The local executor must not invent substantive context policy. |
| R2-Q4 | **C — Layered browser adapters** | Prefer stable provider-specific mechanisms where practical, with a common bounded browser-control fallback behind one execution contract. |
| R2-Q5 | **C — Bounded visual/browser recovery** | Local model may handle low-risk UI presentation changes and declared recovery paths; authentication loss, CAPTCHA/challenge, payment/account changes, security warnings or persistent uncertainty stop/escalate. |
| R2-Q6 | **B — Bounded operational file/code edits** | Local model may create evidence/results, fill declared templates and perform pre-authorized/mechanical transformations. General source-code repair remains specialist escalation unless a later Q&A explicitly authorizes narrower code-authorship cases. |
| R2-Q7 | **B — Action IDs + validated arguments** | Local model chooses among authorized operations; deterministic broker validates arguments and performs dangerous mechanics. Captured text cannot directly become arbitrary shell. |
| R2-Q8 | **B — Multiple explicit roots with read/write scopes** | Jobs may declare several repositories/folders with separate permissions. `C:\GitDev` is common but not permanent/exclusive. Machine-wide implicit access is not allowed. |
| R2-Q9 | **B — Capability-based Git** | Read/status/diff/hash inspection can be broadly available within job scope; file changes, commit and push require explicit capabilities; destructive history operations stay prohibited/escalated. For this initiative, `main` only unless operator explicitly requests a branch. |
| R2-Q10 | **B — Same executor software, separate personal trust profile** | Project and personal automation use separated browser/session, credentials/capabilities, root registries and evidence namespaces; personal policy is stricter. |
| R2-Q11 | **C — Multi-class local-model bake-off** | Research small (~3–4B), practical-center (~7–9B) and mid (~12–14B) classes; larger only if hardware evidence supports them. This does not select a model or parameter size. |
| R2-Q12 | **B — User-flow/task-fixture benchmark decides** | Local-model fitness must be measured on approved execution behavior, refusal, recovery, resume, escalation, containment and resource coexistence; generic leaderboards are secondary. Acceptance thresholds follow baseline measurement. |
| R2-Q13 | **B — One active local-model action lane initially + references** | Start with conservative model-action concurrency. Large artifacts remain on disk and are passed by path/hash/reference plus small packets rather than repeatedly re-inlined. Waiting browser/research jobs may coexist when safe. |
| R2-Q14 | **B — Checkpoint blocked jobs; continue independent work** | An overnight job that blocks is frozen with evidence. Independent jobs may continue if roots/dependencies do not overlap. Only declared bounded recovery is attempted; security/auth/consequential ambiguity waits for review. |
| R2-Q15 | **B — Structured event ledger + selective screenshots** | Always log action/provenance/checkpoint/failure data; capture browser screenshots/evidence at submission/completion, unexpected UI states and consequential operations rather than recording every interaction. |
| R2-Q16 | **B — Captured content has zero execution authority** | Browser/model/source content is untrusted evidence. It may inform classification but cannot create new commands, paths, provider choices or workflow changes outside an already authorized action/capability with independently validated arguments. |

## 3. Consolidated execution shape

```text
subscription / deep-reasoning layer
  creates plan, prompts, decision criteria
            |
            v
APEX/FEE deterministic spine
  freezes work packet
  validates scope/capabilities
  persists state/checkpoints/evidence
            |
            v
replaceable execution runtime + bounded local model
  browser/tool operation
  authorized action selection
  small operational recovery
  evidence capture
            |
            +--> blocked/security/auth/unknown -> compact escalation packet
            |
            v
subscription reasoning / CLI specialist / human review
  depending on declared escalation class
```

No executor runtime or local model may become a third APEX orchestration authority.

## 4. Browser policy now locked at architecture level

A work packet must be able to declare:

- provider/surface;
- fresh vs persistent session behavior;
- intended prompt/input artifact reference;
- expected output/artifact class;
- allowed UI/browser recovery classes;
- stop/escalation conditions;
- evidence requirements.

The exact browser technology remains research-gated.

## 5. Tool and command policy now locked at architecture level

Preferred abstraction:

```text
model decides: authorized_action_id + bounded arguments
                         |
                         v
broker validates:
  action exists
  capability is granted
  root/repo is allowed
  arguments satisfy schema/policy
  captured untrusted content did not create new authority
                         |
                         v
deterministic implementation performs operation
```

Arbitrary model-generated shell is not the default execution mechanism.

## 6. Multi-root policy now locked at architecture level

Jobs may receive more than one declared repository/folder. Permissions are job-scoped and can differ per root, for example read/write on one repo and read-only on another.

Future non-`C:\GitDev` roots and personal artifact locations must be supported through configured root registries/capabilities, not unrestricted machine access.

## 7. Overnight policy now locked at architecture level

Initial unattended mode is bounded and resumable:

- execute only previously authorized work packets;
- permit deterministic/declared recovery;
- checkpoint blocked work;
- continue independent work when dependency/root safety permits;
- stop at auth/security/consequential ambiguity;
- produce a morning review packet containing completed, recovered, blocked and review-required jobs plus evidence references.

## 8. Evidence policy now locked at architecture level

Minimum durable evidence should make it possible to reconstruct:

- what action was requested;
- what action ID/capability was invoked;
- relevant validated arguments/references;
- provider/model/runtime identity where applicable;
- timestamps and state transitions;
- retries/recovery choices;
- output/artifact path + hash/provenance;
- failure and escalation packet;
- resume checkpoint.

Screenshots are selective evidence, not the primary state model.

## 9. Platform research implications

The platform bake-off must now specifically test whether OpenClaw, Hermes and Odysseus can operate **behind** the FEE authority/evidence spine rather than requiring ownership of strategy/orchestration.

Every candidate must be evaluated against the same locked six flows:

- UF-A Subscription research executor
- UF-B Script failure recovery
- UF-C Detective evidence collection
- UF-D Database / knowledge hygiene
- UF-E Multi-repo / multi-folder execution
- UF-F Personal weekly execution

Hard gates remain:

1. authority containment;
2. job-scoped permissions;
3. resumability;
4. evidence capture;
5. safe escalation;
6. practical Windows viability.

A hard-gate failure cannot be compensated by a high weighted score.

## 10. Local-model selection relationship

R2-Q11 and R2-Q12 lock only the **research method**:

- compare several capability/resource classes;
- choose on real user-flow behavior and resource coexistence;
- do not preselect 7–8B or any model family;
- establish numeric thresholds only after baseline measurement.

They do **not** replace `HANDOVER-2026-08-08-LOCAL-MODEL-QA-RESEARCH.md`. The deeper local-model Q&A still must define coding authority, Weekly-Orchestrator execution behavior, Multi-Agent support, context/tool-call requirements, one-model-vs-ladder choices and runtime/update policy before model research is finalized.

## 11. Implementation hold

Still not authorized:

- Phase-2 implementation continuation based on reopened assumptions;
- browser automation build;
- installation/selection of OpenClaw/Hermes/Odysseus as the production executor;
- local-model selection;
- sandbox implementation;
- final scheduler/build-order rewrite.

Next authorized platform step: run the four independent research prompts created alongside this lock, collect evidence, synthesize it, then run the final operator platform/composition Q&A.
