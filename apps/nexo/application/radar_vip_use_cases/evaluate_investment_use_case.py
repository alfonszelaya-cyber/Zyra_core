from apps.nexo.domain.radar_vip.investment_evaluation_engine import (
    InvestmentEvaluationEngine,
)


class EvaluateInvestmentUseCase:

    def __init__(
        self,
        investment_evaluation_engine: (
            InvestmentEvaluationEngine
        ),
    ):
        self._investment_evaluation_engine = (
            investment_evaluation_engine
        )

    def execute(
        self,
        investment_data: dict,
    ) -> dict:

        evaluation = (
            self._investment_evaluation_engine.evaluate(
                investment_data=investment_data,
            )
        )

        return {
            "investment": investment_data,
            "evaluation": evaluation,
            "status": "EVALUATED",
        }
