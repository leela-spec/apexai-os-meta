# R01 — Hermes Local Safety Guardrails Research

Status: **RESEARCH REQUIRED / PRE-INSTALL**  
Priority: **P0 — blocks installation**  
Decision owner: Human CEO

## Decision question

Which **official Hermes security configuration** gives strong protection on the operator's local Windows/WSL environment while still allowing normal Master of Arts work to run without constant approval friction or an over-engineered policy layer?

The answer must use Hermes' existing security mechanisms. Do not design a new guardrail framework.

## Hard constraints

- no custom security daemon;
- no custom command parser;
- no bespoke permissions engine;
- no blanket `--yolo` or approvals-off configuration on the host;
- no security profile that makes ordinary repo edits, Git work, QMD search, Kanban work or approved scripts practically unusable;
- no claim based only on model memory;
- prefer official Hermes documentation/repository and official Docker/Windows/WSL documentation when needed.

## Current verified upstream mechanisms to investigate

Official Hermes documentation currently describes:

- dangerous-command detection and approval modes;
- user-configurable `approvals.deny` rules;
- `HERMES_WRITE_SAFE_ROOT` for file-write tools;
- local, Docker, SSH and other terminal backends;
- Docker hardening and resource limits;
- environment/credential filtering;
- MCP environment filtering;
- context-file prompt-injection scanning;
- gateway allowlists/DM pairing;
- denial circuit breaker;
- security guidance specifically for personal/work machines.

Primary sources:

- https://hermes-agent.nousresearch.com/docs/user-guide/security/
- https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine
- https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- https://hermes-agent.nousresearch.com/docs/user-guide/features/tools/
- https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime
- https://hermes-agent.nousresearch.com/docs/getting-started/platform-support

## Research tasks

### 1. Threat model for this actual use case

Classify risks by consequence and likelihood:

- accidental destructive filesystem command;
- unintended modification outside MasterOfArts;
- destructive Git history operation;
- credential/API-key exposure;
- arbitrary remote download/pipe-to-shell execution;
- malicious/untrusted skill;
- malicious project context/prompt injection;
- unwanted remote user controlling Hermes through gateway/messaging;
- runaway process/resource use;
- QMD/MCP exposing data beyond localhost;
- normal AI mistakes that are non-destructive and should not create approval friction.

Do not treat every terminal command as equally dangerous.

### 2. Compare official execution profiles

Compare at minimum:

A. local terminal backend + manual dangerous-command approval;
B. local terminal backend + smart/default approval + explicit deny rules;
C. Docker terminal backend with project workspace mounted/available;
D. WSL2 + Docker or other officially supported isolation path if relevant.

For each report:

| Profile | Host isolation | File access | Git usability | QMD usability | Credential exposure | Approval burden | Windows/WSL support | Maintenance | Verdict |
|---|---|---|---|---|---|---|---|---|---|

### 3. Determine the recommended baseline

The recommendation must specify only official settings/mechanisms, including where appropriate:

- `approvals.mode`;
- `approvals.deny`;
- whether to use `command_allowlist` and under what rule;
- `HERMES_WRITE_SAFE_ROOT` or equivalent write restriction;
- terminal backend;
- container mounts/workspace persistence;
- `docker_forward_env` and credential-file behavior;
- gateway user allowlists/pairing if gateway is enabled;
- network exposure rules for local MCP/QMD;
- whether computer-use/browser features should be disabled unless specifically needed;
- backup/rollback prerequisites before allowing write operations.

Do not add settings just because they exist. Every recommended restriction needs a named risk it mitigates.

### 4. Allowed-work simulation

Prove the proposed safety profile permits these workflows:

1. Hermes reads an existing project file.
2. Hermes edits an approved project file.
3. Hermes runs a deterministic local validation script.
4. Hermes queries QMD.
5. Hermes creates/updates Kanban task state.
6. Hermes performs `git status`, `git diff`, `git add`, `git commit`.
7. Hermes performs an ordinary push only when the workflow/operator authorizes it.
8. Hermes uses approved model credentials without exposing unrelated secrets.

For every step record:

`operation | official control encountered | human approval needed? | expected friction | pass/fail`

### 5. Blocked-work simulation

Test on paper using official behavior:

- recursive destructive delete outside the approved project;
- disk/device write;
- `curl | sh` or equivalent remote pipe-to-shell;
- force push;
- reading/exporting credentials not required by the task;
- writing outside the approved workspace through write-file tools;
- an unapproved messaging user issuing a command;
- QMD HTTP server accidentally bound beyond localhost without authentication.

Record whether each is:

`hard blocked | approval gated | container-isolated | not protected by this mechanism | requires another official setting`.

### 6. Skills security

Verify current Hermes behavior for:

- project skill trust;
- Skills Guard/security scan;
- hub-installed vs project/local skills;
- writable external skill directories;
- which skill types the Curator can mutate;
- how to keep approved BMAD/MarketingSkills from unwanted autonomous mutation using existing supported controls.

## Required output

Produce:

1. plain-language threat model;
2. official-control matrix;
3. recommended Hermes safety profile;
4. exact verified config/commands with source links;
5. allowed-work test matrix;
6. blocked-work test matrix;
7. remaining risks that Hermes itself does not prevent;
8. operational friction estimate;
9. rollback/recovery notes;
10. decision: `SAFETY_PROFILE_CONFIRMED` or `BLOCKER`.

## Pass standard

Pass only if the configuration protects the real host/data risks while the normal Master of Arts execution path remains practically usable.

A profile that is extremely restrictive but prevents the target workflows is **not a pass**. A profile that is convenient but leaves obvious destructive/credential risks uncontrolled is also **not a pass**.
