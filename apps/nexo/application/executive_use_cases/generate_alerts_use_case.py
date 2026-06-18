from apps.nexo.domain.executive.executive_alert_engine import (
    ExecutiveAlertEngine,
)


class GenerateAlertsUseCase:

    def __init__(
        self,
        alert_engine: ExecutiveAlertEngine,
    ):
        self._alert_engine = alert_engine

    def execute(
        self,
        company_id: str,
    ) -> dict:

        alerts = self._alert_engine.generate_alerts(
            company_id
        )

        return {
            "company_id": company_id,
            "alerts": alerts,
            "total_alerts": len(alerts),
        }
