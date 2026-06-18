from datetime import datetime


class RegulatoryMonitor:

    def monitor(
        self,
        jurisdiction: str,
    ) -> dict:

        return {
            "jurisdiction": jurisdiction,
            "checked_at": datetime.utcnow(),
            "changes_detected": False,
        }
