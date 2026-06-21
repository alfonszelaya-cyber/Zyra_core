# ============================================================
# inheritance_engine.py
# NEXO / ZYRA
# Inheritance Management Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class InheritanceEngine:

    """
    Gestión de herencias.
    """

    def __init__(self):

        self._inheritances = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def _inheritance_id(self):

        return f"INH-{uuid4()}"

    def create_inheritance(
        self,
        estate_name: str,
        beneficiaries: List[str],
        total_value: float,
    ) -> Dict:

        inheritance = {

            "inheritance_id":
                self._inheritance_id(),

            "estate_name":
                estate_name,

            "beneficiaries":
                beneficiaries,

            "total_value":
                total_value,

            "status":
                "PLANNED",

            "created_at":
                self._now(),
        }

        self._inheritances.append(
            inheritance
        )

        return inheritance

    def get_inheritances(
        self,
    ) -> List[Dict]:

        return list(
            self._inheritances
        )
