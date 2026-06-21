# ============================================================
# compliance_risk_engine.py
# NEXO / ZYRA
# Compliance Risk Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class ComplianceRiskEngine:

    def __init__(self):

        self._history = []

    def evaluate(
        self,
        compliance_record: dict,
        sanctions_result: dict,
    ) -> dict:

        score = 0

        if not compliance_record.get(
            "valid",
            False,
        ):
            score += 50

        if sanctions_result.get(
            "sanctioned",
            False,
        ):
            score += 50

        if score >= 80:
            level = "CRITICAL"

        elif score >= 50:
            level = "HIGH"

        elif score >= 20:
            level = "MEDIUM"

        else:
            level = "LOW"

        result = {

            "risk_id":
                f"CR-{uuid4()}",

            "risk_type":
                "COMPLIANCE",

            "score":
                score,

            "level":
                level,

            "generated_at":
                datetime.utcnow().isoformat(),

            "status":
                "EVALUATED",
        }

        self._history.append(
            result
        )

        return result


compliance_risk_engine = (
    ComplianceRiskEngine()
)
