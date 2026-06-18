from datetime import datetime

from apps.nexo.domain.executive.executive_report_engine import (
    ExecutiveReportEngine,
)


class GenerateExecutiveReportUseCase:

    def __init__(
        self,
        report_engine: ExecutiveReportEngine,
    ):
        self._report_engine = report_engine

    def execute(
        self,
        company_id: str,
        period: str,
    ) -> dict:

        report = self._report_engine.generate(
            company_id=company_id,
            period=period,
        )

        return {
            "company_id": company_id,
            "period": period,
            "generated_at": datetime.utcnow(),
            "report": report,
        }
