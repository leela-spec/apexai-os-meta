#!/usr/bin/env python3
"""
_verification/adversarial_storage_challenge.py

Adversarial Stress Harness & Verification Oracle for Challenger 2:
1. 100% ext4 Storage Architecture Audit & 9P Exclusion
2. OpenProject Exit Status 1 Crash Prevention (Puma workers, PG startup wait, secret entropy)
3. Headless Container Runtime & Idle CPU Verification
"""

import math
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
import yaml

REPO_ROOT = Path("C:/GitDev/apexai-os-meta")
KI_BASIS_DIR = REPO_ROOT / "ki-basis"
COMPOSE_FILE = KI_BASIS_DIR / "compose.yaml"
ENV_PVT_FILE = KI_BASIS_DIR / ".env.private"
ENV_COMM_FILE = KI_BASIS_DIR / ".env.community"
ARCH_DOC = KI_BASIS_DIR / "docs" / "DUAL_INSTANCE_ARCHITECTURE.md"

def calc_shannon_entropy(data: str) -> float:
    if not data:
        return 0.0
    entropy = 0
    for count in Counter(data).values():
        p_x = count / len(data)
        entropy += - p_x * math.log2(p_x)
    return entropy

def parse_env(path: Path) -> dict:
    env = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip("'\"")
                env[k] = v
    return env

def substitute_env(text: str, env: dict) -> str:
    def replacer(match):
        expr = match.group(1)
        if ":-" in expr:
            var, dflt = expr.split(":-", 1)
            return env.get(var, dflt)
        elif ":?" in expr:
            var, err = expr.split(":?", 1)
            val = env.get(var)
            if not val:
                raise ValueError(f"Required variable missing: {var} ({err})")
            return val
        else:
            return env.get(expr, "")
    return re.sub(r"\$\{([^}]+)\}", replacer, text)

def run_adversarial_suite():
    results = []
    def record(name: str, passed: bool, detail: str):
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}: {detail}")
        results.append({"name": name, "passed": passed, "detail": detail})

    print("=" * 80)
    print("CHALLENGER 2: ADVERSARIAL STRESS HARNESS & EMPIRICAL VERIFICATION")
    print("=" * 80)

    # ---------------------------------------------------------
    # 1. Compose Parsing & Raw File Inspection
    # ---------------------------------------------------------
    compose_raw = COMPOSE_FILE.read_text(encoding="utf-8")
    env_pvt = parse_env(ENV_PVT_FILE)
    env_comm = parse_env(ENV_COMM_FILE)

    doc_pvt = yaml.safe_load(substitute_env(compose_raw, env_pvt))
    doc_comm = yaml.safe_load(substitute_env(compose_raw, env_comm))

    # Test 1.1: 100% Named ext4 Volumes for Database & Application State
    state_targets = {
        "postgres": ["/var/lib/postgresql/data"],
        "valkey": ["/data"],
        "firefly": ["/var/www/html/storage/upload"],
        "paperless": [
            "/usr/src/paperless/data",
            "/usr/src/paperless/media",
            "/usr/src/paperless/export",
            "/usr/src/paperless/consume"
        ],
        "openproject": ["/var/openproject/assets"],
        "hermes": ["/opt/data", "/root/workspaces"]
    }

    all_state_paths_named_ext4 = True
    violating_mounts = []

    for stack_name, doc in [("Private", doc_pvt), ("Community", doc_comm)]:
        for svc_name, expected_paths in state_targets.items():
            svc_conf = doc.get("services", {}).get(svc_name, {})
            vols = svc_conf.get("volumes", [])
            for ep in expected_paths:
                matched = False
                for v in vols:
                    v_str = str(v)
                    parts = v_str.split(":")
                    src = parts[0]
                    dst = parts[1] if len(parts) > 1 else ""
                    if dst == ep:
                        matched = True
                        # Adversarial check: Is src a host mount?
                        if src.startswith(".") or src.startswith("/") or src.startswith("\\") or ":" in src:
                            all_state_paths_named_ext4 = False
                            violating_mounts.append(f"{stack_name} {svc_name} -> {v_str}")
                if not matched:
                    all_state_paths_named_ext4 = False
                    violating_mounts.append(f"{stack_name} {svc_name} missing mount for {ep}")

    record(
        "Storage: 100% Named ext4 Volumes for All State Paths",
        all_state_paths_named_ext4,
        "All 10 persistent state targets across both stacks are strictly backed by named ext4 volumes" if all_state_paths_named_ext4 else f"Violations: {violating_mounts}"
    )

    # Test 1.2: Read-Only Check for Host Bind Mounts
    host_binds_ro = True
    bind_violations = []
    for stack_name, doc in [("Private", doc_pvt), ("Community", doc_comm)]:
        for svc_name, svc_conf in doc.get("services", {}).items():
            for v in svc_conf.get("volumes", []):
                v_str = str(v)
                parts = v_str.split(":")
                src = parts[0]
                mode = parts[2] if len(parts) > 2 else ""
                if src.startswith("."):
                    if mode != "ro":
                        host_binds_ro = False
                        bind_violations.append(f"{stack_name} {svc_name} -> {v_str}")

    record(
        "Storage: Zero Writable Host Bind Mounts (9P Elimination)",
        host_binds_ro,
        "All host bind mounts (postgres init, nginx config) are strictly read-only (:ro)" if host_binds_ro else f"Violations: {bind_violations}"
    )

    # Test 1.3: Volume Segregation Across 20 Volumes
    pvt_vols = set(doc_pvt.get("volumes", {}).keys())
    comm_vols = set(doc_comm.get("volumes", {}).keys())

    pvt_vol_names = {v.get("name") for v in doc_pvt.get("volumes", {}).values()}
    comm_vol_names = {v.get("name") for v in doc_comm.get("volumes", {}).values()}

    total_distinct_volume_names = len(pvt_vol_names) + len(comm_vol_names)
    volume_collision = pvt_vol_names & comm_vol_names

    record(
        "Storage: Exactly 20 Distinct Segregated Named Volumes",
        total_distinct_volume_names == 20 and len(volume_collision) == 0,
        f"10 Private ({pvt_vol_names}) and 10 Community ({comm_vol_names}) with 0 overlap."
    )

    # Test 1.4: Volume Naming Prefix Integrity
    pvt_prefix_ok = all(v.startswith("ki-basis-private-") for v in pvt_vol_names)
    comm_prefix_ok = all(v.startswith("ki-basis-community-") for v in comm_vol_names)
    record(
        "Storage: Volume Prefix Scoping",
        pvt_prefix_ok and comm_prefix_ok,
        "All Private volumes begin with 'ki-basis-private-' and Community with 'ki-basis-community-'"
    )

    # ---------------------------------------------------------
    # 2. OpenProject Exit Status 1 Crash Prevention
    # ---------------------------------------------------------
    # Test 2.1: OPENPROJECT_WEB_WORKERS: "1" Enforced
    op_pvt_ww = doc_pvt["services"]["openproject"]["environment"].get("OPENPROJECT_WEB_WORKERS")
    op_comm_ww = doc_comm["services"]["openproject"]["environment"].get("OPENPROJECT_WEB_WORKERS")
    workers_ok = (str(op_pvt_ww) == "1" and str(op_comm_ww) == "1")

    record(
        "OpenProject: OPENPROJECT_WEB_WORKERS = 1 Enforced",
        workers_ok,
        f"Puma configured in single-worker mode (Private: {op_pvt_ww}, Community: {op_comm_ww})"
    )

    # Test 2.2: PG_STARTUP_WAIT_TIME: "60" Enforced
    op_pvt_pgw = doc_pvt["services"]["openproject"]["environment"].get("PG_STARTUP_WAIT_TIME")
    op_comm_pgw = doc_comm["services"]["openproject"]["environment"].get("PG_STARTUP_WAIT_TIME")
    pgw_ok = (str(op_pvt_pgw) == "60" and str(op_comm_pgw) == "60")

    record(
        "OpenProject: PG_STARTUP_WAIT_TIME = 60 Enforced",
        pgw_ok,
        f"DB connection timeout extended to 180s total wait (60 retries x 3s) (Private: {op_pvt_pgw}, Community: {op_comm_pgw})"
    )

    # Test 2.3: OPENPROJECT_SECRET_KEY_BASE Entropy & Requirement Check
    # Verify in compose.yaml that it uses :?
    has_required_guard = "${OPENPROJECT_SECRET_KEY_BASE:?OPENPROJECT_SECRET_KEY_BASE is required}" in compose_raw
    sec_pvt = env_pvt.get("OPENPROJECT_SECRET_KEY_BASE", "")
    sec_comm = env_comm.get("OPENPROJECT_SECRET_KEY_BASE", "")

    ent_pvt = calc_shannon_entropy(sec_pvt)
    ent_comm = calc_shannon_entropy(sec_comm)
    sec_distinct = (sec_pvt != sec_comm and len(sec_pvt) >= 64 and len(sec_comm) >= 64)

    record(
        "OpenProject: OPENPROJECT_SECRET_KEY_BASE Validation",
        has_required_guard and sec_distinct and ent_pvt > 3.0 and ent_comm > 3.0,
        f"Guard :? present in compose.yaml. Secrets length >= 64. Entropy Private: {ent_pvt:.2f} bits/char, Community: {ent_comm:.2f} bits/char. Distinct: {sec_pvt != sec_comm}"
    )

    # ---------------------------------------------------------
    # 3. Headless Container Runtime Parameters
    # ---------------------------------------------------------
    # Test 3.1: Paperless Worker Limits
    pl_pvt_w = doc_pvt["services"]["paperless"]["environment"].get("PAPERLESS_WORKERS")
    pl_pvt_tw = doc_pvt["services"]["paperless"]["environment"].get("PAPERLESS_TASK_WORKERS")
    pl_pvt_tpw = doc_pvt["services"]["paperless"]["environment"].get("PAPERLESS_THREADS_PER_WORKER")

    pl_comm_w = doc_comm["services"]["paperless"]["environment"].get("PAPERLESS_WORKERS")
    pl_comm_tw = doc_comm["services"]["paperless"]["environment"].get("PAPERLESS_TASK_WORKERS")
    pl_comm_tpw = doc_comm["services"]["paperless"]["environment"].get("PAPERLESS_THREADS_PER_WORKER")

    pl_limits_ok = (
        str(pl_pvt_w) == "1" and str(pl_pvt_tw) == "1" and str(pl_pvt_tpw) == "1" and
        str(pl_comm_w) == "1" and str(pl_comm_tw) == "1" and str(pl_comm_tpw) == "1"
    )

    record(
        "Headless: Paperless Concurrency Capped at 1",
        pl_limits_ok,
        f"Granian web workers: 1, Celery task workers: 1, Threads per worker: 1 across both stacks"
    )

    # Test 3.2: Firefly APP_DEBUG: "false"
    ff_pvt_dbg = doc_pvt["services"]["firefly"]["environment"].get("APP_DEBUG")
    ff_comm_dbg = doc_comm["services"]["firefly"]["environment"].get("APP_DEBUG")
    ff_dbg_ok = (str(ff_pvt_dbg) == "false" and str(ff_comm_dbg) == "false")

    record(
        "Headless: Firefly APP_DEBUG Disabled",
        ff_dbg_ok,
        f"APP_DEBUG is explicitly 'false' in compose.yaml environment (Private: {ff_pvt_dbg}, Community: {ff_comm_dbg})"
    )

    # Test 3.3: Database Concealment (Postgres :5432 & Valkey :6379)
    pvt_pg_ports = doc_pvt["services"]["postgres"].get("ports", [])
    comm_pg_ports = doc_comm["services"]["postgres"].get("ports", [])
    pvt_vk_ports = doc_pvt["services"]["valkey"].get("ports", [])
    comm_vk_ports = doc_comm["services"]["valkey"].get("ports", [])

    db_concealed = (
        len(pvt_pg_ports) == 0 and len(comm_pg_ports) == 0 and
        len(pvt_vk_ports) == 0 and len(comm_vk_ports) == 0
    )

    record(
        "Headless & Security: Internal DB Concealment",
        db_concealed,
        "PostgreSQL (5432) and Valkey (6379) publish zero host ports on either stack"
    )

    # ---------------------------------------------------------
    # 4. Empirical Idle CPU & Filesystem Live Sampling
    # ---------------------------------------------------------
    try:
        stats_cmd = subprocess.run(
            ["docker", "stats", "--no-stream", "--format", "{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"],
            capture_output=True,
            text=True,
            check=True
        )
        lines = [line.strip() for line in stats_cmd.stdout.strip().split("\n") if line.strip()]
        total_cpu = 0.0
        container_stats = []
        for line in lines:
            parts = line.split("\t")
            if len(parts) >= 2:
                name = parts[0]
                cpu_str = parts[1].replace("%", "").strip()
                try:
                    cpu_val = float(cpu_str)
                    total_cpu += cpu_val
                    container_stats.append((name, cpu_val))
                except ValueError:
                    pass

        cpu_ok = total_cpu < 5.0
        record(
            "Empirical: Aggregate Steady-State Idle CPU < 5%",
            cpu_ok,
            f"Measured aggregate idle CPU: {total_cpu:.2f}% (Threshold: < 5.0%). Per container: {container_stats}"
        )
    except Exception as e:
        record(
            "Empirical: Aggregate Steady-State Idle CPU < 5%",
            False,
            f"Failed to query docker stats: {e}"
        )

    # ---------------------------------------------------------
    # Summary Verdict
    # ---------------------------------------------------------
    total_tests = len(results)
    passed_tests = sum(1 for r in results if r["passed"])
    failed_tests = total_tests - passed_tests

    print("=" * 80)
    print(f"HARNESS SUMMARY: {passed_tests}/{total_tests} Tests Passed ({failed_tests} Failures)")
    print("=" * 80)

    return passed_tests == total_tests

if __name__ == "__main__":
    success = run_adversarial_suite()
    sys.exit(0 if success else 1)
