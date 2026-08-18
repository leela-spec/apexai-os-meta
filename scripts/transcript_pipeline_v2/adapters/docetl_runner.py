"""
DocETL Orchestration Adapter for Transcript Pipeline V2.
Evaluates DocETL declarative pipeline integration under Trial 1 subscription CLI constraints.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class DocETLAdapter:

    def __init__(self, config_path: Path | None = None):
        self.config_path = config_path
        self.optimizer_enabled = False
        self.trial1_transport = "subscription_cli_only"

    def run_pipeline(self, evidence_ledger: dict[str, Any]) -> dict[str, Any]:
        """
        DocETL execution requires litellm / direct model API transport.
        Under Trial 1 lock (06-TRIAL1-TRANSPORT-LOCK.yaml), direct API billing is forbidden.
        """
        return {
            "status": "BLOCKED_FOR_TRIAL1",
            "reason": "DocETL requires LiteLLM API key transport. Subscription CLI integration is not supported without forking DocETL core.",
            "optimizer": False
        }
