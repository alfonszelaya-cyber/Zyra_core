============================================================

client_validation_engine.py

NEXO / ZYRA

Client Validation Domain Engine

============================================================

import re
from datetime import datetime
from typing import Dict, List

class ClientValidationEngine:

"""
Motor de validación de clientes.

Responsabilidades:
- Validar datos mínimos
- Validar email
- Validar documento
- Validar estados
- Validar tipo de cliente
- Generar observaciones
"""

def __init__(self):

    self._audit_log = []

# ========================================================
# UTILIDADES
# ========================================================

def _now(self):

    return datetime.utcnow().isoformat()

def _audit(
    self,
    action: str,
    data: dict,
):

    self._audit_log.append(
        {
            "action": action,
            "timestamp": self._now(),
            "data": data,
        }
    )

# ========================================================
# VALIDACIONES BÁSICAS
# ========================================================

def validate_required_fields(
    self,
    client_data: Dict,
) -> bool:

    required_fields = [

        "name",

        "document",

        "email",

    ]

    return all(

        field in client_data

        and client_data[field]

        for field in required_fields
    )

def validate_email(
    self,
    email: str,
) -> bool:

    pattern = r"^[^@]+@[^@]+\.[^@]+$"

    return bool(
        re.match(
            pattern,
            email,
        )
    )

def validate_document(
    self,
    document: str,
) -> bool:

    return len(
        str(document).strip()
    ) >= 4

# ========================================================
# VALIDACIÓN GENERAL
# ========================================================

def validate(
    self,
    client_data: Dict,
) -> bool:

    result = (

        self.validate_required_fields(
            client_data
        )

        and

        self.validate_email(
            client_data.get(
                "email",
                "",
            )
        )

        and

        self.validate_document(
            client_data.get(
                "document",
                "",
            )
        )
    )

    self._audit(
        "CLIENT_VALIDATION",
        {
            "client":
                client_data.get(
                    "document",
                    "N/A",
                ),
            "result":
                result,
        },
    )

    return result

# ========================================================
# OBSERVACIONES
# ========================================================

def validation_report(
    self,
    client_data: Dict,
) -> List[str]:

    issues = []

    if not client_data.get("name"):
        issues.append(
            "Missing name"
        )

    if not self.validate_document(
        client_data.get(
            "document",
            "",
        )
    ):
        issues.append(
            "Invalid document"
        )

    if not self.validate_email(
        client_data.get(
            "email",
            "",
        )
    ):
        issues.append(
            "Invalid email"
        )

    return issues

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

def summary(
    self,
):

    return {

        "audit_events":
            len(
                self._audit_log
            ),

        "generated_at":
            self._now(),
    }

============================================================

FIN

============================================================
