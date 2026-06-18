from datetime import datetime


class ServiceHistoryEngine:

    def register_event(
        self,
        ticket_id: str,
        event_type: str,
        details: dict,
    ) -> dict:

        return {
            "ticket_id": ticket_id,
            "event_type": event_type,
            "details": details,
            "created_at": datetime.utcnow(),
        }
