from datetime import datetime

from apps.nexo.domain.clients.client_registry import ClientRegistry


class RegisterClientHistoryUseCase:

    def __init__(
        self,
        client_registry: ClientRegistry,
    ):
        self._client_registry = client_registry

    def execute(
        self,
        client_id: str,
        event_type: str,
        description: str,
    ) -> dict:

        history_event = {
            "event_type": event_type,
            "description": description,
            "created_at": datetime.utcnow().isoformat(),
        }

        self._client_registry.register_history(
            client_id=client_id,
            history_event=history_event,
        )

        return history_event
