# Module 05A — CLI Reasoning -> Hermes Routing Bridge

**Status:** NEXT ESSENTIAL CAPABILITY

## 1. Architecture decision

The final product skill sets will be supplied later.

Do not build placeholder Firefly/Paperless/OpenProject skills now.

The canonical future control path is:

```text
Operator
-> heavy-reasoning CLI agent
-> Hermes local API server
-> Hermes routing / skill system
-> final product skills (later)
-> Firefly / Paperless / OpenProject
```

This prevents two competing application-control logics.

Direct localhost product APIs remain available for infrastructure testing and manual debugging, but local reasoning agents should not make them their permanent primary control interface once Hermes skills exist.

## 2. What "CLI agent powers Hermes" means

The external CLI agent is the **upstream planner/reasoner**. It can:

- perform deep reasoning;
- decide what operation is needed;
- reduce/structure context;
- send a bounded task to Hermes;
- consume Hermes' result and continue reasoning.

Hermes remains the **local execution/routing agent**. It still needs its own inference provider to interpret the bounded request, select/load skills, run tools, and formulate the execution result.

Current Hermes does not expose a generic "use this external CLI session's hidden reasoning as my model" interface. Do not claim that the CLI agent literally replaces Hermes' model.

If a future CLI/runtime exposes a provider interface Hermes natively supports (OpenAI-compatible endpoint, supported ACP/provider, etc.), that can be evaluated later.

## 3. OpenRouter role

OpenRouter will be configured now because the operator intends to use it.

Its role in this architecture is:

- Hermes routing/tool-execution inference;
- flexible model selection;
- fallback/provider experimentation.

It is **not** the only possible reasoning brain for KI Basis.

The upstream CLI agent may use its own model/provider independently.

Do not hard-code one OpenRouter model in repository authority. Configure provider/model interactively through Hermes and keep selection changeable.

## 4. Hermes local API server — canonical bridge

Enable Hermes' official OpenAI-compatible API server on the already-published host port `127.0.0.1:8642`.

Required container settings:

- `API_SERVER_ENABLED=true`
- `API_SERVER_HOST=0.0.0.0` inside the container so Docker port publishing reaches it
- `API_SERVER_KEY` from ignored host `.env`
- no CORS allowlist unless a browser client is deliberately added

The host publication remains loopback-only:

`127.0.0.1:8642:8642`

The API server is the stable machine-to-machine bridge for future CLI agents.

## 5. Secrets

Two secret classes stay separate:

### Hermes bridge credential

`HERMES_API_SERVER_KEY`

Stored in ignored `ki-basis/.env`, injected into the Hermes container as `API_SERVER_KEY`, and used by local CLI clients to authenticate to Hermes.

### Hermes inference/provider credentials

Example: `OPENROUTER_API_KEY`.

Configured interactively inside Hermes and persisted under `/opt/data`. Do not duplicate this key into host `ki-basis/.env` unless Hermes' supported provider flow explicitly requires it.

The existing backup deliberately excludes Hermes `/opt/data/.env`; preserve that behavior.

## 6. Operator gate — OpenRouter

Antigravity prepares the running Hermes container, then asks the operator for the smallest action:

1. create/select the dedicated OpenRouter key outside chat;
2. run the Hermes provider setup interactively inside the container;
3. enter the key only in Hermes' local secure setup;
4. select a tool-capable model appropriate for routing/execution;
5. run one non-sensitive test prompt.

Do not request the key in Antigravity/chat/evidence.

## 7. Local CLI bridge helper

Create one deterministic host-side script:

`ki-basis/scripts/invoke-hermes.ps1`

Purpose:

- read `HERMES_API_SERVER_KEY` from ignored `ki-basis/.env`;
- call `http://127.0.0.1:8642/v1/chat/completions`;
- send one supplied prompt;
- return Hermes' response;
- never print the key;
- fail non-zero on missing key, HTTP failure, or malformed response.

It is a transport adapter only. It must contain no Firefly/Paperless/OpenProject business logic.

Future CLI-agent skills can call this bridge rather than implementing a second product-access stack.

## 8. Current proof

Before the final product skills exist, prove:

1. Dashboard closed;
2. Hermes API server responds through loopback;
3. API request without/wrong `HERMES_API_SERVER_KEY` is rejected;
4. bridge helper with valid key succeeds;
5. Hermes provider responds to a non-sensitive prompt;
6. existing stack verifier still proves application/network/auth boundaries.

Do not claim product-operation-via-Hermes until the real skills are installed later.

## 9. Privacy routing — important limitation

A CLI agent doing heavy reasoning upstream does **not** automatically keep application data out of Hermes' model provider.

When Hermes executes a skill and receives sensitive product output, that output can become part of Hermes' model context and therefore may be sent to the configured provider.

Therefore:

- do not label OpenRouter mode "private";
- send only bounded/minimized task context to Hermes where possible;
- before genuinely sensitive workflows, define a Hermes profile/provider whose data-handling policy the operator accepts;
- keep the same Hermes skill/routing architecture across profiles rather than creating a second product-access logic.

A future privacy profile is the preferred extension point. Fully local models are currently deferred because prior attempts were not satisfactory.

## 10. Final skills later

When the real skill set arrives:

- install/review those skills inside Hermes;
- create the `ki-basis-control` bundle over the real skills;
- run cross-application proofs;
- add selected write workflows with approval/read-after-write where needed.

Do not build placeholders now.

## Acceptance

PASS for this phase when:

- Docker runs background/CLI-first with Dashboard closed;
- OpenRouter/provider is configured in Hermes;
- Hermes official API server is authenticated and loopback-only;
- `invoke-hermes.ps1` works;
- upstream CLI agents have one canonical machine interface to Hermes;
- no duplicate product-control implementation is introduced;
- final skills remain explicitly deferred.
