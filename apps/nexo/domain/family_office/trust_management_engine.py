# ============================================================
# trust_management_engine.py
# NEXO / ZYRA
# Trust Management Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class TrustManagementEngine:

    """
    Gestión de Trusts.
    """

    def __init__(self):

        self._trusts = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def _trust_id(self):

        return f"TRUST-{uuid4()}"

    def create_trust(
        self,
        trust_name: str,
        jurisdiction: str,
        beneficiaries: List[str],
    ) -> Dict:

        trust = {

            "trust_id":
                self._trust_id(),

            "trust_name":
                trust_name,

            "jurisdiction":
                jurisdiction,

            "beneficiaries":
                beneficiaries,

            "status":
                "ACTIVE",

            "created_at":
                self._now(),
        }

        self._trusts.append(
            trust
        )

        return trust

    def get_trusts(
        self,
    ) -> List[Dict]:

        return list(
            self._trusts
        )
