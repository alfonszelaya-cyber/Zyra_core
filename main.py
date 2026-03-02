"""
ZYRA CORE
Sistema Soberano Base
Entry Point Oficial API
ESCANEO COMPLETO REAL
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
    return {"status": "ok"}


# ===============================
# FULL SYSTEM SCAN
# ===============================

@app.get("/scan")
def full_system_scan():

    report = {
        "total_files": 0,
        "imported_ok": [],
        "failed": [],
    }

    for root_dir, dirs, files in os.walk(BASE_DIR):

        # evitar carpetas irrelevantes
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
