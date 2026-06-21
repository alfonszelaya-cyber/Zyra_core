# ============================================================
# family_governance_engine.py
# NEXO / ZYRA
# Family Governance Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class FamilyGovernanceEngine:

    """
    Gobierno familiar.
    """

    def __init__(self):

        self._decisions = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def _decision_id(self):

        return f"FGV-{uuid4()}"

    def register_decision(
        self,
        subject: str,
        participants: List[str],
        resolution: str,
    ) -> Dict:

        decision = {

            "decision_id":
                self._decision_id(),

            "subject":
                subject,

            "participants":
                participants,

            "resolution":
                resolution,

            "created_at":
                self._now(),

            "status":
                "APPROVED",
        }

        self._decisions.append(
            decision
        )

        return decision

    def get_decisions(
        self,
    ) -> List[Dict]:

        return list(
            self._decisions
        )
