class ExecutiveKPIEngine:

    def generate_kpis(
        self,
        metrics: dict,
    ) -> dict:

        return {
            "revenue_growth":
                metrics.get("revenue_growth", 0),
            "profit_margin":
                metrics.get("profit_margin", 0),
            "cash_flow":
                metrics.get("cash_flow", 0),
            "customer_growth":
                metrics.get("customer_growth", 0),
        }
