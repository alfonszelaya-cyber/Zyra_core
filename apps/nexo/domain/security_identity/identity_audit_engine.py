# ============================================================
# identity_audit_engine.py
# NEXO / ZYRA
# Identity Audit Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class IdentityAuditEngine:

    def __init__(self):

        self._events = []

    def register_event(
        self,
        identity_id: str,
        event_type: str,
        details: dict,
    ) -> dict:

        event = {

            "audit_id":
                f"AUD-{uuid4()}",

            "identity_id":
                identity_id,

            "event_type":
                event_type,

            "details":
                details,

            "created_at":
                datetime.utcnow().isoformat(),

            "status":
                "RECORDED",
        }

        self._events.append(
            event
        )

        return event

    def get_history(
        self,
        identity_id: str,
    ) -> list:

        return [

            event
            for event in self._events
            if event["identity_id"]
            == identity_id
        ]


identity_audit_engine = (
    IdentityAuditEngine()
)
