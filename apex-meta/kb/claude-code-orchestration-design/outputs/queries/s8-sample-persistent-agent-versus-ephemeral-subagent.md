---
title: "Query: persistent agent versus ephemeral subagent"
page_type: query_output
kb_slug: "claude-code-orchestration-design"
created_at: "2026-07-03T09:28:10Z"
confidence: "unknown"
claim_label: "source_backed_summary"
status: "active"
---

# Query: persistent agent versus ephemeral subagent

- KB: `claude-code-orchestration-design`
- Backend: `sqlite_fts5_bm25`
- Stale status: `fresh`
- Generated: `2026-07-03T09:28:10Z`

## Evidence results

### 1. Persistent Agent vs Ephemeral Subagent

- Path: `wiki/concepts/persistent-agent-vs-ephemeral-subagent.md`
- Heading: `Persistent Agent vs Ephemeral Subagent`
- Lines: `29-51`
- Confidence: `high`
- Claim label: `source_backed_summary`

> # [Persistent] [Agent] vs [Ephemeral] [Subagent]  ```yaml pattern: "[Persistent] agents hold stable repeated roles; [ephemeral] subagents isolate temporary or exploratory work and return compact results." used_when:   - "A domain ... 

### 2. Ephemeral Subagent Boundary

- Path: `wiki/concepts/ephemeral-subagent-boundary.md`
- Heading: `Ephemeral Subagent Boundary`
- Lines: `24-44`
- Confidence: `high`
- Claim label: `source_backed_summary`

> # [Ephemeral] [Subagent] Boundary  ```yaml pattern: "Use an [ephemeral] [subagent] for isolated temporary research, comparison, or exploration." used_when:   - "The task benefits from a separate context window and compact ... 

### 3. Production Agent Readiness Gate

- Path: `wiki/concepts/production-agent-readiness-gate.md`
- Heading: `Production Agent Readiness Gate`
- Lines: `24-49`
- Confidence: `medium`
- Claim label: `behavioral_inference`

>  ... candidate role is proposed for [persistent] production use." not_used_when:   - "The candidate can remain a skill, workflow stage, or [ephemeral] [subagent]." reads:   - "recurrence evidence"   - "stable owned scope ... 

### 4. Production Agent Readiness and Roster Boundary

- Path: `wiki/summaries/production-agent-readiness-and-roster-boundary.md`
- Heading: `Production Agent Readiness and Roster Boundary`
- Lines: `29-61`
- Confidence: `medium`
- Claim label: `source_backed_summary`

>  ... Final production [agent] roster."   - "[Agent]-specific KB folder convention."   - "Verifier loop implementation." ```  This page extends `[persistent]-[agent]-boundary.md` and `[persistent]-[agent]-vs-[ephemeral]-[subagent].md` without editing ... 

### 5. Claude Mechanism Decision Model

- Path: `wiki/summaries/claude-mechanism-decision-model.md`
- Heading: `Claude Mechanism Decision Model`
- Lines: `29-65`
- Confidence: `high`
- Claim label: `source_backed_summary`

>  ... mechanism_order:   - "markdown_or_yaml_artifact"   - "skill"   - "workflow"   - "[ephemeral]_[subagent]"   - "[persistent]_[agent]"   - "deterministic_script"   - "hook"   - "plugin_or_mcp_later" used_when:   - "Choosing between guidance, procedure, delegation, enforcement, packaging ... 

## Raw JSON

```json
{
  "backend": "sqlite_fts5_bm25",
  "fallback_error": null,
  "generated_at": "2026-07-03T09:28:10Z",
  "kb_slug": "claude-code-orchestration-design",
  "policy": "read_only; derived indexes are not canonical",
  "query": "persistent agent versus ephemeral subagent",
  "result_count": 5,
  "results": [
    {
      "chunk_id": "017c5a658e70abc738afd5a3",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 51,
      "heading": "Persistent Agent vs Ephemeral Subagent",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "concept",
      "rel_path": "wiki/concepts/persistent-agent-vs-ephemeral-subagent.md",
      "score": -13.013595038158998,
      "snippet": "# [Persistent] [Agent] vs [Ephemeral] [Subagent]\n\n```yaml\npattern: \"[Persistent] agents hold stable repeated roles; [ephemeral] subagents isolate temporary or exploratory work and return compact results.\"\nused_when:\n  - \"A domain ... ",
      "start_line": 29,
      "status": "active",
      "title": "Persistent Agent vs Ephemeral Subagent"
    },
    {
      "chunk_id": "8a56c7bae54310a009bf5a55",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 44,
      "heading": "Ephemeral Subagent Boundary",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "concept",
      "rel_path": "wiki/concepts/ephemeral-subagent-boundary.md",
      "score": -10.629871341667055,
      "snippet": "# [Ephemeral] [Subagent] Boundary\n\n```yaml\npattern: \"Use an [ephemeral] [subagent] for isolated temporary research, comparison, or exploration.\"\nused_when:\n  - \"The task benefits from a separate context window and compact ... ",
      "start_line": 24,
      "status": "active",
      "title": "Ephemeral Subagent Boundary"
    },
    {
      "chunk_id": "04e069fdcc6f9dea9e6d4c81",
      "claim_label": "behavioral_inference",
      "confidence": "medium",
      "end_line": 49,
      "heading": "Production Agent Readiness Gate",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "concept",
      "rel_path": "wiki/concepts/production-agent-readiness-gate.md",
      "score": -9.1853601580579,
      "snippet": " ... candidate role is proposed for [persistent] production use.\"\nnot_used_when:\n  - \"The candidate can remain a skill, workflow stage, or [ephemeral] [subagent].\"\nreads:\n  - \"recurrence evidence\"\n  - \"stable owned scope ... ",
      "start_line": 24,
      "status": "needs_review",
      "title": "Production Agent Readiness Gate"
    },
    {
      "chunk_id": "6c36d545e1b8a63d367c874f",
      "claim_label": "source_backed_summary",
      "confidence": "medium",
      "end_line": 61,
      "heading": "Production Agent Readiness and Roster Boundary",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "summary",
      "rel_path": "wiki/summaries/production-agent-readiness-and-roster-boundary.md",
      "score": -8.395215557059332,
      "snippet": " ... Final production [agent] roster.\"\n  - \"[Agent]-specific KB folder convention.\"\n  - \"Verifier loop implementation.\"\n```\n\nThis page extends `[persistent]-[agent]-boundary.md` and `[persistent]-[agent]-vs-[ephemeral]-[subagent].md` without editing ... ",
      "start_line": 29,
      "status": "needs_review",
      "title": "Production Agent Readiness and Roster Boundary"
    },
    {
      "chunk_id": "b3425074f5487969c4fe31ed",
      "claim_label": "source_backed_summary",
      "confidence": "high",
      "end_line": 65,
      "heading": "Claude Mechanism Decision Model",
      "kb_slug": "claude-code-orchestration-design",
      "page_type": "summary",
      "rel_path": "wiki/summaries/claude-mechanism-decision-model.md",
      "score": -8.080742847005096,
      "snippet": " ... mechanism_order:\n  - \"markdown_or_yaml_artifact\"\n  - \"skill\"\n  - \"workflow\"\n  - \"[ephemeral]_[subagent]\"\n  - \"[persistent]_[agent]\"\n  - \"deterministic_script\"\n  - \"hook\"\n  - \"plugin_or_mcp_later\"\nused_when:\n  - \"Choosing between guidance, procedure, delegation, enforcement, packaging ... ",
      "start_line": 29,
      "status": "active",
      "title": "Claude Mechanism Decision Model"
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
