#!/usr/bin/env python3
"""
Atomic Fail-Closed Portfolio Rollup Publisher for Hermes Multi-Repo Orchestration v2.
Implements C03 deterministic publication with last-known-good preservation.
"""

import os
import sys
import json
import sqlite3
import datetime
import tempfile
import yaml
import subprocess

CONFIG = {
    "repos": {
        "apex": {
            "name": "Apex AIOS Meta",
            "repo": "leela-spec/apexai-os-meta",
            "branch": "main",
            "board": "apex",
            "path": "/mnt/c/GitDev/apexai-os-meta" if os.path.exists("/mnt/c/GitDev/apexai-os-meta") else r"C:\GitDev\apexai-os-meta",
            "wsl_path": "/root/workspaces/apexai-os-meta"
        },
        "masterofarts": {
            "name": "Master of Arts",
            "repo": "leela-spec/MasterOfArts",
            "branch": "main",
            "board": "masterofarts",
            "path": "/mnt/c/GitDev/MasterOfArts" if os.path.exists("/mnt/c/GitDev/MasterOfArts") else r"C:\GitDev\MasterOfArts",
            "wsl_path": "/root/workspaces/MasterOfArts"
        },
        "acim": {
            "name": "ACIM Secular",
            "repo": "leela-spec/acim-secular",
            "branch": "master",
            "board": "acim",
            "path": "/root/workspaces/acim-secular" if os.path.exists("/root/workspaces/acim-secular") else r"C:\GitDev\acim-secular",
            "wsl_path": "/root/workspaces/acim-secular"
        },
        "investment": {
            "name": "Investment",
            "repo": "leela-spec/Investment",
            "branch": "main",
            "board": "investment",
            "path": "/root/workspaces/Investment" if os.path.exists("/root/workspaces/Investment") else r"C:\GitDev\Investment",
            "wsl_path": "/root/workspaces/Investment"
        }
    },
    "output_snapshot_json": "apex-meta/orchestration/rollups/portfolio-snapshot.json",
    "output_snapshot_md": "apex-meta/orchestration/rollups/portfolio-snapshot.md",
    "output_health_yaml": "apex-meta/orchestration/rollups/health-receipt.yaml"
}

def get_git_info(repo_path, expected_branch):
    if not os.path.exists(repo_path):
        raise FileNotFoundError(f"Repo path does not exist: {repo_path}")
    
    try:
        branch = subprocess.check_output(["git", "-C", repo_path, "branch", "--show-current"], text=True).strip()
        head = subprocess.check_output(["git", "-C", repo_path, "rev-parse", "HEAD"], text=True).strip()
    except Exception as e:
        raise RuntimeError(f"Git query failed for {repo_path}: {e}")

    if branch != expected_branch:
        raise ValueError(f"Branch mismatch in {repo_path}: expected '{expected_branch}', found '{branch}'")

    return branch, head

def query_board_tasks(board_slug):
    db_path = f"/root/.hermes/kanban/boards/{board_slug}/kanban.db"
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Board database not found: {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, status, assignee, priority, created_at, completed_at FROM tasks WHERE status != 'archived'")
    rows = cursor.fetchall()
    conn.close()

    tasks = []
    for r in rows:
        tasks.append({
            "id": r[0],
            "title": r[1],
            "status": r[2],
            "assignee": r[3],
            "priority": r[4],
            "created_at": r[5],
            "completed_at": r[6]
        })
    return tasks

def generate_rollup(config, target_dir_base):
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    candidate = {
        "schema_version": 1,
        "program": "hermes_multi_repo_orchestration_v2",
        "generated_at": now,
        "status": "PASS",
        "repositories": {}
    }

    errors = []
    for slug, info in config["repos"].items():
        try:
            branch, head = get_git_info(info["path"], info["branch"])
            tasks = query_board_tasks(info["board"])
            candidate["repositories"][slug] = {
                "name": info["name"],
                "repo": info["repo"],
                "branch": branch,
                "head": head,
                "board": info["board"],
                "active_tasks_count": len(tasks),
                "tasks": tasks
            }
        except Exception as ex:
            errors.append(f"[{slug}] {str(ex)}")

    out_dir = os.path.join(target_dir_base, "apex-meta/orchestration/rollups")
    os.makedirs(out_dir, exist_ok=True)

    json_path = os.path.join(target_dir_base, config["output_snapshot_json"])
    md_path = os.path.join(target_dir_base, config["output_snapshot_md"])
    health_path = os.path.join(target_dir_base, config["output_health_yaml"])

    if errors:
        # Failure: write degraded health receipt, preserve last-known-good snapshot
        health_data = {
            "timestamp": now,
            "status": "DEGRADED_PUBLICATION_BLOCKED",
            "errors": errors,
            "last_known_good_preserved": os.path.exists(json_path)
        }
        with open(health_path, "w", encoding="utf-8") as f:
            yaml.dump(health_data, f, default_flow_style=False, sort_keys=False)
        return False, health_data

    # Success: Atomic publish via temp file + rename
    # 1. Write JSON
    temp_json = tempfile.NamedTemporaryFile("w", dir=out_dir, delete=False, encoding="utf-8")
    json.dump(candidate, temp_json, indent=2)
    temp_json.flush()
    temp_json.close()
    os.replace(temp_json.name, json_path)

    # 2. Write MD
    md_lines = [
        f"# Apex Portfolio Status Rollup Snapshot",
        f"",
        f"- Generated At: `{now}`",
        f"- Status: **HEALTHY**",
        f"",
        f"| Repository | Branch | HEAD | Board | Active Tasks |",
        f"|---|---|---|---|:--:|",
    ]
    for rslug, rdata in candidate["repositories"].items():
        md_lines.append(f"| {rdata['name']} (`{rdata['repo']}`) | `{rdata['branch']}` | `{rdata['head'][:10]}` | `{rdata['board']}` | {rdata['active_tasks_count']} |")

    temp_md = tempfile.NamedTemporaryFile("w", dir=out_dir, delete=False, encoding="utf-8")
    temp_md.write("\n".join(md_lines) + "\n")
    temp_md.flush()
    temp_md.close()
    os.replace(temp_md.name, md_path)

    # 3. Write healthy health receipt
    health_data = {
        "timestamp": now,
        "status": "HEALTHY",
        "errors": [],
        "snapshot_sha": candidate["repositories"]["apex"]["head"]
    }
    with open(health_path, "w", encoding="utf-8") as f:
        yaml.dump(health_data, f, default_flow_style=False, sort_keys=False)

    return True, candidate

if __name__ == "__main__":
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    success, res = generate_rollup(CONFIG, base)
    if success:
        print("Rollup published successfully.")
        sys.exit(0)
    else:
        print("Rollup failed; degraded health emitted:", res)
        sys.exit(1)
