# ============================================================
# executive_report_engine.py
# NEXO / ZYRA
# Executive Report Domain Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class ExecutiveReportEngine:

    """
    Motor Ejecutivo de Reportes.

    Responsabilidades:

    - Generar reportes ejecutivos
    - Consolidar dashboard
    - Consolidar KPIs
    - Consolidar métricas
    - Consolidar alertas
    - Consolidar decisiones
    - Alimentar Panel Ejecutivo ROOT
    - Alimentar Gobierno del Sistema
    - Alimentar ZYRA
    """

    def __init__(self):

        self._reports: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _report_id(self):

        return f"EXR-{uuid4()}"

    # ========================================================
    # GENERACIÓN
    # ========================================================

    def generate_report(
        self,
        dashboard_data: Dict,
        report_scope: str = "GLOBAL",
    ) -> Dict:

        report = {

            "report_id":
                self._report_id(),

            "generated_at":
                self._now(),

            "report_type":
                "EXECUTIVE",

            "report_scope":
                report_scope,

            "data":
                dashboard_data,

            "status":
                "GENERATED",
        }

        self._reports.append(
            report
        )

        return report

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_reports(
        self,
    ) -> List[Dict]:

        return list(
            self._reports
        )

    def get_report(
        self,
        report_id: str,
    ) -> Optional[Dict]:

        for report in self._reports:

            if (
                report["report_id"]
                == report_id
            ):
                return report

        return None

    def get_last_report(
        self,
    ) -> Optional[Dict]:

        if not self._reports:
            return None

        return self._reports[-1]

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        return {

            "total_reports":
                len(
                    self._reports
                ),

            "generated_at":
                self._now(),

            "status":
                "ACTIVE",
        }

    # ========================================================
    # EXPORTACIÓN
    # ========================================================

    def export_report(
        self,
        report_id: str,
    ) -> Optional[Dict]:

        report = self.get_report(
            report_id
        )

        if not report:
            return None

        return {

            "report_id":
                report["report_id"],

            "exported_at":
                self._now(),

            "status":
                "EXPORTED",

            "data":
                report,
        }

    # ========================================================
    # REPORTE GENERAL
    # ========================================================

    def generate_global_report(
        self,
    ) -> Dict:

        return {

            "report_type":
                "EXECUTIVE_REPORT_ENGINE",

            "reports":
                self.get_reports(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),
        }


# ============================================================
# FIN
# executive_report_engine.py
# ============================================================
