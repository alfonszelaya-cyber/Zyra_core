# ============================================================
# client_history_engine.py
# NEXO / ZYRA
# Client History Domain Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import List, Optional


class ClientHistoryEngine:

    """
    Motor de historial de clientes.

    Responsabilidades:
    - Registrar eventos
    - Registrar actividad financiera
    - Registrar actividad fiscal
    - Registrar actividad operativa
    - Registrar alertas
    - Registrar auditoría
    - Construir línea de tiempo completa
    """

    def __init__(self):

        self._history = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _event_id(self):

        return f"HIS-{uuid4()}"

    # ========================================================
    # REGISTRO DE EVENTOS
    # ========================================================

    def register_event(
        self,
        client_id: str,
        event_type: str,
        details: dict,
    ) -> dict:

        event = {

            "event_id": self._event_id(),

            "client_id": client_id,

            "event_type": event_type,

            "details": details,

            "created_at": self._now(),
        }

        self._history.append(event)

        return event

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_client_history(
        self,
        client_id: str,
    ) -> List[dict]:

        return [
            item
            for item in self._history
            if item["client_id"] == client_id
        ]

    def get_events_by_type(
        self,
        client_id: str,
        event_type: str,
    ) -> List[dict]:

        return [
            item
            for item in self._history
            if item["client_id"] == client_id
            and item["event_type"] == event_type
        ]

    def get_event(
        self,
        event_id: str,
    ) -> Optional[dict]:

        for item in self._history:

            if item["event_id"] == event_id:
                return item

        return None

    # ========================================================
    # EVENTOS ESPECIALIZADOS NEXO
    # ========================================================

    def register_financial_event(
        self,
        client_id: str,
        details: dict,
    ):

        return self.register_event(
            client_id,
            "FINANCIAL",
            details,
        )

    def register_fiscal_event(
        self,
        client_id: str,
        details: dict,
    ):

        return self.register_event(
            client_id,
            "FISCAL",
            details,
        )

    def register_operational_event(
        self,
        client_id: str,
        details: dict,
    ):

        return self.register_event(
            client_id,
            "OPERATIONAL",
            details,
        )

    def register_risk_event(
        self,
        client_id: str,
        details: dict,
    ):

        return self.register_event(
            client_id,
            "RISK",
            details,
        )

    def register_compliance_event(
        self,
        client_id: str,
        details: dict,
    ):

        return self.register_event(
            client_id,
            "COMPLIANCE",
            details,
        )

    def register_audit_event(
        self,
        client_id: str,
        details: dict,
    ):

        return self.register_event(
            client_id,
            "AUDIT",
            details,
        )

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def get_total_events(
        self,
        client_id: str,
    ) -> int:

        return len(
            self.get_client_history(
                client_id
            )
        )

    # ========================================================
    # TIMELINE
    # ========================================================

    def generate_timeline(
        self,
        client_id: str,
    ) -> List[dict]:

        history = self.get_client_history(
            client_id
        )

        return sorted(
            history,
            key=lambda x: x["created_at"],
            reverse=True,
        )

    # ========================================================
    # RESUMEN
    # ========================================================

    def generate_summary(
        self,
        client_id: str,
    ) -> dict:

        history = self.get_client_history(
            client_id
        )

        return {

            "client_id": client_id,

            "total_events": len(
                history
            ),

            "financial_events": len(
                self.get_events_by_type(
                    client_id,
                    "FINANCIAL",
                )
            ),

            "fiscal_events": len(
                self.get_events_by_type(
                    client_id,
                    "FISCAL",
                )
            ),

            "operational_events": len(
                self.get_events_by_type(
                    client_id,
                    "OPERATIONAL",
                )
            ),

            "risk_events": len(
                self.get_events_by_type(
                    client_id,
                    "RISK",
                )
            ),

            "generated_at": self._now(),
        }
