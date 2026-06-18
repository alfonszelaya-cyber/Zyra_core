from apps.nexo.domain.government.institution_coordination_engine import (
    InstitutionCoordinationEngine,
)


class CoordinateInstitutionUseCase:

    def __init__(
        self,
        coordination_engine: InstitutionCoordinationEngine,
    ):
        self._coordination_engine = (
            coordination_engine
        )

    def execute(
        self,
        institution_id: str,
        operation_id: str,
    ) -> dict:

        coordination = (
            self._coordination_engine.coordinate(
                institution_id=institution_id,
                operation_id=operation_id,
            )
        )

        return {
            "institution_id": institution_id,
            "operation_id": operation_id,
            "coordination": coordination,
        }
