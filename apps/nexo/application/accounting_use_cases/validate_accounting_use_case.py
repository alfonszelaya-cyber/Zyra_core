
from apps.nexo.domain.accounting.accounting_validation_engine import (
    AccountingValidationEngine,
)


class ValidateAccountingUseCase:

    def __init__(
        self,
        validation_engine: AccountingValidationEngine,
    ):
        self._validation_engine = validation_engine

    def execute(self, journal_entry: dict) -> bool:

        return self._validation_engine.validate(
            journal_entry=journal_entry
        )
