from datetime import datetime

from apps.nexo.domain.clients.client_registry import ClientRegistry
from foundation.audit_core.audit_logger import AuditLogger


class UpdateClientUseCase:

    def __init__(
        self,
        client_registry: ClientRegistry,
        audit_logger: AuditLogger,
    ):
        self._client_registry = client_registry
        self._audit_logger = audit_logger

    def execute(
        self,
        client_id: str,
        updates: dict,
        updated_by: str,
    ) -> dict:

        updates["updated_at"] = datetime.utcnow().isoformat()

        client = self._client_registry.update(
            client_id=client_id,
            updates=updates,
        )

        self._audit_logger.log(
            event_type="CLIENT_UPDATED",
            entity_id=client_id,
            actor=updated_by,
            payload=updates,
        )

        return client
