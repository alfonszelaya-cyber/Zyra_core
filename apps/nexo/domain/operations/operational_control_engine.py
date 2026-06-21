# ============================================================
# operational_control_engine.py
# NEXO / ZYRA
# Operational Control Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class OperationalControlEngine:

    def __init__(self):

        self._controls: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def create_control(
        self,
        operation_id: str,
        control_type: str,
        details: Dict,
    ) -> Dict:

        control = {

            "control_id":
                f"CTRL-{uuid4()}",

            "operation_id":
                operation_id,

            "control_type":
                control_type,

            "details":
                details,

            "created_at":
                self._now(),

            "status":
                "ACTIVE",
        }

        self._controls.append(
            control
        )

        return control

    def close_control(
        self,
        control_id: str,
    ) -> Optional[Dict]:

        for control in self._controls:

            if (
                control["control_id"]
                == control_id
            ):

                control["status"] = (
                    "CLOSED"
                )

                control[
                    "closed_at"
                ] = self._now()

                return control

        return None

    def get_controls(
        self,
    ):

        return list(
            self._controls
        )


operational_control_engine = (
    OperationalControlEngine()
)
