from apps.nexo.domain.executive.business_monitor_engine import (
    BusinessMonitorEngine,
)


class MonitorBusinessUseCase:

    def __init__(
        self,
        business_monitor_engine: BusinessMonitorEngine,
    ):
        self._business_monitor_engine = (
            business_monitor_engine
        )

    def execute(
        self,
        company_id: str,
    ) -> dict:

        monitoring = (
            self._business_monitor_engine.monitor(
                company_id
            )
        )

        return {
            "company_id": company_id,
            "status": monitoring.get(
                "status",
                "UNKNOWN",
            ),
            "indicators": monitoring.get(
                "indicators",
                {},
            ),
            "risks": monitoring.get(
                "risks",
                [],
            ),
        }
