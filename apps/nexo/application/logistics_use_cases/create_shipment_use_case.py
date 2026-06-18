from apps.nexo.domain.logistics.shipment_engine import (
    ShipmentEngine,
)


class CreateShipmentUseCase:

    def __init__(
        self,
        shipment_engine: ShipmentEngine,
    ):
        self._shipment_engine = shipment_engine

    def execute(
        self,
        origin: str,
        destination: str,
        cargo: dict,
    ) -> dict:

        shipment = (
            self._shipment_engine.create_shipment(
                origin=origin,
                destination=destination,
                cargo=cargo,
            )
        )

        return {
            "shipment_id": shipment["shipment_id"],
            "origin": origin,
            "destination": destination,
            "status": "CREATED",
        }
