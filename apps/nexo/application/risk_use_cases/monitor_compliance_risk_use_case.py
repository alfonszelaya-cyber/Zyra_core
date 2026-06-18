from apps.nexo.domain.risk.compliance_risk_engine import (
    ComplianceRiskEngine,
)


class MonitorComplianceRiskUseCase:

    def __init__(
        self,
        compliance_risk_engine: (
            ComplianceRiskEngine
        ),
    ):
        self._compliance_risk_engine = (
            compliance_risk_engine
        )

    def execute(
        self,
        compliance_context: dict,
    ) -> dict:

        monitoring = (
            self._compliance_risk_engine.monitor(
                compliance_context=compliance_context,
            )
        )

        return {
            "monitoring": monitoring,
            "status": "MONITORED",
        }
