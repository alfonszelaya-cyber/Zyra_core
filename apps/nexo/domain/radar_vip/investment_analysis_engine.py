# ============================================================
# investment_analysis_engine.py
# NEXO / ZYRA
# Radar VIP - Investment Analysis Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class InvestmentAnalysisEngine:

    def __init__(self):

        self._analysis_history: List[dict] = []

    def _now(self) -> str:

        return datetime.utcnow().isoformat()

    def analyze_asset(
        self,
        asset_id: str,
        finance_data: Dict,
        logistics_data: Dict,
        operations_data: Dict,
        market_data: Dict,
    ) -> Dict:

        acquisition_cost = float(
            finance_data.get(
                "acquisition_cost",
                0.0,
            )
        )

        taxes_cost = float(
            finance_data.get(
                "taxes_cost",
                0.0,
            )
        )

        logistics_cost = float(
            logistics_data.get(
                "total_logistics_cost",
                0.0,
            )
        )

        operational_cost = float(
            operations_data.get(
                "operational_cost",
                0.0,
            )
        )

        projected_sale = float(
            market_data.get(
                "projected_sale",
                0.0,
            )
        )

        total_cost = (
            acquisition_cost
            + taxes_cost
            + logistics_cost
            + operational_cost
        )

        projected_profit = (
            projected_sale
            - total_cost
        )

        roi = 0.0

        if total_cost > 0:

            roi = round(
                (
                    projected_profit
                    / total_cost
                ) * 100,
                2,
            )

        analysis = {

            "analysis_id":
                f"INV-{uuid4()}",

            "asset_id":
                asset_id,

            "acquisition_cost":
                acquisition_cost,

            "taxes_cost":
                taxes_cost,

            "logistics_cost":
                logistics_cost,

            "operational_cost":
                operational_cost,

            "total_cost":
                round(
                    total_cost,
                    2,
                ),

            "projected_sale":
                projected_sale,

            "projected_profit":
                round(
                    projected_profit,
                    2,
                ),

            "roi":
                roi,

            "created_at":
                self._now(),

            "status":
                "COMPLETED",
        }

        self._analysis_history.append(
            analysis
        )

        return analysis

    def get_history(
        self,
    ) -> List[dict]:

        return list(
            self._analysis_history
        )


investment_analysis_engine = (
    InvestmentAnalysisEngine()
)
