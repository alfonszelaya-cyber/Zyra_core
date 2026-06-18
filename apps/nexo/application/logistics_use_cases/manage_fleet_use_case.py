from apps.nexo.domain.logistics.fleet_engine import (
    FleetEngine,
)


class ManageFleetUseCase:

    def __init__(
        self,
        fleet_engine: FleetEngine,
    ):
        self._fleet_engine = fleet_engine

    def execute(
        self,
        vehicle_id: str,
        action: str,
        payload: dict,
    ) -> dict:

        result = self._fleet_engine.manage_vehicle(
            vehicle_id=vehicle_id,
            action=action,
            payload=payload,
        )

        return {
            "vehicle_id": vehicle_id,
            "action": action,
            "status": "PROCESSED",
            "result": result,
        }
