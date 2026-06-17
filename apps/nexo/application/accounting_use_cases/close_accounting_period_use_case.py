from datetime import datetime

from apps.nexo.domain.accounting.accounting_registry import (
    AccountingRegistry,
)
from foundation.audit_core.audit_logger import AuditLogger


class CloseAccountingPeriodUseCase:

    def __init__(
        self,
        accounting_registry: AccountingRegistry,
        audit_logger: AuditLogger,
    ):
        self._accounting_registry = accounting_registry
        self._audit_logger = audit_logger

    def execute(
        self,
        company_id: str,
        period_id: str,
        closed_by: str,
    ) -> dict:

        result = self._accounting_registry.close_period(
            company_id=company_id,
            period_id=period_id,
        )

        self._audit_logger.log(
            event_type="ACCOUNTING_PERIOD_CLOSED",
            entity_id=period_id,
            actor=closed_by,
            payload={
                "company_id": company_id,
                "closed_at": datetime.utcnow().isoformat(),
            },
        )

        return {
            "company_id": company_id,
            "period_id": period_id,
            "status": "CLOSED",
            "result": result,
        }
