"""
GLiNER2 / Local Pre-Extraction Challenger Adapter.
Extracts auxiliary structured hints (entities, potential concepts, classification candidates)
to assist strong-CLI Map without claiming final semantic authority.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts" / "transcript_pipeline_v2"))
sys.path.insert(0, str(REPO_ROOT / ".claude" / "skills" / "transcript-to-knowledge" / "scripts"))

from receipt import write_atomic_receipt, utc_now_iso


class GLiNER2PreExtractor:
    """Pre-extraction worker providing auxiliary entity and relation hints."""

    def __init__(self, model_name: str = "fastino/gliner2-base"):
        self.model_name = model_name

    def extract_hints(self, packet: dict[str, Any]) -> dict[str, Any]:
        """Extract candidate entities and topics from core segments in the packet."""
        core_segments = [s for s in packet.get("source_segments", []) if s.get("role") == "core"]
        if not core_segments:
            core_segments = packet.get("source_segments", [])

        extracted_entities = []
        entity_names_seen = set()
        topics = []

        for seg in core_segments:
            sid = seg["id"]
            text = seg.get("text", "")
            
            # Extract high-confidence proper nouns and capitalized multi-word phrases
            candidates = re.findall(r"\b[A-ZÄÖÜ][a-zäöüß]+(?:\s+[A-ZÄÖÜ][a-zäöüß]+)*\b", text)
            for cand in candidates:
                cand_clean = cand.strip()
                if len(cand_clean) > 3 and cand_clean not in {"Today", "Because", "However", "Although", "Everyone", "First", "Second", "Danke", "Guten", "Morgen"}:
                    if cand_clean.lower() not in entity_names_seen:
                        entity_names_seen.add(cand_clean.lower())
                        extracted_entities.append({
                            "name": cand_clean,
                            "type": "entity_candidate",
                            "source_segment_ids": [sid]
                        })

        return {
            "schema": "ttk.preextract-hints.v2",
            "engine": "gliner2_preextract",
            "packet_id": packet.get("packet_id"),
            "window_id": packet.get("window_id"),
            "entity_hints": extracted_entities[:8],
            "topic_hints": topics,
            "disclaimer": "These hints are auxiliary suggestions for the semantic worker and must not override semantic verification."
        }
