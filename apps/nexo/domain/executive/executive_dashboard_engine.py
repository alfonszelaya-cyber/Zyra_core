# ============================================================
# executive_dashboard_engine.py
# NEXO / ZYRA
# Executive Dashboard Domain Engine
# ============================================================

from datetime import datetime
from typing import Dict, List


class ExecutiveDashboardEngine:

    """
    Dashboard Ejecutivo Central.

    Responsabilidades:

    - Consolidar KPIs
    - Consolidar métricas
    - Consolidar alertas
    - Consolidar decisiones
    - Preparar panel ejecutivo
    - Entregar resumen para ROOT
    - Servir información a ZYRA
    """

    def __init__(self):

        self._snapshots = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    # ========================================================
    # DASHBOARD
    # ========================================================

    def build_dashboard(
        self,
        kpis: Dict,
        metrics: Dict,
        alerts: List,
        decisions: List,
    ) -> Dict:

        dashboard = {

            "generated_at":
                self._now(),

            "kpis":
                kpis,

            "metrics":
                metrics,

            "alerts":
                alerts,

            "decisions":
                decisions,

            "critical_alerts":
                len(
                    [
                        a
                        for a in alerts
                        if a.get("level")
                        == "CRITICAL"
                    ]
                ),

            "open_alerts":
                len(
                    [
                        a
                        for a in alerts
                        if a.get("status")
                        == "OPEN"
                    ]
                ),

            "total_decisions":
                len(
                    decisions
                ),

            "status":
                "ACTIVE",
        }

        self._snapshots.append(
            dashboard
        )

        return dashboard

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_snapshots(
        self,
    ) -> List[Dict]:

        return list(
            self._snapshots
        )

    def get_last_snapshot(
        self,
    ) -> Dict | None:

        if not self._snapshots:
            return None

        return self._snapshots[-1]

    # ========================================================
    # RESUMEN EJECUTIVO
    # ========================================================

    def generate_executive_summary(
        self,
    ) -> Dict:

        dashboard = (
            self.get_last_snapshot()
        )

        if not dashboard:

            return {

                "status":
                    "NO_DATA",

                "generated_at":
                    self._now(),
            }

        return {

            "generated_at":
                self._now(),

            "critical_alerts":
                dashboard[
                    "critical_alerts"
                ],

            "open_alerts":
                dashboard[
                    "open_alerts"
                ],

            "total_decisions":
                dashboard[
                    "total_decisions"
                ],

            "status":
                dashboard[
                    "status"
                ],
        }

    # ========================================================
    # REPORTE
    # ========================================================

    def generate_report(
        self,
    ) -> Dict:

        return {

            "report_type":
                "EXECUTIVE_DASHBOARD",

            "snapshots":
                self.get_snapshots(),

            "generated_at":
                self._now(),
        }


# ============================================================
# FIN
# executive_dashboard_engine.py
# ============================================================
