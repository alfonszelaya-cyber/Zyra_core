# ============================================================
# shipment_engine.py
# NEXO / ZYRA
# Shipment Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class ShipmentEngine:

    def __init__(self):

        self._shipments: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def create_shipment(
        self,
        customer_id: str,
        origin: str,
        destination: str,
        cargo_type: str,
        weight: float,
    ) -> Dict:

        shipment = {

            "shipment_id":
                f"SHP-{uuid4()}",

            "customer_id":
                customer_id,

            "origin":
                origin,

            "destination":
                destination,

            "cargo_type":
                cargo_type,

            "weight":
                weight,

            "created_at":
                self._now(),

            "status":
                "CREATED",
        }

        self._shipments.append(
            shipment
        )

        return shipment

    def update_status(
        self,
        shipment_id: str,
        status: str,
    ) -> Optional[Dict]:

        for shipment in self._shipments:

            if (
                shipment["shipment_id"]
                == shipment_id
            ):

                shipment["status"] = status

                shipment["updated_at"] = (
                    self._now()
                )

                return shipment

        return None

    def get_shipments(
        self,
    ):

        return list(
            self._shipments
        )


shipment_engine = (
    ShipmentEngine()
)
