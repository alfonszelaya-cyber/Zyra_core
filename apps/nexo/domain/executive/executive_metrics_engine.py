# ============================================================
# executive_metrics_engine.py
# NEXO / ZYRA
# Executive Metrics Domain Engine
# ============================================================

from datetime import datetime
from typing import Dict, List, Optional


class ExecutiveMetricsEngine:

    """
    Motor Ejecutivo de Métricas.

    Responsabilidades:

    - Consolidar métricas operativas
    - Consolidar métricas financieras
    - Consolidar métricas fiscales
    - Consolidar métricas comerciales
    - Alimentar KPIs Ejecutivos
    - Alimentar Dashboard Ejecutivo
    - Alimentar ZYRA Analytics
    """

    def __init__(self):

        self._metrics_history: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    # ========================================================
    # CÁLCULO
    # ========================================================

    def calculate_metrics(
        self,
        source_data: Dict,
    ) -> Dict:

        metrics = {

            "generated_at":
                self._now(),

            "metrics":
                source_data,

            "status":
                "CALCULATED",
        }

        self._metrics_history.append(
            metrics
        )

        return metrics

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_metrics_history(
        self,
    ) -> List[Dict]:

        return list(
            self._metrics_history
        )

    def get_last_metrics(
        self,
    ) -> Optional[Dict]:

        if not self._metrics_history:
            return None

        return self._metrics_history[-1]

    # ========================================================
    # RESUMEN
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        latest = self.get_last_metrics()

        if not latest:

            return {

                "status":
                    "NO_DATA",

                "generated_at":
                    self._now(),
            }

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

    # ========================================================
    # REPORTE
    # ========================================================

    def generate_report(
        self,
    ) -> Dict:

        return {

            "report_type":
                "EXECUTIVE_METRICS",

            "history":
                self.get_metrics_history(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),
        }


# ============================================================
# FIN
# executive_metrics_engine.py
# ============================================================
