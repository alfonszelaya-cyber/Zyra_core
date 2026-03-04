# ============================================================
# tax_events.py
# ZYRA CORE — FISCAL / IMPUESTOS
# EVENTOS FISCALES
# PASIVO | SOLO EMITE
# ============================================================

from protocol.event_bus.emit_events import emit_events


def emit_tax_event(event_name: str, payload: dict) -> None:
    """
    Emite eventos fiscales del sistema.
    """
    emit_events("business", {
        "module": "TAX",
        "event": event_name,
        "payload": payload
    })
