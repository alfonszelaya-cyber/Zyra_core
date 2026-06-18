from apps.nexo.domain.security.authentication_engine import (
    AuthenticationEngine,
)


class AuthenticateUserUseCase:

    def __init__(
        self,
        authentication_engine: AuthenticationEngine,
    ):
        self._authentication_engine = (
            authentication_engine
        )

    def execute(
        self,
        username: str,
        password: str,
    ) -> dict:

        result = (
            self._authentication_engine.authenticate(
                username=username,
                password=password,
            )
        )

        return {
            "authenticated": result,
            "status": "SUCCESS"
            if result
            else "DENIED",
        }
