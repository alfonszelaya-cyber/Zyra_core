from apps.nexo.domain.customer_service.ticket_registry import (
    TicketRegistry,
)


class CloseTicketUseCase:

    def __init__(
        self,
        ticket_registry: TicketRegistry,
    ):
        self._ticket_registry = ticket_registry

    def execute(
        self,
        ticket_id: str,
        resolution_note: str,
    ) -> dict:

        ticket = self._ticket_registry.get(ticket_id)

        ticket.close(resolution_note)

        self._ticket_registry.save(ticket)

        return {
            "ticket_id": ticket_id,
            "status": "CLOSED",
            "resolution": resolution_note,
        }
