from apps.nexo.domain.meta_government.institution_coordination_engine import (
    InstitutionCoordinationEngine,
)


class CoordinateInstitutionsUseCase:

    def __init__(
        self,
        institution_coordination_engine: InstitutionCoordinationEngine,
    ):
        self._institution_coordination_engine = (
            institution_coordination_engine
        )

    def execute(
        self,
        institutions: list,
        objective: str,
    ) -> dict:

        coordination = (
            self._institution_coordination_engine.coordinate(
                institutions=institutions,
                objective=objective,
            )
        )

        return {
            "objective": objective,
            "institutions": institutions,
            "coordination": coordination,
            "status": "COORDINATED",
        }
