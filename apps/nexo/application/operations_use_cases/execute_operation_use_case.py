from apps.nexo.domain.operations.operations_engine import (
    OperationsEngine,
)


class ExecuteOperationUseCase:

    def __init__(
        self,
        operations_engine: OperationsEngine,
    ):
        self._operations_engine = operations_engine

    def execute(
        self,
        operation_id: str,
        operation_type: str,
        payload: dict,
    ) -> dict:

        result = self._operations_engine.execute_operation(
            operation_id=operation_id,
            operation_type=operation_type,
            payload=payload,
        )

        return {
            "operation_id": operation_id,
            "operation_type": operation_type,
            "result": result,
            "status": "EXECUTED",
        }
