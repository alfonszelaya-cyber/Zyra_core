from apps.nexo.domain.meta_government.national_dashboard_engine import (
    NationalDashboardEngine,
)


class GenerateNationalDashboardUseCase:

    def __init__(
        self,
        national_dashboard_engine: NationalDashboardEngine,
    ):
        self._national_dashboard_engine = (
            national_dashboard_engine
        )

    def execute(
        self,
        period: str,
    ) -> dict:

        dashboard = (
            self._national_dashboard_engine.generate(
                period=period,
            )
        )

        return {
            "period": period,
            "dashboard": dashboard,
            "status": "GENERATED",
        }
