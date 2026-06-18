from apps.nexo.domain.meta_government.public_decision_engine import (
    PublicDecisionEngine,
)


class SupportPublicDecisionUseCase:

    def __init__(
        self,
        public_decision_engine: PublicDecisionEngine,
    ):
        self._public_decision_engine = (
            public_decision_engine
        )

    def execute(
        self,
        decision_context: dict,
    ) -> dict:

        recommendation = (
            self._public_decision_engine.evaluate(
                decision_context=decision_context,
            )
        )

        return {
            "decision_context": decision_context,
            "recommendation": recommendation,
            "status": "ANALYZED",
        }
