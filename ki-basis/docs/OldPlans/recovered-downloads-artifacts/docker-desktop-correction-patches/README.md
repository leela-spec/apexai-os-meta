# Docker Desktop Correction Patches

These are **incremental patches** for the already-corrected ki-basis migration/patch bundles. They do not replace the previous plan and intentionally preserve the correct service/network/secrets/image/backup/Hermes decisions.

## Corrected target

```text
Windows 11
└── Docker Desktop for Windows
    └── Hyper-V Linux-container backend
        └── one Docker Engine
            └── one Compose project: ki-basis
                └── one shared network: ki-basis-net
                    ├── nginx
                    ├── postgres + pgvector
                    ├── valkey
                    ├── firefly
                    ├── paperless
                    ├── openproject
                    └── hermes
```

The existing Ubuntu WSL Docker Engine remains **source/rollback only** during migration.

## Apply

Assuming the previously corrected bundles are extracted as:

```text
./ki-basis-local-patch-program/
./hermes-activation-patches/
./docker-desktop-correction-patches/
```

run:

```bash
bash docker-desktop-correction-patches/PATCH-03-docker-desktop-main.patch.sh \
  ./ki-basis-local-patch-program

bash docker-desktop-correction-patches/PATCH-04-docker-desktop-hermes.patch.sh \
  ./hermes-activation-patches

bash docker-desktop-correction-patches/PATCH-VERIFY-docker-desktop-correction.sh \
  ./ki-basis-local-patch-program \
  ./hermes-activation-patches
```

## First runtime gate after patching

1. Record the **source Ubuntu WSL** Engine ID before switching away from it:

```bash
docker info --format '{{.ID}}'
```

2. Install/configure **Docker Desktop on Windows** for Linux containers using its **Hyper-V backend**.

3. From Windows PowerShell, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\ki-basis-local-patch-program\00a-docker-desktop-target-gate.ps1 -SourceEngineId '<SOURCE_ENGINE_ID>'
```

The gate fails if:
- Docker Desktop is missing;
- the target Engine ID equals the WSL source Engine ID;
- Docker is not in Linux-container mode;
- the Engine does not identify as Docker Desktop;
- the target kernel identifies as WSL2.

4. Then continue with `ENVIRONMENT-CORRECTION-IMPLEMENTATION-PLAN.md` and `README-STEP-BY-STEP.md`.

## Preserved, not changed

- one Compose project;
- seven canonical service containers;
- one `ki-basis-net` bridge network;
- Docker service-name DNS;
- PostgreSQL/Valkey internal-only;
- official upstream images for complex products;
- Alpine only where appropriate;
- immutable image pinning;
- fail-closed secret handling;
- target-local persistence;
- complete backup + application restore proof;
- nginx route proof;
- Hermes without Docker socket;
- Hermes control through supported application APIs;
- old WSL stack retained for rollback until explicit deletion.
