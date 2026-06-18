from datetime import datetime


class AccountingEngine:

    def create_entry(
        self,
        account_code: str,
        amount: float,
        entry_type: str,
        description: str,
    ) -> dict:

        return {
            "account_code": account_code,
            "amount": amount,
            "entry_type": entry_type,
            "description": description,
            "created_at": datetime.utcnow(),
            "status": "POSTED",
        }
