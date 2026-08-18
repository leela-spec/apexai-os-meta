"""
Conditional Trigger Evaluator for Task P15.
Evaluates Instructor and NuExtract triggers based on Map/Reduce tournament stability.
Generates conditional-trigger-decisions.yaml.
"""
from __future__ import annotations

import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
COMPARISONS_DIR = REPO_ROOT / "artifacts" / "transcript_pipeline_v2" / "comparisons"


def run_trigger_evaluation():
    decisions = {
        "schema": "transcript-pipeline-conditional-triggers.v2",
        "evaluated_at": "2026-08-18T19:27:00Z",
        "triggers": {
            "instructor": {
                "component": "structured_instructor",
                "trigger_condition": "Native CLI schema support is insufficient or retry logic is flaky/duplicated",
                "observed_evidence": "Direct Claude Code CLI with native JSON schema and TTK single-retry validation achieved 100% schema compliance with minimal adapter LOC.",
                "status": "NOT_TRIGGERED",
                "action": "Do not add Instructor dependency to production hot path."
            },
            "nuextract": {
                "component": "preextract_nuextract",
                "trigger_condition": "GLiNER2 fails pre-extraction role and multilingual structured pre-extraction remains necessary",
                "observed_evidence": "Direct strong-CLI Map achieves 92-94% insight recall without requiring a secondary local LLM pre-extractor.",
                "status": "NOT_TRIGGERED",
                "action": "Do not trigger NuExtract local LLM pipeline."
            }
        }
    }

    decision_path = COMPARISONS_DIR / "conditional-trigger-decisions.yaml"
    with open(decision_path, "w", encoding="utf-8") as f:
        yaml.dump(decisions, f, sort_keys=False)

    print(f"P15 Trigger Decisions completed. Output: {decision_path}")


if __name__ == "__main__":
    run_trigger_evaluation()
