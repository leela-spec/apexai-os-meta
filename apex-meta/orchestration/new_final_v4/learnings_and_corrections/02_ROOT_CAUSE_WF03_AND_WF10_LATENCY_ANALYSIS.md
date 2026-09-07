# Root Cause Analysis: Latency Spikes in WF03 and WF10

**Document ID:** ALR-002  
**Date:** 2026-09-07  
**Location:** `apex-meta/orchestration/new_final_v4/learnings_and_corrections/`  

---

## 1. Incident Diagnosis: Workflow 03 (~11m 34s)

### Problem Description
WF03 (*"Transcendents" Workshop Concept & Curriculum Generator*) took 11 minutes and 34 seconds to complete—more than 30 times longer than the average workflow.

### Root Causes
1. **Monolithic Prompt Architecture**:
   The prompt requested Hermes to generate:
   - Module 1 (*The Lens of Perception*) with minute-by-minute breakdowns.
   - Module 2 (*Undoing Projection*) with minute-by-minute breakdowns.
   - Four full exercise scripts ("The Same Room, Two Worlds", "Event vs. Story Autopsy", "Trigger Reversal Workshop", "Withdrawal Letter").
   - Seven Agreements, distress titration safety protocols, and daily practice logs.
   This resulted in a massive ~20 KB (214 lines) single generation.
2. **Cloud SSE Stream Drop**:
   While streaming tokens from OpenRouter (`z-ai/glm-5.3-flash`), the connection timed out mid-stream. An incomplete payload containing malformed escape tokens was written to disk.
3. **Autonomous Self-Healing Recovery Overhead**:
   Hermes detected the corrupt stream, wiped the output file, and re-initiated the prompt from scratch. This doubled the total inference window and consumed unnecessary tokens.

### Remediation Protocol
- **Chunking by Module**: Never generate two complete 90-minute workshop modules in a single eval turn.
  - Call 1: Generate Module 1 (`modules_1.md`)
  - Call 2: Generate Module 2 (`modules_2.md`)
  - Call 3: Generate Facilitator Quick Reference (`modules_facilitator.md`)
- **Deterministic Pre-Scaffolding**: Python script writes the timing table and headers; Hermes fills in the exercise descriptions and scripts.

---

## 2. Incident Diagnosis: Workflow 10 (~3m 00s)

### Problem Description
WF10 (*ACIM Secular Cross-Reference & Text Extraction*) required ~3 minutes to find 3 definitions and write 1 paragraph.

### Root Causes
1. **Multi-Turn Agent Tool Calling over Cloud API**:
   Hermes executed as an autonomous agent in a 4-turn loop:
   - Turn 1: Directory traversal (`file` tool).
   - Turn 2: Text search (`grep` tool across markdown files).
   - Turn 3: Line verification (`read_file` tool to verify exact line citations).
   - Turn 4: Final synthesis generation.
2. **Roundtrip Network Overhead**:
   Each tool call turn required:
   - Local tool execution in WSL.
   - JSON serialization and network POST to OpenRouter over the public internet.
   - Remote model inference and response streaming back to WSL.
   With 4 sequential turns, latency multiplied fourfold.

### Remediation Protocol
- **Local SQLite / ripgrep Pre-Indexing**: Run a deterministic local search command (`rg -n -C 2 "projection" /root/workspaces/acim-secular`) in a single bash pipeline, then pass the matched snippets into Hermes for a single-turn synthesis.
- **Local LLM Backend**: Routing the turns through local Ollama (`qwen3.5:9b` on `localhost`) reduces network latency per turn from ~15s to <1s.
