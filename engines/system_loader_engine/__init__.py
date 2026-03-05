"""
ZYRA CORE
SYSTEM LOADER ENGINE

Motor que arranca el sistema completo.
Carga engines, apps y estado base.
"""

from engines.app_engine.app_engine import app_engine
from foundation.system_core.module_config import SYSTEM_NAME


class SystemLoaderEngine:

    def __init__(self):

        self.system_name = SYSTEM_NAME
        self.apps_loaded = []

    def boot(self):

        print(f"Booting {self.system_name}...")

        apps = app_engine.list_apps()

        for app in apps:
            self.apps_loaded.append(app)

        print("Apps cargadas:")
        print(self.apps_loaded)

        return {
            "system": self.system_name,
            "apps_loaded": self.apps_loaded
        }


system_loader = SystemLoaderEngine()
