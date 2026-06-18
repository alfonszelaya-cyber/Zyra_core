from datetime import datetime

from apps.nexo.domain.logistics.delivery_engine import (
    DeliveryEngine,
)


class ConfirmDeliveryUseCase:

    def __init__(
        self,
        delivery_engine: DeliveryEngine,
    ):
        self._delivery_engine = delivery_engine

    def execute(
        self,
        shipment_id: str,
        receiver_id: str,
    ) -> dict:

        delivery = (
            self._delivery_engine.confirm_delivery(
                shipment_id=shipment_id,
                receiver_id=receiver_id,
                delivered_at=datetime.utcnow(),
            )
        )

        return {
            "shipment_id": shipment_id,
            "receiver_id": receiver_id,
            "status": "DELIVERED",
            "delivery": delivery,
        }
