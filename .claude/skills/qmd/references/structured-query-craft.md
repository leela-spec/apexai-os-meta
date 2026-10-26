---
type: Reference
id: REF-QMD-STRUCTURED-QUERY-CRAFT
title: QMD Structured Query Document Authoring & Anti-Drift Grammar
description: Grammar, field definitions, and authoring guidelines for typed QMD query documents to eliminate query expansion latency and prevent semantic drift.
status: current
tags: [qmd, query-craft, anti-drift, intent, hyde, grammar]
---

# QMD Structured Query Document Authoring & Anti-Drift Grammar

> **Governance Authority:** Decision `DEC-QMD-05` in [`07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/final/07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md).  
> **Complements:** [`SKILL.md`](../SKILL.md), [`search-speed-protocol.md`](search-speed-protocol.md).

---

## 1. Why Single-Line Queries Drift

When a bare single-line query is passed to `qmd query "specbench failure rate"`, the built-in 1.7B expansion model attempts to guess the user's intent. In empirical testing, it generated:
```text
├─ lex: understanding specbench errors
├─ lex: how to troubleshoot specbench issues
├─ vec: understanding specbench errors and their solutions
└─ hyde: If you encounter specbench failure rate problems, first check your environment...
```
The expansion model hallucinated that "failure rate" meant *software debugging and crash troubleshooting*, completely missing that *SpecBench* is an academic empirical benchmark evaluating coding agent criteria compliance!

---

## 2. The Structured Query Document Grammar

To bypass the 11.8s expansion phase, prevent hallucination, and cut latency down to ~8.4s, agents MUST author structured query documents:

```bash
qmd query $'intent: <what to find AND what to avoid>\nlex: <exact terms, aliases, benchmark names>\nvec: <natural language source-like paraphrase>\nhyde: <hypothetical answer passage>' -c apex-informatics-final
```

### The Four Field Types:
1. **`intent:` (Mandatory):** Defines the exact objective **and the negative space** (what to avoid). This prevents cross-encoder confusion:
   - *Example:* `intent: Find empirical benchmark findings on agent self-authored unit tests. Avoid general unit testing best practices or software crash debugging.`
2. **`lex:` (BM25 Keywords):** Exact anchor tokens, author names, rule tags, or IDs:
   - *Example:* `lex: SpecBench self-authored acceptance criteria 42.7% proxy replacement`
3. **`vec:` (Semantic Paraphrase):** How the originating document would describe the concept in prose:
   - *Example:* `vec: empirical failure rate when coding agents evaluate their own work using self-generated tests`
4. **`hyde:` (Hypothetical Document Embeddings - Optional):** A 1-2 sentence hypothetical passage matching the expected document format.

---

## 3. Worked Production Examples for Apex OS

### Example A: Looking Up Benchmark Findings (RP-05)
```bash
qmd query $'intent: Find SpecBench empirical failure rate on agent-authored criteria. Avoid generic testing guides.\nlex: SpecBench criteria failure 42.7% Zhao\nvec: how often agents fail when writing their own acceptance criteria' -c apex-informatics-final
```

### Example B: Looking Up Rule Compression Rationale (Layer 1 KB)
```bash
qmd query $'intent: Find the surgical compression rationale for Rule 01 Target. Avoid general prompt engineering tips.\nlex: SB-01.1 Option B Target surgical compression\nvec: default behavior audit and compressed phrasing for target outcome' -c apex-informatics-final
```

### Example C: Looking Up FixedBench No-Op Legitimacy (RP-07)
```bash
qmd query $'intent: Find FixedBench empirical measurements on unwanted code edits on already-fixed bugs. Avoid bug-fixing tutorials.\nlex: FixedBench over-building unwanted modifications 35%-65% no-op\nvec: coding agents making unnecessary edits instead of stopping when no change is needed' -c apex-informatics-final
```
