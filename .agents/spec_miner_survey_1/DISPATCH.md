# Task Assignment: Spec Miner (Survey)

## Identity
- Role: Spec Miner
- Working Directory: C:\GitDev\apexai-os-meta\.agents\spec_miner_survey_1
- Parent Orchestrator: orchestrator_1 (ID: 96367b83-1fd0-4e20-8a61-cc9640b72e38)

## Objective
Thoroughly examine `C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md` and any related project documentation. Extract a complete, unambiguous, and structured specification of all functional requirements, architectural constraints, non-functional requirements, quantitative thresholds, acceptance criteria, and operational expectations for the `ki-basis` dual-instance separation.

## Mandatory Inputs to Read
- `C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md`

## Key Focus Areas
1. Requirements R1, R2, R3 full breakdown:
   - R1: Storage architecture (ext4 vs 9P), OpenProject exit status 1 cause and fix, headless container parameters.
   - R2: Dual-Instance isolation (namespaces `ki-basis-private` vs `ki-basis-community`, isolated bridge networks, non-overlapping port bands 8080-8089 vs 9080-9089, segregated databases, Valkey, Paperless, Firefly).
   - R3: Multi-Engine vs Multi-Project comparison (Strategy A vs Strategy B, localhostForwarding conflicts, resource footprint, operational tradeoffs).
2. Acceptance Criteria & Validation Metrics (CPU <5% at idle, zero port binding conflicts, zero shared volumes/DBs, complete runbooks).

## Output
Write your comprehensive specification report to:
`C:\GitDev\apexai-os-meta\.agents\spec_miner_survey_1\spec_report.md`
And write `handoff.md` summarizing your findings. Send a message to orchestrator_1 when done.

## 2026-09-07T08:31:46Z
You are spec_miner_survey_1. Your working directory is C:\GitDev\apexai-os-meta\.agents\spec_miner_survey_1.
Read your instructions in C:\GitDev\apexai-os-meta\.agents\spec_miner_survey_1\DISPATCH.md and the authoritative request in C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md.
Extract all functional and non-functional requirements, constraints, acceptance criteria, and quantitative thresholds for the ki-basis dual-instance separation (R1, R2, R3).
Write your full report to C:\GitDev\apexai-os-meta\.agents\spec_miner_survey_1\spec_report.md and your handoff to C:\GitDev\apexai-os-meta\.agents\spec_miner_survey_1\handoff.md.
When finished, notify orchestrator_1 via send_message with your handoff summary.
