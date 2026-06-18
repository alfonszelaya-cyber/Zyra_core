from datetime import datetime

from apps.nexo.domain.customer_service.ticket_registry import (
    TicketRegistry,
)


class EscalateTicketUseCase:

    def __init__(
        self,
        ticket_registry: TicketRegistry,
    ):
        self._ticket_registry = ticket_registry

    def execute(
        self,
        ticket_id: str,
        escalation_level: str,
        reason: str,
    ) -> dict:

        ticket = self._ticket_registry.get(ticket_id)

        ticket.escalate(
            level=escalation_level,
            reason=reason,
            escalated_at=datetime.utcnow(),
        )

        self._ticket_registry.save(ticket)

        return {
            "ticket_id": ticket_id,
            "escalation_level": escalation_level,
            "status": "ESCALATED",
        }
