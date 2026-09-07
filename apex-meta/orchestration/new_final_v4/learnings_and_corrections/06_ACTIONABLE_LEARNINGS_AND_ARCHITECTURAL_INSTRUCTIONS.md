# Actionable Learnings & Universal Architectural Instructions

**Document ID:** ALR-006  
**Date:** 2026-09-07  
**Location:** `apex-meta/orchestration/new_final_v4/learnings_and_corrections/`  
**Target Architecture Level:** Tier 1 & Tier 2 Prompting Rules & Governance  

---

## 1. Universal Instruction 1: The 80-Line Output Cap & Chunking Rule

> [!IMPORTANT]
> **No single generative eval prompt may request more than 80 lines or 4 KB of output in a single turn.**

### The Rule
When designing automated pipelines that require large creative or structural deliverables (such as full weekend workshop curriculums, multi-part essays, or comprehensive specifications):
- **Never issue a monolithic prompt** asking for the entire package at once.
- **Partition the deliverable into discrete sub-eval calls**:
  - `Turn 1`: Architecture & Table of Contents Outline.
  - `Turn 2`: Module 1 Detailed Script.
  - `Turn 3`: Module 2 Detailed Script.
  - `Turn 4`: Integration & Verification Review.
- Concatenate the resulting files using a deterministic script (e.g. `cat part1.md part2.md > final.md`).

### Rationale
- Prevents LLM context memory exhaustion.
- Eliminates HTTP/SSE streaming socket timeouts on cloud providers.
- Isolates generation failures to a single chunk rather than losing the entire document.

---

## 2. Universal Instruction 2: Deterministic Pre-Scaffolding

> [!TIP]
> **Deterministic code generates the skeleton; LLM only fills the prose.**

### The Rule
- Python scripts or bash generators should create the file structure, markdown headers, timing tables, and boilerplates first.
- The LLM should only be called to write specific sections (e.g., `"Write a 200-word facilitation guide for Exercise A"`).

---

## 3. Universal Instruction 3: Two-Phase Search for Corpus Cross-Referencing

> [!TIP]
> **Ripgrep / SQLite local index first, LLM synthesis second.**

### The Rule
When extracting textual citations from large philosophical repositories (such as `acim-secular/`):
- Do NOT let the LLM wander across directory trees using multi-turn directory scanning tools.
- Use a single deterministic command (`rg -n -C 2 "projection" ...`) to extract candidate line snippets.
- Feed the extracted snippets directly into Hermes in a single turn for synthesis.
- Reduces execution time from ~3 minutes to under 5 seconds.

---

## 4. Universal Instruction 4: Host-to-WSL Direct Invocation Standard

> [!IMPORTANT]
> **Always specify `--cd /root/workspaces/<repo>` when invoking `wsl.exe` from Windows PowerShell.**

```powershell
# Mandatory execution pattern:
wsl.exe -d Ubuntu -u root --cd /root/workspaces/<repo> -e <command>
```
Eliminates all `/mnt/c/` path translations and guarantees instant native ext4 execution.
