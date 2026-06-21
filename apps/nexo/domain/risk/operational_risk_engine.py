# ============================================================
# operational_risk_engine.py
# NEXO / ZYRA
# Operational Risk Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class OperationalRiskEngine:

    def __init__(self):

        self._history = []

    def evaluate(
        self,
        logistics_data: dict,
        operations_data: dict,
    ) -> dict:

        score = 0
        findings = []

        delayed_shipments = logistics_data.get(
            "delayed_shipments",
            0,
        )

        failed_processes = operations_data.get(
            "failed_processes",
            0,
        )

        incidents = operations_data.get(
            "incidents",
            0,
        )

        score += min(
            delayed_shipments * 2,
            30,
        )

        score += min(
            failed_processes * 5,
            40,
        )

        score += min(
            incidents * 10,
            30,
        )

        if delayed_shipments > 0:
            findings.append(
                "DELAYED_SHIPMENTS"
            )

        if failed_processes > 0:
            findings.append(
                "FAILED_PROCESSES"
            )

        if incidents > 0:
            findings.append(
                "OPERATIONAL_INCIDENTS"
            )

        if score >= 80:
            level = "CRITICAL"
        elif score >= 60:
            level = "HIGH"
        elif score >= 30:
            level = "MEDIUM"
        else:
            level = "LOW"

        result = {

            "risk_id":
                f"OPR-{uuid4()}",

            "score":
                score,

            "level":
                level,

            "findings":
                findings,

            "generated_at":
                datetime.utcnow().isoformat(),

            "status":
                "EVALUATED",
        }

        self._history.append(
            result
        )

        return result


operational_risk_engine = (
    OperationalRiskEngine()
)
