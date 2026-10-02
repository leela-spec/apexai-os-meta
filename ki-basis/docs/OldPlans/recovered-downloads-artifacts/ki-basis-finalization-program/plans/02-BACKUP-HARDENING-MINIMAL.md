# Module 02 — Minimal Backup Hardening

## Is the backup architecture overengineering?

**No.** For this stack, the current shape is approximately the minimum credible backup:

- PostgreSQL globals/roles plus three application DB dumps;
- stateful Docker volumes containing user-generated files and Hermes state;
- a checksum manifest;
- one real application-level disposable restore test.

Docker explicitly treats volumes as the persistence mechanism and documents tar-based backup/restore. PostgreSQL recommends logical dumps and custom-format `pg_dump` archives for flexible restore. The current architecture is therefore conventional, not excessive.

What **would** be overengineering now:

- restoring every application on every backup run;
- adding a dedicated enterprise backup server/product before there is a demonstrated need;
- snapshot orchestration, deduplication, replication, or HA;
- tuning backup concurrency before data size requires it;
- trying to make Valkey a source-of-truth backup system.

## Exact residual defect

`ki-basis/scripts/backup-stack.sh` currently allows archive failure to disappear through a terminal `|| true` path. A backup must fail closed.

The helper image value captured from Windows-native Docker output should also be normalized for CRLF, and helper commands should explicitly override the service image entrypoint.

## Required correction

Patch only `ki-basis/scripts/backup-stack.sh` unless a tiny fixture/helper is necessary.

For every Docker volume archive:

1. verify the named volume exists;
2. invoke helper container with explicit `--entrypoint sh`;
3. tar must return success;
4. produced archive must exist and be non-empty;
5. `tar -tzf` (or equivalent inside a helper container if host tar is unavailable) must successfully list the archive;
6. only then include it in `SHA256SUMS`;
7. any failure exits non-zero and restarts stopped application writers through the trap.

Normalize native Docker output used as an identifier with CR/LF stripping.

## Hermes secret-backup policy

Module 05 will store provider/application credentials in Hermes `/opt/data/.env` using the official secure setup path.

**Recommended minimal policy:** exclude `/opt/data/.env` from the Hermes state archive and document that credentials must be re-entered by the operator after disaster restore.

Reason:

- credentials remain recoverable by reissuing/rotating them;
- copying long-lived API secrets into every backup increases the breach surface;
- this avoids adding backup encryption machinery just to preserve replaceable credentials.

Do not exclude sessions, memories, skills, config, or workspaces.

If the current Hermes archive mechanism cannot exclude `.env` cleanly without broad rewrite, mark this one item `DEFERRED_TO_M07_ENCRYPTED_OFFHOST_POLICY` rather than destabilizing the working backup.

## Preserve

- Postgres custom-format DB dumps;
- `pg_dumpall --globals-only`;
- current named-volume list;
- application-writer stop/restart safety;
- checksums;
- Windows `docker cp` / no-stdin-pipe lessons where already required.

## Adversarial tests

1. Call a disposable copy of the archive function with a nonexistent volume -> backup must fail.
2. Force helper command failure -> backup must fail.
3. Corrupt a copied archive -> integrity listing/checksum verification must fail.
4. Confirm application writers restart after a deliberate failure.

Never corrupt live volumes.

## Acceptance

`PASS` only if a fresh target backup is generated with all required artifacts and the script would not print `Backup complete` after any required artifact failed.

## Commit boundary

One local backup-hardening commit. No push. STOP.

## Source basis

- Docker volume backup/restore: https://docs.docker.com/engine/storage/volumes/
- PostgreSQL custom dump format: https://www.postgresql.org/docs/current/backup-dump.html
- PostgreSQL globals: https://www.postgresql.org/docs/current/app-pg-dumpall.html
