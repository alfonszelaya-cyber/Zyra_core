# ============================================================
# risk_scoring_engine.py
# NEXO / ZYRA
# Global Risk Scoring Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class RiskScoringEngine:

    def __init__(self):

        self._history = []

    def calculate(
        self,
        compliance_risk: dict,
        financial_risk: dict,
        operational_risk: dict,
        geopolitical_risk: dict,
        fraud_risk: dict,
        supply_chain_risk: dict,
        sanctions_risk: dict,
        war_risk: dict,
    ) -> dict:

        scores = [

            compliance_risk.get("score", 0),
            financial_risk.get("score", 0),
            operational_risk.get("score", 0),
            geopolitical_risk.get("score", 0),
            fraud_risk.get("score", 0),
            supply_chain_risk.get("score", 0),
            sanctions_risk.get("score", 0),
            war_risk.get("score", 0),

        ]

        global_score = round(
            sum(scores) / len(scores),
            2,
        )

        if global_score >= 85:
            level = "CRITICAL"

        elif global_score >= 70:
            level = "HIGH"

        elif global_score >= 40:
            level = "MEDIUM"

        else:
            level = "LOW"

        result = {

            "score_id":
                f"RSK-{uuid4()}",

            "global_score":
                global_score,

            "risk_level":
                level,

            "generated_at":
                datetime.utcnow().isoformat(),

            "status":
                "CALCULATED",
        }

        self._history.append(
            result
        )

        return result


risk_scoring_engine = (
    RiskScoringEngine()
)
