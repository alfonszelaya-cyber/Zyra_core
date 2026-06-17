from apps.nexo.domain.clients.client_registry import ClientRegistry


class GenerateClientProfileUseCase:

    def __init__(
        self,
        client_registry: ClientRegistry,
    ):
        self._client_registry = client_registry

    def execute(
        self,
        client_id: str,
    ) -> dict:

        client = self._client_registry.get_by_id(
            client_id=client_id,
        )

        return {
            "client_id": client["client_id"],
            "name": client.get("name"),
            "email": client.get("email"),
            "phone": client.get("phone"),
            "status": client.get("status"),
            "profile": client,
        }
