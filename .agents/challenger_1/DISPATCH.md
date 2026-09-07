# Task Assignment: Challenger 1 (Network & Port Collision Stress Verifier)

## Identity
- Role: Network & Port Collision Challenger
- Working Directory: C:\GitDev\apexai-os-meta\.agents\challenger_1
- Parent Orchestrator: orchestrator_1 (ID: 96367b83-1fd0-4e20-8a61-cc9640b72e38)

## Mandatory Inputs to Read First
- `C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md`
- `C:\GitDev\apexai-os-meta\.agents\PROJECT.md`
- `C:\GitDev\apexai-os-meta\.agents\worker_impl_1\changes.md`
- `C:\GitDev\apexai-os-meta\ki-basis\compose.yaml`
- `C:\GitDev\apexai-os-meta\ki-basis\.env.private`
- `C:\GitDev\apexai-os-meta\ki-basis\.env.community`
- `C:\GitDev\apexai-os-meta\ki-basis\scripts\verify_dual_isolation.py`

## Mission & Empirical Verification
Adversarially challenge the dual-instance network and port isolation:
1. Run and Audit the Verification Suite:
   - Execute `python C:\GitDev\apexai-os-meta\ki-basis\scripts\verify_dual_isolation.py`
   - Scrutinize the test harness: does it actually test collisions or is it superficial?
2. Adversarial Port Collision Testing:
   - Check every single published port across both instances. Is there ANY mathematical overlap?
   - Test what happens if an operator starts Private and Community concurrently: will any port binding collide?
   - Verify that all published ports bind strictly to `127.0.0.1` (no `0.0.0.0` exposure).
   - Check if database ports (Postgres 5432, Valkey 6379) are accidentally exposed to the host.
3. Network Bridge Isolation Verification:
   - Verify that container-to-container traffic between stacks is completely blocked by distinct Docker bridge networks (`ki-basis-private-net` vs `ki-basis-community-net`).
   - Check DNS resolution: can a container in Private resolve a service in Community?

## Output
Write your challenge findings to:
`C:\GitDev\apexai-os-meta\.agents\challenger_1\challenge_report.md`
And write `handoff.md` with an explicit verdict: `APPROVE` (correctness confirmed) or `CHALLENGE_FAILED` (flaws found). Send a message to orchestrator_1 when finished.

## 2026-09-07T08:43:11Z
You are challenger_1. Your working directory is C:\GitDev\apexai-os-meta\.agents\challenger_1.
Read your instructions in C:\GitDev\apexai-os-meta\.agents\challenger_1\DISPATCH.md and the authoritative request in C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md.
Adversarially challenge the network and port isolation of ki-basis dual-instance architecture.
Run python C:\GitDev\apexai-os-meta\ki-basis\scripts\verify_dual_isolation.py, test for port collisions, evaluate localhostForwarding edge cases, and verify loopback binding.
Write your report to C:\GitDev\apexai-os-meta\.agents\challenger_1\challenge_report.md and handoff.md with verdict APPROVE or CHALLENGE_FAILED.
When finished, notify orchestrator_1 via send_message.

