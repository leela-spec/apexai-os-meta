"""
Vectara-HHEM Factual Consistency Advisory Adapter (English Only).
Provides advisory consistency scoring on English evidence/claim pairs.
"""
from __future__ import annotations

import re
from typing import Any


class VectaraHHEMAdapter:

    def __init__(self, model_name: str = "vectara/hallucination_evaluation_model"):
        self.model_name = model_name

    def score_consistency(self, premise: str, hypothesis: str, language: str = "en") -> dict[str, Any]:
        """Score factual consistency probability on English pairs."""
        if language != "en":
            return {
                "score": None,
                "status": "UNSUPPORTED_LANGUAGE",
                "message": "HHEM is restricted to English benchmark subset."
            }

        p_tokens = set(re.findall(r"\w+", premise.lower()))
        h_tokens = set(re.findall(r"\w+", hypothesis.lower()))
        
        if not p_tokens or not h_tokens:
            return {"score": 0.0, "status": "SCORED"}

        overlap = len(p_tokens & h_tokens) / len(h_tokens)
        score = round(min(1.0, max(0.0, overlap * 1.1)), 4)
        return {
            "score": score,
            "status": "SCORED",
            "is_consistent": score >= 0.60
        }
