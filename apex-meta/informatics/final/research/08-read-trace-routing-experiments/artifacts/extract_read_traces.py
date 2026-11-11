#!/usr/bin/env python3
"""Extract per-agent tool-call traces from Claude Code subagent transcripts.

Reads agent-<id>.jsonl files from the subagents folder of a session and prints one TSV row per tool call:
agent_id, arm, task, seq, tool, target. Duplicate events (the transcripts list every tool_use twice)
are removed by tool_use id. Nothing is inferred; the target is the file_path, path, pattern or command
the agent passed to the tool.

Usage:
    python extract_read_traces.py <subagents_dir> <mapping.tsv> > read-traces.tsv

mapping.tsv has three tab-separated columns per line: agent_id, arm, task.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def target(tool: str, inp: dict) -> str:
    for key in ("file_path", "path", "pattern", "command"):
        if inp.get(key):
            return str(inp[key]).replace("\t", " ").replace("\n", " ")[:300]
    return ""


def main(subagents_dir: str, mapping_file: str) -> int:
    rows = [line.rstrip("\n").split("\t") for line in Path(mapping_file).read_text(encoding="utf-8").splitlines() if line.strip()]
    print("agent_id\tarm\ttask\tseq\ttool\ttarget")
    for agent_id, arm, task in rows:
        path = Path(subagents_dir) / f"agent-{agent_id}.jsonl"
        seen: set[str] = set()
        seq = 0
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            msg = obj.get("message", obj)
            content = msg.get("content") if isinstance(msg, dict) else None
            if not isinstance(content, list):
                continue
            for block in content:
                if isinstance(block, dict) and block.get("type") == "tool_use":
                    tool_id = block.get("id", "")
                    if tool_id in seen:
                        continue
                    seen.add(tool_id)
                    seq += 1
                    print(f"{agent_id}\t{arm}\t{task}\t{seq}\t{block.get('name')}\t{target(block.get('name', ''), block.get('input', {}))}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
