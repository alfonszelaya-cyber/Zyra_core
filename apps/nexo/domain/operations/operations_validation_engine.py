# ============================================================
# operations_validation_engine.py
# NEXO / ZYRA
# Operations Validation Engine
# ============================================================

from datetime import datetime
from typing import Dict, List


class OperationsValidationEngine:

    def __init__(self):

        self._validation_log: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def validate_operation(
        self,
        operation: Dict,
    ) -> Dict:

        required_fields = [

            "operation_id",
            "operation_type",
            "title",
            "status",
        ]

        missing = []

        for field in required_fields:

            if (
                field not in operation
                or operation[field] in (
                    None,
                    "",
                    [],
                    {},
                )
            ):

                missing.append(
                    field
                )

        result = {

            "valid":
                len(missing) == 0,

            "missing_fields":
                missing,

            "validated_at":
                self._now(),
        }

        self._validation_log.append(
            result
        )

        return result

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

        successful = len(

            [
                x
                for x
                in self._validation_log

                if x["valid"]
            ]
        )

        return {

            "validations":
                total,

            "successful":
                successful,

            "failed":
                total
                - successful,

            "generated_at":
                self._now(),
        }


operations_validation_engine = (
    OperationsValidationEngine()
  )
