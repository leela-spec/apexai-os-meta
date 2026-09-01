# M02 — Fail-Closed Required Secrets in Compose

## Goal

Prevent the stack from silently starting with known placeholder passwords or application secrets when required environment variables are missing.

## Depends on

M01 PASS.

## Required active context

Read only:

- correction control files;
- this module;
- `ki-basis/compose.yaml`;
- `ki-basis/.env.example`;
- live `docker compose config` behavior;
- current official Compose variable-interpolation semantics if needed.

Do not load application implementation plans unless a specific variable's required/optional status cannot be resolved from current Compose/runtime evidence.

## Current defect

Required secrets currently use fallback expressions such as `${VAR:-known_placeholder}`. This is fail-open: a missing `.env` can produce a syntactically valid stack using predictable credentials.

## Scope

Patch only secret/credential interpolation and directly related comments/examples.

Likely required secret classes:

- PostgreSQL superuser password;
- Firefly DB password and app key;
- Paperless DB password, secret key, initial admin password if bootstrap still uses it;
- OpenProject DB password and secret key base;
- Hermes dashboard/API authentication secret(s).

Do not convert non-secret convenience values such as host ports, service names, timezone, DB names, or usernames to required variables unless current runtime policy requires it.

## Implementation rule

For secrets that must exist at runtime, use fail-closed Compose interpolation, e.g.:

```yaml
${POSTGRES_PASSWORD:?POSTGRES_PASSWORD is required}
```

Keep placeholder values only in `.env.example`, clearly labeled as examples that must be changed before use.

If any secret is generated automatically by the actual upstream product and should not be supplied by Compose, remove the misleading variable instead of making it required. Verify current official product behavior before doing so.

## Verification

Positive:

1. valid local `.env` -> `docker compose config` succeeds;
2. existing running stack remains able to start with its real ignored secrets;
3. no real secret enters Git diff.

Negative/adversarial:

1. run Compose config with one required secret deliberately absent in a disposable environment;
2. it must fail with an explicit missing-variable error;
3. repeat for at least one app secret and the PostgreSQL password;
4. grep tracked stack files for the known placeholder password patterns and confirm they appear only in `.env.example` or documentation explicitly marked as examples.

## Acceptance

PASS only when missing required secrets fail before deployment and the valid local stack still renders with real ignored values.

Persist M02 result, update state, commit the bounded secret-policy patch, context-reset, continue M03.