# ============================================================
# accounting_validation_engine.py
# NEXO / ZYRA
# Accounting Validation Engine
# ============================================================

from datetime import datetime
from typing import Dict, List
import uuid


class AccountingValidationEngine:
    """
    Motor de validación contable.

    Responsabilidades:
    - Validar asientos
    - Validar montos
    - Validar cuentas
    - Detectar inconsistencias
    - Mantener historial de validaciones
    """

    def __init__(self):

        self._validation_history: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self) -> str:

        return datetime.utcnow().isoformat()

    def _register_validation(
        self,
        validation_type: str,
        result: bool,
        details: dict,
    ) -> None:

        self._validation_history.append(
            {
                "validation_id":
                    str(uuid.uuid4()),
                "validation_type":
                    validation_type,
                "result":
                    result,
                "details":
                    details,
                "timestamp":
                    self._now(),
            }
        )

    # ========================================================
    # VALIDACIONES
    # ========================================================

    def validate_account_code(
        self,
        account_code: str,
    ) -> bool:

        result = bool(
            account_code
            and len(account_code) >= 3
        )

        self._register_validation(
            "ACCOUNT_CODE",
            result,
            {
                "account_code":
                    account_code,
            },
        )

        return result

    def validate_amount(
        self,
        amount: float,
    ) -> bool:

        result = (
            isinstance(
                amount,
                (int, float),
            )
            and amount > 0
        )

        self._register_validation(
            "AMOUNT",
            result,
            {
                "amount":
                    amount,
            },
        )

        return result

    def validate_entry_type(
        self,
        entry_type: str,
    ) -> bool:

        result = (
            entry_type
            in [
                "DEBIT",
                "CREDIT",
            ]
        )

        self._register_validation(
            "ENTRY_TYPE",
            result,
            {
                "entry_type":
                    entry_type,
            },
        )

        return result

    def validate_entry(
        self,
        entry: dict,
    ) -> Dict:

        errors = []

        if not self.validate_account_code(
            entry.get(
                "account_code",
                "",
            )
        ):
            errors.append(
                "INVALID_ACCOUNT_CODE"
            )

        if not self.validate_amount(
            entry.get(
                "amount",
                0,
            )
        ):
            errors.append(
                "INVALID_AMOUNT"
            )

        if not self.validate_entry_type(
            entry.get(
                "entry_type",
                "",
            )
        ):
            errors.append(
                "INVALID_ENTRY_TYPE"
            )

        result = {
            "valid":
                len(errors) == 0,
            "errors":
                errors,
            "validated_at":
                self._now(),
        }

        self._register_validation(
            "ACCOUNTING_ENTRY",
            result["valid"],
            result,
        )

        return result

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_validation_history(
        self,
    ) -> List[dict]:

        return list(
            self._validation_history
        )

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_validation_metrics(
        self,
    ) -> Dict:

        success = 0
        failed = 0

        for item in self._validation_history:

            if item["result"]:
                success += 1
            else:
                failed += 1

        return {
            "total_validations":
                len(
                    self._validation_history
                ),
            "successful":
                success,
            "failed":
                failed,
            "generated_at":
                self._now(),
        }
