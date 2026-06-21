# ============================================================
# executive_monitor_engine.py
# NEXO / ZYRA
# Executive Monitor Domain Engine
# ============================================================

from datetime import datetime
from typing import Dict, List, Optional


class ExecutiveMonitorEngine:

    """
    Motor Ejecutivo de Monitoreo.

    Responsabilidades:

    - Monitorear indicadores críticos
    - Monitorear operaciones
    - Monitorear finanzas
    - Monitorear cumplimiento
    - Detectar anomalías
    - Alimentar Dashboard Ejecutivo
    - Alimentar Alertas Ejecutivas
    - Alimentar ZYRA
    """

    def __init__(self):

        self._monitoring_history: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    # ========================================================
    # MONITOREO
    # ========================================================

    def monitor_business(
        self,
        indicators: Dict,
    ) -> Dict:

        monitoring = {

            "checked_at":
                self._now(),

            "indicators":
                indicators,

            "status":
                "MONITORED",
        }

        self._monitoring_history.append(
            monitoring
        )

        return monitoring

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_monitoring_history(
        self,
    ) -> List[Dict]:

        return list(
            self._monitoring_history
        )

    def get_last_monitoring(
        self,
    ) -> Optional[Dict]:

        if not self._monitoring_history:
            return None

        return self._monitoring_history[-1]

    # ========================================================
    # ANOMALÍAS
    # ========================================================

    def detect_anomalies(
        self,
        indicators: Dict,
        threshold: float = 100.0,
    ) -> List[Dict]:

        anomalies = []

        for key, value in indicators.items():

            if isinstance(
                value,
                (int, float)
            ):

                if value > threshold:

                    anomalies.append({

                        "indicator":
                            key,

                        "value":
                            value,

                        "threshold":
                            threshold,

                        "detected_at":
                            self._now(),
                    })

        return anomalies

    # ========================================================
    # RESUMEN
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        return {

            "monitoring_records":
                len(
                    self._monitoring_history
                ),

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
                "EXECUTIVE_MONITOR",

            "history":
                self.get_monitoring_history(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),
        }


# ============================================================
# FIN
# executive_monitor_engine.py
# ============================================================
