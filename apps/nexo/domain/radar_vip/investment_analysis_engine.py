# ============================================================
# investment_analysis_engine.py
# NEXO / ZYRA
# Radar VIP Investment Analysis Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class InvestmentAnalysisEngine:

    def __init__(self):

        self._analyses: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def analyze(
        self,
        asset_id: str,
        acquisition_cost: float,
        projected_sale: float,
    ) -> Dict:

        profit = (
            projected_sale
            - acquisition_cost
        )

        roi = 0.0

        if acquisition_cost > 0:

            roi = round(

                (
                    profit
                    / acquisition_cost
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

            "projected_sale":
                projected_sale,

            "profit":
                round(profit, 2),

            "roi":
                roi,

            "created_at":
                self._now(),
        }

        self._analyses.append(
            analysis
        )

        return analysis

    def get_analyses(self):

        return list(
            self._analyses
        )


investment_analysis_engine = (
    InvestmentAnalysisEngine()
)
