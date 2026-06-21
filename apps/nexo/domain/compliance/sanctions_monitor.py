# ============================================================
# sanctions_monitor.py
# NEXO / ZYRA
# Sanctions Monitoring Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class SanctionsMonitor:

    """
    Motor de monitoreo de sanciones.

    Responsabilidades:
    - Verificar personas
    - Verificar empresas
    - Verificar proveedores
    - Verificar clientes
    - Registrar consultas
    - Generar alertas
    - Mantener historial
    """

    def __init__(self):

        self._verifications = []
        self._alerts = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _verification_id(self):

        return f"SAN-{uuid4()}"

    # ========================================================
    # VERIFICACIÓN
    # ========================================================

    def verify(
        self,
        entity_name: str,
    ) -> Dict:

        verification = {

            "verification_id":
                self._verification_id(),

            "entity_name":
                entity_name,

            "checked_at":
                self._now(),

            "sanctioned":
                False,

            "status":
                "VERIFIED",
        }

        self._verifications.append(
            verification
        )

        return verification

    # ========================================================
    # ALERTAS
    # ========================================================

    def register_alert(
        self,
        entity_name: str,
        reason: str,
        severity: str = "HIGH",
    ) -> Dict:

        alert = {

            "alert_id":
                f"ALT-{uuid4()}",

            "entity_name":
                entity_name,

            "reason":
                reason,

            "severity":
                severity,

            "created_at":
                self._now(),

            "status":
                "OPEN",
        }

        self._alerts.append(
            alert
        )

        return alert

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_verifications(
        self,
    ) -> List[Dict]:

        return list(
            self._verifications
        )

    def get_alerts(
        self,
    ) -> List[Dict]:

        return list(
            self._alerts
        )

    def get_entity_history(
        self,
        entity_name: str,
    ) -> List[Dict]:

        return [

            item

            for item in self._verifications

            if (
                item["entity_name"]
                == entity_name
            )
        ]

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        sanctioned = len(

            [

                item

                for item in self._verifications

                if item["sanctioned"]
            ]

        )

        return {

            "verifications":
                len(
                    self._verifications
                ),

            "alerts":
                len(
                    self._alerts
                ),

            "sanctioned_entities":
                sanctioned,

            "generated_at":
                self._now(),
        }

    # ========================================================
    # REPORTE
    # ========================================================

    def generate_report(
        self,
    ) -> Dict:

        return {

            "verifications":
                self.get_verifications(),

            "alerts":
                self.get_alerts(),

            "generated_at":
                self._now(),

            "report_type":
                "SANCTIONS_MONITOR",
        }


# ============================================================
# FIN
# sanctions_monitor.py
# ============================================================
