# ============================================================
# profitability_engine.py
# NEXO / ZYRA
# Radar VIP Profitability Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class ProfitabilityEngine:

    def __init__(self):

        self._history: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def calculate(
        self,
        investment_analysis: Dict,
        logistics_data: Dict,
        finance_data: Dict,
        operations_data: Dict,
    ) -> Dict:

        acquisition_cost = float(
            investment_analysis.get(
                "acquisition_cost",
                0,
            )
        )

        logistics_cost = float(
            logistics_data.get(
                "total_logistics_cost",
                0,
            )
        )

        taxes_cost = float(
            finance_data.get(
                "taxes_cost",
                0,
            )
        )

        operational_cost = float(
            operations_data.get(
                "operational_cost",
                0,
            )
        )

        sale_price = float(
            investment_analysis.get(
                "projected_sale",
                0,
            )
        )

        total_cost = (
            acquisition_cost
            + logistics_cost
            + taxes_cost
            + operational_cost
        )

        net_profit = (
            sale_price
            - total_cost
        )

        margin = 0.0

        if sale_price > 0:

            margin = round(
                (
                    net_profit
                    / sale_price
                ) * 100,
                2,
            )

        result = {

            "profitability_id":
                f"PROF-{uuid4()}",

            "total_cost":
                round(total_cost, 2),

            "sale_price":
                sale_price,

            "net_profit":
                round(net_profit, 2),

            "margin":
                margin,

            "generated_at":
                self._now(),

            "status":
                "CALCULATED",
        }

        self._history.append(
            result
        )

        return result


profitability_engine = (
    ProfitabilityEngine()
)
