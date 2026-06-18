from datetime import datetime


class SanctionsMonitor:

    def verify(
        self,
        entity_name: str,
    ) -> dict:

        return {
            "entity_name": entity_name,
            "checked_at": datetime.utcnow(),
            "sanctioned": False,
        }
