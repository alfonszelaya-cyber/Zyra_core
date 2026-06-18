from apps.nexo.domain.radar_vip.risk_reward_engine import (
    RiskRewardEngine,
)


class CalculateRiskRewardUseCase:

    def __init__(
        self,
        risk_reward_engine: RiskRewardEngine,
    ):
        self._risk_reward_engine = (
            risk_reward_engine
        )

    def execute(
        self,
        operation_data: dict,
    ) -> dict:

        calculation = (
            self._risk_reward_engine.calculate(
                operation_data=operation_data,
            )
        )

        return {
            "risk_reward": calculation,
            "status": "CALCULATED",
        }
