# Module 07 — Cold Reboot and Second-Copy Backup

## Target

Prove lifecycle resilience after the architecture/skills are complete.

## Part A — Windows cold reboot

This is an operator gate because the machine must reboot.

Before asking:

- ensure repo working tree is safe;
- ensure a fresh target backup exists;
- ensure no long-running unrelated job will be interrupted;
- record target Docker Engine ID and seven-service state.

Ask operator to reboot Windows normally.

After reboot verify:

1. Docker Desktop starts successfully.
2. Target Docker Engine is Docker Desktop, not Ubuntu WSL Docker.
3. Ubuntu WSL remains stopped unless explicitly opened.
4. Exactly seven ki-basis services return healthy/running.
5. Persistent Paperless/Firefly/OpenProject/Hermes fixture state remains.
6. Hermes provider starts and can answer a non-sensitive prompt.
7. Each of the three Hermes application skills completes one read-only real-product call.
8. PostgreSQL/Valkey host isolation and no Hermes Docker socket still hold.

## Part B — second-copy/off-host backup

The current backup on the same laptop protects against container/operator errors but not laptop/SSD loss.

Do not install a new backup platform automatically.

Ask the operator to choose an already trusted second failure domain, for example:

- encrypted external SSD;
- existing encrypted cloud backup location;
- another trusted machine/storage destination.

Because databases/documents themselves may be sensitive, the second copy must be encrypted at rest by the chosen destination or by an existing trusted encryption workflow.

Do not add a new encryption product without operator choice.

Copy one already-verified backup plus checksum manifest to that destination and verify checksums after transfer.

## Overengineering guard

One verified second copy is enough for this phase. Do not implement rotation schedules, retention daemons, deduplication, HA, or automated cloud replication unless data volume/recovery objectives later justify them.

## Acceptance

- cold reboot target acceptance PASS;
- one verified second-copy backup exists outside the laptop's primary storage failure domain.

Runtime evidence only unless a small sanitized receipt is explicitly required. STOP.
