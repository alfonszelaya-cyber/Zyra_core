from apps.nexo.domain.risk.risk_reporting_engine import (
    RiskReportingEngine,
)


class GenerateRiskReportUseCase:

    def __init__(
        self,
        risk_reporting_engine: RiskReportingEngine,
    ):
        self._risk_reporting_engine = (
            risk_reporting_engine
        )

    def execute(
        self,
        period: str,
        filters: dict | None = None,
    ) -> dict:

        report = (
            self._risk_reporting_engine.generate_report(
                period=period,
                filters=filters or {},
            )
        )

        return {
            "period": period,
            "report": report,
            "status": "GENERATED",
        }
