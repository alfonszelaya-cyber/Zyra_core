# ============================================================
# security_monitor_engine.py
# NEXO / ZYRA
# Security Monitor Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4

from .identity_audit_engine import (
    identity_audit_engine,
)


class SecurityMonitorEngine:

    def __init__(self):

        self._alerts = []

    def analyze_event(
        self,
        audit_event: dict,
    ) -> dict:

        severity = "LOW"

        event_type = audit_event.get(
            "event_type",
            ""
        )

        if event_type in [

            "FAILED_LOGIN",
            "ACCESS_DENIED",
            "TOKEN_TAMPERING",
            "BIOMETRIC_FAILURE",

        ]:

            severity = "HIGH"

        alert = {

            "alert_id":
                f"SEC-{uuid4()}",

            "identity_id":
                audit_event.get(
                    "identity_id"
                ),

            "event_type":
                event_type,

            "severity":
                severity,

            "created_at":
                datetime.utcnow().isoformat(),

            "status":
                "OPEN",
        }

        self._alerts.append(
            alert
        )

        return alert

    def active_alerts(
        self,
    ) -> list:

        return [

            alert
            for alert in self._alerts
            if alert["status"] == "OPEN"
        ]


security_monitor_engine = (
    SecurityMonitorEngine()
)
