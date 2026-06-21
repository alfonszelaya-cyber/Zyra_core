# ============================================================
# client_relationship_engine.py
# NEXO / ZYRA
# Client Relationship Domain Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import List, Optional


class ClientRelationshipEngine:

    """
    Motor de relaciones.

    Responsabilidades:
    - Vincular clientes con empresas
    - Gestionar roles
    - Gestionar representantes
    - Gestionar beneficiarios
    - Gestionar relaciones corporativas
    - Auditoría de relaciones
    """

    def __init__(self):

        self._relationships = []

    # ========================================================
    # UTILIDADES
    # ========================================================

    def _now(self):

        return datetime.utcnow().isoformat()

    def _relationship_id(self):

        return f"REL-{uuid4()}"

    # ========================================================
    # CREAR RELACIÓN
    # ========================================================

    def link_company(
        self,
        client_id: str,
        company_id: str,
        relationship: str = "OWNER",
        ownership_percentage: float = 100.0,
    ) -> dict:

        relation = {

            "relationship_id":
                self._relationship_id(),

            "client_id":
                client_id,

            "company_id":
                company_id,

            "relationship":
                relationship,

            "ownership_percentage":
                ownership_percentage,

            "status":
                "LINKED",

            "created_at":
                self._now(),
        }

        self._relationships.append(
            relation
        )

        return relation

    # ========================================================
    # CONSULTAS
    # ========================================================

    def get_relationship(
        self,
        relationship_id: str,
    ) -> Optional[dict]:

        for item in self._relationships:

            if (
                item["relationship_id"]
                == relationship_id
            ):
                return item

        return None

    def get_client_relationships(
        self,
        client_id: str,
    ) -> List[dict]:

        return [

            item

            for item in self._relationships

            if (
                item["client_id"]
                == client_id
            )
        ]

    def get_company_relationships(
        self,
        company_id: str,
    ) -> List[dict]:

        return [

            item

            for item in self._relationships

            if (
                item["company_id"]
                == company_id
            )
        ]

    # ========================================================
    # ESTADOS
    # ========================================================

    def unlink_company(
        self,
        relationship_id: str,
    ) -> Optional[dict]:

        relation = self.get_relationship(
            relationship_id
        )

        if not relation:
            return None

        relation["status"] = "UNLINKED"

        relation["updated_at"] = self._now()

        return relation

    def suspend_relationship(
        self,
        relationship_id: str,
    ) -> Optional[dict]:

        relation = self.get_relationship(
            relationship_id
        )

        if not relation:
            return None

        relation["status"] = "SUSPENDED"

        relation["updated_at"] = self._now()

        return relation

    # ========================================================
    # TIPOS DE RELACIÓN NEXO
    # ========================================================

    def link_owner(
        self,
        client_id: str,
        company_id: str,
        percentage: float,
    ):

        return self.link_company(
            client_id,
            company_id,
            "OWNER",
            percentage,
        )

    def link_legal_representative(
        self,
        client_id: str,
        company_id: str,
    ):

        return self.link_company(
            client_id,
            company_id,
            "LEGAL_REPRESENTATIVE",
            0,
        )

    def link_shareholder(
        self,
        client_id: str,
        company_id: str,
        percentage: float,
    ):

        return self.link_company(
            client_id,
            company_id,
            "SHAREHOLDER",
            percentage,
        )

    def link_beneficiary(
        self,
        client_id: str,
        company_id: str,
    ):

        return self.link_company(
            client_id,
            company_id,
            "BENEFICIARY",
            0,
        )

    # ========================================================
    # MÉTRICAS
    # ========================================================

    def generate_summary(self):

        active = len([
            x
            for x in self._relationships
            if x["status"] == "LINKED"
        ])

        return {

            "relationships":
                len(
                    self._relationships
                ),

            "active_relationships":
                active,

            "generated_at":
                self._now(),
        }
