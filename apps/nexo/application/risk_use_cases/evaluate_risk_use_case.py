from apps.nexo.domain.risk.risk_evaluation_engine import (
    RiskEvaluationEngine,
)


class EvaluateRiskUseCase:

    def __init__(
        self,
        risk_evaluation_engine: (
            RiskEvaluationEngine
        ),
    ):
        self._risk_evaluation_engine = (
            risk_evaluation_engine
        )

    def execute(
        self,
        risk_context: dict,
    ) -> dict:

        evaluation = (
            self._risk_evaluation_engine.evaluate(
                risk_context=risk_context,
            )
        )

        return {
            "evaluation": evaluation,
            "status": "COMPLETED",
        }
