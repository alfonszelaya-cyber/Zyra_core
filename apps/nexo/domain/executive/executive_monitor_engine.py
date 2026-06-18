from datetime import datetime


class ExecutiveMonitorEngine:

    def monitor_business(
        self,
        indicators: dict,
    ) -> dict:

        return {
            "checked_at": datetime.utcnow(),
            "indicators": indicators,
            "status": "MONITORED",
        }
