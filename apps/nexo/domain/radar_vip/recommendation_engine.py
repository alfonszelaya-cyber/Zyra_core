# ============================================================
# recommendation_engine.py
# NEXO / ZYRA
# Radar VIP Recommendation Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class RecommendationEngine:

    def __init__(self):

        self._history: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def generate(
        self,
        profitability_result: Dict,
        risk_result: Dict,
        opportunity_result: Dict,
    ) -> Dict:

        margin = float(
            profitability_result.get(
                "margin",
                0,
            )
        )

        risk_level = (
            risk_result.get(
                "risk_level",
                "HIGH",
            )
        )

        priority = (
            opportunity_result.get(
                "priority",
                "LOW",
            )
        )

        recommendation = "REJECT"

        if (
            margin >= 20
            and risk_level == "LOW"
        ):
            recommendation = "BUY"

        elif (
            margin >= 10
            and risk_level != "HIGH"
        ):
            recommendation = "REVIEW"

        result = {

            "recommendation_id":
                f"REC-{uuid4()}",

            "recommendation":
                recommendation,

            "margin":
                margin,

            "risk_level":
                risk_level,

            "priority":
                priority,

            "generated_at":
                self._now(),

            "status":
                "READY",
        }

        self._history.append(
            result
        )

        return result


recommendation_engine = (
    RecommendationEngine()
)
