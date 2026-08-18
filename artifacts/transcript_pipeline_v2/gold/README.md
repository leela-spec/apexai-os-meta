# V2 Benchmark Fixtures and Gold Labels

This directory contains representative evaluation fixtures for the V2 transcript-to-knowledge reuse bake-off.

## Evidence Hierarchy & Label Authorities
1. **HUMAN_GOLD (Rank 1):** Adjudicated manually against raw source audio/text.
2. **SOURCE_METADATA (Rank 2):** Established by source video/transcript metadata.
3. **AI_SILVER (Rank 3):** Extracted by strong AI from source evidence, reported separately from gold.
4. **AUTOMATIC_JUDGE (Rank 4):** Model/metric-based signals (e.g., DeepEval, NLI).
5. **UNMEASURED (Rank 99):** Explicitly unmeasured where defensible ground truth is not available.

## Files
- `asr-slices.yaml`: Difficult audio slices across all 4 sources with phonetic/domain vocabulary challenges.
- `map-windows.yaml`: Representative Map windows (at least 10 total) covering EN/DE and early/middle/late positions with insight checklists.
- `support-pairs.yaml`: 44 support test pairs across EN/DE with labeled entailment/support states and adversarial/overreaching negative examples.
- `operator-rubric.yaml`: 0..5 scoring rubric across thesis usefulness, Meso coherence, insight recall, source fidelity, uncertainty preservation, and concision.
- `gold-status.yaml`: Status tracking of human gold vs silver vs unmeasured references.
