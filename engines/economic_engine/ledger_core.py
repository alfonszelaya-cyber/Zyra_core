# ledger_core.py
# ZYRA CORE LEDGER

import os
import json

from foundation.system_core.module_config import LEDGER_FILE, DATA_DIR
from infrastructure.monitoring_adapters.logging.zyra_logs_hook import log

os.makedirs(DATA_DIR, exist_ok=True)


def _load_ledger():

    if not os.path.exists(LEDGER_FILE):
        return []

    try:
        with open(LEDGER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []


def _save_ledger(entries):

    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)


def add_entry(entry: dict):

    ledger = _load_ledger()

    ledger.append(entry)

    _save_ledger(ledger)

    log(
        "INFO",
        f"Entrada agregada al ledger: {entry.get('id', 'sin_id')}",
        "LEDGER"
    )


def get_all_entries():
    return _load_ledger()
