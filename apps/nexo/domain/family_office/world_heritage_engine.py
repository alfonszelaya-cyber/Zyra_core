# ============================================================
# world_heritage_engine.py
# NEXO / ZYRA
# World Heritage Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class WorldHeritageEngine:

    """
    Gestión de patrimonio mundial.

    Aplicable a:

    - Sitios históricos
    - Patrimonio cultural
    - Patrimonio natural
    - Patrimonio digital
    - Colecciones privadas
    - Activos históricos familiares
    - Conservación patrimonial
    """

    def __init__(self):

        self._heritage_assets = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _heritage_id(self):

        return f"WH-{uuid4()}"

    # ========================================================
    # REGISTRO
    # ========================================================

    def register_heritage_asset(
        self,
        asset_name: str,
        asset_type: str,
        country: str,
        estimated_value: float,
        metadata: Optional[Dict] = None,
    ) -> Dict:

        asset = {

            "heritage_id":
                self._heritage_id(),

            "asset_name":
                asset_name,

            "asset_type":
                asset_type,

            "country":
                country,

            "estimated_value":
                estimated_value,

            "metadata":
                metadata or {},

            "status":
                "REGISTERED",

            "created_at":
                self._now(),
        }

        self._heritage_assets.append(
            asset
        )

        return asset

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_assets(
        self,
    ) -> List[Dict]:

        return list(
            self._heritage_assets
        )

    def get_asset(
        self,
        heritage_id: str,
    ) -> Optional[Dict]:

        for asset in self._heritage_assets:

            if (
                asset["heritage_id"]
                == heritage_id
            ):
                return asset

        return None

    # ========================================================
    # VALORACIÓN
    # ========================================================

    def calculate_total_value(
        self,
    ) -> float:

        return round(

            sum(
                asset.get(
                    "estimated_value",
                    0
                )
                for asset
                in self._heritage_assets
            ),

            2,
        )

    # ========================================================
    # RESUMEN
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        return {

            "total_assets":
                len(
                    self._heritage_assets
                ),

            "total_value":
                self.calculate_total_value(),

            "generated_at":
                self._now(),

            "status":
                "ACTIVE",
        }

    # ========================================================
    # REPORTE
    # ========================================================

    def generate_report(
        self,
    ) -> Dict:

        return {

            "report_type":
                "WORLD_HERITAGE",

            "assets":
                self.get_assets(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),
        }


# ============================================================
# FIN
# world_heritage_engine.py
# ============================================================
