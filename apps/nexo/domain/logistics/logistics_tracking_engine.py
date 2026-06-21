# ============================================================
# logistics_tracking_engine.py
# NEXO / ZYRA
# Logistics Tracking Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class LogisticsTrackingEngine:

    def __init__(self):

        self._tracking_events: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def register_event(
        self,
        shipment_id: str,
        location: str,
        status: str,
        details: Dict = None,
    ) -> Dict:

        event = {

            "tracking_id":
                f"TRK-{uuid4()}",

            "shipment_id":
                shipment_id,

            "location":
                location,

            "status":
                status,

            "details":
                details or {},

            "created_at":
                self._now(),
        }

        self._tracking_events.append(
            event
        )

        return event

    def get_tracking(
        self,
        shipment_id: str,
    ) -> List[Dict]:

        return [

            e

            for e
            in self._tracking_events

            if (
                e["shipment_id"]
                == shipment_id
            )
        ]

    def get_last_status(
        self,
        shipment_id: str,
    ) -> Optional[Dict]:

        events = self.get_tracking(
            shipment_id
        )

        if not events:
            return None

        return events[-1]


logistics_tracking_engine = (
    LogisticsTrackingEngine()
)
