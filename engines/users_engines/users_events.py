# ============================================================
# users_events.py
# ZYRA CORE — USUARIOS & ROLES
# EVENTOS DE IDENTIDAD
# PASIVO | SOLO EMITE
# ============================================================

from protocol.event_bus.emit_events import emit_events


def emit_user_event(event_name: str, payload: dict) -> None:
    """
    Emite eventos relacionados con usuarios.
    """
    emit_events("business", {
        "module": "USERS",
        "event": event_name,
        "payload": payload
    })
