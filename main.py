"""
ZYRA CORE
Sistema Soberano Base
Entry Point Oficial API
"""

import os
import sys
import traceback
from fastapi import FastAPI

# FIX IMPORT PATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

app = FastAPI(title="ZYRA CORE")


# ===============================
# ROOT
# ===============================

@app.get("/")
def root():
    return {
        "system": "ZYRA CORE",
        "status": "running"
    }


# ===============================
# HEALTH
# ===============================

@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# ===============================
# DIAGNOSTIC
# ===============================

@app.get("/diagnostic")
def diagnostic():

    report = {
        "foundation": False,
        "engines": False,
        "protocol": False,
        "apps": False,
        "errors": []
    }

    # FOUNDATION
    try:
        import foundation
        report["foundation"] = True
    except Exception as e:
        report["errors"].append(f"foundation: {str(e)}")

    # ENGINES
    try:
        import engines
        report["engines"] = True
    except Exception as e:
        report["errors"].append(f"engines: {str(e)}")

    # PROTOCOL
    try:
        import protocol
        report["protocol"] = True
    except Exception as e:
        report["errors"].append(f"protocol: {str(e)}")

    # APPS
    try:
        import apps
        report["apps"] = True
    except Exception as e:
        report["errors"].append(f"apps: {str(e)}")

    return report


# ===============================
# GLOBAL ERROR HANDLER
# ===============================

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return {
        "error": str(exc),
        "trace": traceback.format_exc()
    }
