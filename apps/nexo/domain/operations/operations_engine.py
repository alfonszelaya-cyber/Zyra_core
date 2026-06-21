# ============================================================
# operations_engine.py
# NEXO / ZYRA
# Operations Engine
# ============================================================

from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional


class OperationsEngine:

    def __init__(self):

        self._operations: List[dict] = []

    def _now(self):

        return datetime.utcnow().isoformat()

    def create_operation(
        self,
        operation_type: str,
        title: str,
        details: Dict,
    ) -> Dict:

        operation = {

            "operation_id":
                f"OPS-{uuid4()}",

            "operation_type":
                operation_type,

            "title":
                title,

            "details":
                details,

            "created_at":
                self._now(),

            "status":
                "OPEN",
        }

        self._operations.append(
            operation
        )

        return operation

    def update_status(
        self,
        operation_id: str,
        status: str,
    ) -> Optional[Dict]:

        for operation in self._operations:

            if (
                operation["operation_id"]
                == operation_id
            ):

                operation["status"] = (
                    status
                )

                operation[
                    "updated_at"
                ] = self._now()

                return operation

        return None

    def get_operations(
        self,
    ):

        return list(
            self._operations
        )


operations_engine = (
    OperationsEngine()
)
