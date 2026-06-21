# ============================================================
# opportunity_detection_engine.py
# NEXO / ZYRA
# Radar VIP Opportunity Detection Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class OpportunityDetectionEngine:

    def __init__(self):

        self._opportunities: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def register_opportunity(
        self,
        source: str,
        title: str,
        estimated_cost: float,
        estimated_sale: float,
    ) -> Dict:

        estimated_profit = (
            estimated_sale
            - estimated_cost
        )

        opportunity = {

            "opportunity_id":
                f"OPP-{uuid4()}",

            "source":
                source,

            "title":
                title,

            "estimated_cost":
                estimated_cost,

            "estimated_sale":
                estimated_sale,

            "estimated_profit":
                estimated_profit,

            "created_at":
                self._now(),

            "status":
                "DETECTED",
        }

        self._opportunities.append(
            opportunity
        )

        return opportunity

    def get_opportunities(self):

        return list(
            self._opportunities
        )


opportunity_detection_engine = (
    OpportunityDetectionEngine()
)
