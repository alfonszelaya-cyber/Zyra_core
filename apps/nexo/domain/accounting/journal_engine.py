from datetime import datetime


class JournalEngine:

    def create_journal_entry(
        self,
        debit_account: str,
        credit_account: str,
        amount: float,
    ) -> dict:

        return {
            "debit_account": debit_account,
            "credit_account": credit_account,
            "amount": amount,
            "date": datetime.utcnow(),
        }
