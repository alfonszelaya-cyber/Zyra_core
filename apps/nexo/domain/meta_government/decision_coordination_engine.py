# ============================================================
# decision_coordination_engine.py
# NEXO / ZYRA
# Meta Government Decision Coordination Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class DecisionCoordinationEngine:

    def __init__(self):

        self._decisions: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def create_decision(
        self,
        title: str,
        description: str,
        priority: str,
        stakeholders: List[str],
    ) -> Dict:

        decision = {

            "decision_id":
                f"DEC-{uuid4()}",

            "title":
                title,

            "description":
                description,

            "priority":
                priority,

            "stakeholders":
                stakeholders,

            "created_at":
                self._now(),

            "status":
                "PENDING",
        }

        self._decisions.append(
            decision
        )

        return decision

    def approve_decision(
        self,
        decision_id: str,
    ) -> Optional[Dict]:

        for decision in self._decisions:

            if (
                decision["decision_id"]
                == decision_id
            ):

                decision["status"] = (
                    "APPROVED"
                )

                decision[
                    "approved_at"
                ] = self._now()

                return decision

        return None

    def get_decisions(self):

        return list(
            self._decisions
        )


decision_coordination_engine = (
    DecisionCoordinationEngine()
)
