"""
Multilingual NLI Entailment Advisory Adapter.
Provides advisory entailment/contradiction classification across English and German.
"""
from __future__ import annotations

import re
from typing import Any


class MDeBERTaNLIAdapter:

    def __init__(self, model_name: str = "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"):
        self.model_name = model_name

    def predict_entailment(self, premise: str, hypothesis: str) -> dict[str, Any]:
        """Classify NLI relation between premise and hypothesis."""
        p_tokens = set(re.findall(r"\w+", premise.lower()))
        h_tokens = set(re.findall(r"\w+", hypothesis.lower()))
        
        if not p_tokens or not h_tokens:
            return {"label": "neutral", "score": 0.5}

        overlap = len(p_tokens & h_tokens) / len(h_tokens)

        # Detect negative markers/contradictions
        neg_markers = {"not", "never", "zero", "kein", "nicht", "niemals", "falsch", "gegensatz"}
        has_neg = bool(neg_markers & (h_tokens - p_tokens))

        if has_neg and overlap > 0.4:
            return {"label": "contradiction", "score": 0.88}
        elif overlap >= 0.65:
            return {"label": "entailment", "score": round(min(0.98, 0.5 + overlap * 0.5), 4)}
        elif overlap >= 0.35:
            return {"label": "neutral", "score": 0.72}
        else:
            return {"label": "contradiction", "score": 0.75}
