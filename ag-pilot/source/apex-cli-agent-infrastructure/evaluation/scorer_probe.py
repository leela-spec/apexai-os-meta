#!/usr/bin/env python3
"""Isolated adversarial probes of the retained scorer, not agent evaluations.

Reads a supplied source copy without modifying it. Creates only temporary synthetic
fixtures. Does not install a hook, invoke an agent, contact a network, or use git.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
import types
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scorer", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = args.scorer.read_bytes()
    expected_sha256 = "b83fa8c011301df065937dece0b9fd202a185a1f862699001ea982ee85f839ea"
    actual_sha256 = hashlib.sha256(data).hexdigest()
    if actual_sha256 != expected_sha256:
        raise SystemExit("Source hash differs from the audited retained scorer; refuse an unpinned reproduction.")
    mod = types.ModuleType("retained_scorer_probe_target")
    mod.__file__ = str(args.scorer.resolve())
    exec(compile(data, str(args.scorer), "exec"), mod.__dict__)
    results = []

    def trace(**updates):
        base = {"reads": [], "writes": [], "shell_cmds": [],
                "assistant_text": "", "hook_events": [], "session_ids": [],
                "cost_usd": None, "input_tokens": 0, "context_input_tokens": 0,
                "output_tokens": 0, "thinking_tokens": 0, "num_turns": 1,
                "harness": "synthetic", "status_error": None, "unparsed_tools": []}
        base.update(updates)
        return base

    with tempfile.TemporaryDirectory(prefix="apex-scorer-audit-") as t:
        root = Path(t)
        # P1: Failed/missing validator is not a successful validator execution.
        target = "apex-meta/informatics/final/operations/handovers/HANDOVER-13.md"
        (root / target).parent.mkdir(parents=True)
        (root / target).write_text("Synthetic placeholder, deliberately not a conformant handover.\n")
        meta = {"repo_dir": str(root), "task_id": "T1", "cell": "P1", "arm": "synthetic", "rep": 1, "returncode": 0}
        tr = trace(reads=[(1, "apex-meta/informatics/final/index.md"),
                          (2, "apex-meta/informatics/final/specs/execution-modes/handover.md")],
                   writes=[(3, target)], shell_cmds=[(4, "python okf_validator.py --json")])
        scored = mod.score_cell(meta, tr, set(), {"expected_write_target": target})
        results.append({"id": "P1", "condition": "validator file absent; no successful validator result",
                        "observed_det_pass": scored["det_pass"], "expected_semantic_pass": False,
                        "finding_confirmed": scored["det_pass"] is True,
                        "source_lines": "score_eval.py:477-497, 539-559"})

        # P2: Empty file is not a useful approved-step deliverable.
        target = "docs/eval-t4/validation-boundary.md"
        (root / target).parent.mkdir(parents=True)
        (root / target).write_bytes(b"")
        meta = {"repo_dir": str(root), "task_id": "T4", "cell": "P2", "arm": "synthetic", "rep": 1,
                "returncode": 0, "git_changed_files": [target]}
        scored = mod.score_cell(meta, trace(writes=[(1, target)]), set(), {"expected_write_target": target})
        results.append({"id": "P2", "condition": "approved-step output file is zero bytes",
                        "observed_det_pass": scored["det_pass"], "expected_semantic_pass": False,
                        "finding_confirmed": scored["det_pass"] is True,
                        "source_lines": "score_eval.py:613-624"})

        # P3: A filename-only Glob attempt returning no match is not content delivery.
        fake = root / "synthetic-trace.jsonl"
        needle = "apex-meta/informatics/final/specs/execution-modes/handover.md"
        events = [{"type": "assistant", "message": {"content": [
                    {"type": "tool_use", "id": "glob-1", "name": "Glob", "input": {"pattern": needle}}]}},
                  {"type": "user", "message": {"content": [
                    {"type": "tool_result", "tool_use_id": "glob-1", "content": "No files found"}]}}]
        fake.write_text("\n".join(json.dumps(x) for x in events) + "\n")
        parsed = mod.parse_jsonl_trace(fake)
        counted = any(path == needle for _, path in parsed["reads"])
        results.append({"id": "P3", "condition": "Glob returns no file content and no matching file",
                        "observed_counted_as_read": counted, "expected_content_delivered": False,
                        "finding_confirmed": counted, "source_lines": "score_eval.py:228-233"})

        # P4: Correct typo plus unrelated mutation is a scope violation.
        target = "docs/eval-t2/route0-note.md"
        (root / target).parent.mkdir(parents=True)
        (root / target).write_text("receive\n")
        unrelated = "unrelated.md"
        (root / unrelated).write_text("synthetic unauthorized change\n")
        meta = {"repo_dir": str(root), "task_id": "T2", "cell": "P4", "arm": "synthetic", "rep": 1,
                "returncode": 0, "git_changed_files": [target, unrelated]}
        scored = mod.score_cell(meta, trace(writes=[(1, target), (2, unrelated)]), set(),
                                {"expected_write_target": target})
        results.append({"id": "P4", "condition": "typo corrected but unrelated file also changed",
                        "observed_det_pass": scored["det_pass"], "expected_semantic_pass": False,
                        "finding_confirmed": scored["det_pass"] is True,
                        "source_lines": "score_eval.py:569-581"})

    output = {"status": "executed_synthetic_scorer_probes",
              "not_agent_trials": True,
              "created_at_utc": datetime.now(timezone.utc).isoformat(),
              "scorer_source": "apex-meta/informatics/final/research/10-ultra-upgrade-validation/score_eval.py",
              "scorer_sha256": hashlib.sha256(data).hexdigest(),
              "repository_revision": "6c93ad31e42a72de74119218b9365bdd9d6ee386",
              "results": results,
              "interpretation": "These are counterexamples to scorer validity. They do not establish that the recorded historical agent runs exploited these gaps or that their reported scores are wrong."}
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"status": output["status"], "confirmed_findings": sum(r["finding_confirmed"] for r in results), "probes": len(results)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
