# Task Assignment: Reviewer 1 (Architecture & Isolation)

## Identity
- Role: Architecture & Isolation Reviewer
- Working Directory: C:\GitDev\apexai-os-meta\.agents\reviewer_1
- Parent Orchestrator: orchestrator_1 (ID: 96367b83-1fd0-4e20-8a61-cc9640b72e38)

## Mandatory Inputs to Read First
- `C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md`
- `C:\GitDev\apexai-os-meta\.agents\PROJECT.md`
- `C:\GitDev\apexai-os-meta\.agents\worker_impl_1\changes.md`
- `C:\GitDev\apexai-os-meta\.agents\worker_impl_1\handoff.md`
- `C:\GitDev\apexai-os-meta\ki-basis\compose.yaml`
- `C:\GitDev\apexai-os-meta\ki-basis\.env.private`
- `C:\GitDev\apexai-os-meta\ki-basis\.env.community`
- `C:\GitDev\apexai-os-meta\ki-basis\docs\DUAL_INSTANCE_ARCHITECTURE.md`

## Mission & Evaluation Criteria
Perform an independent, objective, and adversarial review of the dual-instance architecture:
1. Check Compose Parameterization & Namespaces:
   - Does `compose.yaml` dynamically use `${COMPOSE_PROJECT_NAME}` for containers and volumes?
   - Are there any remaining hardcoded static volume names or container names that could cause collision?
2. Check Network Isolation:
   - Are `ki-basis-private-net` and `ki-basis-community-net` completely separate bridge networks?
   - Is inter-stack routing or cross-stack DNS discovery prevented?
3. Check Port Bands & Loopback Binding:
   - Is Private strictly on 8080-8089 (8086, 8010, 8082, 8084, 8642, 9119)?
   - Is Community strictly on 9080-9089 (9086, 9010, 9082, 9084, 9642, 9219)?
   - Are all published ports explicitly bound to `127.0.0.1`?
   - Are PostgreSQL (5432) and Valkey (6379) strictly internal?
4. Check Strategy Evaluation (R3):
   - Is Strategy A vs Strategy B rigorously compared with empirical justification and WSL2 `localhostForwarding` analysis?
   - Is ADR-001 complete and well-structured?
5. Run verification commands:
   - Execute `python C:\GitDev\apexai-os-meta\ki-basis\scripts\verify_dual_isolation.py` and inspect output.

## Output
Write your review report to:
`C:\GitDev\apexai-os-meta\.agents\reviewer_1\review.md`
And write `handoff.md` with an explicit verdict: `APPROVE` or `REQUEST_CHANGES`. Send a message to orchestrator_1 when finished.

## 2026-09-07T08:43:11Z
You are reviewer_1. Your working directory is C:\GitDev\apexai-os-meta\.agents\reviewer_1.
Read your instructions in C:\GitDev\apexai-os-meta\.agents\reviewer_1\DISPATCH.md and the authoritative request in C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md.
Review the architectural and isolation implementation (compose parameterization, bridge networks, port bands, volume namespaces, Strategy A vs B evaluation).
Run python C:\GitDev\apexai-os-meta\ki-basis\scripts\verify_dual_isolation.py and review compose files.
Write your report to C:\GitDev\apexai-os-meta\.agents\reviewer_1\review.md and handoff.md with verdict APPROVE or REQUEST_CHANGES.
When finished, notify orchestrator_1 via send_message.
