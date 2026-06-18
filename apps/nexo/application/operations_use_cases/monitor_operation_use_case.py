from apps.nexo.domain.operations.operational_control_engine import (
    OperationalControlEngine,
)


class MonitorOperationUseCase:

    def __init__(
        self,
        operational_control_engine: OperationalControlEngine,
    ):
        self._operational_control_engine = (
            operational_control_engine
        )

    def execute(
        self,
        operation_id: str,
    ) -> dict:

        monitoring = (
            self._operational_control_engine.monitor_operation(
                operation_id=operation_id,
            )
        )

        return {
            "operation_id": operation_id,
            "monitoring": monitoring,
            "status": "MONITORED",
        }
