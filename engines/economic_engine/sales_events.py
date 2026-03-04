# ============================================================
# sales_events.py
# ZYRA CORE — VENTAS / POS
# EVENTOS DE VENTAS
# PASIVO | SOLO EMITE
# ============================================================

from protocol.event_bus.emit_events import emit_events


def emit_sales_event(event_name: str, payload: dict) -> None:
    """
    Emite eventos del motor de ventas.
    """
    emit_events("business", {
        "module": "SALES",
        "event": event_name,
        "payload": payload
    })
