"""
ZYRA CORE
SUPERVISOR ENGINE

Motor de supervisión del sistema.
Monitorea apps, engines y estado general.
"""

from engines.app_engine.app_engine import app_engine


class SupervisorEngine:

    def __init__(self):

        self.apps = []
        self.status = "INIT"

    def system_health(self):

        self.apps = app_engine.list_apps()

        return {
            "status": "OK",
            "apps_detected": self.apps,
            "total_apps": len(self.apps)
        }

    def check_app(self, name):

        exists = app_engine.app_exists(name)

        return {
            "app": name,
            "exists": exists
        }


supervisor_engine = SupervisorEngine()
