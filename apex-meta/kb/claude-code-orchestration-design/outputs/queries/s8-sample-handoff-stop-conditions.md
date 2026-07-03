---
title: "Query: handoff stop conditions"
page_type: query_output
kb_slug: "claude-code-orchestration-design"
created_at: "2026-07-03T09:28:11Z"
confidence: "unknown"
claim_label: "source_backed_summary"
status: "active"
---

# Query: handoff stop conditions

- KB: `claude-code-orchestration-design`
- Backend: `sqlite_fts5_bm25`
- Stale status: `fresh`
- Generated: `2026-07-03T09:28:11Z`

## Evidence results

### 1. Handoff Stop Conditions

- Path: `wiki/concepts/handoff-stop-conditions.md`
- Heading: `Handoff Stop Conditions`
- Lines: `24-45`
- Confidence: `high`
- Claim label: `source_backed_summary`

> # [Handoff] [Stop] [Conditions]  ```yaml pattern: "A [handoff] must state when the receiver should [stop] rather than infer missing context." used_when:   - "Missing source, authority, target, validation, or permission ... 

### 2. Agent Handoff and Contract System

- Path: `wiki/summaries/agent-handoff-and-contract-system.md`
- Heading: `Agent Handoff and Contract System`
- Lines: `29-65`
- Confidence: `high`
- Claim label: `source_backed_summary`

>  ... ownership from validator/operator acceptance."   - "Include [stop] [conditions] when evidence, risk, or authority is insufficient." unresolved_or_deferred:   - "Exact universal [handoff] packet schema remains a reusable contract target ... 

### 3. Stop Condition as Context Saver

- Path: `wiki/concepts/stop-condition-as-context-saver.md`
- Heading: `Stop Condition as Context Saver`
- Lines: `24-44`
- Confidence: `high`
- Claim label: `source_backed_summary`

>  ... required next proof" writes:   - "[stop] status"   - "one next required action" token_efficiency:   - "Stopping prevents speculative expansion and repeated repair passes." drift_controls:   - "[Stop] [conditions] make uncertainty visible instead ... 

### 4. Standard Handoff Packet

- Path: `wiki/concepts/standard-handoff-packet.md`
- Heading: `Standard Handoff Packet`
- Lines: `24-45`
- Confidence: `high`
- Claim label: `source_backed_summary`

>  ... refs"   - "candidate output" writes:   - "bounded [handoff] packet" token_efficiency:   - "References replace copied source bodies." drift_controls:   - "Authority, claim status, risk, and [stop] condition must be explicit." unresolved_or ... 

### 5. Scheduler Boundary

- Path: `wiki/concepts/scheduler-boundary.md`
- Heading: `Scheduler Boundary`
- Lines: `24-47`
- Confidence: `medium`
- Claim label: `behavioral_inference`

>  ... has not defined read/write contracts, [stop] [conditions], and operator gates." reads:   - "trigger condition"   - "eligible workflow or packet"   - "state source"   - "[stop] condition" writes:   - "run request or reminder candidate ... 

## Raw JSON

```json
{
  "backend": "sqlite_fts5_bm25",
  "fallback_error": null,
  "generated_at": "2026-07-03T09:28:11Z",
  "kb_slug": "claude-code-orchestration-design",
  "policy": "read_only; derived indexes are not canonical",
  "query": "handoff stop conditions",
  "result_count": 5,
  "results": [
    {
      "chunk_id": "8b442ded685c8cb6273bd7eb",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 45,
      "heading": "Handoff Stop Conditions",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "concept",
      "rel_path": "wiki/concepts/handoff-stop-conditions.md",
      "score": -9.586837473321,
      "snippet": "# [Handoff] [Stop] [Conditions]\n\n```yaml\npattern: \"A [handoff] must state when the receiver should [stop] rather than infer missing context.\"\nused_when:\n  - \"Missing source, authority, target, validation, or permission ... ",
      "start_line": 24,
      "status": "active",
      "title": "Handoff Stop Conditions"
    },
    {
      "chunk_id": "e42154c12bfe0a57980ee5f6",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 65,
      "heading": "Agent Handoff and Contract System",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "summary",
      "rel_path": "wiki/summaries/agent-handoff-and-contract-system.md",
      "score": -6.368933933259395,
      "snippet": " ... ownership from validator/operator acceptance.\"\n  - \"Include [stop] [conditions] when evidence, risk, or authority is insufficient.\"\nunresolved_or_deferred:\n  - \"Exact universal [handoff] packet schema remains a reusable contract target ... ",
      "start_line": 29,
      "status": "active",
      "title": "Agent Handoff and Contract System"
    },
    {
      "chunk_id": "cc75afe68b31cfe20f4d1870",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 44,
      "heading": "Stop Condition as Context Saver",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "concept",
      "rel_path": "wiki/concepts/stop-condition-as-context-saver.md",
      "score": -5.513152907395841,
      "snippet": " ... required next proof\"\nwrites:\n  - \"[stop] status\"\n  - \"one next required action\"\ntoken_efficiency:\n  - \"Stopping prevents speculative expansion and repeated repair passes.\"\ndrift_controls:\n  - \"[Stop] [conditions] make uncertainty visible instead ... ",
      "start_line": 24,
      "status": "active",
      "title": "Stop Condition as Context Saver"
    },
    {
      "chunk_id": "481ed9a86e7be077e62b86c0",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 45,
      "heading": "Standard Handoff Packet",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "concept",
      "rel_path": "wiki/concepts/standard-handoff-packet.md",
      "score": -4.6328351075490755,
      "snippet": " ... refs\"\n  - \"candidate output\"\nwrites:\n  - \"bounded [handoff] packet\"\ntoken_efficiency:\n  - \"References replace copied source bodies.\"\ndrift_controls:\n  - \"Authority, claim status, risk, and [stop] condition must be explicit.\"\nunresolved_or ... ",
      "start_line": 24,
      "status": "active",
      "title": "Standard Handoff Packet"
    },
    {
      "chunk_id": "0755c99d9503a2cbed017eb6",
      "claim_label": "behavioral_inference",
      "confidence": "medium",
      "end_line": 47,
      "heading": "Scheduler Boundary",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "concept",
      "rel_path": "wiki/concepts/scheduler-boundary.md",
      "score": -4.5244823278468065,
      "snippet": " ... has not defined read/write contracts, [stop] [conditions], and operator gates.\"\nreads:\n  - \"trigger condition\"\n  - \"eligible workflow or packet\"\n  - \"state source\"\n  - \"[stop] condition\"\nwrites:\n  - \"run request or reminder candidate ... ",
      "start_line": 24,
      "status": "needs_review",
      "title": "Scheduler Boundary"
    }
  ],
  "stale": {
    "added": [],
    "deleted": [],
    "generated_at": "2026-07-03T09:27:51Z",
    "modified": [],
    "status": "fresh"
  }
}
```
