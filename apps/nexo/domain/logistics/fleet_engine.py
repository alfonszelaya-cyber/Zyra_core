# ============================================================
# fleet_engine.py
# NEXO / ZYRA
# Fleet Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class FleetEngine:

    def __init__(self):

        self._vehicles: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def register_vehicle(
        self,
        plate: str,
        vehicle_type: str,
        capacity: float,
    ) -> Dict:

        vehicle = {

            "vehicle_id":
                f"FLT-{uuid4()}",

            "plate":
                plate,

            "vehicle_type":
                vehicle_type,

            "capacity":
                capacity,

            "created_at":
                self._now(),

            "status":
                "ACTIVE",
        }

        self._vehicles.append(vehicle)

        return vehicle

    def update_status(
        self,
        vehicle_id: str,
        status: str,
    ) -> Optional[Dict]:

        for vehicle in self._vehicles:

            if (
                vehicle["vehicle_id"]
                == vehicle_id
            ):

                vehicle["status"] = status

                vehicle["updated_at"] = (
                    self._now()
                )

                return vehicle

        return None

    def get_vehicles(self):

        return list(
            self._vehicles
        )


fleet_engine = (
    FleetEngine()
)
