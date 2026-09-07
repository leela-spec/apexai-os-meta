# Task Assignment: Codebase & Service Explorer (Survey)

## Identity
- Role: Codebase & Service Explorer
- Working Directory: C:\GitDev\apexai-os-meta\.agents\explorer_survey_2
- Parent Orchestrator: orchestrator_1 (ID: 96367b83-1fd0-4e20-8a61-cc9640b72e38)

## Objective
Explore the workspace `C:\GitDev\apexai-os-meta` to discover all existing compose files, services, configurations, scripts, environment definitions, and data paths related to `ki-basis` (OpenProject, Hermes, Paperless, Firefly, PostgreSQL, Valkey/Redis, etc.).

## Mandatory Inputs to Read
- `C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md`

## Key Focus Areas
1. Discover all files and directories in `C:\GitDev\apexai-os-meta` related to `ki-basis`, Docker Compose, docker configurations, `.env` files, scripts, or documentation.
2. For each service (OpenProject, Hermes, Paperless, Firefly, PostgreSQL, Valkey, etc.), map out:
   - Current image, tag, entrypoint, command
   - Current port mappings
   - Current volume mounts (host path vs named volume)
   - Current environment variables (database connection strings, secret keys, headless flags)
   - Network definitions
3. Identify existing port collisions, volume sharing, or shared database usage.

## Output
Write your comprehensive survey report to:
`C:\GitDev\apexai-os-meta\.agents\explorer_survey_2\codebase_survey.md`
And write `handoff.md` summarizing your findings. Send a message to orchestrator_1 when done.

## 2026-09-07T08:31:46Z
You are explorer_survey_2. Your working directory is C:\GitDev\apexai-os-meta\.agents\explorer_survey_2.
Read your instructions in C:\GitDev\apexai-os-meta\.agents\explorer_survey_2\DISPATCH.md and the authoritative request in C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md.
Survey the repository at C:\GitDev\apexai-os-meta to identify all existing ki-basis files, docker-compose manifests, services (OpenProject, Hermes, Paperless, Firefly, PostgreSQL, Valkey), ports, volumes, networks, environment configs, and scripts.
Write your full report to C:\GitDev\apexai-os-meta\.agents\explorer_survey_2\codebase_survey.md and your handoff to C:\GitDev\apexai-os-meta\.agents\explorer_survey_2\handoff.md.
When finished, notify orchestrator_1 via send_message with your handoff summary.
