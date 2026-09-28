---
type: Handover
title: OpenProject browser keepalive — end the idle-sleep cold boots
description: Make the private Leela OpenProject reliably reachable from the Windows browser (and agents) without the ~80s WSL cold-boot on every access. Transport is already fixed; only idle-sleep remains.
tags: [handover, openproject, wsl2, keepalive, idle-sleep]
status: ready
generated: { by: "claude/opus-4.8", at: "2026-09-27" }
implementation_authority: operator-gated
---

# Handover: OpenProject browser keepalive (idle-sleep fix)

## Goal
The operator can open `http://127.0.0.1:8083` at any time and it responds within a few seconds — no
~80s wait, no "link doesn't work." Same benefit for agents.

## What is already true (verified 2026-09-27 — do not re-derive)
- The instance **is reachable from Windows** now: OpenProject was republished on `0.0.0.0:8083`
  (`C:\GitDev\leela-op178\compose.shared-db.yaml`, service `openproject`), and Windows `curl`/browser
  reach `http://127.0.0.1:8083` **when the instance is warm** (verified: `GET /` → 200 → `/login`).
- The **only** remaining problem is idle-sleep: the WSL2 VM shuts down after ~60s idle; the next access
  cold-boots the whole VM + OpenProject (progression `000 → 503 → 401/200` over ~65–85s). A browser gives
  up long before that, which is exactly why "the link does not work" when clicked cold.
- Host-check: `OPENPROJECT_HOST__NAME=127.0.0.1:8083`, so the operator **must** browse
  `http://127.0.0.1:8083` (not `localhost`, which many browsers resolve to IPv6 `::1` first, and not the
  WSL VM IP → those give host-check 400 or fail).
- **Root access without a password:** `wsl -d Ubuntu -u root -- <cmd>` runs as root (WSL default). Docker
  commands work as root. Permission allow-rules already exist in `C:\.claude\settings.local.json`
  (`Bash(wsl -d Ubuntu -u root -- docker:*)`, `…-- bash:*`).

## Why it was left open
The operator chose to skip it for now (wanted the plan built first). It is a **persistent scheduled
task**, which both this repo's global rule ("never create cron jobs/schedulers automatically") and the
agent's own "don't modify system settings" boundary say must be **operator-approved / operator-run**, not
auto-created.

## Options (recommend A)

**A — Windows Scheduled Task (recommended: durable, no WSL restart).**
A hidden task that pings the instance every ~45–60s to hold the VM awake; trigger at logon + repeat;
survives reboot. The operator runs (or explicitly approves) one command; no admin needed for a per-user
task. Example (operator runs in an elevated-not-required PowerShell, or approve the agent to run it):
```
$act = New-ScheduledTaskAction -Execute "wsl.exe" -Argument "-d Ubuntu -- curl -s -o /dev/null http://127.0.0.1:8083/api/v3"
$trg = New-ScheduledTaskTrigger -AtLogOn ; $trg.Repetition = (New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Seconds 60)).Repetition
Register-ScheduledTask -TaskName "OpenProject-Keepalive" -Action $act -Trigger $trg -RunLevel Limited -Settings (New-ScheduledTaskSettingsSet -Hidden -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries)
```
(Verify the console window is hidden; if it flashes, wrap the ping in a hidden `conhost`/VBS launcher.)

**B — WSL boot-command keepalive (self-contained, but restarts both stacks once).**
Add to `/etc/wsl.conf` (as root) a `[boot] command=` that launches a background `while true; do curl -s -o
/dev/null http://127.0.0.1:8083/api/v3; sleep 30; done &`. A running loop keeps the VM alive. Needs one
`wsl --shutdown` to apply — that restarts **both** the Leela and the Lika community stacks (they
auto-restart via `restart: unless-stopped`; verify both healthy after).

**C — `.wslconfig` `vmIdleTimeout` (uncertain).** Editable at `C:\Users\gehma\.wslconfig` (`[wsl2]` has
`memory=16GB, swap=4GB`). Raising `vmIdleTimeout` *may* delay shutdown but is not reliably effective on
its own; treat as a supplement, not the fix.

## Safety
- Do not create the scheduler without explicit operator approval (repo + agent boundaries).
- Option B's `wsl --shutdown` is disruptive — get operator OK; re-verify Leela **and** community stacks
  after (`docker ps`, `priv_openproject` = 83 WPs now, `comm_openproject` = 56).
- The port is on `0.0.0.0` inside the WSL NAT VM — reachable from the Windows host, isolated from the LAN
  by WSL NAT + the default Hyper-V firewall (deny inbound). A belt-and-suspenders explicit firewall rule
  needs an elevated prompt; optional.

## Definition of done
Cold-start test from Windows: after inactivity, `curl http://127.0.0.1:8083/api/v3` returns a real HTTP
code (200/302/401) within ~2s on repeated checks over 10+ minutes, with no `000` window — proving the VM
no longer idle-sleeps. Operator confirms the browser opens the login page immediately.
