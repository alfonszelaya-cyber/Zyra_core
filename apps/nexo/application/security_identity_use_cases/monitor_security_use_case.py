from apps.nexo.domain.security.security_monitor_engine import (
    SecurityMonitorEngine,
)


class MonitorSecurityUseCase:

    def __init__(
        self,
        security_monitor_engine:
        SecurityMonitorEngine,
    ):
        self._security_monitor_engine = (
            security_monitor_engine
        )

    def execute(
        self,
        monitoring_scope: dict,
    ) -> dict:

        monitoring = (
            self._security_monitor_engine.monitor(
                monitoring_scope
            )
        )

        return {
            "monitoring": monitoring,
            "status": "ACTIVE",
        }
