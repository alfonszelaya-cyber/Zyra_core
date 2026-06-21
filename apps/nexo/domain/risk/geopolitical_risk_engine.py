# ============================================================
# geopolitical_risk_engine.py
# NEXO / ZYRA
# Geopolitical Risk Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class GeopoliticalRiskEngine:

    def __init__(self):

        self._history = []

    def evaluate(
        self,
        country_code: str,
        geopolitical_events: dict,
    ) -> dict:

        score = int(
            geopolitical_events.get(
                "risk_score",
                0,
            )
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
                f"GEO-{uuid4()}",

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


geopolitical_risk_engine = (
    GeopoliticalRiskEngine()
)
