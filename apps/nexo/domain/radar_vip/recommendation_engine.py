# ============================================================
# recommendation_engine.py
# NEXO / ZYRA
# Radar VIP Recommendation Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict


class RecommendationEngine:

    def _now(self):

        return datetime.utcnow().isoformat()

    def generate_recommendation(
        self,
        profitability: float,
        risk_score: float,
    ) -> Dict:

        recommendation = "HOLD"

        if (
            profitability >= 20
            and risk_score <= 30
        ):
            recommendation = "BUY"

        elif (
            profitability < 10
            or risk_score >= 70
        ):
            recommendation = "REJECT"

        return {

            "recommendation_id":
                f"REC-{uuid4()}",

            "profitability":
                profitability,

            "risk_score":
                risk_score,

            "recommendation":
                recommendation,

            "generated_at":
                self._now(),

            "status":
                "READY",
        }


recommendation_engine = (
    RecommendationEngine()
)
