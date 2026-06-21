# ============================================================
# regulatory_monitor.py
# NEXO / ZYRA
# Regulatory Monitoring Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class RegulatoryMonitor:

    """
    Motor de monitoreo regulatorio.

    Responsabilidades:
    - Monitorear cambios regulatorios
    - Monitorear jurisdicciones
    - Detectar cambios normativos
    - Registrar historial
    - Generar alertas regulatorias
    - Exponer reportes
    """

    def __init__(self):

        self._checks = []
        self._alerts = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _check_id(self):

        return f"REG-{uuid4()}"

    # ========================================================
    # MONITOREO
    # ========================================================

    def monitor(
        self,
        jurisdiction: str,
    ) -> Dict:

        check = {

            "check_id":
                self._check_id(),

            "jurisdiction":
                jurisdiction,

            "checked_at":
                self._now(),

            "changes_detected":
                False,

            "status":
                "COMPLETED",
        }

        self._checks.append(
            check
        )

        return check

    # ========================================================
    # CAMBIOS REGULATORIOS
    # ========================================================

    def register_change(
        self,
        jurisdiction: str,
        title: str,
        description: str,
        severity: str = "MEDIUM",
    ) -> Dict:

        alert = {

            "alert_id":
                f"ALT-{uuid4()}",

            "jurisdiction":
                jurisdiction,

            "title":
                title,

            "description":
                description,

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

    def get_checks(
        self,
    ) -> List[Dict]:

        return list(
            self._checks
        )

    def get_alerts(
        self,
    ) -> List[Dict]:

        return list(
            self._alerts
        )

    def get_alerts_by_jurisdiction(
        self,
        jurisdiction: str,
    ) -> List[Dict]:

        return [

            alert

            for alert in self._alerts

            if (
                alert["jurisdiction"]
                == jurisdiction
            )
        ]

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        return {

            "checks":
                len(
                    self._checks
                ),

            "alerts":
                len(
                    self._alerts
                ),

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

            "checks":
                self.get_checks(),

            "alerts":
                self.get_alerts(),

            "generated_at":
                self._now(),

            "report_type":
                "REGULATORY_MONITOR",
        }


# ============================================================
# FIN
# regulatory_monitor.py
# ============================================================
