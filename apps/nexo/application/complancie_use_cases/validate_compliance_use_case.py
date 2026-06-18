from apps.nexo.domain.compliance.compliance_validation_engine import (
    ComplianceValidationEngine,
)


class ValidateComplianceUseCase:

    def __init__(
        self,
        validation_engine: ComplianceValidationEngine,
    ):
        self._validation_engine = validation_engine

    def execute(
        self,
        operation_data: dict,
    ) -> dict:

        result = self._validation_engine.validate(
            operation_data=operation_data,
        )

        return {
            "is_valid": result.get("is_valid", False),
            "violations": result.get("violations", []),
            "warnings": result.get("warnings", []),
        }
