from fastapi import FastAPI
import traceback

app = FastAPI(title="ZYRA CORE")

@app.get("/")
def root():
    return {
        "system": "ZYRA CORE",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.get("/diagnostic")
def diagnostic():
    report = {
        "foundation": False,
        "engines": False,
        "protocol": False,
        "apps": False,
        "errors": []
    }

    try:
        from foundation.system_core.bootstrap import SystemBootstrap
        report["foundation"] = True
    except Exception as e:
        report["errors"].append(str(e))

    try:
        from engines.economic_engine.bootstrap import EconomicEngineBootstrap
        report["engines"] = True
    except Exception as e:
        report["errors"].append(str(e))

    try:
        from protocol.event_bus.core_event_bus import CoreEventBus
        report["protocol"] = True
    except Exception as e:
        report["errors"].append(str(e))

    try:
        from apps.nexo.bootstrap import NexoBootstrap
        report["apps"] = True
    except Exception as e:
        report["errors"].append(str(e))

    return report
