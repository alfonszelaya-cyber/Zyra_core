# ============================================================
# compliance_validation_engine.py
# NEXO / ZYRA
# Compliance Validation Engine
# ============================================================

from datetime import datetime
from typing import Dict, List


class ComplianceValidationEngine:

    """
    Motor de validación de cumplimiento.

    Responsabilidades:
    - Validar registros regulatorios
    - Validar estructura mínima
    - Detectar inconsistencias
    - Generar observaciones
    - Mantener historial de validación
    """

    def __init__(self):

        self._validations = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    # ========================================================
    # VALIDACIÓN DE CAMPOS
    # ========================================================

    def validate(
        self,
        compliance_record: Dict,
    ) -> bool:

        required_fields = [

            "entity_id",

            "event_type",

            "status",

        ]

        result = all(

            field in compliance_record

            and compliance_record[field] is not None

            and compliance_record[field] != ""

            for field in required_fields
        )

        self._validations.append(
            {
                "validated_at":
                    self._now(),

                "entity_id":
                    compliance_record.get(
                        "entity_id"
                    ),

                "result":
                    result,
            }
        )

        return result

    # ========================================================
    # VALIDACIÓN DETALLADA
    # ========================================================

    def validation_report(
        self,
        compliance_record: Dict,
    ) -> List[str]:

        issues = []

        if not compliance_record.get(
            "entity_id"
        ):
            issues.append(
                "Missing entity_id"
            )

        if not compliance_record.get(
            "event_type"
        ):
            issues.append(
                "Missing event_type"
            )

        if not compliance_record.get(
            "status"
        ):
            issues.append(
                "Missing status"
            )

        return issues

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_validations(
        self,
    ) -> List[Dict]:

        return list(
            self._validations
        )

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(
        self,
    ) -> Dict:

        successful = len(

            [

                item

                for item in self._validations

                if item["result"]
            ]

        )

        failed = len(
            self._validations
        ) - successful

        return {

            "total_validations":
                len(
                    self._validations
                ),

            "successful":
                successful,

            "failed":
                failed,

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

            "validations":
                self.get_validations(),

            "summary":
                self.generate_summary(),

            "generated_at":
                self._now(),

            "report_type":
                "COMPLIANCE_VALIDATION",
        }


# ============================================================
# FIN
# compliance_validation_engine.py
# ============================================================
