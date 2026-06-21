# ============================================================
# agro_adapter/event_bridge.py
# Event Bridge NEXO ↔ AGRO
# ============================================================

from datetime import datetime
from uuid import uuid4


class AgroEventBridge:

    def build_event(
        self,
        event_type: str,
        payload: dict,
    ) -> dict:

        return {
            "event_id": str(uuid4()),
            "source": "NEXO",
            "target": "AGRO",
            "event_type": event_type,
            "payload": payload,
            "created_at": datetime.utcnow().isoformat(),
        }

    def invoice_created(
        self,
        invoice_data: dict,
    ) -> dict:

        return self.build_event(
            event_type="INVOICE_CREATED",
            payload=invoice_data,
        )

    def payment_registered(
        self,
        payment_data: dict,
    ) -> dict:

        return self.build_event(
            event_type="PAYMENT_REGISTERED",
            payload=payment_data,
        )

    def inventory_updated(
        self,
        inventory_data: dict,
    ) -> dict:

        return self.build_event(
            event_type="INVENTORY_UPDATED",
            payload=inventory_data,
        )
