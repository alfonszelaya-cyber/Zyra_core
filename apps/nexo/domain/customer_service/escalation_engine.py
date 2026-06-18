from datetime import datetime


class EscalationEngine:

    def escalate(
        self,
        ticket_id: str,
        level: int,
        reason: str,
    ) -> dict:

        return {
            "ticket_id": ticket_id,
            "level": level,
            "reason": reason,
            "escalated_at": datetime.utcnow(),
            "status": "ESCALATED",
        }
