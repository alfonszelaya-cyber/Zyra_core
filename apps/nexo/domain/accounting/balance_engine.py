class BalanceEngine:

    def generate_balance(
        self,
        assets: float,
        liabilities: float,
        equity: float,
    ) -> dict:

        return {
            "assets": assets,
            "liabilities": liabilities,
            "equity": equity,
            "balanced": (
                assets == liabilities + equity
            ),
        }
