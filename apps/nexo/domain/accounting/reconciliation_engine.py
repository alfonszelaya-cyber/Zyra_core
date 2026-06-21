============================================================

reconciliation_engine.py

NEXO / ZYRA

Reconciliation Domain Engine

============================================================

from datetime import datetime
from typing import Dict, List
import uuid

class ReconciliationEngine:
"""
Motor de conciliación.

Responsabilidades:

- Conciliar registros internos
- Conciliar movimientos bancarios
- Detectar diferencias
- Detectar faltantes
- Mantener auditoría
"""

def __init__(self):

    self._audit_log: List[dict] = []

# ========================================================
# UTILIDADES
# ========================================================

def _now(self) -> str:

    return datetime.utcnow().isoformat()

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
# CONCILIACIÓN
# ========================================================

def reconcile(
    self,
    internal_records: list,
    bank_records: list,
) -> Dict:

    matched = []
    missing_internal = []
    missing_bank = []

    bank_lookup = {
        str(item)
        for item in bank_records
    }

    internal_lookup = {
        str(item)
        for item in internal_records
    }

    for item in internal_records:

        if str(item) in bank_lookup:
            matched.append(item)

        else:
            missing_bank.append(item)

    for item in bank_records:

        if str(item) not in internal_lookup:
            missing_internal.append(item)

    result = {
        "matched": len(matched),
        "missing_in_bank": len(
            missing_bank
        ),
        "missing_in_internal": len(
            missing_internal
        ),
        "internal_records": len(
            internal_records
        ),
        "bank_records": len(
            bank_records
        ),
        "status": (
            "RECONCILED"
            if (
                len(missing_bank)
                == 0
                and len(missing_internal)
                == 0
            )
            else "DIFFERENCES_FOUND"
        ),
        "generated_at": self._now(),
    }

    self._audit(
        "RECONCILIATION_EXECUTED",
        result,
    )

    return result

# ========================================================
# AUDITORÍA
# ========================================================

def get_audit_log(
    self,
) -> List[dict]:

    return list(
        self._audit_log
    )

# ========================================================
# RESUMEN
# ========================================================

def summary(
    self,
) -> Dict:

    return {
        "audit_events": len(
            self._audit_log
        ),
        "generated_at": self._now(),
    }

============================================================

FIN

============================================================
