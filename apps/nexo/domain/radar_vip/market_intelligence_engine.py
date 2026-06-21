# ============================================================
# market_intelligence_engine.py
# NEXO / ZYRA
# Radar VIP - Market Intelligence Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class MarketIntelligenceEngine:

    def __init__(self):

        self._signals: List[dict] = []

    def _now(self) -> str:

        return datetime.utcnow().isoformat()

    def build_market_context(
        self,
        finance_metrics: Dict,
        logistics_metrics: Dict,
        operations_metrics: Dict,
    ) -> Dict:

        demand_score = float(
            operations_metrics.get(
                "demand_score",
                50,
            )
        )

        inventory_score = float(
            logistics_metrics.get(
                "inventory_score",
                50,
            )
        )

        margin_score = float(
            finance_metrics.get(
                "margin_score",
                50,
            )
        )

        market_score = round(

            (
                demand_score
                + inventory_score
                + margin_score
            ) / 3,

            2,
        )

        trend = "STABLE"

        if market_score >= 80:
            trend = "STRONG_UP"

        elif market_score >= 60:
            trend = "UP"

        elif market_score <= 30:
            trend = "DOWN"

        context = {

            "context_id":
                f"MKT-{uuid4()}",

            "market_score":
                market_score,

            "trend":
                trend,

            "demand_score":
                demand_score,

            "inventory_score":
                inventory_score,

            "margin_score":
                margin_score,

            "created_at":
                self._now(),

            "status":
                "READY",
        }

        self._signals.append(
            context
        )

        return context

    def get_history(
        self,
    ) -> List[dict]:

        return list(
            self._signals
        )


market_intelligence_engine = (
    MarketIntelligenceEngine()
        )
