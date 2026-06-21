============================================================

accounting_registry.py

NEXO / ZYRA

Accounting Registry Domain

Registro Central de Asientos Contables

============================================================

from datetime import datetime
from typing import Dict, List, Optional
import uuid

class AccountingRegistry:
"""
Registro central contable.

Responsabilidades:

- Registrar asientos
- Consultar asientos
- Buscar por cuenta
- Buscar por referencia
- Buscar por fecha
- Actualizar registros
- Eliminar registros
- Mantener auditoría
"""

def __init__(self):

    self._entries: List[dict] = []
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
# REGISTRO
# ========================================================

def register(
    self,
    entry: dict,
) -> dict:

    self._entries.append(entry)

    self._audit(
        "ACCOUNTING_ENTRY_REGISTERED",
        entry,
    )

    return entry

# ========================================================
# CONSULTAS
# ========================================================

def get_all(
    self,
) -> List[dict]:

    return list(self._entries)

def get_by_id(
    self,
    entry_id: str,
) -> Optional[dict]:

    for entry in self._entries:

        if (
            entry.get("entry_id")
            == entry_id
        ):
            return entry

    return None

def get_by_account(
    self,
    account_code: str,
) -> List[dict]:

    return [
        entry
        for entry in self._entries
        if (
            entry.get("account_code")
            == account_code
        )
    ]

def get_by_reference(
    self,
    reference_id: str,
) -> List[dict]:

    return [
        entry
        for entry in self._entries
        if (
            entry.get("reference_id")
            == reference_id
        )
    ]

def get_by_date(
    self,
    date_value: str,
) -> List[dict]:

    return [
        entry
        for entry in self._entries
        if (
            date_value
            in entry.get(
                "created_at",
                "",
            )
        )
    ]

# ========================================================
# ACTUALIZACIÓN
# ========================================================

def update(
    self,
    entry_id: str,
    updates: Dict,
) -> Optional[dict]:

    entry = self.get_by_id(
        entry_id
    )

    if not entry:
        return None

    entry.update(
        updates
    )

    self._audit(
        "ACCOUNTING_ENTRY_UPDATED",
        {
            "entry_id": entry_id,
            "updates": updates,
        },
    )

    return entry

# ========================================================
# ELIMINACIÓN
# ========================================================

def delete(
    self,
    entry_id: str,
) -> bool:

    for i, entry in enumerate(
        self._entries
    ):

        if (
            entry.get("entry_id")
            == entry_id
        ):

            deleted = self._entries.pop(i)

            self._audit(
                "ACCOUNTING_ENTRY_DELETED",
                deleted,
            )

            return True

    return False

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
# MÉTRICAS
# ========================================================

def total_entries(
    self,
) -> int:

    return len(
        self._entries
    )

def summary(
    self,
) -> Dict:

    return {
        "entries": len(
            self._entries
        ),
        "audit_events": len(
            self._audit_log
        ),
        "generated_at": self._now(),
    }

============================================================

FIN

============================================================
