# ============================================================
# risk_reward_engine.py
# NEXO / ZYRA
# Radar VIP Risk Reward Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class RiskRewardEngine:

    def __init__(self):

        self._evaluations: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def evaluate(
        self,
        estimated_profit: float,
        capital_required: float,
    ) -> Dict:

        ratio = 0.0

        if capital_required > 0:

            ratio = round(

                estimated_profit
                / capital_required,

                4,
            )

        risk_level = "HIGH"

        if ratio >= 0.50:
            risk_level = "LOW"

        elif ratio >= 0.25:
            risk_level = "MEDIUM"

        result = {

            "evaluation_id":
                f"RR-{uuid4()}",

            "estimated_profit":
                estimated_profit,

            "capital_required":
                capital_required,

            "risk_reward_ratio":
                ratio,

            "risk_level":
                risk_level,

            "generated_at":
                self._now(),
        }

        self._evaluations.append(
            result
        )

        return result

    def get_history(
        self,
    ):

        return list(
            self._evaluations
        )


risk_reward_engine = (
    RiskRewardEngine()
)
