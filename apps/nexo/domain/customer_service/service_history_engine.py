# ============================================================
# service_history_engine.py
# NEXO / ZYRA
# Service History Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class ServiceHistoryEngine:

    """
    Motor de historial de servicio.

    Responsabilidades:
    - Registrar eventos de soporte
    - Registrar cambios de estado
    - Mantener trazabilidad completa
    - Consultar historial
    - Generar métricas
    - Generar reportes
    """

    def __init__(self):

        self._events = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _event_id(self):

        return f"SVH-{uuid4()}"

    # ========================================================
    # REGISTRO
    # ========================================================

    def register_event(
        self,
        ticket_id: str,
        event_type: str,
        details: Dict,
    ) -> Dict:

        event = {

            "event_id":
                self._event_id(),

            "ticket_id":
                ticket_id,

            "event_type":
                event_type,

            "details":
                details,

            "created_at":
                self._now(),
        }

        self._events.append(
            event
        )

        return event

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_events(
        self,
    ) -> List[Dict]:

        return list(
            self._events
        )

    def get_ticket_history(
        self,
        ticket_id: str,
    ) -> List[Dict]:

        return [

            event

            for event in self._events

            if (
                event["ticket_id"]
                == ticket_id
            )

        ]

    def get_event(
        self,
        event_id: str,
    ) -> Optional[Dict]:

        for event in self._events:

            if (
                event["event_id"]
                == event_id
            ):
                return event

        return None

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        return {

            "events":
                len(
                    self._events
                ),

            "generated_at":
                self._now(),
        }

    # ========================================================
    # REPORTE
    # ========================================================

    def generate_report(
        self,
    ) -> Dict:

        return {

            "events":
                self.get_events(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),

            "report_type":
                "SERVICE_HISTORY",
        }


# ============================================================
# FIN
# service_history_engine.py
# ============================================================
