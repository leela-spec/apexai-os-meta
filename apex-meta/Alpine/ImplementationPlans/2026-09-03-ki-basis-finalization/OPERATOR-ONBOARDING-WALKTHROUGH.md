# KI Basis — Compact Operator Next Steps

**Goal:** finish the usable local platform without reloading implementation history and without building the final product skills yet.

Read first:

1. `ki-basis/CURRENT-STATE.md`
2. `ki-basis/AGENT-OPERATING-CONTEXT.md`

Open deeper files only when the active step requires them.

## Step 0 — Reconcile Git safely

Why: local bridge work was previously reported while remote `main` also advanced.

Agent actions:

- inspect branch, local HEAD, `origin/main`, ahead/behind, working tree;
- identify whether the bridge changes already exist locally;
- preserve unrelated dirty files and newer remote work;
- never force-push or auto-reset.

PASS when local/remote state is understood and the smallest safe sync action is explicit.

## Step 1 — Configure OpenRouter in Hermes

Why: Hermes needs its own provider for routing/tool execution; the upstream CLI agent can still do heavier reasoning separately.

Operator gate:

```powershell
docker exec -it ki-basis-hermes /opt/hermes/.venv/bin/hermes model
```

Operator selects OpenRouter, enters the key locally, selects a current tool-capable model, then reports only `provider configured`.

Agent verifies without exposing the key:

- provider = OpenRouter;
- selected model name;
- one non-sensitive call through `ki-basis/scripts/invoke-hermes.ps1` succeeds.

## Step 2 — Make KI Basis on-demand

Why: the seven-service server stack materially affects laptop responsiveness when left running.

Do one A/B check only:

1. with stack running, record `docker stats --no-stream` + basic Windows CPU/RAM;
2. gracefully stop KI Basis and Docker Desktop;
3. compare after a short wait.

If laptop pressure materially improves:

- Docker sign-in autostart -> off;
- Dashboard autostart -> off;
- Hyper-V backend retained;
- Compose restart policies retained;
- create/use `start-ki-basis.ps1` and `stop-ki-basis.ps1` only if not already present;
- verify one `stopped -> start -> verify -> stop` cycle.

If it does not materially improve, STOP with evidence. Do not tune services speculatively.

## Step 3 — Prove agent orientation

Use one intended CLI agent.

Prompt it to read:

`C:\GitDev\apexai-os-meta\ki-basis\AGENT-OPERATING-CONTEXT.md`

and, because setup status matters now:

`C:\GitDev\apexai-os-meta\ki-basis\CURRENT-STATE.md`

It must correctly state:

- seven services;
- `CLI -> Hermes -> real skills -> apps` boundary;
- major forbidden shortcuts;
- current runtime state.

Then let it perform one safe task such as runtime health inspection or a non-sensitive Hermes call.

## Step 4 — Seed tiny manual app fixtures

Purpose: give future real skills known real objects to test against without creating temporary API automation.

- Paperless (`127.0.0.1:8010`): upload 1–2 harmless PDFs; prove OCR/search; optionally tag `KI-BASIS-TEST`.
- Firefly (`127.0.0.1:8086`): create clearly fake `KI BASIS TEST` account/category/transaction.
- OpenProject (`127.0.0.1:8082`): create `KI Basis Test Project` + 1–2 harmless work packages.

Use normal UIs. No sensitive real data is required.

## Step 5 — Close this phase

Verify only the essentials:

- seven-service runtime starts successfully;
- Hermes API auth still rejects missing/wrong key and accepts valid key;
- OpenRouter-backed non-sensitive Hermes call succeeds;
- Postgres/Valkey remain internal-only;
- Hermes has no Docker socket;
- on-demand stop returns laptop resources and preserves data;
- canonical agent context is usable;
- each application has a harmless test fixture.

Then inspect Git status/diff, commit only bounded changes, and push only if operator explicitly authorizes it.

Return one status:

`PASS | PASS_WITH_LIMITATIONS | CORRECTION_REQUIRED | BLOCKED_HUMAN_GATE | FAIL`

STOP. Do not start the real Hermes product-skill phase.
