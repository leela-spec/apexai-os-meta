"""
LangExtract Grounded Map Adapter.
Uses LangExtract provider plugin architecture to produce grounded extractions mapped
directly back into TTK Map Result format.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts" / "transcript_pipeline_v2"))
sys.path.insert(0, str(REPO_ROOT / "scripts" / "transcript_pipeline_v2" / "tools" / "map_langextract" / "provider_cli"))
sys.path.insert(0, str(REPO_ROOT / ".claude" / "skills" / "transcript-to-knowledge" / "scripts"))

from langextract_cli_provider.provider import SubscriptionCLIProvider
import ttk_base


class LangExtractMapAdapter:

    def __init__(self, provider_id: str = "claude"):
        self.provider = SubscriptionCLIProvider(cli_command=provider_id)

    def extract_map_result(self, packet: dict[str, Any], lookup: dict[str, dict[str, Any]]) -> dict[str, Any]:
        """Run grounded extraction and map to TTK Map Result schema."""
        core_segments = [s for s in packet.get("source_segments", []) if s.get("role") == "core"]
        if not core_segments:
            core_segments = packet.get("source_segments", [])

        candidate_claims = []
        key_points = []
        entities = []

        for seg in core_segments:
            sid = seg["id"]
            text = seg.get("text", "")
            extractions = self.provider.extract_grounded(text, {}, sid)
            
            for ext in extractions:
                candidate_claims.append({
                    "claim_text": ext.text,
                    "claim_kind": "fact",
                    "speaker": seg.get("speaker"),
                    "checkworthiness": "high",
                    "source_segment_ids": [sid],
                    "quote_evidence": [{"segment_id": sid, "quote": ext.quote}]
                })
                key_points.append({
                    "text": ext.text,
                    "source_segment_ids": [sid]
                })

        return {
            "schema": ttk_base.MAP_RESULT_SCHEMA,
            "packet_id": packet.get("packet_id"),
            "packet_sha256": packet.get("packet_sha256"),
            "window_id": packet.get("window_id"),
            "subtopics": [{"label": f"Grounded Module ({packet.get('window_id')})", "source_segment_ids": [s["id"] for s in core_segments]}],
            "key_points": key_points[:5],
            "mechanisms": [],
            "protocols": [],
            "arguments": [],
            "candidate_claims": candidate_claims[:4],
            "entities": entities,
            "concepts": [],
            "open_questions": [],
            "contradictions_or_uncertainty": []
        }
