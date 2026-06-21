# ============================================================
# family_asset_engine.py
# NEXO / ZYRA
# Family Office Asset Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class FamilyAssetEngine:

    """
    Gestión de activos patrimoniales.
    """

    def __init__(self):

        self._assets = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def _asset_id(self):

        return f"AST-{uuid4()}"

    def register_asset(
        self,
        asset_type: str,
        asset_name: str,
        value: float,
        jurisdiction: str,
        metadata: dict | None = None,
    ) -> Dict:

        asset = {

            "asset_id":
                self._asset_id(),

            "asset_type":
                asset_type,

            "asset_name":
                asset_name,

            "value":
                value,

            "jurisdiction":
                jurisdiction,

            "metadata":
                metadata or {},

            "status":
                "ACTIVE",

            "created_at":
                self._now(),
        }

        self._assets.append(
            asset
        )

        return asset

    def get_assets(
        self,
    ) -> List[Dict]:

        return list(
            self._assets
        )

    def calculate_total_assets(
        self,
    ) -> float:

        return round(

            sum(
                asset["value"]
                for asset
                in self._assets
            ),

            2,
        )
