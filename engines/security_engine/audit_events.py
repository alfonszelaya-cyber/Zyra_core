# ==========================================================
# audit_events.py
# ZYRA CORE — AUDITORÍA & TRAZABILIDAD
# EVENTOS DE AUDITORÍA DEL SISTEMA
# PASIVO | SOLO EMITE
# ==========================================================

from protocol.event_bus.emit_events import emit_events


def emit_audit_event(event_name: str, payload: dict) -> None:
    """
    Emite eventos del sistema de auditoría.
    """
    emit_events("core", {
        "module": "AUDIT",
        "event": event_name,
        "payload": payload
    })
