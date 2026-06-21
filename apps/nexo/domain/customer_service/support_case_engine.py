# ============================================================
# support_case_engine.py
# NEXO / ZYRA
# Support Case Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class SupportCaseEngine:

    """
    Motor de casos de soporte.

    Responsabilidades:
    - Crear reportes de casos
    - Mantener historial
    - Consultar casos
    - Gestionar estados
    - Generar métricas
    - Generar reportes ejecutivos
    """

    def __init__(self):

        self._cases = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _case_id(self):

        return f"CAS-{uuid4()}"

    # ========================================================
    # CREACIÓN
    # ========================================================

    def create_case(
        self,
        case_data: Dict,
    ) -> Dict:

        case = {

            "case_id":
                self._case_id(),

            "created_at":
                self._now(),

            "case_data":
                case_data,

            "status":
                "OPEN",
        }

        self._cases.append(
            case
        )

        return case

    # ========================================================
    # REPORTE
    # ========================================================

    def generate_case_report(
        self,
        case_data: Dict,
    ) -> Dict:

        report = {

            "report_id":
                f"REP-{uuid4()}",

            "generated_at":
                self._now(),

            "case_data":
                case_data,

            "report_type":
                "SUPPORT_CASE",

            "status":
                "GENERATED",
        }

        return report

    # ========================================================
    # ESTADOS
    # ========================================================

    def update_status(
        self,
        case_id: str,
        status: str,
    ) -> Optional[Dict]:

        for case in self._cases:

            if (
                case["case_id"]
                == case_id
            ):

                case["status"] = (
                    status
                )

                case["updated_at"] = (
                    self._now()
                )

                return case

        return None

    def close_case(
        self,
        case_id: str,
    ) -> Optional[Dict]:

        return self.update_status(
            case_id,
            "CLOSED",
        )

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_case(
        self,
        case_id: str,
    ) -> Optional[Dict]:

        for case in self._cases:

            if (
                case["case_id"]
                == case_id
            ):
                return case

        return None

    def get_cases(
        self,
    ) -> List[Dict]:

        return list(
            self._cases
        )

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        open_cases = len(

            [

                case

                for case in self._cases

                if (
                    case["status"]
                    == "OPEN"
                )

            ]

        )

        closed_cases = len(

            [

                case

                for case in self._cases

                if (
                    case["status"]
                    == "CLOSED"
                )

            ]

        )

        return {

            "total_cases":
                len(
                    self._cases
                ),

            "open_cases":
                open_cases,

            "closed_cases":
                closed_cases,

            "generated_at":
                self._now(),
        }

    # ========================================================
    # REPORTE EJECUTIVO
    # ========================================================

    def generate_report(
        self,
    ) -> Dict:

        return {

            "cases":
                self.get_cases(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),

            "report_type":
                "SUPPORT_CASE_ENGINE",
        }


# ============================================================
# FIN
# support_case_engine.py
# ============================================================
