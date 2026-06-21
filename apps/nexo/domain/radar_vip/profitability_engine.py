# ============================================================
# profitability_engine.py
# NEXO / ZYRA
# Radar VIP Profitability Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class ProfitabilityEngine:

    def __init__(self):

        self._calculations: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def calculate(
        self,
        acquisition_cost: float,
        logistics_cost: float,
        taxes_cost: float,
        sale_price: float,
    ) -> Dict:

        total_cost = (

            acquisition_cost
            + logistics_cost
            + taxes_cost
        )

        profit = (
            sale_price
            - total_cost
        )

        margin = 0.0

        if sale_price > 0:

            margin = round(

                (
                    profit
                    / sale_price
                ) * 100,

                2,
            )

        result = {

            "calculation_id":
                f"PROF-{uuid4()}",

            "total_cost":
                round(
                    total_cost,
                    2,
                ),

            "sale_price":
                sale_price,

            "profit":
                round(
                    profit,
                    2,
                ),

            "margin":
                margin,

            "generated_at":
                self._now(),
        }

        self._calculations.append(
            result
        )

        return result

    def get_history(
        self,
    ):

        return list(
            self._calculations
        )


profitability_engine = (
    ProfitabilityEngine()
)
