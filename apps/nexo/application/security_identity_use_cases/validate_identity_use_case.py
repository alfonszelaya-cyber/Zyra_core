from apps.nexo.domain.security.identity_validation_engine import (
    IdentityValidationEngine,
)


class ValidateIdentityUseCase:

    def __init__(
        self,
        identity_validation_engine:
        IdentityValidationEngine,
    ):
        self._identity_validation_engine = (
            identity_validation_engine
        )

    def execute(
        self,
        identity_payload: dict,
    ) -> dict:

        validation = (
            self._identity_validation_engine.validate(
                identity_payload
            )
        )

        return {
            "validation": validation,
            "status": "VALIDATED",
        }
