# ============================================================
# Zyra_finance_master.py
# NEXO / ZYRA
# FINANCE MASTER ORCHESTRATOR
# PRODUCCIÓN
# ============================================================

from datetime import datetime
from decimal import Decimal
from typing import Dict
import uuid

# ============================================================
# DOMINIOS NEXO
# ============================================================

from apps.nexo.domain.accounting.accounting_engine import AccountingEngine
from apps.nexo.domain.accounting.balance_engine import BalanceEngine
from apps.nexo.domain.accounting.journal_engine import JournalEngine
from apps.nexo.domain.accounting.reconciliation_engine import ReconciliationEngine

# ============================================================
# FINANCE MASTER
# ============================================================

class ZyraFinanceMaster:

    """
    Motor Financiero Maestro.

    Responsabilidades:

    - Consolidar Contabilidad
    - Consolidar Balance
    - Consolidar Journal
    - Consolidar Reconciliación
    - Generar Reporte Maestro
    - Alimentar Dashboard Ejecutivo
    - Alimentar KPIs
    - Alimentar ZYRA
    """

    def __init__(self):

        self.accounting_engine = AccountingEngine()

        self.balance_engine = BalanceEngine()

        self.journal_engine = JournalEngine()

        self.reconciliation_engine = (
            ReconciliationEngine()
        )

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _report_id(self):

        return f"FIN-{uuid.uuid4()}"

    # ========================================================
    # CONSOLIDACIÓN
    # ========================================================

    def _calculate_totals(self):

        entries = (
            self.accounting_engine
            .get_entries()
        )

        revenue = Decimal("0")

        expenses = Decimal("0")

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
                revenue += amount

            else:
                expenses += amount

        taxes = Decimal("0")

        profit = (
            revenue
            - expenses
            - taxes
        )

        return {

            "revenue":
                float(revenue),

            "expenses":
                float(expenses),

            "taxes":
                float(taxes),

            "profit":
                float(profit),
        }

    # ========================================================
    # REPORTE MAESTRO
    # ========================================================

    def generar_reporte_maestro(
        self,
    ) -> Dict:

        totals = (
            self._calculate_totals()
        )

        report = {

            "report_id":
                self._report_id(),

            "generated_at":
                self._now(),

            "report_type":
                "MASTER_FINANCIAL",

            "revenue":
                totals["revenue"],

            "expenses":
                totals["expenses"],

            "taxes":
                totals["taxes"],

            "profit":
                totals["profit"],

            "total_entries":
                len(
                    self.accounting_engine
                    .get_entries()
                ),

            "audit_events":
                len(
                    self.accounting_engine
                    .get_audit_log()
                ),

            "status":
                "GENERATED",
        }

        return report

    # ========================================================
    # DASHBOARD
    # ========================================================

    def dashboard_snapshot(
        self,
    ) -> Dict:

        report = (
            self.generar_reporte_maestro()
        )

        return {

            "generated_at":
                self._now(),

            "revenue":
                report["revenue"],

            "expenses":
                report["expenses"],

            "taxes":
                report["taxes"],

            "profit":
                report["profit"],

            "status":
                "ACTIVE",
        }

    # ========================================================
    # RESUMEN
    # ========================================================

    def summary(
        self,
    ) -> Dict:

        report = (
            self.generar_reporte_maestro()
        )

        return {

            "report_id":
                report["report_id"],

            "profit":
                report["profit"],

            "entries":
                report["total_entries"],

            "generated_at":
                report["generated_at"],
        }


# ============================================================
# INSTANCIA GLOBAL
# ============================================================

finance_master = ZyraFinanceMaster()

# ============================================================
# COMPATIBILIDAD LEGACY
# ============================================================

def generar_reporte_maestro():

    return (
        finance_master
        .generar_reporte_maestro()
    )
