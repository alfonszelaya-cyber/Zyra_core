# ============================================================
# national_strategy_engine.py
# NEXO / ZYRA
# National Strategy Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class NationalStrategyEngine:

    def __init__(self):

        self._strategies: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def create_strategy(
        self,
        name: str,
        objective: str,
        initiatives: List[str],
    ) -> Dict:

        strategy = {

            "strategy_id":
                f"STR-{uuid4()}",

            "name":
                name,

            "objective":
                objective,

            "initiatives":
                initiatives,

            "created_at":
                self._now(),

            "status":
                "ACTIVE",
        }

        self._strategies.append(
            strategy
        )

        return strategy

    def get_strategies(
        self,
    ):

        return list(
            self._strategies
        )

    def get_summary(
        self,
    ):

        return {

            "strategies":
                len(
                    self._strategies
                ),

            "generated_at":
                self._now(),
        }


national_strategy_engine = (
    NationalStrategyEngine()
)
