# ============================================================
# logistics_metrics_engine.py
# NEXO / ZYRA
# Logistics Metrics Engine
# ============================================================

from datetime import datetime
from typing import Dict, List


class LogisticsMetricsEngine:

    def _now(self):

        return datetime.utcnow().isoformat()

    def calculate_metrics(
        self,
        shipments: List[dict],
    ) -> Dict:

        total_shipments = len(
            shipments
        )

        delivered = len(

            [
                s
                for s in shipments
                if s.get("status")
                == "DELIVERED"
            ]
        )

        pending = (
            total_shipments
            - delivered
        )

        delivery_rate = 0.0

        if total_shipments:

            delivery_rate = round(

                (
                    delivered
                    / total_shipments
                ) * 100,

                2,
            )

        return {

            "generated_at":
                self._now(),

            "total_shipments":
                total_shipments,

            "delivered":
                delivered,

            "pending":
                pending,

            "delivery_rate":
                delivery_rate,

            "status":
                "CALCULATED",
        }


logistics_metrics_engine = (
    LogisticsMetricsEngine()
)
