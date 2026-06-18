from apps.nexo.domain.executive.executive_dashboard_engine import (
    ExecutiveDashboardEngine,
)


class GenerateDashboardUseCase:

    def __init__(
        self,
        dashboard_engine: ExecutiveDashboardEngine,
    ):
        self._dashboard_engine = dashboard_engine

    def execute(
        self,
        company_id: str,
    ) -> dict:

        dashboard = self._dashboard_engine.build_dashboard(
            company_id
        )

        return {
            "company_id": company_id,
            "dashboard": dashboard,
        }
