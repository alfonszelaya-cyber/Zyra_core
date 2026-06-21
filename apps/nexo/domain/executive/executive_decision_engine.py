# ============================================================
# executive_decision_engine.py
# NEXO / ZYRA
# Executive Decision Domain Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class ExecutiveDecisionEngine:

    """
    Motor Ejecutivo de Decisiones.

    Responsabilidades:

    - Apoyar decisiones ejecutivas
    - Registrar recomendaciones ZYRA
    - Mantener historial de decisiones
    - Evaluar impacto
    - Gestionar prioridades
    - Generar reportes ejecutivos
    """

    VALID_STATUS = (
        "READY",
        "APPROVED",
        "REJECTED",
        "EXECUTED",
        "CANCELLED",
    )

    def __init__(self):

        self._decisions: List[dict] = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _decision_id(self):

        return f"DEC-{uuid4()}"

    # ========================================================
    # CREAR DECISIÓN
    # ========================================================

    def support_decision(
        self,
        decision_context: dict,
        recommendation: str = "REVIEW_REQUIRED",
        priority: str = "NORMAL",
    ) -> Dict:

        decision = {

            "decision_id":
                self._decision_id(),

            "generated_at":
                self._now(),

            "context":
                decision_context,

            "recommendation":
                recommendation,

            "priority":
                priority,

            "status":
                "READY",
        }

        self._decisions.append(
            decision
        )

        return decision

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_decision(
        self,
        decision_id: str,
    ) -> Optional[Dict]:

        for decision in self._decisions:

            if (
                decision["decision_id"]
                == decision_id
            ):
                return decision

        return None

    def get_decisions(
        self,
    ) -> List[Dict]:

        return list(
            self._decisions
        )

    # ========================================================
    # ESTADOS
    # ========================================================

    def update_status(
        self,
        decision_id: str,
        status: str,
    ) -> Optional[Dict]:

        if status not in (
            self.VALID_STATUS
        ):
            return None

        decision = self.get_decision(
            decision_id
        )

        if not decision:
            return None

        decision["status"] = status

        decision["updated_at"] = (
            self._now()
        )

        return decision

    # ========================================================
    # IMPACTO
    # ========================================================

    def evaluate_impact(
        self,
        decision_id: str,
        financial: str,
        operational: str,
        compliance: str,
    ) -> Optional[Dict]:

        decision = self.get_decision(
            decision_id
        )

        if not decision:
            return None

        decision["impact"] = {

            "financial":
                financial,

            "operational":
                operational,

            "compliance":
                compliance,
        }

        decision["updated_at"] = (
            self._now()
        )

        return decision

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        return {

            "total_decisions":
                len(
                    self._decisions
                ),

            "ready":
                len([
                    d
                    for d in self._decisions
                    if d["status"]
                    == "READY"
                ]),

            "approved":
                len([
                    d
                    for d in self._decisions
                    if d["status"]
                    == "APPROVED"
                ]),

            "executed":
                len([
                    d
                    for d in self._decisions
                    if d["status"]
                    == "EXECUTED"
                ]),

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

            "report_type":
                "EXECUTIVE_DECISIONS",

            "decisions":
                self.get_decisions(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),
        }


# ============================================================
# FIN
# executive_decision_engine.py
# ============================================================
