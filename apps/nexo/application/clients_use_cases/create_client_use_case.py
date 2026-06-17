from uuid import uuid4
from datetime import datetime

from apps.nexo.domain.clients.client_registry import ClientRegistry
from foundation.audit_core.audit_logger import AuditLogger


class CreateClientUseCase:

    def __init__(
        self,
        client_registry: ClientRegistry,
        audit_logger: AuditLogger,
    ):
        self._client_registry = client_registry
        self._audit_logger = audit_logger

    def execute(
        self,
        name: str,
        email: str,
        phone: str,
        created_by: str,
    ) -> dict:

        client = {
            "client_id": str(uuid4()),
            "name": name,
            "email": email,
            "phone": phone,
            "status": "ACTIVE",
            "created_at": datetime.utcnow().isoformat(),
        }

        self._client_registry.store(client)

        self._audit_logger.log(
            event_type="CLIENT_CREATED",
            entity_id=client["client_id"],
            actor=created_by,
            payload=client,
        )

        return client
