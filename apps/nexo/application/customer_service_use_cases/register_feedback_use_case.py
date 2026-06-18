from datetime import datetime

from apps.nexo.domain.customer_service.feedback_entity import (
    FeedbackEntity,
)
from apps.nexo.domain.customer_service.feedback_registry import (
    FeedbackRegistry,
)


class RegisterFeedbackUseCase:

    def __init__(
        self,
        feedback_registry: FeedbackRegistry,
    ):
        self._feedback_registry = feedback_registry

    def execute(
        self,
        ticket_id: str,
        client_id: str,
        score: int,
        comments: str,
    ) -> dict:

        feedback = FeedbackEntity(
            ticket_id=ticket_id,
            client_id=client_id,
            score=score,
            comments=comments,
            created_at=datetime.utcnow(),
        )

        self._feedback_registry.save(feedback)

        return {
            "ticket_id": ticket_id,
            "client_id": client_id,
            "score": score,
            "status": "REGISTERED",
        }
