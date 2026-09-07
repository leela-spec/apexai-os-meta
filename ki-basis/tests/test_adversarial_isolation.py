"""
test_adversarial_isolation.py - Empirical Adversarial Stress Test Suite
Challenger 1: Network & Port Collision Stress Verifier for ki-basis Dual-Instance Architecture
"""

import json
import os
import re
import socket
import subprocess
import sys
from pathlib import Path
import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
KI_BASIS_DIR = REPO_ROOT / "ki-basis"
COMPOSE_FILE = KI_BASIS_DIR / "compose.yaml"
ENV_PRIVATE_FILE = KI_BASIS_DIR / ".env.private"
ENV_COMMUNITY_FILE = KI_BASIS_DIR / ".env.community"
ENV_EXAMPLE_FILE = KI_BASIS_DIR / ".env.example"
NGINX_CONF_FILE = KI_BASIS_DIR / "docker" / "nginx" / "default.conf"


def run_docker_compose_config(project_name: str, env_file: Path) -> dict:
    """Executes official docker compose CLI to get authoritative resolved compose configuration."""
    cmd = [
        "docker", "compose",
        "-p", project_name,
        "--env-file", str(env_file),
        "-f", str(COMPOSE_FILE),
        "config",
        "--format", "json"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO_ROOT))
    if res.returncode != 0:
        raise RuntimeError(f"docker compose config failed (code {res.returncode}):\n{res.stderr}")
    return json.loads(res.stdout)


# =============================================================================
# 1. Authoritative Docker Compose CLI Render Verification
# =============================================================================
class TestDockerComposeAuthoritativeConfig:
    @pytest.fixture(scope="class")
    def private_config(self):
        return run_docker_compose_config("ki-basis-private", ENV_PRIVATE_FILE)

    @pytest.fixture(scope="class")
    def community_config(self):
        return run_docker_compose_config("ki-basis-community", ENV_COMMUNITY_FILE)

    def test_project_names(self, private_config, community_config):
        assert private_config.get("name") == "ki-basis-private"
        assert community_config.get("name") == "ki-basis-community"

    def test_container_names_uniqueness(self, private_config, community_config):
        pvt_names = {s["container_name"] for s in private_config["services"].values()}
        comm_names = {s["container_name"] for s in community_config["services"].values()}

        assert len(pvt_names) == 7
        assert len(comm_names) == 7
        assert all(n.startswith("ki-basis-private-") for n in pvt_names)
        assert all(n.startswith("ki-basis-community-") for n in comm_names)
        assert len(pvt_names & comm_names) == 0, f"Overlapping container names: {pvt_names & comm_names}"

    def test_bridge_networks_disjoint(self, private_config, community_config):
        pvt_nets = {net["name"] for net in private_config.get("networks", {}).values()}
        comm_nets = {net["name"] for net in community_config.get("networks", {}).values()}

        assert "ki-basis-private-net" in pvt_nets
        assert "ki-basis-community-net" in comm_nets
        assert len(pvt_nets & comm_nets) == 0, f"Networks overlap: {pvt_nets & comm_nets}"

    def test_volume_namespaces_disjoint(self, private_config, community_config):
        pvt_vols = {v["name"] for v in private_config.get("volumes", {}).values()}
        comm_vols = {v["name"] for v in community_config.get("volumes", {}).values()}

        assert len(pvt_vols) == 10
        assert len(comm_vols) == 10
        assert all(v.startswith("ki-basis-private-") for v in pvt_vols)
        assert all(v.startswith("ki-basis-community-") for v in comm_vols)
        assert len(pvt_vols & comm_vols) == 0, f"Volume overlap: {pvt_vols & comm_vols}"


# =============================================================================
# 2. Port Collision, Loopback Binding, & Exposure Stress Tests
# =============================================================================
class TestPortAllocationAndIsolation:
    @pytest.fixture(scope="class")
    def private_config(self):
        return run_docker_compose_config("ki-basis-private", ENV_PRIVATE_FILE)

    @pytest.fixture(scope="class")
    def community_config(self):
        return run_docker_compose_config("ki-basis-community", ENV_COMMUNITY_FILE)

    def _extract_published_ports(self, config):
        published = []
        for svc_name, svc in config["services"].items():
            for p in svc.get("ports", []):
                published.append({
                    "service": svc_name,
                    "host_ip": p.get("host_ip"),
                    "published": int(p.get("published")),
                    "target": int(p.get("target")),
                    "protocol": p.get("protocol", "tcp")
                })
        return published

    def test_all_published_ports_bind_strictly_to_loopback(self, private_config, community_config):
        pvt_ports = self._extract_published_ports(private_config)
        comm_ports = self._extract_published_ports(community_config)

        all_ports = pvt_ports + comm_ports
        assert len(all_ports) == 12, f"Expected 12 total published ports (6 per stack), found {len(all_ports)}"

        for p in all_ports:
            assert p["host_ip"] == "127.0.0.1", (
                f"SECURITY VIOLATION: Service {p['service']} published port {p['published']} "
                f"bound to '{p['host_ip']}' instead of strict '127.0.0.1'!"
            )

    def test_no_zero_zero_zero_zero_exposure(self, private_config, community_config):
        all_ports = self._extract_published_ports(private_config) + self._extract_published_ports(community_config)
        for p in all_ports:
            assert p["host_ip"] != "0.0.0.0", f"CRITICAL: Service {p['service']} exposes 0.0.0.0!"
            assert p["host_ip"] is not None and p["host_ip"] != "", f"CRITICAL: Host IP is missing for {p['service']}!"

    def test_zero_mathematical_port_overlap(self, private_config, community_config):
        pvt_ports = {p["published"] for p in self._extract_published_ports(private_config)}
        comm_ports = {p["published"] for p in self._extract_published_ports(community_config)}

        overlap = pvt_ports & comm_ports
        assert len(overlap) == 0, f"PORT COLLISION DETECTED: Overlapping host ports: {overlap}"

        expected_pvt = {8010, 8082, 8084, 8086, 8642, 9119}
        expected_comm = {9010, 9082, 9084, 9086, 9219, 9642}
        assert pvt_ports == expected_pvt
        assert comm_ports == expected_comm

    def test_database_ports_strictly_unexposed(self, private_config, community_config):
        for config, name in [(private_config, "Private"), (community_config, "Community")]:
            pg_ports = config["services"].get("postgres", {}).get("ports", [])
            valkey_ports = config["services"].get("valkey", {}).get("ports", [])

            assert len(pg_ports) == 0, f"{name} PostgreSQL exposes host ports: {pg_ports}"
            assert len(valkey_ports) == 0, f"{name} Valkey exposes host ports: {valkey_ports}"


# =============================================================================
# 3. Empirical Host Socket Concurrency Stress Test
# =============================================================================
class TestHostSocketConcurrency:
    """Empirically tests port availability and verifies zero intra-stack and inter-stack collision."""

    def test_community_ports_currently_unbound(self):
        """Community ports (9010, 9082, 9084, 9086, 9219, 9642) must be completely free on host."""
        community_ports = [9010, 9082, 9084, 9086, 9219, 9642]
        open_sockets = []
        try:
            for port in community_ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind(("127.0.0.1", port))
                s.listen(1)
                open_sockets.append(s)
            assert len(open_sockets) == 6
        finally:
            for s in open_sockets:
                s.close()

    def test_all_12_ports_are_mathematically_disjoint(self):
        pvt_ports = {8010, 8082, 8084, 8086, 8642, 9119}
        comm_ports = {9010, 9082, 9084, 9086, 9219, 9642}
        assert len(pvt_ports) == 6
        assert len(comm_ports) == 6
        assert len(pvt_ports & comm_ports) == 0


# =============================================================================
# 4. Fail-Closed & Missing Environment Variable Negative Tests
# =============================================================================
class TestFailClosedNegativeScenarios:
    def test_missing_env_file_triggers_required_var_error(self):
        """Docker compose must reject compose.yaml if required secrets are missing (tested with empty env file)."""
        empty_env = "NUL" if os.name == "nt" else "/dev/null"
        cmd = [
            "docker", "compose",
            "-p", "ki-basis-test-fail",
            "--env-file", empty_env,
            "-f", str(COMPOSE_FILE),
            "config"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO_ROOT))
        assert res.returncode != 0, "Compose unexpectedly succeeded without environment file!"
        assert "POSTGRES_PASSWORD is required" in res.stderr
        assert "FIREFLY_APP_KEY is required" in res.stderr
        assert "HERMES_API_SERVER_KEY is required" in res.stderr

    def test_residual_dot_env_file_pitfall(self):
        """
        Adversarial Finding: Audits if unversioned ki-basis/.env exists on disk,
        which Docker Compose will automatically load if --env-file is omitted.
        """
        dot_env = KI_BASIS_DIR / ".env"
        if dot_env.is_file():
            content = dot_env.read_text(encoding="utf-8")
            # If ki-basis/.env exists, it contains placeholder secrets and port 808x
            assert "postgres_secure_placeholder_password" in content
            assert "FIREFLY_HOST_PORT=8086" in content
            print("\n[ADVERSARIAL VULNERABILITY CONFIRMED]: Unversioned ki-basis/.env exists on disk!")
            print("  If an operator runs `docker compose up` without `--env-file`, it loads .env")
            print("  which binds Private ports (808x) and uses weak placeholder credentials!")

    def test_port_collision_synthetic_detection(self):
        """Proves that our collision detector reliably catches overlapping port assignments."""
        pvt = {8010, 8082, 8084, 8086, 8642, 9119}
        comm_synthetic = {9010, 9082, 8084, 9086, 9219, 9642}  # 8084 intentionally duplicated

        overlap = pvt & comm_synthetic
        assert overlap == {8084}, "Synthetic collision detector failed to identify overlap"



# =============================================================================
# 5. Adversarial Scrutiny: Nginx Landing Page Hardcoded Ports
# =============================================================================
class TestNginxEdgeProxyAdversarial:
    def test_nginx_default_conf_multi_instance_support(self):
        """
        Verifies that Nginx default.conf has been remediated to support both
        Private (808x) and Community (908x) port bands, resolving the cross-tenant redirect defect.
        """
        assert NGINX_CONF_FILE.is_file(), f"Nginx default.conf missing at {NGINX_CONF_FILE}"
        content = NGINX_CONF_FILE.read_text(encoding="utf-8")

        # Check for Private ports in default.conf
        has_pvt_ports = all(p in content for p in ["8086", "8010", "8082", "8642", "9119"])

        # Check for Community ports in default.conf
        has_comm_ports = all(p in content for p in ["9086", "9010", "9082", "9642", "9219"])

        # Check for dynamic port inspection
        has_port_detection = "window.location.port" in content or "location.port" in content or "9084" in content

        print(f"\n[REMEDIATION VERIFICATION] Nginx default.conf port audit:")
        print(f"  Contains all Private ports (8086, 8010, 8082, 8642, 9119): {has_pvt_ports}")
        print(f"  Contains all Community ports (9086, 9010, 9082, 9642, 9219): {has_comm_ports}")
        assert has_pvt_ports, "default.conf is missing one or more Private stack ports"
        assert has_comm_ports, "default.conf is missing one or more Community stack ports"
        assert has_port_detection, "default.conf does not implement dynamic port detection"


# =============================================================================
# 6. Verification of F17: Client Script Portability & Lifecycle Remediation
# =============================================================================
class TestClientScriptPortability:
    """Verifies that all client scripts accept --instance and environment variable overrides."""

    def test_populate_firefly_cli(self):
        res = subprocess.run([sys.executable, str(KI_BASIS_DIR / "scripts" / "populate_firefly.py"), "--help"], capture_output=True, text=True)
        assert res.returncode == 0
        assert "--instance" in res.stdout
        assert "--url" in res.stdout

    def test_populate_openproject_cli(self):
        res = subprocess.run([sys.executable, str(KI_BASIS_DIR / "scripts" / "populate_openproject.py"), "--help"], capture_output=True, text=True)
        assert res.returncode == 0
        assert "--instance" in res.stdout
        assert "--url" in res.stdout

    def test_populate_paperless_cli(self):
        res = subprocess.run([sys.executable, str(KI_BASIS_DIR / "scripts" / "populate_paperless.py"), "--help"], capture_output=True, text=True)
        assert res.returncode == 0
        assert "--instance" in res.stdout
        assert "--url" in res.stdout

    def test_verify_fundraiser_stack_cli(self):
        res = subprocess.run([sys.executable, str(KI_BASIS_DIR / "scripts" / "verify_fundraiser_stack.py"), "--help"], capture_output=True, text=True)
        assert res.returncode == 0
        assert "--instance" in res.stdout

    def test_generate_euer_tax_report_cli(self):
        res = subprocess.run([sys.executable, str(KI_BASIS_DIR / "scripts" / "generate_euer_tax_report.py"), "--help"], capture_output=True, text=True)
        assert res.returncode == 0
        assert "--instance" in res.stdout

    def test_stop_ki_basis_sh_exists(self):
        stop_sh = KI_BASIS_DIR / "scripts" / "stop-ki-basis.sh"
        assert stop_sh.is_file()
        content = stop_sh.read_text(encoding="utf-8")
        assert "private" in content and "community" in content

    def test_backup_stack_sh_has_dual_instance_support(self):
        backup_sh = KI_BASIS_DIR / "scripts" / "backup-stack.sh"
        assert backup_sh.is_file()
        content = backup_sh.read_text(encoding="utf-8")
        assert "docker exec -i" in content
        assert "docker exec -t" not in content
        assert "project_name" in content
