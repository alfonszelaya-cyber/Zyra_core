# ============================================================
# executive_kpi_engine.py
# NEXO / ZYRA
# Executive KPI Domain Engine
# ============================================================

from datetime import datetime
from typing import Dict, List


class ExecutiveKPIEngine:

    """
    Motor Ejecutivo de KPIs.

    Responsabilidades:

    - Generar KPIs ejecutivos
    - Consolidar métricas estratégicas
    - Calcular tendencias
    - Alimentar Dashboard Ejecutivo
    - Alimentar Reportes Ejecutivos
    - Alimentar ZYRA Analytics
    """

    def __init__(self):

        self._history: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    # ========================================================
    # GENERACIÓN KPI
    # ========================================================

    def generate_kpis(
        self,
        metrics: Dict,
    ) -> Dict:

        kpis = {

            "revenue_growth":
                metrics.get(
                    "revenue_growth",
                    0
                ),

            "profit_margin":
                metrics.get(
                    "profit_margin",
                    0
                ),

            "cash_flow":
                metrics.get(
                    "cash_flow",
                    0
                ),

            "customer_growth":
                metrics.get(
                    "customer_growth",
                    0
                ),

            "generated_at":
                self._now(),
        }

        self._history.append(
            kpis
        )

        return kpis

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_history(
        self,
    ) -> List[Dict]:

        return list(
            self._history
        )

    def get_last_kpis(
        self,
    ) -> Dict | None:

        if not self._history:
            return None

        return self._history[-1]

    # ========================================================
    # SCORE EJECUTIVO
    # ========================================================

    def calculate_executive_score(
        self,
        kpis: Dict,
    ) -> float:

        values = [

            float(
                kpis.get(
                    "revenue_growth",
                    0
                )
            ),

            float(
                kpis.get(
                    "profit_margin",
                    0
                )
            ),

            float(
                kpis.get(
                    "cash_flow",
                    0
                )
            ),

            float(
                kpis.get(
                    "customer_growth",
                    0
                )
            ),
        ]

        if not values:
            return 0.0

        return round(
            sum(values)
            / len(values),
            2,
        )

    # ========================================================
    # RESUMEN
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        last = self.get_last_kpis()

        if not last:

            return {

                "status":
                    "NO_DATA",

                "generated_at":
                    self._now(),
            }

        return {

            "executive_score":
                self.calculate_executive_score(
                    last
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
                "EXECUTIVE_KPI",

            "records":
                len(
                    self._history
                ),

            "history":
                self.get_history(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),
        }


# ============================================================
# FIN
# executive_kpi_engine.py
# ============================================================
