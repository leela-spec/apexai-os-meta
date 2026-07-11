---
title: "Query: System 2 phase1 fallback compiled wiki"
page_type: query_output
kb_slug: "old-apex-full-orchestration-agent-kb-v2"
created_at: "2026-07-11T11:38:28Z"
confidence: "unknown"
claim_label: "source_backed_summary"
status: "active"
---

# Query: System 2 phase1 fallback compiled wiki

- KB: `old-apex-full-orchestration-agent-kb-v2`
- Backend: `sqlite_fts5_bm25`
- Stale status: `fresh`
- Generated: `2026-07-11T11:38:28Z`

## Evidence results

### 1. Claude Orchestration Implementation Brief

- Path: `wiki/summaries/claude-orchestration-implementation-brief.md`
- Heading: `Routes Here`
- Lines: `58-63`
- Confidence: `mixed`
- Claim label: `source_backed_summary`

>  ... route [System] 2 questions without a [wiki] page?; leads_to: ingest-analysis/[phase1]-agent-architecture.md; rationale: Phase 1 is the required [fallback] knowledge surface until [compiled] coverage ... 

### 2. Claude Orchestration Implementation Brief

- Path: `wiki/summaries/claude-orchestration-implementation-brief.md`
- Heading: `Uncertainty / Raw Source Reopen Triggers`
- Lines: `64-67`
- Confidence: `mixed`
- Claim label: `source_backed_summary`

>  ... No [compiled] [System] 2 [wiki] page exists in this KB. For [System] 2 questions, read ingest-analysis first, especially [phase1]-*.md, and do not claim [compiled] coverage.; source ... 

### 3. Meta Detective

- Path: `wiki/entities/meta-detective.md`
- Heading: `Macro`
- Lines: `20-21`
- Confidence: `high`
- Claim label: `source_backed_summary`

> ### Macro Protects the [system] from plausible but unsupported progress.

### 4. Agent Architecture, Isolation, and Intentional Overlap

- Path: `wiki/summaries/agent-architecture.md`
- Heading: `Macro`
- Lines: `27-29`
- Confidence: `high`
- Claim label: `source_backed_summary`

> ### Macro The [system] decomposes orchestration into intake, sequencing, strategy, investigation, knowledge placement, information design, workflow construction, AI/tool routing, and hygiene validation. No single agent is supposed to ... 

## Raw JSON

```json
{
  "backend": "sqlite_fts5_bm25",
  "fallback_error": null,
  "generated_at": "2026-07-11T11:38:28Z",
  "kb_slug": "old-apex-full-orchestration-agent-kb-v2",
  "policy": "read_only; derived indexes are not canonical",
  "query": "System 2 phase1 fallback compiled wiki",
  "result_count": 4,
  "results": [
    {
      "chunk_id": "7da059fe5a00f06fb3606fd6",
      "claim_label": "source_backed_summary",
      "confidence": "mixed",
      "end_line": 63,
      "heading": "Routes Here",
      "kb_slug": "old-apex-full-orchestration-agent-kb-v2",
      "page_type": "summary",
      "rel_path": "wiki/summaries/claude-orchestration-implementation-brief.md",
      "score": -11.230344282563362,
      "snippet": " ... route [System] 2 questions without a [wiki] page?; leads_to: ingest-analysis/[phase1]-agent-architecture.md; rationale: Phase 1 is the required [fallback] knowledge surface until [compiled] coverage ... ",
      "start_line": 58,
      "status": "active",
      "title": "Claude Orchestration Implementation Brief"
    },
    {
      "chunk_id": "15b5bcc1ae48b236b3782c07",
      "claim_label": "source_backed_summary",
      "confidence": "mixed",
      "end_line": 67,
      "heading": "Uncertainty / Raw Source Reopen Triggers",
      "kb_slug": "old-apex-full-orchestration-agent-kb-v2",
      "page_type": "summary",
      "rel_path": "wiki/summaries/claude-orchestration-implementation-brief.md",
      "score": -9.471084348056191,
      "snippet": " ... No [compiled] [System] 2 [wiki] page exists in this KB. For [System] 2 questions, read ingest-analysis first, especially [phase1]-*.md, and do not claim [compiled] coverage.; source ... ",
      "start_line": 64,
      "status": "active",
      "title": "Claude Orchestration Implementation Brief"
    },
    {
      "chunk_id": "65480c431cb251fb56230966",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 21,
      "heading": "Macro",
      "kb_slug": "old-apex-full-orchestration-agent-kb-v2",
      "page_type": "entity",
      "rel_path": "wiki/entities/meta-detective.md",
      "score": -3.384241381341332,
      "snippet": "### Macro\nProtects the [system] from plausible but unsupported progress.",
      "start_line": 20,
      "status": "active",
      "title": "Meta Detective"
    },
    {
      "chunk_id": "c3d013236ba505f645ebc685",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 29,
      "heading": "Macro",
      "kb_slug": "old-apex-full-orchestration-agent-kb-v2",
      "page_type": "summary",
      "rel_path": "wiki/summaries/agent-architecture.md",
      "score": -3.3230803925219106,
      "snippet": "### Macro\nThe [system] decomposes orchestration into intake, sequencing, strategy, investigation, knowledge placement, information design, workflow construction, AI/tool routing, and hygiene validation. No single agent is supposed to ... ",
      "start_line": 27,
      "status": "active",
      "title": "Agent Architecture, Isolation, and Intentional Overlap"
    }
  ],
  "stale": {
    "added": [],
    "deleted": [],
    "generated_at": "2026-07-11T11:38:17Z",
    "modified": [],
    "status": "fresh"
  }
}
```
