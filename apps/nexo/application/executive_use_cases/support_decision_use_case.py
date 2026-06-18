from apps.nexo.domain.executive.executive_decision_engine import (
    ExecutiveDecisionEngine,
)


class SupportDecisionUseCase:

    def __init__(
        self,
        decision_engine: ExecutiveDecisionEngine,
    ):
        self._decision_engine = decision_engine

    def execute(
        self,
        company_id: str,
        decision_context: dict,
    ) -> dict:

        recommendation = (
            self._decision_engine.generate_recommendation(
                company_id=company_id,
                context=decision_context,
            )
        )

        return {
            "company_id": company_id,
            "recommendation": recommendation,
            "context": decision_context,
        }
