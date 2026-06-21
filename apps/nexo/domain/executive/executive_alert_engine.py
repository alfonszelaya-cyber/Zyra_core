# ============================================================
# executive_alert_engine.py
# NEXO / ZYRA
# Executive Alert Domain Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class ExecutiveAlertEngine:

    """
    Motor Ejecutivo de Alertas.

    Responsabilidades:

    - Crear alertas ejecutivas
    - Clasificar severidad
    - Gestionar estados
    - Escalar eventos críticos
    - Integrar con Dashboard Ejecutivo
    - Integrar con KPIs
    - Integrar con Monitor Ejecutivo
    - Integrar con Reportes
    - Preparar datos para ZYRA
    """

    VALID_LEVELS = (
        "INFO",
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
    )

    VALID_STATUS = (
        "OPEN",
        "IN_PROGRESS",
        "RESOLVED",
        "CLOSED",
        "ESCALATED",
    )

    def __init__(self):

        self._alerts: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self) -> str:

        return datetime.utcnow().isoformat()

    def _generate_alert_id(self) -> str:

        return f"ALT-{uuid4()}"

    # ========================================================
    # VALIDACIÓN
    # ========================================================

    def validate_alert(
        self,
        level: str,
        title: str,
        description: str,
    ) -> bool:

        if level not in self.VALID_LEVELS:
            return False

        if not title:
            return False

        if not description:
            return False

        return True

    # ========================================================
    # CREACIÓN
    # ========================================================

    def create_alert(
        self,
        level: str,
        title: str,
        description: str,
        source_module: Optional[str] = None,
        reference_id: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> Dict:

        if not self.validate_alert(
            level,
            title,
            description,
        ):
            raise ValueError(
                "Invalid alert data"
            )

        alert = {

            "alert_id":
                self._generate_alert_id(),

            "level":
                level,

            "title":
                title,

            "description":
                description,

            "source_module":
                source_module,

            "reference_id":
                reference_id,

            "metadata":
                metadata or {},

            "status":
                "OPEN",

            "created_at":
                self._now(),

            "updated_at":
                self._now(),
        }

        self._alerts.append(alert)

        return alert

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_alert(
        self,
        alert_id: str,
    ) -> Optional[Dict]:

        for alert in self._alerts:

            if (
                alert["alert_id"]
                == alert_id
            ):
                return alert

        return None

    def get_alerts(
        self,
    ) -> List[Dict]:

        return list(
            self._alerts
        )

    def get_open_alerts(
        self,
    ) -> List[Dict]:

        return [

            alert

            for alert in self._alerts

            if (
                alert["status"]
                == "OPEN"
            )

        ]

    def get_critical_alerts(
        self,
    ) -> List[Dict]:

        return [

            alert

            for alert in self._alerts

            if (
                alert["level"]
                == "CRITICAL"
            )

        ]

    # ========================================================
    # ACTUALIZACIÓN
    # ========================================================

    def update_status(
        self,
        alert_id: str,
        status: str,
    ) -> Optional[Dict]:

        if status not in self.VALID_STATUS:
            return None

        alert = self.get_alert(
            alert_id
        )

        if not alert:
            return None

        alert["status"] = status

        alert["updated_at"] = (
            self._now()
        )

        return alert

    def escalate_alert(
        self,
        alert_id: str,
    ) -> Optional[Dict]:

        alert = self.get_alert(
            alert_id
        )

        if not alert:
            return None

        alert["status"] = (
            "ESCALATED"
        )

        alert["updated_at"] = (
            self._now()
        )

        return alert

    def close_alert(
        self,
        alert_id: str,
    ) -> Optional[Dict]:

        alert = self.update_status(
            alert_id,
            "CLOSED",
        )

        if alert:

            alert["closed_at"] = (
                self._now()
            )

        return alert

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        return {

            "total_alerts":
                len(
                    self._alerts
                ),

            "open_alerts":
                len(
                    self.get_open_alerts()
                ),

            "critical_alerts":
                len(
                    self.get_critical_alerts()
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

            "report_type":
                "EXECUTIVE_ALERTS",

            "alerts":
                self.get_alerts(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),
        }


# ============================================================
# FIN
# executive_alert_engine.py
# ============================================================
