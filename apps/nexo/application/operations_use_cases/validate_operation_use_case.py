from apps.nexo.domain.operations.operations_validation_engine import (
    OperationsValidationEngine,
)


class ValidateOperationUseCase:

    def __init__(
        self,
        operations_validation_engine: (
            OperationsValidationEngine
        ),
    ):
        self._operations_validation_engine = (
            operations_validation_engine
        )

    def execute(
        self,
        operation_data: dict,
    ) -> dict:

        validation = (
            self._operations_validation_engine.validate(
                operation_data=operation_data,
            )
        )

        return {
            "valid": validation.get(
                "valid",
                False,
            ),
            "details": validation,
        }
