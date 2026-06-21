# ============================================================
# war_monitor_engine.py
# NEXO / ZYRA
# Global Conflict Monitoring Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class WarMonitorEngine:

    def __init__(self):

        self._history = []

    def evaluate(
        self,
        country_data: dict,
    ) -> dict:

        active_conflict = country_data.get(
            "active_conflict",
            False,
        )

        military_risk = country_data.get(
            "military_risk",
            0,
        )

        score = military_risk

        if active_conflict:

            score = max(
                score,
                90,
            )

        if score >= 85:
            level = "CRITICAL"

        elif score >= 70:
            level = "HIGH"

        elif score >= 40:
            level = "MEDIUM"

        else:
            level = "LOW"

        result = {

            "war_risk_id":
                f"WAR-{uuid4()}",

            "country":
                country_data.get(
                    "country"
                ),

            "active_conflict":
                active_conflict,

            "score":
                score,

            "risk_level":
                level,

            "generated_at":
                datetime.utcnow().isoformat(),

            "status":
                "MONITORED",
        }

        self._history.append(
            result
        )

        return result


war_monitor_engine = (
    WarMonitorEngine()
)
