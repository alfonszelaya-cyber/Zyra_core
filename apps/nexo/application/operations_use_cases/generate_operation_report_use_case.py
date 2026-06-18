from apps.nexo.domain.operations.operations_reporting_engine import (
    OperationsReportingEngine,
)


class GenerateOperationReportUseCase:

    def __init__(
        self,
        operations_reporting_engine: OperationsReportingEngine,
    ):
        self._operations_reporting_engine = (
            operations_reporting_engine
        )

    def execute(
        self,
        period: str,
        filters: dict | None = None,
    ) -> dict:

        report = (
            self._operations_reporting_engine.generate_report(
                period=period,
                filters=filters or {},
            )
        )

        return {
            "period": period,
            "filters": filters or {},
            "report": report,
            "status": "GENERATED",
        }
