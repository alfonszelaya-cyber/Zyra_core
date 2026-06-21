# ============================================================
# fraud_detection_engine.py
# NEXO / ZYRA
# Fraud Detection Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class FraudDetectionEngine:

    def __init__(self):

        self._history = []

    def detect(
        self,
        client_data: dict,
        accounting_data: dict,
        operations_data: dict,
    ) -> dict:

        score = 0
        flags = []

        if accounting_data.get(
            "duplicate_transactions",
            0,
        ) > 0:

            score += 30

            flags.append(
                "DUPLICATE_TRANSACTIONS"
            )

        if accounting_data.get(
            "unusual_amounts",
            False,
        ):

            score += 30

            flags.append(
                "UNUSUAL_AMOUNTS"
            )

        if operations_data.get(
            "abnormal_activity",
            False,
        ):

            score += 40

            flags.append(
                "ABNORMAL_ACTIVITY"
            )

        if score >= 80:
            level = "CRITICAL"
        elif score >= 50:
            level = "HIGH"
        elif score >= 25:
            level = "MEDIUM"
        else:
            level = "LOW"

        result = {

            "fraud_id":
                f"FRD-{uuid4()}",

            "client_id":
                client_data.get(
                    "client_id"
                ),

            "score":
                score,

            "level":
                level,

            "flags":
                flags,

            "generated_at":
                datetime.utcnow().isoformat(),

            "status":
                "ANALYZED",
        }

        self._history.append(
            result
        )

        return result


fraud_detection_engine = (
    FraudDetectionEngine()
)
