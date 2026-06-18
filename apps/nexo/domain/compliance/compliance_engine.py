from datetime import datetime


class ComplianceEngine:

    def register_event(
        self,
        event_type: str,
        entity_id: str,
        details: dict,
    ) -> dict:

        return {
            "event_type": event_type,
            "entity_id": entity_id,
            "details": details,
            "created_at": datetime.utcnow(),
            "status": "REGISTERED",
        }

    def validate_compliance(
        self,
        compliance_data: dict,
    ) -> bool:

        return bool(compliance_data)
