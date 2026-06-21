# ============================================================
# client_segmentation_engine.py
# NEXO / ZYRA
# Client Segmentation Domain Engine
# ============================================================

from datetime import datetime
from typing import Dict


class ClientSegmentationEngine:

    """
    Motor de segmentación.

    Responsabilidades:
    - Segmentación comercial
    - Segmentación financiera
    - Segmentación fiscal
    - Segmentación operativa
    - Segmentación de riesgo
    - Segmentación VIP
    """

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    # ========================================================
    # SEGMENTACIÓN PRINCIPAL
    # ========================================================

    def segment(
        self,
        annual_volume: float,
    ) -> str:

        if annual_volume >= 10000000:
            return "CORPORATE"

        if annual_volume >= 1000000:
            return "ENTERPRISE"

        if annual_volume >= 100000:
            return "BUSINESS"

        return "STANDARD"

    # ========================================================
    # SEGMENTACIÓN POR RIESGO
    # ========================================================

    def risk_segment(
        self,
        risk_level: str,
    ) -> str:

        if risk_level == "CRITICAL":
            return "HIGH_RISK"

        if risk_level == "HIGH":
            return "RISK"

        if risk_level == "MEDIUM":
            return "MONITORED"

        return "NORMAL"

    # ========================================================
    # SEGMENTACIÓN VIP
    # ========================================================

    def vip_segment(
        self,
        zyra_score: int,
        annual_volume: float,
    ) -> str:

        if (
            annual_volume >= 1000000
            and zyra_score >= 90
        ):
            return "VIP"

        return "STANDARD"

    # ========================================================
    # PERFIL COMPLETO
    # ========================================================

    def build_segmentation(
        self,
        annual_volume: float,
        risk_level: str,
        zyra_score: int,
    ) -> Dict:

        return {

            "commercial_segment":
                self.segment(
                    annual_volume
                ),

            "risk_segment":
                self.risk_segment(
                    risk_level
                ),

            "vip_segment":
                self.vip_segment(
                    zyra_score,
                    annual_volume,
                ),

            "annual_volume":
                annual_volume,

            "risk_level":
                risk_level,

            "zyra_score":
                zyra_score,

            "generated_at":
                self._now(),
        }

    # ========================================================
    # RESUMEN
    # ========================================================

    def generate_summary(
        self,
        segmentation: Dict,
    ) -> Dict:

        return {

            "commercial_segment":
                segmentation.get(
                    "commercial_segment"
                ),

            "risk_segment":
                segmentation.get(
                    "risk_segment"
                ),

            "vip_segment":
                segmentation.get(
                    "vip_segment"
                ),

            "generated_at":
                self._now(),
        }


# ============================================================
# FIN
# ============================================================
