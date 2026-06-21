# ============================================================
# government_registry.py
# NEXO / ZYRA
# Government Registry
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class GovernmentRegistry:

    def __init__(self):

        self._registry: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def register_entity(
        self,
        entity_name: str,
        entity_type: str,
        jurisdiction: str,
    ) -> Dict:

        record = {

            "registry_id":
                f"REG-{uuid4()}",

            "entity_name":
                entity_name,

            "entity_type":
                entity_type,

            "jurisdiction":
                jurisdiction,

            "registered_at":
                self._now(),

            "status":
                "ACTIVE",
        }

        self._registry.append(record)

        return record

    def get_registry(self):

        return list(self._registry)

    def get_summary(self):

        return {

            "entities":
                len(self._registry),

            "generated_at":
                self._now(),
        }


government_registry = (
    GovernmentRegistry()
)
