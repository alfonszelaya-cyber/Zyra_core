
# ============================================================
# accounting_engine.py
# NEXO / ZYRA
# Accounting Domain Engine
# ============================================================

from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional
import uuid


class AccountingEngine:
    """
    Motor central contable.

    Responsabilidades:
    - Crear asientos
    - Validar estructura básica
    - Mantener auditoría
    - Exponer consultas
    - Preparar información para Journal,
      Balance y Reconciliation
    """

    def __init__(self):

        self._entries: List[dict] = []
        self._audit_log: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self) -> str:
        return datetime.utcnow().isoformat()

    def _generate_id(self) -> str:
        return f"ACC-{uuid.uuid4()}"

    def _audit(
        self,
        action: str,
        data: dict,
    ) -> None:

        self._audit_log.append(
            {
                "event_id": str(uuid.uuid4()),
                "action": action,
                "timestamp": self._now(),
                "data": data,
            }
        )

    # ========================================================
    # VALIDACIONES
    # ========================================================

    def validate_entry(
        self,
        account_code: str,
        amount: float,
        entry_type: str,
    ) -> bool:

        if not account_code:
            return False

        if amount <= 0:
            return False

        if entry_type not in (
            "DEBIT",
            "CREDIT",
        ):
            return False

        return True

    # ========================================================
    # CREACIÓN
    # ========================================================

    def create_entry(
        self,
        account_code: str,
        amount: float,
        entry_type: str,
        description: str,
        reference_id: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> dict:

        if not self.validate_entry(
            account_code,
            amount,
            entry_type,
        ):
            raise ValueError(
                "Invalid accounting entry"
            )

        entry = {
            "entry_id": self._generate_id(),
            "account_code": account_code,
            "amount": float(
                Decimal(str(amount))
            ),
            "entry_type": entry_type,
            "description": description,
            "reference_id": reference_id,
            "metadata": metadata or {},
            "status": "POSTED",
            "created_at": self._now(),
        }

        self._entries.append(entry)

        self._audit(
            "ACCOUNTING_ENTRY_CREATED",
            entry,
        )

        return entry

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_entry(
        self,
        entry_id: str,
    ) -> Optional[dict]:

        for entry in self._entries:

            if (
                entry["entry_id"]
                == entry_id
            ):
                return entry

        return None

    def get_entries(self) -> List[dict]:

        return list(self._entries)

    def get_entries_by_account(
        self,
        account_code: str,
    ) -> List[dict]:

        return [
            e
            for e in self._entries
            if e["account_code"]
            == account_code
        ]

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def calculate_account_balance(
        self,
        account_code: str,
    ) -> float:

        total = 0.0

        for entry in self.get_entries_by_account(
            account_code
        ):

            if (
                entry["entry_type"]
                == "DEBIT"
            ):
                total += entry["amount"]

            elif (
                entry["entry_type"]
                == "CREDIT"
            ):
                total -= entry["amount"]

        return round(total, 2)

    # ========================================================
    # AUDITORÍA
    # ========================================================

    def get_audit_log(
        self,
    ) -> List[dict]:

        return list(self._audit_log)

    # ========================================================
    # REPORTE
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        debits = 0.0
        credits = 0.0

        for entry in self._entries:

            if (
                entry["entry_type"]
                == "DEBIT"
            ):
                debits += entry["amount"]

            else:
                credits += entry["amount"]

        return {
            "entries": len(
                self._entries
            ),
            "debits": round(
                debits,
                2,
            ),
            "credits": round(
                credits,
                2,
            ),
            "audit_events": len(
                self._audit_log
            ),
            "generated_at": self._now(),
        }
