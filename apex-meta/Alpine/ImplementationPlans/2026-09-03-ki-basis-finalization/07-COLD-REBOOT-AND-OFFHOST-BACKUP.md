# Module 07 — Cold Reboot and Second-Copy Backup

## Target

Prove lifecycle resilience after the architecture/skills are complete.

## Part A — background-runtime + Hermes-bridge lifecycle proof

A forced Windows reboot is not required for the current phase.

Required now:

1. keep Docker Dashboard closed;
2. record seven-service state;
3. restart Docker Desktop through the supported CLI/background path;
4. verify all seven services recover;
5. verify Hermes API server recovers on loopback;
6. run `ki-basis/scripts/invoke-hermes.ps1` with a non-sensitive prompt;
7. re-run existing isolation checks.

At the next natural Windows reboot, run the same proof once. Open a correction only if the natural reboot exposes a real startup/persistence defect.

## Part B — second-copy/off-host backup

Keep as a future resilience requirement, not a blocker for the current bridge phase.

When the operator selects an already-trusted encrypted second failure domain, copy one verified backup plus checksum manifest there and verify it.

Do not install a new backup platform, cloud-sync daemon, retention service or encryption product merely to close this phase.

## Overengineering guard

One verified second copy is enough for this phase. Do not implement rotation schedules, retention daemons, deduplication, HA, or automated cloud replication unless data volume/recovery objectives later justify them.

## Acceptance

Blocking now:

- Docker Dashboard remained closed during normal operation;
- supported Docker Desktop restart PASS;
- seven services recovered;
- authenticated Hermes API bridge recovered;
- non-sensitive bridge invocation succeeded;
- isolation boundaries remained intact.

Future, non-blocking:

- natural Windows reboot check;
- encrypted second-copy backup after operator selects a destination;
- final real-skill persistence/cross-app proof after the skill set is installed.

Runtime evidence only unless a small sanitized receipt is explicitly required. STOP.
