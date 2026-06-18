class ClientRelationshipEngine:

    def link_company(
        self,
        client_id: str,
        company_id: str,
    ) -> dict:

        return {
            "client_id": client_id,
            "company_id": company_id,
            "relationship": "OWNER",
            "status": "LINKED",
        }
