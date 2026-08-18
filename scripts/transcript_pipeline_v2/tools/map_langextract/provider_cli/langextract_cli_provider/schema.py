"""Extraction schemas for LangExtract provider."""
from dataclasses import dataclass, field
from typing import Any


@dataclass
class GroundedExtraction:
    text: str
    label: str
    start_char: int
    end_char: int
    source_segment_id: str
    quote: str
    attributes: dict[str, Any] = field(default_factory=dict)
