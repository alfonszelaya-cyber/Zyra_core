from apps.nexo.domain.logistics.tracking_engine import (
    TrackingEngine,
)


class TrackShipmentUseCase:

    def __init__(
        self,
        tracking_engine: TrackingEngine,
    ):
        self._tracking_engine = tracking_engine

    def execute(
        self,
        shipment_id: str,
    ) -> dict:

        tracking = self._tracking_engine.track(
            shipment_id=shipment_id,
        )

        return {
            "shipment_id": shipment_id,
            "tracking": tracking,
            "status": tracking.get(
                "status",
                "UNKNOWN",
            ),
        }
