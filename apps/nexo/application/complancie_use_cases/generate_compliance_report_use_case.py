from apps.nexo.domain.compliance.compliance_registry import (
    ComplianceRegistry,
)


class GenerateComplianceReportUseCase:

    def __init__(
        self,
        compliance_registry: ComplianceRegistry,
    ):
        self._compliance_registry = compliance_registry

    def execute(
        self,
        company_id: str,
        period_id: str,
    ) -> dict:

        events = self._compliance_registry.get_by_period(
            company_id=company_id,
            period_id=period_id,
        )

        return {
            "company_id": company_id,
            "period_id": period_id,
            "events": events,
            "total_events": len(events),
        }
