# ============================================================
# risk_monitor_engine.py
# NEXO / ZYRA
# Continuous Risk Monitor
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class RiskMonitorEngine:

    def __init__(self):

        self._events = []

    def register(
        self,
        risk_result: dict,
    ) -> dict:

        event = {

            "event_id":
                f"RM-{uuid4()}",

            "risk_id":
                risk_result.get(
                    "risk_id"
                ),

            "risk_level":
                risk_result.get(
                    "level"
                ),

            "score":
                risk_result.get(
                    "score"
                ),

            "created_at":
                datetime.utcnow().isoformat(),

            "status":
                "MONITORED",
        }

        self._events.append(
            event
        )

        return event

    def get_active_alerts(
        self,
    ) -> list:

        return [

            event
            for event in self._events
            if event.get(
                "risk_level"
            )
            in [
                "HIGH",
                "CRITICAL",
            ]
        ]


risk_monitor_engine = (
    RiskMonitorEngine()
)
