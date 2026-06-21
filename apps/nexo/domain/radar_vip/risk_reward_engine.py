# ============================================================
# risk_reward_engine.py
# NEXO / ZYRA
# Radar VIP Risk Reward Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class RiskRewardEngine:

    def __init__(self):

        self._history: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def evaluate(
        self,
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

        risk_level = "HIGH"

        if (
            roi >= 30
            and market_score >= 70
        ):
            risk_level = "LOW"

        elif (
            roi >= 15
            and market_score >= 50
        ):
            risk_level = "MEDIUM"

        result = {

            "risk_id":
                f"RISK-{uuid4()}",

            "roi":
                roi,

            "market_score":
                market_score,

            "risk_level":
                risk_level,

            "generated_at":
                self._now(),

            "status":
                "EVALUATED",
        }

        self._history.append(
            result
        )

        return result


risk_reward_engine = (
    RiskRewardEngine()
)
