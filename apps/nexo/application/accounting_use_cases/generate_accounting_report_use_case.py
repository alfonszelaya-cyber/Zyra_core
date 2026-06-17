from apps.nexo.domain.accounting.accounting_registry import (
    AccountingRegistry,
)


class GenerateAccountingReportUseCase:

    def __init__(
        self,
        accounting_registry: AccountingRegistry,
    ):
        self._accounting_registry = accounting_registry

    def execute(
        self,
        company_id: str,
        period_id: str,
    ) -> dict:

        entries = self._accounting_registry.get_by_period(
            company_id=company_id,
            period_id=period_id,
        )

        return {
            "company_id": company_id,
            "period_id": period_id,
            "entries": entries,
            "total_entries": len(entries),
        }
