# ============================================================
# customer_feedback_engine.py
# NEXO / ZYRA
# Customer Feedback Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class CustomerFeedbackEngine:

    """
    Motor de retroalimentación del cliente.

    Responsabilidades:
    - Registrar feedback
    - Registrar comentarios
    - Medir satisfacción
    - Mantener historial
    - Generar métricas
    - Generar reportes
    """

    def __init__(self):

        self._feedbacks = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _feedback_id(self):

        return f"FDB-{uuid4()}"

    # ========================================================
    # REGISTRO
    # ========================================================

    def register_feedback(
        self,
        client_id: str,
        score: int,
        comments: str,
    ) -> Dict:

        if score < 1:
            score = 1

        if score > 10:
            score = 10

        feedback = {

            "feedback_id":
                self._feedback_id(),

            "client_id":
                client_id,

            "score":
                score,

            "comments":
                comments,

            "created_at":
                self._now(),

            "status":
                "REGISTERED",
        }

        self._feedbacks.append(
            feedback
        )

        return feedback

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_feedbacks(
        self,
    ) -> List[Dict]:

        return list(
            self._feedbacks
        )

    def get_client_feedback(
        self,
        client_id: str,
    ) -> List[Dict]:

        return [

            item

            for item in self._feedbacks

            if item["client_id"]
            == client_id
        ]

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def calculate_average_score(
        self,
    ) -> float:

        if not self._feedbacks:
            return 0.0

        total = sum(
            item["score"]
            for item in self._feedbacks
        )

        return round(
            total / len(
                self._feedbacks
            ),
            2,
        )

    # ========================================================
    # REPORTE
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        return {

            "feedbacks":
                len(
                    self._feedbacks
                ),

            "average_score":
                self.calculate_average_score(),

            "generated_at":
                self._now(),
        }

    def generate_report(
        self,
    ) -> Dict:

        return {

            "feedbacks":
                self.get_feedbacks(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),

            "report_type":
                "CUSTOMER_FEEDBACK",
        }


# ============================================================
# FIN
# customer_feedback_engine.py
# ============================================================
