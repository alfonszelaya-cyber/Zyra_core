# ============================================================
# identity_engine.py
# NEXO / ZYRA
# Universal Identity Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4

from .biometric_engine import (
    biometric_engine,
)

from .identity_audit_engine import (
    identity_audit_engine,
)


class IdentityEngine:

    def __init__(self):

        self._identities = {}

    def create_identity(
        self,
        entity_type: str,
        entity_id: str,
        name: str,
        document: str,
    ) -> dict:

        identity = {

            "identity_id":
                f"ID-{uuid4()}",

            "entity_type":
                entity_type,

            "entity_id":
                entity_id,

            "name":
                name,

            "document":
                document,

            "created_at":
                datetime.utcnow().isoformat(),

            "status":
                "ACTIVE",
        }

        self._identities[
            identity["identity_id"]
        ] = identity

        identity_audit_engine.register_event(
            identity["identity_id"],
            "IDENTITY_CREATED",
            identity,
        )

        return identity

    def get_identity(
        self,
        identity_id: str,
    ) -> dict | None:

        return self._identities.get(
            identity_id
        )


identity_engine = (
    IdentityEngine()
)
