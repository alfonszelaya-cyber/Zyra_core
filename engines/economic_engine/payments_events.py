# ============================================================
# payments_events.py
# ZYRA CORE — PAGOS & BANCOS
# EVENTOS DE PAGOS
# PASIVO | SOLO EMITE
# ============================================================

from protocol.event_bus.emit_events import emit_events


def emit_payment_event(event_name: str, payload: dict) -> None:
    """
    Emite eventos relacionados con pagos.
    """
    emit_events("business", {
        "module": "PAYMENTS",
        "event": event_name,
        "payload": payload
    })
