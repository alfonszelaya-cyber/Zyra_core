from apps.nexo.domain.compliance.sanctions_monitor import (
    SanctionsMonitor,
)


class MonitorSanctionsUseCase:

    def __init__(
        self,
        sanctions_monitor: SanctionsMonitor,
    ):
        self._sanctions_monitor = sanctions_monitor

    def execute(
        self,
        company_id: str,
    ) -> dict:

        matches = self._sanctions_monitor.check_company(
            company_id=company_id,
        )

        return {
            "company_id": company_id,
            "matches_found": len(matches),
            "matches": matches,
            "status": "REVIEW_REQUIRED" if matches else "CLEAR",
        }
