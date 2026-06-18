from datetime import datetime

from apps.nexo.domain.logistics.logistics_report_engine import (
    LogisticsReportEngine,
)


class GenerateLogisticsReportUseCase:

    def __init__(
        self,
        report_engine: LogisticsReportEngine,
    ):
        self._report_engine = report_engine

    def execute(
        self,
        company_id: str,
        period: str,
    ) -> dict:

        report = (
            self._report_engine.generate(
                company_id=company_id,
                period=period,
            )
        )

        return {
            "company_id": company_id,
            "period": period,
            "generated_at": datetime.utcnow(),
            "report": report,
        }
