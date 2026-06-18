from apps.nexo.domain.customer_service.ticket_registry import (
    TicketRegistry,
)


class AssignTicketUseCase:

    def __init__(
        self,
        ticket_registry: TicketRegistry,
    ):
        self._ticket_registry = ticket_registry

    def execute(
        self,
        ticket_id: str,
        agent_id: str,
    ) -> dict:

        ticket = self._ticket_registry.get(ticket_id)

        ticket.assign_agent(agent_id)

        self._ticket_registry.save(ticket)

        return {
            "ticket_id": ticket_id,
            "agent_id": agent_id,
            "status": "ASSIGNED",
        }
