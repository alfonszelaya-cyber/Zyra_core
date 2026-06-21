# ============================================================
# government_validation_engine.py
# NEXO / ZYRA
# Government Validation Engine
# ============================================================

from datetime import datetime
from typing import Dict, List


class GovernmentValidationEngine:

    def __init__(self):

        self._validation_log: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    # ========================================================
    # VALIDACIÓN GENERAL
    # ========================================================

    def validate_record(
        self,
        record: Dict,
        required_fields: List[str],
    ) -> Dict:

        missing = []

        for field in required_fields:

            if (
                field not in record
                or record[field] in (
                    None,
                    "",
                    [],
                    {},
                )
            ):
                missing.append(field)

        result = {

            "valid":
                len(missing) == 0,

            "missing_fields":
                missing,

            "validated_at":
                self._now(),
        }

        self._validation_log.append(result)

        return result

    # ========================================================
    # VALIDACIÓN DOCUMENTO
    # ========================================================

    def validate_document(
        self,
        document: Dict,
    ) -> Dict:

        return self.validate_record(

            document,

            [
                "document_id",
                "institution",
                "document_type",
                "status",
            ],
        )

    # ========================================================
    # VALIDACIÓN REGISTRO
    # ========================================================

    def validate_registry(
        self,
        registry: Dict,
    ) -> Dict:

        return self.validate_record(

            registry,

            [
                "registry_id",
                "entity_name",
                "entity_type",
                "status",
            ],
        )

    # ========================================================
    # VALIDACIÓN CUMPLIMIENTO
    # ========================================================

    def validate_compliance(
        self,
        compliance: Dict,
    ) -> Dict:

        return self.validate_record(

            compliance,

            [
                "compliance_id",
                "entity_id",
                "jurisdiction",
                "status",
            ],
        )

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_validation_log(
        self,
    ):

        return list(
            self._validation_log
        )

    def get_summary(
        self,
    ):

        total = len(
            self._validation_log
        )

        valid = len(

            [
                v
                for v
                in self._validation_log

                if v["valid"]
            ]
        )

        return {

            "validations":
                total,

            "successful":
                valid,

            "failed":
                total - valid,

            "generated_at":
                self._now(),
        }


# ============================================================
# INSTANCIA GLOBAL
# ============================================================

government_validation_engine = (
    GovernmentValidationEngine()
)

# ============================================================
# FIN
# government_validation_engine.py
# ============================================================
