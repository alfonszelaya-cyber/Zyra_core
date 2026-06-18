from datetime import datetime

from apps.nexo.domain.government.government_event_registry import (
    GovernmentEventRegistry,
)
from apps.nexo.domain.government.government_event_entity import (
    GovernmentEventEntity,
)


class RegisterGovernmentEventUseCase:

    def __init__(
        self,
        event_registry: GovernmentEventRegistry,
    ):
        self._event_registry = event_registry

    def execute(
        self,
        institution_id: str,
        event_type: str,
        description: str,
        reference_id: str,
    ) -> dict:

        event = GovernmentEventEntity(
            institution_id=institution_id,
            event_type=event_type,
            description=description,
            reference_id=reference_id,
            created_at=datetime.utcnow(),
        )

        self._event_registry.save(event)

        return {
            "institution_id": institution_id,
            "event_type": event_type,
            "reference_id": reference_id,
            "status": "REGISTERED",
        }
