class ClientValidationEngine:

    def validate(
        self,
        client_data: dict,
    ) -> bool:

        required_fields = [
            "name",
            "document",
            "email",
        ]

        return all(
            field in client_data
            and client_data[field]
            for field in required_fields
        )
