# ============================================================
# process_tracking_engine.py
# NEXO / ZYRA
# Process Tracking Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class ProcessTrackingEngine:

    def __init__(self):

        self._events: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def register_event(
        self,
        process_id: str,
        event_type: str,
        details: Dict = None,
    ) -> Dict:

        event = {

            "event_id":
                f"PTR-{uuid4()}",

            "process_id":
                process_id,

            "event_type":
                event_type,

            "details":
                details or {},

            "created_at":
                self._now(),
        }

        self._events.append(
            event
        )

        return event

    def get_process_history(
        self,
        process_id: str,
    ) -> List[Dict]:

        return [

            event

            for event
            in self._events

            if (
                event["process_id"]
                == process_id
            )
        ]

    def get_last_event(
        self,
        process_id: str,
    ) -> Optional[Dict]:

        history = (
            self.get_process_history(
                process_id
            )
        )

        if not history:
            return None

        return history[-1]

    def get_summary(
        self,
    ):

        return {

            "events":
                len(
                    self._events
                ),

            "generated_at":
                self._now(),

            "status":
                "ACTIVE",
        }


process_tracking_engine = (
    ProcessTrackingEngine()
)

# ============================================================
# FIN
# ============================================================
