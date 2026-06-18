from datetime import datetime

from apps.nexo.domain.government.government_report_engine import (
    GovernmentReportEngine,
)


class GenerateGovernmentReportUseCase:

    def __init__(
        self,
        report_engine: GovernmentReportEngine,
    ):
        self._report_engine = report_engine

    def execute(
        self,
        institution_id: str,
        period: str,
    ) -> dict:

        report = (
            self._report_engine.generate(
                institution_id=institution_id,
                period=period,
            )
        )

        return {
            "institution_id": institution_id,
            "period": period,
            "generated_at": datetime.utcnow(),
            "report": report,
        }
