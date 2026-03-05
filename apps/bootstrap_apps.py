"""
ZYRA CORE
APPS REGISTRY

Registro central de todas las apps del ecosistema.
Permite que ZYRA detecte, active y gestione aplicaciones.

Diseñado para:
NEXO
SEMILLA
AXIS
AGRO
MI_PRIMER_EMPLEO
SUBASTAS
RECICLAJE_DIGITAL
ARQUEOLOGIA_DIGITAL
"""

APPS_REGISTRY = {
    "nexo": "apps.nexo",
    "semilla": "apps.semilla",
    "axis": "apps.axis",
    "agro": "apps.agro",
    "mi_primer_empleo": "apps.mi_primer_empleo",
    "subastas": "apps.subastas",
    "reciclaje_digital": "apps.reciclaje_digital",
    "arqueologia_digital": "apps.arqueologia_digital",
}


def list_apps():
    """
    Devuelve todas las apps registradas
    """
    return list(APPS_REGISTRY.keys())


def get_app_module(app_name: str):
    """
    Devuelve el módulo de una app
    """
    return APPS_REGISTRY.get(app_name)


def app_exists(app_name: str) -> bool:
    """
    Verifica si una app existe
    """
    return app_name in APPS_REGISTRY


def get_registry():
    """
    Devuelve el registro completo
    """
    return APPS_REGISTRY
