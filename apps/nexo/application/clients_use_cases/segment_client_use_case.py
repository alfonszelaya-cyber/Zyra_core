from apps.nexo.domain.clients.client_registry import ClientRegistry


class SegmentClientUseCase:

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

        score = client.get("total_transactions", 0)

        if score >= 1000:
            segment = "VIP"
        elif score >= 250:
            segment = "PREFERRED"
        elif score >= 50:
            segment = "ACTIVE"
        else:
            segment = "STANDARD"

        self._client_registry.update(
            client_id=client_id,
            updates={
                "segment": segment,
            },
        )

        return {
            "client_id": client_id,
            "segment": segment,
        }
