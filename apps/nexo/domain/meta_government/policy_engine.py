# ============================================================
# policy_engine.py
# NEXO / ZYRA
# Policy Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class PolicyEngine:

    def __init__(self):

        self._policies: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def create_policy(
        self,
        title: str,
        category: str,
        content: Dict,
    ) -> Dict:

        policy = {

            "policy_id":
                f"POL-{uuid4()}",

            "title":
                title,

            "category":
                category,

            "content":
                content,

            "created_at":
                self._now(),

            "status":
                "DRAFT",
        }

        self._policies.append(
            policy
        )

        return policy

    def publish_policy(
        self,
        policy_id: str,
    ) -> Optional[Dict]:

        for policy in self._policies:

            if (
                policy["policy_id"]
                == policy_id
            ):

                policy["status"] = (
                    "PUBLISHED"
                )

                policy[
                    "published_at"
                ] = self._now()

                return policy

        return None

    def get_policies(
        self,
    ):

        return list(
            self._policies
        )


policy_engine = (
    PolicyEngine()
)
