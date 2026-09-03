# Module 05 — Hermes as the AI Control Stack

## Purpose

This is the main next capability.

The Docker platform already exists. This module makes Hermes the actual operator-facing AI that can inspect the three applications through reusable Hermes skills:

- Firefly III
- Paperless-ngx
- OpenProject

The user must be able to open Hermes locally, ask a normal-language question, have the matching skill execute against the real application, and receive a grounded result.

This module includes the LLM-provider bootstrap because Hermes cannot reason without a configured model provider.

---

## 1. Important conceptual distinction: local skills vs application authentication

Yes, Hermes can be a **local CLI agent executing local skills**.

That does **not** remove the need for application authentication.

The target runtime is:

```text
Windows operator
  -> Hermes CLI inside ki-basis-hermes
       -> Hermes skill
            -> local script/terminal call inside Hermes container
                 -> ki-basis-net
                      -> Firefly/Paperless/OpenProject supported API
```

The skill and script are local. The token is only the credential by which the application decides **which user/permissions the agent has**.

### Why not remove tokens?

The alternatives are worse:

1. **Docker socket + `docker exec` into sibling containers** — gives the agent control of the Docker daemon/host and destroys the current security boundary.
2. **Direct PostgreSQL writes** — bypass application validation, authorization, hooks, audit semantics, and schema invariants.
3. **Disable application authentication on the Docker network** — any compromised container could act as the user.
4. **Username/password in skill scripts** — exposes a more valuable long-lived credential; OpenProject explicitly recommends API/OAuth credentials instead of user passwords for API clients.
5. **Browser/session-cookie automation** — more brittle and less appropriate for headless recurring agent workflows.

Therefore the best-practice design is:

> local Hermes skills + supported local-network APIs + revocable least-privilege app credentials.

The open-source applications themselves do not "run with a token". They run normally. Only the Hermes client authenticates when it asks them to do something.

---

## 2. Credential classes — do not mix them

There are two completely different credential categories.

### A. Model provider credential

`OPENROUTER_API_KEY`

Purpose: Hermes -> OpenRouter -> chosen LLM.

It has nothing to do with Firefly/Paperless/OpenProject permissions.

### B. Application credentials

- `FIREFLY_API_TOKEN`
- `PAPERLESS_API_TOKEN`
- `OPENPROJECT_API_KEY`

Purpose: Hermes skill -> local application.

These never go to OpenRouter as raw values. The model should not see them at all.

---

## 3. OpenRouter setup — operator interaction

OpenRouter is not a local program that needs to be installed into the stack. It is a model API/provider that Hermes supports natively.

Hermes officially supports OpenRouter and expects `OPENROUTER_API_KEY` in its persistent Hermes `.env`.

### Phase 5A — operator gate

Antigravity prepares and verifies the running Hermes container, then asks the operator for exactly this action:

1. Open https://openrouter.ai/ and sign in.
2. Add credits if needed.
3. Create a dedicated key named e.g. `hermes-ki-basis`.
4. Set a conservative spend limit and optional expiry on the key.
5. In OpenRouter privacy settings, keep prompt/completion logging off unless deliberately needed for debugging.
6. Disable routing to providers that may train/store data where appropriate; for sensitive personal documents/finance/project data, prefer data-collection-deny / Zero Data Retention policy where available.
7. Do not paste the key into Antigravity or this chat.

Then, from Windows PowerShell, open the Hermes CLI in the **running Hermes container**:

```powershell
docker exec -it ki-basis-hermes /opt/hermes/.venv/bin/hermes model
```

Choose OpenRouter and enter the key into Hermes' own interactive setup.

The expected persistent location is `/opt/data/.env`, backed by `ki-basis-hermes-data`.

Do not pass the OpenRouter key as a command-line argument.

### Provider verification

Inside the Hermes CLI:

- run `hermes config check` if exposed by the installed version;
- verify OpenRouter is an available provider/model;
- start one fresh conversation and ask a non-sensitive test question;
- record only provider/model/status/cost metadata, never the key.

### Privacy consequence

When Hermes uses OpenRouter, any application data that Hermes includes in an LLM prompt may leave the laptop and be processed by OpenRouter/upstream model providers. The local APIs stay local; the language-model inference is cloud unless a local model provider is chosen later.

This is a separate privacy decision from Docker isolation.

---

## 4. Canonical skill architecture

Create **three separate version-controlled skills**, not one giant generic mutation skill.

Recommended repository location:

```text
ki-basis/hermes-skills/
  firefly-local/
    SKILL.md
    scripts/
  paperless-local/
    SKILL.md
    scripts/
  openproject-local/
    SKILL.md
    scripts/
```

Hermes should scan this location through its official `skills.external_dirs` configuration, using the target-local repo workspace:

```yaml
skills:
  external_dirs:
    - /root/workspaces/apexai-os-meta/ki-basis/hermes-skills
  write_approval: true
```

Why:

- skill definitions are reviewable/version-controlled;
- runtime secrets stay in Hermes `/opt/data/.env`;
- the repo is already target-local in `ki-basis-hermes-workspaces`;
- Hermes officially supports external skill directories;
- `skills.write_approval: true` means Hermes cannot silently rewrite these procedures without operator review.

Do not set `skills.create_dir` to this repo directory in the first iteration. Keep self-created/learned skills separate from operator-maintained integration skills.

---

## 5. Secure skill credential setup

Each skill declares only its own secret through Hermes frontmatter.

Example shape:

```yaml
required_environment_variables:
  - name: PAPERLESS_API_TOKEN
    prompt: Paperless API token
    help: Create/rotate it in the local Paperless My Profile page.
    required_for: Authenticated local Paperless REST API access.
```

Hermes officially states that local CLI setup stores such values in Hermes `.env` and does not expose the raw secret to the model.

### Operator interaction

After Antigravity creates and activates the skills, it must stop and ask the operator to open the local Hermes CLI:

```powershell
docker exec -it ki-basis-hermes /opt/hermes/.venv/bin/hermes
```

Then invoke each skill once:

```text
/paperless-local
/firefly-local
/openproject-local
```

When Hermes prompts for a missing credential, the operator enters it **there**, not in Antigravity.

The module resumes only after the operator reports that secure setup completed. Antigravity verifies only that the variables are marked configured/available; it must not print them.

---

## 6. Product-specific authentication realism

### Paperless-ngx

Official API supports Basic, Session, Token, Remote User, and headless OIDC.

For one local headless Hermes user, token authentication is the simplest and most revocable mechanism. Basic auth would require storing the user's password and is not preferable.

### Firefly III

Firefly's supported automation/import tooling uses personal access tokens. A local CLI still needs a supported Firefly identity when it changes/reads user financial data.

### OpenProject

Current stable API v3 supports personal API tokens, OAuth2, and session auth. OpenProject explicitly documents API keys/OAuth instead of username/password for clients.

OpenProject now also has an MCP server aimed at AI agents, but it was introduced in OpenProject 17.2 as an Enterprise add-on. The currently pinned stack is OpenProject 14, so **do not upgrade or redesign solely to obtain MCP in this module**. Even OpenProject MCP still requires API-token/OAuth authentication.

Future candidate only:

`OpenProject upgrade + Enterprise MCP evaluation`

Do not implement now.

---

## 7. Read-only first

First version of every skill is read-only.

Minimum meaningful actions:

### `paperless-local`

- search documents;
- fetch document metadata;
- retrieve text/content for a specifically selected document;
- optionally download a requested document to a controlled output path.

### `firefly-local`

- verify current user/API identity;
- inspect accounts/transactions/budgets using current supported API endpoints discovered from the installed version's API documentation;
- no transaction creation/update in v1.

### `openproject-local`

- inspect API root;
- list/search work packages/projects visible to the authenticated account;
- use API v3/HATEOAS links rather than inventing unsupported write semantics;
- no mutation in v1.

Do not hard-code endpoints from model memory. Re-open the installed product's API documentation/spec before implementing each client.

---

## 8. Skill implementation rule

Use a Skill rather than a custom Hermes Tool for v1 because Hermes' own guidance says a Skill is appropriate when the capability is instructions + shell commands/scripts wrapping an external API.

Each skill may include a small deterministic Python script using standard library HTTP primitives. This avoids adding another runtime dependency.

A custom Hermes Tool/plugin becomes justified only if later requirements need:

- complex OAuth lifecycle;
- streaming/binary handling that is awkward through terminal scripts;
- event-driven callbacks;
- precise structured tool schemas that materially improve reliability.

Do not start with a plugin.

---

## 9. Security rules for skill scripts

- Never print token values.
- Never include tokens in URLs.
- Use `Authorization` headers.
- Default to read-only endpoints.
- Set connect/read timeouts.
- Fail on non-2xx rather than fabricating data.
- Parse JSON and return bounded structured output.
- Never access sibling application databases directly.
- Never require `/var/run/docker.sock`.
- Never `docker exec` sibling app containers from Hermes.
- Never disable product auth to simplify local access.
- Never create an unauthenticated nginx control facade.

---

## 10. Human approval model

Keep Hermes dangerous command approvals enabled (`approvals.mode: smart`).

Enable:

```yaml
skills:
  write_approval: true
```

For later write-capable application skills, use a separate module and require:

- preview of exact intended mutation;
- explicit operator approval for consequential mutations;
- product response receipt;
- read-after-write verification.

Do not mix write capability into this read-only bootstrap.

---

## 11. Real operator acceptance — the tests that matter

After provider + skills are installed, the operator uses Hermes normally.

### Paperless proof

Operator asks Hermes:

> Find the document titled "Antigravity M5 Test Document" and tell me its document ID and metadata source.

PASS only if:

- Hermes selects/loads the Paperless skill;
- the skill calls the actual `paperless:8000` API;
- authentication succeeds;
- returned ID matches the real Paperless UI/API state.

### Firefly proof

Operator asks a safe read question based on a known Firefly object/account.

PASS only if the answer is sourced through Firefly's real API.

### OpenProject proof

Operator asks Hermes to find the known verification work package/project.

PASS only if the answer is sourced through the real OpenProject API v3.

### Denial proof

For each skill, run one test with a deliberately invalid temporary credential value in a disposable invocation. It must fail with authentication error and no fallback to DB/UI/local fixture.

---

## 12. Optional unified access surface

Once the three individual skills pass, create a Hermes **skill bundle** named `ki-basis-control` that loads the three skills together.

Do this only after individual proof; a bundle is orchestration, not a replacement for the three bounded integrations.

Expected operator UX:

```text
/ki-basis-control
```

or ordinary natural-language requests once skill discovery is reliable.

Do not create a fourth giant implementation that duplicates the three skills.

---

## 13. Advantages / disadvantages

### Advantages of this design

- One local Hermes CLI is the operator surface.
- Skills are small, version-controlled, and progressively disclosed.
- App traffic stays inside `ki-basis-net`.
- Tokens are revocable and scoped to application identities rather than Docker-host privilege.
- No Docker socket.
- No direct DB mutation.
- No application password embedded in scripts.
- Hermes' native skill-secret mechanism keeps raw secrets from the model.
- OpenRouter gives flexible model choice without modifying Hermes code.

### Disadvantages

- You still maintain one credential per application plus one model-provider credential.
- Tokens can expire/rotate and require operator maintenance.
- Product API coverage may not expose every UI operation.
- Data included in LLM prompts can leave the local machine when using OpenRouter/cloud models.
- Skill scripts need maintenance when product APIs change.
- Read-only v1 does not yet perform autonomous changes.

### Realism

**High.** This architecture is directly aligned with Hermes' documented skill model and the three products' documented API/auth models. It is much more realistic and safer than trying to give Hermes Docker-host control merely to avoid tokens.

---

## 14. Commit and stop boundaries

Recommended sub-commits within this module, each independently verified:

1. Hermes provider/config scaffolding only — no secret value.
2. `paperless-local` skill.
3. `firefly-local` skill.
4. `openproject-local` skill.
5. optional `ki-basis-control` bundle after all three pass.
6. final operator acceptance evidence with secrets redacted.

No push. STOP after module acceptance.

## Official sources

- Hermes provider setup: https://hermes-agent.nousresearch.com/docs/integrations/providers
- Hermes Docker layout: https://hermes-agent.nousresearch.com/docs/user-guide/docker
- Hermes Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Hermes skill authoring and secure env requirements: https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills
- Hermes security/approvals: https://hermes-agent.nousresearch.com/docs/user-guide/security
- Paperless API auth: https://docs.paperless-ngx.com/api/
- OpenProject API auth: https://www.openproject.org/docs/api/introduction/
- OpenProject MCP: https://www.openproject.org/docs/system-admin-guide/integrations/mcp-server/
- Firefly CLI/PAT example: https://docs.firefly-iii.org/how-to/data-importer/advanced/cli/
- OpenRouter privacy: https://openrouter.ai/docs/guides/privacy/data-collection
- OpenRouter provider routing/data policy: https://openrouter.ai/docs/guides/routing/provider-selection
