# ============================================================
# succession_engine.py
# NEXO / ZYRA
# Succession Planning Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class SuccessionEngine:

    """
    Planificación sucesoria.
    """

    def __init__(self):

        self._plans = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def _plan_id(self):

        return f"SUC-{uuid4()}"

    def create_plan(
        self,
        title: str,
        successors: List[str],
        assets: List[str],
    ) -> Dict:

        plan = {

            "plan_id":
                self._plan_id(),

            "title":
                title,

            "successors":
                successors,

            "assets":
                assets,

            "status":
                "ACTIVE",

            "created_at":
                self._now(),
        }

        self._plans.append(
            plan
        )

        return plan

    def get_plans(
        self,
    ) -> List[Dict]:

        return list(
            self._plans
        )
