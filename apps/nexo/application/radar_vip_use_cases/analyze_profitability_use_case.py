from apps.nexo.domain.radar_vip.profitability_engine import (
    ProfitabilityEngine,
)


class AnalyzeProfitabilityUseCase:

    def __init__(
        self,
        profitability_engine: ProfitabilityEngine,
    ):
        self._profitability_engine = (
            profitability_engine
        )

    def execute(
        self,
        investment_data: dict,
    ) -> dict:

        profitability = (
            self._profitability_engine.calculate(
                investment_data=investment_data,
            )
        )

        return {
            "profitability": profitability,
            "status": "CALCULATED",
        }
