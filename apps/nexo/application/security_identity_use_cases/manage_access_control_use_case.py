from apps.nexo.domain.security.access_control_engine import (
    AccessControlEngine,
)


class ManageAccessControlUseCase:

    def __init__(
        self,
        access_control_engine:
        AccessControlEngine,
    ):
        self._access_control_engine = (
            access_control_engine
        )

    def execute(
        self,
        policy_data: dict,
    ) -> dict:

        policy = (
            self._access_control_engine.apply_policy(
                policy_data
            )
        )

        return {
            "policy": policy,
            "status": "APPLIED",
        }
