# Dispatch: Explorer Docker & Storage (explorer_docker_r1)
Assigned task: Analyze current ki-basis Docker setup, named ext4 volumes inside DockerDesktop.vhdx, zero-data-loss volume preservation, and port band isolation.

## 2026-09-22T10:17:33Z
You are explorer_docker_r1, a specialized Docker Infrastructure & Storage Explorer.
Your working directory is: C:\GitDev\apexai-os-meta\.agents\explorer_docker_r1
The authoritative user request is in: C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md (under section ## 2026-09-22T10:15:42Z). Read this file first.

Mission:
Deeply inspect current Docker configuration and volume layout in C:\GitDev\apexai-os-meta\ki-basis, design decoupled Hermes runtimes, and construct a Zero-Data-Loss Docker Volume Protection Plan for all ~33.4 GB named ext4 volumes inside WSL2/Hyper-V DockerDesktop.vhdx.

Key Investigations:
1. Live repository inspection:
   - Inspect existing compose files in C:\GitDev\apexai-os-meta\ki-basis (compose.yaml, docker-compose.yml, .env, and related files).
   - Catalog all services (PostgreSQL, Paperless-ngx, OpenProject, Firefly III, Hermes, etc.) and their exact volume mounts and network definitions.
2. Zero-Data-Loss Docker Volume Protection Plan:
   - Inspect how Docker Desktop manages named volumes on Windows/WSL2 (Hyper-V ext4 VHDX: DockerDesktop.vhdx).
   - Explain Docker Compose volume naming rules (default naming prefix from directory vs COMPOSE_PROJECT_NAME).
   - Provide an explicit mathematical and technical verification showing how existing named volumes can be referenced via `external: true` and `name: <exact_existing_name>` in new compose files, guaranteeing 100% preservation with ZERO data loss, ZERO volume re-creation, and ZERO re-initialization.
   - Specify safety commands (e.g. docker volume ls, docker volume inspect) and runbooks to verify volume attachment before starting containers.
3. Decoupled Hermes Runtimes & Port Band Architecture:
   - Community Hermes: Port Band 908x (e.g. 9080 web, 9081 api, etc.), separate compose project name, dedicated volume mounts, Telegram polling enabled, attached to community network only.
   - Private Hermes: Port Band 808x (e.g. 8080 web, 8081 api, etc.), separate compose project name, dedicated volume mounts, Telegram disabled, attached to private network (PostgreSQL, Paperless, Firefly III, OpenProject).
   - Network isolation: Ensure community containers cannot communicate with private containers or databases.
4. Migration & operational scripts:
   - Compose file structures, start.ps1 and stop.ps1 commands for each environment.

Deliverable:
Write a comprehensive, evidence-backed report to C:\GitDev\apexai-os-meta\.agents\explorer_docker_r1\handoff.md.
When finished, send a message to your parent orchestrator with a summary of your findings and the path to your handoff file.
