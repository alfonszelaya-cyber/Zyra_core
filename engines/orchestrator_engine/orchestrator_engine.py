"""
ZYRA CORE
ORCHESTRATOR ENGINE

Coordina todos los motores del sistema.
Arranca loader, supervisor y apps.
"""

from engines.system_loader_engine.system_loader_engine import system_loader
from engines.supervisor_engine.supervisor_engine import supervisor_engine


class OrchestratorEngine:

    def __init__(self):

        self.system_state = "INIT"

    def start_system(self):

        boot_info = system_loader.boot()

        health = supervisor_engine.system_health()

        self.system_state = "RUNNING"

        return {
            "system_state": self.system_state,
            "boot": boot_info,
            "health": health
        }


orchestrator_engine = OrchestratorEngine()
