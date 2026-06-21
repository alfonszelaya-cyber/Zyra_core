# ============================================================
# document_fiscal_engine.py
# NEXO / ZYRA
# Fiscal Document Engine
# PRODUCCIÓN
# ============================================================

from datetime import datetime
from uuid import uuid4
from copy import deepcopy
from typing import Dict, List, Optional


class FiscalDocumentEngine:

    def __init__(self):

        self._documents: List[dict] = []

        self._simulations: List[dict] = []

        self._audit_log: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _document_id(self):

        return f"DOC-{uuid4()}"

    def _simulation_id(self):

        return f"SIM-{uuid4()}"

    def _audit(
        self,
        action: str,
        data: dict,
    ):

        self._audit_log.append({

            "event_id":
                str(uuid4()),

            "action":
                action,

            "timestamp":
                self._now(),

            "data":
                data,
        })

    # ========================================================
    # SIMULACIÓN
    # ========================================================

    def simular_documento(
        self,
        document: Dict,
    ) -> Dict:

        simulation = deepcopy(document)

        simulation_record = {

            "simulation_id":
                self._simulation_id(),

            "created_at":
                self._now(),

            "valid":
                True,

            "risk":
                "LOW",

            "observations":
                [],

            "preview":
                simulation,
        }

        total = (
            document
            .get("totales", {})
            .get("total", 0)
        )

        if total <= 0:

            simulation_record["valid"] = False

            simulation_record["risk"] = "HIGH"

            simulation_record[
                "observations"
            ].append(
                "INVALID_TOTAL"
            )

        self._simulations.append(
            simulation_record
        )

        self._audit(
            "DOCUMENT_SIMULATED",
            simulation_record,
        )

        return simulation_record

    # ========================================================
    # EMISIÓN
    # ========================================================

    def generar_documento(
        self,
        document: Dict,
    ) -> Dict:

        record = deepcopy(document)

        fiscal_document = {

            "document_id":
                self._document_id(),

            "created_at":
                self._now(),

            "status":
                "ISSUED",

            "document":
                record,
        }

        self._documents.append(
            fiscal_document
        )

        self._audit(
            "DOCUMENT_ISSUED",
            fiscal_document,
        )

        return fiscal_document

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_all_documents(
        self,
    ) -> List[Dict]:

        return list(
            self._documents
        )

    def get_document(
        self,
        document_id: str,
    ) -> Optional[Dict]:

        for document in self._documents:

            if (
                document["document_id"]
                == document_id
            ):
                return document

        return None

    def documentos_por_pais(
        self,
        pais: str,
    ) -> List[Dict]:

        return [

            document

            for document
            in self._documents

            if (

                document
                .get(
                    "document",
                    {}
                )
                .get(
                    "pais"
                )
                == pais
            )
        ]

    def documentos_por_cliente(
        self,
        cliente_id: str,
    ) -> List[Dict]:

        return [

            document

            for document
            in self._documents

            if (

                document
                .get(
                    "document",
                    {}
                )
                .get(
                    "cliente",
                    {}
                )
                .get(
                    "id"
                )
                == cliente_id
            )
        ]

    # ========================================================
    # AUDITORÍA
    # ========================================================

    def get_audit_log(
        self,
    ):

        return list(
            self._audit_log
        )

    # ========================================================
    # RESUMEN
    # ========================================================

    def get_summary(
        self,
    ):

        return {

            "documents":
                len(
                    self._documents
                ),

            "simulations":
                len(
                    self._simulations
                ),

            "audit_events":
                len(
                    self._audit_log
                ),

            "generated_at":
                self._now(),
        }


# ============================================================
# INSTANCIA GLOBAL
# ============================================================

document_fiscal_engine = (
    FiscalDocumentEngine()
)
