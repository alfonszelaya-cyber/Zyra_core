from apps.nexo.domain.customer_service.ticket_registry import (
    TicketRegistry,
)
from apps.nexo.domain.customer_service.feedback_registry import (
    FeedbackRegistry,
)


class GenerateServiceReportUseCase:

    def __init__(
        self,
        ticket_registry: TicketRegistry,
        feedback_registry: FeedbackRegistry,
    ):
        self._ticket_registry = ticket_registry
        self._feedback_registry = feedback_registry

    def execute(
        self,
        company_id: str,
    ) -> dict:

        tickets = self._ticket_registry.get_company_tickets(
            company_id
        )

        feedbacks = self._feedback_registry.get_company_feedback(
            company_id
        )

        total_tickets = len(tickets)

        closed_tickets = len(
            [
                ticket
                for ticket in tickets
                if ticket.status == "CLOSED"
            ]
        )

        satisfaction = 0

        if feedbacks:
            satisfaction = round(
                sum(item.score for item in feedbacks)
                / len(feedbacks),
                2,
            )

        return {
            "company_id": company_id,
            "total_tickets": total_tickets,
            "closed_tickets": closed_tickets,
            "open_tickets": total_tickets - closed_tickets,
            "satisfaction_score": satisfaction,
        }
