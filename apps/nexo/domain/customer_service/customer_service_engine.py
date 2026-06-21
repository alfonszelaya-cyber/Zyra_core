# ============================================================
# customer_service_engine.py
# NEXO / ZYRA
# Customer Service Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class CustomerServiceEngine:

    """
    Motor principal de atención al cliente NEXO.

    Responsabilidades:
    - Crear casos de servicio
    - Cerrar casos
    - Actualizar estados
    - Consultar historial
    - Mantener trazabilidad
    - Generar métricas operativas
    """

    def __init__(self):

        self._service_records = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _record_id(self):

        return f"CSR-{uuid4()}"

    # ========================================================
    # CREACIÓN
    # ========================================================

    def create_service_record(
        self,
        client_id: str,
        category: str,
        description: str,
    ) -> Dict:

        record = {

            "service_record_id":
                self._record_id(),

            "client_id":
                client_id,

            "category":
                category,

            "description":
                description,

            "created_at":
                self._now(),

            "updated_at":
                self._now(),

            "status":
                "OPEN",
        }

        self._service_records.append(
            record
        )

        return record

    # ========================================================
    # ACTUALIZACIÓN
    # ========================================================

    def update_service_record(
        self,
        service_record_id: str,
        updates: Dict,
    ) -> Optional[Dict]:

        for record in self._service_records:

            if (
                record["service_record_id"]
                == service_record_id
            ):

                record.update(
                    updates
                )

                record["updated_at"] = (
                    self._now()
                )

                return record

        return None

    # ========================================================
    # CIERRE
    # ========================================================

    def close_service_record(
        self,
        service_record: Dict,
    ) -> Dict:

        service_record["status"] = (
            "CLOSED"
        )

        service_record["closed_at"] = (
            self._now()
        )

        service_record["updated_at"] = (
            self._now()
        )

        return service_record

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_service_records(
        self,
    ) -> List[Dict]:

        return list(
            self._service_records
        )

    def get_record(
        self,
        service_record_id: str,
    ) -> Optional[Dict]:

        for record in self._service_records:

            if (
                record["service_record_id"]
                == service_record_id
            ):
                return record

        return None

    def get_client_records(
        self,
        client_id: str,
    ) -> List[Dict]:

        return [

            record

            for record in self._service_records

            if (
                record["client_id"]
                == client_id
            )

        ]

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        open_cases = len(

            [

                r

                for r in self._service_records

                if (
                    r["status"]
                    == "OPEN"
                )

            ]

        )

        closed_cases = len(

            [

                r

                for r in self._service_records

                if (
                    r["status"]
                    == "CLOSED"
                )

            ]

        )

        return {

            "total_cases":
                len(
                    self._service_records
                ),

            "open_cases":
                open_cases,

            "closed_cases":
                closed_cases,

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

            "service_records":
                self.get_service_records(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),

            "report_type":
                "CUSTOMER_SERVICE",
        }


# ============================================================
# FIN
# customer_service_engine.py
# ============================================================
