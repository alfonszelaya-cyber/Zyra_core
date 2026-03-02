"""
ZYRA CORE
Sistema Soberano Base
Entry Point Oficial
"""

import sys
import traceback

# FOUNDATION
from foundation.system_core.bootstrap import SystemBootstrap
from foundation.system_core.health import SystemHealthCheck

# ENGINES
from engines.economic_engine.bootstrap import EconomicEngineBootstrap
from engines.logistics_engine.bootstrap import LogisticsEngineBootstrap
from engines.security_engine.bootstrap import SecurityEngineBootstrap

# PROTOCOL
from protocol.event_bus.core_event_bus import CoreEventBus
from protocol.universal_api_gateway.gateway import UniversalAPIGateway

# APPS (registro inicial)
from apps.nexo.bootstrap import NexoBootstrap


class ZyraCore:

    def __init__(self):
        self.event_bus = None
        self.api_gateway = None

    def start(self):
        try:
            print("\n🚀 Starting ZYRA CORE...\n")

            # 1️⃣ FOUNDATION
            SystemBootstrap.initialize()

            # 2️⃣ EVENT BUS
            self.event_bus = CoreEventBus()
            self.event_bus.initialize()

            # 3️⃣ ENGINES
            EconomicEngineBootstrap.initialize(self.event_bus)
            LogisticsEngineBootstrap.initialize(self.event_bus)
            SecurityEngineBootstrap.initialize(self.event_bus)

            # 4️⃣ PROTOCOL
            self.api_gateway = UniversalAPIGateway(self.event_bus)
            self.api_gateway.initialize()

            # 5️⃣ APPS
            NexoBootstrap.initialize(self.event_bus)

            # 6️⃣ HEALTH CHECK
            SystemHealthCheck.run()

            print("\n✅ ZYRA CORE INITIALIZED SUCCESSFULLY\n")

        except Exception as e:
            print("\n❌ ZYRA CORE FAILED TO START")
            print(str(e))
            traceback.print_exc()
            sys.exit(1)


if __name__ == "__main__":
    zyra = ZyraCore()
    zyra.start()
