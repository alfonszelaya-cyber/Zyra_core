from apps.nexo.domain.government.government_audit_engine import (
    GovernmentAuditEngine,
)


class AuditGovernmentProcessUseCase:

    def __init__(
        self,
        audit_engine: GovernmentAuditEngine,
    ):
        self._audit_engine = audit_engine

    def execute(
        self,
        process_id: str,
    ) -> dict:

        audit_result = (
            self._audit_engine.audit_process(
                process_id
            )
        )

        return {
            "process_id": process_id,
            "audit_result": audit_result,
            "status": "AUDITED",
        }
