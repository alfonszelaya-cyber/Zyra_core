from apps.nexo.domain.government.record_validation_engine import (
    RecordValidationEngine,
)


class ValidateGovernmentRecordUseCase:

    def __init__(
        self,
        validation_engine: RecordValidationEngine,
    ):
        self._validation_engine = validation_engine

    def execute(
        self,
        record_id: str,
    ) -> dict:

        validation = (
            self._validation_engine.validate_record(
                record_id
            )
        )

        return {
            "record_id": record_id,
            "valid": validation.get(
                "valid",
                False,
            ),
            "details": validation,
        }
