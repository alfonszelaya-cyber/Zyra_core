# ============================================================
# ledger_events.py
# ZYRA CORE — CONTABILIDAD / LEDGER
# EVENTOS CONTABLES
# PASIVO | SOLO EMITE
# ============================================================

from protocol.event_bus.emit_events import emit_events


def emit_ledger_event(event_name: str, payload: dict) -> None:
    """
    Emite eventos del ledger contable.
    """
    emit_events("business", {
        "module": "LEDGER",
        "event": event_name,
        "payload": payload
    })
