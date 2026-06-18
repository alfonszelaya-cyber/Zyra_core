from apps.nexo.domain.executive.executive_kpi_engine import (
    ExecutiveKpiEngine,
)


class GenerateKpiUseCase:

    def __init__(
        self,
        kpi_engine: ExecutiveKpiEngine,
    ):
        self._kpi_engine = kpi_engine

    def execute(
        self,
        company_id: str,
    ) -> dict:

        kpis = self._kpi_engine.calculate_kpis(
            company_id
        )

        return {
            "company_id": company_id,
            "kpis": kpis,
            "total_kpis": len(kpis),
        }
