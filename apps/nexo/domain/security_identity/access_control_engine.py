# ============================================================
# access_control_engine.py
# NEXO / ZYRA
# Access Control Engine
# Production Ready
# ============================================================

from datetime import datetime
from uuid import uuid4


class AccessControlEngine:

    def __init__(self):

        self._sessions = {}

    def grant_access(
        self,
        user_id: str,
        role: str,
        permissions: list[str],
    ) -> dict:

        session = {

            "session_id":
                f"ACS-{uuid4()}",

            "user_id":
                user_id,

            "role":
                role,

            "permissions":
                permissions,

            "granted_at":
                datetime.utcnow().isoformat(),

            "status":
                "ACTIVE",
        }

        self._sessions[
            session["session_id"]
        ] = session

        return session

    def revoke_access(
        self,
        session_id: str,
    ) -> bool:

        if session_id in self._sessions:

            self._sessions[
                session_id
            ]["status"] = "REVOKED"

            return True

        return False


access_control_engine = (
    AccessControlEngine()
)
