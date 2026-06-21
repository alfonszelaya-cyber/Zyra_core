# ============================================================
# government_document_engine.py
# NEXO / ZYRA
# Government Document Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class GovernmentDocumentEngine:

    def __init__(self):

        self._documents: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def register_document(
        self,
        institution: str,
        document_type: str,
        document_data: Dict,
    ) -> Dict:

        document = {

            "document_id":
                f"GD-{uuid4()}",

            "institution":
                institution,

            "document_type":
                document_type,

            "document_data":
                document_data,

            "created_at":
                self._now(),

            "status":
                "REGISTERED",
        }

        self._documents.append(document)

        return document

    def get_document(
        self,
        document_id: str,
    ) -> Optional[Dict]:

        for document in self._documents:

            if (
                document["document_id"]
                == document_id
            ):
                return document

        return None

    def get_documents(self):

        return list(self._documents)


government_document_engine = (
    GovernmentDocumentEngine()
)
