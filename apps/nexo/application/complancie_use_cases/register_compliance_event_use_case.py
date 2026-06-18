from datetime import datetime
from uuid import uuid4

from apps.nexo.domain.compliance.compliance_registry import (
    ComplianceRegistry,
)
from foundation.audit_core.audit_logger import AuditLogger


class RegisterComplianceEventUseCase:

    def __init__(
        self,
        compliance_registry: ComplianceRegistry,
        audit_logger: AuditLogger,
    ):
        self._compliance_registry = compliance_registry
        self._audit_logger = audit_logger

    def execute(
        self,
        company_id: str,
        event_type: str,
        description: str,
        created_by: str,
    ) -> dict:

        event = {
            "event_id": str(uuid4()),
            "company_id": company_id,
            "event_type": event_type,
            "description": description,
            "created_at": datetime.utcnow().isoformat(),
        }

        self._compliance_registry.store(event)

        self._audit_logger.log(
            event_type="COMPLIANCE_EVENT_REGISTERED",
            entity_id=event["event_id"],
            actor=created_by,
            payload=event,
        )

        return event
