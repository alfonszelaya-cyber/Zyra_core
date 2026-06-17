from apps.nexo.domain.accounting.balance_engine import (
    BalanceEngine,
)


class GenerateBalanceUseCase:

    def __init__(
        self,
        balance_engine: BalanceEngine,
    ):
        self._balance_engine = balance_engine

    def execute(
        self,
        company_id: str,
        period_id: str,
    ) -> dict:

        return self._balance_engine.generate_balance(
            company_id=company_id,
            period_id=period_id,
        )
