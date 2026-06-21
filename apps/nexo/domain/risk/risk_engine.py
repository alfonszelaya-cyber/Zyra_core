# ============================================================
# risk_engine.py
# NEXO / ZYRA
# Master Risk Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4

from .compliance_risk_engine import (
    compliance_risk_engine,
)

from .country_risk_engine import (
    country_risk_engine,
)

from .financial_risk_engine import (
    financial_risk_engine,
)

from .fraud_detection_engine import (
    fraud_detection_engine,
)

from .geopolitical_risk_engine import (
    geopolitical_risk_engine,
)

from .operational_risk_engine import (
    operational_risk_engine,
)


class RiskEngine:

    def __init__(self):

        self._history = []

    def evaluate(
        self,
        risk_components: dict,
    ) -> dict:

        scores = []

        for component in risk_components.values():

            scores.append(
                component.get(
                    "score",
                    0,
                )
            )

        global_score = (
            round(
                sum(scores)
                / len(scores),
                2,
            )
            if scores
            else 0
        )

        if global_score >= 80:
            level = "CRITICAL"

        elif global_score >= 60:
            level = "HIGH"

        elif global_score >= 30:
            level = "MEDIUM"

        else:
            level = "LOW"

        result = {

            "risk_id":
                f"RISK-{uuid4()}",

            "score":
                global_score,

            "level":
                level,

            "components":
                risk_components,

            "generated_at":
                datetime.utcnow().isoformat(),

            "status":
                "COMPLETED",
        }

        self._history.append(
            result
        )

        return result


risk_engine = RiskEngine()
