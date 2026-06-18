
from apps.nexo.domain.radar_vip.vip_operation_registry import (
    VipOperationRegistry,
)


class RegisterVipOperationUseCase:

    def __init__(
        self,
        vip_operation_registry: (
            VipOperationRegistry
        ),
    ):
        self._vip_operation_registry = (
            vip_operation_registry
        )

    def execute(
        self,
        operation_data: dict,
    ) -> dict:

        operation = (
            self._vip_operation_registry.register(
                operation_data=operation_data,
            )
        )

        return {
            "operation": operation,
            "status": "REGISTERED",
        }
