from datetime import datetime


class ComplianceReportingEngine:

    def generate_report(
        self,
        report_data: dict,
    ) -> dict:

        return {
            "generated_at": datetime.utcnow(),
            "report_type": "COMPLIANCE",
            "data": report_data,
            "status": "GENERATED",
        }
