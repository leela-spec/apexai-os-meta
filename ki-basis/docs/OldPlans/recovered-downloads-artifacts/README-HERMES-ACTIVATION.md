# Hermes Activation — Local Patch/Verification Bundle

This bundle treats the user's “Helm” reference as **Hermes**, based on the active Docker-stack context.

It does not redesign Hermes. It prepares local API credential variables and verifies that the existing Hermes container can actually reach and authenticate to Firefly, Paperless and OpenProject.

## 1. Apply the credential-variable patch

From the `apexai-os-meta` repo root:

```bash
bash /path/to/hermes-activation-patches/01-hermes-credential-vars.patch.sh
```

This adds only empty variable names to `.env.example` and optional environment pass-through in the Hermes Compose service:

```text
FIREFLY_API_TOKEN=
PAPERLESS_API_TOKEN=
OPENPROJECT_API_KEY=
```

No real token is committed.

## 2. Put the real values into the existing ignored `ki-basis/.env`

Edit the local file only:

```text
FIREFLY_API_TOKEN=<your existing Firefly PAT>
PAPERLESS_API_TOKEN=<your existing Paperless token>
OPENPROJECT_API_KEY=<your existing OpenProject API key>
```

Do not paste these values into Git or a report.

## 3. Recreate only Hermes

```bash
cd ki-basis
docker compose --env-file .env up -d --force-recreate hermes
cd ..
```

Do not recreate the entire stack just to activate Hermes.

## 4. Run the activation check

```bash
bash /path/to/hermes-activation-patches/02-hermes-activation-check.sh
```

It verifies:
- Hermes is running;
- `/opt/data` and `/root/workspaces` are mounted;
- Docker socket is absent;
- `ki-basis-net` membership exists;
- Firefly/Paperless/OpenProject service DNS/TCP works from Hermes;
- real authenticated API reads work from inside Hermes;
- invalid credentials fail.

## 5. Important boundary

Passing this bundle proves:

```text
Hermes runtime + network + credentials + real application APIs
```

It does **not** by itself prove that durable product-specific Hermes skills are source-controlled.

After Hermes is active, inspect the currently installed Hermes skill/customization mechanism and persist three small product-specific skills/connectors without committing secrets. Do not invent a generic fake connector if Hermes has a supported skill mechanism.
