# Module 04A — Windows Docker Background Runtime

**Status:** CURRENT OPERATING DECISION

## Target

Keep the accepted Docker Desktop Hyper-V Linux-container runtime, but remove the Dashboard from the normal operating path.

```text
Windows 11
-> Docker Desktop background runtime/control plane
-> Hyper-V Linux VM
-> Docker Engine
-> one ki-basis Compose stack
```

The Dashboard window is not required for routine operation.

Completely quitting/stopping Docker Desktop is different: the Linux Docker Engine is inside Docker Desktop's managed Linux VM and does not continue as an independent Windows daemon.

A True Docker-Engine-only design would require a separately managed Linux VM with Docker Engine. That is a future migration candidate only if measured background-runtime cost remains unacceptable.

## Required now

1. Keep Hyper-V Linux-container backend.
2. Disable "Open Docker Dashboard when Docker Desktop starts".
3. Operate with the Dashboard closed.
4. Prefer CLI/background startup (`docker desktop start --detach` where supported).
5. Use `docker`, `docker compose`, and CLI agents for routine operation.
6. Open the Dashboard only for settings/troubleshooting.
7. Do not enable unrelated Desktop features.
8. Do not apply `.wslconfig` because the target is Hyper-V, not WSL2.
9. Do not change service worker/resource/database settings without measurements.

## Control-plane recovery

If Docker CLI/status becomes unhealthy after sleep/resume:

1. run one `docker desktop status`;
2. run one engine probe;
3. if it stalls/fails, do not queue more Docker commands and do not edit Compose;
4. restart Docker Desktop once through the supported CLI/Troubleshoot path;
5. retry once;
6. if still unhealthy, return `BLOCKED_HUMAN_GATE`.

## Acceptance

PASS when the Dashboard can remain closed while:

- Docker Desktop background runtime is healthy;
- Docker CLI/Compose operates normally;
- all seven services remain available.
