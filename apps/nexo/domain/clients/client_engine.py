# ============================================================
# client_engine.py
# NEXO / ZYRA
# Client Domain Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Optional, Dict


class ClientEngine:

    """
    Motor central de clientes NEXO.

    Responsabilidades:
    - Crear clientes
    - Actualizar clientes
    - Gestionar estado
    - Gestionar riesgo
    - Gestionar clasificación
    - Preparar integración con:
        * Finanzas
        * Fiscal
        * Operaciones
        * Identidad
        * Auditoría
        * ZYRA
    """

    def __init__(self):

        self._clients = []
        self._audit_log = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _client_id(self):

        return f"CLI-{uuid4()}"

    def _audit(
        self,
        action: str,
        data: dict,
    ):

        self._audit_log.append(
            {
                "event_id": str(uuid4()),
                "action": action,
                "timestamp": self._now(),
                "data": data,
            }
        )

    # ========================================================
    # CREAR CLIENTE
    # ========================================================

    def create_client(
        self,
        name: str,
        document: str,
        email: str,
        client_type: str = "PERSON",
        country: str = "N/A",
        phone: Optional[str] = None,
    ) -> dict:

        client = {

            "client_id": self._client_id(),

            "name": name,

            "document": document,

            "email": email,

            "phone": phone,

            "country": country,

            "client_type": client_type,

            "status": "ACTIVE",

            "risk_level": "NORMAL",

            "financial_score": 0,

            "fiscal_score": 0,

            "operational_score": 0,

            "zyra_score": 0,

            "created_at": self._now(),

            "updated_at": self._now(),
        }

        self._clients.append(client)

        self._audit(
            "CLIENT_CREATED",
            client,
        )

        return client

    # ========================================================
    # ACTUALIZAR CLIENTE
    # ========================================================

    def update_client(
        self,
        client_id: str,
        updates: Dict,
    ) -> Optional[dict]:

        client = self.get_client(client_id)

        if not client:
            return None

        client.update(updates)

        client["updated_at"] = self._now()

        self._audit(
            "CLIENT_UPDATED",
            {
                "client_id": client_id,
                "updates": updates,
            },
        )

        return client

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_client(
        self,
        client_id: str,
    ) -> Optional[dict]:

        for client in self._clients:

            if client["client_id"] == client_id:
                return client

        return None

    def get_all_clients(self):

        return list(self._clients)

    # ========================================================
    # ESTADOS
    # ========================================================

    def block_client(
        self,
        client_id: str,
    ):

        client = self.get_client(client_id)

        if not client:
            return None

        client["status"] = "BLOCKED"

        self._audit(
            "CLIENT_BLOCKED",
            client,
        )

        return client

    def activate_client(
        self,
        client_id: str,
    ):

        client = self.get_client(client_id)

        if not client:
            return None

        client["status"] = "ACTIVE"

        self._audit(
            "CLIENT_ACTIVATED",
            client,
        )

        return client

    # ========================================================
    # RIESGO
    # ========================================================

    def update_risk_level(
        self,
        client_id: str,
        risk_level: str,
    ):

        client = self.get_client(client_id)

        if not client:
            return None

        client["risk_level"] = risk_level

        self._audit(
            "CLIENT_RISK_UPDATED",
            {
                "client_id": client_id,
                "risk_level": risk_level,
            },
        )

        return client

    # ========================================================
    # AUDITORÍA
    # ========================================================

    def get_audit_log(self):

        return list(self._audit_log)

    # ========================================================
    # RESUMEN
    # ========================================================

    def generate_summary(self):

        active = len(
            [
                c
                for c in self._clients
                if c["status"] == "ACTIVE"
            ]
        )

        blocked = len(
            [
                c
                for c in self._clients
                if c["status"] == "BLOCKED"
            ]
        )

        return {

            "total_clients": len(
                self._clients
            ),

            "active_clients": active,

            "blocked_clients": blocked,

            "audit_events": len(
                self._audit_log
            ),

            "generated_at": self._now(),
        }
