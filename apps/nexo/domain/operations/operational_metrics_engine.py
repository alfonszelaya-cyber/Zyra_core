# ============================================================
# operational_metrics_engine.py
# NEXO / ZYRA
# Operational Metrics Engine
# ============================================================

from datetime import datetime
from typing import Dict, List


class OperationalMetricsEngine:

    def _now(self):

        return datetime.utcnow().isoformat()

    def calculate_metrics(
        self,
        operations: List[Dict],
    ) -> Dict:

        total = len(
            operations
        )

        completed = len(

            [
                op
                for op in operations

                if op.get(
                    "status"
                )
                == "COMPLETED"
            ]
        )

        active = (
            total
            - completed
        )

        completion_rate = 0.0

        if total > 0:

            completion_rate = round(

                (
                    completed
                    / total
                ) * 100,

                2,
            )

        return {

            "generated_at":
                self._now(),

            "total_operations":
                total,

            "completed":
                completed,

            "active":
                active,

            "completion_rate":
                completion_rate,

            "status":
                "CALCULATED",
        }


operational_metrics_engine = (
    OperationalMetricsEngine()
)
