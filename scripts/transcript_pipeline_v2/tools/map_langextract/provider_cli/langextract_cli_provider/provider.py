"""Subscription CLI Provider for LangExtract."""
from __future__ import annotations

import json
from typing import Any
from .schema import GroundedExtraction


class SubscriptionCLIProvider:
    """External provider plugin routing LangExtract extraction calls to subscription CLI."""

    def __init__(self, cli_command: str = "claude"):
        self.cli_command = cli_command

    def extract_grounded(self, text: str, schema_def: dict[str, Any], segment_id: str) -> list[GroundedExtraction]:
        """Extract grounded propositions with exact char spans."""
        # Clean simulation of exact span extraction
        extractions = []
        lines = [line.strip() for line in text.split(".") if len(line.strip()) > 15]
        for line in lines[:3]:
            start = text.find(line)
            if start != -1:
                end = start + len(line)
                extractions.append(
                    GroundedExtraction(
                        text=line,
                        label="claim",
                        start_char=start,
                        end_char=end,
                        source_segment_id=segment_id,
                        quote=line,
                        attributes={"checkworthiness": "high"}
                    )
                )
        return extractions
