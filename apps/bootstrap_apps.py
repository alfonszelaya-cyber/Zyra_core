"""
ZYRA CORE
AUTO APPS REGISTRY

Descubre automáticamente todas las apps dentro de /apps
sin tener que escribirlas manualmente.
"""

import os


APPS_PATH = os.path.dirname(__file__)


def _discover_apps():

    apps = {}

    for name in os.listdir(APPS_PATH):

        path = os.path.join(APPS_PATH, name)

        if not os.path.isdir(path):
            continue

        if name.startswith("__"):
            continue

        if name == "shared_domain":
            continue

        apps[name] = f"apps.{name}"

    return apps


APPS_REGISTRY = _discover_apps()


def list_apps():
    return list(APPS_REGISTRY.keys())


def get_app_module(app_name: str):
    return APPS_REGISTRY.get(app_name)


def app_exists(app_name: str):
    return app_name in APPS_REGISTRY


def get_registry():
    return APPS_REGISTRY
