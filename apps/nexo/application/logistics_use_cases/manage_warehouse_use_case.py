from apps.nexo.domain.logistics.warehouse_engine import (
    WarehouseEngine,
)


class ManageWarehouseUseCase:

    def __init__(
        self,
        warehouse_engine: WarehouseEngine,
    ):
        self._warehouse_engine = warehouse_engine

    def execute(
        self,
        warehouse_id: str,
        operation: str,
        payload: dict,
    ) -> dict:

        result = self._warehouse_engine.execute_operation(
            warehouse_id=warehouse_id,
            operation=operation,
            payload=payload,
        )

        return {
            "warehouse_id": warehouse_id,
            "operation": operation,
            "status": "COMPLETED",
            "result": result,
        }
