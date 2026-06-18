from apps.nexo.domain.risk.financial_risk_engine import (
    FinancialRiskEngine,
)


class MonitorFinancialRiskUseCase:

    def __init__(
        self,
        financial_risk_engine: (
            FinancialRiskEngine
        ),
    ):
        self._financial_risk_engine = (
            financial_risk_engine
        )

    def execute(
        self,
        financial_context: dict,
    ) -> dict:

        monitoring = (
            self._financial_risk_engine.monitor(
                financial_context=financial_context,
            )
        )

        return {
            "monitoring": monitoring,
            "status": "MONITORED",
        }
