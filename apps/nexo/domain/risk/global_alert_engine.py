# ============================================================
# global_alert_engine.py
# NEXO / ZYRA
# Global Alert Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class GlobalAlertEngine:

    def __init__(self):

        self._alerts = []

    def create_alert(
        self,
        compliance_risk: dict,
        country_risk: dict,
        financial_risk: dict,
        fraud_risk: dict,
        geopolitical_risk: dict,
    ) -> dict:

        scores = [

            compliance_risk.get(
                "score",
                0,
            ),

            country_risk.get(
                "score",
                0,
            ),

            financial_risk.get(
                "score",
                0,
            ),

            fraud_risk.get(
                "score",
                0,
            ),

            geopolitical_risk.get(
                "score",
                0,
            ),
        ]

        global_score = max(
            scores
        )

        if global_score >= 80:
            level = "CRITICAL"

        elif global_score >= 60:
            level = "HIGH"

        elif global_score >= 30:
            level = "MEDIUM"

        else:
            level = "LOW"

        alert = {

            "alert_id":
                f"ALT-{uuid4()}",

            "global_score":
                global_score,

            "level":
                level,

            "created_at":
                datetime.utcnow().isoformat(),

            "status":
                "OPEN",
        }

        self._alerts.append(
            alert
        )

        return alert


global_alert_engine = (
    GlobalAlertEngine()
)
