from apps.nexo.domain.risk.operational_risk_engine import (
    OperationalRiskEngine,
)


class MonitorOperationalRiskUseCase:

    def __init__(
        self,
        operational_risk_engine: (
            OperationalRiskEngine
        ),
    ):
        self._operational_risk_engine = (
            operational_risk_engine
        )

    def execute(
        self,
        operational_context: dict,
    ) -> dict:

        monitoring = (
            self._operational_risk_engine.monitor(
                operational_context=operational_context,
            )
        )

        return {
            "monitoring": monitoring,
            "status": "MONITORED",
            "risk_type": "OPERATIONAL",
        }
