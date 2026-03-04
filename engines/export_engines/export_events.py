# ============================================================
# export_events.py
# NEXO / ZYRA — EXPORT EVENTS
# ============================================================

from protocol.event_bus.emit_events import emit_events

def export_event(event: str, payload: dict):
    emit_event("module", {
        "module": "export",
        "event": event,
        "payload": payload
    })
