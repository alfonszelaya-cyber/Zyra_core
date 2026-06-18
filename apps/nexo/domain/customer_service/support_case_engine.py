from datetime import datetime


class SupportCaseEngine:

    def generate_case_report(
        self,
        case_data: dict,
    ) -> dict:

        return {
            "generated_at": datetime.utcnow(),
            "case_data": case_data,
            "report_type": "SUPPORT_CASE",
            "status": "GENERATED",
        }
