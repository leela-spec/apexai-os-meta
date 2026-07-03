---
title: "Query: token efficient handoff design"
page_type: query_output
kb_slug: "claude-code-orchestration-design"
created_at: "2026-07-03T09:28:10Z"
confidence: "unknown"
claim_label: "source_backed_summary"
status: "active"
---

# Query: token efficient handoff design

- KB: `claude-code-orchestration-design`
- Backend: `sqlite_fts5_bm25`
- Stale status: `fresh`
- Generated: `2026-07-03T09:28:10Z`

## Evidence results

### 1. Token-Efficient Information Design

- Path: `wiki/summaries/token-efficient-information-design.md`
- Heading: `Token-Efficient Information Design`
- Lines: `29-61`
- Confidence: `high`
- Claim label: `source_backed_summary`

> # [Token]-[Efficient] Information [Design]  ```yaml summary_id: [token]_[efficient]_information_[design] specialized_indexes:   - [token]_economy_and_information_[design]_index pattern: >   Store durable knowledge in small source-grounded files ... 

### 2. Low-Token Handoff Design

- Path: `wiki/concepts/low-token-handoff-design.md`
- Heading: `Low-Token Handoff Design`
- Lines: `29-49`
- Confidence: `high`
- Claim label: `source_backed_summary`

> # Low-[Token] [Handoff] [Design]  ```yaml pattern: "A [handoff] should carry pointers, claim status, and next action rather than replaying full evidence." used_when:   - "A downstream role needs enough ... 

### 3. Agent Handoff and Contract System

- Path: `wiki/summaries/agent-handoff-and-contract-system.md`
- Heading: `Agent Handoff and Contract System`
- Lines: `29-65`
- Confidence: `high`
- Claim label: `source_backed_summary`

> # Agent [Handoff] and Contract System  ```yaml summary_id: agent_[handoff]_and_contract_system specialized_indexes:   - [handoff]_contract_index   - [token]_economy_and_information_[design]_index pattern: >   Agents exchange bounded ... 

### 4. Packet Size Budget

- Path: `wiki/concepts/packet-size-budget.md`
- Heading: `Packet Size Budget`
- Lines: `24-44`
- Confidence: `medium`
- Claim label: `behavioral_inference`

>  ... used_when:   - "Designing [handoff], task, plan, recap, or query packets." not_used_when:   - "The packet is an archive or full evidence bundle by [design]." reads:   - "essential state"   - "refs ... 

### 5. Handoff Stop Conditions

- Path: `wiki/concepts/handoff-stop-conditions.md`
- Heading: `Handoff Stop Conditions`
- Lines: `24-45`
- Confidence: `high`
- Claim label: `source_backed_summary`

>  ... blocking assumptions"   - "required approvals"   - "source availability" writes:   - "stop or clarify marker"   - "blocked [handoff] status" [token]_efficiency:   - "A stop marker prevents long speculative continuation." drift_controls:   - "No silent fill ... 

## Raw JSON

```json
{
  "backend": "sqlite_fts5_bm25",
  "fallback_error": null,
  "generated_at": "2026-07-03T09:28:10Z",
  "kb_slug": "claude-code-orchestration-design",
  "policy": "read_only; derived indexes are not canonical",
  "query": "token efficient handoff design",
  "result_count": 5,
  "results": [
    {
      "chunk_id": "1068de101a669d6842d05949",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 61,
      "heading": "Token-Efficient Information Design",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "summary",
      "rel_path": "wiki/summaries/token-efficient-information-design.md",
      "score": -8.367164587088556,
      "snippet": "# [Token]-[Efficient] Information [Design]\n\n```yaml\nsummary_id: [token]_[efficient]_information_[design]\nspecialized_indexes:\n  - [token]_economy_and_information_[design]_index\npattern: >\n  Store durable knowledge in small source-grounded files ... ",
      "start_line": 29,
      "status": "active",
      "title": "Token-Efficient Information Design"
    },
    {
      "chunk_id": "57113ceff24115af12763e9b",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 49,
      "heading": "Low-Token Handoff Design",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "concept",
      "rel_path": "wiki/concepts/low-token-handoff-design.md",
      "score": -5.188633615163052,
      "snippet": "# Low-[Token] [Handoff] [Design]\n\n```yaml\npattern: \"A [handoff] should carry pointers, claim status, and next action rather than replaying full evidence.\"\nused_when:\n  - \"A downstream role needs enough ... ",
      "start_line": 29,
      "status": "active",
      "title": "Low-Token Handoff Design"
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
      "score": -3.9870977134993897,
      "snippet": "# Agent [Handoff] and Contract System\n\n```yaml\nsummary_id: agent_[handoff]_and_contract_system\nspecialized_indexes:\n  - [handoff]_contract_index\n  - [token]_economy_and_information_[design]_index\npattern: >\n  Agents exchange bounded ... ",
      "start_line": 29,
      "status": "active",
      "title": "Agent Handoff and Contract System"
    },
    {
      "chunk_id": "8b04bb55ca58249a3135e70b",
      "claim_label": "behavioral_inference",
      "confidence": "medium",
      "end_line": 44,
      "heading": "Packet Size Budget",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "concept",
      "rel_path": "wiki/concepts/packet-size-budget.md",
      "score": -3.2875499987317296,
      "snippet": " ... used_when:\n  - \"Designing [handoff], task, plan, recap, or query packets.\"\nnot_used_when:\n  - \"The packet is an archive or full evidence bundle by [design].\"\nreads:\n  - \"essential state\"\n  - \"refs ... ",
      "start_line": 24,
      "status": "active",
      "title": "Packet Size Budget"
    },
    {
      "chunk_id": "8b442ded685c8cb6273bd7eb",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 45,
      "heading": "Handoff Stop Conditions",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "concept",
      "rel_path": "wiki/concepts/handoff-stop-conditions.md",
      "score": -2.8873876492974104,
      "snippet": " ... blocking assumptions\"\n  - \"required approvals\"\n  - \"source availability\"\nwrites:\n  - \"stop or clarify marker\"\n  - \"blocked [handoff] status\"\n[token]_efficiency:\n  - \"A stop marker prevents long speculative continuation.\"\ndrift_controls:\n  - \"No silent fill ... ",
      "start_line": 24,
      "status": "active",
      "title": "Handoff Stop Conditions"
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
