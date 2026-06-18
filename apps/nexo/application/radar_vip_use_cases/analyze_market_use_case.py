from apps.nexo.domain.radar_vip.market_analysis_engine import (
    MarketAnalysisEngine,
)


class AnalyzeMarketUseCase:

    def __init__(
        self,
        market_analysis_engine: MarketAnalysisEngine,
    ):
        self._market_analysis_engine = (
            market_analysis_engine
        )

    def execute(
        self,
        market: str,
        filters: dict | None = None,
    ) -> dict:

        analysis = (
            self._market_analysis_engine.analyze_market(
                market=market,
                filters=filters or {},
            )
        )

        return {
            "market": market,
            "analysis": analysis,
            "status": "ANALYZED",
        }
