# ============================================================
# ticket_engine.py
# NEXO / ZYRA
# Ticket Management Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class TicketEngine:

    """
    Motor de tickets.

    Responsabilidades:
    - Crear tickets
    - Asignar tickets
    - Actualizar estados
    - Mantener historial
    - Gestionar prioridades
    - Generar métricas
    """

    def __init__(self):

        self._tickets = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _ticket_id(self):

        return f"TKT-{uuid4()}"

    # ========================================================
    # CREACIÓN
    # ========================================================

    def create_ticket(
        self,
        client_id: str,
        subject: str,
        description: str,
        priority: str = "NORMAL",
    ) -> Dict:

        ticket = {

            "ticket_id":
                self._ticket_id(),

            "client_id":
                client_id,

            "subject":
                subject,

            "description":
                description,

            "priority":
                priority,

            "created_at":
                self._now(),

            "updated_at":
                self._now(),

            "status":
                "OPEN",

            "assigned_to":
                None,
        }

        self._tickets.append(
            ticket
        )

        return ticket

    # ========================================================
    # ASIGNACIÓN
    # ========================================================

    def assign_ticket(
        self,
        ticket: Dict,
        assigned_to: str,
    ) -> Dict:

        ticket["assigned_to"] = (
            assigned_to
        )

        ticket["updated_at"] = (
            self._now()
        )

        return ticket

    # ========================================================
    # ESTADOS
    # ========================================================

    def update_status(
        self,
        ticket_id: str,
        status: str,
    ) -> Optional[Dict]:

        ticket = self.get_ticket(
            ticket_id
        )

        if not ticket:
            return None

        ticket["status"] = status

        ticket["updated_at"] = (
            self._now()
        )

        return ticket

    def close_ticket(
        self,
        ticket_id: str,
    ) -> Optional[Dict]:

        ticket = self.update_status(
            ticket_id,
            "CLOSED",
        )

        if ticket:

            ticket["closed_at"] = (
                self._now()
            )

        return ticket

    # ========================================================
    # PRIORIDAD
    # ========================================================

    def change_priority(
        self,
        ticket_id: str,
        priority: str,
    ) -> Optional[Dict]:

        ticket = self.get_ticket(
            ticket_id
        )

        if not ticket:
            return None

        ticket["priority"] = (
            priority
        )

        ticket["updated_at"] = (
            self._now()
        )

        return ticket

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_ticket(
        self,
        ticket_id: str,
    ) -> Optional[Dict]:

        for ticket in self._tickets:

            if (
                ticket["ticket_id"]
                == ticket_id
            ):
                return ticket

        return None

    def get_tickets(
        self,
    ) -> List[Dict]:

        return list(
            self._tickets
        )

    def get_client_tickets(
        self,
        client_id: str,
    ) -> List[Dict]:

        return [

            ticket

            for ticket in self._tickets

            if (
                ticket["client_id"]
                == client_id
            )

        ]

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        open_tickets = len(

            [

                t

                for t in self._tickets

                if (
                    t["status"]
                    == "OPEN"
                )

            ]

        )

        closed_tickets = len(

            [

                t

                for t in self._tickets

                if (
                    t["status"]
                    == "CLOSED"
                )

            ]

        )

        return {

            "total_tickets":
                len(
                    self._tickets
                ),

            "open_tickets":
                open_tickets,

            "closed_tickets":
                closed_tickets,

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

            "tickets":
                self.get_tickets(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),

            "report_type":
                "TICKET_ENGINE",
        }


# ============================================================
# FIN
# ticket_engine.py
# ============================================================
