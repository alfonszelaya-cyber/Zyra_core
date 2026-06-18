from apps.nexo.domain.security.biometric_engine import (
    BiometricEngine,
)


class RegisterBiometricUseCase:

    def __init__(
        self,
        biometric_engine: BiometricEngine,
    ):
        self._biometric_engine = biometric_engine

    def execute(
        self,
        user_id: str,
        biometric_data: dict,
    ) -> dict:

        biometric_id = (
            self._biometric_engine.register(
                user_id=user_id,
                biometric_data=biometric_data,
            )
        )

        return {
            "biometric_id": biometric_id,
            "status": "REGISTERED",
        }
