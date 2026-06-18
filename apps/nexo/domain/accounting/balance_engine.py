# ============================================================
# balance_engine.py
# NEXO / ZYRA
# Accounting Balance Engine
# ============================================================

from datetime import datetime
from typing import Dict, List
import uuid


class BalanceEngine:
    """
    Motor de balances contables.

    Responsabilidades:
    - Consolidar débitos
    - Consolidar créditos
    - Calcular balances
    - Mantener histórico
    - Generar reportes financieros
    """

    def __init__(self):

        self._balances: List[dict] = []
        self._balance_history: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self) -> str:

        return datetime.utcnow().isoformat()

    def _generate_balance_id(self) -> str:

        return f"BAL-{uuid.uuid4()}"

    def _register_history(
        self,
        action: str,
        payload: dict,
    ) -> None:

        self._balance_history.append(
            {
                "history_id":
                    str(uuid.uuid4()),
                "action":
                    action,
                "timestamp":
                    self._now(),
                "payload":
                    payload,
            }
        )

    # ========================================================
    # BALANCE
    # ========================================================

    def calculate_balance(
        self,
        entries: List[dict],
    ) -> dict:

        total_debits = 0.0
        total_credits = 0.0

        for entry in entries:

            entry_type = entry.get(
                "entry_type",
                "",
            )

            amount = float(
                entry.get(
                    "amount",
                    0,
                )
            )

            if entry_type == "DEBIT":

                total_debits += amount

            elif entry_type == "CREDIT":

                total_credits += amount

        balance_record = {
            "balance_id":
                self._generate_balance_id(),
            "total_debits":
                round(
                    total_debits,
                    2,
                ),
            "total_credits":
                round(
                    total_credits,
                    2,
                ),
            "net_balance":
                round(
                    total_debits
                    - total_credits,
                    2,
                ),
            "generated_at":
                self._now(),
            "status":
                "CALCULATED",
        }

        self._balances.append(
            balance_record
        )

        self._register_history(
            "BALANCE_CALCULATED",
            balance_record,
        )

        return balance_record

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_balances(
        self,
    ) -> List[dict]:

        return list(
            self._balances
        )

    def get_last_balance(
        self,
    ) -> dict | None:

        if not self._balances:
            return None

        return self._balances[-1]

    # ========================================================
    # HISTÓRICO
    # ========================================================

    def get_history(
        self,
    ) -> List[dict]:

        return list(
            self._balance_history
        )

    # ========================================================
    # REPORTES
    # ========================================================

    def generate_balance_report(
        self,
    ) -> Dict:

        latest = self.get_last_balance()

        return {
            "balances_generated":
                len(
                    self._balances
                ),
            "latest_balance":
                latest,
            "history_events":
                len(
                    self._balance_history
                ),
            "generated_at":
                self._now(),
        }

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_metrics(
        self,
    ) -> Dict:

        return {
            "total_balances":
                len(
                    self._balances
                ),
            "history_events":
                len(
                    self._balance_history
                ),
            "generated_at":
                self._now(),
        }
