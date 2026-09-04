# KI Basis — Operator Onboarding & Guided Setup Walkthrough

**Audience:** operator + Antigravity coordinator.  
**Mode:** interactive coaching, one bounded step at a time.  
**Goal:** finish the usable KI Basis platform **without** inventing the final product skills yet.

## 1. What we are doing

We already built the hard infrastructure. This walkthrough turns that infrastructure into a usable operator environment and leaves it ready for the real Hermes skill set later.

The current target is:

```text
Operator
  -> heavy-reasoning CLI agent
  -> authenticated Hermes localhost API
  -> Hermes provider-backed routing/tool execution
  -> real Hermes skills later
  -> Firefly / Paperless / OpenProject
```

The important near-term outcome is **not** "automate everything." It is:

1. the stack starts and stops reliably on a laptop;
2. Hermes has a real provider (OpenRouter for now);
3. CLI agents know exactly what environment they are operating in;
4. the applications contain a little real test data so later skills can be proven against actual objects;
5. no second/parallel product-control architecture is created before the real skills arrive.

## 2. Why this walkthrough exists

Several issues during implementation matter for how we operate the system now:

### Docker Desktop confusion

The Dashboard was repeatedly opened/restarted during testing, which made it look as if Docker Desktop had to stay visibly running. It does not.

The current Windows architecture still uses Docker Desktop's **background Hyper-V runtime**, because the Linux Docker Engine lives in its managed Linux VM. The Dashboard is optional.

For a laptop, the preferred normal state is now **on-demand**:

```text
not using KI Basis
-> stack stopped
-> Docker Desktop stopped

need KI Basis
-> start Docker Desktop in background
-> start stack
-> work
-> gracefully stop stack
-> stop Docker Desktop
```

Do not migrate to a manual Linux VM merely to save resources before this simpler operating model is tested.

### Hermes lifecycle workaround was corrected

A temporary `command: sleep infinity` workaround was tried because the Hermes container exited under one detached execution path. Follow-up verification showed that the official Hermes path `command: gateway run` works correctly and internally produces the supervised heartbeat. Keep the official path.

### Antigravity/Docker process ownership

A transient WMI detachment technique was used so Docker Desktop would survive an Antigravity runner Job Object. It did not become a persistent service/task/startup mechanism. Do not make Antigravity responsible for owning Docker Desktop's lifetime.

### OpenRouter is still a human secret gate

Hermes inference has worked through another configured provider, but the intended OpenRouter provider still requires the operator to enter a private key interactively. No agent should request or receive the raw key in chat.

### Product skills are intentionally deferred

The real Paperless/Firefly/OpenProject skill set will arrive later. We therefore do **not** create placeholder product skills or product-specific CLI wrappers now.

The system should be ready to receive the real skills without migration or duplicate logic.

## 3. Canonical files for this run

Before doing anything, read:

1. `ki-basis/AGENT-OPERATING-CONTEXT.md`
2. `ki-basis/AGENTS.md`
3. `apex-meta/Alpine/ARCHITEKTUR-BASIS.md`
4. current `ki-basis/compose.yaml`

Antigravity also reads its own current best-practice authority:

- `apex-meta/SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/SKILL.md`
- `.../references/lessons-learned.md`
- `.../references/prompt-patterns.md`

For every step, live local runtime evidence outranks stale chat/report text.

---

# COACHING METHOD

Antigravity acts as a **coach + bounded executor**, not as a silent monolithic installer.

For each phase:

1. explain in 2–5 sentences what the phase changes and why;
2. inspect current state;
3. tell the operator what will happen next;
4. execute safe machine actions when authorized;
5. ask for the smallest exact operator action when a secret/UI/account decision is required;
6. verify the real result;
7. summarize PASS/limitation before moving on.

Do not dump the entire workflow at the operator and disappear into long uncontrolled automation.

Do not self-update, uninstall, move, or repair Antigravity/Claude/Codex itself as part of this workflow.

---

# PHASE 0 — RECONCILE CURRENT LOCAL/REMOTE STATE

## Purpose

There has been local bridge work plus newer unrelated remote commits. We must preserve both rather than overwrite one with the other.

A previous report named local bridge commit:

`b336aca1cb70b5143ed1deb0b56986925f66d8e2`

Do **not** trust that as current until inspected.

## Antigravity actions

Inspect:

- current branch;
- local HEAD;
- `origin/main`;
- ahead/behind relationship;
- working tree;
- changed files in any local bridge commit;
- unrelated dirty files.

Expected bridge scope from the previous report included only:

- `apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/04A-DOCKER-BACKGROUND-RUNTIME.md`
- `apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/05A-CLI-REASONING-HERMES-ROUTING.md`
- `ki-basis/.env.example`
- `ki-basis/compose.yaml`
- `ki-basis/scripts/invoke-hermes.ps1`

If local and remote diverged only through unrelated commits, rebase/merge safely according to actual state. Never force-push over newer remote work.

Do not include unrelated dirty files in KI Basis commits.

## PASS

- local current work is understood;
- bridge work is preserved;
- current remote work is preserved;
- no destructive reset/stash performed automatically.

---

# PHASE 1 — COMPLETE OPENROUTER IN HERMES

## Purpose

The upstream CLI agent can use its own model/provider for heavy reasoning. Hermes still needs its own provider for routing/tool execution.

OpenRouter is the intended first Hermes provider because it gives flexible model choice later without changing the skill architecture.

## Human gate

Antigravity prepares the running Hermes container and then asks the operator to run locally:

```powershell
docker exec -it ki-basis-hermes /opt/hermes/.venv/bin/hermes model
```

The operator:

1. selects OpenRouter;
2. enters the OpenRouter key **inside the local Hermes prompt**;
3. selects a current tool-capable routing/execution model;
4. tells Antigravity only: `provider configured`.

No API key is pasted into chat, reports, logs, tracked `.env`, screenshots, or evidence.

## Verification

Without exposing the key, prove:

- provider = OpenRouter;
- credential configured;
- selected model name visible/sanitized;
- one non-sensitive `invoke-hermes.ps1` request succeeds through the actual Hermes API.

Do not call a generic Hermes `pong` proof sufficient if provider identity is not verified.

## PASS

```text
Windows CLI
-> authenticated Hermes localhost API
-> Hermes
-> OpenRouter
-> successful response
```

---

# PHASE 2 — PUT KI BASIS INTO LAPTOP-FRIENDLY ON-DEMAND MODE

## Purpose

The stack is a small server environment. OpenProject, Paperless, PostgreSQL, Hermes and the Linux VM should not consume laptop resources all day when unused.

Do not tune individual services until the simpler operating model is proven.

## A. Measure once before changing behavior

With the stack running but no intentional workload, capture a compact baseline:

- `docker stats --no-stream`;
- Windows total CPU/RAM;
- obvious Docker/VM process pressure;
- disk activity only if materially high.

No monitoring stack. No long benchmark campaign.

## B. Graceful stop and compare

Stop KI Basis cleanly with a generous timeout, then stop Docker Desktop through its supported CLI.

Wait briefly and compare Windows responsiveness/CPU/RAM.

If there is **no material improvement**, stop and report that evidence before inventing service tuning.

If the laptop materially improves, adopt on-demand operation.

## C. Settings target

- Docker Desktop sign-in autostart: **off**;
- Dashboard autostart: **off**;
- Hyper-V Linux backend retained;
- Resource Saver retained/enabled where applicable;
- Compose `restart: unless-stopped` retained;
- no CPU/RAM ceilings yet.

## D. Operator lifecycle scripts

If not already present, create exactly two small scripts:

- `ki-basis/scripts/start-ki-basis.ps1`
- `ki-basis/scripts/stop-ki-basis.ps1`

### Start behavior

1. start Docker Desktop detached/background;
2. bounded wait for engine readiness;
3. start current Compose project;
4. wait for service readiness;
5. verify key surfaces;
6. return clear PASS/FAIL.

### Stop behavior

1. gracefully stop full Compose project with a generous shutdown timeout (about 60 seconds unless evidence suggests otherwise);
2. verify containers stopped;
3. stop Docker Desktop;
4. preserve containers, volumes, images and data;
5. return clear PASS/FAIL.

No `down -v`, no volume deletion, no image deletion.

## E. Lifecycle proof

Run one complete:

`stopped -> start -> verify -> stop`

cycle.

Then repeat once if needed to prove reliability, not endlessly.

## PASS

Normal laptop state can be Docker/KI Basis off, with a reliable explicit start/stop path when needed.

---

# PHASE 3 — ORIENT THE LOCAL CLI AGENTS

## Purpose

Before product skills exist, agents still need to know what they are touching so they do not create unsafe shortcuts.

The canonical source is:

`ki-basis/AGENT-OPERATING-CONTEXT.md`

The thin scoped adapter is:

`ki-basis/AGENTS.md`

Do not create several independent KI Basis manuals for Claude, Codex and Antigravity.

## Invocation pattern

For an agent that does not automatically discover `AGENTS.md`, the operator uses:

```text
Read and obey:
C:\GitDev\apexai-os-meta\ki-basis\AGENT-OPERATING-CONTEXT.md

Treat it as the canonical KI Basis operating context.
Do not create alternative product-control logic.
Inspect current state first.

Task: <task>
```

## Agent smoke test

Use one local CLI agent and ask it to:

1. read the context;
2. summarize the seven services and the canonical `CLI -> Hermes -> skills -> apps` boundary;
3. state what it must never do;
4. inspect whether KI Basis is currently running;
5. call Hermes through the existing generic bridge with a non-sensitive prompt.

It must **not** create product-specific automation during this test.

## PASS

The agent understands the environment before touching it and uses Hermes as the future product-control boundary.

---

# PHASE 4 — MANUAL APPLICATION SMOKE TESTS + SMALL TEST DATA

## Purpose

Later skills need real application objects to prove they work. The fastest safe path now is to seed each application manually through its normal UI rather than invent temporary API automation.

Use clearly labeled non-sensitive test data that can be deleted later.

## A. Paperless-ngx

Open:

`http://127.0.0.1:8010`

Coach the operator to:

1. log in;
2. upload 1–2 harmless test PDFs (for example a public/manual/test document, not sensitive personal material);
3. wait for OCR/ingestion completion;
4. confirm the documents are searchable;
5. inspect title/date/tags/correspondent fields;
6. optionally add a simple test tag such as `KI-BASIS-TEST`.

Do not optimize OCR workers during this test unless an actual performance problem is measured.

Record only object names/IDs needed for later verification—never document contents containing sensitive data.

## B. Firefly III

Open:

`http://127.0.0.1:8086`

Coach the operator to create only a minimal safe test set, for example:

- one clearly named test asset account;
- one test category/budget if useful;
- one small fictitious test transaction.

Use unmistakable labels such as `KI BASIS TEST` so later skill verification cannot accidentally act on real finance data.

Do not generate an API token unless the operator wants to prepare the future skill prerequisites now. Missing `FIREFLY_API_TOKEN` is not a blocker for manual smoke testing.

## C. OpenProject

Open:

`http://127.0.0.1:8082`

Coach the operator to create:

- one project named similar to `KI Basis Test Project`;
- one or two harmless work packages;
- optionally one status/assignee/date change so later read/write skill tests have concrete state.

Do not install plugins or upgrade OpenProject.

Missing `OPENPROJECT_API_KEY` is not a blocker for manual smoke testing.

## D. nginx / Hermes

Confirm:

- nginx health surface works;
- Hermes dashboard/API still works;
- no new ports were exposed.

## PASS

Each application is usable manually and contains a tiny, clearly labeled test fixture for future skill integration.

---

# PHASE 5 — SAFE CLI-AGENT PRACTICE WITHOUT FINAL PRODUCT SKILLS

## Purpose

We want the operator to become comfortable using local CLI agents with KI Basis **without** creating throwaway product integrations.

Good tasks now:

- "Start KI Basis and verify all services."
- "Read the KI Basis operating context and tell me which service is failing."
- "Run the backup verifier and explain the result."
- "Call Hermes with this non-sensitive reasoning/routing test."
- "Inspect the OpenProject container logs because the UI is returning 503."
- "Stop KI Basis cleanly when we are finished."

Do not yet normalize tasks like:

- "Create a Firefly transaction via your own curl script."
- "Tag this Paperless document through a temporary Claude script."
- "Create OpenProject work packages using an improvised direct API wrapper."

Those are exactly the behaviors the future Hermes skills should own.

## PASS

The operator can use CLI agents for runtime/diagnostic work while the application-control boundary remains reserved for the real Hermes skills.

---

# PHASE 6 — CLOSE THIS PHASE CLEANLY

Before declaring the onboarding/platform phase done:

1. run the current stack verifier;
2. verify Hermes bridge auth: missing/wrong key denied, valid key works;
3. verify OpenRouter provider/model without exposing secret;
4. verify one start/stop lifecycle;
5. verify Postgres/Valkey remain internal;
6. verify Hermes has no Docker socket;
7. verify `AGENT-OPERATING-CONTEXT.md` is present and usable;
8. verify Paperless/Firefly/OpenProject each have a harmless manual test fixture;
9. inspect Git diff/status;
10. preserve unrelated work;
11. commit only bounded onboarding/runtime changes;
12. push only if operator explicitly authorizes it.

## Final result

Return one:

- `PASS`
- `PASS_WITH_LIMITATIONS`
- `CORRECTION_REQUIRED`
- `BLOCKED_HUMAN_GATE`
- `FAIL`

Then STOP.

Do **not** start implementing final product skills in this run.

---

# FUTURE PHASE — WHEN THE REAL SKILL SET ARRIVES

This is intentionally not executed now.

The later target is:

```text
heavy-reasoning CLI agent
-> Hermes API
-> Hermes
-> ki-basis-control bundle
   -> Paperless real skill
   -> Firefly real skill
   -> OpenProject real skill
-> applications
```

At that time:

1. review the supplied skills against current product versions and safety boundaries;
2. install them in Hermes;
3. configure only the required product API credentials;
4. test each product skill individually with positive + denial proof;
5. create `ki-basis-control` over the proven real skills;
6. prove one cross-application workflow;
7. add selected write workflows only where the operator actually needs them, with preview/approval/read-after-write verification.

No architecture migration should be required if the current onboarding phase is completed correctly.
