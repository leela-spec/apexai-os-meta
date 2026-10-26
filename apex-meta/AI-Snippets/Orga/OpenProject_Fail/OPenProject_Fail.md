Pushed — `bf5eee79..87523a9f main -> main` on `leela-spec/apexai-os-meta`. All 9 bundle docs are committed (including the root-cause note I just added to `02`).

### Why adding to OpenProject kept failing — the honest check

You’re right to flag it. It’s **one root cause, not random incompetence** — and part of it is genuinely on me:

**1. The WSL VM idle-sleeps.** Between my steps (I often wait on background tasks, or there’s a gap in the conversation), the whole Ubuntu VM shuts down. The next time I touch OpenProject it has to **cold-boot the entire VM + OpenProject (~80s)**, during which the API returns `000` then `503`. That boot cycle is what you keep seeing in my thinking.

**2. What looked like “constant failing” is mostly the safety gate working.** Before every write, the skill checks the instance is really there (`GET /api/v3`). If it gets a `503` (still booting), it **refuses to write** — `identity gate failed`. That’s it protecting your data from a half-booted instance, so I re-run once it’s warm. It reads as failure, but nothing was ever written wrong; the gate blocked cleanly every time. The cost was wall-clock re-runs, not data risk.

**3. My actual mistake.** Early on my scripts “warmed up” by pinging `whoami`, saw the first `200`, and started writing — but the instance then flapped back to `503` mid-batch, so the write aborted and I re-ran. I should have done a proper pre-warm from the start (wait for the _root_ endpoint to be stable 3× + settle _before_ any write). I only hardened that after it bit me twice. That’s the avoidable part, and it’s now baked into the scripts.

**4. The real fix is the thing that got deferred.** This is precisely the idle-sleep that handover **05 / Feature #122 (keepalive)** addresses. Keep the instance warm and these retries disappear entirely. So the “constant reboots” are a _known, single, fixable_ infrastructure issue — not a moving target.

I’ve documented this as a durable root-cause note in `02-preflight-and-transport-diagnosis.md` (in the pushed commit), so it’s checked, not just chat.

**My recommendation:** let me implement the keepalive now (it’s the one fix that ends the whole retry pattern for you _and_ for the auditor agent and every future session). Want me to set it up?

okay go ahead, then push and commit after updating all plans and openproject entries for that step

Going with a **WSL-internal keepalive** (a lightweight persistent ping loop that holds the VM awake) — it needs no Windows system-settings change, no console flashing, and auto-starts on boot. First let me inspect how WSL boots here (systemd? existing boot command?) so I hook in without clobbering docker’s startup:

Created inspect_boot.sh, ran a command (1 failed)

systemd is enabled (`[boot] systemd=true`, pid1=systemd) — so the clean fix is a proper **systemd service** running a ping loop: it holds the VM awake (a live process), keeps OpenProject warm, auto-starts on boot, and auto-restarts if it dies. No Windows changes, no window flashing. Installing it:

Created setup_keepalive.sh, ran a command

Keepalive service **installed, active, enabled** (auto-starts on boot, pid 2815). Now verifying it actually holds the instance warm — and confirming the operator’s Windows browser path works:

Created verify_keepalive.sh, ran a command

Instance warmed to serving (401) and the keepalive is active. But I want the **definitive test**: does the internal keepalive actually prevent a cold boot after a real idle gap? Let me leave WSL completely untouched for 90s (longer than the idle timeout), then hit it from Windows — if it responds instantly, the keepalive works:

Session limit reached

Try again after your session limit resets.

- Edited 3 files+31−7
- wsl-keepalive.vbs+11−4
- 05-handover-browser-keepalive.md+17−1
- index.md+3−2

Compacting before your next message keeps later replies fast and lighter on your usage.