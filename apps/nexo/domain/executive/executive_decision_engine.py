from datetime import datetime


class ExecutiveDecisionEngine:

    def support_decision(
        self,
        decision_context: dict,
    ) -> dict:

        return {
            "generated_at": datetime.utcnow(),
            "context": decision_context,
            "recommendation":
                "REVIEW_REQUIRED",
            "status": "READY",
        }
