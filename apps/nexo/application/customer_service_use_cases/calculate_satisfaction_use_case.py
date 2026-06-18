from apps.nexo.domain.customer_service.feedback_registry import (
    FeedbackRegistry,
)


class CalculateSatisfactionUseCase:

    def __init__(
        self,
        feedback_registry: FeedbackRegistry,
    ):
        self._feedback_registry = feedback_registry

    def execute(
        self,
        company_id: str,
    ) -> dict:

        feedbacks = self._feedback_registry.get_company_feedback(
            company_id
        )

        if not feedbacks:
            return {
                "company_id": company_id,
                "score": 0,
                "responses": 0,
            }

        total = sum(item.score for item in feedbacks)

        score = round(total / len(feedbacks), 2)

        return {
            "company_id": company_id,
            "score": score,
            "responses": len(feedbacks),
        }
