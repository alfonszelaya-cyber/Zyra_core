from apps.nexo.domain.radar_vip.opportunity_engine import (
    OpportunityEngine,
)


class AnalyzeOpportunityUseCase:

    def __init__(
        self,
        opportunity_engine: OpportunityEngine,
    ):
        self._opportunity_engine = (
            opportunity_engine
        )

    def execute(
        self,
        opportunity_id: str,
    ) -> dict:

        result = (
            self._opportunity_engine.analyze(
                opportunity_id=opportunity_id,
            )
        )

        return {
            "opportunity_id": opportunity_id,
            "analysis": result,
            "status": "COMPLETED",
        }
