from apps.nexo.domain.meta_government.public_metrics_engine import (
    PublicMetricsEngine,
)


class GeneratePublicMetricsUseCase:

    def __init__(
        self,
        public_metrics_engine: PublicMetricsEngine,
    ):
        self._public_metrics_engine = (
            public_metrics_engine
        )

    def execute(
        self,
        indicators: list,
        period: str,
    ) -> dict:

        metrics = (
            self._public_metrics_engine.generate_metrics(
                indicators=indicators,
                period=period,
            )
        )

        return {
            "period": period,
            "indicators": indicators,
            "metrics": metrics,
            "status": "GENERATED",
        }
