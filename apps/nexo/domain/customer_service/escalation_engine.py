# ============================================================
# escalation_engine.py
# NEXO / ZYRA
# Escalation Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class EscalationEngine:

    """
    Motor de escalamiento.

    Responsabilidades:
    - Escalar tickets
    - Escalar incidencias
    - Escalar casos críticos
    - Mantener trazabilidad
    - Registrar historial
    - Generar métricas
    """

    def __init__(self):

        self._escalations = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _escalation_id(self):

        return f"ESC-{uuid4()}"

    # ========================================================
    # ESCALAMIENTO
    # ========================================================

    def escalate(
        self,
        ticket_id: str,
        level: int,
        reason: str,
    ) -> Dict:

        escalation = {

            "escalation_id":
                self._escalation_id(),

            "ticket_id":
                ticket_id,

            "level":
                level,

            "reason":
                reason,

            "escalated_at":
                self._now(),

            "status":
                "ESCALATED",
        }

        self._escalations.append(
            escalation
        )

        return escalation

    # ========================================================
    # ACTUALIZACIÓN
    # ========================================================

    def update_status(
        self,
        escalation_id: str,
        status: str,
    ) -> Optional[Dict]:

        for escalation in self._escalations:

            if (
                escalation["escalation_id"]
                == escalation_id
            ):

                escalation["status"] = (
                    status
                )

                escalation["updated_at"] = (
                    self._now()
                )

                return escalation

        return None

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_escalations(
        self,
    ) -> List[Dict]:

        return list(
            self._escalations
        )

    def get_ticket_escalations(
        self,
        ticket_id: str,
    ) -> List[Dict]:

        return [

            escalation

            for escalation in self._escalations

            if (
                escalation["ticket_id"]
                == ticket_id
            )

        ]

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        return {

            "total_escalations":
                len(
                    self._escalations
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

            "escalations":
                self.get_escalations(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),

            "report_type":
                "ESCALATION",
        }


# ============================================================
# FIN
# escalation_engine.py
# ============================================================
