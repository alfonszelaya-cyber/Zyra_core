# ============================================================
# delivery_engine.py
# NEXO / ZYRA
# Delivery Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class DeliveryEngine:

    def __init__(self):

        self._deliveries: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def create_delivery(
        self,
        shipment_id: str,
        customer_id: str,
        destination: str,
        carrier: str,
    ) -> Dict:

        delivery = {

            "delivery_id":
                f"DEL-{uuid4()}",

            "shipment_id":
                shipment_id,

            "customer_id":
                customer_id,

            "destination":
                destination,

            "carrier":
                carrier,

            "created_at":
                self._now(),

            "status":
                "PENDING",
        }

        self._deliveries.append(delivery)

        return delivery

    def update_status(
        self,
        delivery_id: str,
        status: str,
    ) -> Optional[Dict]:

        for delivery in self._deliveries:

            if (
                delivery["delivery_id"]
                == delivery_id
            ):

                delivery["status"] = status

                delivery["updated_at"] = (
                    self._now()
                )

                return delivery

        return None

    def get_deliveries(self):

        return list(
            self._deliveries
        )


delivery_engine = (
    DeliveryEngine()
)
