# P12 — Scheduler Selection and Reliability Evidence

- **Phase:** P12
- **Status:** PASS
- **Date:** 2026-08-24
- **Executor:** Google Antigravity
- **Repository:** `leela-spec/apexai-os-meta`
- **Branch:** `main`
- **HEAD Commit:** `03d940fc0b4f521f829ed8716c57debfbb0851be`
- **Selected Scheduler:** WSL Native systemd timer (`apex-portfolio-rollup.timer`)

## 1. Input State
- P11 passed; atomic fail-closed portfolio rollup publisher implemented and verified.
- Need to select and verify a deterministic, observable scheduler mechanism requiring 0 model calls and robust error visibility.

## 2. Candidate Evaluation
- **Hermes no-agent cron:** Requires persistent gateway daemon; documented history of silent empty failures (`#20353`) and job-clobber bugs (`#80624`).
- **WSL Native systemd timer:** Fully deterministic, zero LLM model calls, direct OS process execution, systemd journal logging, automatic persistence across WSL restarts, native `systemctl list-timers` visibility. Selected as simpler and more robust.

## 3. Actions Executed
1. **Unit File Creation:**
   - Service: `/etc/systemd/system/apex-portfolio-rollup.service`
   - Timer: `/etc/systemd/system/apex-portfolio-rollup.timer` (Daily at 09:00:00, `Persistent=true`)
2. **Installation & Activation:**
   - Reloaded systemd daemon and enabled timer (`systemctl enable --now apex-portfolio-rollup.timer`).
3. **Execution Verification:**
   - Ran oneshot service (`systemctl start apex-portfolio-rollup.service`); verified exit code 0 and journald logging.
   - Verified timer appears in `systemctl list-timers`.
4. **Failure Observability Test:**
   - Injected failing service unit (`exit 42`); verified systemd explicitly marked unit as `failed (Result: exit-code)` with code=42.

## 4. Exact Files / Paths Changed
- In WSL systemd:
  - `/etc/systemd/system/apex-portfolio-rollup.service` (NEW)
  - `/etc/systemd/system/apex-portfolio-rollup.timer` (NEW)
- In `apexai-os-meta`:
  - `apex-meta/epics/hermes-multi-repo-orchestration-v2/implementation/implementation-state.yaml` (UPDATED)
  - `apex-meta/epics/hermes-multi-repo-orchestration-v2/implementation/evidence/P12-scheduler-selection-and-reliability.md` (NEW)

## 5. Evidence & Verdict
- `EXECUTED`: systemd timer active and enabled.
- `EXECUTED`: Service executed successfully with zero model calls.
- `EXECUTED`: Failure observability verified with explicit non-zero exit code reporting.

## 6. Rollback / Recovery Information
- `systemctl disable --now apex-portfolio-rollup.timer` and remove unit files from `/etc/systemd/system/`.

## 7. Blockers
- None.

## 8. Final Phase Verdict
**`P12_PASS`**
