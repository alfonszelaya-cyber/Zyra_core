class ComplianceValidationEngine:

    def validate(
        self,
        compliance_record: dict,
    ) -> bool:

        required_fields = [
            "entity_id",
            "event_type",
            "status",
        ]

        return all(
            field in compliance_record
            for field in required_fields
        )
