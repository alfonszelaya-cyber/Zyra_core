class AccountingValidationEngine:

    def validate_entry(
        self,
        amount: float,
    ) -> bool:

        return amount > 0

    def validate_balance(
        self,
        assets: float,
        liabilities: float,
        equity: float,
    ) -> bool:

        return (
            assets ==
            liabilities + equity
        )
