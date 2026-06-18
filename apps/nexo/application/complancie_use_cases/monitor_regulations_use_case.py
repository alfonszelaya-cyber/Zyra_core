from apps.nexo.domain.compliance.regulatory_monitor import (
    RegulatoryMonitor,
)


class MonitorRegulationsUseCase:

    def __init__(
        self,
        regulatory_monitor: RegulatoryMonitor,
    ):
        self._regulatory_monitor = regulatory_monitor

    def execute(
        self,
        jurisdiction: str,
    ) -> dict:

        regulations = self._regulatory_monitor.get_updates(
            jurisdiction=jurisdiction,
        )

        return {
            "jurisdiction": jurisdiction,
            "regulations_found": len(regulations),
            "regulations": regulations,
        }
