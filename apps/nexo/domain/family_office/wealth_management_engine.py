# ============================================================
# wealth_management_engine.py
# NEXO / ZYRA
# Wealth Management Engine
# ============================================================

from datetime import datetime
from typing import Dict


class WealthManagementEngine:

    """
    Gestión global de patrimonio.
    """

    def _now(self):

        return datetime.utcnow().isoformat()

    def generate_wealth_snapshot(
        self,
        total_assets: float,
        total_liabilities: float,
    ) -> Dict:

        net_worth = (
            total_assets
            - total_liabilities
        )

        return {

            "generated_at":
                self._now(),

            "total_assets":
                total_assets,

            "total_liabilities":
                total_liabilities,

            "net_worth":
                net_worth,

            "status":
                "ACTIVE",
        }

    def calculate_growth(
        self,
        current_value: float,
        previous_value: float,
    ) -> float:

        if previous_value <= 0:
            return 0.0

        return round(

            (
                (
                    current_value
                    - previous_value
                )
                / previous_value
            )
            * 100,

            2,
        )
