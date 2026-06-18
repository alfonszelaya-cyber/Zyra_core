from apps.nexo.domain.security.security_audit_engine import (
    SecurityAuditEngine,
)


class GenerateSecurityAuditUseCase:

    def __init__(
        self,
        security_audit_engine:
        SecurityAuditEngine,
    ):
        self._security_audit_engine = (
            security_audit_engine
        )

    def execute(
        self,
        audit_scope: dict,
    ) -> dict:

        report = (
            self._security_audit_engine.generate(
                audit_scope
            )
        )

        return {
            "report": report,
            "status": "GENERATED",
            "audit_type": "SECURITY",
        }
