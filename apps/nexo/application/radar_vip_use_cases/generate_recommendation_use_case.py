from apps.nexo.domain.radar_vip.recommendation_engine import (
    RecommendationEngine,
)


class GenerateRecommendationUseCase:

    def __init__(
        self,
        recommendation_engine: (
            RecommendationEngine
        ),
    ):
        self._recommendation_engine = (
            recommendation_engine
        )

    def execute(
        self,
        opportunity_data: dict,
    ) -> dict:

        recommendation = (
            self._recommendation_engine.generate(
                opportunity_data=opportunity_data,
            )
        )

        return {
            "recommendation": recommendation,
            "status": "GENERATED",
        }
