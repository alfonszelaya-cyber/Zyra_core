from datetime import datetime
from uuid import uuid4


class ClientEngine:

    def create_client(
        self,
        name: str,
        document: str,
        email: str,
    ) -> dict:

        return {
            "client_id": str(uuid4()),
            "name": name,
            "document": document,
            "email": email,
            "created_at": datetime.utcnow(),
            "status": "ACTIVE",
        }

    def update_client(
        self,
        client: dict,
        updates: dict,
    ) -> dict:

        client.update(updates)

        return client
