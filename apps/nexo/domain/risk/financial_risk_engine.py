# ============================================================
# financial_risk_engine.py
# NEXO / ZYRA
# Financial Risk Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class FinancialRiskEngine:

    def __init__(self):

        self._history = []

    def evaluate(
        self,
        accounting_data: dict,
        finance_data: dict,
    ) -> dict:

        liquidity = finance_data.get(
            "liquidity_ratio",
            0,
        )

        debt_ratio = finance_data.get(
            "debt_ratio",
            0,
        )

        score = 0

        if liquidity < 1:
            score += 40

        if debt_ratio > 70:
            score += 40

        if accounting_data.get(
            "negative_cashflow",
            False,
        ):
            score += 20

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
                f"FIN-{uuid4()}",

            "score":
                score,

            "level":
                level,

            "generated_at":
                datetime.utcnow().isoformat(),

            "status":
                "EVALUATED",
        }

        self._history.append(
            result
        )

        return result


financial_risk_engine = (
    FinancialRiskEngine()
)
