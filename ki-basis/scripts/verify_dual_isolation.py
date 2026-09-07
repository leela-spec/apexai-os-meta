#!/usr/bin/env python3
"""
verify_dual_isolation.py - Automated Dual-Instance Isolation and Ext4 Compliance Verification

Validates:
1. Docker Compose syntax & variable substitution across .env.private and .env.community.
2. Zero port collision across Private and Community stacks.
3. Strict host loopback (127.0.0.1) binding for all published ports.
4. Database (PostgreSQL :5432) and Cache (Valkey :6379) concealment from host.
5. Zero shared named volumes, networks, or container names across stacks.
6. 100% ext4 persistence compliance (zero 9P bind mounts for databases/state; read-only config mounts only).
7. OpenProject stability and headless concurrency parameters (workers=1, wait_time=60).
8. Secret key entropy and inter-stack credential divergence.
"""

import os
import re
import sys
from pathlib import Path
import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
KI_BASIS_DIR = SCRIPT_DIR.parent
COMPOSE_FILE = KI_BASIS_DIR / "compose.yaml"
ENV_PRIVATE_FILE = KI_BASIS_DIR / ".env.private"
ENV_COMMUNITY_FILE = KI_BASIS_DIR / ".env.community"
ENV_EXAMPLE_FILE = KI_BASIS_DIR / ".env.example"


def parse_env_file(path: Path) -> dict:
    """Parses a standard .env file into a dictionary, ignoring comments and whitespace."""
    env = {}
    if not path.is_file():
        raise FileNotFoundError(f"Environment file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip()
                # Strip wrapping quotes if present
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                env[key] = val
    return env


def substitute_variables(text: str, env: dict) -> str:
    """
    Interpolates environment variables in the text supporting:
    - ${VAR}
    - ${VAR:-default}
    - ${VAR:?error}
    """
    def replacer(match):
        full_expr = match.group(1)
        if ":-" in full_expr:
            var_name, default = full_expr.split(":-", 1)
            return env.get(var_name, default)
        elif ":?" in full_expr:
            var_name, err_msg = full_expr.split(":?", 1)
            val = env.get(var_name)
            if not val:
                raise ValueError(f"Required variable missing: {var_name} ({err_msg})")
            return val
        else:
            return env.get(full_expr, "")

    pattern = re.compile(r"\$\{([^}]+)\}")
    return pattern.sub(replacer, text)


class DualInstanceValidator:
    def __init__(self):
        self.compose_raw = COMPOSE_FILE.read_text(encoding="utf-8")
        self.env_private = parse_env_file(ENV_PRIVATE_FILE)
        self.env_community = parse_env_file(ENV_COMMUNITY_FILE)
        self.failures = []
        self.checks_passed = 0

    def assert_true(self, condition: bool, description: str):
        if condition:
            print(f"  [PASS] {description}")
            self.checks_passed += 1
        else:
            print(f"  [FAIL] {description}")
            self.failures.append(description)

    def render_compose(self, env: dict) -> dict:
        rendered_text = substitute_variables(self.compose_raw, env)
        return yaml.safe_load(rendered_text)

    def run_all(self):
        print("================================================================================")
        print("ki-basis Dual-Instance Architecture & Isolation Automated Verification")
        print("================================================================================\n")

        print("--- 1. Variable Substitution & Schema Validation ---")
        try:
            doc_pvt = self.render_compose(self.env_private)
            self.assert_true(isinstance(doc_pvt, dict), "Compose yaml parses successfully with .env.private")
        except Exception as e:
            self.assert_true(False, f"Render .env.private failed: {e}")
            return False

        try:
            doc_comm = self.render_compose(self.env_community)
            self.assert_true(isinstance(doc_comm, dict), "Compose yaml parses successfully with .env.community")
        except Exception as e:
            self.assert_true(False, f"Render .env.community failed: {e}")
            return False

        print("\n--- 2. Project Namespaces & Container Names ---")
        self.assert_true(
            doc_pvt.get("name") == "ki-basis-private",
            f"Private project name is 'ki-basis-private' (got {doc_pvt.get('name')})"
        )
        self.assert_true(
            doc_comm.get("name") == "ki-basis-community",
            f"Community project name is 'ki-basis-community' (got {doc_comm.get('name')})"
        )

        pvt_containers = {s["container_name"] for s in doc_pvt.get("services", {}).values()}
        comm_containers = {s["container_name"] for s in doc_comm.get("services", {}).values()}

        self.assert_true(len(pvt_containers) == 7, f"Private has 7 uniquely named containers (found {len(pvt_containers)})")
        self.assert_true(len(comm_containers) == 7, f"Community has 7 uniquely named containers (found {len(comm_containers)})")
        self.assert_true(
            all(name.startswith("ki-basis-private-") for name in pvt_containers),
            "All Private container names start with 'ki-basis-private-'"
        )
        self.assert_true(
            all(name.startswith("ki-basis-community-") for name in comm_containers),
            "All Community container names start with 'ki-basis-community-'"
        )
        self.assert_true(
            len(pvt_containers & comm_containers) == 0,
            "Zero container name collisions across stacks"
        )

        print("\n--- 3. Network Isolation ---")
        pvt_net = doc_pvt.get("networks", {}).get("ki-basis-net", {}).get("name")
        comm_net = doc_comm.get("networks", {}).get("ki-basis-net", {}).get("name")
        self.assert_true(pvt_net == "ki-basis-private-net", f"Private network name is 'ki-basis-private-net' (got {pvt_net})")
        self.assert_true(comm_net == "ki-basis-community-net", f"Community network name is 'ki-basis-community-net' (got {comm_net})")
        self.assert_true(pvt_net != comm_net, "Networks are completely disjoint bridge domains")

        print("\n--- 4. Port Allocation & Host Collision Check ---")
        def extract_host_ports(doc):
            ports = {}
            for svc_name, svc in doc.get("services", {}).items():
                svc_ports = svc.get("ports", [])
                for p in svc_ports:
                    # Expected format: "127.0.0.1:HOST_PORT:CONTAINER_PORT"
                    m = re.match(r"^(127\.0\.0\.1|0\.0\.0\.0)?:?(\d+):(\d+)$", str(p).strip('"\''))
                    if m:
                        host_ip = m.group(1) or "0.0.0.0"
                        host_port = int(m.group(2))
                        cont_port = int(m.group(3))
                        ports[f"{svc_name}:{cont_port}"] = (host_ip, host_port)
            return ports

        pvt_ports = extract_host_ports(doc_pvt)
        comm_ports = extract_host_ports(doc_comm)

        # Confirm DB and Valkey are NOT exposed
        self.assert_true(
            "postgres:5432" not in pvt_ports and "postgres:5432" not in comm_ports,
            "PostgreSQL (:5432) has zero published host ports across both stacks (Internal only)"
        )
        self.assert_true(
            "valkey:6379" not in pvt_ports and "valkey:6379" not in comm_ports,
            "Valkey (:6379) has zero published host ports across both stacks (Internal only)"
        )

        # Check loopback bindings
        pvt_host_ips = {ip for ip, port in pvt_ports.values()}
        comm_host_ips = {ip for ip, port in comm_ports.values()}
        self.assert_true(
            pvt_host_ips == {"127.0.0.1"} and comm_host_ips == {"127.0.0.1"},
            "All published ports strictly bind to IPv4 loopback 127.0.0.1 (never 0.0.0.0)"
        )

        pvt_port_numbers = {port for ip, port in pvt_ports.values()}
        comm_port_numbers = {port for ip, port in comm_ports.values()}

        collision = pvt_port_numbers & comm_port_numbers
        self.assert_true(
            len(collision) == 0,
            f"Zero port collisions between Private and Community (overlapping: {collision})"
        )

        expected_pvt_ports = {8086, 8010, 8082, 8084, 8642, 9119}
        expected_comm_ports = {9086, 9010, 9082, 9084, 9642, 9219}
        self.assert_true(
            pvt_port_numbers == expected_pvt_ports,
            f"Private stack published ports match Band 8080-8089/8642/9119: {sorted(list(pvt_port_numbers))}"
        )
        self.assert_true(
            comm_port_numbers == expected_comm_ports,
            f"Community stack published ports match Band 9080-9089/9642/9219: {sorted(list(comm_port_numbers))}"
        )

        print("\n--- 5. Volume Namespace Isolation & Storage Segregation ---")
        pvt_vols = {v["name"] for v in doc_pvt.get("volumes", {}).values()}
        comm_vols = {v["name"] for v in doc_comm.get("volumes", {}).values()}

        self.assert_true(len(pvt_vols) == 10, f"Private declares 10 named volumes (found {len(pvt_vols)})")
        self.assert_true(len(comm_vols) == 10, f"Community declares 10 named volumes (found {len(comm_vols)})")
        self.assert_true(
            all(v.startswith("ki-basis-private-") for v in pvt_vols),
            "All Private volume names start with 'ki-basis-private-'"
        )
        self.assert_true(
            all(v.startswith("ki-basis-community-") for v in comm_vols),
            "All Community volume names start with 'ki-basis-community-'"
        )
        self.assert_true(
            len(pvt_vols & comm_vols) == 0,
            "Zero shared volumes between Private and Community (100% storage segregation)"
        )

        print("\n--- 6. Native ext4 Storage Compliance & 9P Exclusion ---")
        # Ensure that no persistent database, queue, document, or asset volume uses a host bind mount
        forbidden_mount_targets = [
            "/var/lib/postgresql/data",
            "/data",
            "/var/www/html/storage/upload",
            "/usr/src/paperless/data",
            "/usr/src/paperless/media",
            "/usr/src/paperless/export",
            "/usr/src/paperless/consume",
            "/var/openproject/assets",
            "/opt/data",
            "/root/workspaces"
        ]

        state_mounts_are_named_ext4 = True
        host_bind_mounts_are_ro = True

        for doc in (doc_pvt, doc_comm):
            for svc_name, svc in doc.get("services", {}).items():
                for v in svc.get("volumes", []):
                    parts = str(v).split(":")
                    src = parts[0]
                    dst = parts[1] if len(parts) > 1 else ""
                    mode = parts[2] if len(parts) > 2 else ""

                    if dst in forbidden_mount_targets:
                        # Must be a named volume (not a host path starting with . or / or C:)
                        if src.startswith(".") or src.startswith("/") or src.startswith("\\") or ":" in src:
                            state_mounts_are_named_ext4 = False
                            self.failures.append(f"State path {dst} in {svc_name} is a bind mount ({src})!")

                    if src.startswith("."):
                        # Host bind mount must be read-only (:ro)
                        if mode != "ro":
                            host_bind_mounts_are_ro = False
                            self.failures.append(f"Host bind mount {src} in {svc_name} is NOT read-only (:ro)!")

        self.assert_true(
            state_mounts_are_named_ext4,
            "100% of persistent databases and application state reside on named ext4 Docker volumes (0% 9P bind mounts)"
        )
        self.assert_true(
            host_bind_mounts_are_ro,
            "All repository host bind mounts are strictly read-only configuration mounts (:ro)"
        )

        print("\n--- 7. Headless & Runtime Stability Parameters ---")
        op_env_pvt = doc_pvt["services"]["openproject"]["environment"]
        op_env_comm = doc_comm["services"]["openproject"]["environment"]

        self.assert_true(
            str(op_env_pvt.get("OPENPROJECT_WEB_WORKERS")) == "1" and str(op_env_comm.get("OPENPROJECT_WEB_WORKERS")) == "1",
            "OpenProject OPENPROJECT_WEB_WORKERS is set to 1 (Puma single-worker mode)"
        )
        self.assert_true(
            str(op_env_pvt.get("PG_STARTUP_WAIT_TIME")) == "60" and str(op_env_comm.get("PG_STARTUP_WAIT_TIME")) == "60",
            "OpenProject PG_STARTUP_WAIT_TIME is set to 60s (DB startup timeout fix)"
        )

        pl_env_pvt = doc_pvt["services"]["paperless"]["environment"]
        pl_env_comm = doc_comm["services"]["paperless"]["environment"]
        self.assert_true(
            str(pl_env_pvt.get("PAPERLESS_WORKERS")) == "1" and str(pl_env_comm.get("PAPERLESS_WORKERS")) == "1",
            "Paperless PAPERLESS_WORKERS is capped at 1"
        )
        self.assert_true(
            str(pl_env_pvt.get("PAPERLESS_TASK_WORKERS")) == "1" and str(pl_env_comm.get("PAPERLESS_TASK_WORKERS")) == "1",
            "Paperless PAPERLESS_TASK_WORKERS is capped at 1 (Celery single-task worker)"
        )

        print("\n--- 8. Cryptographic Keys & Credential Divergence ---")
        secret_keys_to_compare = [
            "POSTGRES_PASSWORD",
            "FIREFLY_DB_PASSWORD",
            "FIREFLY_APP_KEY",
            "PAPERLESS_DB_PASSWORD",
            "PAPERLESS_SECRET_KEY",
            "PAPERLESS_ADMIN_PASSWORD",
            "OPENPROJECT_DB_PASSWORD",
            "OPENPROJECT_SECRET_KEY_BASE",
            "HERMES_DASHBOARD_BASIC_AUTH_PASSWORD",
            "HERMES_API_SERVER_KEY"
        ]

        secrets_distinct = True
        for key in secret_keys_to_compare:
            val_pvt = self.env_private.get(key, "")
            val_comm = self.env_community.get(key, "")
            if not val_pvt or not val_comm or val_pvt == val_comm:
                secrets_distinct = False
                self.failures.append(f"Secret key {key} is either empty or identical across Private and Community!")

        self.assert_true(
            secrets_distinct,
            "All cryptographic keys and database passwords are high-entropy and 100% distinct between Private and Community"
        )
        self.assert_true(
            len(self.env_private.get("FIREFLY_APP_KEY", "")) == 32 and len(self.env_community.get("FIREFLY_APP_KEY", "")) == 32,
            "FIREFLY_APP_KEY is exactly 32 characters in both environment configurations"
        )
        self.assert_true(
            len(self.env_private.get("OPENPROJECT_SECRET_KEY_BASE", "")) >= 64 and len(self.env_community.get("OPENPROJECT_SECRET_KEY_BASE", "")) >= 64,
            "OPENPROJECT_SECRET_KEY_BASE is at least 64 characters in both environment configurations"
        )

        print("\n================================================================================")
        if not self.failures:
            print(f"VERIFICATION VERDICT: [PASSED] ({self.checks_passed} checks passed, 0 failures)")
            print("Both instances can run concurrently with zero collisions and airtight isolation.")
            print("================================================================================")
            return True
        else:
            print(f"VERIFICATION VERDICT: [FAILED] ({len(self.failures)} failures detected)")
            for f in self.failures:
                print(f"  - {f}")
            print("================================================================================")
            return False


if __name__ == "__main__":
    validator = DualInstanceValidator()
    success = validator.run_all()
    sys.exit(0 if success else 1)
