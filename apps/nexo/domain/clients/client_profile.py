class ClientProfile:

    def build_profile(
        self,
        client_data: dict,
        history: list,
        companies: list,
    ) -> dict:

        return {
            "client": client_data,
            "history": history,
            "companies": companies,
            "risk_level": "NORMAL",
            "profile_completed": True,
        }
