# Hermes Runtime Architecture — History, Failures, and the Proposed Fix

**Audience:** an engineer taking this over. Written to be self-contained.
**Author:** Claude (Opus) working with the operator, 2026-08-25.
**Status:** proposal for review. Nothing in "Architecture 3" is implemented yet.

---

## 0. TL;DR

There is exactly **one variable** that has caused every problem: **where the Hermes agent
executes relative to the work it operates on.** Three configurations were tried:

1. **Arch 1** — agent worked across the Windows↔Linux filesystem boundary (9p) → *catastrophically slow*.
2. **Arch 2** — agent core ran on the WSL host but executed commands in a *separate* Docker sandbox → *the agent was blind to its own boards, repos, tools, and credentials* ("everything needs a bridge").
3. **Arch 3 (proposed)** — the whole agent runs **inside one persistent container**; it executes commands in that same container. Nothing is separated, so **nothing needs bridging.**

The churn happened because rounds 1→2 fixed the filesystem and mounts (symptoms) but never
questioned the *split* between the agent and its execution environment. Arch 3 removes the split.

---

## 1. Environment primer (so the rest makes sense)

- **Windows** — the physical machine. User's editors and credentials live here (`C:\GitDev`, Windows Credential Manager).
- **WSL2** — "Windows Subsystem for Linux": a lightweight Linux VM inside Windows. Hermes is installed here. Canonical repos live on its native ext4 disk at `/root/workspaces/*`. Kanban boards live at `~/.hermes/kanban/`.
  - Key fact: WSL can read/write Windows files via `/mnt/c` — that cross-OS path uses the **9p** protocol, which is **very slow** for the many small file operations git performs.
- **Docker** — runs on top of WSL2. Can run programs in isolated containers.

Two *different* ways Docker gets used — conflating them is the root of the confusion:
- **"Docker terminal backend"** = Hermes runs on the WSL host and spawns a *separate* container just to run shell commands. (This is a split.)
- **"Hermes in Docker"** = the *whole agent* runs inside one container. (This is self-contained.)

---

## 2. Architecture 1 — the slow bridge (original; caused the incident)

```
Windows (C:\GitDev)  ──9p bridge──►  WSL Linux  ──►  Hermes / git
        (repo on NTFS)                (/mnt/c/...)
```

- Hermes operated on the repo through `/mnt/c/GitDev/...` (a Windows path seen from Linux).
- Every git metadata operation crossed the **9p** boundary.

**Why it failed (measured):** `git status` took **2–6 minutes** (vs 0.5s on native ext4), commits
timed out, and stuck git processes entered an unkillable kernel state; a stale `.git/index.lock`
blocked recovery for 300s. Root cause: **9p is the wrong filesystem for git-heavy work.**

**What fixed the symptom:** moved the canonical repos onto WSL-native ext4 at `/root/workspaces/*`
and enforced that agents never run on `/mnt/c`. This removed the slowness — but left Arch 2's split.

---

## 3. Architecture 2 — agent separated from the work (the "bridge" era)

```
WSL host                                   Docker sandbox (separate, often ephemeral)
────────                                   ───────────────────────────────────────
Hermes core  ──────spawns──────────────►   runs shell commands
kanban boards (~/.hermes/kanban)           /workspace = EMPTY or cwd-mounted
repos (/root/workspaces)                   no boards, no repos, no tools, no creds
credentials                                  ▲
                                             └── everything must be "bridged" in
```

- Filesystem speed was fixed (repos on ext4). But Hermes still used `terminal.backend: docker`:
  the agent **core** ran on the host while its **commands** ran in a *separate* sandbox container.
- Consequences of the split:
  - **Kanban boards** live host-side with the agent core; the sandbox couldn't see them, and the session's toolset didn't load the kanban tools → agent reported "0 boards."
  - **Repos** weren't in the sandbox; it cloned public ones **anonymously** (private repos → 404) and worked off **stale snapshots**.
  - **Tools** (Pandoc, docx2python, etc.) were attempted via a *second AI* (Antigravity) building a custom image and "handing it over" — the sandbox came up empty; tools missing.
  - **Credentials** weren't in the sandbox → git push failed.

**Why basic processes broke:** the agent was structurally separated from its boards, repos, tools,
and identity. Each gap needed a fragile "bridge" (a mount, a token, a toolset toggle), and the
bridges were incomplete. The agent was effectively blind and tool-less while *appearing* to work.

**Root cause:** the **split** between agent core and execution sandbox — not Docker itself, and not
the (now-fast) ext4 filesystem.

---

## 4. Architecture 3 — everything in one container (proposed)

```
ONE persistent Docker container  (image: nousresearch/hermes-agent)
──────────────────────────────────────────────────────────────────
Hermes core + kanban boards + repos + tools + config + memory
terminal.backend: local  →  commands run INSIDE this same container
persistent volume: /opt/data  ←→  host ~/.hermes  (survives restarts)
no /mnt/c, no host filesystem door  →  isolated from Windows
```

- The **whole agent** runs inside one container. `terminal.backend: local` means it runs its
  commands **in that same container** — the container *is* the sandbox. No nested Docker, no split.
- `/opt/data` (a persistent volume mapped to `~/.hermes`) is the single source of truth for config,
  **kanban boards**, memory, sessions, **skills/tools**, and git/ssh home — so state survives restarts.
- This is the pattern the Hermes docs document for "running Hermes in Docker."

**Why it works:** nothing is separated, so **nothing needs bridging.** Boards, repos, and tools are
all in the same place the agent runs.

**Security:** the container has **no door to your Windows files** (unlike WSL's `/mnt/c`), so a
malicious skill is **contained to the container** — it cannot reach your Windows documents. This is
the 2026-recommended way to run autonomous coding agents (isolate the whole agent in a container).
It is not a hardened VM, so a rare container-escape is theoretically possible; acceptable for a
single-user personal machine.

### Honest disadvantages of Arch 3 (no hidden surprises)

1. **One-time migration.** Hermes currently runs as a host install; moving to the container image is
   a real setup change (though existing boards/config/memory carry over via the `/opt/data` volume).
2. **Repos/tools live inside the container.** Other CLI agents (Claude, Codex) and your Windows IDE
   do **not** automatically share them — they keep their own clones and sync via GitHub (normal git
   workflow), unless you choose the "shared mount" option in §5.
3. **Rebuilds lose installed tools.** If the container image is rebuilt, apt/venv tools vanish; a
   checked-in **idempotent bootstrap script** reinstalls them. (Persistent `/opt/data` state survives.)
4. **Editing repos from a Windows IDE** requires either VS Code "attach to container," or the
   shared-mount option in §5.
5. **Container ≠ VM.** Strong but not perfect isolation; a rare kernel-level escape is possible.

---

## 5. The one real decision left: where do the repos physically live?

Both options are valid Arch-3 shapes. Pick one.

| | **5a. Repos inside the container** | **5b. Repos on host ext4, mounted into the container** |
| :-- | :-- | :-- |
| Physical copies | Container has its own clones | One copy on `/root/workspaces`, mounted read-write into the container |
| Divergence risk | Container copy vs Windows copy sync via GitHub (normal) | Only one Linux copy → no host/container divergence |
| Other agents / Windows IDE see repos | No (own clones, sync via GitHub) | Yes — same files on the host |
| Isolation | Strongest (no host door) | Slightly less: container can touch that one mounted folder (but nothing else on the host/Windows) |
| Speed | Native (container volume) | Native (ext4 bind mount — *not* 9p) |

**Recommendation:** **5b** — mount the existing `/root/workspaces` (the 4 canonical repos, **Leela
never included**) into the container. Rationale: you just fought a multi-copy *divergence* problem;
5b keeps a **single Linux copy**, lets other agents share it, and is still fully isolated from the
rest of Windows. The only cost is a bounded door to the repo folder — and repos are in git anyway,
so they're recoverable.

Choose **5a** instead only if you want the container to have **zero** host filesystem access.

---

## 6. The test this architecture must pass

> After a completely fresh start, Hermes can, **by itself**: find the canonical repos, verify its
> execution environment, install the exact required tools from repository-controlled scripts, do the
> approved work, persist auditable state, and recover later — **without another AI explaining what
> was previously configured.**

- Arch 1 fails (too slow to function). Arch 2 fails (blind/tool-less without manual bridges).
- **Arch 3 passes**: one environment, self-contained, tools from a checked-in bootstrap, state in
  `/opt/data`.

---

## 7. What a coder should verify / decide

1. Confirm the Hermes container image + `/opt/data` volume mapping preserves the existing 5 kanban
   boards, config, and memory (mount `~/.hermes:/opt/data`, `terminal.backend: local`).
2. Decide §5a vs §5b (repos inside vs mounted). Recommendation: 5b.
3. Provide a GitHub token **inside the container** for private-repo sync (MasterOfArts, acim). Never
   add any Leela repo.
4. Write one idempotent `bootstrap.sh` (checked into the repo) that installs/verifies the shared
   tools (Pandoc, poppler-utils, a pinned Python venv with docx2python, etc.).
5. Keep the dashboard on `localhost:9119` (WSL forwards to Windows) so existing access is unchanged.
6. Do **not** reintroduce: the 9p `/mnt/c` working path, the separate ephemeral sandbox (`terminal.
   backend: docker`), a second provisioning AI, or a custom foreign image handover.

---

## 8. Verified sources

- Hermes "run inside Docker" + `terminal.backend: local` + `/opt/data` single source of truth:
  https://hermes-agent.nousresearch.com/docs/user-guide/docker
- Kanban tools run in the agent process, reach `~/.hermes/kanban.db` regardless of backend:
  https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- WSL can read Windows files via `/mnt/c`; AV blind spot:
  https://reddogsecurity.substack.com/p/windows-subsystem-for-linux-from
- ext4 bind mounts are native-speed; `/mnt/c` mounts drag the 9p tax:
  https://www.docker.com/blog/docker-desktop-wsl-2-best-practices/
- Containerize the whole agent to avoid "handing it the keys to the host" (2026 guidance):
  https://collabnix.com/whats-new-in-docker-in-2026-sandboxes-hardened-images-and-the-ai-native-container-platform/
