from apps.nexo.domain.clients.client_registry import ClientRegistry
from foundation.audit_core.audit_logger import AuditLogger


class LinkClientCompanyUseCase:

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
        company_id: str,
        linked_by: str,
    ) -> dict:

        result = self._client_registry.link_company(
            client_id=client_id,
            company_id=company_id,
        )

        self._audit_logger.log(
            event_type="CLIENT_COMPANY_LINKED",
            entity_id=client_id,
            actor=linked_by,
            payload={
                "company_id": company_id,
            },
        )

        return result
