from apps.nexo.domain.executive.executive_metrics_engine import (
    ExecutiveMetricsEngine,
)


class AnalyzeMetricsUseCase:

    def __init__(
        self,
        metrics_engine: ExecutiveMetricsEngine,
    ):
        self._metrics_engine = metrics_engine

    def execute(
        self,
        company_id: str,
    ) -> dict:

        metrics = self._metrics_engine.collect_metrics(
            company_id
        )

        analysis = self._metrics_engine.analyze(
            metrics
        )

        return {
            "company_id": company_id,
            "metrics": metrics,
            "analysis": analysis,
        }
