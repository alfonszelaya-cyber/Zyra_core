from apps.nexo.domain.logistics.route_engine import (
    RouteEngine,
)


class ManageRouteUseCase:

    def __init__(
        self,
        route_engine: RouteEngine,
    ):
        self._route_engine = route_engine

    def execute(
        self,
        route_id: str,
        origin: str,
        destination: str,
    ) -> dict:

        route = self._route_engine.optimize_route(
            route_id=route_id,
            origin=origin,
            destination=destination,
        )

        return {
            "route_id": route_id,
            "origin": origin,
            "destination": destination,
            "route": route,
        }
