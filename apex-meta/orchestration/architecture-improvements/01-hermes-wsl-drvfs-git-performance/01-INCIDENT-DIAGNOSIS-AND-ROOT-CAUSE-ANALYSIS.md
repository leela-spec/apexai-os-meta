# 01 — Incident Diagnosis & Root Cause Analysis (RCA)

**Module ID:** `ARCH-IMP-01-INCIDENT-DIAGNOSIS`  
**Parent Package:** `01-hermes-wsl-drvfs-git-performance`  
**Date:** 2026-08-25  

---

## 1. The Incident Trace Breakdown

During Phase 4 handover generation in the weekly orchestration campaign, the Hermes agent was tasked with creating an independent reviewer assignment file and committing it to the repository.

The resulting execution log captured the exact failure progression:

```text
❯ create the handover for another agent to be the reviewer you are missing. write to the repo and push so I can hand the created path to the other agent

└─ ▾ Tool calls (3)
  ├─ ● Write File("/workspace/artifacts/weekly-orchestration-campaign/04-phase4/HA…") (3.2s)
  ├─ ● Terminal("git status --short -- artifacts/weekly-orchestration-campaign/ …") (120.4s)
  └─ ● Terminal("git log --oneline -1 + 1 command") (0.9s)

┊ Files are staged but the commit/push didn't finish within the timeout. Completing them separately.

└─ ▾ Tool calls (4)
  ├─ ● Terminal("git commit -m "docs(campaign) reviewer handover for independen…") (82.9s)
  ├─ ● Terminal("ps aux | grep -i "git" | grep -v grep + 1 command") (0.4s)
  ├─ ● Terminal("kill -9 1893 2>/dev/null + 4 commands") (2.5s)
  └─ ● Terminal("rm -f .git/index.lock + 1 command") (300.3s)

· interrupted
```

### Forensic Phase Breakdown:
1. **File Write (3.2s):** The agent wrote `HANDOVER-INDEPENDENT-REVIEWER.md` to disk. This succeeded rapidly because single-file sequential writes do not traverse the repository directory tree.
2. **Git Status Invocation (120.4s):** The agent ran `git status --short -- artifacts/...`. Despite providing a path argument, Git's default working tree comparator performs index validation and timestamp checks across the working tree, generating an enormous cascade of file stat system calls.
3. **Commit Timeout (82.9s):** The subsequent `git commit` attempted to acquire the index lock, compute directory trees, write the tree objects, and commit the new ref. This stalled indefinitely in the Linux kernel.
4. **The `kill -9` Failure:** The agent detected a timeout and attempted to force-kill PID 1893 (`kill -9 1893`). However, because the process was trapped in kernel disk wait (`D state`), the signal could not be delivered until the I/O request returned or faulted.
5. **The `.git/index.lock` Deadlock (300.3s):** Because PID 1893 held the file descriptor on `.git/index.lock` across the 9P virtual bridge, subsequent attempts to remove the lock (`rm -f .git/index.lock`) blocked on file handle release from the Windows host NTFS lock manager.

---

## 2. In-Depth Root Cause Analysis (RCA)

```mermaid
flowchart TD
    subgraph AgentCall["Agent Layer"]
        A1["Hermes Agent Shell"] -->|Executes 'git status' or 'git commit'| A2["Linux Git Binary (/usr/bin/git)"]
    end

    subgraph LinuxKernel["WSL2 Linux Kernel Space"]
        A2 -->|Issues ~100,000 lstat() syscalls| K1["VFS Layer (Virtual Filesystem)"]
        K1 -->|Routes to 9P / DrvFs Mount Driver| K2["9P File Client Driver"]
        K2 -->|Process enters uninterruptible sleep| K3["Task State: 'D' (TASK_UNINTERRUPTIBLE)"]
    end

    subgraph HypervisorBridge["Hypervisor / Network Bridge"]
        K2 -->|RPC Roundtrip per Syscall over Hyper-V Socket| H1["Hyper-V VM Bus / 9P Server"]
    end

    subgraph WindowsHost["Windows Host Space"]
        H1 -->|Translates to Win32 / NT Kernel API| W1["Windows NT Kernel (ntoskrnl.exe)"]
        W1 -->|Queries 53,866 files on C:\\| W2["NTFS File System Driver"]
        W2 -->|Metadata query & File Lock| W3["Physical NVMe / SSD"]
    end

    K3 -.->|kill -9 signal ignored while in D-state| K3
    K3 -->|Timeout / Stale Lock| D1[".git/index.lock Deadlock (300s stall)"]
```

### Root Cause 1: WSL2 9P / DrvFs Architectural Protocol Overhead
WSL2 is a full Linux virtual machine running on Hyper-V. When Linux accesses files mounted from Windows drives (`/mnt/c/...` or bind mounts from host `C:\...`), it does not communicate via direct DMA or memory mapping. Instead, it runs the **Plan 9 (9P) network filesystem protocol** over an internal Hyper-V socket.
* Every POSIX `lstat()`, `open()`, `read()`, and `close()` call is marshaled into a 9P network packet in Linux, serialized, passed through the Hyper-V bus, deserialized by the Windows 9P server, executed against NTFS via Win32 APIs, and passed back.
* While bulk sequential I/O (e.g. streaming a video) achieves acceptable throughput, **high-frequency metadata traversals** (such as Git inspecting 53,866 files) incur tens of thousands of serialized network roundtrips.

### Root Cause 2: Linux Kernel `D State` (TASK_UNINTERRUPTIBLE)
In Unix systems, when a thread initiates synchronous disk I/O, the kernel puts the thread into `TASK_UNINTERRUPTIBLE` (`D` state) to preserve filesystem consistency until the hardware/driver responds.
* When 9P experiences network/socket queue saturation, the I/O request hangs in the 9P client driver.
* Signals—including `SIGKILL` (`kill -9`)—are only processed when a thread returns to user space or enters `TASK_INTERRUPTIBLE` (`S` state). Consequently, an agent script cannot terminate or recover a stuck Git process in `D state` until the underlying Windows host completes the I/O or the socket resets.

### Root Cause 3: Lock File Atomicity Mismatch Across OS Boundaries
Git relies on atomic file creation (`open(..., O_CREAT | O_EXCL)`) to lock `.git/index.lock`.
* When a process in `D state` is partially terminated or times out, the Windows host NTFS file system continues to hold an active file lease/handle.
* An immediate Linux `rm -f .git/index.lock` encounters a file sharing violation or 9P lock wait, causing the remediation command itself to stall for 300+ seconds.

### Root Cause 4: Untracked Tree Traversals in Agent Git Dispatch
The default behavior of standard Git commands (`git status`, `git commit`) is to verify directory modifications and look for untracked files unless explicitly restricted:
* Without `--untracked-files=no` or `-uno`, Git scans all 53,866 tracked files plus any untracked directories across the entire repository.
* On native Linux ext4, this takes ~0.2 seconds. Over 9P on `/mnt/c/`, this takes ~120 to 180 seconds.
