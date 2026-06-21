# ============================================================
# national_dashboard_engine.py
# NEXO / ZYRA
# National Dashboard Engine
# ============================================================

from datetime import datetime
from typing import Dict


class NationalDashboardEngine:

    def _now(self):

        return datetime.utcnow().isoformat()

    def build_dashboard(
        self,
        public_metrics: Dict,
        governance_metrics: Dict,
        strategy_metrics: Dict,
    ) -> Dict:

        return {

            "generated_at":
                self._now(),

            "public_metrics":
                public_metrics,

            "governance_metrics":
                governance_metrics,

            "strategy_metrics":
                strategy_metrics,

            "status":
                "READY",
        }

    def executive_snapshot(
        self,
        dashboard: Dict,
    ) -> Dict:

        return {

            "generated_at":
                self._now(),

            "status":
                dashboard.get(
                    "status",
                    "UNKNOWN"
                ),

            "summary":
                dashboard,
        }


national_dashboard_engine = (
    NationalDashboardEngine()
)
