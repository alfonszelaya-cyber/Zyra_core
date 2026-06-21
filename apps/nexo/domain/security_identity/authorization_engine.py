# ============================================================
# authorization_engine.py
# NEXO / ZYRA
# Authorization Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class AuthorizationEngine:

    def authorize(
        self,
        user_id: str,
        resource: str,
        action: str,
        permissions: list[str],
    ) -> dict:

        allowed = (
            f"{resource}:{action}"
            in permissions
        )

        return {

            "authorization_id":
                f"AUT-{uuid4()}",

            "user_id":
                user_id,

            "resource":
                resource,

            "action":
                action,

            "allowed":
                allowed,

            "created_at":
                datetime.utcnow().isoformat(),

            "status":
                (
                    "AUTHORIZED"
                    if allowed
                    else "DENIED"
                ),
        }


authorization_engine = (
    AuthorizationEngine()
)
