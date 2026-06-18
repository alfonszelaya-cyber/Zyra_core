from apps.nexo.domain.operations.operational_metrics_engine import (
    OperationalMetricsEngine,
)


class GenerateOperationalMetricsUseCase:

    def __init__(
        self,
        operational_metrics_engine: (
            OperationalMetricsEngine
        ),
    ):
        self._operational_metrics_engine = (
            operational_metrics_engine
        )

    def execute(
        self,
        period: str,
    ) -> dict:

        metrics = (
            self._operational_metrics_engine.calculate_metrics(
                period=period,
            )
        )

        return {
            "period": period,
            "metrics": metrics,
            "status": "CALCULATED",
        }
