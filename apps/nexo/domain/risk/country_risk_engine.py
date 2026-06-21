# ============================================================
# country_risk_engine.py
# NEXO / ZYRA
# Country Risk Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class CountryRiskEngine:

    def __init__(self):

        self._history = []

    def evaluate(
        self,
        country_code: str,
        geopolitical_data: dict,
        sanctions_data: dict,
    ) -> dict:

        score = 0

        score += geopolitical_data.get(
            "risk_score",
            0,
        )

        score += sanctions_data.get(
            "risk_score",
            0,
        )

        score = min(
            score,
            100,
        )

        if score >= 80:
            level = "CRITICAL"

        elif score >= 60:
            level = "HIGH"

        elif score >= 30:
            level = "MEDIUM"

        else:
            level = "LOW"

        result = {

            "risk_id":
                f"CTR-{uuid4()}",

            "country":
                country_code,

            "score":
                score,

            "level":
                level,

            "generated_at":
                datetime.utcnow().isoformat(),

            "status":
                "ACTIVE",
        }

        self._history.append(
            result
        )

        return result


country_risk_engine = (
    CountryRiskEngine()
)
