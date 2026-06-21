# ============================================================
# opportunity_detection_engine.py
# NEXO / ZYRA
# Radar VIP - Opportunity Detection Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class OpportunityDetectionEngine:

    def __init__(self):

        self._opportunities: List[
            dict
        ] = []

    def _now(self) -> str:

        return datetime.utcnow().isoformat()

    def detect(
        self,
        asset_id: str,
        investment_analysis: Dict,
        market_context: Dict,
    ) -> Dict:

        roi = float(
            investment_analysis.get(
                "roi",
                0,
            )
        )

        market_score = float(
            market_context.get(
                "market_score",
                0,
            )
        )

        priority = "LOW"

        if (
            roi >= 30
            and market_score >= 70
        ):

            priority = "HIGH"

        elif (
            roi >= 15
            and market_score >= 50
        ):

            priority = "MEDIUM"

        opportunity = {

            "opportunity_id":
                f"OPP-{uuid4()}",

            "asset_id":
                asset_id,

            "roi":
                roi,

            "market_score":
                market_score,

            "expected_profit":
                investment_analysis.get(
                    "projected_profit",
                    0,
                ),

            "priority":
                priority,

            "detected_at":
                self._now(),

            "status":
                "DETECTED",
        }

        self._opportunities.append(
            opportunity
        )

        return opportunity

    def get_history(
        self,
    ) -> List[dict]:

        return list(
            self._opportunities
        )


opportunity_detection_engine = (
    OpportunityDetectionEngine()
)
