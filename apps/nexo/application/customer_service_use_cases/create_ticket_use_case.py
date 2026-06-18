from uuid import uuid4

from apps.nexo.domain.customer_service.ticket_registry import (
    TicketRegistry,
)
from apps.nexo.domain.customer_service.ticket_entity import (
    TicketEntity,
)


class CreateTicketUseCase:

    def __init__(
        self,
        ticket_registry: TicketRegistry,
    ):
        self._ticket_registry = ticket_registry

    def execute(
        self,
        client_id: str,
        title: str,
        description: str,
        priority: str = "NORMAL",
    ) -> dict:

        ticket = TicketEntity(
            ticket_id=str(uuid4()),
            client_id=client_id,
            title=title,
            description=description,
            priority=priority,
        )

        self._ticket_registry.save(ticket)

        return {
            "ticket_id": ticket.ticket_id,
            "client_id": client_id,
            "status": "OPEN",
        }
