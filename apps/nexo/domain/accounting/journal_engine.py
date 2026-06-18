# ============================================================
# journal_engine.py
# NEXO / ZYRA
# Accounting Journal Engine
# ============================================================

from datetime import datetime
from typing import Dict, List, Optional
import uuid


class JournalEngine:
    """
    Libro Diario Contable.

    Responsabilidades:
    - Registrar movimientos
    - Mantener libro diario
    - Consultar movimientos
    - Historial de eventos
    - Reportes operativos
    """

    def __init__(self):

        self._journal_entries: List[dict] = []
        self._journal_events: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self) -> str:

        return datetime.utcnow().isoformat()

    def _generate_journal_id(self) -> str:

        return f"JRN-{uuid.uuid4()}"

    def _register_event(
        self,
        event_type: str,
        payload: dict,
    ) -> None:

        self._journal_events.append(
            {
                "event_id":
                    str(uuid.uuid4()),
                "event_type":
                    event_type,
                "timestamp":
                    self._now(),
                "payload":
                    payload,
            }
        )

    # ========================================================
    # REGISTRO
    # ========================================================

    def register_entry(
        self,
        accounting_entry: dict,
    ) -> dict:

        journal_record = {
            "journal_id":
                self._generate_journal_id(),
            "entry":
                accounting_entry,
            "registered_at":
                self._now(),
            "status":
                "POSTED",
        }

        self._journal_entries.append(
            journal_record
        )

        self._register_event(
            "JOURNAL_ENTRY_REGISTERED",
            journal_record,
        )

        return journal_record

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_entries(
        self,
    ) -> List[dict]:

        return list(
            self._journal_entries
        )

    def get_entry(
        self,
        journal_id: str,
    ) -> Optional[dict]:

        for item in self._journal_entries:

            if (
                item["journal_id"]
                == journal_id
            ):
                return item

        return None

    def get_entries_by_account(
        self,
        account_code: str,
    ) -> List[dict]:

        results = []

        for item in self._journal_entries:

            entry = item.get(
                "entry",
                {},
            )

            if (
                entry.get(
                    "account_code"
                )
                == account_code
            ):
                results.append(
                    item
                )

        return results

    def get_entries_by_reference(
        self,
        reference_id: str,
    ) -> List[dict]:

        results = []

        for item in self._journal_entries:

            entry = item.get(
                "entry",
                {},
            )

            if (
                entry.get(
                    "reference_id"
                )
                == reference_id
            ):
                results.append(
                    item
                )

        return results

    # ========================================================
    # EVENTOS
    # ========================================================

    def get_events(
        self,
    ) -> List[dict]:

        return list(
            self._journal_events
        )

    # ========================================================
    # REPORTES
    # ========================================================

    def generate_journal_report(
        self,
    ) -> Dict:

        debit_count = 0
        credit_count = 0

        for item in self._journal_entries:

            entry = item.get(
                "entry",
                {},
            )

            if (
                entry.get(
                    "entry_type"
                )
                == "DEBIT"
            ):
                debit_count += 1

            elif (
                entry.get(
                    "entry_type"
                )
                == "CREDIT"
            ):
                credit_count += 1

        return {
            "journal_entries":
                len(
                    self._journal_entries
                ),
            "debit_entries":
                debit_count,
            "credit_entries":
                credit_count,
            "journal_events":
                len(
                    self._journal_events
                ),
            "generated_at":
                self._now(),
        }

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_metrics(
        self,
    ) -> Dict:

        return {
            "entries":
                len(
                    self._journal_entries
                ),
            "events":
                len(
                    self._journal_events
                ),
            "generated_at":
                self._now(),
        }
