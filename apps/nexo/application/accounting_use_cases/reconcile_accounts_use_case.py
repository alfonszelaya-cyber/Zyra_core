from apps.nexo.domain.accounting.reconciliation_engine import (
    ReconciliationEngine,
)


class ReconcileAccountsUseCase:

    def __init__(
        self,
        reconciliation_engine: ReconciliationEngine,
    ):
        self._reconciliation_engine = reconciliation_engine

    def execute(
        self,
        company_id: str,
        period_id: str,
    ) -> dict:

        return self._reconciliation_engine.reconcile(
            company_id=company_id,
            period_id=period_id,
        )
