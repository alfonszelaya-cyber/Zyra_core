"""
ZYRA APP ENGINE
Motor que controla todas las apps del sistema
"""

from apps.bootstrap_apps import get_registry


class AppEngine:

    def __init__(self):

        self.apps = get_registry()

    def list_apps(self):

        return list(self.apps.keys())

    def get_app(self, name):

        return self.apps.get(name)

    def app_exists(self, name):

        return name in self.apps


# instancia global
app_engine = AppEngine()
