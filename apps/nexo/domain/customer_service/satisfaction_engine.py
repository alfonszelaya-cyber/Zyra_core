
# ============================================================
# satisfaction_engine.py
# NEXO / ZYRA
# Satisfaction Engine
# ============================================================

from datetime import datetime
from typing import Dict, List


class SatisfactionEngine:

    """
    Motor de satisfacción.

    Responsabilidades:
    - Calcular satisfacción promedio
    - Clasificar nivel de satisfacción
    - Generar métricas
    - Mantener historial
    - Generar reportes
    """

    def __init__(self):

        self._scores = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    # ========================================================
    # REGISTRO
    # ========================================================

    def register_score(
        self,
        score: int,
    ) -> None:

        if score < 1:
            score = 1

        if score > 10:
            score = 10

        self._scores.append(
            score
        )

    # ========================================================
    # CÁLCULO
    # ========================================================

    def calculate(
        self,
        scores: List[int],
    ) -> float:

        if not scores:
            return 0.0

        return round(
            sum(scores) / len(scores),
            2,
        )

    def calculate_current_score(
        self,
    ) -> float:

        return self.calculate(
            self._scores
        )

    # ========================================================
    # CLASIFICACIÓN
    # ========================================================

    def classify(
        self,
        score: float,
    ) -> str:

        if score >= 9:
            return "EXCELLENT"

        if score >= 7:
            return "GOOD"

        if score >= 5:
            return "REGULAR"

        return "CRITICAL"

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_scores(
        self,
    ) -> List[int]:

        return list(
            self._scores
        )

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        average = (
            self.calculate_current_score()
        )

        return {

            "total_scores":
                len(
                    self._scores
                ),

            "average_score":
                average,

            "classification":
                self.classify(
                    average
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

            "scores":
                self.get_scores(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),

            "report_type":
                "SATISFACTION",
        }


# ============================================================
# FIN
# satisfaction_engine.py
# ============================================================
