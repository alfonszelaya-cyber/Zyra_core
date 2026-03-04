# =========================================
# operations_core.py
# ZYRA CORE — OPERATIONS CORE
# Base única de operaciones | Inmutable | Auditable | Event-driven
# =========================================

from datetime import datetime
import json
import os
from uuid import uuid4

# EVENT BUS NUEVO
from protocol.event_bus.emit_events import emit_events

# LEDGER NUEVO
from foundation.ledger.core_ledger import ledger_record

# LOGGING
from infrastructure.monitoring_adapters.logging.zyra_logs_hook import log


# -------------------------
# PATHS
# -------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

OPERATIONS_FILE = os.path.join(DATA_DIR, "operations.json")


# -------------------------
# UTILIDADES
# -------------------------

def _now():
    return datetime.utcnow().isoformat()


def _load(path, default):
    if not os.path.exists(path):
        return default

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def _save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# -------------------------
# REGISTRO DE OPERACIÓN
# -------------------------

def registrar_operacion(
    tipo_operacion,
    monto,
    moneda="USD",
    origen=None,
    destino=None,
    estado="PENDIENTE",
    metadata=None
):
    """
    tipo_operacion: VENTA | COMPRA | TRANSFERENCIA | PAGO | COBRO | AJUSTE
    """

    operacion = {
        "operation_id": f"OP-{uuid4().hex[:10].upper()}",
        "tipo": tipo_operacion,
        "monto": monto,
        "moneda": moneda,
        "origen": origen,
        "destino": destino,
        "estado": estado,
        "metadata": metadata or {},
        "ts": _now()
    }

    # -------------------------
    # PERSISTENCIA
    # -------------------------

    operaciones = _load(OPERATIONS_FILE, [])
    operaciones.append(operacion)
    _save(OPERATIONS_FILE, operaciones)

    # -------------------------
    # LEDGER
    # -------------------------

    ledger_record(
        event="OPERACION_REGISTRADA",
        status=estado,
        detail=operacion
    )

    # -------------------------
    # EVENTO DEL SISTEMA
    # -------------------------

    emit_events(
        "business",
        {
            "module": "OPERATIONS_CORE",
            "event": "OPERACION_REGISTRADA",
            "payload": operacion
        }
    )

    # -------------------------
    # LOG
    # -------------------------

    log(
        "INFO",
        f"Operación {operacion['operation_id']} registrada",
        "OPERATIONS_CORE"
    )

    return operacion


# -------------------------
# CONSULTAS
# -------------------------

def operaciones_por_tipo(tipo):
    return [
        o for o in _load(OPERATIONS_FILE, [])
        if o["tipo"] == tipo
    ]


def operaciones_por_estado(estado):
    return [
        o for o in _load(OPERATIONS_FILE, [])
        if o["estado"] == estado
    ]


def historial_operaciones():
    return _load(OPERATIONS_FILE, [])
