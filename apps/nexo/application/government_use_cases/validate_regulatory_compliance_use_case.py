from apps.nexo.domain.government.regulatory_compliance_engine import (
    RegulatoryComplianceEngine,
)


class ValidateRegulatoryComplianceUseCase:

    def __init__(
        self,
        compliance_engine: RegulatoryComplianceEngine,
    ):
        self._compliance_engine = compliance_engine

    def execute(
        self,
        institution_id: str,
        regulation_code: str,
    ) -> dict:

        compliance = (
            self._compliance_engine.validate(
                institution_id=institution_id,
                regulation_code=regulation_code,
            )
        )

        return {
            "institution_id": institution_id,
            "regulation_code": regulation_code,
            "compliant": compliance.get(
                "compliant",
                False,
            ),
            "details": compliance,
        }
