from apps.nexo.domain.meta_government.governance_analysis_engine import (
    GovernanceAnalysisEngine,
)


class AnalyzeGovernanceUseCase:

    def __init__(
        self,
        governance_analysis_engine: GovernanceAnalysisEngine,
    ):
        self._governance_analysis_engine = governance_analysis_engine

    def execute(
        self,
        period: str,
        institutions: list,
    ) -> dict:

        analysis = (
            self._governance_analysis_engine.analyze(
                period=period,
                institutions=institutions,
            )
        )

        return {
            "period": period,
            "institutions": institutions,
            "analysis": analysis,
            "status": "COMPLETED",
        }
