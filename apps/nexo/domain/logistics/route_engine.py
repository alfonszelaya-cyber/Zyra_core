# ============================================================
# route_engine.py
# NEXO / ZYRA
# Route Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List


class RouteEngine:

    def __init__(self):

        self._routes: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def create_route(
        self,
        origin: str,
        destination: str,
        checkpoints: List[str],
    ) -> Dict:

        route = {

            "route_id":
                f"RTE-{uuid4()}",

            "origin":
                origin,

            "destination":
                destination,

            "checkpoints":
                checkpoints,

            "created_at":
                self._now(),

            "status":
                "ACTIVE",
        }

        self._routes.append(route)

        return route

    def get_routes(
        self,
    ):

        return list(
            self._routes
        )

    def calculate_distance(
        self,
        route: Dict,
    ) -> Dict:

        return {

            "route_id":
                route["route_id"],

            "estimated_km":
                len(
                    route.get(
                        "checkpoints",
                        []
                    )
                ) * 100,

            "calculated_at":
                self._now(),
        }


route_engine = (
    RouteEngine()
)
