# Environment Correction Implementation Plan — ki-basis

**Target runtime:** Docker Desktop installed on Windows, using its WSL-independent Hyper-V Linux-container backend as the single ki-basis Docker Engine.

```text
Windows 11
└── Docker Desktop for Windows
    └── Hyper-V Linux-container backend
        └── ONE Docker Engine
            └── ONE Compose project: ki-basis
                └── ONE shared bridge network: ki-basis-net
                    ├── nginx
                    ├── postgres + pgvector
                    ├── valkey
                    ├── firefly
                    ├── paperless
                    ├── openproject
                    └── hermes
```

## Preserved architecture rules
- PostgreSQL and Valkey internal-only
- official upstream images for complex products
- Alpine where technically appropriate
- no Docker socket in Hermes
- secret hardening
- image pinning
- backup coverage
- restore proof

## Execution Steps
1. Install Docker Desktop on Windows.
2. Select Linux containers and Hyper-V backend.
3. Run `00a-docker-desktop-target-gate.ps1 -SourceEngineId <source-engine-id>`.
4. Run `00b-environment-boundary-check.sh <source-engine-id>`.
