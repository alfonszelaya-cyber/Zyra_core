# ============================================================
# public_metrics_engine.py
# NEXO / ZYRA
# Public Metrics Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class PublicMetricsEngine:

    def __init__(self):

        self._metrics_history: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    # ========================================================
    # REGISTRO DE MÉTRICAS
    # ========================================================

    def register_metrics(
        self,
        category: str,
        metrics: Dict,
    ) -> Dict:

        record = {

            "metric_id":
                f"PM-{uuid4()}",

            "category":
                category,

            "metrics":
                metrics,

            "created_at":
                self._now(),

            "status":
                "REGISTERED",
        }

        self._metrics_history.append(
            record
        )

        return record

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_metrics(
        self,
    ):

        return list(
            self._metrics_history
        )

    def get_by_category(
        self,
        category: str,
    ):

        return [

            metric

            for metric
            in self._metrics_history

            if (
                metric["category"]
                == category
            )
        ]

    # ========================================================
    # DASHBOARD NACIONAL
    # ========================================================

    def generate_dashboard_metrics(
        self,
    ) -> Dict:

        categories = {}

        for metric in self._metrics_history:

            category = metric[
                "category"
            ]

            categories[
                category
            ] = (

                categories.get(
                    category,
                    0
                ) + 1
            )

        return {

            "generated_at":
                self._now(),

            "total_metrics":
                len(
                    self._metrics_history
                ),

            "categories":
                categories,

            "status":
                "READY",
        }

    # ========================================================
    # RESUMEN
    # ========================================================

    def get_summary(
        self,
    ) -> Dict:

        return {

            "records":
                len(
                    self._metrics_history
                ),

            "generated_at":
                self._now(),

            "status":
                "ACTIVE",
        }


# ============================================================
# INSTANCIA GLOBAL
# ============================================================

public_metrics_engine = (
    PublicMetricsEngine()
)

# ============================================================
# FIN
# public_metrics_engine.py
# ============================================================
