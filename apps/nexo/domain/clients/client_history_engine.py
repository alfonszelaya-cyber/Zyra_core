from datetime import datetime


class ClientHistoryEngine:

    def register_event(
        self,
        client_id: str,
        event_type: str,
        details: dict,
    ) -> dict:

        return {
            "client_id": client_id,
            "event_type": event_type,
            "details": details,
            "created_at": datetime.utcnow(),
        }
