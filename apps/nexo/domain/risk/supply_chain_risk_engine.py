# ============================================================
# supply_chain_risk_engine.py
# NEXO / ZYRA
# Supply Chain Risk Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class SupplyChainRiskEngine:

    def __init__(self):

        self._history = []

    def evaluate(
        self,
        logistics_data: dict,
        supplier_data: dict,
    ) -> dict:

        score = 0

        delays = logistics_data.get(
            "delays",
            0,
        )

        supplier_failures = supplier_data.get(
            "supplier_failures",
            0,
        )

        score += min(
            delays * 5,
            50,
        )

        score += min(
            supplier_failures * 10,
            50,
        )

        if score >= 80:
            level = "CRITICAL"

        elif score >= 60:
            level = "HIGH"

        elif score >= 30:
            level = "MEDIUM"

        else:
            level = "LOW"

        result = {

            "supply_chain_risk_id":
                f"SCR-{uuid4()}",

            "score":
                score,

            "risk_level":
                level,

            "generated_at":
                datetime.utcnow().isoformat(),

            "status":
                "EVALUATED",
        }

        self._history.append(
            result
        )

        return result


supply_chain_risk_engine = (
    SupplyChainRiskEngine()
)
