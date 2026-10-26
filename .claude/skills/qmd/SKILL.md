---
name: qmd
description: Search local markdown knowledge bases, notes, docs, and wikis with QMD. Use when users ask to find notes, retrieve documents, inspect a wiki, or answer from indexed local markdown.
license: MIT
compatibility: Requires qmd CLI. Run `qmd skill show` for upstream version-matched instructions.
allowed-tools: Bash(qmd:*), mcp__qmd__*
---

# QMD — Query Markdown Documents (Apex OS Profile)

> **Canonical Authority:** [`07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/final/07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md) (`DEC-QMD-01..06`).  
> **Supporting References:** [Search Speed Protocol](references/search-speed-protocol.md) | [Windows Runtime Topology](references/runtime-topology-windows.md) | [Structured Query Craft](references/structured-query-craft.md) | [MCP Setup](references/mcp-setup.md) | [Benchmarks & Fixtures](references/benchmarks-and-fixtures.md).

---

## 1. Core Operating Protocols (Mandatory Invariants)

All agents executing in this repository MUST adhere to these three core operational rules:

### Rule 1: Two-Tier Speed Escalation (`DEC-QMD-01`)
- **Tier 1 (Instant Keyword Search — 0.32s):** Always run `qmd search "<term>" -c <collection>` first. It uses SQLite FTS5 (BM25), executes in **321 ms**, and consumes zero GPU memory.
- **Tier 2 (Semantic Hybrid Escalation — 8.4s to 44s):** Escalate to `qmd query` ONLY if keyword search returns zero results or the user prompt is purely conceptual without known identifiers.

### Rule 2: Surgical Slicing via `#docid:line:count` (`AD-04`, `AD-19`)
- Never read entire 500-line markdown files into working context ("context bloat").
- Pull only the relevant 20–40 line slice around search hits:
  ```bash
  # Retrieve lines 140 to 175 of document #6e12d5
  qmd get "#6e12d5:140:35"
  ```
- Always cite the `#docid` and exact line numbers in working responses.

### Rule 3: Windows CLI Only — Background Daemon Banned (`DEC-QMD-02`)
- On Windows hosts, **NEVER** run `qmd mcp --daemon` or `qmd mcp --http --daemon`. Upstream process checks rely on Unix `/proc/`, causing orphaned zombie background tasks on Windows.
- Use direct CLI execution (`qmd search`, `qmd get`, `qmd query`) or direct stdio MCP launched by host IDE tools.

---

## 2. Typical Operational Loop

```bash
# 1. Search candidates with collection scoping (0.32s)
qmd search "FixedBench" -c apex-informatics-final -n 5

# 2. Inspect hit leads (#dac4f3 line 31) and fetch exact slice (0.05s)
qmd get "#dac4f3:25:35"

# 3. If exact keywords are unknown, author a structured query document (8.4s)
qmd query $'intent: Find empirical benchmark on proxy test failure rates. Avoid unit test tutorials.\nlex: SpecBench self-authored criteria 42.7% failure\nvec: coding agents failing when evaluating own work with tests' -c apex-informatics-final
```

---

## 3. Upstream Version-Matched Instructions

To display upstream library documentation directly from the CLI:

```bash
qmd skill show
```
