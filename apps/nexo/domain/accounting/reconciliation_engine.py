class ReconciliationEngine:

    def reconcile(
        self,
        internal_records: list,
        bank_records: list,
    ) -> dict:

        matches = []

        for item in internal_records:
            if item in bank_records:
                matches.append(item)

        return {
            "matched": len(matches),
            "internal": len(internal_records),
            "bank": len(bank_records),
        }
