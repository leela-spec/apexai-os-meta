# Module 01 — Secret Rotation and Operator Gate

## Target

Repair the second Paperless token exposure without widening scope, and establish the permanent rule that **the operator enters secrets locally; Antigravity never receives or stores them**.

## Current defect

`apex-meta/Alpine/HANDOVER-REVIEWER-DOSSIER.md` contains the replacement Paperless API token in plaintext, and that dossier is present on GitHub `main`. Therefore that token must be treated as exposed again.

## Architecture decision

Do not introduce a secret manager product in this module.

For the upcoming Hermes control skills, use Hermes' native secure skill-secret flow:

- skills declare `required_environment_variables`;
- when a secret is missing, the **local Hermes CLI** prompts the operator securely;
- Hermes stores it in its persistent home `.env` (`/opt/data/.env` in the official Docker layout);
- the raw secret is not exposed to the model;
- gateway/chat surfaces must not collect secrets in-band.

This is the native Hermes mechanism and is simpler than adding Vault/1Password/etc. solely for this local stack.

## Antigravity execution contract

### Preflight

1. Verify live `main` and working tree.
2. Search tracked files for plaintext Paperless tokens/API keys without printing matched values into the report.
3. Confirm `ki-basis-hermes-data` is mounted to `/opt/data`.
4. Do not mutate until the operator gate below is prepared.

### Human gate — Paperless token rotation

Antigravity must ask the operator to:

1. Open Paperless locally at `http://127.0.0.1:8010/`.
2. Open **My Profile**.
3. Rotate/re-create the API token using the UI control documented by Paperless.
4. Copy the new token to a temporary trusted clipboard/password-manager location only.
5. Do **not** paste it into Antigravity.

Antigravity then continues with repository sanitization but must not request the secret value.

### Repository sanitation

- Replace any exposed Paperless token in tracked evidence with `<REDACTED_PAPERLESS_API_TOKEN>`.
- Replace stale statements that claim no push occurred when live Git proves otherwise.
- Do not rewrite Git history by default. Revocation neutralizes the credential. A history rewrite is a separate operator/governance decision.

### Temporary handling until Module 05

The newly rotated token remains operator-held until the Paperless Hermes skill exists.

Module 05 will cause the local Hermes CLI to collect and persist it securely via `required_environment_variables`.

Do not add the new token to:

- `ki-basis/.env.example`;
- Compose YAML;
- Git-tracked scripts;
- evidence Markdown;
- shell command arguments;
- Antigravity chat.

## Independent proof

- Old token is rejected by Paperless (`401`).
- Tracked repository contains no real Paperless token value.
- Replacement token is never printed in evidence.

## Negative test

Seed a disposable fake token pattern in a temporary non-repository file and verify the sanitizer/checker detects it; then delete the temporary file. Do not create a real secret fixture in Git.

## Commit boundary

One local security/evidence commit only. No push. STOP.

## Source basis

Paperless documents token creation/rotation under its REST API authorization guide: https://docs.paperless-ngx.com/api/

Hermes documents secure skill setup so required environment variables are collected locally and not exposed to the model: https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills
