from datetime import datetime
from uuid import uuid4

from apps.nexo.domain.accounting.accounting_registry import AccountingRegistry
from foundation.core_ledger.ledger_engine import LedgerEngine
from foundation.audit_core.audit_logger import AuditLogger


class CreateJournalEntryUseCase:
    """
    Caso de uso responsable de crear asientos contables.
    """

    def __init__(
        self,
        ledger_engine: LedgerEngine,
        accounting_registry: AccountingRegistry,
        audit_logger: AuditLogger,
    ):
        self._ledger_engine = ledger_engine
        self._accounting_registry = accounting_registry
        self._audit_logger = audit_logger

    def execute(
        self,
        company_id: str,
        debit_account: str,
        credit_account: str,
        amount: float,
        description: str,
        created_by: str,
    ) -> dict:

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        entry = {
            "entry_id": str(uuid4()),
            "company_id": company_id,
            "debit_account": debit_account,
            "credit_account": credit_account,
            "amount": amount,
            "description": description,
            "created_by": created_by,
            "created_at": datetime.utcnow().isoformat(),
            "status": "POSTED",
        }

        self._ledger_engine.register_entry(entry)
        self._accounting_registry.store(entry)

        self._audit_logger.log(
            event_type="ACCOUNTING_ENTRY_CREATED",
            entity_id=entry["entry_id"],
            actor=created_by,
            payload=entry,
        )

        return entry
