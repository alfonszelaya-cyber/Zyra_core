from datetime import datetime
from uuid import uuid4


class TicketEngine:

    def create_ticket(
        self,
        client_id: str,
        subject: str,
        description: str,
    ) -> dict:

        return {
            "ticket_id": str(uuid4()),
            "client_id": client_id,
            "subject": subject,
            "description": description,
            "created_at": datetime.utcnow(),
            "status": "OPEN",
        }

    def assign_ticket(
        self,
        ticket: dict,
        assigned_to: str,
    ) -> dict:

        ticket["assigned_to"] = assigned_to

        return ticket
