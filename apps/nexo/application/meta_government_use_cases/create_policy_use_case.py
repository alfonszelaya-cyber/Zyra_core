from apps.nexo.domain.meta_government.policy_engine import (
    PolicyEngine,
)


class CreatePolicyUseCase:

    def __init__(
        self,
        policy_engine: PolicyEngine,
    ):
        self._policy_engine = policy_engine

    def execute(
        self,
        policy_data: dict,
    ) -> dict:

        policy = self._policy_engine.create_policy(
            policy_data=policy_data,
        )

        return {
            "policy": policy,
            "status": "CREATED",
        }
