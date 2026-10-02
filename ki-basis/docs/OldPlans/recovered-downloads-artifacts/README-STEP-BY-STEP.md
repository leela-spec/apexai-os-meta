# ki-basis Local Patch Program

**Target repository:** `leela-spec/apexai-os-meta`  
**Run location:** repository root, preferably from WSL/bash.  
**Safety model:** every `*.patch.sh` performs a bounded local edit only. It does **not** commit or push.

This bundle assumes the current architecture already works and corrects repository/reproducibility defects without redesigning the stack.

## What this program changes

1. Removes the **generic, non-Antigravity implementation-plan family** and keeps the Antigravity-specific family as execution authority.
2. Repairs relative links caused by moving the Antigravity plan family into `apex-meta/Alpine/ImplementationPlans/`.
3. Patches stale `ARCHITEKTUR-BASIS.md` to describe the actual implemented stack.
4. Protects `ki-basis/.env` from Git and makes required secrets fail closed.
5. Corrects Hermes port labels **only after probing the real endpoints**.
6. Removes the orphaned `openproject_data` declaration only if live Docker proves it is unused.
7. Adds a real seven-service verification script.
8. Generates a digest-pinning patch from the **actually running images** instead of inventing versions.
9. Adds reproducible backup coverage plus a disposable Paperless application-level restore test.
10. Runs a final repository/runtime verifier.

## Important: preserve these files

The Antigravity-specific plan family stays:

- `00-START-HERE.md`
- `01-META-IMPLEMENTATION-PLAN-ANTIGRAVITY.md`
- `02-NGINX-ANTIGRAVITY.md`
- `03-POSTGRES-PGVECTOR-ANTIGRAVITY.md`
- `04-VALKEY-ANTIGRAVITY.md`
- `05-FIREFLY-ANTIGRAVITY.md`
- `06-PAPERLESS-NGX-ANTIGRAVITY.md`
- `07-OPENPROJECT-ANTIGRAVITY.md`
- `08-HERMES-ANTIGRAVITY.md`
- `09-INTEGRATION-ACCEPTANCE-ANTIGRAVITY.md`

The older generic plan family is deleted because it duplicates authority.

## Before starting

Do **not** regenerate your real `ki-basis/.env`. The stack is already running, so preserve the working secret values you already have.

From the repo root:

```bash
git status --short
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'
```

If the working tree is not clean, commit/stash unrelated work first.

## Execution program

### Step 0 — Preflight

```bash
bash /path/to/ki-basis-local-patch-program/00-preflight-check.sh
```

Stop if it reports a structural mismatch.

### Step 1 — Canonicalize the implementation plans

```bash
bash /path/to/ki-basis-local-patch-program/01-plan-authority-cleanup.patch.sh
git diff --check
git diff -- apex-meta/Alpine/ImplementationPlans
```

Expected:
- generic plans removed;
- Antigravity plans remain;
- `START-HERE` and meta-plan links resolve.

Commit if correct:

```bash
git add -A
git commit -m "docs(alpine): canonicalize Antigravity implementation plan authority"
```

### Step 2 — Patch stale architecture

```bash
bash /path/to/ki-basis-local-patch-program/02-architecture-current.patch.sh
git diff -- apex-meta/Alpine/ARCHITEKTUR-BASIS.md
```

The patch updates only the architecture diagram/status sections. It records the older AnythingLLM/Psono/Auth/Envoy topology as superseded rather than active.

Commit after review.

### Step 3 — Harden secrets

First confirm the real file already exists and is not committed:

```bash
test -f ki-basis/.env && echo "real .env exists"
git ls-files --error-unmatch ki-basis/.env >/dev/null 2>&1 && echo "ERROR: .env tracked" || true
```

Then:

```bash
bash /path/to/ki-basis-local-patch-program/03-secret-hardening.patch.sh
```

What changes:
- adds `/ki-basis/.env` to `.gitignore`;
- removes known fallback secrets from Compose;
- makes required secrets `${VAR:?message}`;
- removes password fallbacks from the PostgreSQL init script;
- makes required secret fields blank in `.env.example`.

**Do not copy the now-blank `.env.example` over your working `.env`.**

Verify:

```bash
git check-ignore -v ki-basis/.env
cd ki-basis
docker compose --env-file .env config >/dev/null
cd ..
```

### Step 4 — Correct Hermes labels

This patch probes both live Hermes endpoints before editing:

```bash
bash /path/to/ki-basis-local-patch-program/04-hermes-labels.patch.sh
```

Expected architecture from the accepted implementation:
- `8642` = gateway/API
- `9119` = dashboard

The script refuses to modify labels if live endpoint evidence points the other way or is too ambiguous. If it aborts, open both URLs manually and use the printed probe evidence before deciding.

### Step 5 — OpenProject volume cleanup

```bash
bash /path/to/ki-basis-local-patch-program/05-openproject-volume.patch.sh
```

It removes only the declared `openproject_data` volume and only if live `docker inspect` confirms the OpenProject container is **not** using it.

### Step 6 — Add real seven-service tests

I interpret “seven accepted sports” as the seven accepted services. The added test also checks the host ports.

```bash
bash /path/to/ki-basis-local-patch-program/06-add-real-stack-tests.patch.sh
cd ki-basis
bash scripts/verify-stack.sh
cd ..
```

For full authenticated API proof later:

```bash
STRICT_AUTH=1 bash ki-basis/scripts/verify-stack.sh
```

This requires these values in the ignored real `.env`:

```text
FIREFLY_API_TOKEN=
PAPERLESS_API_TOKEN=
OPENPROJECT_API_KEY=
```

Do not commit those values.

### Step 7 — Pin the exact images actually running

Do **not** guess version tags.

Generate a patch from Docker's current immutable RepoDigests:

```bash
python3 /path/to/ki-basis-local-patch-program/07-generate-image-pin-patch.py
```

It creates `07-image-pins.generated.patch` in the repository root.

```bash
git apply --check 07-image-pins.generated.patch
git apply 07-image-pins.generated.patch
```

Then validate and recreate **one service at a time**, running `verify-stack.sh` after each. Do not perform a broad product upgrade.

### Step 8 — Add complete backups and real restore proof

```bash
bash /path/to/ki-basis-local-patch-program/08-add-backup-restore-tools.patch.sh
bash ki-basis/scripts/backup-stack.sh
```

Default destination:

```text
~/ki-basis-backups/<timestamp>/
```

Coverage:
- PostgreSQL globals + Firefly/Paperless/OpenProject logical dumps;
- Valkey data;
- Firefly uploads;
- all four Paperless volumes;
- OpenProject assets;
- Hermes `/root/.hermes`;
- repo-controlled Compose/config snapshot without the real `.env`.

Then perform an application-level Paperless restore test:

```bash
PAPERLESS_API_TOKEN='YOUR_EXISTING_TOKEN' \
PAPERLESS_RESTORE_EXPECT_TITLE='Antigravity M5 Test Document' \
bash ki-basis/scripts/restore-test-paperless.sh ~/ki-basis-backups/<timestamp>
```

The restore test creates disposable Postgres, Valkey and Paperless resources, restores DB + physical Paperless volumes, starts the **real Paperless image**, retrieves the restored document through the Paperless API, downloads the physical document content, then destroys only the disposable restore environment.

### Step 9 — nginx proxy proof

The seven-service verifier tests:
- `/healthz`
- `/firefly/`
- `/paperless/`
- `/openproject/`

If one application route fails, do not invent nginx rewrites. Either configure the product's officially supported subpath/base URL and retest, or remove that nginx subpath and keep the already-working direct localhost port.

### Step 10 — Final verification

```bash
bash /path/to/ki-basis-local-patch-program/09-final-verification.sh
STRICT_AUTH=1 bash ki-basis/scripts/verify-stack.sh
git status
git diff --check
```

## Secret policy

Correct model:

```text
Git:
  .env.example -> variable names, blank secret values
  compose.yaml -> required-variable checks

Local machine only:
  ki-basis/.env -> real passwords/API tokens
```

If your current `.env` is already working, keep it and never overwrite it.

## Image policy

Correct model:

```text
running tested container
        ↓
docker inspect RepoDigest
        ↓
pin exact sha256 digest in compose
        ↓
recreate one service
        ↓
run real tests
```

Do not replace `latest` with a guessed version from documentation.

## OpenProject

The existing external PostgreSQL + `/var/openproject/assets` structure is preserved. This program only removes the unused `openproject_data` declaration if Docker proves it has no consumer.

## Hermes

A separate Hermes activation bundle is provided. Apply the main stack corrections first where practical, then use the Hermes bundle to provision local credential variable names and run authenticated connector checks.
