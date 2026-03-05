"""
ZYRA CORE
Sistema Soberano Base
ENTRY POINT OFICIAL API
BOOT + SCAN DEL SISTEMA
"""

import os
import sys
import traceback
import importlib
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# ===============================
# FIX IMPORT PATH
# ===============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# ===============================
# FASTAPI
# ===============================

app = FastAPI(title="ZYRA CORE")

# ===============================
# SYSTEM BOOT
# ===============================

SYSTEM_STATUS = {"boot": "NOT_STARTED"}

try:

    from foundation.system_core.root_controller import boot_system

    boot_result = boot_system()

    SYSTEM_STATUS["boot"] = "OK"
    SYSTEM_STATUS["result"] = boot_result

except Exception as e:

    SYSTEM_STATUS["boot"] = "FAILED"
    SYSTEM_STATUS["error"] = str(e)

# ===============================
# ROOT
# ===============================

@app.get("/")
def root():
    return {
        "system": "ZYRA CORE",
        "status": SYSTEM_STATUS
    }

# ===============================
# HEALTH
# ===============================

@app.get("/health")
def health():
    return {
        "status": "ok",
        "system_boot": SYSTEM_STATUS
    }

# ===============================
# FULL SYSTEM SCAN
# ===============================

@app.get("/scan")
def full_system_scan():

    report = {
        "total_files": 0,
        "imported_ok": [],
        "failed": []
    }

    for root_dir, dirs, files in os.walk(BASE_DIR):

        if any(skip in root_dir for skip in ["__pycache__", ".venv", "venv", ".git"]):
            continue

        for file in files:

            if file.endswith(".py") and file != "main.py":

                full_path = os.path.join(root_dir, file)

                module_path = os.path.relpath(full_path, BASE_DIR)
                module_path = module_path.replace(os.sep, ".")
                module_path = module_path.replace(".py", "")

                report["total_files"] += 1

                try:
                    importlib.import_module(module_path)
                    report["imported_ok"].append(module_path)

                except Exception as e:

                    report["failed"].append({
                        "module": module_path,
                        "error": str(e)
                    })

    report["errors_total"] = len(report["failed"])

    return report

# ===============================
# GLOBAL ERROR HANDLER
# ===============================

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):

    return JSONResponse(
        status_code=500,
        content={
            "error": str(exc),
            "trace": traceback.format_exc()
        }
    )
