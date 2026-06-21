# ============================================================
# government_coordination_engine.py
# NEXO / ZYRA
# Government Coordination Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class GovernmentCoordinationEngine:

    def __init__(self):

        self._requests: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def create_request(
        self,
        institution: str,
        request_type: str,
        details: Dict,
    ) -> Dict:

        request = {

            "request_id":
                f"GOV-{uuid4()}",

            "institution":
                institution,

            "request_type":
                request_type,

            "details":
                details,

            "created_at":
                self._now(),

            "status":
                "OPEN",
        }

        self._requests.append(request)

        return request

    def close_request(
        self,
        request_id: str,
    ):

        for request in self._requests:

            if (
                request["request_id"]
                == request_id
            ):

                request["status"] = "CLOSED"

                return request

        return None

    def get_requests(self):

        return list(self._requests)


government_coordination_engine = (
    GovernmentCoordinationEngine()
)
