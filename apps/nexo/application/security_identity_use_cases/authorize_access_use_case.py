from apps.nexo.domain.security.authorization_engine import (
    AuthorizationEngine,
)


class AuthorizeAccessUseCase:

    def __init__(
        self,
        authorization_engine: AuthorizationEngine,
    ):
        self._authorization_engine = (
            authorization_engine
        )

    def execute(
        self,
        user_id: str,
        resource: str,
        action: str,
    ) -> dict:

        authorized = (
            self._authorization_engine.authorize(
                user_id=user_id,
                resource=resource,
                action=action,
            )
        )

        return {
            "authorized": authorized,
            "resource": resource,
            "action": action,
        }
