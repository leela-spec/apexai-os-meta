---
type: Reference
id: REF-QMD-RUNTIME-TOPOLOGY-WINDOWS
title: QMD Runtime Topology & Windows Host Execution Protocol
description: Architecture specification for QMD on native Windows 11 host, model deployment details, daemon prohibition, and direct CLI execution.
status: current
tags: [qmd, topology, windows, native-workstation, cli]
---

# QMD Runtime Topology & Windows Host Execution Protocol

> **Governance Authority:** Decision `DEC-QMD-02` and `DEC-QMD-03` in [`07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/final/07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md).  
> **Complements:** [`SKILL.md`](../SKILL.md), [`mcp-setup.md`](mcp-setup.md), [`search-speed-protocol.md`](search-speed-protocol.md).

---

## 1. Windows Native Workstation Environment

The QMD infrastructure operates strictly on this Windows 11 host workstation:

| Dimension | Specification |
|---|---|
| **Operating System** | Windows 11 Host (`win32`) |
| **Filesystem Root** | `C:\GitDev\apexai-os-meta\` |
| **Active SQLite Index** | `C:\Users\gehma\.cache\qmd\index.sqlite` |
| **Collection Scope** | `apex-meta/informatics/final/**.md` (`apex-informatics-final`, 152 files) |
| **Execution Mode** | Direct CLI (`qmd search`, `qmd get`, `qmd query`) |
| **Background Daemon** | **STRICTLY PROHIBITED** |

---

## 2. Upstream Windows Daemon Defect & Prohibition

An audit of `@tobilu/qmd/dist/cli/mcp-pid.js` reveals:
- The daemon PID inspector `isQmdMcpPid` attempts to read `/proc/${pid}/cmdline` or calls Unix `ps -p ... -o args=`.
- On native Windows, both calls fail and return `null`.
- Consequently, running `qmd status` or `qmd mcp stop` fails to recognize a running daemon and deletes the PID lockfile while leaving the node process running.
- The orphaned process locks port 8181 and cannot be restarted or stopped cleanly without Windows Task Manager kill commands.

### Mandatory Directive:
Agents operating on this Windows workstation **MUST NOT** execute:
- `qmd mcp --daemon`
- `qmd mcp --http --daemon`

Agents interact with QMD **exclusively via direct CLI commands** (`qmd search`, `qmd get`, `qmd query`) or direct stdio MCP process invocation launched by host tools.

---

## 3. Local Model Cache & Hardware Acceleration

All models execute 100% on-device using local GGUFs stored at `C:\Users\gehma\.cache\qmd\models\`:

| Model Role | GGUF Filename | Disk Size | Runtime Engine |
|---|---|---|---|
| **Vector Embedding** | `hf_ggml-org_embeddinggemma-300M-Q8_0.gguf` | 333 MB | `node-llama-cpp` via Vulkan / CPU |
| **Cross-Encoder Reranker** | `hf_ggml-org_qwen3-reranker-0.6b-q8_0.gguf` | 639 MB | `node-llama-cpp` via Vulkan / CPU |
| **Query Expansion** | `hf_tobil_qmd-query-expansion-1.7B-q4_k_m.gguf` | 1,282 MB | `node-llama-cpp` via Vulkan / CPU |

> **Crash Protection:** QMD source code automatically sets `parallelism = 1` on Windows when CUDA is detected (`dist/llm.js:356`), preventing GPU driver timeout crashes.
