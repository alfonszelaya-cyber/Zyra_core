from apps.nexo.domain.compliance.audit_compliance_engine import (
    AuditComplianceEngine,
)


class AuditComplianceUseCase:

    def __init__(
        self,
        audit_engine: AuditComplianceEngine,
    ):
        self._audit_engine = audit_engine

    def execute(
        self,
        company_id: str,
        period_id: str,
    ) -> dict:

        findings = self._audit_engine.audit(
            company_id=company_id,
            period_id=period_id,
        )

        return {
            "company_id": company_id,
            "period_id": period_id,
            "findings": findings,
            "total_findings": len(findings),
        }
