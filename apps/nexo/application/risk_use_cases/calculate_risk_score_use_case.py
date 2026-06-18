from apps.nexo.domain.risk.risk_scoring_engine import (
    RiskScoringEngine,
)


class CalculateRiskScoreUseCase:

    def __init__(
        self,
        risk_scoring_engine: RiskScoringEngine,
    ):
        self._risk_scoring_engine = (
            risk_scoring_engine
        )

    def execute(
        self,
        entity_data: dict,
    ) -> dict:

        score = (
            self._risk_scoring_engine.calculate_score(
                entity_data=entity_data,
            )
        )

        return {
            "risk_score": score,
            "status": "CALCULATED",
        }
