"""
Semantic CLI Adapter for Strong Subscription-CLI Workers.
Supports Claude Code CLI (primary), Codex CLI, and Antigravity CLI.
Enforces child environment sanitization, atomic receipts, and fail-closed validation.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts" / "transcript_pipeline_v2"))
sys.path.insert(0, str(REPO_ROOT / ".claude" / "skills" / "transcript-to-knowledge" / "scripts"))

from receipt import ExecutionReceipt, write_atomic_receipt, utc_now_iso
import ttk_base
import ttk_map
import ttk_verify


class ProviderUnavailableError(RuntimeError):
    pass


class SemanticExecutionError(RuntimeError):
    pass


def get_sanitized_env() -> dict[str, str]:
    """Create child process environment with API keys stripped to enforce subscription CLI session."""
    env = os.environ.copy()
    keys_to_remove = [
        "ANTHROPIC_API_KEY",
        "ANTHROPIC_AUTH_TOKEN",
        "ANTHROPIC_BASE_URL",
        "OPENAI_API_KEY",
        "GEMINI_API_KEY",
        "GOOGLE_API_KEY",
    ]
    for k in keys_to_remove:
        env.pop(k, None)
    return env


def extract_json_block(text: str) -> dict[str, Any]:
    """Extract and parse pure JSON or fenced JSON codeblock."""
    text = text.strip()
    if not text:
        raise ValueError("Empty output from semantic worker")
    
    # Try parsing direct JSON
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Search for markdown fenced json block
    matches = re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if matches:
        for m in reversed(matches):
            try:
                return json.loads(m)
            except json.JSONDecodeError:
                continue

    # Search for any outer JSON object bounds
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return json.loads(text[start : end + 1])

    raise ValueError("Could not extract valid JSON object from output")


class SemanticCLIWorker:

    def __init__(self, provider: str = "claude", timeout_seconds: int = 180):
        self.provider = provider.lower()
        self.timeout_seconds = timeout_seconds
        self._check_provider_availability()

    def _check_provider_availability(self) -> None:
        if self.provider == "claude":
            if not shutil.which("claude"):
                raise ProviderUnavailableError("claude CLI executable not found on PATH (BLOCKED_FOR_TRIAL1)")
        elif self.provider == "codex":
            if not shutil.which("codex"):
                raise ProviderUnavailableError("codex CLI executable not found on PATH (BLOCKED_FOR_TRIAL1)")
        elif self.provider == "antigravity":
            if not shutil.which("agy"):
                raise ProviderUnavailableError("agy CLI executable not found on PATH (BLOCKED_FOR_TRIAL1)")
        else:
            raise ProviderUnavailableError(f"Unknown provider '{self.provider}'")

    def _build_command(self, prompt: str) -> list[str]:
        if self.provider == "claude":
            # Use noninteractive print mode with tools disabled and no session persistence
            return ["claude", "-p", prompt, "--tools", "", "--no-session-persistence"]
        elif self.provider == "codex":
            return ["codex", "exec", prompt]
        elif self.provider == "antigravity":
            return ["agy", "-p", prompt]
        raise ProviderUnavailableError(f"Cannot build command for provider '{self.provider}'")

    def invoke_raw(self, prompt: str) -> tuple[int, str, str, float]:
        """Invoke CLI worker subprocess with sanitized environment and timeout."""
        cmd = self._build_command(prompt)
        env = get_sanitized_env()
        t0 = time.time()
        
        proc = subprocess.Popen(
            cmd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,
            shell=False,
        )
        try:
            stdout, stderr = proc.communicate(timeout=self.timeout_seconds)
            wall_time = time.time() - t0
            return proc.returncode, stdout, stderr, wall_time
        except subprocess.TimeoutExpired:
            proc.kill()
            stdout, stderr = proc.communicate()
            wall_time = time.time() - t0
            return -1, stdout, f"Timeout after {self.timeout_seconds}s: {stderr}", wall_time

    def execute_map(
        self,
        packet: dict[str, Any],
        lookup: dict[str, dict[str, Any]],
        receipt_path: Path | None = None,
        max_retries: int = 1
    ) -> dict[str, Any]:
        """Execute Map extraction with up to 1 validation-informed retry."""
        packet_json = json.dumps(packet, indent=2, ensure_ascii=False)
        prompt_tmpl = (REPO_ROOT / "scripts" / "transcript_pipeline_v2" / "prompts" / "map.md").read_text(encoding="utf-8")
        base_prompt = prompt_tmpl.replace("{PACKET_JSON}", packet_json)

        attempts = 0
        prompt = base_prompt
        last_error = None
        input_hash = packet.get("packet_sha256") or hashlib.sha256(packet_json.encode("utf-8")).hexdigest()

        while attempts <= max_retries:
            attempts += 1
            code, stdout, stderr, wall_time = self.invoke_raw(prompt)
            
            if code != 0:
                last_error = f"CLI process exited with non-zero code {code}: {stderr}"
                if attempts > max_retries:
                    break
                prompt = f"{base_prompt}\n\n[Previous attempt failed with CLI error: {stderr[:300]}. Please return ONLY valid JSON.]"
                continue

            try:
                result = extract_json_block(stdout)
            except Exception as exc:
                last_error = f"Failed to parse JSON output: {exc}"
                if attempts > max_retries:
                    break
                prompt = f"{base_prompt}\n\n[Previous output was not valid JSON ({exc}). Return ONLY the raw JSON object adhering to ttk.map-result.v2.]"
                continue

            # Validate against TTK Map rules
            validation_errors = ttk_map.validate_map_result(packet, result, lookup)
            if not validation_errors:
                # Valid!
                output_hash = hashlib.sha256(json.dumps(result, sort_keys=True).encode("utf-8")).hexdigest()
                if receipt_path:
                    receipt = ExecutionReceipt(receipt_path, task_id="map_invocation", config={"provider": self.provider})
                    receipt.complete(
                        exit_code=0,
                        input_hash=input_hash,
                        output_hash=output_hash,
                        status="PASS",
                        attempts=attempts,
                        wall_time_seconds=round(wall_time, 4),
                        provider=self.provider,
                        transport="subscription_cli"
                    )
                return result

            last_error = f"TTK Validation errors: {'; '.join(validation_errors)}"
            if attempts > max_retries:
                break
            prompt = f"{base_prompt}\n\n[Previous result had validation errors: {'; '.join(validation_errors)}. Correct these errors and return valid JSON.]"

        # If we reach here, failed
        if receipt_path:
            receipt = ExecutionReceipt(receipt_path, task_id="map_invocation", config={"provider": self.provider})
            receipt.fail(
                error=last_error or "Unknown failure",
                exit_code=1,
                input_hash=input_hash,
                attempts=attempts,
                provider=self.provider,
                transport="subscription_cli"
            )
        raise SemanticExecutionError(f"Map semantic extraction failed after {attempts} attempts: {last_error}")

    def execute_reduce(
        self,
        packet: dict[str, Any],
        lookup: dict[str, dict[str, Any]],
        receipt_path: Path | None = None,
        max_retries: int = 1
    ) -> dict[str, Any]:
        """Execute Reduce synthesis with up to 1 validation-informed retry."""
        packet_json = json.dumps(packet, indent=2, ensure_ascii=False)
        prompt_tmpl = (REPO_ROOT / "scripts" / "transcript_pipeline_v2" / "prompts" / "reduce.md").read_text(encoding="utf-8")
        base_prompt = prompt_tmpl.replace("{PACKET_JSON}", packet_json)

        attempts = 0
        prompt = base_prompt
        last_error = None
        input_hash = packet.get("packet_sha256") or hashlib.sha256(packet_json.encode("utf-8")).hexdigest()

        while attempts <= max_retries:
            attempts += 1
            code, stdout, stderr, wall_time = self.invoke_raw(prompt)
            
            if code != 0:
                last_error = f"CLI process exited with non-zero code {code}: {stderr}"
                if attempts > max_retries:
                    break
                prompt = f"{base_prompt}\n\n[Previous attempt failed with CLI error: {stderr[:300]}. Please return ONLY valid JSON.]"
                continue

            try:
                result = extract_json_block(stdout)
            except Exception as exc:
                last_error = f"Failed to parse JSON output: {exc}"
                if attempts > max_retries:
                    break
                prompt = f"{base_prompt}\n\n[Previous output was not valid JSON ({exc}). Return ONLY the raw JSON object adhering to ttk.reduce-result.v2.]"
                continue

            # Validate against TTK Reduce rules
            validation_errors = ttk_verify.validate_reduce_result(packet, result, lookup)
            if not validation_errors:
                # Valid!
                output_hash = hashlib.sha256(json.dumps(result, sort_keys=True).encode("utf-8")).hexdigest()
                if receipt_path:
                    receipt = ExecutionReceipt(receipt_path, task_id="reduce_invocation", config={"provider": self.provider})
                    receipt.complete(
                        exit_code=0,
                        input_hash=input_hash,
                        output_hash=output_hash,
                        status="PASS",
                        attempts=attempts,
                        wall_time_seconds=round(wall_time, 4),
                        provider=self.provider,
                        transport="subscription_cli"
                    )
                return result

            last_error = f"TTK Validation errors: {'; '.join(validation_errors)}"
            if attempts > max_retries:
                break
            prompt = f"{base_prompt}\n\n[Previous result had validation errors: {'; '.join(validation_errors)}. Correct these errors and return valid JSON.]"

        if receipt_path:
            receipt = ExecutionReceipt(receipt_path, task_id="reduce_invocation", config={"provider": self.provider})
            receipt.fail(
                error=last_error or "Unknown failure",
                exit_code=1,
                input_hash=input_hash,
                attempts=attempts,
                provider=self.provider,
                transport="subscription_cli"
            )
        raise SemanticExecutionError(f"Reduce semantic synthesis failed after {attempts} attempts: {last_error}")
