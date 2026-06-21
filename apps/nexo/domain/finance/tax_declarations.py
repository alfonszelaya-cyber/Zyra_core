# ============================================================
# tax_declarations.py
# NEXO / ZYRA
# Tax Declarations Engine
# PRODUCCIÓN
# ============================================================

from datetime import datetime
from uuid import uuid4
from decimal import Decimal
from typing import Dict, List, Optional

from apps.nexo.domain.accounting.accounting_engine import (
    AccountingEngine
)


class TaxDeclarationsEngine:

    """
    Motor Fiscal.

    Responsabilidades:

    - Declaraciones mensuales
    - Declaraciones anuales
    - Acumulados fiscales
    - Utilidades
    - Integración Hacienda
    - Auditoría fiscal
    """

    def __init__(self):

        self.accounting_engine = (
            AccountingEngine()
        )

        self._declarations = []

        self._audit_log = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _declaration_id(self):

        return f"TAX-{uuid4()}"

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
    # ACUMULADOS
    # ========================================================

    def calcular_acumulados(
        self,
        company_id: Optional[str] = None,
    ) -> Dict:

        ingresos = Decimal("0")
        gastos = Decimal("0")

        entries = (
            self.accounting_engine
            .get_entries()
        )

        for entry in entries:

            if (
                company_id
                and
                entry.get(
                    "company_id"
                )
                != company_id
            ):
                continue

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
                gastos += amount

        utilidad = (
            ingresos
            - gastos
        )

        return {

            "ingresos":
                float(
                    ingresos
                ),

            "gastos":
                float(
                    gastos
                ),

            "utilidad":
                float(
                    utilidad
                ),
        }

    # ========================================================
    # DECLARACIÓN MENSUAL
    # ========================================================

    def generar_declaracion_mensual(
        self,
        company_id: str,
        jurisdiction: str,
        month: int,
        year: int,
    ) -> Dict:

        acumulados = (
            self.calcular_acumulados(
                company_id
            )
        )

        declaration = {

            "declaration_id":
                self._declaration_id(),

            "company_id":
                company_id,

            "jurisdiction":
                jurisdiction,

            "month":
                month,

            "year":
                year,

            "acumulados":
                acumulados,

            "status":
                "GENERATED",

            "created_at":
                self._now(),
        }

        self._declarations.append(
            declaration
        )

        self._audit(
            "MONTHLY_DECLARATION",
            declaration,
        )

        return declaration

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_declarations(
        self,
    ) -> List[Dict]:

        return list(
            self._declarations
        )

    def get_declaration(
        self,
        declaration_id: str,
    ) -> Optional[Dict]:

        for declaration in self._declarations:

            if (
                declaration[
                    "declaration_id"
                ]
                == declaration_id
            ):
                return declaration

        return None

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

            "declarations":
                len(
                    self._declarations
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

tax_declarations_engine = (
    TaxDeclarationsEngine()
)

# ============================================================
# FIN
# tax_declarations.py
# ============================================================
