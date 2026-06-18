from datetime import datetime


class CustomerServiceEngine:

    def create_service_record(
        self,
        client_id: str,
        category: str,
        description: str,
    ) -> dict:

        return {
            "client_id": client_id,
            "category": category,
            "description": description,
            "created_at": datetime.utcnow(),
            "status": "OPEN",
        }

    def close_service_record(
        self,
        service_record: dict,
    ) -> dict:

        service_record["status"] = "CLOSED"

        return service_record
