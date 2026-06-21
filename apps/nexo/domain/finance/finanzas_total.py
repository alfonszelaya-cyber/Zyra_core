# ============================================================
# finanzas_total.py
# NEXO / ZYRA
# FINANCIAL MASTER AGGREGATOR
# PRODUCCIÓN
# ============================================================

from datetime import datetime
from uuid import uuid4
from decimal import Decimal
from typing import Dict

from apps.nexo.domain.accounting.accounting_engine import AccountingEngine
from apps.nexo.domain.finance.declaration_engine import DeclarationEngine
from apps.nexo.domain.finance.document_fiscal_engine import FiscalDocumentEngine


class FinanzasTotal:

    """
    Agregador financiero supremo.

    Responsabilidades:

    - Consolidar contabilidad
    - Consolidar declaraciones
    - Consolidar documentos fiscales
    - Consolidar métricas financieras
    - Alimentar Dashboard Ejecutivo
    - Alimentar KPIs
    - Alimentar ZYRA
    """

    def __init__(self):

        self.accounting_engine = (
            AccountingEngine()
        )

        self.declaration_engine = (
            DeclarationEngine()
        )

        self.document_engine = (
            FiscalDocumentEngine()
        )

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _report_id(self):

        return f"FIN-{uuid4()}"

    # ========================================================
    # REPORTE MAESTRO
    # ========================================================

    def generar_reporte_maestro(
        self,
    ) -> Dict:

        entries = (
            self.accounting_engine
            .get_entries()
        )

        ingresos = Decimal("0")
        egresos = Decimal("0")

        for entry in entries:

            amount = Decimal(
                str(
                    entry.get(
                        "amount",
                        0
                    )
                )
            )

            if (
                entry.get(
                    "entry_type"
                )
                == "CREDIT"
            ):
                ingresos += amount

            else:
                egresos += amount

        declaraciones = (
            self.declaration_engine
            .get_all_declarations()
        )

        documentos = (
            self.document_engine
            .get_all_documents()
        )

        impuestos = Decimal("0")

        ganancia_neta = (
            ingresos
            - egresos
            - impuestos
        )

        return {

            "report_id":
                self._report_id(),

            "generated_at":
                self._now(),

            "report_type":
                "FINANZAS_TOTAL",

            "metricas": {

                "ingresos":
                    float(
                        ingresos
                    ),

                "egresos":
                    float(
                        egresos
                    ),

                "impuestos":
                    float(
                        impuestos
                    ),

                "ganancia_neta":
                    float(
                        ganancia_neta
                    ),
            },

            "declaraciones":
                len(
                    declaraciones
                ),

            "documentos_fiscales":
                len(
                    documentos
                ),

            "asientos_contables":
                len(
                    entries
                ),

            "status":
                "GENERATED",
        }

    # ========================================================
    # DASHBOARD
    # ========================================================

    def dashboard_snapshot(
        self,
    ) -> Dict:

        return (
            self.generar_reporte_maestro()
        )

    # ========================================================
    # RESUMEN
    # ========================================================

    def get_summary(
        self,
    ) -> Dict:

        report = (
            self.generar_reporte_maestro()
        )

        return {

            "report_id":
                report["report_id"],

            "ganancia_neta":
                report["metricas"][
                    "ganancia_neta"
                ],

            "declaraciones":
                report[
                    "declaraciones"
                ],

            "documentos":
                report[
                    "documentos_fiscales"
                ],

            "generated_at":
                report[
                    "generated_at"
                ],
        }


# ============================================================
# INSTANCIA GLOBAL
# ============================================================

finanzas_total = (
    FinanzasTotal()
)

# ============================================================
# COMPATIBILIDAD LEGACY
# ============================================================

def generar_reporte_maestro():

    return (
        finanzas_total
        .generar_reporte_maestro()
    )

# ============================================================
# FIN
# ============================================================
